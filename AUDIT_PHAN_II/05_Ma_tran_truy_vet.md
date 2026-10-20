# 05. Ma trận truy vết Phần I → Phần II (sơ bộ)

Ma trận theo nhóm CN. Cột "UC (PCCN)" là ánh xạ hiện có trong HD-PCCN §2; cột "UC đề xuất" chỉ ghi khi audit thấy ánh xạ PCCN chưa đúng (đề xuất, chờ trưởng nhóm). Ký hiệu cột Desc/AD/Lớp: **✓** có và đúng mã; **✓\*** có nội dung nhưng trích mã ngoài baseline; **~** có một phần hoặc nằm ở bài khác; **–** chưa có.

## 1. Ma trận CN → UC → sản phẩm

### V2 (CN-01..17)

| CN | Nội dung | UC (PCCN) | UC đề xuất | Desc | AD | Lớp | Ghi chú |
|----|----------|-----------|------------|------|----|-----|---------|
| 01, 02 | Tra cứu dự án, chọn công việc | "CN-01–…" (01.1) | 01.1 | ✓\* | ✓ | ✓ (DuAn, CongViec) | B-V2a gọi CN-01 là "khởi tạo hồ sơ nhu cầu" – không đúng nội dung |
| 03 | Yêu cầu bổ sung, nhu cầu chưa cố định | 01.1 | 01.1 | – | – | – | Thiếu nhánh |
| 04, 05 | Loại nguồn lực, yêu cầu kỹ năng | 01.1 | 01.1 | ✓\* (CN-V2-01) | ✓ | ~ (KyNangChuyenMon) | |
| 06 | Quy mô FTE theo giai đoạn | 01.1 | 01.1 | ~ | ~ | – | Thiếu lớp/thuộc tính giai đoạn |
| 07, 08 | Thời điểm, %FTE | 01.1 | 01.1 | ~ | ~ | – | Không có thuộc tính mức tham gia |
| 09, 10 | Tra cứu, cập nhật nhu cầu | 01.1 | 01.1 / 01.3 | ~ | – | – | B-V2b dùng CN-10 cho 01.3 |
| 11 | Chuyển RM | 01.1 | 01.1 | – | – | – | **Thiếu**: không nối được 01.1→01.2 |
| 12, 13 | RM tra cứu, xác nhận | 01.2 | 01.2 | ✓ | ✓ | – (B-V2b chưa làm §7–12) | |
| 14 | RM chuyển lại PM | 01.2 | 01.2 | ✓ | ✓ | – | |
| 15 | PM xem kết quả xem xét | 01.3 | 01.2/01.3 | ✓ | ✓ | – | |
| 16 | Bàn giao V3, V4 | 01.2 | 01.2 | ✓ | ✓ | – | |
| 17 | Nhận phản hồi V4, V10 | 01.3 | 01.3 | ✓ | ✓ | – (PhanHoiNhuCau mới ở §6) | |

### V3 (CN-18..30)

| CN | Nội dung | UC (PCCN) | Desc | AD | Lớp | Ghi chú |
|----|----------|-----------|------|----|-----|---------|
| 18 | Danh mục kỹ năng, tiêu chí, thang 5 mức | 02.1 | ✓\* | ✓ | ~ | B-V3 ghi "số cấp chưa xác định (Q-04)" trái CN-18 |
| 19 | Tiêu chí tạm, PMO duyệt | 02.1 | – | – | – | **Thiếu** trong B-V3 |
| 20–27 | Xác định nguồn lực cần đánh giá, khai báo, đánh giá, trạng thái, đối chiếu vai trò, khoảng thiếu | 02.2 | – | – | – | **Chưa có UC** |
| 28–30 | PMO xác nhận cấp cuối, lưu hồ sơ, tra cứu | 02.3 | – | – | – | **Chưa có UC** |

### V4 (CN-31..46)

