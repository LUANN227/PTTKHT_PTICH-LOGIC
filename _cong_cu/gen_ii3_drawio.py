"""Sinh sơ đồ lớp miền II.3 dạng draw.io gốc (mỗi lớp, mỗi quan hệ là một phần tử sửa được).

Gồm một hình tổng quan theo gói và năm hình cụm lớp. Toạ độ đặt tay theo lưới; mọi cạnh
vuông góc với điểm gấp tính sẵn để draw.io và bản xuất cho cùng một hình.

    python3 _cong_cu/gen_ii3_drawio.py [thư mục ra, mặc định 04_DRAWIO/II.3]
"""
import html
import os
import sys

FONT = "fontFamily=Arial;"

# ---------------------------------------------------------------- mô hình miền
# Thuộc tính lấy theo bản ChatGPT (domain_model.json), là tập bao của bản tích hợp trước.
CLASSES = {
    "DuAn": ["maDuAn", "tenDuAn", "ngayBatDau", "ngayKetThuc", "hangUuTien"],
    "GiaiDoanDuAn": ["maGiaiDoan", "tenGiaiDoan", "ngayBatDau", "ngayKetThuc"],
    "NhuCauNguonLuc": ["maNhuCau", "phamViCongViec", "thoiGianBatDau", "thoiGianKetThuc", "trangThai"],
    "ViTriCanBoTri": ["maViTri", "vaiTro", "soLuong", "tyLeFTE"],
    "YeuCauKyNang": ["capDoYeuCau", "batBuoc"],
    "PhanHoiNhuCau": ["maPhanHoi", "nguonPhanHoi", "noiDung", "thoiDiem"],
    "NguonLuc": ["maNguonLuc", "hoTen", "loaiNguon", "nangLucChuan"],
    "KyNang": ["maKyNang", "tenKyNang"],
    "HoSoNangLuc": ["kinhNghiem", "chungChi"],
    "NangLucKyNang": ["mucThanhThao", "trangThaiXacNhan", "ngayDanhGia", "canCuXacNhan"],
    "BoTieuChiNangLuc": ["maBo", "trangThai"],
    "TieuChiNangLuc": ["maTieuChi", "tenTieuChi", "trangThai"],
    "MucDoNangLuc": ["thuTu", "moTa", "dieuKienCongNhan"],
    "BoTieuChiPhuHop": ["phienBan", "ngayXacLap"],
    "TieuChiPhuHop": ["tenTieuChi", "loai", "trongSo"],
    "PhienTimKiem": ["maPhien", "thoiDiem", "trangThai"],
    "KetQuaDanhGiaPhuHop": ["phanLoai", "diemTong", "thuHang", "vaiTroShortlist", "mucDapUng", "khoangThieuNangLuc", "lyDoKhongDat",
                            "coXungDotLoiIch"],
    "DiemTieuChi": ["diem"],
    "DeNghiMienTru": ["lyDo", "trangThai", "noiDungDieuKienDuocMien", "nguoiPheDuyet",
                      "thoiDiemQuyetDinh"],
    "YeuCauNguonLuc": ["maYeuCau", "loaiYeuCau", "khungThoiGianTu", "khungThoiGianDen"],
    "LichNguonLuc": ["thoiGianNghi", "ngayCapNhat"],
    "PhanBoNguonLuc": ["loaiPhanBo", "tuNgay", "denNgay", "tyLe", "trangThaiXacNhan"],
    "KetLuanKhaNangThamGia": ["trangThaiKhaNang", "mucSuDung", "thoiGianTrong", "coRuiRoQuaTai",
                              "ngayYeuCauXacNhan", "hanXacNhan", "lyDoChoXacNhan", "canCuDanhGia"],
    "DeXuatThamGiaMotPhan": ["tyLe", "khungThoiGian", "trangThaiPM"],
    "HoSoVuotTaiNgoaiLe": ["mucCanhBao", "lyDo", "capThamQuyen", "trangThai"],
    "PhuongAnBoTri": ["maPhuongAn", "phienBan", "loaiPhuongAn", "trangThai", "laChapNhanMotPhan",
                      "ngayBatDauXayDung", "ngayGuiPM"],
    "ChiTietBoTri": ["vaiTroDuocGan", "tyLeThamGia", "tuNgay", "denNgay"],
    "RuiRoViTri": ["loaiRuiRo", "bienPhapGiamThieu"],
    "DiemXungDot": ["maXungDot", "mucSuDung", "mucCanhBao", "trangThaiXuLy"],
    "NhatKyXuLyXungDot": ["thoiDiem", "noiDung", "loaiXuLy"],
    "PhanXuXungDot": ["ngayChuyenCap", "lyDoBeTac", "capPhanXu", "noiDungQuyetDinh"],
    "DeXuatThayDoi": ["loaiThayDoi", "noiDung"],
    "HoSoTrinhDuyet": ["maHoSo", "ngayTrinh", "mucRuiRo", "capThamQuyen", "trangThaiXuLy", "ngayChuyenCap"],
    "YeuCauGiaiTrinh": ["noiDungCanLamRo", "ngayYeuCau", "trangThai"],
    "QuyetDinhPheDuyet": ["loaiQuyetDinh", "lyDo", "dieuKienApDung", "nguoiQuyetDinh", "thoiDiem"],
    "DonGia": ["loaiNguonLuc", "giaTri", "donViTinh = VNĐ/ngày công", "ngayApDung"],
    "DuToanChiPhi": ["ngayLap", "/tongChiPhi"],
    "DuBaoChiPhi": ["ngayCapNhat", "lyDoCapNhat", "/tongChiPhiDuBao"],
    "ChiPhiThucTe": ["soTien", "ngayPhatSinh"],
    "NganSach": ["nganSachDuyet", "/conLai"],
    "DanhGiaChiPhi": ["thoiDiem", "chenhLech", "tyLeVuot", "trangThaiNganSach", "capXuLy",
                      "chiPhiDuKienTaiThoiDiem", "nganSachConLaiTaiThoiDiem"],
    "NguyenNhanVuot": ["noiDung"],
    "HuongXuLy": ["loai", "ghiChu"],
    "SoSanhPhuongAn": ["thoiDiem"],
    "ChiTietSoSanh": ["mucChatLuong", "thoiGianThucHien", "/chiPhi", "datChatLuongToiThieu",
                      "thuTuUuTien"],
    "KetQuaDuBao": ["loaiLap", "tuNgay", "denNgay", "mucThieuDuLieu", "quyetDinhChuyen"],
    "TongHopNguonCung": ["khoangThoiGian", "/nguonCungCoTheDapUng"],
    "NhuCauDuBao": ["mucDoChacChan", "duCoSo", "vaiTro", "kyNang", "soLuong", "khoangThoiGian",
                    "nguonNhuCau", "trangThaiNhuCau", "phamVi"],
    "DongDoiChieuCungCau": ["khoangThoiGian", "mucDoDapUng", "chenhLech", "laThieuNangLuc", "vaiTro",
                            "kyNang", "cungDuBao", "cauDuBao"],
}

