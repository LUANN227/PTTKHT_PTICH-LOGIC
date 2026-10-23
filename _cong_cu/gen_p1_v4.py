"""Vẽ lại Hình AD V4 của Phần I (I.1.3.4), giữ đúng kiểu vẽ của Phần I, thêm làn PMO/Quản lý danh mục
cho hai bước phê duyệt miễn trừ (CN-37) và phê duyệt điều chỉnh xếp hạng, shortlist (CN-43).

    python3 _cong_cu/gen_p1_v4.py [file .drawio ra, mặc định 04_DRAWIO/I/AD_PhanI_V4.drawio]
"""
import os
import sys
from xml.sax.saxutils import escape

LANE = ("swimlane;html=1;startSize=34;horizontal=1;fillColor=none;swimlaneFillColor=none;fontStyle=1;"
        "fontSize=13;strokeColor=#333333;collapsible=0;")
ACT = "rounded=1;whiteSpace=wrap;html=1;arcSize=30;fillColor=#F7F7F7;strokeColor=#444444;fontSize=12;"
DEC = "rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;"
START = "ellipse;html=1;aspect=fixed;fillColor=#111111;strokeColor=#111111;"
END = "ellipse;html=1;shape=endState;aspect=fixed;fillColor=#111111;strokeColor=#111111;"
FFIN = "shape=sumEllipse;perimeter=ellipsePerimeter;html=1;aspect=fixed;fillColor=#FFFFFF;strokeColor=#111111;"
EDGE = ("edgeStyle=orthogonalEdgeStyle;html=1;rounded=0;endArrow=block;endFill=1;endSize=8;strokeColor=#333333;"
        "fontSize=12;labelBackgroundColor=#FFFFFF;")

cells, n = [], [0]
geo = {}


def nid():
    n[0] += 1
    return f"v{n[0]}"


