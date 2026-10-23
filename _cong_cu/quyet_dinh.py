"""Nội dung các quyết định đã chốt dùng chung cho bài sửa, II.3 và Word tổng hợp (một nguồn, tránh lệch chữ).

QĐ-02: trạng thái nhu cầu nguồn lực. QĐ-07: công thức tỷ lệ vượt ngân sách.
QĐ-21: miền giá trị thuộc tính trạng thái của các lớp có sơ đồ trạng thái ở II.4.1.
QĐ-22: đơn vị tính đơn giá và mức tham gia.
"""

# ---------------------------------------------------------------- QĐ-07
QT51 = ("Phương án vượt ngân sách còn lại trên 10% phải chuyển phê duyệt CEO/Managing Director; không quá 10% thì PM "
        "tự điều chỉnh hoặc xin phê duyệt cấp Quản lý danh mục. Ngưỡng dùng chung với DoA của V8.")
QD07_CT = ("Ngân sách còn lại = ngân sách được duyệt − chi phí thực tế đã phát sinh. Tỷ lệ vượt = (chi phí dự kiến của "
           "phần việc còn lại − ngân sách còn lại) / ngân sách còn lại × 100%. Các giá trị tính bằng VNĐ, lấy tại cùng "
           "một thời điểm. Tỷ lệ vượt ≤ 0 là trong ngân sách. Nếu ngân sách còn lại ≤ 0 mà vẫn phát sinh chi phí thì "
           "coi là vượt trên 10% và chuyển CEO/Managing Director.")
QD07 = "Cách tính: " + QD07_CT

# ---------------------------------------------------------------- QĐ-22
DON_VI = ("Đơn giá nguồn lực tính bằng VNĐ/ngày công, theo từng vai trò; mức tham gia tính bằng %FTE (0–100%). "
          "Chi phí một dòng bố trí = đơn giá ngày công × số ngày làm việc trong khoảng thời gian bố trí × %FTE.")

# ---------------------------------------------------------------- QĐ-02, QĐ-21
# Lớp -> (thuộc tính, [giá trị], chuỗi chuyển trạng thái, căn cứ)
TRANG_THAI = {
    "NhuCauNguonLuc": (
        "trangThai",
        ["Đang xây dựng", "Đã chuyển RM", "Đã xác nhận", "Cần tiếp tục hoàn thiện"],
        "Đang xây dựng (PM xác định, hoàn thiện nhu cầu) → Đã chuyển RM (PM chuyển RM xem xét, CN-11) → Đã xác "
        "nhận (RM xác nhận, bàn giao V3, V4) hoặc Cần tiếp tục hoàn thiện (RM chuyển lại PM bổ sung, điều chỉnh, "
        "rồi PM chuyển RM lại)",
        "CN-11, CN-13–CN-15; I.1.3.2"),
    "PhuongAnBoTri": (
        "trangThai",
        ["Đang xây dựng", "Đã gửi PM", "Cần điều chỉnh", "Đang cân đối", "Chờ phê duyệt", "Yêu cầu chỉnh sửa",
         "Locked Baseline", "Bị từ chối"],
        "Đang xây dựng (RM lập phương án, tối đa 3 ngày làm việc) → Đã gửi PM → Cần điều chỉnh (PM yêu cầu, RM "
        "điều chỉnh rồi gửi lại) hoặc PM xác nhận; sau xác nhận: có nghi ngờ xung đột → Đang cân đối (V7), không "
        "nghi ngờ xung đột → Chờ phê duyệt (V8, V9); V7 cân đối xong → Chờ phê duyệt; V8 quyết định: Phê duyệt "
        "hoặc Duyệt ngoại lệ → Locked Baseline, Yêu cầu chỉnh sửa → trả về V6 (Đang xây dựng) hoặc V7 (Đang cân "
        "đối), Từ chối → Bị từ chối",
        "QT-31; CN-68, CN-69, CN-72, CN-73, CN-88, CN-99, CN-101; I.1.3.6, I.1.3.8"),
    "DiemXungDot": (
        "trangThaiXuLy",
        ["Chưa xử lý", "Chỉ theo dõi", "Đang đàm phán", "Đã làm mịn", "Đã san bằng", "Đã đề xuất thay đổi",
         "Chờ phân xử", "Đã giải quyết"],
        "Chưa xử lý → Chỉ theo dõi (dưới Mức 3) hoặc Đang đàm phán (Mức 3 trở lên, tối đa 3 ngày làm việc); từ Đang "
        "đàm phán: thống nhất, còn khoảng dự trữ → Đã làm mịn; hết khoảng dự trữ → Đã san bằng; bế tắc hoàn toàn → "
        "Đã đề xuất thay đổi; hết 3 ngày chưa thống nhất hoặc bế tắc → Chờ phân xử (UC-06.3); Đã làm mịn, Đã san "
        "bằng, Đã đề xuất thay đổi (sau khi ghi nhật ký, bàn giao) và Chờ phân xử (khi có quyết định) → Đã giải "
        "quyết",
        "QT-33, QT-35–QT-38; CN-78–CN-88; I.1.3.7"),
    "HoSoTrinhDuyet": (
        "trangThaiXuLy",
        ["Đã tiếp nhận", "Đã chuyển cấp CEO", "Đang rà soát", "Chờ giải trình", "Đủ cơ sở, chờ quyết định",
         "Đã phê duyệt", "Duyệt ngoại lệ", "Yêu cầu chỉnh sửa", "Từ chối"],
        "Đã tiếp nhận → Đã chuyển cấp CEO (Mức 4–5, tối đa 1 ngày làm việc) hoặc giữ ở PMO (Mức 1–3) → Đang rà "
        "soát → Chờ giải trình (UC-07.2; chỉ bổ sung, làm rõ thì quay lại Đang rà soát; cần thay đổi phân bổ thì "
        "Yêu cầu chỉnh sửa) hoặc Đủ cơ sở, chờ quyết định → Đã phê duyệt, Duyệt ngoại lệ, Yêu cầu chỉnh sửa hoặc "
        "Từ chối",
        "QT-40–QT-46; CN-89–CN-102; I.1.3.8"),
}


def mien(cls):
    """Chuỗi miền giá trị: 'trangThai: A, B, C'."""
    attr, vals, _, _ = TRANG_THAI[cls]
    return f"{attr}: " + ", ".join(vals)
