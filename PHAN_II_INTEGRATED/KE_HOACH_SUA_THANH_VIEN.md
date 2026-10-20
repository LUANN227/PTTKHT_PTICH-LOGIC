# Kế hoạch sửa bài thành viên V2–V10

Đây là bảng giao việc tổng hợp duy nhất. Mỗi lỗi chỉ được ghi sau khi đã đối chiếu trên bài thực tế, với các căn cứ sau:

- **Phần I** (P1).
- **HD-PCCN** và **mẫu II.2** (HD-MAU).
- Bài thành viên:
  - V2b: bản mới nhất (`V2-Phan II 2 1.docx`, trưởng nhóm gửi ngày 20/10).
  - V8: ba sơ đồ mới gửi (UCD UC-07.1, AD UC-07.1, sơ đồ lớp).
  - V9: UCD, AD và sơ đồ lớp vẫn chỉ có trên Drive, chưa kiểm tra được hình.

Quy ước của bảng:

- **Mức độ:** NT = nghiêm trọng (sai nghiệp vụ hoặc phạm vi); Cao = UC bắt buộc chưa xong, hoặc mâu thuẫn ảnh hưởng II.1/II.3; TB = mã truy vết, ký pháp UML; Thấp = trình bày.
- **Trạng thái:** *Sẵn sàng sửa* = làm được ngay; *Cần xác nhận* = chờ trưởng nhóm chốt mã Q/D trong mục cuối; *Đã kiểm tra* = đã đúng, không cần sửa.
- **Bảng ánh xạ mã:** `AUDIT_PHAN_II/05_Ma_tran_truy_vet.md` §3.
- **Tên lớp chung:** `II.3_Domain_Class_Diagram/II3_Danh_muc_va_anh_xa.md` §3.

## 0. Yêu cầu chung cho mọi thành viên: UCD cấp vùng

Mỗi vùng phải có **một** UCD bao quát mọi UC con theo danh mục HD-PCCN §1:

- Ranh giới hệ thống đặt tiêu đề bằng tên vùng, ví dụ "UC-03 Tìm kiếm và đánh giá mức độ phù hợp".
- Actor lấy theo P1.
- Chỉ dùng `include`/`extend` khi có căn cứ trong mục 3 của `QUY_UOC_PHAN_II.md`.
- Giữ sơ đồ UC trọng tâm hiện có nếu vẫn đúng.

| Vùng | Người vẽ (chịu trách nhiệm chính) | Hiện trạng | Còn thiếu |
|---|---|---|---|
| UC-01 | V2b (Tuấn Long) | V2a có 01.1; V2b có 01.2 + 01.3 | Gộp thành 1 UCD đủ 01.1–01.3. V2a không vẽ lại |
| UC-02 | V3 | Chỉ 02.1 | 02.2, 02.3; actor Nguồn lực, PMO |
| UC-03 | V4 | Chỉ 03.3 | 03.1, 03.2, 03.4 |
| UC-04 | V5 | Đủ 04.1–04.3 | Đổi tiêu đề "PHÂN HỆ V5" thành "UC-04 Đánh giá khả năng tham gia"; nối RM với 04.2, 04.3 (P1 I.3.4) |
| UC-05 | V6 | Chỉ 05.1; association vẽ thành mũi tên | 05.2; association không mũi tên |
| UC-06 | V7 | Đủ 06.1–06.3 | Bỏ `include` 06.1 (là tuần tự); tiêu đề theo tên vùng |
| UC-07 | V8 | 07.1–07.3 và hai UC ngoài vùng (UC-08, UC-09) | 07.4; bỏ UC-08, UC-09 khỏi sơ đồ |
| UC-08 | V9 | Chỉ có trên Drive | Chèn hình; đủ 08.1–08.4 (hoặc 08.1 gộp + 08.4 nếu chốt D-03) |
| UC-09 | V10 | Đã có: `II.2_V10/UCD_UC-09.png` | Đã kiểm tra |

**Nghiệm thu:** mã và tên trên sơ đồ trùng HD-PCCN §1. Actor là tập con của actor nối với UC-0x trong II.1. Hình nằm trong file nộp, không chỉ là link Drive.