def vertex(style, x, y, w, h, value="", key=None):
    i = key or nid()
    geo[i] = (x, y, w, h)
    cells.append(f'<mxCell id="{i}" value="{escape(value)}" style="{style}" vertex="1" parent="1">'
                 f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
    return i


def act(key, cx, y, text, w=300, h=40):
    return vertex(ACT, cx - w / 2, y, w, h, text, key)


def node(key, style, cx, cy, s):
    return vertex(style, cx - s / 2, cy - s / 2, s, s, "", key)


def side(k, s):
    x, y, w, h = geo[k]
    return {"T": (x + w / 2, y), "B": (x + w / 2, y + h), "L": (x, y + h / 2), "R": (x + w, y + h / 2)}[s]


def flow(a, b, sa="B", sb="T", pts=(), guard="", gx=0, gy=0):
    fx = {"T": (0.5, 0), "B": (0.5, 1), "L": (0, 0.5), "R": (1, 0.5)}
    (ax, ay), (bx, by) = fx[sa], fx[sb]
    st = EDGE + f"exitX={ax};exitY={ay};exitDx=0;exitDy=0;entryX={bx};entryY={by};entryDx=0;entryDy=0;"
    p = "".join(f'<mxPoint x="{x}" y="{y}"/>' for x, y in pts)
    i = nid()
    cells.append(f'<mxCell id="{i}" style="{st}" edge="1" parent="1" source="{a}" target="{b}">'
                 f'<mxGeometry relative="1" as="geometry">{"<Array as=\"points\">" + p + "</Array>" if p else ""}'
                 f'</mxGeometry></mxCell>')
    if guard:
        x, y = side(a, sa)
        cells.append(f'<mxCell id="{nid()}" value="{escape(guard)}" style="text;html=1;align=left;'
                     f'verticalAlign=middle;fontSize=12;labelBackgroundColor=none;" vertex="1" parent="1">'
                     f'<mxGeometry x="{x + gx}" y="{y + gy}" width="10" height="16" as="geometry"/></mxCell>')


def build():
    H = 1110
    lanes = [("RM", 15, 491), ("PM", 506, 294), ("PMO/Quản lý danh mục", 800, 300)]
    for name, x, w in lanes:
        vertex(LANE, x, 0, w, H, name)
    R, P, M = 15 + 299, 506 + 147, 800 + 150
    node("s", START, R, 52, 20)
    act("a1", R, 72, "Tiếp nhận nhu cầu đã xác nhận và hồ sơ năng lực (V4)", 320, 46)
    act("a2", R, 146, "Xác định tiêu chí đánh giá mức độ phù hợp (V4)", 310, 46)
    act("a3", R, 220, "Tìm kiếm ứng viên, đối chiếu điều kiện bắt buộc (V4)", 310, 46)
    node("d1", DEC, R, 312, 24)
    act("x2", R, 372, "Điều chỉnh nhu cầu, phản hồi về V2 (V4)", 264, 34)
    act("p1", P, 440, "Tiếp nhận phản hồi, rà soát lại nhu cầu (V2)", 270, 34)
    node("pf", FFIN, P, 512, 20)
    act("m1a", M, 360, "Phê duyệt miễn trừ điều kiện bắt buộc (V4)", 270, 40)
    node("m1", DEC, R, 560, 24)
    act("a4", R, 600, "Chấm điểm mức độ phù hợp theo bộ tiêu chí và trọng số đánh giá (V4)", 300, 40)
    act("a5", R, 672, "Xếp hạng ứng viên theo kết quả đánh giá mức độ phù hợp (V4)", 304, 40)
    act("a6", R, 744, "Rà soát bảng xếp hạng, ghi lý do nếu điều chỉnh (V4)", 311, 40)
    node("d2", DEC, R, 822, 24)
    act("m2a", M, 802, "Phê duyệt điều chỉnh xếp hạng, shortlist (V4)", 270, 40)
    node("m2", DEC, R, 900, 24)
    act("a7", R, 940, "Chốt shortlist và lưu thông tin tiêu chí, trọng số, kết quả đánh giá", 318, 46)
    act("a8", R, 1012, "Bàn giao bản ghi kết quả tìm kiếm cho V5", 272, 34)
    node("e", END, R, 1076, 22)
    for a, b in [("s", "a1"), ("a1", "a2"), ("a2", "a3"), ("a3", "d1"), ("m1", "a4"), ("a4", "a5"),
                 ("a5", "a6"), ("a6", "d2"), ("m2", "a7"), ("a7", "a8"), ("a8", "e"), ("x2", "p1", ), ("p1", "pf")]:
        if (a, b) == ("x2", "p1"):
            flow(a, b, "B", "T", [(R, 420), (P, 420)])
        else:
            flow(a, b)
    flow("d1", "x2", "B", "T", guard="[Không có ứng viên đáp ứng]", gx=6, gy=14)
    flow("d1", "m1", "L", "L", [(137, 312), (137, 560)], guard="[Có ứng viên đạt đầy đủ hoặc đạt có điều kiện]",
         gx=-161, gy=170)
    flow("d1", "m1a", "R", "T", [(M, 312)], guard="[Ứng viên không đạt, có đề nghị miễn trừ]", gx=10, gy=-14)
    flow("m1a", "m1", "B", "R", [(M, 560)])
    flow("d2", "m2a", "R", "L", guard="[Có điều chỉnh xếp hạng hoặc shortlist]", gx=10, gy=-14)
    flow("d2", "m2", "B", "T", guard="[Không điều chỉnh]", gx=6, gy=14)
    flow("m2a", "m2", "B", "R", [(M, 900)])
    body = "".join(cells)
    return ('<mxfile host="app.diagrams.net"><diagram name="Activity Diagram V4: tìm kiếm và đánh giá mức độ phù '
            'hợp"><mxGraphModel grid="0" page="0"><root><mxCell id="0"/><mxCell id="1" parent="0"/>'
            f'{body}</root></mxGraphModel></diagram></mxfile>')


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "04_DRAWIO", "I", "AD_PhanI_V4.drawio")
    open(out, "w", encoding="utf-8").write(build())
