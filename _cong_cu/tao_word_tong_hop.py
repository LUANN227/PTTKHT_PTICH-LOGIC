"""Ghép báo cáo Phần I và Phần II đến hết II.3 từ các bài đã sửa.

- Phần I: bản Phần I đã sửa (giữ nguyên định dạng gốc, dùng làm khuôn style).
- II.1: UCD tổng quát, phân cấp chức năng, bảng chức năng con (catalogue.json).
- II.2: theo mẫu MAU_FDS_SUMMARY_VA_UC_DESCRIPTION. Mỗi vùng có UCD vùng, rồi từng UC theo thứ tự mã.
  UC ngoài trọng tâm: bảng FDS Summary (fds.json). UC trọng tâm: bảng UC Description 10 thành phần,
  nội dung lấy từ bốn bảng mục 3 của bài thành viên đã sửa (thông tin chung, luồng chính, luồng thay
  thế/ngoại lệ, quy tắc), chỉ đổi cách trình bày; kèm Activity Diagram. V10 lấy FDS chi tiết trong fds.json.
- II.3: tổng quan gói, năm hình cụm lớp, bảng danh mục lớp.
- II.4: chỉ đề mục cho sơ đồ hành vi của UC trọng tâm.

    python3 _cong_cu/tao_word_tong_hop.py [file .docx ra]

Mặc định ghi vào 05_TONG_HOP_CUOI/PTTKHTTT_PHAN_I_II3_TONG_HOP.docx.
"""
import copy
import importlib.util
import json
import os
import re
import sys
import tempfile

from docx import Document
from docx.enum.text import WD_BREAK
from docx.oxml.ns import qn
from docxcompose.composer import Composer

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DATA = os.path.join(HERE, "du_lieu")
P1_DIR = os.path.join(REPO, "01_MUC_I", "da_sua")
MEMBER_DIR = os.path.join(REPO, "02_MUC_II_BAI_THANH_VIEN", "da_sua")
DRAWIO = os.path.join(REPO, "04_DRAWIO")
OUT = os.path.join(REPO, "05_TONG_HOP_CUOI", "PTTKHTTT_PHAN_I_II3_TONG_HOP.docx")


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


W = load("w", os.path.join(HERE, "word_chung.py"))
G3 = load("g3", os.path.join(HERE, "gen_ii3_drawio.py"))
Q = load("q", os.path.join(HERE, "quyet_dinh.py"))
QD07 = Q.QD07_CT
W.MEANING["YeuCauNguonLuc"] = "Yêu cầu nguồn lực PM gửi cho V5 kèm khung thời gian (CN-127)"

P1 = "[PTTKHT] I - PHÂN TÍCH YÊU CẦU FINAL (đã sửa).docx"
# UC trọng tâm -> (bài đã sửa, tiêu đề mục); bài V2b gồm cả 01.2 và 01.3.
MEMBER = {
    "UC-01.1": ("V2-Phần II (đã sửa).docx", "V2a – Nguyễn Thị Thùy Linh"),
    "UC-01.2": ("V2-Phần II (2) - ban 22-10 (đã sửa).docx", "V2b – Nguyễn Tuấn Long"),
    "UC-02.1": ("V3- Phần 2 (đã sửa).docx", "V3 – Lê Hoài Linh"),
    "UC-03.3": ("V4 - Phần II (đã sửa).docx", "V4 – Nguyễn Hoàng Linh"),
    "UC-04.1": ("NV05 I2 - I3 (đã sửa).docx", "V5 – Nguyễn Hoàng Khánh Linh"),
    "UC-05.1": ("V6 - Phần II (đã sửa).docx", "V6 – Nguyễn Thi Thùy Linh"),
    "UC-06.2": ("MNV7_II_Thiết kế Logic (đã sửa).docx", "V7 – Lưu Thùy Linh"),
    "UC-07.1": ("MNV8 - Ngọc Linh (đã sửa).docx", "V8 – Ngọc Linh"),
    "UC-08.1": ("V9 - Phần II (đã sửa).docx", "V9 – Ngô Nhật Long"),
}
COVERED = {"UC-01.3": "UC-01.2"}


