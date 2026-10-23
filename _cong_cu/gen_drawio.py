"""Sinh file .drawio (hình gốc của draw.io, sửa trực tiếp được) cho:
- II.1 sơ đồ ca sử dụng tổng quát,
- UCD cấp vùng UC-01..UC-09,
- sơ đồ phân rã chức năng dạng cũ (bản dùng trong báo cáo là Phan_cap_chuc_nang của gen_phan_cap.py).

Dữ liệu (mã, tên, actor, quan hệ) lấy từ HD-PCCN §1 và Phần I. Thường không chạy trực tiếp mà qua
gen_phan_cap.py, script này chép kết quả vào 04_DRAWIO.
Chạy riêng: python3 gen_drawio.py <thư mục ra>
"""
import html
import os
import sys

SYSTEM = "Hệ thống quản lý và điều phối nguồn lực dự án – Lạc Việt Consulting"

# HD-PCCN §1: mã và tên giữ nguyên.
VUNG = [
    ("UC-01", "Xác định nhu cầu nguồn lực", "V2", [
        ("UC-01.1", "Xây dựng và hoàn thiện nhu cầu"),
        ("UC-01.2", "Xác nhận nhu cầu"),
        ("UC-01.3", "Điều chỉnh nhu cầu theo phản hồi")]),
    ("UC-02", "Đánh giá năng lực nguồn lực", "V3", [
        ("UC-02.1", "Quản lý tiêu chí đánh giá năng lực"),
        ("UC-02.2", "Đánh giá năng lực nguồn lực"),
        ("UC-02.3", "Xác nhận và cập nhật hồ sơ năng lực")]),
    ("UC-03", "Tìm kiếm và đánh giá mức độ phù hợp", "V4", [
        ("UC-03.1", "Xác lập tiêu chí tìm kiếm và đánh giá"),
        ("UC-03.2", "Tìm kiếm ứng viên"),
        ("UC-03.3", "Đánh giá, xếp hạng và lập shortlist ứng viên"),
        ("UC-03.4", "Điều chỉnh kết quả đánh giá")]),
    ("UC-04", "Đánh giá khả năng tham gia", "V5", [
        ("UC-04.1", "Đánh giá khả năng tham gia"),
        ("UC-04.2", "Xử lý phương án tham gia một phần"),
        ("UC-04.3", "Xử lý trường hợp vượt tải ngoại lệ")]),
    ("UC-05", "Lập phương án bố trí nguồn lực", "V6", [
        ("UC-05.1", "Xây dựng phương án bố trí"),
        ("UC-05.2", "Rà soát phương án bố trí")]),
    ("UC-06", "Xử lý xung đột và cân đối nguồn lực", "V7", [
        ("UC-06.1", "Phân tích và đánh giá xung đột"),
        ("UC-06.2", "Cân đối nguồn lực"),
        ("UC-06.3", "Phân xử xung đột")]),
    ("UC-07", "Rà soát và phê duyệt phương án", "V8", [
        ("UC-07.1", "Rà soát và đánh giá phương án"),
        ("UC-07.2", "Yêu cầu giải trình và hoàn thiện phương án"),
        ("UC-07.3", "Phê duyệt phương án"),
        ("UC-07.4", "Phê duyệt ngoại lệ")]),
    ("UC-08", "Đánh giá tác động chi phí và ngân sách", "V9", [
        ("UC-08.1", "Tính và cập nhật chi phí phương án"),
        ("UC-08.2", "Đối chiếu chi phí và ngân sách"),
        ("UC-08.3", "So sánh đánh đổi giữa các phương án"),
        ("UC-08.4", "Xác định hướng xử lý và chuyển cấp ngân sách")]),
    ("UC-09", "Theo dõi và dự báo nguồn lực", "V10", [
        ("UC-09.1", "Tổng hợp và phân tích cung – cầu nguồn lực"),
        ("UC-09.2", "Dự báo cung – cầu nguồn lực")]),
]

ACTOR_NAME = {
    "PM": "PM", "RM": "RM", "NL": "Nguồn lực", "TC": "Tài chính",
    "PMO": "PMO/Quản lý danh mục", "CEO": "CEO/Managing Director",
}