## 1. V2a — Thùy Linh — UC-01.1

| # | Vị trí | Mức | Vấn đề | Căn cứ | Hành động | Hướng sửa | Phụ thuộc | Nghiệm thu | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|
| 1 | §3.3 A2, §3.4, AD decision "FTE ≤ 1.0" | NT | Quy tắc FTE tự thêm | P1 không có; PCN-09 chỉ quy định %FTE 0–100% | Xóa A2 và decision FTE | FTE của nhu cầu là quy mô, không phải tải một người | – | Không còn "≤ 1.0" trong bài và AD | Sẵn sàng sửa |
| 2 | §3.2 cuối, hậu điều kiện | NT | Không có bước gửi RM; UC-01.2 thiếu đầu vào | CN-11 | Thêm bước "PM chuyển nhu cầu hoàn thiện cho RM xác nhận" | Trạng thái sau bước này theo Q-01 | Q-01 | Có bước mang CN-11; hậu điều kiện khớp tiền điều kiện UC-01.2 của V2b | Cần xác nhận (tên trạng thái) |
| 3 | §3.2 | Cao | Thiếu nhánh thông tin chưa đủ | CN-03; P1 I.1.3.2 điểm quyết định 1 | Thêm A: ghi nội dung cần bổ sung | | – | Có A1 mang CN-03, có trên AD | Sẵn sàng sửa |
| 4 | §3.2 bước 6–7 | Cao | Thiếu giai đoạn và %FTE | CN-07, 08; QT-03 | Thêm bước xác định giai đoạn và mức tham gia cho từng vị trí | Theo lớp ViTriCanBoTri | – | Có CN-07, 08 trong BR | Sẵn sàng sửa |
| 5 | §2.1, UCD | Cao | Actor "PM/RM" gộp | P1 I.1.3.2 | Actor chính PM; bỏ RM khỏi UC-01.1 | | – | UCD có một actor PM | Sẵn sàng sửa |
| 6 | §3.4 | TB | Mã CN-V2-xx, RB-V2-xx | Bảng 05 §3 | Đổi mã theo bảng | Không tạo mã mới | – | Mọi mã có trong P1 | Sẵn sàng sửa |
| 7 | §7–11 | TB | KyNangChuyenMon chứa thuộc tính của yêu cầu; CongViec | II.3 §3 | Đổi thành YeuCauKyNang; bỏ CongViec, chuyển phamVi về NhuCauNguonLuc | | Q-05 | Tên lớp trùng II.3 | Cần xác nhận |
| 8 | AD | TB | Hai action không có luồng ra | UML | Nối về action nhập tương ứng | | – | Mọi node có luồng ra | Sẵn sàng sửa |
| 9 | §3.3 E1, AD "Đăng nhập", "Nhấn…" | Thấp | Thao tác giao diện | HD-MAU §3.2 | Bỏ E1; đổi tên action theo nghiệp vụ | | – | Không còn từ "nhấn", "đăng nhập" | Sẵn sàng sửa |

## 2. V2b — Tuấn Long — UC-01.2, UC-01.3 (bản mới)

Đã kiểm tra: §7–12 đã hoàn thành; lập luận không tách lớp "kết quả xem xét" là tốt; bảng BR UC-01.2 đúng mã P1.