# Cụm lớp: mã hình, tên, vùng, lớp sở hữu.
CLUSTERS = [
    ("A", "II.3-2", "Nhu cầu và năng lực", "V2, V3",
     ["DuAn", "GiaiDoanDuAn", "NhuCauNguonLuc", "ViTriCanBoTri", "YeuCauKyNang", "PhanHoiNhuCau",
      "NguonLuc", "KyNang", "HoSoNangLuc", "NangLucKyNang", "BoTieuChiNangLuc", "TieuChiNangLuc",
      "MucDoNangLuc"]),
    ("B", "II.3-3", "Tìm kiếm, khả năng tham gia và lịch", "V4, V5",
     ["BoTieuChiPhuHop", "TieuChiPhuHop", "PhienTimKiem", "KetQuaDanhGiaPhuHop", "DiemTieuChi",
      "DeNghiMienTru", "YeuCauNguonLuc", "LichNguonLuc", "PhanBoNguonLuc", "KetLuanKhaNangThamGia",
      "DeXuatThamGiaMotPhan", "HoSoVuotTaiNgoaiLe"]),
    ("C", "II.3-4", "Phương án, xung đột và phê duyệt", "V6, V7, V8",
     ["PhuongAnBoTri", "ChiTietBoTri", "RuiRoViTri", "DiemXungDot", "NhatKyXuLyXungDot",
      "PhanXuXungDot", "DeXuatThayDoi", "HoSoTrinhDuyet", "YeuCauGiaiTrinh", "QuyetDinhPheDuyet"]),
    ("D", "II.3-5", "Chi phí và ngân sách", "V9",
     ["DonGia", "DuToanChiPhi", "DuBaoChiPhi", "ChiPhiThucTe", "NganSach", "DanhGiaChiPhi",
      "NguyenNhanVuot", "HuongXuLy", "SoSanhPhuongAn", "ChiTietSoSanh"]),
    ("E", "II.3-6", "Theo dõi và dự báo cung – cầu", "V10",
     ["KetQuaDuBao", "TongHopNguonCung", "NhuCauDuBao", "DongDoiChieuCungCau"]),
]
OWNER = {c: k for k, _, _, _, cs in CLUSTERS for c in cs}
FIG = {k: f for k, f, *_ in CLUSTERS}

