# 09. Kế hoạch V10 (2 UC + II.1 + II.3)

V10 chưa có bài. Phạm vi gồm: UC-09.1, UC-09.2, sơ đồ tổng quát II.1, mô hình lớp hợp nhất II.3.

## 1. UC-09.1 Theo dõi sử dụng nguồn lực

| Mục | Nội dung |
|-----|----------|
| Actor chính | RM [Nguồn: P1 I.1.2]; PMO là phương án thay thế (D-08) |
| Tiền điều kiện | Có PhanBoNguonLuc ở trạng thái đã phê duyệt (từ UC-07.3) |
| Kích hoạt | Định kỳ hoặc khi có thay đổi lịch |
| Kết quả | Bảng theo dõi, cảnh báo quá tải/thiếu hụt |
| CN | Nhóm CN thuộc V10 theo P1 trừ CN-116–119 |
| Liên kết | Cảnh báo phản hồi về V2 (CN-17) |

## 2. UC-09.2 Dự báo nhu cầu nguồn lực

| Mục | Nội dung |
|-----|----------|
| Actor chính | RM; PMO nhận báo cáo |
| Đầu vào | Dữ liệu theo dõi từ 09.1, danh mục dự án |
| Kết quả | Báo cáo dự báo, đề xuất tuyển dụng/điều chỉnh |
| CN | [Đề xuất] CN-116–119 chuyển về 09.2 |

## 3. Việc cần trước

- D-08 (actor), D-10 (trạng thái phương án), D-09 (đối tượng phân bổ).
- UC-07.3 có đặc tả (vì 09.1 cần trạng thái "đã phê duyệt").

## 4. II.1 Sơ đồ tổng quát

- Nếu chọn phương án B (D-01): 6 chức năng lớn CN-L1..L6 (tài liệu 03).
- Actor: PM, RM, Nguồn lực, Tài chính, PMO/Quản lý danh mục, CEO/MD. CCB không là actor.
- Association theo cột "Tham gia tại" P1 I.1.2.
- Không vẽ include/extend ở II.1; để ở II.2.

## 5. II.3 Mô hình lớp hợp nhất

Bước làm:
1. Lấy danh sách lớp từ 8 bài hiện có (tài liệu 06).
2. Gộp tên đồng nghĩa theo D-12, D-13.
3. Chốt vòng đời NhuCau (D-07), PhuongAnBoTri (D-10).
4. Thêm lớp cấu hình/người dùng theo D-14.
5. Kiểm tra mỗi lớp có ít nhất một UC tạo và một UC dùng.

## 6. Ước lượng

UC-09.1: M; UC-09.2: M; II.1: M; II.3: L. [Giả định]
