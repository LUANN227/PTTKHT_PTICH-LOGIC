# Quy ước Phần II

Áp dụng cho mọi bài V2–V10.

Nguồn ưu tiên theo thứ tự: Outline → Phần I (P1) → HD-PCCN, HD-MAU → bài thành viên. Quy ước nào cần trưởng nhóm quyết định thì có ghi chú **[TN]**.

## 1. Nghiệp vụ và truy vết

| # | Quy tắc | Căn cứ | Ví dụ đúng / sai |
|---|---|---|---|
| 1.1 | Chỉ dùng mã CN-01..129, QT-01..57, RB-01..62, PCN-01..11 đúng như P1. Không tạo mã theo vùng | P1 I.2, I.1.4 | Đúng: CN-17. Sai: CN-V2-01, BR-V5-03 |
| 1.2 | Mã UC theo HD-PCCN §1. Không đổi tên UC | HD-PCCN | Sai: đổi UC-08.1 thành tên cả nhóm V9 |
| 1.3 | Mỗi bước luồng ghi mã CN hỗ trợ bước đó; bảng BR ghi mã kèm vai trò trong UC | HD-MAU §3.4 | |
| 1.4 | Một CN liên quan nhiều UC: ghi ở UC thực hiện hành vi; UC khác ghi "nhận kết quả" | P1 I.3 | CN-122 thuộc V10; V2 ghi CN-17 |
| 1.5 | Điểm chưa xác định: ghi **[Chưa xác định]** và nêu câu hỏi. Không tự điền ngưỡng, công thức, thời hạn | Yêu cầu trưởng nhóm | Sai: "FTE ≤ 1.0" |
| 1.6 | Dùng thuật ngữ P1 | P1 I.1.2 | "Hạng ưu tiên 1", không dùng "Rank 1" |

## 2. Actor

Actor chỉ gồm PM, RM, Nguồn lực, Tài chính, PMO/Quản lý danh mục, CEO/Managing Director (P1 I.1.2). Khi HD-PCCN khác P1, theo P1.

| # | Quy tắc | Căn cứ |
|---|---|---|
| 2.1 | Actor chính là người khởi động và đạt mục tiêu; actor phụ chỉ tham gia ở nhánh | HD-MAU §2.1 |
| 2.2 | Không có actor "Hệ thống", "Người dùng", "CCB" | P1 I.1.2 |
| 2.3 | Actor không phải lớp miền | Outline II.3 |

## 3. Use Case

| # | Quy tắc | Căn cứ | Ví dụ đúng / sai |
|---|---|---|---|
| 3.1 | Tên UC là mục tiêu nghiệp vụ; bước luồng không thành UC | HD-PCCN §3 | |
| 3.2 | Tiền điều kiện của UC sau khớp hậu điều kiện của UC trước | P1 I.1.3.1 | 01.1 → 01.2 |
| 3.3 | Luồng thay thế (A) là nhánh nghiệp vụ bình thường; ngoại lệ (E) là lỗi nghiệp vụ. Không ghi thao tác giao diện, lỗi kỹ thuật | HD-MAU §3.3 | Sai: E "Lỗi kết nối CSDL" |
| 3.4 | `include`: UC gốc luôn gọi UC con, không có điều kiện | UML | Đúng: 09.1 include 09.2 |
| 3.5 | `extend`: UC con chạy ở UC gốc khi có điều kiện | UML | Đúng: 07.2 extend 07.1; 06.3 extend 06.2; 01.3 extend 01.2 (khi RM trả lại, chờ D-06) |
| 3.6 | Bàn giao dữ liệu giữa vùng **không** vẽ include/extend | P1 I.1.3.1 | Sai: 07.1 include UC-08 |
| 3.7 | Generalization chỉ dùng khi UC con kế thừa toàn bộ hành vi của UC cha. Hiện chưa có trường hợp nào | | |
| 3.8 | Mỗi vùng có một UCD cấp vùng, đủ UC con | Yêu cầu trưởng nhóm | |

## 4. Activity Diagram

