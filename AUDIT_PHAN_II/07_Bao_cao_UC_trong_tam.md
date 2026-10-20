# 07. Báo cáo UC trọng tâm (xương sống)

Mục tiêu: xác định các UC mà phần còn lại phụ thuộc vào, và chỉ ra UC xương sống nào chưa có người đặc tả. Căn cứ: ma trận phụ thuộc trong tài liệu 04, luồng chính P1 I.1.3.1.

## 1. Luồng xương sống

[Nguồn] P1 I.1.3.1: Nhu cầu (V2) → Hồ sơ năng lực (V3) → Tìm ứng viên (V4) → Khả năng tham gia (V5) → Phương án (V6) → Xung đột (V7, nếu có) → Phê duyệt (V8) song song Ngân sách (V9) → Theo dõi (V10, liên tục).

[Đối chiếu] Mỗi bước trên cần ít nhất một UC "tạo ra đối tượng" cho bước sau dùng. Bảng dưới là các UC đó.

| Thứ tự | UC xương sống | Đối tượng tạo ra | Bước sau dùng | Hiện trạng đặc tả |
|-------|---------------|------------------|---------------|-------------------|
| 1 | UC-01.1 Lập nhu cầu | NhuCau (+ ViTriCanBoTri) | V4, V5, V6, V9 | Có (Thùy Linh), cần thống nhất trạng thái (D-07) |
| 2 | UC-01.2 Xác nhận nhu cầu | NhuCau "Đã xác nhận" | V4 | Có (Tuấn Long), §7–12 trống |
| 3 | UC-02.1 Cập nhật hồ sơ năng lực | HoSoNangLuc | V4 | Có (Lê Hoài Linh) |
| 4 | **UC-02.2** (hồ sơ năng lực được duyệt/công bố) | HoSoNangLuc "Hiệu lực" | V4 | **Chưa có** (D-05) |
| 5 | UC-03.1/03.3 Tìm và xếp hạng ứng viên | Danh sách ứng viên | V5 | Có 03.3 (Nguyễn Hoàng Linh) |
| 6 | UC-04.1 Đánh giá khả năng tham gia | Kết luận khả năng tham gia | V6 | Có (Khánh Linh) |
| 7 | **UC-05.2** Lập/hoàn thiện phương án (CN-70, CN-72) | PhuongAnBoTri | V7, V8, V9 | **Chưa có chủ** (D-11) |
| 8 | UC-06.2 Xử lý xung đột | PhuongAnBoTri đã cân đối | V8 | Có nhưng tràn phạm vi (Lưu Thùy Linh) |
| 9 | UC-07.1 Thẩm định phương án | Kết luận thẩm định | 07.3 | Có (Ngọc Linh), sơ đồ chỉ trên Drive |
| 10 | **UC-07.3** Phê duyệt phương án | PhuongAnBoTri "Đã phê duyệt", PhanBoNguonLuc | V10 | **Chưa có** |
| 11 | UC-08.1 (mở rộng) Đánh giá ngân sách | DanhGiaChiPhi | V8 | Có (Ngô Nhật Long) |
| 12 | UC-09.1/09.2 Theo dõi, dự báo | Cảnh báo, dự báo | V2 (CN-17) | Chưa có (V10, tài liệu 09) |

## 2. Ba lỗ hổng xương sống

1. **UC-05.2** — không có ai được giao. Không có nó thì V7, V8, V9 đang nhận một "phương án" mà không UC nào định nghĩa cách tạo ra. Ưu tiên cao nhất.
2. **UC-07.3** — không có đặc tả. Đây là điểm đổi trạng thái chính thức của phương án và là đầu vào của V10. Không có nó, II.3 (lớp) không chốt được vòng đời PhuongAnBoTri (D-10).
3. **UC-02.2** — chưa xác định nội dung (D-05). Nếu chọn không cần UC riêng, phải ghi rõ trạng thái "Hiệu lực" của HoSoNangLuc do UC-02.1 đặt.

## 3. Đối tượng xương sống (cho II.3)

[Đề xuất] Bộ lớp tối thiểu phải thống nhất trước khi thành viên sửa: NhuCau, ViTriCanBoTri, NguonLuc, HoSoNangLuc, LichNguonLuc, PhuongAnBoTri, ChiTietBoTri/PhanBoNguonLuc (D-09), XungDot, HoSoTrinhDuyet (D-10), DanhGiaChiPhi. Các tên đồng nghĩa đang dùng (UngVien, YeuCauNguonLuc) chờ D-12, D-13.

## 4. Thứ tự làm đề xuất

[Đề xuất] Chốt D-07, D-09, D-10, D-12, D-13, D-15 → viết UC-05.2 → UC-07.3 → UC-02.2 (nếu giữ) → thành viên sửa theo tài liệu 08.