| # | Vị trí | Mức | Vấn đề | Căn cứ | Hành động | Hướng sửa | Phụ thuộc | Nghiệm thu | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|
| 1 | UC-01.2 §3.1.3 E1 | NT | E1 gồm cả "PM điều chỉnh nhu cầu", tức là luồng của UC-01.3 nằm trong UC-01.2 | HD-PCCN §3; quan hệ extend do chính bài vẽ | E1 dừng ở "Hệ thống chuyển lại nhu cầu cho PM; mở rộng sang UC-01.3"; đổi mã thành A1 | Extend: UC-01.2 là UC gốc, UC-01.3 chỉ chạy khi có điều kiện | – | E1 không còn bước của PM | Sẵn sàng sửa |
| 2 | §2.2 bảng quan hệ | TB | Ghi "UC-01.3 extend UC-01.3" | Hình UCD | Sửa đích thành UC-01.2 | | – | Bảng khớp hình | Sẵn sàng sửa |
| 3 | UC-01.3 trigger | Cao | Trigger gồm phản hồi từ V4/V10 xảy ra **sau khi** nhu cầu đã xác nhận, nên không phải điểm mở rộng của UC-01.2 | CN-17; HD-PCCN §3 | Tách hai nguồn: (a) RM trả lại → extend 01.2; (b) phản hồi V4/V10 → PM khởi động UC-01.3 trực tiếp (association PM–01.3 đã có) | | D-06 | Description ghi rõ hai cách bắt đầu | Cần xác nhận |
| 4 | UC-01.3 §3.2 bước 3–4 | Cao | "Xem xét phản hồi", "Điều chỉnh nguồn lực" quá chung | CN-17, CN-10 | Ghi rõ PM xem từng loại phản hồi và sửa loại, quy mô, thời gian, %FTE. Thêm A "giữ nguyên nhu cầu" | | – | Có ít nhất một A | Sẵn sàng sửa |
| 5 | Lớp NhuCauNguonLuc | TB | quyMoFTE, tyLeFTE, loaiNguonLuc đặt ở nhu cầu | II.3 §3 | Chuyển sang ViTriCanBoTri, hoặc ghi chú tham chiếu II.3 | | V2a | Thuộc tính khớp II.3 | Sẵn sàng sửa |
| 6 | §3.2 tiêu đề | Thấp | UC-01.3 đang đánh số "3.1.2", "3.1.3", "3.1.4" | | Đổi thành 3.2.2–3.2.4 | | – | | Sẵn sàng sửa |
| 7 | Trạng thái "Chờ xác nhận", "Đã xác nhận" | TB | Chưa thống nhất với V2a | Q-01 | Dùng bộ trạng thái được chốt | | Q-01 | | Cần xác nhận |
| 8 | UCD cấp vùng | Cao | Mục 0 | | Vẽ UCD UC-01 đủ 01.1–01.3 | | – | Mục 0 | Sẵn sàng sửa |

## 3. V3 — Lê Hoài Linh — UC-02.1

| # | Vị trí | Mức | Vấn đề | Căn cứ | Hành động | Hướng sửa | Phụ thuộc | Nghiệm thu | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Toàn UC | NT | Thiếu luồng tiêu chí tạm chờ PMO duyệt | CN-19; P1 I.3.2 bước 5 | Thêm A: RM đề xuất tiêu chí tạm, PMO duyệt hoặc từ chối; thêm actor phụ PMO | | – | Có CN-19 trong BR, có trên AD | Sẵn sàng sửa |
| 2 | §7 MucDo "số cấp chưa xác định" | Cao | Trái P1 | CN-18 | Ghi số mức theo CN-18 | | – | Không còn "chưa xác định" | Sẵn sàng sửa |
| 3 | §3.4 | Cao | Bảng BR còn trống | | Điền CN-18, 19, QT liên quan đúng mã | | – | Bảng có dữ liệu | Sẵn sàng sửa |
| 4 | §7 nguồn "QT-01..04" | TB | Mã sai | Bảng 05 | Đổi mã | | – | | Sẵn sàng sửa |
| 5 | §7 RM, Yeucauquanlytieuchi, Nhatkythaydoi | TB | Lớp actor, lớp đề xuất không căn cứ | II.3 §3 | Bỏ RM; hai lớp còn lại theo Q-07 | | Q-07 | | Cần xác nhận |
| 6 | §3.3 E1, E3 | Thấp | Kiểm tra quyền, lỗi lưu | HD-MAU | Bỏ | | – | | Sẵn sàng sửa |
| 7 | UCD cấp vùng | Cao | Mục 0 | | Vẽ đủ 02.1–02.3 | | – | | Sẵn sàng sửa |

## 4. V4 — Nguyễn Hoàng Linh — UC-03.3

Đã kiểm tra: Description, AD và bảng BR đều tốt. Bài này dùng làm bài mẫu.