# ---------------------------------------------------------------- vẽ
CHAR_W, NAME_W, LINE_H = 6.4, 7.6, 14


class Doc:
    def __init__(self, name, page_w=1169, page_h=827):
        self.name, self.cells, self.n = name, [], 1
        self.page_w, self.page_h = page_w, page_h
        self.box = {}

    def _id(self):
        self.n += 1
        return f"c{self.n}"

    def add(self, xml):
        self.cells.append(xml)

    def vertex(self, label, style, x, y, w, h):
        i = self._id()
        self.add(f'<mxCell id="{i}" value="{html.escape(label, quote=True)}" style="{style}" '
                 f'vertex="1" parent="1"><mxGeometry x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" '
                 f'height="{h:.0f}" as="geometry"/></mxCell>')
        return i

    def xml(self):
        return ('<mxfile host="gen_ii3_drawio.py" type="device">'
                f'<diagram id="{self.name}" name="{html.escape(self.name)}">'
                '<mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" '
                'connect="1" arrows="1" fold="1" page="1" pageScale="1" '
                f'pageWidth="{self.page_w}" pageHeight="{self.page_h}" math="0" shadow="0"><root>'
                '<mxCell id="0"/><mxCell id="1" parent="0"/>'
                + "".join(self.cells) + '</root></mxGraphModel></diagram></mxfile>\n')


def class_size(name, shared):
    if shared:
        w = max(len(name) * NAME_W + 24, 150)
        return round(w / 10) * 10 + 10, 44
    attrs = CLASSES[name]
    w = max(len(name) * NAME_W + 24, max(len(a) for a in attrs) * CHAR_W + 18)
    return round(w / 10) * 10 + 10, 32 + LINE_H * len(attrs) + 4


def class_label(name, shared):
    head = f'<p style="margin:0px;margin-top:5px;text-align:center;"><b>{name}</b></p>'
    if shared:
        f = FIG[OWNER[name]]
        return head + (f'<p style="margin:0px;text-align:center;font-size:10px;">'
                       f'<i>dùng chung – Hình {f}</i></p>')
    body = "<br>".join(html.escape(a) for a in CLASSES[name])
    return head + '<hr size="1"/>' + f'<p style="margin:0px;margin-left:6px;">{body}</p>'


S_CLASS = ("verticalAlign=top;align=left;overflow=fill;html=1;whiteSpace=wrap;fontSize=11;"
           "strokeColor=#333333;" + FONT)


def place(doc, name, cx, cy, shared=False):
    w, h = class_size(name, shared)
    x, y = cx - w / 2, cy - h / 2
    fill = "fillColor=#E6E6E6;dashed=1;" if shared else "fillColor=#FFFFFF;"
    i = doc.vertex(class_label(name, shared), S_CLASS + fill, x, y, w, h)
    doc.box[name] = (x, y, w, h, i)


def port(box, side, f):
    x, y, w, h, _ = box
    return {"L": (x, y + f * h), "R": (x + w, y + f * h),
            "T": (x + f * w, y), "B": (x + f * w, y + h)}[side]


SIDE_EXIT = {"L": ("0", None), "R": ("1", None), "T": (None, "0"), "B": (None, "1")}


