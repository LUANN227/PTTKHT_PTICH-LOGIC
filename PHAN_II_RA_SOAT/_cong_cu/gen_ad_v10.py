"""Sinh AD UC-09.1 và UC-09.2 (V10) dạng draw.io gốc, theo UC Description V10 trong bản rà soát.

    python3 gen_ad_v10.py <thư mục ra>
"""
import html
import os
import sys

FONT = "fontFamily=Arial;"
STYLE = {
    "start": "ellipse;html=1;fillColor=#000000;strokeColor=#000000;",
    "final": "ellipse;html=1;shape=endState;fillColor=#000000;strokeColor=#000000;",
    "action": ("rounded=1;arcSize=20;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;"
               "fontSize=11;" + FONT),
    "decision": ("rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=10;"
                 + FONT),
    "merge": "rhombus;html=1;fillColor=#FFFFFF;strokeColor=#333333;",
    "bar": "rounded=0;html=1;fillColor=#000000;strokeColor=#000000;",
}
SIZE = {"start": (26, 26), "final": (28, 28), "action": (250, 54), "decision": (180, 84),
        "merge": (36, 36)}
S_FLOW = ("edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=open;endSize=10;"
          "strokeColor=#333333;fontSize=10;labelBackgroundColor=#FFFFFF;" + FONT)


class AD:
    def __init__(self, name, lanes, height):
        self.name, self.cells, self.n, self.node = name, [], 1, {}
        x = 20
        self.lane = {}
        for title, w in lanes:
            self._v(f"<b>{html.escape(title)}</b>", "rounded=0;html=1;fillColor=#F2F2F2;"
                    "strokeColor=#333333;fontSize=12;" + FONT, x, 20, w, 34)
            self._v("", "rounded=0;html=1;fillColor=none;strokeColor=#333333;", x, 54, w, height)
            self.lane[title] = x + w / 2
            x += w
        self.width = x + 20

    def _v(self, label, style, x, y, w, h):
        self.n += 1
        i = f"n{self.n}"
        self.cells.append(f'<mxCell id="{i}" value="{html.escape(label, quote=True)}" style="{style}" vertex="1" parent="1">'
                          f'<mxGeometry x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" '
                          f'as="geometry"/></mxCell>')
        return i

    def add(self, key, kind, lane, cy, label="", dx=0, w=None):
        bw, bh = SIZE.get(kind, (0, 0))
        if kind == "bar":
            x0, x1 = lane
            bw, bh, cx = x1 - x0, 7, (x0 + x1) / 2
        else:
            cx = self.lane[lane] + dx
            bw = w or bw
        i = self._v(html.escape(label, quote=False), STYLE[kind], cx - bw / 2, cy - bh / 2, bw, bh)
        self.node[key] = (cx - bw / 2, cy - bh / 2, bw, bh, i)

    def flow(self, a, b, sa="B", sb="T", fa=0.5, fb=0.5, guard="", points=None, lx=-0.6):
        A, B = self.node[a], self.node[b]

        def port(box, s, f):
            x, y, w, h, _ = box
            return {"L": (x, y + f * h), "R": (x + w, y + f * h), "T": (x + f * w, y),
                    "B": (x + f * w, y + h)}[s]
        p1, p2 = port(A, sa, fa), port(B, sb, fb)
        if points is None:
            points = []
            if sa in "TB" and sb in "TB" and abs(p1[0] - p2[0]) > 1:
                m = (p1[1] + p2[1]) / 2
                points = [(p1[0], m), (p2[0], m)]
            elif sa in "LR" and sb in "LR" and abs(p1[1] - p2[1]) > 1:
                m = (p1[0] + p2[0]) / 2
                points = [(m, p1[1]), (m, p2[1])]
            elif (sa in "LR") != (sb in "LR"):
                points = [(p2[0], p1[1])] if sa in "LR" else [(p1[0], p2[1])]

        def xy(s, f):
            return ((1 if s == "R" else 0, f) if s in "LR" else (f, 1 if s == "B" else 0))
        ex, ey = xy(sa, fa)
        nx, ny = xy(sb, fb)
        st = S_FLOW + f"exitX={ex};exitY={ey};entryX={nx};entryY={ny};"
        self.n += 1
        pts = "".join(f'<mxPoint x="{x:.0f}" y="{y:.0f}"/>' for x, y in points)
        pts = f'<Array as="points">{pts}</Array>' if pts else ""
        lab = html.escape(f"[{guard}]") if guard else ""
        self.cells.append(f'<mxCell id="e{self.n}" value="{lab}" style="{st}" edge="1" parent="1" '
                          f'source="{A[4]}" target="{B[4]}"><mxGeometry x="{lx if guard else 0}" '
                          f'relative="1" as="geometry">{pts}</mxGeometry></mxCell>')

    def xml(self):
        return ('<mxfile host="gen_ad_v10.py" type="device">'
                f'<diagram id="{self.name}" name="{self.name}"><mxGraphModel dx="1200" dy="800" '
                'grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" '
                f'page="1" pageScale="1" pageWidth="{self.width:.0f}" pageHeight="1400" math="0" '
                'shadow="0"><root><mxCell id="0"/><mxCell id="1" parent="0"/>'
                + "".join(self.cells) + '</root></mxGraphModel></diagram></mxfile>\n')