| # | Vị trí | Mức | Vấn đề | Căn cứ | Hành động | Hướng sửa | Phụ thuộc | Nghiệm thu | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|
| 1 | §7–11 | TB | Tên lớp trùng V3, V5 | II.3 §3 | Đổi thành BoTieuChiPhuHop, TieuChiPhuHop, PhienTimKiem, KetQuaDanhGiaPhuHop | | – | Tên khớp II.3 | Sẵn sàng sửa |
| 2 | §7 UngVien, KyNang | TB | Kỹ năng gắn trực tiếp ứng viên | PCN-02 | Tham chiếu NguonLuc và NangLucKyNang của V3 | | Q-04 | | Cần xác nhận |
| 3 | §7 NguoiDung, Shortlist | Thấp | Lớp actor; lớp Shortlist gần như rỗng | II.3 §3 | Bỏ NguoiDung; Shortlist thành thuộc tính vaiTroShortlist | | – | | Sẵn sàng sửa |
| 4 | Hậu điều kiện CN-46 | – | Đã tự đánh dấu điểm mở | CN-46 | Không sửa | | D-16 | | Cần xác nhận |
| 5 | UCD cấp vùng | Cao | Mục 0 | | Vẽ đủ 03.1–03.4 | | – | | Sẵn sàng sửa |

## 5. V5 — Khánh Linh — UC-04.1

| # | Vị trí | Mức | Vấn đề | Căn cứ | Hành động | Hướng sửa | Phụ thuộc | Nghiệm thu | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|
| 1 | §1 và §2.1 | TB | Tên UC khác nhau | HD-PCCN | Dùng "Đánh giá khả năng tham gia" | | – | | Sẵn sàng sửa |
| 2 | §3.4, §7 | TB | Mã BR-V5, CN-V5 | Bảng 05 | Đổi mã | | – | | Sẵn sàng sửa |
| 3 | §3.3 A6 | TB | Ghi "không tự chốt 24 hoặc 48 giờ" | P1 ghi "dưới 24–48 giờ" | Ghi đúng như P1 | | D-17 | | Sẵn sàng sửa |
| 4 | AD | TB | Hành động của RM nằm ở làn Hệ thống; các nhánh kết thúc bằng hộp chữ | UML | Đưa hành động về đúng làn; thêm nút kết thúc | | – | Mỗi nhánh có final node | Sẵn sàng sửa |
| 5 | §7 KetQuaDanhGia, YeuCauXacNhan | TB | Trùng tên lớp V4; lớp đề xuất | II.3 §3 | Đổi thành KetLuanKhaNangThamGia; gộp YeuCauXacNhan vào trạng thái | | – | | Sẵn sàng sửa |
| 6 | §7 YeuCauNguonLuc | – | Chưa rõ có trùng NhuCauNguonLuc | CN-127 | Giữ, chờ quyết định | | Q-03 | | Cần xác nhận |
| 7 | §11 lẫn §12, chữ mẫu còn sót | Thấp | | | Tách mục, xóa chữ mẫu | | – | | Sẵn sàng sửa |
| 8 | UCD cấp vùng | TB | Mục 0 | | Sửa tiêu đề, nối RM | | – | | Sẵn sàng sửa |

## 6. V6 — Nguyễn Thi Thùy Linh — UC-05.1

| # | Vị trí | Mức | Vấn đề | Căn cứ | Hành động | Hướng sửa | Phụ thuộc | Nghiệm thu | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|
| 1 | AD cuối | Cao | Có quyết định "PM phê duyệt?" của UC-05.2 | CN-69 | Kết thúc ở "Gửi phương án cho PM" | | – | AD không còn bước của PM | Sẵn sàng sửa |
| 2 | §7 LichPhanBo, KhaNangThamGia | TB | Trùng V5 | II.3 §3 | Đổi thành PhanBoNguonLuc, KetLuanKhaNangThamGia | | – | | Sẵn sàng sửa |
| 3 | UCD | TB | Association vẽ mũi tên; thiếu 05.2 | UML | Mục 0 | | – | | Sẵn sàng sửa |

## 7. V7 — Lưu Thùy Linh — UC-06.2

Bài này cần sửa nhiều nhất, nhưng không phải làm lại.

