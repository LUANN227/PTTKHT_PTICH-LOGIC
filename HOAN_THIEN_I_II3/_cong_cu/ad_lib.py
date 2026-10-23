"""Thư viện vẽ Activity Diagram dạng draw.io gốc (làn, action, decision, merge, fork/join).

Dùng chung cho mọi AD của II.2: mỗi phần tử là một ô draw.io sửa được.
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
SIZE = {"start": (26, 26), "final": (28, 28), "action": (250, 54), "decision": (210, 90),
        "merge": (36, 36)}
S_FLOW = ("edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=open;endSize=10;"
          "strokeColor=#333333;fontSize=10;labelBackgroundColor=#FFFFFF;" + FONT)


class AD:
    def __init__(self, name, lanes, height, title=None):
        self.name, self.cells, self.n, self.node = name, [], 1, {}
        x = 20
        self.lane = {}
        top = 20
        if title:
            total = sum(w for _, w in lanes)
            self._v(f"<b>{html.escape(title)}</b>", "text;html=1;align=left;verticalAlign=middle;"
                    "fontSize=14;" + FONT, 20, 8, total, 30)
            top = 44
        self.top = top
        self.off = top - 20
        for t_, w in lanes:
            self._v(f"<b>{html.escape(t_)}</b>", "rounded=0;html=1;fillColor=#F2F2F2;"
                    "strokeColor=#333333;fontSize=12;" + FONT, x, top, w, 34)
            self._v("", "rounded=0;html=1;fillColor=none;strokeColor=#333333;", x, top + 34, w, height)
            self.lane[t_] = x + w / 2
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
        cy += self.off
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
        if points is not None:
            points = [(x, y + self.off) for x, y in points]
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
        return ('<mxfile host="ad_lib.py" type="device">'
                f'<diagram id="{self.name}" name="{self.name}"><mxGraphModel dx="1200" dy="800" '
                'grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" '
                f'page="1" pageScale="1" pageWidth="{self.width:.0f}" pageHeight="1400" math="0" '
                'shadow="0"><root><mxCell id="0"/><mxCell id="1" parent="0"/>'
                + "".join(self.cells) + '</root></mxGraphModel></diagram></mxfile>\n')


