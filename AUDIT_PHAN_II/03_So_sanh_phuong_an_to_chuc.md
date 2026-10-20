# 03. So sánh phương án tổ chức hệ thống

Mục tiêu tài liệu: so sánh công khai các cách tổ chức 9 nhóm chức năng và 28 UC, dựa trên kết quả audit. Việc chọn phương án thuộc trưởng nhóm (Decision D-01, D-03 trong tài liệu 10).

## 1. Hai câu hỏi cần tách riêng

1. **Trình bày**: II.1 và II.2 nên hiện bao nhiêu "phân hệ" hoặc "chức năng lớn"? Đây là cách nhóm UC trên sơ đồ, không đổi nghiệp vụ.
2. **Cấu trúc nghiệp vụ**: có UC nào cần gộp, tách, đổi phạm vi, hoặc chuyển nhóm không? Đây là thay đổi thật, kéo theo sửa Description, AD, lớp và mã truy vết.

Đề xuất "5–6 phân hệ" của trưởng nhóm có thể hiểu theo nghĩa 1 hoặc nghĩa 2. Audit cho thấy **nghĩa 1 có căn cứ và rẻ; nghĩa 2 chỉ có căn cứ cho vài điểm nhỏ**.

## 2. Các phương án

### Phương án A — Giữ nguyên 9 nhóm, chỉ sửa lỗi cần thiết

Giữ UC-01..UC-09 theo V2..V10 trên II.1; 28 UC giữ mã.

### Phương án B — Gom 9 nhóm thành 6 chức năng lớn khi trình bày (đề xuất)

Giữ nguyên 9 nhóm và 28 UC với mã hiện tại. Trên II.1 vẽ 6 chức năng lớn; II.2 trình bày UC chi tiết bên dưới từng chức năng lớn. Mã UC không đổi.

| Chức năng lớn (đề xuất) | Nhóm hiện có | Căn cứ gom |
|-------------------------|--------------|------------|
| CN-L1. Quản lý nhu cầu nguồn lực | UC-01 (V2) | Đối tượng trung tâm: Nhu cầu. PM là chủ thể. Nhận phản hồi từ V4, V10 (CN-17) |
| CN-L2. Quản lý năng lực và tìm kiếm ứng viên | UC-02 (V3), UC-03 (V4) | Cùng actor chính RM; cùng dựa trên hồ sơ năng lực (P1 I.1.3.1 "V4 sử dụng kết quả V3"); HD-PCCN §3 đã có ranh giới UC-02.1↔UC-03.1 |
| CN-L3. Đánh giá khả năng tham gia và lập phương án | UC-04 (V5), UC-05 (V6) | Cùng dùng lịch nguồn lực tập trung; V5 bàn giao trực tiếp V6; kết luận khả năng tham gia là đầu vào bắt buộc của phương án |
| CN-L4. Xử lý xung đột và cân đối | UC-06 (V7) | Có actor, thời hạn và quy tắc riêng (3 ngày, 1 ngày, Mức 3); đầu vào từ V5 và V6 |
| CN-L5. Phê duyệt phương án và kiểm soát ngân sách | UC-07 (V8), UC-08 (V9) | P1 nói rõ V9 song song V8, cấp thông tin cho V8, dùng chung ngưỡng DoA (QT-51, RB-61) |
| CN-L6. Theo dõi và dự báo nguồn lực | UC-09 (V10) | Chạy liên tục, không thuộc luồng chính (P1 I.1.3.1) |

Phương án thay thế trong B (nếu muốn 5 nhóm): gộp CN-L4 vào CN-L3 thành "Lập và cân đối phương án bố trí". Căn cứ yếu hơn vì V7 có actor PMO/CEO và quy tắc riêng; không khuyến nghị.

### Phương án C — Điều chỉnh ranh giới thật thành 5–6 phân hệ

Đổi mã nhóm (ví dụ UC-02 và UC-03 thành một nhóm mới, đánh lại UC-02.x), chuyển UC giữa nhóm. Audit **không tìm thấy UC nào đặt sai nhóm** so với Phần I: mọi UC đều có CN thuộc đúng vùng. Vì vậy C chỉ là A/B cộng thêm việc đánh lại mã, mà không giải quyết được vấn đề thật (mô hình đối tượng không thống nhất).

### Phương án D — Điều chỉnh danh mục UC có chọn lọc

Chỉ xét những chỗ có bằng chứng. Mỗi điểm là một quyết định riêng, có thể kết hợp với A hoặc B.