| # | Quy tắc |
|---|---|
| 4.1 | Có một nút bắt đầu; mỗi nhánh kết thúc bằng final node. Không có action treo |
| 4.2 | Decision có điều kiện trên mỗi nhánh; Merge hợp các nhánh loại trừ nhau |
| 4.3 | Fork/Join chỉ dùng khi P1 nói rõ là song song (ví dụ V10 bước 1–2) |
| 4.4 | Swimlane theo người thực hiện; action của RM nằm ở làn RM |
| 4.5 | Gọi UC khác thì vẽ thành một action "Thực hiện UC-xx". Không vẽ ký hiệu include |
| 4.6 | AD không chứa bước của UC khác |
| 4.7 | Hình nằm trong file nộp |

## 5. Domain Class Diagram

| # | Quy tắc | Ví dụ |
|---|---|---|
| 5.1 | Tên lớp viết PascalCase tiếng Việt không dấu; dùng tên trong II.3 | ChiTietBoTri |
| 5.2 | Thuộc tính viết camelCase; thuộc tính suy ra có `/` | /nguonCungCoTheDapUng |
| 5.3 | Không có lớp actor, UI, controller, service, repository | Sai: NguoiDung, ConflictController |
| 5.4 | Composition chỉ dùng khi phần không tồn tại ngoài toàn thể | PhuongAnBoTri ◆ ChiTietBoTri |
| 5.5 | Multiplicity ghi theo nghiệp vụ, có căn cứ | |
| 5.6 | Trạng thái là thuộc tính; kết quả đánh giá có vòng đời riêng thì là lớp | KetLuanKhaNangThamGia |
| 5.7 | Không sao chép lớp của vùng khác; dùng liên kết | V8 tham chiếu DanhGiaChiPhi |
| 5.8 | Không thay liên kết bằng thuộc tính danh sách | Sai: DanhSachXungDot |
| 5.9 | Quy tắc (DoA, ngưỡng 10%) không vẽ thành lớp **[TN Q-08]** | |

## 6. Kiểm tra chéo trước khi nộp

- Description khớp AD.
- Mã khớp P1.
- Lớp có trong II.3.
- UCD cấp vùng khớp II.1.
- Không tự đặt quy tắc trái baseline.

## 7. Trình bày [TN]

Cấu trúc theo Phần I. Cách xuất hình theo ba hình mới của V8 (nền trắng, nét rõ, chữ đọc được ở chiều rộng trang).

| # | Quy tắc | Ví dụ |
|---|---|---|
| 7.1 | Mục cấp vùng đánh số theo Phần I: `II.2.x. Vy — <tên vùng>` | "II.2.3. V4 — Tìm kiếm và đánh giá mức độ phù hợp" |
| 7.2 | Chú thích hình đặt dưới hình, in nghiêng, dạng "Hình II.n. <loại sơ đồ> <mã UC>: <tên UC>" (P1 dùng "Hình n. Activity Diagram V4: …") | "Hình II.12. Activity Diagram UC-03.3: Đánh giá, xếp hạng và lập shortlist ứng viên" |
| 7.3 | Tiêu đề trên sơ đồ là mã và tên UC theo HD-PCCN | Sai: "PHÂN HỆ V5" |
| 7.4 | Chèn hình PNG xuất từ file nguồn ở tỷ lệ 150–200%, không chụp màn hình | |
| 7.5 | Không để link Drive thay cho hình | |

## 8. File nguồn của sơ đồ

| # | Quy tắc |
|---|---|
| 8.1 | Mỗi hình trong bài có file nguồn sửa được nằm cạnh bản xuất |
| 8.2 | Nhóm dùng draw.io, nên `.drawio` là nguồn chính. UCD và sơ đồ phân rã là hình gốc draw.io |
| 8.3 | AD và sơ đồ lớp do trưởng nhóm lập bằng PlantUML: nguồn là `.puml`; file `.drawio` cùng tên chứa hình và mã PlantUML, mở được trong draw.io |
| 8.4 | Sau khi sửa nguồn phải xuất lại PNG và xem lại hình trước khi chèn |