def edge(doc, a, b, ma, mb, kind="--", label="", sa="R", sb="L", fa=0.5, fb=0.5, mid=None,
         points=None, lx=0):
    """a, b: tên lớp. kind: '--' liên kết, '*--' hợp thành (a là toàn thể), 'o--' kết tập.
    sa/sb: cạnh ra/vào; fa/fb: vị trí trên cạnh. mid: toạ độ đoạn giữa khi cần gấp hai lần."""
    A, B = doc.box[a], doc.box[b]
    p1, p2 = port(A, sa, fa), port(B, sb, fb)
    if points is None:
        points = []
        horiz = {sa, sb} <= {"L", "R"}
        vert = {sa, sb} <= {"T", "B"}
        if horiz and abs(p1[1] - p2[1]) > 1:
            m = mid if mid is not None else (p1[0] + p2[0]) / 2
            points = [(m, p1[1]), (m, p2[1])]
        elif vert and abs(p1[0] - p2[0]) > 1:
            m = mid if mid is not None else (p1[1] + p2[1]) / 2
            points = [(p1[0], m), (p2[0], m)]
        elif not horiz and not vert:
            points = [(p2[0], p1[1])] if sa in "LR" else [(p1[0], p2[1])]
    start = {"*--": "startArrow=diamondThin;startFill=1;startSize=14;",
             "o--": "startArrow=diamondThin;startFill=0;startSize=14;"}.get(kind, "startArrow=none;")
    ex = "exitX={};exitY={};".format(*(([1, 0][sa == "L"], fa) if sa in "LR" else (fa, [1, 0][sa == "T"])))
    en = "entryX={};entryY={};".format(*(([1, 0][sb == "L"], fb) if sb in "LR" else (fb, [1, 0][sb == "T"])))
    style = ("edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;strokeColor=#333333;"
             "fontSize=10;labelBackgroundColor=#FFFFFF;" + FONT + start + ex + en)
    i = doc._id()
    pts = "".join(f'<mxPoint x="{x:.0f}" y="{y:.0f}"/>' for x, y in points)
    pts = f'<Array as="points">{pts}</Array>' if pts else ""
    sid, tid = A[4], B[4]
    doc.add(f'<mxCell id="{i}" value="{html.escape(label, quote=True)}" style="{style}" edge="1" '
            f'parent="1" source="{sid}" target="{tid}"><mxGeometry x="{lx}" relative="1" '
            f'as="geometry">{pts}</mxGeometry></mxCell>')
    for end, m, side in ((-1, ma, sa), (1, mb, sb)):
        if not m:
            continue
        dx, dy, al, va = {"R": (6, -2, "left", "bottom"), "L": (-6, -2, "right", "bottom"),
                          "T": (5, -4, "left", "bottom"), "B": (5, 4, "left", "top")}[side]
        if kind != "--" and end == -1 and side in "LR":
            dx += 12 if side == "R" else -12
        if kind != "--" and end == -1 and side in "TB":
            dy += -10 if side == "T" else 10
        j = doc._id()
        doc.add(f'<mxCell id="{j}" value="{html.escape(m)}" style="edgeLabel;html=1;align={al};'
                f'verticalAlign={va};fontSize=11;resizable=0;points=[];labelBackgroundColor=none;'
                f'{FONT}" vertex="1" connectable="0" parent="{i}"><mxGeometry x="{end}" '
                f'relative="1" as="geometry"><mxPoint x="{dx}" y="{dy}" as="offset"/></mxGeometry></mxCell>')


def note(doc, text, x, y, w=520):
    doc.vertex(text, "text;html=1;align=left;verticalAlign=top;fontSize=10;fontStyle=2;"
               "whiteSpace=wrap;" + FONT, x, y, w, 30)


LEGEND = "Lớp nền xám, viền nét đứt: lớp dùng chung, thuộc tính xem ở hình ghi trong lớp."


def grid(cols, rows):
    return lambda c, r: (cols[c], rows[r])


# ---------------------------------------------------------------- các hình
def fig_A():
    d = Doc("II.3-2 Nhu cau va nang luc")
    g = grid([120, 380, 640, 900], [80, 250, 420, 590, 750])
    for n, (c, r) in {"DuAn": (0, 0), "NhuCauNguonLuc": (1, 0), "PhanHoiNhuCau": (2, 0),
                      "GiaiDoanDuAn": (0, 1), "ViTriCanBoTri": (1, 1),
                      "YeuCauKyNang": (1, 2), "KyNang": (2, 2), "NangLucKyNang": (3, 2),
                      "MucDoNangLuc": (1, 3), "TieuChiNangLuc": (2, 3), "HoSoNangLuc": (3, 3),
                      "BoTieuChiNangLuc": (2, 4), "NguonLuc": (3, 4)}.items():
        place(d, n, *g(c, r))
    edge(d, "DuAn", "NhuCauNguonLuc", "1", "0..*")
    edge(d, "NhuCauNguonLuc", "PhanHoiNhuCau", "1", "0..*")
    edge(d, "DuAn", "GiaiDoanDuAn", "1", "0..*", "*--", sa="B", sb="T")
    edge(d, "NhuCauNguonLuc", "ViTriCanBoTri", "1", "1..*", "*--", sa="B", sb="T")
    edge(d, "ViTriCanBoTri", "GiaiDoanDuAn", "0..*", "0..1", sa="L", sb="R")
    edge(d, "ViTriCanBoTri", "YeuCauKyNang", "1", "0..*", "*--", sa="B", sb="T")
    edge(d, "YeuCauKyNang", "KyNang", "0..*", "1")
    edge(d, "NangLucKyNang", "KyNang", "0..*", "1", sa="L", sb="R")
    edge(d, "HoSoNangLuc", "NangLucKyNang", "1", "0..*", "*--", sa="T", sb="B")
    edge(d, "NguonLuc", "HoSoNangLuc", "1", "1", sa="T", sb="B")
    edge(d, "TieuChiNangLuc", "KyNang", "0..*", "0..1", sa="T", sb="B")
    edge(d, "TieuChiNangLuc", "MucDoNangLuc", "1", "1..*", "*--", sa="L", sb="R")
    edge(d, "BoTieuChiNangLuc", "TieuChiNangLuc", "1", "1..*", "o--", sa="T", sb="B")
    note(d, LEGEND, 20, 820)
    return d