def text(el):
    return "".join(t.text or "" for t in el.iter(qn("w:t"))).strip()


def blank(template):
    """Tài liệu rỗng mang style của Phần I."""
    d = Document(template)
    body = d.element.body
    for el in list(body):
        if el.tag != qn("w:sectPr"):
            body.remove(el)
    return d


def cells(row):
    out, seen = [], set()
    for c in row.cells:
        if id(c._tc) in seen:
            continue
        seen.add(id(c._tc))
        out.append(c.text.strip())
    return out


def step_ref(x):
    x = re.sub(r"^[Bb]ước\s*", "", x.strip())
    return x


def member_rows(path, uc, cn):
    """Bảng UC Description theo mẫu, dựng từ bốn bảng mục 3 của bài thành viên (giữ nguyên câu chữ)."""
    d = Document(path)
    ts = d.tables
    i = next(k for k, t in enumerate(ts) if len(t.rows) > 5 and cells(t.rows[0])[0] == "Trường"
             and cells(t.rows[1])[1] == uc)
    info = {}
    for r in ts[i].rows[1:]:
        k, v = cells(r)[:2]
        info.setdefault(k, v)
    post = [(k, v) for k, v in ((cells(r)[0], cells(r)[1]) for r in ts[i].rows[1:]) if k.startswith("Hậu điều kiện")]
    main, alt, br = ts[i + 1], ts[i + 2], ts[i + 3]
    actor = info.get("Actor chính", "")
    side = info.get("Actor phụ", "")
    tac = actor + ("" if not side or side.lower().startswith("không") else f" (chính); {side} (phụ)")

    def who(x):
        x = x.replace("System", "Hệ thống").replace("Actor/ System", "").strip()
        return actor.split(" (")[0] if x == "Actor" else x
    hm = cells(main.rows[0])
    steps = []
    for r in main.rows[1:]:
        c = cells(r)
        w, desc = who(c[1]), c[2]
        if desc.startswith(w + " "):
            desc = desc[len(w) + 1:]
            desc = desc[:1].upper() + desc[1:]
        line = f"{c[0]} — {w}: {desc}"
        if len(c) > 3 and c[3] and "Căn" in hm[3]:
            line += f" ({c[3]})"
        steps.append(line)
    ha = cells(alt.rows[0])
    col = {h: j for j, h in enumerate(ha)}
    flows = {"A": [], "E": []}
    for r in alt.rows[1:]:
        c = cells(r)
        code = c[col["Mã"]]
        line = (f"{code} — tại bước {step_ref(c[col['Tại bước']])}: {c[col['Điều kiện']].rstrip('.')} → "
                f"{c[col['Xử lý']]}")
        if "Căn cứ" in col and c[col["Căn cứ"]]:
            line += f" ({c[col['Căn cứ']]})"
        flows["E" if code.startswith("E") else "A"].append(line)
    rules = []
    for r in br.rows[1:]:
        c = cells(r)
        rules.append(f"{c[0]}: {c[1]}" + (f" ({c[2]})" if len(c) > 2 and c[2] else ""))
    rules.append(f"Truy vết: I FINAL CN-{cn}")
    pre = info.get("Tiền điều kiện", "")
    if info.get("Trigger"):
        pre = f"Sự kiện kích hoạt: {info['Trigger']}\n{pre}"
    if len(post) > 1:
        hau = "\n".join(f"{re.sub(r'^Hậu điều kiện \((.*)\)$', r'\1', k).capitalize()}: {v}" for k, v in post)
    else:
        hau = post[0][1]
    return [("Tên ca sử dụng", info.get("Tên UC", "")), ("ID", uc), ("Tác nhân liên quan", tac),
            ("Mục tiêu", info.get("Mục tiêu", "")), ("Tiền điều kiện", pre), ("Luồng chính", "\n".join(steps)),
            ("Hậu điều kiện", hau), ("Luồng phụ", "\n".join(flows["A"]) or "Không có."),
            ("Luồng ngoại lệ", "\n".join(flows["E"]) or "Không có."),
            ("Ràng buộc nghiệp vụ (quy tắc nghiệp vụ)", "\n".join(rules))]




