"""Sửa trực tiếp bài Word gốc: thay chữ trong ô/đoạn mà giữ định dạng run đầu, thêm/xóa dòng,
thêm/xóa đoạn, thay ảnh. Mọi thao tác ghi vào nhật ký để đối chiếu với bản gốc.

Chỉ số đoạn (P) và bảng (T) là chỉ số cấp thân tài liệu, giống `doc.paragraphs`/`doc.tables`
của python-docx, tính trên bản gốc. Vì vậy thao tác xóa/thêm đoạn được gom lại và thực hiện
sau cùng (Sua.apply), để chỉ số không bị lệch giữa chừng.
"""
import copy
import os

from docx import Document
from docx.image.image import Image
from docx.oxml.ns import qn
from docx.shared import Cm, Emu


def _text(el):
    return "".join(t.text or "" for t in el.iter(qn("w:t")))


def _set_par_text(p, text):
    """Đặt chữ cho một đoạn, giữ định dạng của run đầu tiên. Dòng mới -> ngắt dòng."""
    runs = p.findall(qn("w:r"))
    keep = None
    for r in runs:
        if r.find(qn("w:t")) is not None:
            keep = r
            break
    if keep is None and runs:
        keep = runs[0]
    for child in list(p):
        if child.tag in (qn("w:r"), qn("w:hyperlink"), qn("w:ins"), qn("w:del")):
            if child is not keep:
                p.remove(child)
    if keep is None:
        keep = p.makeelement(qn("w:r"), {})
        p.append(keep)
    for child in list(keep):
        if child.tag != qn("w:rPr"):
            keep.remove(child)
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if i:
            keep.append(keep.makeelement(qn("w:br"), {}))
        t = keep.makeelement(qn("w:t"), {})
        t.text = line
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        keep.append(t)


def _set_cell_text(tc, text):
    """Đặt chữ cho ô. Mỗi dòng của text là một đoạn, dùng định dạng đoạn đầu của ô."""
    ps = tc.findall(qn("w:p"))
    first = ps[0]
    for p in ps[1:]:
        tc.remove(p)
    lines = text.split("\n")
    _set_par_text(first, lines[0])
    prev = first
    for line in lines[1:]:
        np_ = copy.deepcopy(first)
        _set_par_text(np_, line)
        prev.addnext(np_)
        prev = np_