def fig_B():
    d = Doc("II.3-3 Tim kiem kha nang tham gia va lich")
    g = grid([120, 400, 680, 960], [70, 230, 410, 650, 860, 1030])
    for n, (c, r), s in [("NhuCauNguonLuc", (0, 0), 1), ("BoTieuChiPhuHop", (1, 0), 0),
                         ("TieuChiPhuHop", (2, 0), 0), ("PhienTimKiem", (1, 1), 0),
                         ("DiemTieuChi", (2, 1), 0), ("DeNghiMienTru", (3, 1), 0),
                         ("NguonLuc", (0, 2), 1), ("KetQuaDanhGiaPhuHop", (1, 2), 0),
                         ("LichNguonLuc", (0, 3), 0), ("KetLuanKhaNangThamGia", (1, 3), 0),
                         ("DeXuatThamGiaMotPhan", (2, 3), 0), ("PhanBoNguonLuc", (0, 4), 0),
                         ("HoSoVuotTaiNgoaiLe", (1, 4), 0), ("DuAn", (0, 5), 1),
                         ("YeuCauNguonLuc", (2, 5), 0)]:
        place(d, n, *g(c, r), shared=bool(s))
    edge(d, "NhuCauNguonLuc", "BoTieuChiPhuHop", "1", "0..*")
    edge(d, "BoTieuChiPhuHop", "TieuChiPhuHop", "1", "1..*", "*--")
    edge(d, "BoTieuChiPhuHop", "PhienTimKiem", "1", "0..*", sa="B", sb="T")
    edge(d, "PhienTimKiem", "KetQuaDanhGiaPhuHop", "1", "0..*", "*--", sa="B", sb="T")
    edge(d, "KetQuaDanhGiaPhuHop", "NguonLuc", "0..*", "1", sa="L", sb="R")
    edge(d, "KetQuaDanhGiaPhuHop", "DiemTieuChi", "1", "0..*", "*--", sa="R", sb="B", fa=0.3)
    edge(d, "DiemTieuChi", "TieuChiPhuHop", "0..*", "1", sa="T", sb="B")
    edge(d, "KetQuaDanhGiaPhuHop", "DeNghiMienTru", "1", "0..1", sa="R", sb="B", fa=0.7)
    edge(d, "DeNghiMienTru", "TieuChiPhuHop", "0..*", "1..*", label="điều kiện được miễn",
         sa="T", sb="R", lx=0.45)
    edge(d, "NguonLuc", "LichNguonLuc", "1", "1", sa="B", sb="T")
    edge(d, "LichNguonLuc", "PhanBoNguonLuc", "1", "0..*", "*--", sa="B", sb="T")
    edge(d, "PhanBoNguonLuc", "DuAn", "0..*", "1", sa="B", sb="T")
    edge(d, "KetQuaDanhGiaPhuHop", "KetLuanKhaNangThamGia", "1", "0..1", label="shortlist",
         sa="B", sb="T")
    edge(d, "KetLuanKhaNangThamGia", "DeXuatThamGiaMotPhan", "1", "0..*")
    edge(d, "KetLuanKhaNangThamGia", "HoSoVuotTaiNgoaiLe", "1", "0..*", sa="B", sb="T")
    edge(d, "DuAn", "YeuCauNguonLuc", "1", "0..*")
    edge(d, "YeuCauNguonLuc", "KetLuanKhaNangThamGia", "1", "0..*", sa="T", sb="R", fb=0.8)
    note(d, LEGEND, 20, 1130)
    return d