def fds_rows(uc, rows):
    """FDS Summary theo fds.json; bỏ mã quyết định nội bộ (Dxx) và áp QĐ-07 đã chốt cho UC-08.2."""
    out = []
    for k, v in rows[1:]:
        v = re.sub(r"; D\d\d(–D\d\d)?:", ":", v)
        v = re.sub(r"^([AE]\d+) tại bước", r"\1 — tại bước", v, flags=re.M)
        if uc == "UC-08.2":
            if k == "Luồng chính":
                v = v.replace("theo công thức chung.", "theo công thức ở QT-51.")
            elif k == "Luồng ngoại lệ":
                v = ("E1 — tại bước 2: Thiếu số liệu → yêu cầu Tài chính xác nhận căn cứ; chưa kết luận trạng thái "
                     "ngân sách.\nE2 — tại bước 2: Ngân sách còn lại ≤ 0 mà vẫn phát sinh chi phí → coi là vượt trên "
                     "10%, chuyển cấp CEO/Managing Director tại UC-08.4.")
            elif k.startswith("Ràng buộc"):
                v = ("QT-47, QT-51; CN-108–109: so cùng thời điểm, cùng phạm vi. " + QD07 +
                     "\nTruy vết: I FINAL CN-108–109")
        out.append((k, v))
    return out


def v10_rows(spec, fds_r):
    """UC Description V10 theo bản chi tiết (v10.json); bỏ các câu còn treo Q-08, Q-09 vì QĐ-08, QĐ-09 đã chốt."""
    def clean(t):
        return re.sub(r"\s*[^.]*\bQ-0\d[^.]*\.", "", t).strip()
    steps = "\n".join(f"{n} — {who}: {clean(d)}" for n, who, d in spec["steps"])
    flows = {"A": [], "E": []}
    for code, st, cond, act in spec["alternatives"]:
        flows[code[0]].append(f"{code} — tại bước {st}: {cond.rstrip('.')} → {clean(act)}")
    rule = dict(fds_r)["Ràng buộc nghiệp vụ (quy tắc nghiệp vụ)"]
    trig = spec["trigger"].replace(" Không chạy một lần liên tục đến tuần kế tiếp trong AD.", "")
    return [("Tên ca sử dụng", spec["name"]), ("ID", spec["id"]),
            ("Tác nhân liên quan", f"{spec['actor']} (chính); {spec['secondary']} (phụ)"),
            ("Mục tiêu", spec["goal"]), ("Tiền điều kiện", f"Sự kiện kích hoạt: {trig}\n{spec['pre']}"),
            ("Luồng chính", steps), ("Hậu điều kiện", spec["post"]),
            ("Luồng phụ", "\n".join(sorted(flows["A"])) or "Không có."),
            ("Luồng ngoại lệ", "\n".join(sorted(flows["E"])) or "Không có."),
            ("Ràng buộc nghiệp vụ (quy tắc nghiệp vụ)", rule)]


def fig(doc, path, cap, width=15, max_h=21):
    from docx.shared import Cm
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from PIL import Image
    w, h = Image.open(path).size
    if width * h / w > max_h:
        doc.add_picture(path, height=Cm(max_h))
    else:
        doc.add_picture(path, width=Cm(width))
    doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.paragraphs[-1].paragraph_format.keep_with_next = True
    W.caption(doc, cap)