| CN | Nội dung | UC (PCCN) | UC đề xuất | Desc | AD | Lớp | Ghi chú |
|----|----------|-----------|------------|------|----|-----|---------|
| 31, 32 | Tiếp nhận nhu cầu, xác lập tiêu chí | 03.1 | 03.1 | ~ (tiền điều kiện B-V4) | – | ✓ (BoTieuChi, TieuChi) | |
| 33 | Tìm theo thứ tự nguồn | 03.2 | 03.2 | ~ | – | ✓ (UngVien.nguonUngVien) | |
| 34–41 | Phân loại, xung đột lợi ích, cảnh báo, miễn trừ, điểm, xếp hạng, shortlist | 03.3 | 03.3 | ✓ | ✓ | ✓ | B-V4 đạt |
| 42 | Xem mức đáp ứng, khoảng thiếu | 03.4 | **03.3** | ✓ | ✓ | ✓ | B-V4 đã đặt đúng ở 03.3 |
| 43 | Điều chỉnh có PMO duyệt | 03.4 | 03.4 | – | – | – | |
| 44 | Lưu tiêu chí, trọng số, kết quả mỗi lần | 03.4 | **03.3** | ✓ | ✓ | ✓ (PhienDanhGia) | |
| 45 | Bàn giao V5 | 03.4 | **03.3** (và 03.4 khi có điều chỉnh) | ~ | – | – | |
| 46 | Phản hồi V2 | 03.4 | **03.2** (khi tìm hết nguồn) | – | – | – | B-V4 ghi "cần nhóm chốt UC phụ trách" |

### V5 (CN-47..59, 127)

| CN | Nội dung | UC (PCCN) | UC đề xuất | Desc | AD | Lớp | Ghi chú |
|----|----------|-----------|------------|------|----|-----|---------|
| 127 | PM gửi yêu cầu nguồn lực + khung thời gian | không gán | 04.1 (trigger) | ~ | ~ | ~ (YeuCauNguonLuc) | Xem D-13 |
| 47–52 | Tiếp nhận, tra lịch, khả dụng, ngưỡng, 4 trạng thái, dữ liệu chưa rõ | 04.1 | 04.1 | ✓\* | ✓ | ✓ | |
| 53, 54 | Đề xuất một phần, PM xác nhận | 04.2 | 04.2 | ~ (A4) | ~ | ✓ | |
| 55 | Ghi xung đột, chuyển V7 | không gán | 04.1 | ✓\* | ✓ | – | |
| 56, 57 | Vượt tải ngoại lệ, PMO/CEO duyệt | 04.3 | 04.3 | ~ (A5) | ~ | ✓ (HoSoVuotTaiNgoaiLe) | |
| 58 | Đánh giá nhanh yêu cầu gấp | 04.1 | 04.1 | ✓\* | ✓ | – | B-V5 nói "không tự chốt 24 hoặc 48 giờ", nhưng P1 đã ghi "dưới 24–48 giờ" |
| 59 | Tổng hợp, bàn giao V6 | không gán | 04.1 | ✓\* | ✓ | ✓ | |

### V6 (CN-60..73)

| CN | Nội dung | UC (PCCN) | UC đề xuất | Desc | AD | Lớp | Ghi chú |
|----|----------|-----------|------------|------|----|-----|---------|
| 60–68 | Xem, tra cứu, lập phương án chính/thay thế/duy nhất/chấp nhận một phần, gửi PM | 05.1 | 05.1 | ✓ | ✓ | ✓ | B-V6 đạt |
| 69 | PM xác nhận / yêu cầu điều chỉnh | 05.2 | 05.2 | ~ (A4 B-V6) | ~ (AD B-V6) | – | |
| 70 | Đánh dấu nghi ngờ xung đột | 05.2 | 05.2 | – | – | – | **Chưa có** |
| 71, 72 | Tổng hợp hồ sơ, chuyển V7 hoặc V8+V9 | 05.2 | 05.2 | – | – | – | **Chưa có** |
| 73 | Hạn 3 ngày "đang xây dựng" | 05.2 | **05.1** | ✓ (E1) | ~ | ✓ | B-V6 đặt ở 05.1 hợp lý hơn |

