"""Sơ đồ phân cấp chức năng (II.1) bố cục hai tầng, vừa trang dọc của báo cáo Word.

Mã, tên vùng và UC con lấy từ gen_drawio.py (HD-PCCN §1). gen_drawio.py cũng sinh UCD tổng quát và UCD
cấp vùng; script chép các hình đó vào 04_DRAWIO/II.1 và 04_DRAWIO/II.2_UCD_vung.

    python3 _cong_cu/gen_phan_cap.py [thư mục drawio ra, mặc định 04_DRAWIO]
"""
import html
import importlib.util
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    spec = importlib.util.spec_from_file_location("g", os.path.join(HERE, "gen_drawio.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def hierarchy(g):
    doc = g.Doc("Phan_cap_chuc_nang")
    F = g.FONT
    col_w, gap, child_w, child_h, child_gap = 206, 16, 186, 54, 14
    S_TREE = "rounded=0;html=1;endArrow=none;strokeColor=#333333;"
    width = 5 * col_w + 4 * gap + 40
    root = doc.vertex(g.SYSTEM, "rounded=0;whiteSpace=wrap;html=1;fillColor=#DAE8FC;"
                      "strokeColor=#333333;fontStyle=1;fontSize=14;" + F,
                      width / 2 - 270, 20, 540, 52)
    rows = [g.VUNG[:5], g.VUNG[5:]]
    top = 130
    for r, row in enumerate(rows):
        bus = top - 28
        for i, (code, name, v, subs) in enumerate(row):
            x = 20 + i * (col_w + gap)
            l1 = doc.vertex(f"<b>{code}</b><br>{html.escape(name)}<br><i>({v})</i>",
                            "rounded=0;whiteSpace=wrap;html=1;fillColor=#F5F5F5;"
                            "strokeColor=#333333;fontSize=12;spacingLeft=6;spacingRight=6;" + F,
                            x, top, col_w, 76)
            cx = x + col_w / 2
            if r == 0:
                doc.edge(root, l1, S_TREE + "exitX=0.5;exitY=1;entryX=0.5;entryY=0;",
                         points=[(width / 2, bus), (cx, bus)])
            else:
                doc.edge(root, l1, S_TREE + "exitX=0;exitY=0.5;entryX=0.5;entryY=0;",
                         points=[(8, 46), (8, bus), (cx, bus)])
            for j, (c2, n2) in enumerate(subs):
                y = top + 76 + 26 + j * (child_h + child_gap)
                l2 = doc.vertex(g.lbl(c2, n2), "rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;"
                                "strokeColor=#333333;fontSize=11;spacingLeft=6;spacingRight=6;" + F,
                                x + col_w - child_w, y, child_w, child_h)
                tx = (col_w - child_w) / 2
                doc.edge(l1, l2, S_TREE + f"exitX={tx / col_w:.3f};exitY=1;entryX=0;entryY=0.5;",
                         points=[(x + tx, y + child_h / 2)])
        deepest = max(len(s) for *_, s in row)
        top = top + 76 + 26 + deepest * (child_h + child_gap) + 60
    return doc


def main(out):
    g = load()
    src = tempfile.mkdtemp()
    g.main(src)
    os.makedirs(os.path.join(out, "II.1"), exist_ok=True)
    with open(os.path.join(out, "II.1", "Phan_cap_chuc_nang.drawio"), "w", encoding="utf-8") as f:
        f.write(hierarchy(g).xml())
    shutil.copy(os.path.join(src, "II.1_Use_Case_Tong_Quat", "II1_UC_Tong_Quat.drawio"),
                os.path.join(out, "II.1", "II1_UC_Tong_Quat.drawio"))
    os.makedirs(os.path.join(out, "II.2_UCD_vung"), exist_ok=True)
    for k in range(1, 10):
        folder = "II.2_V10" if k == 9 else "II.2_UCD_cap_vung"
        shutil.copy(os.path.join(src, folder, f"UCD_UC-0{k}.drawio"),
                    os.path.join(out, "II.2_UCD_vung", f"UCD_UC-0{k}.drawio"))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(HERE), "04_DRAWIO"))
