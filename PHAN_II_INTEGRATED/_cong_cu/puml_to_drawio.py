"""Bọc một sơ đồ PlantUML thành file .drawio.

File .drawio chứa ảnh SVG kèm mã PlantUML gốc (thuộc tính plantUmlData),
giống cách draw.io lưu hình chèn bằng Arrange > Insert > Advanced > PlantUML.
Trong draw.io: chọn hình > Edit > Edit Data/Edit PlantUML để sửa mã và vẽ lại.
Chạy: python3 puml_to_drawio.py <file.puml> <file.svg> <file.drawio>
"""
import base64
import html
import json
import re
import sys


def main(puml, svg, out):
    src = open(puml, encoding="utf-8").read()
    data = open(svg, "rb").read()
    m = re.search(rb'width="(\d+)(?:px)?"[^>]*height="(\d+)(?:px)?"', data)
    w, h = (int(m.group(1)), int(m.group(2))) if m else (800, 600)
    uri = "data:image/svg+xml," + base64.b64encode(data).decode()
    pdata = html.escape(json.dumps({"data": src, "format": "svg"}, ensure_ascii=False), quote=True)
    style = f"shape=image;noLabel=1;verticalAlign=top;aspect=fixed;imageAspect=0;image={uri};"
    name = html.escape(puml.rsplit("/", 1)[-1].rsplit(".", 1)[0])
    xml = (
        '<mxfile host="puml_to_drawio.py" type="device">'
        f'<diagram id="{name}" name="{name}"><mxGraphModel grid="1" gridSize="10" page="1" '
        'pageWidth="1169" pageHeight="827"><root><mxCell id="0"/><mxCell id="1" parent="0"/>'
        f'<UserObject label="" plantUmlData="{pdata}" id="p1">'
        f'<mxCell style="{style}" vertex="1" parent="1">'
        f'<mxGeometry x="10" y="10" width="{w}" height="{h}" as="geometry"/></mxCell>'
        '</UserObject></root></mxGraphModel></diagram></mxfile>\n')
    open(out, "w", encoding="utf-8").write(xml)


if __name__ == "__main__":
    main(*sys.argv[1:4])
