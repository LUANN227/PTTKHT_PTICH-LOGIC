"""Tách sơ đồ lớp miền II.3 thành các khung nhìn để trình bày.

Nguồn duy nhất vẫn là II3_Lop_Mien_Tong_Quat.puml. Mỗi khung nhìn giữ nguyên
các package được chọn; lớp của vùng khác có liên kết tới được vẽ màu xám, chỉ
ghi tên. Thêm một khung nhìn tổng quan chỉ có tên lớp và liên kết.
Chạy: python3 tach_view_II3.py <thư mục II.3_Domain_Class_Diagram>
"""
import os
import re
import sys

SRC = "II3_Lop_Mien_Tong_Quat.puml"
VIEWS = {
    "II3_View_A_V2-V4": ("Khung nhìn A: Nhu cầu, năng lực, tìm kiếm (V2–V4)", ["V2", "V3", "V4"]),
    "II3_View_B_V5-V7": ("Khung nhìn B: Khả năng tham gia, phương án, xung đột (V5–V7)",
                         ["V5", "V6", "V7"]),
    "II3_View_C_V8-V10": ("Khung nhìn C: Phê duyệt, chi phí, dự báo (V8–V10)", ["V8", "V9", "V10"]),
}
REL = re.compile(r'^(\w+)\s+(?:"[^"]*"\s+)?\S*--\S*\s+(?:"[^"]*"\s+)?(\w+)')


def parse(text):
    lines = text.splitlines()
    head, packages, rels = [], [], []
    i = 0
    while i < len(lines) and not lines[i].startswith("package "):
        if not lines[i].startswith("@"):
            head.append(lines[i])
        i += 1
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("package "):
            vung = re.search(r"\((V\d+)\)", ln).group(1)
            block = [ln]
            i += 1
            while lines[i] != "}":
                block.append(lines[i])
                i += 1
            block.append("}")
            classes = re.findall(r"^\s*class (\w+)", "\n".join(block), re.M)
            packages.append((vung, block, classes))
        elif REL.match(ln):
            rels.append(ln)
        i += 1
    return head, packages, rels


def main(folder):
    head, packages, rels = parse(open(os.path.join(folder, SRC), encoding="utf-8").read())
    owner = {c: v for v, _, cs in packages for c in cs}
    for name, (title, vs) in VIEWS.items():
        keep = {c for c, v in owner.items() if v in vs}
        out_rels, refs = [], set()
        for r in rels:
            a, b = REL.match(r).groups()
            if a in keep or b in keep:
                out_rels.append(r)
                refs |= {a, b} - keep
        body = [f"@startuml {name}", f"' Sinh tự động từ {SRC} bằng _cong_cu/tach_view_II3.py. Không sửa tay."]
        body += head + [f"title {title}"]
        for v, block, _ in packages:
            if v in vs:
                body += block
        if refs:
            body.append('package "Lớp của vùng khác (chỉ tham chiếu)" #F5F5F5 {')
            body += [f"  class {c} #EEEEEE" for c in sorted(refs)]
            body.append("}")
            body += [f"hide {c} members" for c in sorted(refs)]
        body += out_rels + ["@enduml", ""]
        open(os.path.join(folder, name + ".puml"), "w", encoding="utf-8").write("\n".join(body))
        print(name, len(keep), "lớp,", len(refs), "tham chiếu,", len(out_rels), "liên kết")
    # Tổng quan: chỉ tên lớp.
    src = open(os.path.join(folder, SRC), encoding="utf-8").read()
    src = src.replace("@startuml II3_Lop_Mien_Tong_Quat",
                      "@startuml II3_Tong_Quan_Ten_Lop\n' Sinh tự động từ " + SRC + ". Không sửa tay.", 1)
    src = src.replace("hide methods", "hide members\ntitle Tổng quan lớp miền (chỉ tên lớp và liên kết)", 1)
    open(os.path.join(folder, "II3_Tong_Quan_Ten_Lop.puml"), "w", encoding="utf-8").write(src)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
