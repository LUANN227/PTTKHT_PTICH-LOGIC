# Sơ đồ phân rã chức năng và đối chiếu PCCN với Phần I

## 1. Sản phẩm

| File | Vai trò |
|---|---|
| `Phan_ra_chuc_nang.drawio` | **Nguồn chính.** Hình gốc draw.io, sửa trực tiếp từng hộp |
| `Phan_ra_chuc_nang.png`, `.svg` | Bản xuất để chèn vào bài |
| `../_cong_cu/gen_drawio.py` | Script sinh lại file `.drawio` từ danh mục mã (dùng khi đổi hàng loạt) |

Sơ đồ có ba cấp:

- Cấp 0 là hệ thống.
- Cấp 1 là 9 chức năng cấp vùng, UC-01 đến UC-09, tương ứng V2–V10.
- Cấp 2 là 28 UC chi tiết.

Mã và tên giữ nguyên theo HD-PCCN §1. Không thêm, bớt hay đổi mã.

**Về nguồn.** Phần I không có sơ đồ phân rã chức năng. PCCN chỉ có ở dạng bảng trong HD-PCCN §1–2, nên sơ đồ này vẽ lại từ bảng đó. Sau đó từng dòng được đối chiếu với Phần I:

- I.1.2: actor và cột "Tham gia tại".
- I.1.3.2–I.1.3.10: quy trình từng vùng.
- I.2.1.1–I.2.1.9: CN-01..CN-129.

## 2. Kết luận

| Nội dung | Kết quả |
|---|---|
| Cấu trúc 9 vùng / 28 UC | **Khớp.** Mỗi vùng V2–V10 có đúng một UC cấp vùng; không UC chi tiết nào thuộc hai vùng |
| Tên cấp vùng so với tên vùng P1 | Khớp, trừ UC-04: P1 ghi "Đánh giá khả năng tham gia nguồn lực", PCCN bỏ chữ "nguồn lực". Giữ tên PCCN vì là tên mã đã dùng trong mọi bài (không đổi mã) |
| Phân bổ CN | **Có 6 điểm lệch:** V2 ghi mơ hồ; CN-42..46 xếp chung một UC; CN-55, 59, 127 chưa xếp; 07.1 và 07.2 chồng mã; CN-87, 88 không thuộc riêng UC nào; ranh giới 09.1/09.2 |
| Actor chính trong bảng Summary | **Có 7 điểm lệch** so với CN của P1 (mục 4) |
| Mô tả UC-09.2 | Lệch QT-57 và RB-62 (mục 4, dòng P-12) |
| Sơ đồ phân rã có dùng được làm căn cứ cho II.1 và UCD cấp vùng | **Có.** Các điểm lệch nằm ở cột CN và actor của bảng Summary, không làm thay đổi cây chức năng |

## 3. Bảng đối chiếu từng chức năng

Quy ước cột **Kết quả**:

- **Khớp**: đúng P1.
- **Lệch actor**: actor trong HD-PCCN §2 khác người thực hiện các CN trong P1.
- **Lệch CN**: dải CN thiếu, chồng hoặc mơ hồ.

Cột **Vị trí** là vị trí trên sơ đồ, theo dạng cột / hàng. Ví dụ "Cột 3 / hàng 2" là ô thứ hai dưới UC-03.