# UCD cấp vùng: actor bên trái (chính), bên phải (phụ), association, quan hệ UC.
# Căn cứ CN của từng association: UCD_cap_vung_Bang_kiem.md.
UCD = {
    "UC-01": dict(left=["PM"], right=["RM"],
                  assoc={"UC-01.1": ["PM"], "UC-01.2": ["RM"], "UC-01.3": ["PM"]},
                  rel=[("UC-01.3", "UC-01.2", "extend")]),
    "UC-02": dict(left=["RM"], right=["NL", "PMO"],
                  assoc={"UC-02.1": ["RM", "PMO"], "UC-02.2": ["RM", "NL"],
                         "UC-02.3": ["RM", "PMO"]}, rel=[]),
    "UC-03": dict(left=["RM"], right=["PMO"],
                  assoc={"UC-03.1": ["RM"], "UC-03.2": ["RM"],
                         "UC-03.3": ["RM", "PMO"], "UC-03.4": ["RM", "PMO"]}, rel=[]),
    "UC-04": dict(left=["RM"], right=["PM", "PMO", "CEO"],
                  assoc={"UC-04.1": ["RM", "PM"], "UC-04.2": ["RM", "PM"],
                         "UC-04.3": ["RM", "PMO", "CEO"]}, rel=[]),
    "UC-05": dict(left=["RM"], right=["PM"],
                  assoc={"UC-05.1": ["RM"], "UC-05.2": ["PM", "RM"]}, rel=[]),
    "UC-06": dict(left=["RM", "PM"], right=["PMO", "CEO"],
                  assoc={"UC-06.1": ["RM", "PM"], "UC-06.2": ["RM", "PM"],
                         "UC-06.3": ["RM", "PMO", "CEO"]},
                  rel=[("UC-06.3", "UC-06.2", "extend")]),
    "UC-07": dict(left=["PMO"], right=["RM", "CEO"],
                  assoc={"UC-07.1": ["PMO", "CEO"], "UC-07.2": ["PMO", "RM"],
                         "UC-07.3": ["PMO", "CEO"], "UC-07.4": ["PMO", "CEO"]},
                  rel=[("UC-07.2", "UC-07.1", "extend")]),
    "UC-08": dict(left=["PM"], right=["TC", "PMO", "CEO"],
                  assoc={"UC-08.1": ["PM", "TC"], "UC-08.2": ["PM", "TC"],
                         "UC-08.3": ["PM"], "UC-08.4": ["PM", "PMO", "CEO"]}, rel=[]),
    "UC-09": dict(left=["RM"], right=["PM"],
                  assoc={"UC-09.1": ["RM", "PM"], "UC-09.2": ["RM"]},
                  rel=[("UC-09.1", "UC-09.2", "include")]),
}

# II.1: theo cột "Tham gia tại" của P1 I.1.2, cộng PMO–UC-03 (CN-37, CN-43; D-P3-01).
II1_LEFT = ["PM", "RM", "NL"]
II1_RIGHT = ["TC", "PMO", "CEO"]
II1_ASSOC = {
    "PM": ["UC-01", "UC-04", "UC-05", "UC-06", "UC-08", "UC-09"],
    "RM": ["UC-01", "UC-02", "UC-03", "UC-04", "UC-05", "UC-06", "UC-07", "UC-09"],
    "NL": ["UC-02"],
    "TC": ["UC-08"],
    "PMO": ["UC-02", "UC-03", "UC-04", "UC-06", "UC-07", "UC-08"],
    "CEO": ["UC-04", "UC-06", "UC-07", "UC-08"],
}

FONT = "fontFamily=Arial;"
S_ACTOR = ("shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;"
           "outlineConnect=0;" + FONT)
S_ACTOR_R = ("shape=umlActor;labelPosition=right;verticalLabelPosition=middle;align=left;"
             "verticalAlign=middle;html=1;outlineConnect=0;spacingLeft=4;" + FONT)