def ad_0901():
    d = AD("AD UC-09.1", [("RM", 380), ("Hệ thống", 360), ("PM", 300)], 1250)
    d.add("s", "start", "RM", 85)
    d.add("a1", "action", "RM", 150, "Mở lần tổng hợp theo kỳ tuần hoặc khi có thay đổi đáng kể")
    d.add("f", "bar", (90, 990), 220)
    d.add("a2", "action", "RM", 290, "Tổng hợp nguồn cung, lịch/phân bổ và các cam kết hiện có")
    d.add("a2b", "action", "PM", 290, "Cung cấp, xác nhận nhu cầu theo dự án, vai trò, kỹ năng, "
          "thời gian", w=250)
    d.add("j", "bar", (90, 990), 360)
    d.add("d1", "decision", "RM", 440, "Nguồn cung đủ cơ sở?")
    d.add("e1", "action", "Hệ thống", 440, "Ghi phần thiếu, yêu cầu bổ sung; lưu tổng hợp tạm, "
          "chưa lập dự báo chính thức", w=250)
    d.add("f1", "final", "Hệ thống", 515)
    d.add("a4", "action", "RM", 545, "Xác định nguồn cung có thể đáp ứng sau khi trừ đủ phân bổ "
          "và cam kết", w=250)
    d.add("a5", "action", "RM", 635, "Lập dự báo và đối chiếu (thực hiện UC-09.2)")
    d.add("d2", "decision", "RM", 730, "Có kết quả đủ cơ sở?")
    d.add("e2", "action", "Hệ thống", 730, "Ghi tình trạng đầu vào; chuyển RM, PM xác nhận hoặc "
          "bổ sung (không coi cầu bằng 0)", w=250)
    d.add("f2", "final", "Hệ thống", 805)
    d.add("a6", "action", "RM", 835, "Phân tích thiếu/dư theo số lượng, vai trò, kỹ năng và "
          "thời điểm", w=250)
    d.add("a7", "action", "RM", 925, "Tổng hợp kết quả; thông tin chi phí V9 chỉ là căn cứ bổ sung",
          w=250)
    d.add("d3", "decision", "RM", 1020, "RM quyết định chuyển kết quả?")
    d.add("a9", "action", "Hệ thống", 1020, "Chuyển đúng nhóm thông tin cho V2, V6, V7, V8", w=250)
    d.add("m", "merge", "Hệ thống", 1110)
    d.add("a10", "action", "Hệ thống", 1185, "Lưu quyết định của RM và kết quả; PM tra cứu được",
          w=250)
    d.add("f3", "final", "Hệ thống", 1260)
    d.flow("s", "a1")
    d.flow("a1", "f", fb=(d.lane["RM"] - 90) / 900)
    d.flow("f", "a2", fa=(d.lane["RM"] - 90) / 900)
    d.flow("f", "a2b", fa=(d.lane["PM"] - 90) / 900)
    d.flow("a2", "j", fb=(d.lane["RM"] - 90) / 900)
    d.flow("a2b", "j", fb=(d.lane["PM"] - 90) / 900)
    d.flow("j", "d1", fa=(d.lane["RM"] - 90) / 900)
    d.flow("d1", "e1", "R", "L", guard="Chưa đủ", lx=-0.3)
    d.flow("e1", "f1")
    d.flow("d1", "a4", guard="Đủ", lx=-0.2)
    d.flow("a4", "a5")
    d.flow("a5", "d2")
    d.flow("d2", "e2", "R", "L", guard="Chưa", lx=-0.3)
    d.flow("e2", "f2")
    d.flow("d2", "a6", guard="Có", lx=-0.2)
    d.flow("a6", "a7")
    d.flow("a7", "d3")
    d.flow("d3", "a9", "R", "L", guard="Chuyển", lx=-0.3)
    d.flow("a9", "m")
    d.flow("d3", "m", "B", "L", guard="Tiếp tục theo dõi", lx=-0.3)
    d.flow("m", "a10")
    d.flow("a10", "f3")
    return d