| Mã | Tên | Vị trí | Nội dung PCCN (HD-PCCN §2: actor; CN) | Kết quả | Căn cứ P1 | Đề xuất (chờ trưởng nhóm) |
|---|---|---|---|---|---|---|
| UC-01 | Xác định nhu cầu nguồn lực | Cột 1 / cấp 1 | V2; CN-01–17 | Khớp | I.2.1.1 | – |
| UC-01.1 | Xây dựng và hoàn thiện nhu cầu | Cột 1 / hàng 1 | PM/RM; "CN-01–CN liên quan…" | Lệch actor, lệch CN | CN-01..11 đều là PM | Actor PM. CN-01–09, 11 (P-01, P-02) |
| UC-01.2 | Xác nhận nhu cầu | Cột 1 / hàng 2 | PM; "CN-xx" | Lệch actor, lệch CN | CN-12, 13, 14, 16 là RM | Actor RM. CN-12–14, 16 (P-01, P-03) |
| UC-01.3 | Điều chỉnh nhu cầu theo phản hồi | Cột 1 / hàng 3 | PM/RM; "CN-xx" | Lệch actor, lệch CN | CN-10, 15, 17 là PM | Actor PM. CN-10, 15, 17 (P-01) |
| UC-02 | Đánh giá năng lực nguồn lực | Cột 2 / cấp 1 | V3; CN-18–30 | Khớp | I.2.1.2 | – |
| UC-02.1 | Quản lý tiêu chí đánh giá năng lực | Cột 2 / hàng 1 | RM; CN-18–19 | Khớp (thiếu actor phụ) | CN-19: PMO phê duyệt tiêu chí tạm | Thêm PMO là actor phụ trên UCD cấp vùng |
| UC-02.2 | Đánh giá năng lực nguồn lực | Cột 2 / hàng 2 | RM; CN-20–27 | Khớp (thiếu actor phụ) | CN-21: Nguồn lực khai báo | Thêm Nguồn lực là actor phụ |
| UC-02.3 | Xác nhận và cập nhật hồ sơ năng lực | Cột 2 / hàng 3 | RM/PMO; CN-28–30 | Khớp | CN-28 PMO; CN-29, 30 RM | – |
| UC-03 | Tìm kiếm và đánh giá mức độ phù hợp | Cột 3 / cấp 1 | V4; CN-31–46 | Khớp | I.2.1.3 | – |
| UC-03.1 | Xác lập tiêu chí tìm kiếm và đánh giá | Cột 3 / hàng 1 | RM; CN-31–32 | Khớp | | – |
| UC-03.2 | Tìm kiếm ứng viên | Cột 3 / hàng 2 | RM; CN-33 | Khớp | | – |
| UC-03.3 | Đánh giá, xếp hạng và lập shortlist ứng viên | Cột 3 / hàng 3 | RM; CN-34–41 | Khớp CN, thiếu actor phụ | CN-37: PMO phê duyệt miễn trừ | Thêm PMO là actor phụ (P-09) |
| UC-03.4 | Điều chỉnh kết quả đánh giá | Cột 3 / hàng 4 | RM/PMO; CN-42–46 | Lệch CN | Chỉ CN-43 là điều chỉnh. CN-42 (xem khoảng thiếu shortlist), 44 (lưu), 45 (bàn giao V5) là phần cuối 03.3. CN-46 là phản hồi V2 | 03.4 = CN-43; CN-42, 44, 45 → 03.3; CN-46 theo D-16 (P-04) |
| UC-04 | Đánh giá khả năng tham gia | Cột 4 / cấp 1 | V5; CN-47–59, 127 | Khớp | I.2.1.4 | – |
| UC-04.1 | Đánh giá khả năng tham gia | Cột 4 / hàng 1 | RM/PM; CN-47–52, 58 | Lệch CN | CN-55, 59, 127 không thuộc UC nào | Thêm CN-55, 59, 127 vào 04.1 (P-05) |
| UC-04.2 | Xử lý phương án tham gia một phần | Cột 4 / hàng 2 | RM/PM; CN-53–54 | Khớp | CN-53 RM; CN-54 PM | – |
| UC-04.3 | Xử lý trường hợp vượt tải ngoại lệ | Cột 4 / hàng 3 | RM/PMO/CEO; CN-56–57 | Khớp | CN-56 RM; CN-57 PMO, CEO | – |
| UC-05 | Lập phương án bố trí nguồn lực | Cột 5 / cấp 1 | V6; CN-60–73 | Khớp | I.2.1.5 | – |
| UC-05.1 | Xây dựng phương án bố trí | Cột 5 / hàng 1 | RM/PM; CN-60–68 | Lệch actor (nhẹ) | CN-60..68 đều là RM; PM chỉ nhận ở CN-68 | Actor chính RM; PM không nối với 05.1 |
| UC-05.2 | Rà soát phương án bố trí | Cột 5 / hàng 2 | PM; CN-69–73 | Lệch actor | CN-69 PM; CN-70–73 RM | Actor PM và RM (P-06) |
| UC-06 | Xử lý xung đột và cân đối nguồn lực | Cột 6 / cấp 1 | V7; CN-74–88 | Khớp | I.2.1.6 | – |
| UC-06.1 | Phân tích và đánh giá xung đột | Cột 6 / hàng 1 | PM/RM; CN-74–77 | Khớp | CN-74, 75, 77 RM; CN-76 PM | – |
| UC-06.2 | Cân đối nguồn lực | Cột 6 / hàng 2 | PM/RM; CN-78–82 | Khớp | | – |
| UC-06.3 | Phân xử xung đột | Cột 6 / hàng 3 | PMO/CEO/PM; CN-83–88 | Lệch actor, lệch CN | CN-83 RM chuyển cấp; P1 không có PM ở bước phân xử. CN-87 (nhật ký) và CN-88 (bàn giao) chạy cả khi không phân xử | Actor RM, PMO, CEO. CN-87, 88 ghi "dùng chung UC-06.1–06.3" (P-07) |
| UC-07 | Rà soát và phê duyệt phương án | Cột 7 / cấp 1 | V8; CN-89–102 | Khớp | I.2.1.7 | – |
| UC-07.1 | Rà soát và đánh giá phương án | Cột 7 / hàng 1 | "PMO/Portfolio Manager"; CN-89–94 | Khớp CN; tên actor lệch | P1 I.1.2 dùng "PMO/Quản lý danh mục" | Dùng tên P1 (P-10) |
| UC-07.2 | Yêu cầu giải trình và hoàn thiện phương án | Cột 7 / hàng 2 | PMO/RM; CN-91–96 | Lệch CN | CN-91–94 đã thuộc 07.1 | 07.2 = CN-95, 96 (P-08) |
| UC-07.3 | Phê duyệt phương án | Cột 7 / hàng 3 | PMO/CEO; CN-97, 99–102 | Khớp | CN-97 "cấp có thẩm quyền theo DoA" | – |
| UC-07.4 | Phê duyệt ngoại lệ | Cột 7 / hàng 4 | PMO/CEO; CN-98 | Khớp | | – |
| UC-08 | Đánh giá tác động chi phí và ngân sách | Cột 8 / cấp 1 | V9; CN-103–112, 128, 129 | Khớp | I.2.1.8 | – |
| UC-08.1 | Tính và cập nhật chi phí phương án | Cột 8 / hàng 1 | Tài chính/RM; CN-103–107 | Lệch actor | CN-103, 104 PM; 105–107 Tài chính. RM không tham gia V9 (I.1.2) | Actor PM, Tài chính (P-11) |
| UC-08.2 | Đối chiếu chi phí và ngân sách | Cột 8 / hàng 2 | Tài chính; CN-108–109 | Lệch actor | CN-108 "Tài chính và PM"; CN-109 "PM và Tài chính" | Actor Tài chính, PM (P-11) |
| UC-08.3 | So sánh đánh đổi giữa các phương án | Cột 8 / hàng 3 | Tài chính/RM/PM; CN-110 | Lệch actor | CN-110 chỉ PM | Actor PM (P-11) |
| UC-08.4 | Xác định hướng xử lý và chuyển cấp ngân sách | Cột 8 / hàng 4 | Tài chính/PMO/CEO; CN-111, 112, 128, 129 | Lệch actor | CN-111, 112 PM; 128 CEO; 129 PMO | Actor PM, PMO, CEO (P-11) |
| UC-09 | Theo dõi và dự báo nguồn lực | Cột 9 / cấp 1 | V10; CN-113–126 | Khớp | I.2.1.9 | – |
| UC-09.1 | Tổng hợp và phân tích cung – cầu nguồn lực | Cột 9 / hàng 1 | PMO; CN-113–121 | Lệch actor, ranh giới CN | CN-113..126 chủ yếu là RM; PM ở CN-114, 123 | Actor RM, PM. CN theo D-V10-01 |
| UC-09.2 | Dự báo cung – cầu nguồn lực | Cột 9 / hàng 2 | PMO; CN-122–126; "dữ liệu lịch sử", "khuyến nghị" | Lệch actor, lệch nội dung | QT-57: dự báo theo dữ liệu hiện có. RB-62: V10 không ra quyết định | Actor RM. Bỏ "lịch sử", "khuyến nghị" (P-12; D-V10-02) |