### V7 (CN-74..88)

| CN | Nội dung | UC (PCCN) | Desc | AD | Lớp | Ghi chú |
|----|----------|-----------|------|----|-----|---------|
| 74–77 | Xác định Mức, xem V10, PM đánh giá ảnh hưởng, kịch bản CPM | 06.1 | ✓\* (trong 06.2) | ✓ | ✓ (DiemXungDotNguonLuc) | Lấn |
| 78–82 | Đàm phán, làm mịn, san bằng, đề xuất lùi mốc/cắt phạm vi | 06.2 | ✓\* | ✓ | ✓ | |
| 83, 84 | Chuyển cấp, PMO phân xử | 06.3 | ✓\* (A1 06.2) | ✓ | ✓ | Lấn |
| 85 | CEO quyết định Mức 4–5 | 06.3 | – | – | – | Thiếu |
| 86 | Đề xuất thay đổi qua V8, CCB | 06.3 | ~ | ~ | ✓ (ChangeRequest) | |
| 87, 88 | Nhật ký, bàn giao V8, V9, V10 | 06.3 | ✓\* (trong 06.2) | ✓ | ✓ | PCCN gán 06.3, nhưng đây là bước kết thúc chung của V7; đề xuất gán 06.2 |

### V8 (CN-89..102)

| CN | Nội dung | UC (PCCN) | UC đề xuất | Desc | AD | Lớp | Ghi chú |
|----|----------|-----------|------------|------|----|-----|---------|
| 89–94 | Tiếp nhận, DoA, chuyển cấp, xem hồ sơ, V9, V10 | 07.1 (91–94 cũng gán 07.2) | 07.1 | ✓ | Drive | ✓ | Bỏ trùng 91–94 khỏi 07.2 |
| 95, 96 | Yêu cầu giải trình, RM cập nhật | 07.2 | 07.2 | ~ (A2 07.1) | Drive | ✓ (YeuCauGiaiTrinh) | |
| 97, 99–102 | Ra quyết định, Locked Baseline, cung cấp V10, trả về V6/V7, lưu vết | 07.3 | 07.3 | – | – | – | **Chưa có** |
| 98 | Điều kiện hoàn trả khi duyệt ngoại lệ | 07.4 | 07.4 | – | – | – | Chưa có |

### V9 (CN-103..112, 128, 129)

| CN | Nội dung | UC (PCCN) | UC nếu chấp nhận D-a | Desc | AD | Lớp | Ghi chú |
|----|----------|-----------|----------------------|------|----|-----|---------|
| 103–107 | Xác định phương án, lượng hóa, đơn giá, dự toán/dự báo, tính lại | 08.1 | 08.1 | ✓\* | Drive | ✓ | |
| 108, 109 | Đối chiếu ngân sách, nguyên nhân | 08.2 | 08.1 | ✓\* | Drive | ✓ | |
| 110 | So sánh đánh đổi | 08.3 | 08.1 | ✓\* | Drive | ✓ | |
| 111 | Hướng xử lý, chuyển cấp | 08.4 | 08.4 | ✓\* (bước 7) | Drive | ✓ | |
| 112 | Chuyển V8, V10 | 08.4 | 08.1 | ✓\* | Drive | – | |
| 128, 129 | CEO / PMO quyết định vượt ngân sách | 08.4 | 08.4 | – | – | – | Thiếu actor quyết định |

### V10 (CN-113..126)