S_UC = "ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;" + FONT
S_BOUND = ("rounded=0;whiteSpace=wrap;html=1;fillColor=none;verticalAlign=top;"
           "fontStyle=1;strokeColor=#333333;" + FONT)
S_ASSOC = "endArrow=none;html=1;rounded=0;strokeColor=#333333;"
S_DEP = ("endArrow=open;endFill=0;dashed=1;html=1;rounded=0;strokeColor=#333333;"
         "fontSize=11;labelBackgroundColor=#FFFFFF;" + FONT)
S_TREE = ("edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;"
          "strokeColor=#333333;")


class Doc:
    def __init__(self, name):
        self.name = name
        self.cells = []
        self.n = 1

    def _id(self):
        self.n += 1
        return f"c{self.n}"

    def vertex(self, label, style, x, y, w, h):
        i = self._id()
        self.cells.append(
            f'<mxCell id="{i}" value="{html.escape(label, quote=True)}" style="{style}" '
            f'vertex="1" parent="1"><mxGeometry x="{x:.0f}" y="{y:.0f}" '
            f'width="{w:.0f}" height="{h:.0f}" as="geometry"/></mxCell>')
        return i

    def edge(self, src, dst, style, label="", points=()):
        i = self._id()
        pts = "".join(f'<mxPoint x="{x:.0f}" y="{y:.0f}"/>' for x, y in points)
        pts = f'<Array as="points">{pts}</Array>' if pts else ""
        self.cells.append(
            f'<mxCell id="{i}" value="{html.escape(label, quote=True)}" style="{style}" '
            f'edge="1" parent="1" source="{src}" target="{dst}">'
            f'<mxGeometry relative="1" as="geometry">{pts}</mxGeometry></mxCell>')
        return i

    def xml(self):
        body = "".join(self.cells)
        return (
            '<mxfile host="gen_drawio.py" type="device">'
            f'<diagram id="{self.name}" name="{html.escape(self.name)}">'
            '<mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" '
            'tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" '
            'pageWidth="1169" pageHeight="827" math="0" shadow="0"><root>'
            '<mxCell id="0"/><mxCell id="1" parent="0"/>'
            f'{body}</root></mxGraphModel></diagram></mxfile>\n')


def lbl(code, name):
    return f"{code}<br>{html.escape(name)}"


def place_actors(doc, keys, ys, x, used, gap=120, style=S_ACTOR):
    """Đặt actor theo trung bình y của các UC nối tới, tránh chồng nhau."""
    want = sorted(keys, key=lambda k: ys[k])
    pos, last = {}, -1e9
    for k in want:
        y = max(ys[k], last + gap)
        pos[k] = y
        last = y
    ids = {}
    for k in want:
        ids[k] = doc.vertex(ACTOR_NAME[k], style, x, pos[k] - 30, 30, 60)
    used.update(ids)
    return ids


def usecase_diagram(name, title, ucs, left, right, assoc, rel, uc_w=270, uc_h=72, gap=34,
                    actor_gap=120, actor_y=None):
    """ucs: list (code, label_html). assoc: code -> actors. rel: (src, dst, kind)."""
    doc = Doc(name)
    lw = 190 if any(len(ACTOR_NAME[a]) > 12 for a in left) else 120
    bx, by = lw + 60, 20
    top = by + 50
    uc_x = bx + 60
    uc_y = {}
    for i, (code, _) in enumerate(ucs):
        uc_y[code] = top + i * (uc_h + gap)
    bh = len(ucs) * (uc_h + gap) - gap + 80
    bw = uc_w + 120
    doc.vertex(title, S_BOUND, bx, by, bw, bh)
    uc_id = {}
    for code, label in ucs:
        uc_id[code] = doc.vertex(label, S_UC, uc_x, uc_y[code], uc_w, uc_h)
    ys = {}
    for a in left + right:
        cs = [c for c, acts in assoc.items() if a in acts]
        ys[a] = sum(uc_y[c] + uc_h / 2 for c in cs) / len(cs)
    for a, c in (actor_y or {}).items():
        ys[a] = uc_y[c] + uc_h / 2
    ids = {}
    place_actors(doc, left, ys, lw / 2 - 15, ids, actor_gap)
    place_actors(doc, right, ys, bx + bw + 110, ids, actor_gap, S_ACTOR_R)
    for code, acts in assoc.items():
        for a in acts:
            # Đoạn trong khung vẽ ngang để không cắt qua UC khác.
            cy = uc_y[code] + uc_h / 2
            if a in left:
                doc.edge(ids[a], uc_id[code], S_ASSOC + "exitX=1;exitY=0.5;entryX=0;entryY=0.5;",
                         points=[(bx - 20, cy)])
            else:
                doc.edge(uc_id[code], ids[a], S_ASSOC + "exitX=1;exitY=0.5;entryX=0;entryY=0.5;",
                         points=[(bx + bw + 20, cy)])
    for s, d, kind in rel:
        doc.edge(uc_id[s], uc_id[d], S_DEP, f"«{kind}»")
    return doc


