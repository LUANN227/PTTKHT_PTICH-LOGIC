"""Thư viện vẽ Activity Diagram dạng draw.io gốc (làn, action, decision, merge, fork/join).

Dùng chung cho mọi AD của II.2: mỗi phần tử là một ô draw.io sửa được. Cách vẽ theo AD của Phần I:
decision và merge là hình thoi nhỏ, rỗng; điều kiện chỉ ghi ở guard [..] cạnh đường ra; nhánh kết thúc sớm
dùng flow final (⊗), chỉ điểm kết thúc chính dùng activity final (◉).

Bố cục đặt theo toạ độ gốc; khi xuất, chiều ngang được thu theo hệ số sx để sơ đồ không quá rộng (chữ còn
đọc được khi chèn vào trang A4). Action thu hẹp thì tự tăng chiều cao theo số dòng chữ.
"""
import html
import math

FONT = "fontFamily=Arial;"
STYLE = {
    "start": "ellipse;html=1;fillColor=#000000;strokeColor=#000000;",
    "final": "ellipse;html=1;shape=endState;fillColor=#000000;strokeColor=#000000;",
    "flowfinal": "shape=sumEllipse;perimeter=ellipsePerimeter;html=1;fillColor=#FFFFFF;strokeColor=#333333;",
    "action": ("rounded=1;arcSize=20;whiteSpace=wrap;html=1;fillColor=#F7F7F7;strokeColor=#333333;"
               "fontSize=11;" + FONT),
    "decision": "rhombus;html=1;fillColor=#FFFFFF;strokeColor=#333333;",
    "merge": "rhombus;html=1;fillColor=#FFFFFF;strokeColor=#333333;",
    "bar": "rounded=0;html=1;fillColor=#000000;strokeColor=#000000;",
}
SIZE = {"start": (26, 26), "final": (28, 28), "flowfinal": (24, 24), "action": (250, 54),
        "decision": (24, 24), "merge": (24, 24)}
S_FLOW = ("edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;endSize=8;"
          "strokeColor=#333333;" + FONT)
S_GUARD = "text;html=1;verticalAlign=middle;fontSize=11;labelBackgroundColor=#FFFFFF;" + FONT
S_HEAD = "rounded=0;html=1;fillColor=#F2F2F2;strokeColor=#333333;fontSize=12;" + FONT
S_LANE = "rounded=0;html=1;fillColor=none;strokeColor=#333333;"
MAX_W = 1080   # bề rộng tối đa của sơ đồ sau khi thu
MIN_SX = 0.7
CH = 5.6       # bề rộng trung bình một ký tự cỡ 11 (px)


def text_w(s):
    return int(len(s) * 5.3) + 4