| CN | Nội dung | UC (PCCN) | UC đề xuất | Trạng thái |
|----|----------|-----------|------------|------------|
| 113–115 | Tổng hợp nguồn cung, PM cung cấp nhu cầu, nguồn cung có thể đáp ứng | 09.1 | 09.1 | Chưa |
| 116, 117 | Nhu cầu đủ cơ sở dự báo, nhãn chắc chắn | 09.1 | **09.2** | Chưa |
| 118, 119 | Lập dự báo, đối chiếu cung – cầu dự báo | 09.1 | **09.2** | Chưa |
| 120 | Phân tích thiếu/dư 4 chiều | 09.1 | 09.1 (hiện trạng) và 09.2 (dự báo) | Chưa |
| 121, 123 | Tổng hợp, quyết định chuyển; PM tra cứu | 09.1 | 09.1 | Chưa |
| 122, 124–126 | Chuyển kết quả, xem V9, cập nhật ngoài chu kỳ, chu kỳ tuần | 09.2 | 09.2 | Chưa |

Lý do đề xuất cho V10: HD-PCCN §3 nói "UC-09.1 phản ánh hiện trạng; UC-09.2 hướng tới tương lai và dự báo", nên các CN có chữ "dự báo" (116–119) nên thuộc 09.2. Chi tiết trong 09.

## 2. QT/RB và lớp miền

| Nhóm quy tắc | Đối tượng chịu ràng buộc | Lớp hiện có | Thiếu |
|--------------|--------------------------|-------------|-------|
| QT-01..05 (RB-02..06) | NhuCauNguonLuc | B-V2a NhuCauNguonLuc | Giai đoạn, %FTE, trạng thái chuẩn |
| QT-06..11 (RB-07..12) | Tiêu chí, Hồ sơ năng lực, Kết quả đánh giá năng lực | B-V3 TieuChiDanhGia, MucDo | HoSoNangLuc, NangLucKyNang, ChungChi |
| QT-12..19 (RB-13..20) | BoTieuChiPhuHop, PhienDanhGia, KetQuaDanhGiaPhuHop, Shortlist | B-V4 đủ | — |
| QT-20..26 (RB-21..27, 59) | KetLuanKhaNangThamGia, PhanBoNguonLuc, LichNguonLuc | B-V5 | Chốt tên, chốt thang mức |
| QT-27..31 (RB-28..32) | PhuongAnBoTri, ChiTietBoTri | B-V6 | Cờ nghi ngờ xung đột (UC-05.2) |
| QT-32..39 (RB-33..40) | DiemXungDot, NhatKyXungDot, DeXuatThayDoi, QuyetDinhPhanXu | B-V7 | Nhánh CEO, CCB |
| QT-40..46 (RB-41..47) | Quyết định phê duyệt, lưu vết, Locked Baseline | B-V8 (một phần) | **QuyetDinhPheDuyet, phiên bản phương án** |
| QT-47..51 (RB-48..52, 61) | DanhGiaChiPhi, NganSach | B-V9 | Người quyết định vượt ngân sách |
| QT-52..57 (RB-53..58, 62) | DuBao, KhoangThieuDu | — | Toàn bộ (V10) |

## 3. Bảng ánh xạ mã ngoài baseline → mã Phần I (đề xuất)

Ánh xạ theo **nội dung**, vì không có tài liệu nguồn từng vùng để ánh xạ theo mã. Thành viên kiểm tra lại khi sửa.

### B-V7

| Mã trong bài | Nội dung | Mã P1 đề xuất |
|--------------|----------|---------------|
| CN-01, 02, 03 | Quét lịch, lọc cảnh báo 5 mức | CN-74 |
| CN-04, 05 | CPM, float, kịch bản | CN-77 (và CN-76 cho PM đánh giá) |
| CN-06, 07 | Đàm phán, đếm 3 ngày | CN-78, CN-79 |
| CN-08, 09 | Làm mịn, san bằng | CN-80, CN-81 |
| CN-10 | Đề xuất thay đổi khi bế tắc | CN-82, CN-86 |
| CN-11, 12 | Chuyển cấp, PMO phân xử | CN-83, CN-84 |
| CN-13, 14 | Nhật ký, bàn giao | CN-87, CN-88 |
| QT-01 (RB-01) | ≤100% công suất | QT-32 (RB-33) |
| QT-02 | Ưu tiên theo xếp hạng | QT-34 (RB-35) |
| QT-03 (RB-02) | Làm mịn trong float | QT-35 (RB-36) |
| QT-04 (RB-03) | 3 ngày / 1 ngày | QT-36 (RB-37) |
| QT-05 (RB-04) | Ngưỡng Mức 3 | QT-33 (RB-34) |
| QT-07 | Bế tắc hoàn toàn | QT-37 (RB-38) |
| QT-08 (RB-05) | Nhật ký | QT-38 (RB-39) |
| PCN-04 | Lưu vết vĩnh viễn | PCN-06 (lưu 3 năm), PCN-07 (ghi người thực hiện). Lưu ý: P1 nói "tối thiểu 3 năm", không nói "vĩnh viễn" |