def ad_0902():
    d = AD("AD UC-09.2", [("RM", 420), ("Hệ thống", 400)], 1110)
    rm, ht = d.lane["RM"], d.lane["Hệ thống"]
    d.add("s", "start", "Hệ thống", 85)
    d.add("b1", "action", "Hệ thống", 150, "Nhận nguồn cung có thể đáp ứng, nhu cầu và khoảng thời "
          "gian từ UC-09.1", w=260)
    d.add("m1", "merge", "RM", 240)
    d.add("dc", "decision", "RM", 325, "Còn nhu cầu cần xét?")
    d.add("b2", "action", "RM", 425, "Xét trạng thái, mức chắc chắn, thời gian và phạm vi của nhu cầu",
          w=260)
    d.add("dd", "decision", "RM", 525, "Nhu cầu đủ cơ sở?")
    d.add("b3", "action", "Hệ thống", 525, "Gắn nhãn đã xác nhận hoặc dự kiến; đưa vào tập dự báo",
          w=260)
    d.add("b4", "action", "RM", 625, "Ghi lý do chưa đủ cơ sở; chưa đưa nhu cầu vào dự báo", w=260)
    d.add("m2", "merge", "RM", 710)
    d.add("dk", "decision", "RM", 830, "Có nhu cầu đủ cơ sở?")
    d.add("b5", "action", "Hệ thống", 830, "Ghi tình trạng đầu vào; trả RM, PM xác nhận cơ sở "
          "(không coi cầu bằng 0)", w=260)
    d.add("f1", "final", "Hệ thống", 910, dx=0)
    d.add("b6", "action", "RM", 935, "Lập dự báo cung và cầu theo khoảng thời gian đã xác định",
          w=260)
    d.add("b7", "action", "RM", 1025, "Đối chiếu cung – cầu từng khoảng; xác định đáp ứng, thiếu, dư",
          w=260)
    d.add("b8", "action", "Hệ thống", 1025, "Lưu kết quả, mức chắc chắn và phần dữ liệu thiếu; "
          "trả UC-09.1", w=260)
    d.add("f2", "final", "Hệ thống", 1110)
    d.flow("s", "b1")
    d.flow("b1", "m1", "B", "R", points=[(ht, 240)])
    d.flow("m1", "dc")
    d.flow("dc", "b2", guard="Còn", lx=-0.2)
    d.flow("b2", "dd")
    d.flow("dd", "b3", "R", "L", guard="Đủ", lx=-0.3)
    d.flow("dd", "b4", guard="Chưa đủ", lx=-0.2)
    d.flow("b4", "m2")
    d.flow("b3", "m2", "B", "R", points=[(ht, 710)])
    d.flow("m2", "m1", "L", "L", points=[(45, 710), (45, 240)])
    d.flow("dc", "dk", "R", "T", guard="Hết", lx=-0.75,
           points=[(ht + 175, 325), (ht + 175, 770), (rm, 770)])
    d.flow("dk", "b5", "R", "L", guard="Chưa có", lx=-0.3)
    d.flow("b5", "f1")
    d.flow("dk", "b6", guard="Có", lx=-0.2)
    d.flow("b6", "b7")
    d.flow("b7", "b8", "R", "L")
    d.flow("b8", "f2")
    return d


def main(out):
    os.makedirs(out, exist_ok=True)
    for n, d in (("AD_UC-09.1", ad_0901()), ("AD_UC-09.2", ad_0902())):
        with open(os.path.join(out, n + ".drawio"), "w", encoding="utf-8") as f:
            f.write(d.xml())
        print(n)


if __name__ == "__main__":
    main(sys.argv[1])
