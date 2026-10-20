# 08. Kế hoạch chỉnh sửa theo thành viên

Nguyên tắc: chỉ liệt kê việc có căn cứ (tài liệu 06). Việc phụ thuộc quyết định chưa chốt được đánh dấu **"Chờ D-xx"** và **không giao** cho tới khi trưởng nhóm chốt. Mức thay đổi theo thang A–E (A: không đổi; B: chỉnh câu chữ; C: sửa nội dung trong UC; D: đổi phạm vi UC; E: đổi cấu trúc nhóm).

Ước lượng công sức: S (< 2 giờ), M (nửa ngày), L (1 ngày trở lên). Đây là [Giả định], thành viên tự điều chỉnh.

## 1. Bảng việc

| # | Thành viên / Bài | UC | Việc | Mức | Công sức | Phụ thuộc | Trạng thái |
|---|------------------|----|------|-----|---------|-----------|-----------|
| 1 | Thùy Linh (V2a) | 01.1 | Sửa mã truy vết theo bảng ánh xạ tài liệu 05 | B | S | – | Giao được |
| 2 | Thùy Linh (V2a) | 01.1 | Thống nhất trạng thái NhuCau | C | S | D-07 | Chờ D-07 |
| 3 | Thùy Linh (V2a) | 01.1 | Tách ViTriCanBoTri trong lớp | C | M | D-15 | Chờ D-15 |
| 4 | Tuấn Long (V2b) | 01.2, 01.3 | Hoàn thành §7–12 đang trống | C | L | – | Giao được |
| 5 | Tuấn Long (V2b) | 01.3 | Ranh giới RM trả lại vs phản hồi bước sau | D | M | D-06 | Chờ D-06 |
| 6 | Lê Hoài Linh (V3) | 02.1 | Sửa mã truy vết | B | S | – | Giao được |
| 7 | Lê Hoài Linh (V3) | 02.2 | Viết hoặc bỏ UC-02.2 | D | M | D-05 | Chờ D-05 |
| 8 | Nguyễn Hoàng Linh (V4) | 03.3 | Đổi UngVien → tên thống nhất | B | S | D-12 | Chờ D-12 |
| 9 | Khánh Linh (V5) | 04.1 | Sửa mã truy vết; bổ sung điều kiện thang 5 mức | C | M | D-04 | Phần mã giao được; phần thang chờ D-04 |
| 10 | Nguyễn Thi Thùy Linh (V6) | 05.1 | Thống nhất PhanBoNguonLuc/ChiTietBoTri | C | M | D-09 | Chờ D-09 |
| 11 | (chưa có chủ) | 05.2 | Đặc tả UC-05.2 đầy đủ | – | L | D-11 | Chờ D-11 |
| 12 | Lưu Thùy Linh (V7) | 06.2 | Trả 06.1, 06.3 về đúng chỗ; sửa mã sai | D | L | D-18 | Phần mã giao được; phạm vi chờ D-18 |
| 13 | Lưu Thùy Linh (V7) | – | Tạm gác phần II.4 đã viết | – | – | D-19 | Chờ D-19 |
| 14 | Ngọc Linh (V8) | 07.1 | Đưa sơ đồ từ Drive vào file nộp | B | S | – | Giao được |
| 15 | Ngọc Linh (V8) hoặc người khác | 07.3 | Đặc tả UC-07.3 | – | L | D-10 | Chờ D-10 |
| 16 | Ngô Nhật Long (V9) | 08.1 | Ghi chú "08.2, 08.3 đã gộp vào 08.1" | B | S | D-03 | Chờ D-03 |
| 17 | Ngô Nhật Long (V9) | 08.1 | Làm rõ công thức ngân sách | C | M | D-20 | Chờ D-20 |
| 18 | Trưởng nhóm | II.1 | Vẽ sơ đồ tổng quát | – | M | D-01, D-08 | Chờ D-01 |
| 19 | Trưởng nhóm | II.3 | Hợp nhất mô hình lớp | – | L | D-09, D-10, D-12, D-13, D-14 | Chờ |

Chi tiết lỗi từng bài: tài liệu 06. Bảng ánh xạ mã: tài liệu 05.

## 2. Việc giao được ngay (không phụ thuộc quyết định)

Dòng 1, 4, 6, 9 (phần mã), 12 (phần mã), 14. Các việc này an toàn vì không đổi phạm vi nghiệp vụ.

## 3. Kiểm tra trước khi nộp lại

- Mã CN/QT/RB khớp P1, không tự tạo mã mới.
- Tên lớp và trạng thái khớp danh mục thống nhất (sau khi chốt).
- Không có bước của UC khác nằm trong luồng chính.
- Sơ đồ nằm trong file nộp, không chỉ ở link ngoài.