## 4. Điểm cần sửa trong HD-PCCN

Sơ đồ phân rã không bị ảnh hưởng. Các điểm dưới đây chỉ sửa ở **bảng Summary (HD-PCCN §2)**, do người giữ HD-PCCN thực hiện sau khi trưởng nhóm chốt. Tài liệu này không sửa HD-PCCN.

| Mã | Nội dung | Đề xuất | Ghi nhận ở |
|---|---|---|---|
| P-01 | Cột CN của V2 ghi "CN-01–CN liên quan…", "CN-xx" | 01.1 = CN-01–09, 11; 01.2 = CN-12–14, 16; 01.3 = CN-10, 15, 17. Cách chia này trùng với bản V2b mới | Bảng giao việc PC-01 |
| P-02 | 01.1 actor "PM/RM" | PM | PC-02 |
| P-03 | 01.2 actor "PM" | RM | PC-02 |
| P-04 | 03.4 = CN-42–46 | 03.4 = CN-43; CN-42, 44, 45 → 03.3; CN-46 theo D-16 | PC-03 |
| P-05 | CN-55, 59, 127 chưa thuộc UC nào | Đưa vào 04.1 | PC-04 |
| P-06 | 05.2 actor chỉ PM | PM, RM | PC-02 |
| P-07 | 06.3 có PM; CN-87, 88 xếp vào 06.3 | Actor RM, PMO, CEO; CN-87, 88 dùng chung cả vùng | PC-05 |
| P-08 | 07.2 = CN-91–96, chồng 07.1 | 07.2 = CN-95, 96 | PC-03 |
| P-09 | PMO tham gia V4 (CN-37, 43) nhưng P1 I.1.2 không liệt kê V4 cho PMO | Xem D-P3-01 | PC-06 |
| P-10 | "Portfolio Manager" | "PMO/Quản lý danh mục" | PC-02 |
| P-11 | Actor V9 có RM; 08.2 thiếu PM | Theo bảng mục 3 | PC-02 |
| P-12 | 09.x actor PMO; 09.2 nhắc "dữ liệu lịch sử", "khuyến nghị" | Actor RM; bỏ hai cụm từ | D-V10-02 |

## 5. Mâu thuẫn trong chính Phần I

### D-P3-01: PMO có tham gia V4 không

| Nguồn | Nội dung |
|---|---|
| P1 I.1.2, cột "Tham gia tại" của PMO | V3, V5, V7, V8, V9. Không có V4 |
| P1 CN-37 | PMO/Quản lý danh mục phê duyệt đề nghị miễn trừ điều kiện bắt buộc (V4) |
| P1 CN-43 | Điều chỉnh xếp hạng hoặc shortlist có hiệu lực khi PMO/Quản lý danh mục phê duyệt (V4) |

**Cách đang dùng trong bản đề xuất này:**

- II.1 và UCD UC-03 có association PMO–UC-03 (03.3, 03.4).
- Lý do: CN mô tả hành vi cụ thể của hệ thống, còn I.1.2 là bảng tóm tắt.

**Chưa sửa Phần I.** Trưởng nhóm chọn một trong hai cách:

- (a) bổ sung V4 vào cột "Tham gia tại" của PMO trong I.1.2;
- (b) bỏ PMO khỏi CN-37, CN-43.

Nếu chọn (b), xóa association PMO–UC-03 trong II.1 và UCD UC-03.