def fig_C():
    d = Doc("II.3-4 Phuong an xung dot va phe duyet")
    g = grid([120, 370, 640, 910, 1170], [50, 220, 410, 600, 800])
    for n, (c, r), s in [("YeuCauGiaiTrinh", (3, 0), 0),
                         ("DeXuatThayDoi", (1, 1), 0), ("NhuCauNguonLuc", (2, 1), 1),
                         ("HoSoTrinhDuyet", (3, 1), 0), ("QuyetDinhPheDuyet", (4, 1), 0),
                         ("RuiRoViTri", (1, 2), 0), ("PhuongAnBoTri", (2, 2), 0),
                         ("DiemXungDot", (3, 2), 0), ("NhatKyXuLyXungDot", (4, 2), 0),
                         ("ViTriCanBoTri", (1, 3), 1), ("ChiTietBoTri", (2, 3), 0),
                         ("NguonLuc", (3, 3), 1), ("PhanXuXungDot", (4, 3), 0),
                         ("KetLuanKhaNangThamGia", (1, 4), 1), ("PhanBoNguonLuc", (2, 4), 1),
                         ("GiaiDoanDuAn", (3, 4), 1)]:
        place(d, n, *g(c, r), shared=bool(s))
    edge(d, "NhuCauNguonLuc", "PhuongAnBoTri", "1", "0..*", sa="B", sb="T")
    edge(d, "PhuongAnBoTri", "DeXuatThayDoi", "1", "0..*", sa="T", sb="B", fa=0.15)
    edge(d, "PhuongAnBoTri", "HoSoTrinhDuyet", "1", "0..*", sa="T", sb="B", fa=0.85)
    edge(d, "HoSoTrinhDuyet", "YeuCauGiaiTrinh", "1", "0..*", "*--", sa="T", sb="B")
    edge(d, "HoSoTrinhDuyet", "QuyetDinhPheDuyet", "1", "0..1")
    edge(d, "PhuongAnBoTri", "RuiRoViTri", "1", "0..*", sa="L", sb="R")
    edge(d, "RuiRoViTri", "ViTriCanBoTri", "0..*", "1", sa="B", sb="T")
    edge(d, "PhuongAnBoTri", "DiemXungDot", "1", "0..*")
    edge(d, "DiemXungDot", "NhatKyXuLyXungDot", "1", "1..*", "*--")
    edge(d, "DiemXungDot", "NguonLuc", "0..*", "1", sa="B", sb="T")
    edge(d, "DiemXungDot", "PhanXuXungDot", "1", "0..1", sa="B", sb="T", fa=0.85)
    edge(d, "PhuongAnBoTri", "ChiTietBoTri", "1", "1..*", "*--", sa="B", sb="T")
    edge(d, "ChiTietBoTri", "ViTriCanBoTri", "0..*", "1", sa="L", sb="R")
    edge(d, "ChiTietBoTri", "NguonLuc", "0..*", "1")
    edge(d, "ChiTietBoTri", "KetLuanKhaNangThamGia", "0..*", "0..1", sa="B", sb="T", fa=0.15,
         mid=700)
    edge(d, "ChiTietBoTri", "PhanBoNguonLuc", "0..1", "0..1", label="Locked Baseline<br>tạo phân bổ cứng",
         sa="B", sb="T")
    edge(d, "ChiTietBoTri", "GiaiDoanDuAn", "0..*", "0..1", label="theo giai đoạn",
         sa="B", sb="T", fa=0.85, mid=700)
    note(d, LEGEND, 20, 860)
    return d


