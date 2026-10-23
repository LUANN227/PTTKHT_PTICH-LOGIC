"""Sinh lại Activity Diagram của các UC trọng tâm dạng draw.io gốc, theo UC Description đã sửa
trong bài thành viên (bai_goc_da_sua/). Bố cục đặt tay; mỗi AD một hàm.

    python3 gen_ad.py <thư mục ra>
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ad_lib import AD  # noqa: E402

ADS = {}


def ad(fn):
    ADS[fn.__name__.replace("ad_", "AD_UC-").replace("_", ".", 1).replace("UC-.", "UC-")] = fn
    return fn


def reg(code):
    def wrap(fn):
        ADS[code] = fn
        return fn
    return wrap


# ------------------------------------------------------------------ V2a
@reg("AD_UC-01.1")
def ad_0101():
    d = AD("AD UC-01.1", [("PM", 400), ("Hệ thống", 380)], 1170,
           title="AD UC-01.1 Xây dựng và hoàn thiện nhu cầu")
    P, H = "PM", "Hệ thống"
    d.add("s", "start", P, 85)
    d.add("a1", "action", P, 145, "1. Chọn dự án; xem bối cảnh, công việc, kế hoạch giai đoạn")
    d.add("a2", "action", H, 145, "2. Hiển thị thông tin dự án, công việc và các mốc thời gian")
    d.add("m1", "merge", P, 225)
    d.add("a3", "action", P, 290, "3. Xác lập phạm vi công việc cần nguồn lực")
    d.add("a4", "action", H, 290, "4. Kiểm tra thông tin dự án và phạm vi")
    d.add("d1", "decision", H, 390, "Đủ để hiểu công việc, giai đoạn, thời gian?")
    d.add("x1", "action", P, 390, "A1. Yêu cầu bổ sung thông tin dự án hoặc điều chỉnh phạm vi; "
          "nhu cầu chưa cố định", w=260, dx=-40)
    d.add("a5", "action", P, 500, "5. Xác định loại nguồn lực, yêu cầu chuyên môn, kỹ năng cho "
          "từng công việc", w=270)
    d.add("a6", "action", P, 585, "6. Xác định quy mô FTE theo từng giai đoạn")
    d.add("m2", "merge", P, 655)
    d.add("a7", "action", P, 720, "7. Xác định thời gian hoặc giai đoạn và mức tham gia %FTE "
          "của từng vị trí", w=270)
    d.add("d2", "decision", H, 720, "Thời gian và %FTE hợp lệ?")
    d.add("a8", "action", P, 840, "8. Rà soát toàn bộ nhu cầu và lưu")
    d.add("a9", "action", H, 840, "9. Lưu nhu cầu, trạng thái “Đang xây dựng”")
    d.add("d3", "decision", P, 950, "Nhu cầu đã hoàn thiện, chuyển RM?")
    d.add("f1", "final", P, 1040, dx=-140)
    d.add("a10", "action", P, 1060, "10. Chuyển nhu cầu đã hoàn thiện cho RM xem xét")
    d.add("a11", "action", H, 1060, "11. Ghi nhận nhu cầu ở trạng thái “Chờ xác nhận” (sang UC-01.2)")
    d.add("f2", "final", H, 1150)
    d.flow("s", "a1")
    d.flow("a1", "a2", "R", "L")
    d.flow("a2", "m1", "B", "R", points=[(d.lane[H], 225)])
    d.flow("m1", "a3")
    d.flow("a3", "a4", "R", "L")
    d.flow("a4", "d1")
    d.flow("d1", "x1", "L", "R", guard="Chưa đủ", lx=-0.1)
    d.flow("x1", "m1", "T", "L", points=[(d.node["x1"][0] + 130, 225)])
    d.flow("d1", "a5", "B", "T", guard="Đủ", points=[(d.lane[H], 455), (d.lane[P], 455)], lx=-0.85)
    d.flow("a5", "a6")
    d.flow("a6", "m2")
    d.flow("m2", "a7")
    d.flow("a7", "d2", "R", "L")
    d.flow("d2", "m2", "T", "R", guard="Không hợp lệ (E1)", points=[(d.lane[H], 655)], lx=-0.4)
    d.flow("d2", "a8", "B", "T", guard="Hợp lệ", points=[(d.lane[H], 790), (d.lane[P], 790)], lx=-0.8)
    d.flow("a8", "a9", "R", "L")
    d.flow("a9", "d3", "B", "R", points=[(d.lane[H], 950)])
    d.flow("d3", "f1", "L", "T", guard="Chưa (A2)", lx=-0.2)
    d.flow("d3", "a10", guard="Đã hoàn thiện", lx=-0.4)
    d.flow("a10", "a11", "R", "L")
    d.flow("a11", "f2")
    return d


# ------------------------------------------------------------------ V2b
@reg("AD_UC-01.2")
def ad_0102():
    d = AD("AD UC-01.2", [("RM", 560), ("Hệ thống", 380)], 830,
           title="AD UC-01.2 Xác nhận nhu cầu")
    R, H = "RM", "Hệ thống"
    M, B = -130, 140
    d.add("s", "start", R, 85, dx=M)
    d.add("a1", "action", R, 145, "1. Tiếp nhận nhu cầu nguồn lực đã hoàn thiện cần xem xét", dx=M)
    d.add("a2", "action", H, 145, "2. Hiển thị thông tin nhu cầu nguồn lực")
    d.add("a3", "action", R, 250, "3. Xem xét nhu cầu, đánh giá mức đáp ứng điều kiện xác nhận", dx=M)
    d.add("d1", "decision", R, 350, "Nhu cầu đủ điều kiện?", dx=M)
    d.add("x1", "action", R, 350, "A1. Ghi nhận nội dung cần bổ sung, điều chỉnh", dx=B, w=230)
    d.add("x2", "action", H, 350, "A1. Chuyển lại nhu cầu cho PM, trạng thái “Cần tiếp tục hoàn thiện” "
          "(PM xử lý ở UC-01.3)", w=270)
    d.add("f1", "final", H, 440)
    d.add("a4", "action", R, 540, "4. Xác nhận nhu cầu đủ điều kiện", dx=M)
    d.add("a5", "action", H, 540, "5. Ghi nhận kết quả, cập nhật trạng thái “Đã xác nhận”")
    d.add("a6", "action", R, 650, "6. Bàn giao nhu cầu đã xác nhận cho V3 và V4", dx=M)
    d.add("a7", "action", H, 760, "7. Chuyển nhu cầu “Đã xác nhận” sang V3 và V4")
    d.add("f2", "final", H, 850)
    xm = d.lane[R] + M
    d.flow("s", "a1")
    d.flow("a1", "a2", "R", "L")
    d.flow("a2", "a3", "B", "R", points=[(d.lane[H], 250)])
    d.flow("a3", "d1")
    d.flow("d1", "x1", "R", "L", guard="Chưa đủ", lx=-0.3)
    d.flow("x1", "x2", "R", "L")
    d.flow("x2", "f1")
    d.flow("d1", "a4", guard="Đủ", lx=-0.6)
    d.flow("a4", "a5", "R", "L")
    d.flow("a5", "a6", "B", "R", points=[(d.lane[H], 650)])
    d.flow("a6", "a7", "B", "L", points=[(xm, 760)])
    d.flow("a7", "f2")
    return d


@reg("AD_UC-01.3")
def ad_0103():
    d = AD("AD UC-01.3", [("PM", 560), ("Hệ thống", 380)], 830,
           title="AD UC-01.3 Điều chỉnh nhu cầu theo phản hồi")
    P, H = "PM", "Hệ thống"
    M, B = -130, 140
    d.add("s", "start", P, 85, dx=M)
    d.add("a1", "action", P, 150, "1. Tra cứu nhu cầu hiện tại và phản hồi: yêu cầu bổ sung của RM "
          "(từ UC-01.2), phản hồi V4 hoặc thông tin V10", dx=M, w=260)
    d.add("a2", "action", H, 150, "2. Hiển thị nhu cầu hiện tại và phản hồi đã ghi nhận")
    d.add("a3", "action", P, 255, "3. Xem xét phản hồi, xác định nội dung cần điều chỉnh", dx=M)
    d.add("d1", "decision", P, 345, "Nhu cầu cần điều chỉnh?", dx=M)
    d.add("x1", "action", P, 345, "A1. Giữ nguyên nhu cầu hiện tại", dx=B, w=200)
    d.add("f1", "final", P, 415, dx=B)
    d.add("m1", "merge", P, 465, dx=M)
    d.add("a4", "action", P, 540, "4. Điều chỉnh loại nguồn lực, quy mô FTE, thời gian hoặc giai "
          "đoạn, %FTE", dx=M, w=260)
    d.add("a5", "action", H, 540, "5. Kiểm tra và lưu thông tin điều chỉnh")
    d.add("d2", "decision", H, 650, "Thông tin hợp lệ?")
    d.add("a6", "action", P, 650, "6. Gửi lại nhu cầu cho RM xem xét", dx=M)
    d.add("a7", "action", H, 770, "7. Ghi nhận nhu cầu ở trạng thái “Chờ xác nhận” (sang UC-01.2)")
    d.add("f2", "final", H, 855)
    xm = d.lane[P] + M
    d.flow("s", "a1")
    d.flow("a1", "a2", "R", "L")
    d.flow("a2", "a3", "B", "R", points=[(d.lane[H], 255)])
    d.flow("a3", "d1")
    d.flow("d1", "x1", "R", "L", guard="Không (A1)", lx=-0.3)
    d.flow("x1", "f1")
    d.flow("d1", "m1", guard="Có", lx=-0.5)
    d.flow("m1", "a4")
    d.flow("a4", "a5", "R", "L")
    d.flow("a5", "d2")
    d.flow("d2", "m1", "R", "R", guard="Không (E1)", lx=-0.75,
           points=[(d.lane[H] + 170, 650), (d.lane[H] + 170, 465)])
    d.flow("d2", "a6", "L", "R", guard="Hợp lệ", lx=-0.5)
    d.flow("a6", "a7", "B", "L", points=[(xm, 770)])
    d.flow("a7", "f2")
    return d


# ------------------------------------------------------------------ V3
@reg("AD_UC-02.1")
def ad_0201():
    d = AD("AD UC-02.1", [("RM", 440), ("Hệ thống", 600), ("PMO/Quản lý danh mục", 300)], 1220,
           title="AD UC-02.1 Quản lý tiêu chí đánh giá năng lực")
    R, H, Q = "RM", "Hệ thống", "PMO/Quản lý danh mục"
    M, B = -130, 150
    d.add("s", "start", R, 85)
    d.add("a1", "action", R, 145, "1. Yêu cầu quản lý tiêu chí đánh giá năng lực")
    d.add("a2", "action", H, 145, "2. Cung cấp bộ tiêu chí hiện hành: kỹ năng, tiêu chí, thang 5 mức, "
          "điều kiện", dx=M, w=270)
    d.add("m1", "merge", R, 235)
    d.add("a3", "action", R, 300, "3. Xác định nội dung thay đổi")
    d.add("dA", "decision", R, 400, "Kỹ năng chưa có tiêu chí?")
    d.add("x1", "action", H, 400, "A3. Ghi tiêu chí tạm ở trạng thái chờ phê duyệt", dx=B, w=230)
    d.add("x2", "action", Q, 400, "A3. Phê duyệt hoặc từ chối tiêu chí tạm", w=240)
    d.add("fq", "final", Q, 490)
    d.add("a4", "action", H, 510, "4. Kiểm tra tính hợp lệ của nội dung thay đổi", dx=M)
    d.add("d1", "decision", H, 610, "Hợp lệ?", dx=M)
    d.add("d2", "decision", H, 720, "Ngừng áp dụng tiêu chí đang dùng?", dx=M)
    d.add("xa1", "action", H, 720, "A1. Chuyển tiêu chí sang ngừng áp dụng thay vì xóa", dx=B, w=230)
    d.add("a5", "action", H, 820, "5. Xử lý thay đổi theo loại yêu cầu, trình RM xem xét", dx=M)
    d.add("m2", "merge", H, 900, dx=M)
    d.add("a6", "action", R, 900, "6. Xem xét và xác nhận lưu thay đổi")
    d.add("d3", "decision", R, 1000, "Xác nhận lưu?")
    d.add("a7", "action", H, 1000, "7. Lưu thay đổi, ghi người thực hiện, thời điểm, nội dung", dx=M)
    d.add("a8", "action", H, 1100, "8. Cập nhật bộ tiêu chí ở trạng thái sẵn sàng sử dụng", dx=M)
    d.add("xa2", "action", R, 1110, "A2. Hủy thay đổi, giữ nguyên bộ tiêu chí")
    d.add("fr", "final", R, 1190)
    d.add("fh", "final", H, 1190, dx=M)
    xh, xb, xr = d.lane[H] + M, d.lane[H] + B, d.lane[R]
    d.flow("s", "a1")
    d.flow("a1", "a2", "R", "L")
    d.flow("a2", "m1", "B", "R", points=[(xh, 235)])
    d.flow("m1", "a3")
    d.flow("a3", "dA")
    d.flow("dA", "x1", "R", "L", guard="Có (A3)", lx=-0.75)
    d.flow("x1", "x2", "R", "L")
    d.flow("x2", "fq")
    d.flow("dA", "a4", "B", "L", guard="Không", points=[(xr, 510)], lx=-0.8)
    d.flow("a4", "d1")
    d.flow("d1", "m1", "L", "L", guard="Không (E1): báo lỗi, sửa lại", lx=-0.3,
           points=[(xr - 180, 610), (xr - 180, 235)])
    d.flow("d1", "d2", guard="Hợp lệ", lx=-0.5)
    d.flow("d2", "xa1", "R", "L", guard="Có (A1)", lx=-0.5)
    d.flow("d2", "a5", guard="Không", lx=-0.5)
    d.flow("a5", "m2")
    d.flow("xa1", "m2", "B", "R", points=[(xb, 900)])
    d.flow("m2", "a6", "L", "R")
    d.flow("a6", "d3")
    d.flow("d3", "a7", "R", "L", guard="Có", lx=-0.7)
    d.flow("a7", "a8")
    d.flow("a8", "fh")
    d.flow("d3", "xa2", guard="Không (A2)", lx=-0.5)
    d.flow("xa2", "fr")
    return d


# ------------------------------------------------------------------ V4
@reg("AD_UC-03.3")
def ad_0303():
    d = AD("AD UC-03.3", [("RM", 440), ("Hệ thống", 600), ("PMO/Quản lý danh mục", 300)], 1600,
           title="AD UC-03.3 Đánh giá, xếp hạng và lập shortlist ứng viên")
    R, H, Q = "RM", "Hệ thống", "PMO/Quản lý danh mục"
    M, B = -90, 175
    xr, xh = d.lane[R], d.lane[H] + M
    d.add("s", "start", R, 85)
    d.add("a1", "action", R, 150, "1. Chọn nhu cầu đã xác nhận và danh sách ứng viên cần đánh giá")
    d.add("d0", "decision", H, 150, "Đủ tiền điều kiện?", dx=M)
    d.add("f0", "final", H, 150, dx=B + 40)
    d.add("a2", "action", H, 265, "2. Trình bày nhu cầu, ứng viên, điều kiện bắt buộc, tiêu chí, trọng số, "
          "năng lực từ hồ sơ tập trung", dx=M, w=290)
    d.add("a3", "action", R, 365, "3. Đối chiếu điều kiện bắt buộc; loại ứng viên xung đột lợi ích (A1)",
          w=270)
    d.add("a4", "action", H, 465, "4. Ghi phân loại và lý do không đạt; cảnh báo kỹ năng chưa xác nhận "
          "hoặc quá hạn (A3)", dx=M, w=290)
    d.add("dm", "decision", R, 575, "Cần miễn trừ ứng viên?")
    d.add("xa", "action", R, 690, "A2. Ghi đề nghị miễn trừ kèm lý do")
    d.add("xp", "action", Q, 690, "A2. Phê duyệt hoặc từ chối đề nghị miễn trừ", w=240)
    d.add("m", "merge", H, 790, dx=M)
    d.add("d1", "decision", H, 880, "Còn ứng viên đủ điều kiện?", dx=M)
    d.add("xe", "action", H, 880, "E3. Lưu phân loại, lý do loại; không lập shortlist (RM tìm tiếp ở "
          "UC-03.2)", dx=B, w=230)
    d.add("fe", "final", H, 970, dx=B)
    d.add("a6", "action", R, 1000, "6. Chấm điểm từng tiêu chí cho ứng viên đủ điều kiện")
    d.add("a7", "action", H, 1100, "7. Tính điểm tổng theo trọng số; xếp hạng; đồng hạng theo thứ tự ưu "
          "tiên nguồn (A4)", dx=M, w=290)
    d.add("a8", "action", R, 1200, "8. Lập shortlist: tối thiểu 1 ứng viên chính, khuyến nghị 1–2 thay thế "
          "(A5)", w=270)
    d.add("a9", "action", H, 1300, "9. Hiển thị mức đáp ứng và khoảng thiếu năng lực", dx=M)
    d.add("a10", "action", R, 1400, "10. Rà soát kết quả, xác nhận hoàn tất")
    d.add("a11", "action", H, 1500, "11. Lưu tiêu chí, trọng số, điểm, thứ hạng và shortlist", dx=M)
    d.add("f", "final", H, 1585, dx=M)
    d.flow("s", "a1")
    d.flow("a1", "d0", "R", "L")
    d.flow("d0", "f0", "R", "L", guard="Không (E1, E2)", lx=-0.4)
    d.flow("d0", "a2", guard="Đủ", lx=-0.5)
    d.flow("a2", "a3", "B", "R", points=[(xh, 365)])
    d.flow("a3", "a4", "B", "L", points=[(xr, 465)])
    d.flow("a4", "dm", "B", "R", points=[(xh, 575)])
    d.flow("dm", "xa", guard="Có (A2)", lx=-0.5)
    d.flow("xa", "xp", "R", "L")
    d.flow("xp", "m", "B", "R", points=[(d.lane[Q], 790)])
    d.flow("dm", "m", "L", "L", guard="Không", lx=-0.15,
           points=[(xr - 185, 575), (xr - 185, 790)])
    d.flow("m", "d1")
    d.flow("d1", "xe", "R", "L", guard="Không (E3)", lx=-0.6)
    d.flow("xe", "fe")
    d.flow("d1", "a6", "B", "R", guard="Có", points=[(xh, 1000)], lx=-0.8)
    d.flow("a6", "a7", "B", "L", points=[(xr, 1100)])
    d.flow("a7", "a8", "B", "R", points=[(xh, 1200)])
    d.flow("a8", "a9", "B", "L", points=[(xr, 1300)])
    d.flow("a9", "a10", "B", "R", points=[(xh, 1400)])
    d.flow("a10", "a11", "B", "L", points=[(xr, 1500)])
    d.flow("a11", "f")
    return d


# ------------------------------------------------------------------ V5
@reg("AD_UC-04.1")
def ad_0401():
    d = AD("AD UC-04.1", [("RM", 640), ("Hệ thống", 600)], 1520,
           title="AD UC-04.1 Đánh giá khả năng tham gia")
    R, H = "RM", "Hệ thống"
    C1, C2, HM, HB = -160, 160, -130, 150
    c1, c2, hm, hb = d.lane[R] + C1, d.lane[R] + C2, d.lane[H] + HM, d.lane[H] + HB
    d.add("s", "start", R, 85, dx=C1)
    d.add("a1", "action", R, 150, "1. Tiếp nhận yêu cầu nguồn lực, khung thời gian và shortlist từ V4",
          dx=C1, w=270)
    d.add("dg", "decision", R, 250, "Yêu cầu gấp, thời hạn dưới 24–48 giờ?", dx=C1, w=230)
    d.add("x6", "action", R, 250, "A6. Đánh giá nhanh theo phân bổ cứng, ghi nhận rủi ro, tiếp tục theo "
          "dõi", dx=C2, w=250)
    d.add("f6", "final", R, 330, dx=C2)
    d.add("m0", "merge", R, 380, dx=C1)
    d.add("a2", "action", H, 380, "2. Kiểm tra đầu vào: yêu cầu, khung thời gian, shortlist", dx=HM)
    d.add("d1", "decision", H, 480, "Đủ thông tin?", dx=HM)
    d.add("xa1", "action", R, 480, "A1. Yêu cầu bổ sung, xác nhận thông tin; chưa kết luận", dx=C2, w=250)
    d.add("ml", "merge", H, 570, dx=HM)
    d.add("a3", "action", H, 640, "3. Tra cứu năng lực chuẩn, lịch, nghỉ, phân bổ cứng và mềm của ứng "
          "viên; kiểm tra độ mới", dx=HM, w=270)
    d.add("dd", "decision", R, 740, "Dữ liệu đủ rõ?", dx=C1)
    d.add("xa2", "action", R, 740, "A2. Gắn nhãn “dữ liệu chưa đủ rõ”", dx=C2, w=250)
    d.add("dw", "decision", R, 845, "Chờ xác nhận?", dx=C2)
    d.add("xw", "action", H, 845, "A2. Đặt chờ xác nhận trong 2 ngày làm việc", dx=HB, w=230)
    d.add("xn", "action", H, 945, "A2. Coi như chưa có dữ liệu, gửi yêu cầu xác nhận ngay", dx=HM)
    d.add("a5", "action", R, 845, "4. Xác định năng lực khả dụng thực tế: năng lực chuẩn trừ nghỉ, không "
          "tính phí, phân bổ cứng", dx=C1, w=270)
    d.add("a6", "action", R, 945, "5. Đối chiếu mức sử dụng với 70–85%; trên 85% xem phần chờ xác nhận; "
          "trên 90% liên tục trên 2 tuần gắn cờ Mức 2", dx=C1, w=280)
    d.add("ma", "merge", H, 1030, dx=HM)
    d.add("mk", "merge", R, 1030, dx=C1)
    d.add("a7", "action", R, 1105, "6. Ghi nhận kết luận theo bốn trạng thái kèm căn cứ (dữ liệu chưa rõ: "
          "chờ xác nhận)", dx=C1, w=280)
    d.add("a8", "action", H, 1105, "7. Lưu kết luận và căn cứ của ứng viên", dx=HM)
    d.add("dm", "decision", H, 1205, "Còn ứng viên cần đánh giá?", dx=HM)
    d.add("a9", "action", R, 1305, "8. Tổng hợp kết luận của từng ứng viên, bàn giao", dx=C1)
    d.add("a10", "action", H, 1405, "9. Chuyển theo kết luận: đầy đủ → V6 (cờ Mức 2 kèm sang V6, V10); "
          "một phần → UC-04.2 (A4); vượt tải ngoại lệ → UC-04.3 (A5); trùng phân bổ cứng → V7 (A3)",
          dx=HM + 20, w=320)
    d.add("f", "final", H, 1495, dx=HM + 20)
    d.flow("s", "a1")
    d.flow("a1", "dg")
    d.flow("dg", "x6", "R", "L", guard="Có", lx=-0.5)
    d.flow("x6", "f6")
    d.flow("dg", "m0", guard="Không", lx=-0.4)
    d.flow("m0", "a2", "R", "L")
    d.flow("a2", "d1")
    d.flow("d1", "xa1", "L", "R", guard="Không (A1)", lx=-0.5)
    d.flow("xa1", "m0", "L", "B", points=[(c1, 480)])
    d.flow("d1", "ml", guard="Đủ", lx=-0.5)
    d.flow("ml", "a3")
    d.flow("a3", "dd", "L", "T", points=[(c1, 640)])
    d.flow("dd", "xa2", "R", "L", guard="Không (A2)", lx=-0.5)
    d.flow("xa2", "dw")
    d.flow("dw", "xw", "R", "L", guard="Chờ", lx=-0.6)
    d.flow("dw", "xn", "B", "L", guard="Không chờ", points=[(c2, 945)], lx=-0.9)
    d.flow("xn", "ma")
    d.flow("xw", "ma", "B", "R", points=[(hb, 1030)])
    d.flow("ma", "mk", "L", "R")
    d.flow("dd", "a5", guard="Đủ rõ", lx=-0.5)
    d.flow("a5", "a6")
    d.flow("a6", "mk")
    d.flow("mk", "a7")
    d.flow("a7", "a8", "R", "L")
    d.flow("a8", "dm")
    d.flow("dm", "ml", "R", "R", guard="Còn", lx=-0.9,
           points=[(d.lane[H] + 285, 1205), (d.lane[H] + 285, 570)])
    d.flow("dm", "a9", "B", "R", guard="Hết", points=[(hm, 1305)], lx=-0.8)
    d.flow("a9", "a10", "B", "L", points=[(c1, 1405)])
    d.flow("a10", "f")
    return d


# ------------------------------------------------------------------ V6
@reg("AD_UC-05.1")
def ad_0501():
    d = AD("AD UC-05.1", [("RM", 700), ("Hệ thống", 460)], 1690,
           title="AD UC-05.1 Xây dựng phương án bố trí")
    R, H = "RM", "Hệ thống"
    C1, C2 = -160, 180
    c1, c2, hx = d.lane[R] + C1, d.lane[R] + C2, d.lane[H]
    xl = d.lane[R] - 325
    d.add("s", "start", R, 85, dx=C1)
    d.add("ds", "decision", R, 165, "Bắt đầu từ phản hồi điều chỉnh của PM (UC-05.2)?", dx=C1, w=290)
    d.add("a1", "action", R, 270, "1. Tiếp nhận nhu cầu đã xác nhận và ứng viên còn khả năng tham gia; xác "
          "định vị trí cần bố trí", dx=C1, w=270)
    d.add("a2", "action", H, 270, "2. Hiển thị theo vị trí: nhu cầu, ứng viên, kết luận khả năng tham gia "
          "(V5)", w=280)
    d.add("a3", "action", R, 390, "3. Tra cứu hồ sơ năng lực, mức sử dụng, lịch phân bổ, nguồn cung còn lại",
          dx=C1, w=270)
    d.add("a4", "action", H, 390, "4. Cung cấp thông tin; so sánh mức phù hợp, mức sử dụng, chi phí khi "
          "nhiều ứng viên đạt", w=280)
    d.add("m5", "merge", R, 465, dx=C1)
    d.add("df", "decision", R, 555, "Có ứng viên đáp ứng đầy đủ?", dx=C1)
    d.add("x3", "action", R, 555, "A3. Lập phương án “chấp nhận một phần”, ghi mức thiếu hụt", dx=C2, w=260)
    d.add("a5", "action", R, 665, "5. Xây dựng phương án chính: chọn người, vai trò, tỷ lệ, thời gian theo "
          "giai đoạn", dx=C1, w=270)
    d.add("mf", "merge", R, 755, dx=C1)
    d.add("a6", "action", H, 835, "6. Lưu phương án, trạng thái “đang xây dựng” (bắt đầu tính hạn 3 ngày "
          "làm việc)", w=280)
    d.add("a7", "action", H, 925, "7. Nhận biết vị trí rủi ro cao (chỉ một ứng viên đạt)", w=280)
    d.add("dr", "decision", R, 1015, "Có vị trí chỉ một ứng viên đạt?", dx=C1)
    d.add("du", "decision", R, 1125, "Dự án gấp, chưa đủ thời gian?", dx=C1)
    d.add("xa2", "action", R, 1125, "A2. Lập phương án chính duy nhất, ghi lý do và cảnh báo rủi ro",
          dx=C2, w=260)
    d.add("a8", "action", R, 1225, "8. Lập phương án thay thế hoặc biện pháp giảm thiểu rủi ro", dx=C1, w=270)
    d.add("mr", "merge", R, 1315, dx=C1)
    d.add("de", "decision", R, 1405, "Quá 3 ngày làm việc ở “đang xây dựng”?", dx=C1, w=250)
    d.add("xe", "action", R, 1405, "E1. Ghi lý do, báo cáo PMO", dx=C2, w=230)
    d.add("me", "merge", R, 1495, dx=C1)
    d.add("a9", "action", R, 1575, "9. Gửi phương án bố trí (chính và thay thế) cho PM xem xét", dx=C1, w=270)
    d.add("a10", "action", H, 1575, "10. Ghi nhận việc gửi, chuyển phương án cho PM (sang UC-05.2)", w=280)
    d.add("f", "final", H, 1665)
    d.flow("s", "ds")
    d.flow("ds", "a1", guard="Không", lx=-0.4)
    d.flow("ds", "m5", "L", "L", guard="Có (A4)", lx=-0.1, points=[(xl, 165), (xl, 465)])
    d.flow("a1", "a2", "R", "L")
    d.flow("a2", "a3", "B", "T", points=[(hx, 333), (c1, 333)])
    d.flow("a3", "a4", "R", "L")
    d.flow("a4", "m5", "B", "R", points=[(hx, 465)])
    d.flow("m5", "df")
    d.flow("df", "a5", guard="Có", lx=-0.5)
    d.flow("df", "x3", "R", "L", guard="Không (A3)", lx=-0.5)
    d.flow("a5", "mf")
    d.flow("x3", "mf", "B", "R", points=[(c2, 755)])
    d.flow("mf", "a6", "B", "L", points=[(c1, 835)])
    d.flow("a6", "a7")
    d.flow("a7", "dr", "B", "R", points=[(hx, 1015)])
    d.flow("dr", "du", guard="Có", lx=-0.5)
    d.flow("dr", "mr", "L", "L", guard="Không (A1)", lx=-0.2, points=[(xl, 1015), (xl, 1315)])
    d.flow("du", "xa2", "R", "L", guard="Có (A2)", lx=-0.5)
    d.flow("du", "a8", guard="Không", lx=-0.5)
    d.flow("a8", "mr")
    d.flow("xa2", "mr", "B", "R", points=[(c2, 1315)])
    d.flow("mr", "de")
    d.flow("de", "xe", "R", "L", guard="Có (E1)", lx=-0.5)
    d.flow("de", "me", guard="Không", lx=-0.5)
    d.flow("xe", "me", "B", "R", points=[(c2, 1495)])
    d.flow("me", "a9")
    d.flow("a9", "a10", "R", "L")
    d.flow("a10", "f")
    return d


# ------------------------------------------------------------------ V7
@reg("AD_UC-06.2")
def ad_0602():
    d = AD("AD UC-06.2", [("RM", 700), ("PM", 380), ("Hệ thống", 420)], 1340,
           title="AD UC-06.2 Cân đối nguồn lực")
    R, P, H = "RM", "PM", "Hệ thống"
    C1, C2 = -170, 170
    c1, c2, px, hx = d.lane[R] + C1, d.lane[R] + C2, d.lane[P], d.lane[H]
    d.add("s", "start", R, 85, dx=C1)
    d.add("a1", "action", R, 150, "1. Chọn điểm xung đột cần cân đối (từ UC-06.1); mở phiên đàm phán", dx=C1,
          w=270)
    d.add("de", "decision", R, 250, "Mức 3 trở lên?", dx=C1)
    d.add("xe", "action", R, 250, "E1. Chỉ ghi nhận để theo dõi", dx=C2, w=230)
    d.add("fe", "final", R, 330, dx=C2)
    d.add("a2", "action", H, 370, "2. Hiển thị điểm xung đột, kịch bản, đường găng, khoảng dự trữ, xếp hạng "
          "danh mục; theo dõi hạn 3 ngày làm việc", w=300)
    d.add("a3", "action", P, 470, "3. Đàm phán chia sẻ, thay thế hoặc điều chỉnh nhu cầu nguồn lực", w=270)
    d.add("dn", "decision", R, 570, "Kết quả đàm phán?", dx=C1)
    d.add("xa1", "action", R, 570, "A1. Quá 3 ngày làm việc hoặc bế tắc: chuyển hồ sơ sang UC-06.3", dx=C2, w=250)
    d.add("fa1", "final", R, 650, dx=C2)
    d.add("a4", "action", R, 680, "4. Ghi nhận phương án được thống nhất", dx=C1)
    d.add("df", "decision", R, 780, "Còn khoảng dự trữ?", dx=C1)
    d.add("dd", "decision", R, 780, "Bế tắc hoàn toàn?", dx=C2)
    d.add("xa3", "action", P, 780, "A3. RM và PM lập đề xuất lùi mốc tiến độ gốc hoặc cắt giảm phạm vi",
          w=270)
    d.add("a5", "action", R, 890, "5. Làm mịn: điều chỉnh thời điểm trong khoảng dự trữ, không đổi ngày "
          "hoàn thành", dx=C1, w=270)
    d.add("xa2", "action", R, 890, "A2. San bằng nguồn lực trong hạn mức công suất", dx=C2, w=230)
    d.add("m", "merge", R, 990, dx=C2)
    d.add("a6", "action", H, 1070, "6. Ghi điều chỉnh trên phương án; kiểm tra tổng phân bổ mỗi người không "
          "quá 100%", w=300)
    d.add("a7", "action", R, 1170, "7. Ghi nhật ký xử lý xung đột: điểm xung đột, đàm phán, điều chỉnh",
          dx=C1, w=270)
    d.add("a8", "action", R, 1265, "8. Hoàn thiện phương án đã cân đối, bàn giao V8, V9, V10 (kèm đề xuất "
          "thay đổi nếu có)", dx=C1, w=280)
    d.add("a9", "action", H, 1265, "9. Lưu nhật ký (tối thiểu 3 năm); chuyển phương án sang V8, V9, V10",
          w=300)
    d.add("f", "final", H, 1350)
    d.flow("s", "a1")
    d.flow("a1", "de")
    d.flow("de", "xe", "R", "L", guard="Không (E1)", lx=-0.5)
    d.flow("xe", "fe")
    d.flow("de", "a2", "B", "L", guard="Có", points=[(c1, 370)], lx=-0.85)
    d.flow("a2", "a3", "B", "R", points=[(hx, 470)])
    d.flow("a3", "dn", "L", "T", points=[(c1, 470)])
    d.flow("dn", "xa1", "R", "L", guard="Quá hạn, bế tắc", lx=-0.5)
    d.flow("xa1", "fa1")
    d.flow("dn", "a4", guard="Thống nhất", lx=-0.5)
    d.flow("a4", "df")
    d.flow("df", "a5", guard="Còn", lx=-0.5)
    d.flow("df", "dd", "R", "L", guard="Hết", lx=-0.5)
    d.flow("dd", "xa2", guard="Không (A2)", lx=-0.5)
    d.flow("dd", "xa3", "R", "L", guard="Có (A3)", lx=-0.5)
    d.flow("xa2", "m")
    d.flow("a5", "m", "B", "L", points=[(c1, 990)])
    d.flow("xa3", "m", "B", "R", points=[(px, 990)])
    d.flow("m", "a6", "B", "L", points=[(c2, 1070)])
    d.flow("a6", "a7", "B", "R", points=[(hx, 1170)])
    d.flow("a7", "a8")
    d.flow("a8", "a9", "R", "L")
    d.flow("a9", "f")
    return d


@reg("AD_UC-07.1")
def ad_0701():
    T = "Cấp thẩm quyền (PMO Mức 1–3 / CEO Mức 4–5)"
    d = AD("AD UC-07.1", [("PMO/Quản lý danh mục", 600), (T, 460), ("Hệ thống", 420)], 1180,
           title="AD UC-07.1 Rà soát và đánh giá phương án")
    P, H = "PMO/Quản lý danh mục", "Hệ thống"
    C1, C2 = -160, 150
    c1, c2, tx, hx = d.lane[P] + C1, d.lane[P] + C2, d.lane[T], d.lane[H]
    d.add("s", "start", P, 85, dx=C1)
    d.add("a1", "action", P, 160, "1. Tiếp nhận hồ sơ phương án gửi trình duyệt từ V6 hoặc V7", dx=C1)
    d.add("a2", "action", H, 260, "2. Đối chiếu mức rủi ro với ma trận DoA, xác định cấp thẩm quyền", w=280)
    d.add("dc", "decision", P, 360, "Mức rủi ro?", dx=C1)
    d.add("xa1", "action", P, 360, "A1. Chuyển cấp hồ sơ lên CEO/Managing Director trong tối đa 1 ngày "
          "làm việc", dx=C2, w=220)
    d.add("xb1", "action", T, 460, "A1. CEO/Managing Director tiếp nhận hồ sơ chuyển cấp")
    d.add("m", "merge", T, 550)
    d.add("a3", "action", T, 640, "3. Rà soát tính hợp lý: phân bổ nhân sự, mức đáp ứng năng lực, tỷ lệ "
          "tải trọng, điểm xung đột", w=320)
    d.add("a4", "action", H, 740, "4. Cung cấp thông tin chi phí, chênh lệch ngân sách (V9) và cung – cầu, "
          "kết quả dự báo (V10)", w=300)
    d.add("a5", "action", T, 840, "5. Đánh giá rủi ro, kết luận hồ sơ đủ hay chưa đủ cơ sở ra quyết định",
          w=300)
    d.add("dd", "decision", T, 950, "Đủ cơ sở ra quyết định?")
    d.add("a6", "action", H, 950, "6. Ghi nhận kết quả rà soát, chuyển hồ sơ sang UC-07.3 hoặc UC-07.4",
          w=280)
    d.add("f", "final", H, 1040)
    d.add("xa2", "action", T, 1065, "A2. Lập danh sách nội dung cần giải trình, bổ sung; chuyển UC-07.2",
          w=300)
    d.add("fa2", "final", T, 1145)
    d.flow("s", "a1")
    d.flow("a1", "a2", "B", "L", points=[(c1, 260)])
    d.flow("a2", "dc", "B", "T", points=[(hx, 300), (c1, 300)])
    d.flow("dc", "xa1", "R", "L", guard="Mức 4–5 (A1)", lx=-0.5)
    d.flow("xa1", "xb1", "B", "L", points=[(c2, 460)])
    d.flow("xb1", "m")
    d.flow("dc", "m", "B", "L", guard="Mức 1–3", points=[(c1, 550)], lx=-0.8)
    d.flow("m", "a3")
    d.flow("a3", "a4", "R", "T", points=[(hx, 640)])
    d.flow("a4", "a5", "B", "R", points=[(hx, 840)])
    d.flow("a5", "dd")
    d.flow("dd", "a6", "R", "L", guard="Đủ", lx=-0.5)
    d.flow("a6", "f")
    d.flow("dd", "xa2", guard="Chưa đủ (A2)", lx=-0.5)
    d.flow("xa2", "fa2")
    return d


@reg("AD_UC-08.1")
def ad_0801():
    P, F, H = "PM", "Tài chính", "Hệ thống"
    d = AD("AD UC-08.1", [(P, 480), (F, 600), (H, 600)], 1360,
           title="AD UC-08.1 Tính và cập nhật chi phí phương án")
    L, R = -150, 160
    px, fl, fr, hl = d.lane[P], d.lane[F] + L, d.lane[F] + R, d.lane[H] + L
    d.add("s", "start", P, 85)
    d.add("a1", "action", P, 160, "1. Chọn phương án bố trí cần đánh giá chi phí, ghi lý do")
    d.add("d0", "decision", H, 260, "Có phương án và phạm vi công việc?", dx=L)
    d.add("xe2", "action", H, 260, "E2. Không bắt đầu đánh giá", dx=R, w=200)
    d.add("fe2", "final", H, 345, dx=R)
    d.add("a2", "action", H, 370, "2. Hiển thị phương án, phạm vi công việc, nhân sự, số lượng, thời gian, "
          "mức độ tham gia", dx=L, w=270)
    d.add("a3", "action", P, 470, "3. Lượng hóa, xác nhận yếu tố tạo chi phí: nhân sự, số lượng, thời gian, "
          "mức độ tham gia", w=300)
    d.add("a4", "action", F, 570, "4. Cung cấp, cập nhật đơn giá; ghi nhận chi phí thực tế nếu đã phát sinh",
          dx=L, w=260)
    d.add("d1", "decision", F, 680, "Đủ đơn giá và dữ liệu?", dx=L)
    d.add("xe1", "action", H, 680, "E1. Đánh dấu dữ liệu thiếu, yêu cầu Tài chính bổ sung; chưa kết luận "
          "chính thức", dx=100, w=260)
    d.add("fe1", "final", H, 765, dx=100)
    d.add("d2", "decision", F, 800, "Có thay đổi hoặc lệch dự toán?", dx=L)
    d.add("xa1", "action", F, 800, "A1. Tính lại phần chi phí bị ảnh hưởng, cập nhật dự báo", dx=R, w=220)
    d.add("m", "merge", F, 910, dx=L)
    d.add("a5", "action", F, 1000, "5. Tính chi phí dự toán; cập nhật dự báo, lưu tách dự toán và dự báo",
          dx=L, w=260)
    d.add("a6", "action", P, 1110, "6. Xem kết quả chi phí dự toán, dự báo của phương án")
    d.add("a7", "action", H, 1210, "7. Lưu kết quả chi phí, sẵn sàng cho UC-08.2 Đối chiếu chi phí và ngân "
          "sách", dx=L, w=270)
    d.add("f", "final", H, 1300, dx=L)
    d.flow("s", "a1")
    d.flow("a1", "d0", "R", "T", points=[(hl, 160)])
    d.flow("d0", "xe2", "R", "L", guard="Không (E2)", lx=-0.5)
    d.flow("xe2", "fe2")
    d.flow("d0", "a2", guard="Có", lx=-0.5)
    d.flow("a2", "a3", "B", "R", points=[(hl, 470)])
    d.flow("a3", "a4", "B", "L", points=[(px, 570)])
    d.flow("a4", "d1")
    d.flow("d1", "xe1", "R", "L", guard="Không (E1)", lx=-0.6)
    d.flow("xe1", "fe1")
    d.flow("d1", "d2", guard="Có", lx=-0.5)
    d.flow("d2", "xa1", "R", "L", guard="Có (A1)", lx=-0.5)
    d.flow("d2", "m", guard="Không", lx=-0.5)
    d.flow("xa1", "m", "B", "R", points=[(fr, 910)])
    d.flow("m", "a5")
    d.flow("a5", "a6", "B", "R", points=[(fl, 1110)])
    d.flow("a6", "a7", "B", "L", points=[(px, 1210)])
    d.flow("a7", "f")
    return d


def main(out):
    os.makedirs(out, exist_ok=True)
    only = sys.argv[2:] or list(ADS)
    for code in only:
        with open(os.path.join(out, code + ".drawio"), "w", encoding="utf-8") as f:
            f.write(ADS[code]().xml())


if __name__ == "__main__":
    main(sys.argv[1])