| # | Vị trí | Mức | Vấn đề | Căn cứ | Hành động | Hướng sửa | Phụ thuộc | Nghiệm thu | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|
| 1 | §3.3 E1 | NT | Dưới Mức 3 "chuyển PM tự đàm phán" | QT-33 | Ghi "dưới Mức 3: ghi nhận theo dõi, kết thúc" | | – | | Sẵn sàng sửa |
| 2 | §3.3 A3, A4 | NT | Overtime, thuê ngoài, chia 50-50 không có trong P1 | P1 I.1.3.7 | Bỏ A3, A4 | | D-18 | | Cần xác nhận |
| 3 | Bước 1–2, A1 | NT | Gồm nội dung UC-06.1 và 06.3 | HD-PCCN §3 | Bước 1–2 thành tiền điều kiện; A1 thành "chuyển UC-06.3" | Extend 06.3 | – | | Sẵn sàng sửa |
| 4 | Tiền điều kiện | NT | Thiếu đầu vào từ V5 (xung đột lịch); gán V10 làm nguồn kích hoạt | P1 I.1.3.7 | Nguồn: V6, V5; V10 chỉ cung cấp thông tin (CN-75) | | – | | Sẵn sàng sửa |
| 5 | §3.4, §III.1 | Cao | Dùng nhầm mã V2 (CN-01..14) | Bảng 05 | Đổi mã | | – | | Sẵn sàng sửa |
| 6 | §7–12 | TB | ConflictLog, ChangeRequest, KichBanCanDoi, lớp kỹ thuật | II.3 §3 | Đổi tên; bỏ lớp kỹ thuật | | Q-09 | | Sẵn sàng sửa (trừ Q-09) |
| 7 | II.4 | Thấp | Đã làm trước khi chốt II.3 | | Giữ làm nháp | | D-19 | | Cần xác nhận |
| 8 | UCD | TB | Mục 0 | | Bỏ include 06.1 | | – | | Sẵn sàng sửa |

## 8. V8 — Ngọc Linh — UC-07.1 (đã kiểm tra trên 3 sơ đồ mới)

| # | Vị trí | Mức | Vấn đề | Căn cứ | Hành động | Hướng sửa | Phụ thuộc | Nghiệm thu | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|
| 1 | UCD | NT | `include` UC-08, UC-09 | RB-61; P1 I.1.3.1 | Bỏ hai quan hệ và hai UC ngoài vùng | Đây là bàn giao dữ liệu | – | Không còn UC-08, UC-09 trên sơ đồ | Sẵn sàng sửa |
| 2 | UCD | Cao | `include` giữa 07.3 và 07.1 | P1 I.1.3.8: tuần tự | Bỏ include; 07.3 là UC riêng của PMO/CEO | | – | | Sẵn sàng sửa |
| 3 | AD | NT | "Cho phép PMO tự phê duyệt phương án"; "Ra quyết định" nằm trong 07.1 | P1 I.1.3.8; HD-PCCN §3 | Đổi thành "Xác định cấp thẩm quyền: PMO (Mức 1–3)"; "Ra quyết định" thành "Kết luận hồ sơ đủ/chưa đủ cơ sở" | | – | AD không chứa bước phê duyệt | Sẵn sàng sửa |
| 4 | AD nhánh "Gửi yêu cầu giải trình → RM" | Cao | Vòng giải trình của UC-07.2 nằm trong 07.1 | HD-PCCN §3 | Dừng tại "chuyển UC-07.2" | | – | | Sẵn sàng sửa |
| 5 | Sơ đồ lớp | Cao | ThongTinChiPhi, ThongTinDuBao sao chép dữ liệu V9, V10 | RB-61; CN-122 | Tham chiếu DanhGiaChiPhi, KetQuaDuBao | | – | | Sẵn sàng sửa |
| 6 | Sơ đồ lớp | TB | MaTranPhanQuyenDoA; thuộc tính dạng danh sách; HoSo–PA 1:1 | II.3 §3 | Theo Q-08, Q-02 | | Q-02, Q-08 | | Cần xác nhận |
| 7 | UC-07.3 | Cao | UC trọng tâm đề xuất cho V8 chưa có | HD-PCCN §5 | Đặc tả UC-07.3 | | Mục 10 | | Cần xác nhận |
| 8 | UCD | TB | Thiếu 07.4 | | Mục 0 | | – | | Sẵn sàng sửa |