def fig_D():
    d = Doc("II.3-5 Chi phi va ngan sach")
    g = grid([130, 400, 680, 960], [50, 200, 400, 600, 770])
    for n, (c, r), s in [("ChiTietBoTri", (0, 0), 1), ("DonGia", (1, 0), 0),
                         ("DuToanChiPhi", (1, 1), 0), ("DuBaoChiPhi", (2, 1), 0),
                         ("HoSoTrinhDuyet", (3, 1), 1),
                         ("PhuongAnBoTri", (0, 2), 1), ("DanhGiaChiPhi", (2, 2), 0),
                         ("NguyenNhanVuot", (3, 2), 0),
                         ("ChiTietSoSanh", (0, 3), 0), ("SoSanhPhuongAn", (1, 3), 0),
                         ("NganSach", (2, 3), 0), ("HuongXuLy", (3, 3), 0),
                         ("ChiPhiThucTe", (1, 4), 0), ("DuAn", (3, 4), 1)]:
        place(d, n, *g(c, r), shared=bool(s))
    edge(d, "ChiTietBoTri", "DonGia", "0..*", "1")
    edge(d, "PhuongAnBoTri", "DuToanChiPhi", "1", "0..1", sa="T", sb="L", fa=0.3)
    edge(d, "DuToanChiPhi", "DuBaoChiPhi", "1", "0..*")
    edge(d, "PhuongAnBoTri", "DanhGiaChiPhi", "1", "0..*")
    edge(d, "DanhGiaChiPhi", "DuToanChiPhi", "0..*", "1", label="căn cứ chi phí",
         sa="T", sb="B", fa=0.15)
    edge(d, "DanhGiaChiPhi", "DuBaoChiPhi", "0..*", "0..1", label="tham chiếu khi có",
         sa="T", sb="B")
    edge(d, "HoSoTrinhDuyet", "DanhGiaChiPhi", "0..*", "0..*", label="tham chiếu",
         sa="B", sb="T", fb=0.85)
    edge(d, "DanhGiaChiPhi", "NguyenNhanVuot", "1", "0..*", "*--")
    edge(d, "DanhGiaChiPhi", "HuongXuLy", "1", "0..1", "*--", sa="B", sb="T", fa=0.85)
    edge(d, "DanhGiaChiPhi", "SoSanhPhuongAn", "1", "0..1", sa="B", sb="T", fa=0.15)
    edge(d, "SoSanhPhuongAn", "ChiTietSoSanh", "1", "2..*", "*--", sa="L", sb="R")
    edge(d, "ChiTietSoSanh", "PhuongAnBoTri", "0..*", "1", sa="T", sb="B")
    edge(d, "DanhGiaChiPhi", "NganSach", "0..*", "1", sa="B", sb="T")
    edge(d, "NganSach", "ChiPhiThucTe", "1", "0..*", sa="B", sb="R", fa=0.2)
    edge(d, "PhuongAnBoTri", "ChiPhiThucTe", "1", "0..*", sa="L", sb="L",
         points=[(20, 400), (20, 770)])
    edge(d, "DuAn", "NganSach", "1", "0..*", sa="L", sb="B", fb=0.8)
    note(d, LEGEND, 20, 840)
    return d


def fig_E():
    d = Doc("II.3-6 Theo doi va du bao")
    g = grid([150, 450, 760], [60, 230, 450, 620])
    for n, (c, r), s in [("PhanHoiNhuCau", (1, 0), 1), ("HoSoTrinhDuyet", (2, 0), 1),
                         ("TongHopNguonCung", (0, 1), 0), ("KetQuaDuBao", (1, 1), 0),
                         ("DongDoiChieuCungCau", (2, 1), 0),
                         ("NguonLuc", (0, 2), 1), ("NhuCauDuBao", (1, 2), 0), ("DuAn", (2, 2), 1),
                         ("NhuCauNguonLuc", (1, 3), 1)]:
        place(d, n, *g(c, r), shared=bool(s))
    edge(d, "PhanHoiNhuCau", "KetQuaDuBao", "0..*", "0..1", sa="B", sb="T")
    edge(d, "HoSoTrinhDuyet", "KetQuaDuBao", "0..*", "0..1", label="tham chiếu", sa="B", sb="T", fb=0.85)
    edge(d, "KetQuaDuBao", "TongHopNguonCung", "1", "0..*", "*--", sa="L", sb="R")
    edge(d, "KetQuaDuBao", "DongDoiChieuCungCau", "1", "0..*", "*--")
    edge(d, "KetQuaDuBao", "NhuCauDuBao", "1", "0..*", "*--", sa="B", sb="T")
    edge(d, "TongHopNguonCung", "NguonLuc", "0..*", "1", sa="B", sb="T")
    edge(d, "NhuCauDuBao", "NhuCauNguonLuc", "0..*", "0..1", sa="B", sb="T")
    edge(d, "NhuCauDuBao", "DuAn", "0..*", "1", label="nhu cầu theo dự án")
    note(d, LEGEND, 20, 680)
    return d


