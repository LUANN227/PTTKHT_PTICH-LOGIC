# Danh sách chờ quyết định (nội bộ, không đưa vào báo cáo)

Bản rà soát 22/10/2026. Mỗi mục là một đề xuất. Mục nào chưa được trưởng nhóm chốt thì chưa phải quyết định.

## Hợp nhất mã

Bản tích hợp ngày 20/10 và gói ChatGPT dùng chung ký hiệu Q-01..Q-09 nhưng với nội dung khác nhau. Danh sách này đánh lại thành **QĐ-01..QĐ-20**. Cột "Mã cũ" ghi mã tương ứng trong từng nguồn.

Viết tắt trong cột "Mã cũ":

- **GPT** = `CHOT_NOI_DUNG_CHUNG.md` của ChatGPT.
- **TH** = bản tích hợp: II.3 §5, `KE_HOACH_SUA_THANH_VIEN.md` §4, `Bang_doi_chieu_PCCN.md`.

## Các mục cần chốt

| Mã | Câu hỏi | Mã cũ | Đề xuất | Căn cứ | Ảnh hưởng nếu chưa chốt |
|---|---|---|---|---|---|
| QĐ-01 | PMO có tham gia V4 không? Bảng vai trò I.1.2 không có, nhưng CN-37 và CN-43 có | GPT Q-01; TH D-P3-01 | Có. Bổ sung V4 vào cột "Tham gia tại" của PMO trong I.1.2 | CN-37, CN-43 | II.1 và UCD UC-03 đang vẽ PMO; Phần I chưa khớp |
| QĐ-02 | Bộ tên trạng thái duy nhất của NhuCauNguonLuc | GPT Q-02; TH Q-01 (II.3), D-07 | Dùng các tên có trong CN: đang xây dựng, đã chuyển RM, đã xác nhận, cần bổ sung (trả lại) | CN-03, CN-11, CN-13, CN-14 | V2a, V2b, State Machine NhuCauNguonLuc |
| QĐ-03 | UC cá nhân của V3 (02.1 hay 02.2) và của V8 (07.1 hay 07.3) | GPT Q-03; TH D-05, TT-02, TT-04 | Giữ 02.1 và 07.1. FDS tóm tắt 02.2, 07.3 trong bản Word đã đủ cho phần chung | HD-PCCN §5; Outline | Phân công II.4 của V3, V8 |
| QĐ-04 | Ngưỡng "dưới 24–48 giờ" có cần chốt thành một con số không? | GPT Q-04; TH D-17 | Không. Giữ nguyên văn P1 | CN-58 | Guard trên AD 04.1 |
| QĐ-05 | Bội số còn để trống trong II.3 (danh sách bên dưới) | GPT Q-05; TH Q-02, Q-06 | Xem đề xuất từng dòng ở bảng bội số | PCN-02; CN-99, CN-101, CN-102 | II.3 Hình II.3-2 đến II.3-6; Sequence, State của V6, V8 |
| QĐ-06 | Khoảng 100–120% không thuộc rõ mức nào của thang 5 mức | GPT Q-06 | Không sửa P1. Trong Phần II chỉ dùng đúng điều kiện có nguồn (QT-33, CN-70) | Thang 5 mức; QT-33 | AD 06.1, 06.2 |
| QĐ-07 | Công thức tỷ lệ vượt ngân sách, đơn vị và trường hợp ngân sách còn lại ≤ 0 | GPT Q-07; TH D-20 | Trưởng nhóm hoặc V9 đề xuất một công thức, ghi là quy ước của nhóm | QT-51 | FDS 08.2, D 08.1 A2, AD V9 |
| QĐ-08 | V10 có dự báo một phần khi nguồn cung thiếu dữ liệu không? Danh sách nhu cầu rỗng xử lý thế nào? | GPT Q-08; TH D-V10 | Giữ như bản Word: dừng trước dự báo chính thức; không coi rỗng là cầu bằng 0 | QT-55; CN-113, CN-116 | D, AD 09.1, 09.2 |
| QĐ-09 | Câu ở I.3.9 bước 7 là điều kiện bắt buộc chuyển hay căn cứ để RM cân nhắc? | GPT Q-09 | Căn cứ để RM cân nhắc; quyết định vẫn do RM ghi (CN-121) | CN-121; I.1.3.10; I.3.9 | 09.1 bước 8 |
| QĐ-10 | UC trọng tâm của V9: 08.1 đúng phạm vi mã, hay gộp 08.1–08.3 (hoặc cả 08.4)? | TH D-03 | 08.1 đúng phạm vi CN-103–107. Nội dung đã viết chuyển sang FDS 08.2–08.4 | HD-PCCN §1; bảng II.1 | D, AD V9; bảng II.1 đang ghi theo đề xuất này |
| QĐ-11 | YeuCauNguonLuc (CN-127) có là lớp riêng không? | TH Q-03 | Chưa vẽ trong bản chính. CN-127 là bước tiếp nhận của 04.1 | CN-47, CN-127 | II.3; lớp V5 |
| QĐ-12 | UC-01.3 bắt đầu theo hai cách: extend từ 01.2 và phản hồi V4/V10 | TH D-06 | Chấp nhận cả hai. Giữ extend 01.3 → 01.2 trên UCD | CN-14, CN-17 | UCD UC-01; D 01.3 |
| QĐ-13 | CN-73 (hạn 3 ngày của phương án đang xây dựng) thuộc 05.1 hay 05.2? | TH D-11, DA-27 | 05.1, như bảng II.1 đang ghi: đây là trạng thái trong lúc lập phương án | CN-73; QT-31 | D, AD 05.1; HD-PCCN |
| QĐ-14 | Ứng viên tuyển ngoài có là NguonLuc không? | TH Q-04 | Có, phân biệt bằng `loaiNguon` | CN-33 | II.3; lớp V4 |
| QĐ-15 | Thuộc tính `mucDapUngVaiTro`, `khoangThieu` của HoSoNangLuc | mới | Kết quả này phụ thuộc vai trò được đối chiếu (CN-26, CN-27). Một hồ sơ không thể có một giá trị duy nhất. Đề xuất: bỏ khỏi HoSoNangLuc; xem là kết quả tính khi đối chiếu với một vai trò, hiển thị ở 02.2 và 03.3 (CN-42) | CN-26, CN-27, CN-42 | II.3 Hình II.3-2 hiện vẫn giữ hai thuộc tính theo nguồn nhóm |
| QĐ-16 | DeXuatThayDoi có giữ là lớp không? | TH Q-09 | Giữ. QT-39 nêu rõ "đề xuất thay đổi do san bằng nguồn lực" là đối tượng phải qua V8 | QT-39; CN-86 | Đã vẽ trong Hình II.3-4 |
| QĐ-17 | Thứ tự UC cá nhân, người vẽ sơ đồ II.4 liên vùng | – | Theo bảng phân công II.4 | Outline | II.4 |
| QĐ-18 | Sửa bảng Summary của HD-PCCN (P-01..P-12) | TH P-01..P-12 | Theo `Bang_doi_chieu_PCCN.md` | HD-PCCN; P1 | HD-PCCN khác bảng II.1 |
| QĐ-19 | DoA và ngưỡng 10% có vẽ thành lớp không? | TH Q-08 | Không. Giữ là quy tắc nghiệp vụ | QT-40, QT-51 | Lớp V8, V9 |
| QĐ-20 | Quy ước đánh số mục và chú thích hình | TH TB-01 | Theo bản Word: Hình II.x-n, Bảng II.x-n | Cấu trúc P1 | Trình bày |