## 9. V9 — Ngô Nhật Long — UC-08.1 (gộp)

| # | Vị trí | Mức | Vấn đề | Căn cứ | Hành động | Hướng sửa | Phụ thuộc | Nghiệm thu | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|
| 1 | §1–2 | Cao | Gộp 08.1–08.3 | P1 I.1.3.9 | Ghi chú "đã gộp" | | D-03 | | Cần xác nhận |
| 2 | Toàn bài | TB | Mã CN-V9, RB-V9 | Bảng 05 | Đổi mã | | – | | Sẵn sàng sửa |
| 3 | §2.2 | TB | Include ngược từ 07.1 | RB-61 | Bỏ | | – | | Sẵn sàng sửa |
| 4 | §2.3, §4, §12 | Cao | Sơ đồ chỉ trên Drive | HD-MAU | Chèn hình vào file | | – | | Sẵn sàng sửa |
| 5 | §7 PhanBoNguonLuc, NguoiDung, NguongPheDuyetNganSach | TB | | II.3 §3 | Đổi thành ChiTietBoTri; bỏ NguoiDung; ngưỡng theo Q-08 | | Q-08 | | Sẵn sàng sửa (trừ Q-08) |
| 6 | Công thức ngân sách | TB | Giả định | QT-51 | Ghi rõ là giả định | | D-20 | | Cần xác nhận |

## 10. V10 — trưởng nhóm

Đã hoàn thành trong `II.2_V10/V10_Phan_II.md` và đã kiểm tra. Còn chờ D-V10-01 đến D-V10-07.

## 11. Rà soát UC trọng tâm

UC trọng tâm đã chốt gồm 01.1, 01.2/01.3, 02.1, 03.3, 04.1, 05.1, 06.2, 07.1, 08.1 (gộp) và 09.1/09.2. Không đề xuất chọn lại. Bảng dưới chỉ ra các khoảng trống thật sự:

| UC | Tình trạng | Bằng chứng | Đề xuất |
|---|---|---|---|
| UC-05.2 | **Nguy cơ bỏ sót** | CN-70, CN-72: điểm rẽ nhánh sang V7 hoặc V8/V9; chưa UC nào mô tả | Bổ sung đặc tả (D-11) |
| UC-07.3 | **Nguy cơ bỏ sót** | CN-99, CN-101: Locked Baseline, trả về V6/V7; HD-PCCN §5 đề xuất cho V8 | V8 đặc tả |
| UC-02.2 | **Chưa đủ căn cứ kết luận** | Tạo hồ sơ năng lực dùng chung; HD-PCCN §5 đề xuất | Trưởng nhóm quyết định (D-05) |
| 04.2, 04.3, 06.1, 06.3, 07.2, 08.4 | Đã thể hiện ở nơi khác | Trong A của 04.1, 06.2, 07.1, 08.1 | Giữ nguyên |
| 01.x, 03.x còn lại | Đã bao quát | | Giữ nguyên |

## 12. Câu hỏi cần trưởng nhóm chốt

Chi tiết: Q-xx trong II.3 §5, D-xx trong `AUDIT_PHAN_II/10_Decision_Log.md`, D-V10-xx trong V10 §14.

- Q-01: trạng thái của nhu cầu.
- Q-02: một phương án có thể có nhiều hồ sơ trình.
- Q-03: YeuCauNguonLuc có là lớp riêng.
- Q-04: ứng viên tuyển ngoài có là NguonLuc.
- Q-08: DoA có vẽ thành lớp.
- D-03: chấp nhận gộp UC-08.1–08.3.
- D-05: UC-02.2.
- D-06: ranh giới UC-01.2 và UC-01.3.
- D-11: ai đặc tả UC-05.2.
- D-18: bỏ A3, A4 của V7.
- D-V10-01, D-V10-02: phân bổ CN và actor của UC-09.