def fig_overview():
    d = Doc("II.3-1 Tong quan cac goi lop")
    S = ("rounded=0;whiteSpace=wrap;html=1;verticalAlign=top;align=left;spacingLeft=8;"
         "spacingTop=4;fontSize=11;strokeColor=#333333;fillColor=#FFFFFF;" + FONT)
    L, W, MW, GAP = 230, 1000, 310, 35
    pos = {"A": (L, 20, W, 100), "B": (L, 220, MW, 140), "D": (L + MW + GAP, 220, MW, 140),
           "E": (L + 2 * (MW + GAP), 220, MW, 140), "C": (L, 460, W, 100)}
    ids = {}
    for k, f, name, v, cs in CLUSTERS:
        x, y, w, h = pos[k]
        per = 6 if w > 600 else 2
        rows = [cs[i:i + per] for i in range(0, len(cs), per)]
        body = "<br>".join(" · ".join(r) for r in rows)
        ids[k] = d.vertex(f"<b>Gói {k}. {name} ({v})</b> – chi tiết Hình {f}"
                          f'<hr size="1"/>{body}', S, x, y, w, h)
    S_DEP = ("edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;dashed=1;endArrow=open;endFill=0;"
             "endSize=10;strokeColor=#333333;fontSize=10;labelBackgroundColor=#FFFFFF;" + FONT)

    def fx(k, x):
        return f"{(x - pos[k][0]) / pos[k][2]:.4f}"

    def dep(a, b, label, ex, en, pts=()):
        i = d._id()
        p = "".join(f'<mxPoint x="{x}" y="{y}"/>' for x, y in pts)
        p = f'<Array as="points">{p}</Array>' if p else ""
        d.add(f'<mxCell id="{i}" value="{html.escape(label, quote=True)}" style="{S_DEP}{ex}{en}" '
              f'edge="1" parent="1" source="{ids[a]}" target="{ids[b]}"><mxGeometry relative="1" '
              f'as="geometry">{p}</mxGeometry></mxCell>')

    for k, lab in (("B", "NhuCauNguonLuc, NguonLuc, DuAn"), ("D", "DuAn"),
                   ("E", "NguonLuc, NhuCauNguonLuc,<br>PhanHoiNhuCau, DuAn")):
        cx = pos[k][0] + pos[k][2] / 2
        dep(k, "A", lab, "exitX=0.5;exitY=0;", f"entryX={fx('A', cx)};entryY=1;")
    cx = pos["B"][0] + pos["B"][2] / 2
    dep("C", "B", "KetLuanKhaNangThamGia,<br>PhanBoNguonLuc", f"exitX={fx('C', cx)};exitY=0;",
        "entryX=0.5;entryY=1;")
    for k, lab in (("D", "PhuongAnBoTri, ChiTietBoTri,<br>HoSoTrinhDuyet"), ("E", "HoSoTrinhDuyet")):
        cx = pos[k][0] + pos[k][2] / 2
        dep(k, "C", lab, "exitX=0.5;exitY=1;", f"entryX={fx('C', cx)};entryY=0;")
    dep("C", "A", "", "exitX=0;exitY=0.5;", "entryX=0;entryY=0.5;", pts=[(L - 30, 510), (L - 30, 70)])
    d.vertex("NhuCauNguonLuc, ViTriCanBoTri,<br>NguonLuc, GiaiDoanDuAn",
             "text;html=1;align=right;verticalAlign=middle;fontSize=10;whiteSpace=wrap;" + FONT,
             10, 270, L - 50, 40)
    note(d, "Mũi tên nét đứt (phụ thuộc): gói ở gốc mũi tên có quan hệ tới các lớp ghi cạnh mũi "
            "tên, thuộc gói ở đầu mũi tên.", L, 575, W)
    return d


def main(out):
    os.makedirs(out, exist_ok=True)
    figs = {"II3-1_Tong_quan_goi_lop": fig_overview(), "II3-2_Nhu_cau_va_nang_luc": fig_A(),
            "II3-3_Tim_kiem_kha_nang_tham_gia_lich": fig_B(),
            "II3-4_Phuong_an_xung_dot_phe_duyet": fig_C(),
            "II3-5_Chi_phi_ngan_sach": fig_D(), "II3-6_Theo_doi_du_bao": fig_E()}
    for n, d in figs.items():
        with open(os.path.join(out, n + ".drawio"), "w", encoding="utf-8") as f:
            f.write(d.xml())
        print(n)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else
         os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "04_DRAWIO", "II.3"))