### B-V9

| Mã trong bài | Mã P1 đề xuất |
|--------------|---------------|
| CN-V9-01..05 | CN-103, CN-104 |
| CN-V9-06, 07 | CN-105, CN-106 |
| CN-V9-08 | CN-106 |
| CN-V9-09, 10 | CN-106, CN-107 |
| CN-V9-11..14 | CN-108 |
| CN-V9-15 | CN-109 |
| CN-V9-16..18 | CN-110 |
| CN-V9-19..22 | CN-111 (và CN-128, CN-129 cho cấp quyết định) |
| CN-V9-23, PCN-V9-04 | PCN-08 |
| PCN-V9-05 | PCN-07 |
| RB-V9-02 | CN-103 (P1 không có RB riêng cho "đánh giá dựa trên phương án") |
| RB-V9-03 | QT-48 (RB-49) |
| RB-V9-04 | QT-47 (RB-48) |
| RB-V9-05 | CN-109 |
| RB-V9-06 | QT-50 (RB-51) |
| RB-V9-07, 08 | QT-51 (RB-52) |
| RB-V9-09, 10 | RB-61 |
| RB-V9-11 | CN-112 |
| QT-03 (trong §6.1) | QT-49 (RB-50) |
| Q-02 (đơn vị đơn giá), Q-03 (mức tham gia %) | Q-03 đã được P1 chốt: %FTE (PCN-09). Q-02 chưa có trong P1 → giữ là giả định |

### B-V5

| Mã trong bài | Mã P1 đề xuất |
|--------------|---------------|
| BR-V5-01 | P1 I.1.3.5 câu cuối ("V5 chỉ kết luận khả năng tham gia") – không có mã QT; có thể dẫn QT-20 (RB-21) |
| BR-V5-02 | QT-26 (RB-27), CN-55 |
| BR-V5-03 | QT-21 (RB-22), CN-49 |
| BR-V5-04..06 | QT-22 (RB-23), CN-50 |
| BR-V5-07, 08 | QT-24 (RB-25), CN-52 |
| BR-V5-09..11 | QT-23 (RB-24), CN-53, CN-54 |
| BR-V5-12, 13 | QT-25 (RB-26), CN-56, CN-57 |
| BR-V5-14 | CN-58 |
| CN-V5-01..10, C-V5-01 (ở §7) | CN-47..59, CN-127 tương ứng |

### B-V2a

| Mã trong bài | Mã P1 đề xuất |
|--------------|---------------|
| CN-01 (nội dung "khởi tạo hồ sơ nhu cầu") | CN-01, CN-02 (với đúng nội dung P1) |
| CN-V2-01 | CN-04, CN-05, CN-06 |
| RB-V2-03 | **Không có** trong P1 → bỏ quy tắc hoặc đưa vào Decision Log |

### B-V3

| Mã trong bài | Mã P1 đề xuất |
|--------------|---------------|
| QT-01 | QT-06 (RB-07) |
| QT-02 | QT-07 (RB-08) |
| QT-03, QT-04 | QT-08 (RB-09) |
| Q-04 (số cấp mức độ) | Đã chốt: thang 5 mức (CN-18, PCN-09) |
| "mục 04" | Không rõ; thay bằng P1 I.1.2 |
| Bổ sung cho §3.4 | CN-18, CN-19, QT-06, QT-07, PCN-07 |