class AD:
    def __init__(self, name, lanes, height, title=None, sx=None):
        self.name, self.n, self.node = name, 1, {}
        self.items = []     # ("v", id, kind, label, style, x, y, w, h) | ("e", id, src, dst, style, points)
        self.guards = []
        self.top = 20
        self.off = 0
        x = 20
        self.lane = {}
        for t_, w in lanes:
            self._v("head", f"<b>{html.escape(t_)}</b>", S_HEAD, x, 20, w, 34)
            self._v("lane", "", S_LANE, x, 54, w, height)
            self.lane[t_] = x + w / 2
            x += w
        self.width = x + 20
        self.sx = sx or max(MIN_SX, min(1.0, (MAX_W - 40) / (x - 20)))

    def _v(self, kind, label, style, x, y, w, h):
        self.n += 1
        i = f"n{self.n}"
        self.items.append(["v", i, kind, label, style, x, y, w, h])
        return i

    def add(self, key, kind, lane, cy, label="", dx=0, w=None):
        bw, bh = SIZE.get(kind, (0, 0))
        if kind == "bar":
            x0, x1 = lane
            bw, bh, cx = x1 - x0, 7, (x0 + x1) / 2
        else:
            cx = self.lane[lane] + dx
            bw = bw if kind in ("decision", "merge") else (w or bw)
        if kind in ("decision", "merge"):
            label = ""  # điều kiện ghi ở guard của đường ra, không ghi trong hình thoi
        i = self._v(kind, html.escape(label, quote=False), STYLE[kind], cx - bw / 2, cy - bh / 2, bw, bh)
        self.node[key] = (cx - bw / 2, cy - bh / 2, bw, bh, i)

    def flow(self, a, b, sa="B", sb="T", fa=0.5, fb=0.5, guard="", points=None, lx=None, gpos=None):
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
        self.items.append(["e", f"e{self.n}", A[4], B[4], st, list(points)])
        if guard:
            self.guards.append((f"[{guard}]", a, sa, gpos))

    # ------------------------------------------------------------ xuất
    def _layout(self):
        """Thu chiều ngang theo sx; trả về danh sách ô đã đặt và hình chữ nhật của guard."""
        sx = self.sx

        def X(x):
            return 20 + (x - 20) * sx
        geo, out = {}, []
        for it in self.items:
            if it[0] != "v":
                continue
            _, i, kind, label, style, x, y, w, h = it
            if kind in ("head", "lane", "bar"):
                x, w = X(x), w * sx
            elif kind == "action":
                cx, cy = X(x + w / 2), y + h / 2
                w = w * sx
                plain = html.unescape(label)
                lines = math.ceil(len(plain) * CH / max(w - 12, 40))
                h = max(h, lines * 14 + 14)
                x, y = cx - w / 2, cy - h / 2
            else:
                cx = X(x + w / 2)
                x = cx - w / 2
            geo[i] = (x, y, w, h)
            out.append(("v", i, kind, label, style, x, y, w, h))
        for it in self.items:
            if it[0] == "e":
                _, i, s, d, st, pts = it
                out.append(("e", i, s, d, st, [(X(px), py) for px, py in pts]))
        rects = []
        for lab, key, side, gpos in self.guards:
            x, y, w, h = geo[self.node[key][4]]
            p = {"L": (x, y + h / 2), "R": (x + w, y + h / 2), "T": (x + w / 2, y), "B": (x + w / 2, y + h)}[side]
            gw = text_w(lab)
            px, py = p
            if gpos == "BL":       # ra dưới, guard bên trái đường
                gx, gy, al = px - 5 - gw, py + 3, "right"
            elif gpos == "LB":     # ra trái, guard phía dưới đường
                gx, gy, al = px - 4 - gw, py + 3, "right"
            elif gpos:
                gx, gy, al = px + gpos[0], py + gpos[1], "left"
            elif side == "B":
                gx, gy, al = px + 5, py + 3, "left"
            elif side == "T":
                gx, gy, al = px + 5, py - 21, "left"
            elif side == "R":
                gx, gy, al = px + 4, py - 19, "left"
            else:
                gx, gy, al = px - 4 - gw, py - 19, "right"
            rects.append((lab, gx, gy, gw, 18, al))
        return out, geo, rects

    def check(self):
        """Báo guard đè phần tử khác hoặc ra ngoài làn, và action đè nhau sau khi thu chiều ngang."""
        out, geo, rects = self._layout()
        boxes = [(i, k, x, y, w, h) for _, i, k, *_r in [o for o in out if o[0] == "v"]
                 for (x, y, w, h) in [geo[i]] if k not in ("head", "lane")]
        names = {v[4]: k for k, v in self.node.items()}
        right = max(x + w for i, k, x, y, w, h in [(o[1], o[2], *geo[o[1]]) for o in out if o[0] == "v"])
        bad = []
        for lab, gx, gy, gw, gh, _ in rects:
            for i, k, x, y, w, h in boxes:
                tol = 8  # bề rộng chữ ước lượng dư
                if gx + tol < x + w and x < gx + gw - tol and gy < y + h and y < gy + gh:
                    bad.append(f"{self.name}: {lab} đè {names.get(i, i)}")
            if gx < 20 or gx + gw > right:
                bad.append(f"{self.name}: {lab} ra ngoài làn")
        for a in range(len(boxes)):
            for b in range(a + 1, len(boxes)):
                i, _, x, y, w, h = boxes[a]
                j, _, X2, Y2, W2, H2 = boxes[b]
                if x < X2 + W2 and X2 < x + w and y < Y2 + H2 and Y2 < y + h:
                    bad.append(f"{self.name}: {names.get(i, i)} đè {names.get(j, j)}")
        return bad

    def xml(self):
        out, geo, rects = self._layout()
        cells = []
        for o in out:
            if o[0] == "v":
                _, i, kind, label, style, x, y, w, h = o
                cells.append(f'<mxCell id="{i}" value="{html.escape(label, quote=True)}" style="{style}" '
                             f'vertex="1" parent="1"><mxGeometry x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" '
                             f'height="{h:.0f}" as="geometry"/></mxCell>')
            else:
                _, i, s, d, st, pts = o
                p = "".join(f'<mxPoint x="{x:.0f}" y="{y:.0f}"/>' for x, y in pts)
                p = f'<Array as="points">{p}</Array>' if p else ""
                cells.append(f'<mxCell id="{i}" value="" style="{st}" edge="1" parent="1" source="{s}" '
                             f'target="{d}"><mxGeometry relative="1" as="geometry">{p}</mxGeometry></mxCell>')
        for k, (lab, gx, gy, gw, gh, al) in enumerate(rects):
            cells.append(f'<mxCell id="g{k}" value="{html.escape(html.escape(lab), quote=True)}" '
                         f'style="{S_GUARD}align={al};" vertex="1" parent="1"><mxGeometry x="{gx:.0f}" '
                         f'y="{gy:.0f}" width="{gw}" height="{gh}" as="geometry"/></mxCell>')
        width = 20 + (self.width - 40) * self.sx + 20
        return ('<mxfile host="ad_lib.py" type="device">'
                f'<diagram id="{self.name}" name="{self.name}"><mxGraphModel dx="1200" dy="800" '
                'grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" '
                f'page="1" pageScale="1" pageWidth="{width:.0f}" pageHeight="1400" math="0" '
                'shadow="0"><root><mxCell id="0"/><mxCell id="1" parent="0"/>'
                + "".join(cells) + '</root></mxGraphModel></diagram></mxfile>\n')