class Sua:
    def __init__(self, path, name):
        self.doc = Document(path)
        self.name = name
        self.P = list(self.doc.paragraphs)
        self.T = list(self.doc.tables)
        self.log = []
        self._later = []

    # ------------------------------------------------------------ bảng
    def cell(self, t, r, c, text, why=""):
        tc = self.T[t].rows[r].cells[c]._tc
        before = " / ".join(_text(p) for p in tc.findall(qn("w:p")))
        _set_cell_text(tc, text)
        self.log.append((f"Bảng {t}, dòng {r}, cột {c}", before, text, why))

    def row(self, t, r, values, why=""):
        for c, v in enumerate(values):
            if v is not None:
                tc = self.T[t].rows[r].cells[c]._tc
                _set_cell_text(tc, v)
        self.log.append((f"Bảng {t}, dòng {r}", "", " | ".join(v or "(giữ)" for v in values), why))

    def add_row(self, t, after, values, why=""):
        tr = self.T[t].rows[after]._tr
        nr = copy.deepcopy(tr)
        tcs = nr.findall(qn("w:tc"))
        for tc, v in zip(tcs, values):
            _set_cell_text(tc, v)
        tr.addnext(nr)
        self.log.append((f"Bảng {t}, thêm sau dòng {after}", "", " | ".join(values), why))
        return nr

    def del_row(self, t, r, why=""):
        tr = self.T[t].rows[r]._tr
        before = " | ".join(_text(tc) for tc in tr.findall(qn("w:tc")))
        self._later.append(lambda: tr.getparent().remove(tr))
        self.log.append((f"Bảng {t}, xóa dòng {r}", before, "", why))

    def rename(self, tables, pairs, why=""):
        """Đổi tên (theo ranh giới từ) trong mọi ô của các bảng; giữ định dạng run."""
        import re
        n = 0
        for t in tables:
            for tt in self.T[t]._tbl.iter(qn("w:t")):
                txt = tt.text or ""
                for old, new in pairs:
                    txt2 = re.sub(r"\b%s\b" % re.escape(old), new, txt)
                    if txt2 != txt:
                        n += 1
                        txt = txt2
                tt.text = txt
        self.log.append((f"Bảng {', '.join(map(str, tables))}", ", ".join(o for o, _ in pairs),
                         ", ".join(n_ for _, n_ in pairs), f"{why} ({n} chỗ)"))

    # ------------------------------------------------------------ đoạn
    def par(self, i, text, why=""):
        p = self.P[i]._p
        before = _text(p)
        _set_par_text(p, text)
        self.log.append((f"Đoạn {i}", before, text, why))

    def replace(self, i, old, new, why=""):
        """Thay một cụm trong đoạn i; nếu cụm nằm gọn trong một run thì giữ định dạng từng run."""
        p = self.P[i]._p
        before = _text(p)
        assert old in before, (self.name, i, old)
        done = False
        for t in p.iter(qn("w:t")):
            if t.text and old in t.text:
                t.text = t.text.replace(old, new)
                done = True
                break
        if not done:
            _set_par_text(p, before.replace(old, new))
        self.log.append((f"Đoạn {i}", old, new, why))

    def cell_replace(self, t, r, c, old, new, why=""):
        tc = self.T[t].rows[r].cells[c]._tc
        full = " / ".join(_text(p) for p in tc.findall(qn("w:p")))
        assert old in "".join(_text(p) for p in tc.findall(qn("w:p"))) or old in full, (self.name, t, r, c, old)
        done = False
        for p in tc.findall(qn("w:p")):
            for tt in p.iter(qn("w:t")):
                if tt.text and old in tt.text:
                    tt.text = tt.text.replace(old, new)
                    done = True
                    break
            if done:
                break
        if not done:
            for p in tc.findall(qn("w:p")):
                pt = _text(p)
                if old in pt:
                    _set_par_text(p, pt.replace(old, new))
                    done = True
                    break
        assert done, (self.name, t, r, c, old)
        self.log.append((f"Bảng {t}, dòng {r}, cột {c}", old, new, why))

    def add_par(self, i, texts, why="", like=None):
        """Chèn các đoạn mới ngay sau đoạn i, định dạng theo đoạn `like` (mặc định đoạn i)."""
        base = self.P[like if like is not None else i]._p
        anchor = self.P[i]._p
        if isinstance(texts, str):
            texts = [texts]
        for tx in texts:
            np_ = copy.deepcopy(base)
            for b in list(np_.iter(qn("w:drawing"))):
                b.getparent().remove(b)
            _set_par_text(np_, tx)
            anchor.addnext(np_)
            anchor = np_
        self.log.append((f"Thêm sau đoạn {i}", "", "\n".join(texts), why))

    def del_par(self, i, why=""):
        p = self.P[i]._p
        before = _text(p)
        self._later.append(lambda: p.getparent().remove(p))
        self.log.append((f"Xóa đoạn {i}", before, "", why))

    def del_table(self, t, why=""):
        tbl = self.T[t]._tbl
        self._later.append(lambda: tbl.getparent().remove(tbl))
        self.log.append((f"Xóa bảng {t}", "", "", why))

    # ------------------------------------------------------------ ảnh
    def image(self, i, png, width_cm=None, why=""):
        """Thay ảnh trong đoạn i bằng png; giữ vị trí, đổi kích thước theo tỷ lệ ảnh mới."""
        p = self.P[i]
        blips = list(p._p.iter(qn("a:blip")))
        assert blips, (self.name, i)
        blip = blips[0]
        part = p.part
        rid, _ = part.get_or_add_image(png)
        blip.set(qn("r:embed"), rid)
        img = Image.from_file(png)
        ext = next(p._p.iter(qn("wp:extent")))
        cx = int(ext.get("cx"))
        if width_cm:
            cx = Cm(width_cm)
        cy = int(cx * img.px_height / img.px_width)
        max_h = Cm(22)
        if cy > max_h:
            cx, cy = int(cx * max_h / cy), int(max_h)
        ext.set("cx", str(int(cx)))
        ext.set("cy", str(int(cy)))
        for e in p._p.iter(qn("a:ext")):
            e.set("cx", str(int(cx)))
            e.set("cy", str(int(cy)))
        self.log.append((f"Ảnh ở đoạn {i}", "", os.path.basename(png), why))

    def add_image(self, i, png, width_cm=16, why=""):
        """Chèn một đoạn ảnh (căn giữa) ngay sau đoạn i, dùng cho bài chưa có ảnh."""
        from docx.enum.text import WD_ALIGN_PARAGRAPH
        np_ = self.doc.add_paragraph()
        np_.alignment = WD_ALIGN_PARAGRAPH.CENTER
        img = Image.from_file(png)
        cx = Cm(width_cm)
        if cx * img.px_height / img.px_width > Cm(22):
            np_.add_run().add_picture(png, height=Cm(22))
        else:
            np_.add_run().add_picture(png, width=cx)
        self.P[i]._p.addnext(np_._p)
        self.log.append((f"Thêm ảnh sau đoạn {i}", "", os.path.basename(png), why))

    # ------------------------------------------------------------ kết thúc
    def apply(self, out):
        for f in self._later:
            f()
        self.doc.save(out)
        return self.log


def log_md(name, log):
    lines = [f"## {name}", "", "| Vị trí (theo bản gốc) | Trước | Sau | Lý do |", "|---|---|---|---|"]
    for loc, b, a, why in log:
        def esc(s):
            s = (s or "").replace("|", "\\|").replace("\n", "<br>")
            return s if len(s) < 400 else s[:400] + "…"
        lines.append(f"| {loc} | {esc(b)} | {esc(a)} | {esc(why)} |")
    return "\n".join(lines) + "\n"