## Bội số còn để trống (QĐ-05)

Trong II.3, các quan hệ dưới đây không ghi bội số, vì nguồn chưa đủ để quyết định. Cột "Đề xuất" là đề xuất của bản rà soát. Chỉ ghi lên hình sau khi trưởng nhóm chốt.

| Quan hệ | Hình | Đề xuất | Lý do |
|---|---|---|---|
| NguonLuc — HoSoNangLuc | II.3-2 | 1 — 1 | PCN-02 nói hồ sơ năng lực tập trung, mỗi nguồn lực một hồ sơ |
| NguonLuc — LichNguonLuc | II.3-3 | 1 — 1 | Lịch nguồn lực tập trung; các lần phân bổ là PhanBoNguonLuc |
| KetQuaDanhGiaPhuHop — KetLuanKhaNangThamGia ("shortlist") | II.3-3 | 1 — 0..1 | Chỉ ứng viên trong shortlist mới được V5 đánh giá; mỗi người có một kết luận |
| ChiTietBoTri — PhanBoNguonLuc ("Locked Baseline tạo phân bổ cứng") | II.3-4 | 0..1 — 0..1 | Chỉ dòng của phương án đã xác lập Locked Baseline mới tạo phân bổ cứng (CN-99) |
| PhuongAnBoTri — HoSoTrinhDuyet | II.3-4 | 1 — 0..* | Một phương án có thể trình lại sau khi chỉnh sửa (CN-101, CN-102) |
| ChiTietBoTri — DonGia | II.3-5 | 0..* — 1 | Mỗi dòng bố trí tính theo một đơn giá áp dụng |
| HoSoTrinhDuyet — KetQuaDuBao ("tham chiếu") | II.3-6 | 0..* — 0..1 | Hồ sơ xem kết quả dự báo mới nhất nếu có (CN-94) |

## Đã xử lý, không cần chốt

| Mục | Kết quả | Căn cứ |
|---|---|---|
| D-18 (A3, A4 của V7) | Bỏ tỷ lệ 50/50 và thuê ngoài khẩn vì P1 không có; giữ tham chiếu làm thêm giờ Mức 5 | Thang 5 mức; QT-37 |
| Ngưỡng "trên 110% kéo dài trên 2 tuần", "2 ngày làm việc", "1 ngày làm việc" trong FDS | Có nguồn | QT-41, QT-43, QT-42; CN-84 |
| Mốc "quá 6 tháng" của V4 | Có nguồn gián tiếp: đánh giá lại định kỳ 6 tháng | CN-20 |
| Mã "D07", "D08–D09" trong FDS ChatGPT | Không có trong P1 hay danh sách quyết định; đã bỏ khỏi bản Word | – |
| PMO trên UCD 03.3 của V4 | Hình gốc đã có PMO. Bảng kiểm 20/10 ghi sai | Hình UCD trong `V4 - Phần II.docx` |