| Điểm | Hiện trạng | Bằng chứng | Đề xuất | Mức |
|------|-----------|------------|---------|-----|
| D-a. V9 | 4 UC 08.1–08.4 | B-V9 đã tự gộp 08.1–08.3 thành một luồng liền mạch cùng actor PM + Tài chính, cùng đối tượng DanhGiaChiPhi; P1 I.1.3.9 mô tả V9 là một chuỗi 6 bước liên tục, các bước 4–5 là điều kiện của nhau. Riêng 08.4 có actor khác (PMO/CEO quyết định, CN-128, CN-129) | Chấp nhận UC-08.1 mở rộng gồm 08.1+08.2+08.3, giữ UC-08.4 riêng. Giữ mã 08.2, 08.3 dưới dạng "đã gộp vào 08.1", không đánh lại mã | D |
| D-b. V7 | 06.1, 06.2, 06.3 | B-V7 gộp 06.1 vào 06.2. Tuy nhiên P1 tách rõ bước 1–2 (phát hiện, phân tích) với bước 3–5 (đàm phán, làm mịn, san bằng) và bước 6 (PMO/CEO phân xử). 06.3 có actor và thời hạn riêng | Giữ 3 UC. Yêu cầu B-V7 trả 06.1 và 06.3 về đúng chỗ; nếu cần thể hiện phân xử, dùng `<<extend>>` từ 06.3 vào 06.2 có điều kiện "hết 3 ngày hoặc bế tắc" | C ở B-V7, không đổi danh mục |
| D-c. V8 | 07.1–07.4 | 07.2 (giải trình) chỉ xảy ra khi 07.1 kết luận chưa đủ cơ sở; B-V8 đã vẽ nó như extend của 07.1 | Giữ 4 UC; quan hệ 07.2 `<<extend>>` 07.1 là hợp lý | B |
| D-d. V2 | 01.1, 01.2, 01.3 | Ranh giới 01.3 chỉ "phản hồi từ bước sau" (HD-PCCN §3), nhưng B-V2b cho 01.3 xử lý cả việc RM trả lại | Giữ 3 UC, làm rõ ranh giới (D-06) | C |
| D-e. V5 | 04.1, 04.2, 04.3 | Không có bằng chứng trùng | Giữ | A |

Nếu áp dụng D-a, số UC chi tiết giảm từ 28 xuống 26. Không có bằng chứng để giảm thêm.

## 3. Bảng so sánh

| Tiêu chí | A. Giữ 9 nhóm | B. Gom 6 chức năng lớn (trình bày) | C. Đổi ranh giới 5–6 phân hệ | D. Điều chỉnh UC chọn lọc (D-a) |
|----------|---------------|-------------------------------------|-------------------------------|----------------------------------|
| Phù hợp Phần I | Cao, ánh xạ 1–1 V↔nhóm | Cao, vẫn giữ V bên dưới | Trung bình, phải giải thích lại ánh xạ V→phân hệ mới | Cao, dựa trên chính luồng V9 |
| Bao phủ nghiệp vụ | Như nhau | Như nhau | Như nhau | Như nhau |
| Rõ ranh giới chức năng | Rõ nhưng nhiều nhóm nhỏ | Rõ hơn: mỗi chức năng lớn gắn một đối tượng chính | Rõ nếu làm tốt, nhưng dễ tạo ranh giới mới chưa kiểm chứng | Rõ hơn ở V9 |
| Trùng lặp, giao thoa | Không đổi | Không đổi | Có thể giảm nhẹ | Giảm ở V9 |
| Giữ được bài hiện tại | Toàn bộ | Toàn bộ | Phải đổi mã, tiêu đề, bảng truy vết trong mọi bài | Giữ B-V9; chỉ sửa ghi chú mã |
| Số UC phải điều chỉnh vì phương án | 0 | 0 | 28 (đổi mã) | 3 (08.1 mở rộng, 08.2, 08.3 ghi "đã gộp") |
| Số thành viên bị ảnh hưởng | 0 | 0 (chỉ người vẽ II.1) | 9 | 1 (V9) |
| Khối lượng sửa sơ đồ, tài liệu | Không | Vẽ II.1 và đoạn dẫn II.2 | Lớn: UCD, bảng BR, ma trận | Nhỏ |
| Tác động mô hình lớp | Không | Không | Không trực tiếp | Không (lớp V9 đã viết cho phạm vi gộp) |
| Tác động Sequence / Communication / State | Không | Không | Phải đổi tên tham chiếu UC | Không |
| Rủi ro mâu thuẫn mới | Thấp | Thấp | Cao: mã cũ vẫn nằm trong Phần I, I.3, CN | Thấp |

## 4. Khuyến nghị

[Đề xuất] **Phương án B kết hợp D-a.** Lý do:

- Đáp ứng mong muốn trình bày gọn 5–6 nhóm mà không động tới cấu trúc nghiệp vụ đã khớp Phần I.
- Không bắt 9 thành viên sửa lại mã hay tiêu đề.
- D-a hợp thức hóa cái B-V9 đã làm thay vì bắt làm lại, và có căn cứ rõ trong P1 I.1.3.9.
- Công sức của nhóm nên dành cho vấn đề thật: thống nhất mô hình đối tượng và lấp ba UC nền tảng chưa có chủ (tài liệu 07).

Không khuyến nghị C: chi phí lớn, không giải quyết vấn đề nào audit phát hiện, và tạo hai hệ mã song song với Phần I.

## 5. Nếu chọn B: những gì cần thay đổi

| Việc | Ai | Tài liệu |
|------|----|----------|
| Vẽ II.1: 6 chức năng lớn, 6 actor, association theo P1 I.1.2 | V10/trưởng nhóm | Xem 09 mục 4 |
| Viết đoạn dẫn II.2 cho mỗi chức năng lớn, liệt kê UC chi tiết bên dưới | Trưởng nhóm | |
| Thêm cột "Chức năng lớn" vào bảng PCCN (HD-PCCN §1), không đổi mã | Trưởng nhóm | |
| Bài thành viên: **không cần sửa** vì lý do phương án B | | |

Lưu ý phân biệt: gom nhóm trình bày **không** làm mất các package V2..V10. Nếu giảng viên hỏi "phân hệ" là gì, câu trả lời nhất quán là: 6 chức năng lớn để đọc sơ đồ, 9 vùng nghiệp vụ là đơn vị truy vết với Phần I.