def decomposition():
    doc = Doc("Phan_ra_chuc_nang")
    col_w, col_gap, child_w, child_h, child_gap = 184, 18, 166, 58, 16
    total = len(VUNG) * col_w + (len(VUNG) - 1) * col_gap
    root = doc.vertex(SYSTEM, "rounded=0;whiteSpace=wrap;html=1;fillColor=#DAE8FC;"
                      "strokeColor=#333333;fontStyle=1;fontSize=14;" + FONT,
                      total / 2 - 260, 20, 520, 56)
    for i, (code, name, v, subs) in enumerate(VUNG):
        x = 20 + i * (col_w + col_gap)
        l1 = doc.vertex(f"<b>{code}</b><br>{html.escape(name)}<br><i>({v})</i>",
                        "rounded=0;whiteSpace=wrap;html=1;fillColor=#F5F5F5;"
                        "strokeColor=#333333;fontSize=12;" + FONT,
                        x, 130, col_w, 80)
        doc.edge(root, l1, S_TREE + "exitX=0.5;exitY=1;entryX=0.5;entryY=0;")
        for j, (c2, n2) in enumerate(subs):
            y = 240 + j * (child_h + child_gap)
            l2 = doc.vertex(lbl(c2, n2), "rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;"
                            "strokeColor=#333333;fontSize=11;" + FONT,
                            x + col_w - child_w, y, child_w, child_h)
            tx = (col_w - child_w) / 2
            doc.edge(l1, l2, "rounded=0;html=1;endArrow=none;strokeColor=#333333;"
                     f"exitX={tx / col_w:.3f};exitY=1;entryX=0;entryY=0.5;",
                     points=[(x + tx, y + child_h / 2)])
    return doc


def main(out_root):
    targets = {}
    targets["I_Phan_ra_chuc_nang/Phan_ra_chuc_nang.drawio"] = decomposition()
    ucs = [(c, lbl(c, n)) for c, n, _, _ in VUNG]
    targets["II.1_Use_Case_Tong_Quat/II1_UC_Tong_Quat.drawio"] = usecase_diagram(
        "II1_UC_Tong_Quat", SYSTEM, ucs, II1_LEFT, II1_RIGHT,
        {c: [a for a, cs in II1_ASSOC.items() if c in cs] for c, *_ in VUNG}, [],
        uc_w=250, uc_h=64, gap=22, actor_gap=150,
        actor_y={"PMO": "UC-03", "CEO": "UC-06", "TC": "UC-08", "NL": "UC-02",
                 "RM": "UC-04", "PM": "UC-07"})
    for code, name, v, subs in VUNG:
        d = UCD[code]
        folder = ("II.2_V10" if code == "UC-09" else "II.2_UCD_cap_vung")
        targets[f"{folder}/UCD_{code}.drawio"] = usecase_diagram(
            f"UCD_{code}", f"{code} {name} ({v})",
            [(c, lbl(c, n)) for c, n in subs], d["left"], d["right"], d["assoc"], d["rel"])
    for rel, doc in targets.items():
        p = os.path.join(out_root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(doc.xml())
        print(p)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