OWNER = W.OWNER
# II.4: chỉ UC trọng tâm. (UC, lớp II.3 tham gia)
II4 = [
    ("II.4.1. Sơ đồ trạng thái", "đối tượng có vòng đời phức tạp", [
        ("NhuCauNguonLuc", ["UC-01.1", "UC-01.2", "UC-01.3"]),
        ("PhuongAnBoTri", ["UC-05.1"]),
        ("DiemXungDot", ["UC-06.2"]),
        ("HoSoTrinhDuyet", ["UC-07.1"]),
    ]),
    ("II.4.2. Sơ đồ giao tiếp", "sự kiện truy vấn dữ liệu", [
        ("UC-03.3", "NhuCauNguonLuc, NguonLuc, HoSoNangLuc, BoTieuChiPhuHop, TieuChiPhuHop, KetQuaDanhGiaPhuHop, "
                    "DiemTieuChi, DeNghiMienTru"),
        ("UC-07.1", "HoSoTrinhDuyet, PhuongAnBoTri, ChiTietBoTri, DanhGiaChiPhi, KetQuaDuBao"),
        ("UC-09.1", "TongHopNguonCung, NguonLuc, LichNguonLuc, PhanBoNguonLuc, NhuCauNguonLuc, KetQuaDuBao"),
    ]),
    ("II.4.3. Sơ đồ tuần tự", "sự kiện thay đổi dữ liệu", [
        ("UC-01.1", "DuAn, GiaiDoanDuAn, NhuCauNguonLuc, ViTriCanBoTri, YeuCauKyNang"),
        ("UC-01.2", "NhuCauNguonLuc, PhanHoiNhuCau"),
        ("UC-02.1", "KyNang, BoTieuChiNangLuc, TieuChiNangLuc, MucDoNangLuc"),
        ("UC-04.1", "YeuCauNguonLuc, NguonLuc, HoSoNangLuc, LichNguonLuc, PhanBoNguonLuc, KetLuanKhaNangThamGia"),
        ("UC-05.1", "NhuCauNguonLuc, KetLuanKhaNangThamGia, PhuongAnBoTri, ChiTietBoTri, RuiRoViTri"),
        ("UC-06.2", "DiemXungDot, PhuongAnBoTri, ChiTietBoTri, NhatKyXuLyXungDot, DeXuatThayDoi"),
        ("UC-08.1", "PhuongAnBoTri, ChiTietBoTri, DonGia, DuToanChiPhi, DuBaoChiPhi, ChiPhiThucTe"),
        ("UC-09.2", "NhuCauDuBao, TongHopNguonCung, KetQuaDuBao, DongDoiChieuCungCau"),
    ]),
]


def build(out):
    src = MEMBER_DIR
    p1 = os.path.join(P1_DIR, P1)
    dr = DRAWIO
    cat = json.load(open(os.path.join(DATA, "catalogue.json"), encoding="utf-8"))
    fds = json.load(open(os.path.join(DATA, "fds.json"), encoding="utf-8"))
    v10 = json.load(open(os.path.join(DATA, "v10.json"), encoding="utf-8"))
    tmp = tempfile.mkdtemp()
    parts = []          # (loại, đường dẫn) theo thứ tự ghép
    cur = [None]

    def chunk():
        if cur[0] is None:
            cur[0] = blank(p1)
        return cur[0]

    def flush():
        if cur[0] is not None:
            path = os.path.join(tmp, f"chunk_{len(parts):02d}.docx")
            cur[0].save(path)
            parts.append(path)
            cur[0] = None

    doc = chunk()
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
    doc.add_heading("II — PHÂN TÍCH (THIẾT KẾ LOGIC)", level=1)

    # ---------------- II.1
    doc.add_heading("II.1 — PHẠM VI HỆ THỐNG CÔNG NGHỆ", level=2)
    W.para(doc, "Hệ thống quản lý và điều phối nguồn lực dự án của Lạc Việt Consulting hỗ trợ toàn bộ quá trình "
                "từ xác định nhu cầu nguồn lực đến theo dõi và dự báo cung – cầu. Phạm vi gồm 9 chức năng cấp vùng "
                f"(UC-01 đến UC-09), tương ứng các vùng nghiệp vụ V2–V10 của Phần I, và {len(cat['ucs'])} chức "
                "năng con. Tác nhân gồm PM, RM, Nguồn lực, Tài chính, PMO/Quản lý danh mục và CEO/Managing "
                "Director.")
    W.figure(doc, os.path.join(dr, "II.1", "II1_UC_Tong_Quat.png"), "Hình II.1-1. Sơ đồ ca sử dụng tổng quát.",
             width=14)
    W.figure(doc, os.path.join(dr, "II.1", "Phan_cap_chuc_nang.png"), "Hình II.1-2. Sơ đồ phân cấp chức năng.",
             width=16)
    W.para(doc, f"Bảng II.1-1 liệt kê {len(cat['ucs'])} chức năng con. 12 ca sử dụng trọng tâm được đặc tả đầy đủ "
                "kèm sơ đồ hoạt động; các ca sử dụng còn lại được mô tả bằng FDS tóm tắt.")
    W.caption(doc, "Bảng II.1-1. Danh sách chức năng con.", before=True)
    W.table(doc, ["Vùng", "Mã", "Chức năng", "Tác nhân", "Chức năng Phần I", "Mức đặc tả"],
            [(u["region"], u["id"], u["name"], u["actor"].replace(";", ","), "CN-" + u["cn"],
              "Đặc tả đầy đủ, AD" if u["id"] in W.FOCUS else "FDS tóm tắt") for u in cat["ucs"]],
            widths=[1.3, 1.9, 5, 2.6, 3, 2.2], size=10)

    # ---------------- II.2
    ucs = {u["id"]: u for u in cat["ucs"]}
    doc.add_heading("II.2 — MÔ HÌNH HÓA CHỨC NĂNG CỦA HỆ THỐNG CÔNG NGHỆ", level=2)
    W.para(doc, "Mỗi vùng trình bày sơ đồ ca sử dụng của vùng, sau đó từng ca sử dụng theo thứ tự mã. Ca sử dụng "
                "trọng tâm được đặc tả ở mức cụ thể (UC Description) kèm sơ đồ hoạt động; các ca sử dụng còn lại "
                "được đặc tả ở mức khái quát (FDS Summary). Hai mức dùng cùng các thành phần. Luồng chính đánh số "
                "theo bước, ghi người thực hiện; luồng phụ đánh A1, A2; luồng ngoại lệ đánh E1, E2.")
    fno = 0
    for k, (code, vname, v, subs) in enumerate(cat["regions"], 1):
        doc = chunk()
        doc.add_heading(f"II.2.{k}. {v} — {vname} ({code})", level=3)
        fno += 1
        fig(doc, os.path.join(dr, "II.2_UCD_vung", f"UCD_{code}.png"),
            f"Hình II.2-{fno}. Sơ đồ ca sử dụng {code} {vname}.", width=15, max_h=20)
        for cid, cname in subs:
            if cid in W.FOCUS:
                doc.add_heading(f"{cid} {cname} (ca sử dụng trọng tâm)", level=4)
                fname = MEMBER.get(cid, MEMBER.get(COVERED.get(cid, ""), (None,)))[0]
                if fname:
                    rows = member_rows(os.path.join(src, fname), cid, ucs[cid]["cn"])
                else:
                    spec = next(x for x in v10["specs"] if x["id"] == cid)
                    rows = v10_rows(spec, fds_rows(cid, fds[cid]))
                W.kv_table(doc, rows)
                W.para(doc, f"Activity Diagram {cid}", bold=True)
                fno += 1
                fig(doc, os.path.join(dr, "II.2_AD", f"AD_{cid}.png"),
                    f"Hình II.2-{fno}. Activity Diagram {cid} {cname}.")
            else:
                doc.add_heading(f"{cid} {cname}", level=4)
                W.kv_table(doc, fds_rows(cid, fds[cid]))

    # ---------------- II.3
    doc = chunk()
    doc.add_heading("II.3 — MÔ HÌNH HÓA CẤU TRÚC TĨNH CỦA HỆ THỐNG CÔNG NGHỆ", level=2)
    n = sum(len(c[4]) for c in G3.CLUSTERS)
    W.para(doc, f"Sơ đồ lớp miền nghiệp vụ gồm {n} lớp, chia thành năm gói theo nhóm vùng. Hình II.3-1 cho thấy các "
                "gói và quan hệ phụ thuộc giữa chúng. Hình II.3-2 đến II.3-6 trình bày từng gói với thuộc tính, liên "
                "kết và bội số. Lớp thuộc gói khác được vẽ nền xám, viền nét đứt, chỉ để thể hiện liên kết; thuộc "
                "tính của lớp đó xem ở hình của gói sở hữu. Bảng lớp, thuộc tính và bội số trong phần đề xuất lớp "
                "(II.2+) của từng thành viên đã được sửa cho khớp các hình này.")
    files = ["II3-1_Tong_quan_goi_lop", "II3-2_Nhu_cau_va_nang_luc", "II3-3_Tim_kiem_kha_nang_tham_gia_lich",
             "II3-4_Phuong_an_xung_dot_phe_duyet", "II3-5_Chi_phi_ngan_sach", "II3-6_Theo_doi_du_bao"]
    W.figure(doc, os.path.join(dr, "II.3", files[0] + ".png"), "Hình II.3-1. Tổng quan các gói lớp miền nghiệp vụ.",
             width=15)
    for k, ((key, fno, title, vung, _), f) in enumerate(zip(G3.CLUSTERS, files[1:]), 1):
        doc.add_heading(f"II.3.{k}. Gói {key}: {title} ({vung})", level=3)
        W.figure(doc, os.path.join(dr, "II.3", f + ".png"), f"Hình {fno}. Sơ đồ lớp miền: {title.lower()}.",
                 width=16)
    doc.add_heading("II.3.6. Danh mục lớp", level=3)
    W.caption(doc, "Bảng II.3-1. Danh mục lớp miền nghiệp vụ.", before=True)
    rows = []
    for key, fno, _, vung, cs in G3.CLUSTERS:
        for c in cs:
            rows.append((c, W.MEANING[c], ", ".join(G3.CLASSES[c]), fno))
    W.table(doc, ["Lớp", "Ý nghĩa", "Thuộc tính", "Hình"], rows, widths=[4.4, 4.6, 5.4, 1.6], size=10)
    W.para(doc, "Bảng II.3-2 ghi miền giá trị của các thuộc tính trạng thái. Tên trạng thái lấy theo các bước và điểm "
                "quyết định của Phần I; sơ đồ trạng thái ở II.4.1 dùng đúng các giá trị này. Đơn giá (DonGia) tính "
                "bằng VNĐ/ngày công theo vai trò; mức tham gia (tyLeThamGia, tyLeFTE) tính bằng %FTE.")
    W.caption(doc, "Bảng II.3-2. Miền giá trị thuộc tính trạng thái.", before=True)
    W.table(doc, ["Lớp", "Thuộc tính", "Giá trị", "Căn cứ"],
            [(c, a, ", ".join(v), b) for c, (a, v, _, b) in Q.TRANG_THAI.items()],
            widths=[3.4, 2.6, 6.4, 3.6], size=10)

    # ---------------- II.4 (đề mục)
    doc.add_heading("II.4 — MÔ HÌNH HÓA HÀNH VI CỦA HỆ THỐNG CÔNG NGHỆ", level=2)
    W.para(doc, "Chỉ vẽ cho các ca sử dụng trọng tâm đã đặc tả ở II.2, dùng tên lớp của II.3, để giữ mạch ca sử "
                "dụng → lớp → hành vi. Không chọn thêm ca sử dụng ngoài trọng tâm.")
    for h, kind, items in II4:
        doc.add_heading(f"{h} ({kind})", level=3)
        for n, it in enumerate(items, 1):
            sub = h.split(".")[2]
            if sub == "1":
                cls, uc_list = it
                attr, _, chain, base = Q.TRANG_THAI[cls]
                doc.add_heading(f"II.4.{sub}.{n}. Sơ đồ trạng thái lớp {cls}", level=4)
                who = "; ".join(dict.fromkeys(OWNER[u] for u in uc_list))
                W.para(doc, f"Theo {', '.join(uc_list)}; thuộc tính {attr}: {chain}. Căn cứ: {base}. "
                            f"Người thực hiện: {who}.", italic=True)
            else:
                uc, cls = it
                kind_name = "giao tiếp" if sub == "2" else "tuần tự"
                doc.add_heading(f"II.4.{sub}.{n}. Sơ đồ {kind_name} {uc} {ucs[uc]['name']}", level=4)
                W.para(doc, f"Lớp II.3: {cls}. Người thực hiện: {OWNER[uc]}.", italic=True)
    flush()

    base = Document(p1)
    comp = Composer(base)
    for p in parts:
        comp.append(Document(p))
    comp.save(out)


if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else OUT)
