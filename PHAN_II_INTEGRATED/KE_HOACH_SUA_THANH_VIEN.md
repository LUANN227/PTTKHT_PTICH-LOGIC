# Kế hoạch sửa bài thành viên V2–V10

Tài liệu này là **bảng giao việc hợp nhất duy nhất** của Phần II. Không có file audit riêng cho từng UC.

Mỗi dòng chỉ được ghi sau khi đã đối chiếu trên bài thực tế, theo các căn cứ sau:

- Phần I (P1).
- HD-PCCN, HD-MAU.
- Sơ đồ phân rã chức năng: `I_Phan_ra_chuc_nang/`.
- Bài thành viên:
  - V2b: bản `V2-Phan II 2 1.docx`, trưởng nhóm gửi ngày 20/10.
  - V8: ba sơ đồ mới gửi.
  - V9: AD `4. Activity Diagram.drawio` mới gửi. UCD và sơ đồ lớp V9 vẫn chỉ có trên Drive.

## Quy ước

**Loại việc** (9 loại theo yêu cầu của trưởng nhóm):

| Mã | Loại việc |
|---|---|
| PC | Sửa phân rã chức năng / PCCN |
| UV | UCD cấp vùng |
| TT | Khoảng trống của UC trọng tâm |
| DA | Đồng bộ Description ↔ AD |
| MU | Mã truy vết, ký pháp UML |
| V10 | Hoàn thiện V10 |
| LO | Đồng bộ lớp với II.3 |
| TB | Trình bày |
| CB | Chuẩn bị giai đoạn sau |

**Mức:**

- NT = sai nghiệp vụ hoặc phạm vi.
- Cao = thiếu nội dung bắt buộc, hoặc mâu thuẫn ảnh hưởng II.1/II.3.
- TB = mã, ký pháp.
- Thấp = trình bày.

**Trạng thái:**

- *Sẵn sàng sửa*: làm được ngay.
- *Cần xác nhận*: chờ trưởng nhóm chốt mã D/Q/P ở §4.

**Tài liệu tra cứu:**

- Bảng đổi mã: `AUDIT_PHAN_II/05_Ma_tran_truy_vet.md` §3.
- Tên lớp: `II.3_Domain_Class_Diagram/II3_Danh_muc_va_anh_xa.md` §3.
- UCD mẫu: `II.2_UCD_cap_vung/`.

## 1. Bảng giao việc

Cột "Vị trí D" là vị trí trong UC Description; cột "Vị trí AD / sơ đồ" là vị trí trên Activity Diagram hoặc sơ đồ khác.

### 1.1 Trưởng nhóm / người giữ HD-PCCN

| Mã | Loại | UC | Vấn đề | Vị trí D | Vị trí AD / sơ đồ | Căn cứ | Nội dung cần sửa | Nghiệm thu | Mức | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|---|
| PC-01 | PC | UC-01.x | Cột CN của V2 ghi "CN-xx", "CN liên quan…" | – | HD-PCCN §2 | CN-01..17 | Ghi CN theo P-01 | Không còn "CN-xx" | TB | Cần xác nhận |
| PC-02 | PC | 01.1, 01.2, 05.2, 07.x, 08.x | Actor chính trong Summary khác P1 | – | HD-PCCN §2 | P-02, 03, 06, 10, 11 | Sửa cột Actor theo `Bang_doi_chieu_PCCN.md` §3 | Actor trùng UCD cấp vùng | Cao | Cần xác nhận |
| PC-03 | PC | 03.3/03.4; 07.1/07.2 | Dải CN chồng hoặc sai | – | HD-PCCN §2 | P-04, P-08 | 03.4 = CN-43; 07.2 = CN-95, 96 | Không CN nào thuộc hai UC | TB | Cần xác nhận |
| PC-04 | PC | 04.1 | CN-55, 59, 127 chưa thuộc UC nào | – | HD-PCCN §2 | P-05 | Thêm vào 04.1 | Mọi CN của V5 có UC | TB | Cần xác nhận |
| PC-05 | PC | 06.3 | PM là actor; CN-87, 88 xếp vào 06.3 | – | HD-PCCN §2 | P-07 | Theo P-07 | | TB | Cần xác nhận |
| PC-06 | PC | UC-03 | P1 I.1.2 không có PMO ở V4, nhưng CN-37 và CN-43 có PMO | – | II.1, UCD UC-03 | D-P3-01 | Chọn (a) hoặc (b) | II.1 và P1 thống nhất | Cao | Cần xác nhận |
| PC-07 | PC | 09.2 | Có "dữ liệu lịch sử", "khuyến nghị" | – | HD-PCCN §2 | QT-57, RB-62 (P-12) | Bỏ hai cụm từ | | TB | Cần xác nhận |
| V10-01 | V10 | 09.1, 09.2 | Phân bổ CN và actor | V10 §14 | – | D-V10-01..07 | Chốt bảy điểm | V10 không còn [Chưa xác định] | Cao | Cần xác nhận |
| TB-01 | TB | Tất cả | Chưa có chuẩn đánh số mục và chú thích hình | – | – | Cấu trúc P1 | Chốt quy ước theo `QUY_UOC_PHAN_II.md` §7 | | Thấp | Cần xác nhận |

### 1.2 V2a — Thùy Linh — UC-01.1

| Mã | Loại | UC | Vấn đề | Vị trí D | Vị trí AD / sơ đồ | Căn cứ | Nội dung cần sửa | Nghiệm thu | Mức | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|---|
| DA-01 | DA | 01.1 | Quy tắc FTE tự thêm | §3.3 A2, §3.4 | Decision "FTE ≤ 1.0" | P1 không có; PCN-09 chỉ quy định %FTE 0–100% | Xóa A2 và decision | Không còn "≤ 1.0" ở cả hai nơi | NT | Sẵn sàng sửa |
| DA-02 | DA | 01.1 | Không có bước gửi RM. AD có "Gửi thông báo V2.2", Description không có | §3.2 cuối; hậu điều kiện | Action "Gửi thông báo V2.2" | CN-11 | Thêm bước "PM chuyển nhu cầu hoàn thiện cho RM xem xét" (CN-11) vào D; đổi tên action AD cho trùng | Cùng một bước, cùng tên ở D và AD; hậu điều kiện khớp tiền điều kiện 01.2 | NT | Cần xác nhận (trạng thái, Q-01) |
| DA-03 | DA | 01.1 | Kiểm tra đủ thông tin ở hai vị trí khác nhau | Bước 4 | Decision kiểm tra đặt sau "Lưu" | HD-MAU §4 | Đặt decision ngay sau action tương ứng bước 4 | Thứ tự action AD trùng thứ tự bước D | Cao | Sẵn sàng sửa |
| DA-04 | DA | 01.1 | Thiếu nhánh thông tin dự án chưa đủ | §3.2 | Không có | CN-03; P1 I.1.3.2 | Thêm A1 "ghi nội dung cần bổ sung" ở D và decision ở AD | A1 mang CN-03, có trên AD | Cao | Sẵn sàng sửa |
| DA-05 | DA | 01.1 | Thiếu giai đoạn và %FTE | Bước 6–7 | Không có | CN-07, 08; QT-03 | Thêm bước xác định giai đoạn và mức tham gia cho từng vị trí | Có ở D, AD và BR | Cao | Sẵn sàng sửa |
| DA-06 | DA | 01.1 | Tên trạng thái lệch nhau | "Đã xây dựng" | "Đã xây dựng nội dung" | Q-01 | Dùng một tên theo Q-01 | Trùng nhau | TB | Cần xác nhận |
| DA-07 | DA | 01.1 | AD có thao tác không phải nghiệp vụ | E1 "lỗi CSDL" | "Đăng nhập", "Ghi log", "Nhấn…" | HD-MAU §3.3 | Bỏ E1 ở D; bỏ các action này ở AD | Không còn từ "đăng nhập", "nhấn", "lỗi CSDL" | Thấp | Sẵn sàng sửa |
| MU-01 | MU | 01.1 | Hai action không có luồng ra | – | Hai action cuối nhánh | QUY_UOC 4.1 | Nối về action tương ứng hoặc final node | Mọi node có luồng ra | TB | Sẵn sàng sửa |
| MU-02 | MU | 01.1 | Mã CN-V2-xx, RB-V2-xx | §3.4 | – | Bảng 05 §3 | Đổi theo bảng | Mọi mã có trong P1 | TB | Sẵn sàng sửa |
| MU-03 | MU | 01.1 | Actor "PM/RM" | §2.1 | UCD | P1 I.1.3.2; P-02 | Actor chính PM | UCD có PM | Cao | Sẵn sàng sửa |
| LO-01 | LO | 01.1 | KyNangChuyenMon chứa thuộc tính của yêu cầu; có lớp CongViec | §7–11 | Sơ đồ lớp | II.3 §3 | Đổi thành YeuCauKyNang; bỏ CongViec | Tên lớp trùng II.3 | TB | Cần xác nhận (Q-05) |
| CB-01 | CB | 01.1 → 01.2 | Chuẩn bị sơ đồ Sequence | – | – | §3 dòng H-01 | Đọc tiền đề, chưa vẽ | | – | Sau khi chốt |

### 1.3 V2b — Tuấn Long — UC-01.2, UC-01.3

Đã kiểm tra:

- §7–12 hoàn thành.
- BR của UC-01.2 đúng mã P1.
- AD UC-01.3 khớp Description.

| Mã | Loại | UC | Vấn đề | Vị trí D | Vị trí AD / sơ đồ | Căn cứ | Nội dung cần sửa | Nghiệm thu | Mức | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|---|
| DA-08 | DA | 01.2 | Bước PM điều chỉnh (nội dung của 01.3) nằm trong 01.2 | §3.1.3 E1 | Nhánh "chưa đủ điều kiện" có action của PM | HD-PCCN §3; extend do bài tự vẽ | E1 dừng ở "chuyển lại PM; mở rộng UC-01.3"; đổi mã thành A1 | D và AD 01.2 không còn action của PM | NT | Sẵn sàng sửa |
| DA-09 | DA | 01.2 | Đoạn văn mô tả merge trái với hình | §4.1 | Hình quay về trước "Xem xét" | UML | Sửa đoạn văn theo hình, hoặc ngược lại | Văn bản mô tả đúng hình | TB | Sẵn sàng sửa |
| DA-10 | DA | 01.2 | Action bàn giao nằm ở làn khác với người thực hiện trong D | Bước bàn giao | Action bàn giao V3/V4 | CN-16 (RM) | Đặt ở làn RM | Làn = actor ở D | TB | Sẵn sàng sửa |
| DA-11 | DA | 01.3 | Merge không cần thiết | – | Merge trước final | UML | Bỏ merge, nối thẳng | | Thấp | Sẵn sàng sửa |
| DA-12 | DA | 01.3 | Trigger gồm phản hồi V4/V10, xảy ra sau khi đã xác nhận | Trigger | Initial node | CN-17; HD-PCCN §3 | Ghi hai cách bắt đầu: RM trả lại (extend 01.2); phản hồi V4/V10 (PM khởi động) | D và AD ghi đủ hai cách | Cao | Cần xác nhận (D-06) |
| DA-13 | DA | 01.3 | "Xem xét phản hồi", "Điều chỉnh nguồn lực" quá chung | Bước 3–4 | Action tương ứng | CN-17, CN-10 | Ghi rõ PM sửa loại, quy mô, thời gian, %FTE; thêm A "giữ nguyên nhu cầu" | Có ít nhất một A, có trên AD | Cao | Sẵn sàng sửa |
| MU-04 | MU | 01.2 | Bảng quan hệ ghi "UC-01.3 extend UC-01.3" | §2.2 | UCD | Hình UCD | Sửa thành UC-01.2 | | TB | Sẵn sàng sửa |
| UV-01 | UV | UC-01 | UCD cấp vùng thiếu 01.1 | – | UCD | `UCD_UC-01.drawio` | Vẽ một UCD đủ 01.1–01.3. V2a không vẽ lại | Khớp bảng kiểm UV | Cao | Sẵn sàng sửa |
| LO-02 | LO | 01.x | quyMoFTE, tyLeFTE, loaiNguonLuc đặt ở NhuCauNguonLuc | Lớp | Sơ đồ lớp | II.3 §3 | Chuyển sang ViTriCanBoTri | Thuộc tính khớp II.3 | TB | Sẵn sàng sửa |
| TB-02 | TB | 01.3 | Mục đánh số "3.1.2–3.1.4" | §3.2 | – | | Đổi thành 3.2.2–3.2.4 | | Thấp | Sẵn sàng sửa |
| CB-02 | CB | 01.x | State Machine NhuCauNguonLuc | – | – | §3 dòng H-02 | Chờ Q-01 | | – | Sau khi chốt |

### 1.4 V3 — Lê Hoài Linh — UC-02.1

| Mã | Loại | UC | Vấn đề | Vị trí D | Vị trí AD / sơ đồ | Căn cứ | Nội dung cần sửa | Nghiệm thu | Mức | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|---|
| DA-14 | DA | 02.1 | Thiếu luồng tiêu chí tạm chờ PMO duyệt | Toàn UC | Không có | CN-19; P1 I.3.2 bước 5 | Thêm A ở D và nhánh ở AD; thêm làn PMO | Có CN-19 trong BR và trên AD | NT | Sẵn sàng sửa |
| DA-15 | DA | 02.1 | Bước 8 có "thông báo kết quả cho RM", AD không có | Bước 8 | Action cuối "Cập nhật bộ tiêu chí sẵn sàng sử dụng" | HD-MAU §4 | Thêm vào AD, hoặc bỏ khỏi D (thông báo không phải nghiệp vụ, xem §9 của bài) | D và AD trùng | Thấp | Sẵn sàng sửa |
| DA-16 | DA | 02.1 | Nhánh A1 "Ngừng áp dụng thay vì xóa" không có luồng ra | A1 | Hộp nét đứt A1 | QUY_UOC 4.1 | Nối A1 về "Lưu thay đổi" hoặc final node | Mọi node có luồng ra | TB | Sẵn sàng sửa |
| DA-17 | DA | 02.1 | Kiểm tra quyền, lỗi lưu | E1, E3 | "Có quyền?", "Lưu thành công?" | HD-MAU §3.3 | Bỏ ở cả D và AD | | Thấp | Sẵn sàng sửa |
| MU-05 | MU | 02.1 | Số mức "chưa xác định"; bảng BR trống; mã "QT-01..04" sai | §7, §3.4 | – | CN-18; Bảng 05 | Ghi 5 mức theo CN-18; điền BR; đổi mã | Không còn ô trống | Cao | Sẵn sàng sửa |
| UV-02 | UV | UC-02 | Chỉ có 02.1 | – | UCD | `UCD_UC-02.drawio` | Vẽ đủ 02.1–02.3; thêm PMO, Nguồn lực | Khớp bảng kiểm UV | Cao | Sẵn sàng sửa |
| LO-03 | LO | 02.1 | Lớp RM (actor); Yeucauquanlytieuchi, Nhatkythaydoi chưa có căn cứ | §7 | Sơ đồ lớp | II.3 §3 | Bỏ RM; hai lớp còn lại theo Q-07 | | TB | Cần xác nhận |
| CB-03 | CB | 02.1 | State Machine tiêu chí tạm | – | – | §3 dòng H-03 | Sau DA-14 | | – | Sau khi chốt |

### 1.5 V4 — Nguyễn Hoàng Linh — UC-03.3 (bài mẫu)

Đã kiểm tra: Description, AD và BR khớp nhau.

Hai điểm nhỏ ở AD (Thấp, không bắt buộc sửa):

- Chưa có merge trước một decision.
- Tiêu đề AD không phải tên UC.

| Mã | Loại | UC | Vấn đề | Vị trí D | Vị trí AD / sơ đồ | Căn cứ | Nội dung cần sửa | Nghiệm thu | Mức | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|---|
| DA-18 | DA | 03.3 | Tiêu đề AD khác tên UC | – | Tiêu đề | HD-PCCN §1 | Đặt "UC-03.3 Đánh giá, xếp hạng và lập shortlist ứng viên" | | Thấp | Sẵn sàng sửa |
| UV-03 | UV | UC-03 | Chỉ có 03.3 | – | UCD | `UCD_UC-03.drawio`; D-P3-01 | Vẽ đủ 03.1–03.4; PMO nối 03.3, 03.4 | Khớp bảng kiểm UV | Cao | Sẵn sàng sửa |
| LO-04 | LO | 03.3 | Tên lớp trùng V3, V5 | §7–11 | Sơ đồ lớp | II.3 §3 | Đổi thành BoTieuChiPhuHop, TieuChiPhuHop, PhienTimKiem, KetQuaDanhGiaPhuHop | Tên khớp II.3 | TB | Sẵn sàng sửa |
| LO-05 | LO | 03.3 | Kỹ năng gắn trực tiếp ứng viên; lớp NguoiDung, Shortlist | §7 | Sơ đồ lớp | PCN-02; II.3 | Tham chiếu NangLucKyNang; bỏ NguoiDung; Shortlist thành thuộc tính | | TB | Cần xác nhận (Q-04) |
| MU-06 | MU | 03.3 | CN-46 đang để mở | Hậu điều kiện | – | D-16 | Không sửa đến khi chốt | | – | Cần xác nhận |
| CB-04 | CB | 03.3 | Sequence 03.3; State Machine DeNghiMienTru | – | – | §3 dòng H-04, H-05 | | | – | Sau khi chốt |

### 1.6 V5 — Khánh Linh — UC-04.1

| Mã | Loại | UC | Vấn đề | Vị trí D | Vị trí AD / sơ đồ | Căn cứ | Nội dung cần sửa | Nghiệm thu | Mức | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|---|
| DA-19 | DA | 04.1 | AD rẽ nhánh trước "RM ghi nhận kết luận", nên các trường hợp một phần và ngoại lệ không ghi kết luận | Bước 7 | Decision trước action ghi kết luận | CN-51 | Mọi nhánh merge vào "Ghi nhận kết luận" rồi mới rẽ sang 04.2/04.3 | Mọi nhánh đi qua action CN-51 | Cao | Sẵn sàng sửa |
| DA-20 | DA | 04.1 | AD thiếu nhánh A2 "không chờ" | A2 | Không có | CN-52 | Thêm nhánh | Mọi A có trên AD | Cao | Sẵn sàng sửa |
| DA-21 | DA | 04.1 | D đánh giá từng ứng viên, AD không lặp | Bước 3–7 | Không có vòng lặp | CN-48–51 | Thêm vòng "còn ứng viên?" | | TB | Sẵn sàng sửa |
| DA-22 | DA | 04.1 | Số bước lệch giữa D và ghi chú AD | Bước 6 / 7 | Ghi chú | | Thống nhất số bước | | Thấp | Sẵn sàng sửa |
| DA-23 | DA | 04.1 | Action của RM nằm ở làn Hệ thống; nhánh kết thúc bằng hộp chữ | – | Làn Hệ thống; cuối nhánh | QUY_UOC 4.1, 4.4 | Đưa action về làn RM; thêm final node | | TB | Sẵn sàng sửa |
| DA-24 | DA | 04.1 | "không tự chốt 24 hoặc 48 giờ" | A6 | – | P1 "dưới 24–48 giờ" | Ghi đúng như P1 | | TB | Sẵn sàng sửa (D-17) |
| MU-07 | MU | 04.1 | Mã BR-V5, CN-V5; tên UC khác nhau giữa §1 và §2.1 | §1, §2.1, §3.4, §7 | – | Bảng 05; HD-PCCN | Đổi mã; dùng "Đánh giá khả năng tham gia" | | TB | Sẵn sàng sửa |
| UV-04 | UV | UC-04 | Tiêu đề "PHÂN HỆ V5"; RM chỉ nối 04.1 | – | UCD | `UCD_UC-04.drawio` | Đổi tiêu đề; nối RM–04.2, 04.3 | Khớp bảng kiểm UV | TB | Sẵn sàng sửa |
| LO-06 | LO | 04.1 | KetQuaDanhGia trùng V4; YeuCauXacNhan; YeuCauNguonLuc | §7 | Sơ đồ lớp | II.3 §3 | Đổi thành KetLuanKhaNangThamGia; YeuCauXacNhan thành trạng thái; YeuCauNguonLuc theo Q-03 | | TB | Cần xác nhận (Q-03) |
| TB-03 | TB | 04.1 | §11 lẫn §12; còn chữ mẫu | §11–12 | – | HD-MAU | Tách mục, xóa chữ mẫu | | Thấp | Sẵn sàng sửa |
| CB-05 | CB | 04.1 | Sequence 04.1; State Machine HoSoVuotTaiNgoaiLe | – | – | §3 dòng H-06, H-07 | | | – | Sau khi chốt |

### 1.7 V6 — Nguyễn Thi Thùy Linh — UC-05.1

| Mã | Loại | UC | Vấn đề | Vị trí D | Vị trí AD / sơ đồ | Căn cứ | Nội dung cần sửa | Nghiệm thu | Mức | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|---|
| DA-25 | DA | 05.1 | AD có quyết định "PM phê duyệt?" của UC-05.2 | – | Phần cuối AD | CN-69; HD-PCCN §3 | Kết thúc ở "Gửi phương án cho PM" (CN-68) | AD không còn action của PM | Cao | Sẵn sàng sửa |
| DA-26 | DA | 05.1 | A4 trong D quay lại bước 5, AD kết thúc | A4 | Nhánh A4 | HD-MAU §4 | Nối nhánh AD về action bước 5 | | TB | Sẵn sàng sửa |
| DA-27 | DA | 05.1 | E1 quá hạn 3 ngày có trong D, không có trong AD; CN-73 thuộc 05.2 theo PCCN | E1 | Không có | CN-73; HD-PCCN §2 | Nếu giữ 05.1 thì thêm vào AD; nếu theo PCCN thì chuyển sang 05.2 | D và AD trùng | TB | Cần xác nhận (D-11) |
| DA-28 | DA | 05.1 | Bước 10 không có trên AD | Bước 10 | Không có | | Thêm action | | TB | Sẵn sàng sửa |
| UV-05 | UV | UC-05 | Chỉ có 05.1; association vẽ mũi tên | – | UCD | `UCD_UC-05.drawio` | Thêm 05.2; bỏ mũi tên | Khớp bảng kiểm UV | TB | Sẵn sàng sửa |
| LO-07 | LO | 05.1 | LichPhanBo, KhaNangThamGia trùng V5 | §7 | Sơ đồ lớp | II.3 §3 | Đổi thành PhanBoNguonLuc, KetLuanKhaNangThamGia | | TB | Sẵn sàng sửa |
| CB-06 | CB | 05.x | State Machine PhuongAnBoTri; Communication 05.1 | – | – | §3 dòng H-08, H-09 | | | – | Sau khi chốt |

### 1.8 V7 — Lưu Thùy Linh — UC-06.2

| Mã | Loại | UC | Vấn đề | Vị trí D | Vị trí AD / sơ đồ | Căn cứ | Nội dung cần sửa | Nghiệm thu | Mức | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|---|
| DA-29 | DA | 06.2 | Dưới Mức 3 ghi "<20%", "chuyển PM tự đàm phán" | E1 | Nhánh E1 | QT-33 | Ghi "dưới Mức 3: ghi nhận theo dõi, kết thúc" ở cả hai | Không còn "<20%" | NT | Sẵn sàng sửa |
| DA-30 | DA | 06.2 | Overtime, thuê ngoài, chia 50-50 không có trong P1; AD không có hai nhánh này | A3, A4 | Không có | P1 I.1.3.7 | Bỏ A3, A4 khỏi D (AD đã không có) | D và AD trùng | NT | Cần xác nhận (D-18) |
| DA-31 | DA | 06.2 | Bước 1–2 và A1 chứa nội dung 06.1, 06.3 | Bước 1–2, A1 | Action đầu, nhánh A1 | HD-PCCN §3 | Bước 1–2 thành tiền điều kiện; A1 thành "chuyển UC-06.3" | | NT | Sẵn sàng sửa |
| DA-32 | DA | 06.2 | Nhánh làm mịn/san bằng và bế tắc nối nhầm sang action đề xuất thay đổi | – | Các nhánh Leveling, Deadlock | CN-80–82, 86 | Nối mỗi nhánh tới đúng action của nó | Mỗi guard dẫn tới action có cùng CN | Cao | Sẵn sàng sửa |
| DA-33 | DA | 06.2 | Bước 3 actor RM; AD đặt ở làn PM | Bước 3 | Làn PM | CN-79 (RM điều phối) | Đặt action ở làn RM | | TB | Sẵn sàng sửa |
| DA-34 | DA | 06.2 | Decision về thời hạn đàm phán khó hiểu | – | Decision thời hạn | CN-79 | Ghi guard đúng như CN-79, không thêm số ngày | | TB | Sẵn sàng sửa |
| MU-08 | MU | 06.2 | Tiền điều kiện thiếu nguồn V5; gán V10 là nguồn kích hoạt | Tiền điều kiện | – | P1 I.1.3.7; CN-75 | Nguồn V6, V5; V10 chỉ cung cấp thông tin | | NT | Sẵn sàng sửa |
| MU-09 | MU | 06.2 | Dùng nhầm mã V2 (CN-01..14) | §3.4, §III.1 | – | Bảng 05 | Đổi mã | | Cao | Sẵn sàng sửa |
| UV-06 | UV | UC-06 | `include` 06.1 | – | UCD | `UCD_UC-06.drawio` | Bỏ include; extend 06.3 → 06.2 | Khớp bảng kiểm UV | TB | Sẵn sàng sửa |
| LO-08 | LO | 06.2 | ConflictLog, ChangeRequest, KichBanCanDoi, lớp kỹ thuật | §7–12 | Sơ đồ lớp | II.3 §3 | Đổi tên theo II.3; bỏ lớp kỹ thuật | | TB | Sẵn sàng sửa (trừ Q-09) |
| CB-07 | CB | 06.x | II.4 làm trước khi chốt II.3; State Machine DiemXungDot; Sequence 06.2 | II.4 | – | D-19; §3 dòng H-10, H-11 | Giữ II.4 làm nháp | | – | Cần xác nhận |

### 1.9 V8 — Ngọc Linh — UC-07.1 (đã kiểm tra trên ba sơ đồ mới)

| Mã | Loại | UC | Vấn đề | Vị trí D | Vị trí AD / sơ đồ | Căn cứ | Nội dung cần sửa | Nghiệm thu | Mức | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|---|
| DA-35 | DA | 07.1 | AD có bước phê duyệt của 07.3 | Bước 5–6 | "Cho phép PMO tự phê duyệt phương án", "Ra quyết định" | P1 I.1.3.8; HD-PCCN §3 | Đổi thành "Xác định cấp thẩm quyền theo DoA" và "Kết luận hồ sơ đủ / chưa đủ cơ sở" (decision "Hồ sơ đủ cơ sở" đã khớp bước 5) | D và AD không chứa quyết định phê duyệt | NT | Sẵn sàng sửa |
| DA-36 | DA | 07.1 | Vòng giải trình (07.2) nằm trong 07.1 | A2 có bước RM giải trình | Vòng "Gửi yêu cầu giải trình → RM" | HD-PCCN §3; CN-95, 96 | A2 và AD dừng ở "chuyển UC-07.2" (extend) | Không còn action của RM | Cao | Sẵn sàng sửa |
| DA-37 | DA | 07.1 | Bước 4 ghi "<<include>> V9/V10" | Bước 4 | Action xem chi phí, dự báo | CN-93, 94; RB-61 | Ghi "xem thông tin chi phí (V9) và dự báo (V10)" | Không còn "include" trong D | Cao | Sẵn sàng sửa |
| DA-38 | DA | 07.1 | A1 chuyển cấp CEO: kiểm tra trên AD | A1 | Nhánh Mức 4–5 | CN-91 | Giữ; đặt guard "Mức 4–5" | | Thấp | Sẵn sàng sửa |
| UV-07 | UV | UC-07 | include UC-08, UC-09; include 07.3 – 07.1; thiếu 07.4 | – | UCD mới | RB-61; `UCD_UC-07.drawio` | Bỏ UC ngoài vùng và include; thêm 07.4; extend 07.2 → 07.1 | Khớp bảng kiểm UV | NT | Sẵn sàng sửa |
| LO-09 | LO | 07.1 | ThongTinChiPhi, ThongTinDuBao sao chép V9, V10 | – | Sơ đồ lớp mới | RB-61; CN-122 | Tham chiếu DanhGiaChiPhi, KetQuaDuBao | | Cao | Sẵn sàng sửa |
| LO-10 | LO | 07.1 | MaTranPhanQuyenDoA; thuộc tính dạng danh sách; HoSo–PA 1:1; có phương thức | – | Sơ đồ lớp mới | II.3 §3; QUY_UOC 5.8, 5.9 | Theo Q-08, Q-02; bỏ thuộc tính danh sách | | TB | Cần xác nhận |
| CB-08 | CB | 07.x | State Machine HoSoTrinhDuyet; Sequence 07.1 → 07.3 | – | – | §3 dòng H-12, H-13 | | | – | Sau khi chốt |

### 1.10 V9 — Ngô Nhật Long — UC-08.1 (gộp 08.1–08.3)

AD `4. Activity Diagram.drawio` đã đọc và render. Description khớp AD về thứ tự bước, A1–A3, E1 và E2.

| Mã | Loại | UC | Vấn đề | Vị trí D | Vị trí AD / sơ đồ | Căn cứ | Nội dung cần sửa | Nghiệm thu | Mức | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|---|
| DA-39 | DA | 08.1 | Đối chiếu ngân sách giao cho System | Bước 6 | Action "Đối chiếu ngân sách" ở làn Hệ thống | CN-108: "Tài chính và PM đối chiếu" | Ghi Tài chính/PM thực hiện, hệ thống hỗ trợ; chuyển action sang làn Tài chính | Làn = actor ở D = CN | TB | Sẵn sàng sửa |
| DA-40 | DA | 08.1 / 08.4 | Bước 7 "ghi nhận hướng xử lý" và nhánh gắn cấp ≤10% / >10% là nội dung của 08.4. Quyết định của PMO/CEO (CN-128, 129) không có ở đâu | Bước 7, A2 | "Gắn cấp…", "Ghi nhận hướng xử lý" | HD-PCCN §1; D-03 | Nếu D-03 gộp cả 08.4: ghi tên UC và phạm vi đúng, thêm làn PMO/CEO. Nếu không: dừng ở "chuyển UC-08.4" | Phạm vi D/AD trùng quyết định D-03 | Cao | Cần xác nhận (D-03) |
| DA-41 | DA | 08.1 | E1 "yêu cầu Tài chính bổ sung" không có trên AD; bước 8 ghi tài khoản thực hiện không có trên AD | E1, bước 8 | Nhánh E1, action cuối | HD-MAU §4 | Thêm hoặc bỏ cho trùng; ghi tài khoản là phi chức năng, nên bỏ khỏi luồng | | Thấp | Sẵn sàng sửa |
| DA-42 | DA | 08.1 | E2 gồm "không có quyền" | E2 | Guard "không có quyền" | HD-MAU §3.3 | Bỏ phần quyền | | Thấp | Sẵn sàng sửa |
| DA-43 | DA | 08.1 | Tiêu đề AD "UC-08.1 Đánh giá tác động chi phí và ngân sách…" khác tên UC-08.1 | – | Tiêu đề AD | HD-PCCN §1 | Theo D-03 | | Thấp | Cần xác nhận |
| MU-10 | MU | 08.1 | Mã CN-V9, RB-V9, PCN-V9; công thức tỷ lệ vượt | Toàn bài; A2 | – | Bảng 05; QT-51 | Đổi mã; ghi công thức là giả định | | TB | Sẵn sàng sửa (D-20) |
| MU-11 | MU | 08.1 | Include ngược từ 07.1 | §2.2 | UCD (Drive) | RB-61 | Bỏ | | TB | Sẵn sàng sửa |
| UV-08 | UV | UC-08 | UCD chỉ có trên Drive | §2.3 | – | `UCD_UC-08.drawio` | Chèn hình vào bài; đối chiếu mẫu | Khớp bảng kiểm UV | Cao | Sẵn sàng sửa |
| LO-11 | LO | 08.1 | PhanBoNguonLuc, NguoiDung, NguongPheDuyetNganSach | §7 | Sơ đồ lớp (Drive) | II.3 §3 | Đổi thành ChiTietBoTri; bỏ NguoiDung; ngưỡng theo Q-08 | | TB | Sẵn sàng sửa (trừ Q-08) |
| TB-04 | TB | 08.1 | Hình chỉ có link Drive | §2.3, §4, §12 | – | HD-MAU | Chèn hình (PNG xuất từ `.drawio`) | Hình nằm trong file nộp | Cao | Sẵn sàng sửa |
| CB-09 | CB | 08.1 | Communication 08.1 | – | – | §3 dòng H-14 | | | – | Sau khi chốt |

### 1.11 Việc chung về trình bày

V8 dùng làm mẫu về cách xuất hình. Phần I dùng làm mẫu về cấu trúc.

| Mã | Loại | Phạm vi | Vấn đề | Nội dung cần sửa | Nghiệm thu | Mức | Trạng thái |
|---|---|---|---|---|---|---|---|
| TB-05 | TB | V2–V9 | Ảnh chụp màn hình mờ, nền màu, cỡ chữ không đều | Xuất PNG từ draw.io với nền trắng, tỷ lệ 150–200%, giống ba hình mới của V8 | Chữ đọc được khi chèn bằng chiều rộng trang | Thấp | Sẵn sàng sửa |
| TB-06 | TB | V2–V10 | Đánh số mục và chú thích hình chưa thống nhất | Theo `QUY_UOC_PHAN_II.md` §7 | | Thấp | Cần xác nhận (TB-01) |
| TB-07 | TB | II.3 | Sơ đồ tổng quát quá dày khi in | Dùng hình tổng quan tên lớp và ba khung nhìn A, B, C; hình đầy đủ để ở phụ lục | | Thấp | Sẵn sàng sửa |
| CB-10 | CB | V10 | Sequence 09.1 | §3 dòng H-15 | | – | Sau khi chốt |

## 2. Rà soát UC trọng tâm

UC trọng tâm đã chốt:

- 01.1;
- 01.2/01.3;
- 02.1;
- 03.3;
- 04.1;
- 05.1;
- 06.2;
- 07.1;
- 08.1 (gộp);
- 09.1/09.2.

**Không đề xuất chọn lại.** Bảng dưới phân loại cả 28 UC theo mức bao quát của bộ UC trọng tâm.

| UC | Phân loại | Bằng chứng | Việc |
|---|---|---|---|
| 01.1, 01.2, 01.3 | Đã bao quát | UC trọng tâm của V2a, V2b | – |
| 02.1 | Đã bao quát | UC trọng tâm V3 | – |
| 02.2 | **Chưa đủ căn cứ kết luận** | Tạo hồ sơ năng lực dùng chung cho V4–V6, V10 (CN-20–27). HD-PCCN §5 đề xuất làm trọng tâm, nhưng V3 chọn 02.1 | TT-04 (D-05) |
| 02.3 | Thể hiện ở nơi khác | II.3 (HoSoNangLuc); UCD UC-02 | – |
| 03.1, 03.2 | Thể hiện ở nơi khác | Tiền điều kiện của 03.3 | – |
| 03.3 | Đã bao quát | UC trọng tâm V4 | – |
| 03.4 | Thể hiện ở nơi khác | A của 03.3 (CN-43) | – |
| 04.1 | Đã bao quát | UC trọng tâm V5 | – |
| 04.2, 04.3 | Thể hiện ở nơi khác | A của 04.1, sau khi sửa DA-19 | – |
| 05.1 | Đã bao quát | UC trọng tâm V6 | – |
| 05.2 | **Nguy cơ bỏ sót** | CN-70, CN-72: điểm rẽ sang V7 hoặc V8/V9. Chưa UC nào mô tả | TT-01 (D-11) |
| 06.1, 06.3 | Thể hiện ở nơi khác | Tiền điều kiện và extend của 06.2 | – |
| 06.2 | Đã bao quát | UC trọng tâm V7 | – |
| 07.1 | Đã bao quát | UC trọng tâm V8 | – |
| 07.2 | Thể hiện ở nơi khác | Extend của 07.1 | – |
| 07.3, 07.4 | **Nguy cơ bỏ sót** | CN-97–101: quyết định 4 hướng, điều kiện hoàn trả, Locked Baseline, trả về V6/V7. HD-PCCN §5 đề xuất 07.3 cho V8 | TT-02 |
| 08.1–08.3 | Đã bao quát | UC gộp của V9 (D-03) | – |
| 08.4 | **Nguy cơ bỏ sót (một phần)** | Hướng xử lý đã có ở bước 7 của V9; quyết định của PMO/CEO (CN-128, 129) chưa có ở đâu | TT-03 (D-03) |
| 09.1, 09.2 | Đã bao quát | V10 | – |

| Mã | Loại | UC | Nội dung cần làm | Đề xuất người làm | Trạng thái |
|---|---|---|---|---|---|
| TT-01 | TT | 05.2 | Đặc tả Description + AD | V6 | Cần xác nhận (D-11) |
| TT-02 | TT | 07.3 (và 07.4) | Đặc tả Description + AD | V8 | Cần xác nhận |
| TT-03 | TT | 08.4 | Bổ sung bước quyết định của PMO/CEO (CN-128, 129) | V9 | Cần xác nhận (D-03) |
| TT-04 | TT | 02.2 | Quyết định có đặc tả hay không | Trưởng nhóm | Cần xác nhận (D-05) |

## 3. Kế hoạch sơ đồ hành vi (chưa vẽ)

Chỉ bắt đầu vẽ sau khi:

- Description và AD của UC liên quan đã sửa xong;
- các mã ở cột "Tiền đề" đã được chốt.

Trạng thái chỉ dùng các trạng thái có trong P1. Không thêm trạng thái mới.

Cột **Đề xuất phân công** là đề xuất. Trưởng nhóm quyết định.

| Mã | Vùng | UC | Loại sơ đồ | Đối tượng / luồng | Căn cứ | Lý do | Tiền đề | Thành viên phù hợp | Đề xuất phân công |
|---|---|---|---|---|---|---|---|---|---|
| H-01 | V2 | 01.1 → 01.2 | Sequence | PM lập nhu cầu, chuyển RM; RM xác nhận hoặc trả lại | CN-02–11, 12–14 | Có trao đổi qua lại giữa hai actor | DA-02, Q-01 | V2a, V2b | V2a |
| H-02 | V2 | 01.1–01.3 | State Machine | NhuCauNguonLuc: đang xây dựng, chờ xem xét, đã xác nhận, trả lại điều chỉnh | CN-03, 11, 13, 14, 10 | Một đối tượng đi qua cả ba UC | Q-01 (tên trạng thái) | V2b | V2b |
| H-03 | V3 | 02.1 | State Machine | Tiêu chí tạm: chờ PMO duyệt, được duyệt, bị từ chối; ngừng áp dụng | CN-19; CN-18 | Có trạng thái chờ phê duyệt rõ trong P1 | DA-14 | V3 | V3 |
| H-04 | V4 | 03.3 | Sequence | RM đối chiếu điều kiện, đề nghị miễn trừ, PMO duyệt, tính điểm, xếp hạng, shortlist | CN-34–41 | Nhiều đối tượng: KetQuaDanhGiaPhuHop, DeNghiMienTru, HoSoNangLuc | D-P3-01 | V4 | V4 |
| H-05 | V4 | 03.3 | State Machine | DeNghiMienTru: chờ PMO duyệt, chấp thuận, từ chối | CN-37 | Nhỏ; tùy chọn nếu V4 còn thời gian | D-P3-01 | V4 | V4 (tùy chọn) |
| H-06 | V5 | 04.1 | Sequence | RM tra cứu lịch, tính năng lực khả dụng, so ngưỡng, ghi kết luận, bàn giao V6 | CN-47–52, 59 | Nhiều truy vấn dữ liệu | DA-19, PC-04 | V5 | V5 |
| H-07 | V5 | 04.3 | State Machine | HoSoVuotTaiNgoaiLe: chờ duyệt theo mức (PMO Mức 2–3, CEO Mức 4–5), chấp thuận, từ chối | CN-56, 57; RB-59 | Có thẩm quyền theo mức | – | V5 | V5 |
| H-08 | V6–V8 | 05.1–07.4 | State Machine | PhuongAnBoTri: đang xây dựng, chờ PM xác nhận, yêu cầu điều chỉnh, chờ phê duyệt, yêu cầu chỉnh sửa, từ chối, Locked Baseline | CN-69, 72, 73, 97, 99, 101; QT-31 | Đối tượng trung tâm, đi qua ba vùng | Q-02, D-11, TT-02 | V6, V8 | V6 (V8 rà phần V8) |
| H-09 | V6 | 05.1 | Communication | RM, PhuongAnBoTri, ChiTietBoTri, HoSoNangLuc, LichNguonLuc, KetLuanKhaNangThamGia | CN-60–68 | Nhiều lớp phối hợp, ít thứ tự thời gian | DA-25 | V6 | V6 |
| H-10 | V7 | 06.1–06.3 | State Machine | DiemXungDot: phát hiện, đang đàm phán, đã thống nhất, chuyển cấp, đã phân xử | CN-74, 79, 83–85; QT-33 | V7 đã có bản nháp | D-18, D-19 | V7 | V7 |
| H-11 | V7 | 06.2 | Sequence | RM điều phối PM các dự án; làm mịn, san bằng; đề xuất thay đổi | CN-78–82, 86 | Nhiều bên, có thời hạn | DA-31, DA-32 | V7 | V7 |
| H-12 | V8 | 07.1–07.2 | State Machine | HoSoTrinhDuyet: đã tiếp nhận, chờ giải trình, đã cập nhật, chờ quyết định | CN-89–96 | Vòng giải trình lặp | Q-02 | V8 | V8 |
| H-13 | V8 | 07.1 → 07.3 | Sequence | PMO nhận hồ sơ, đối chiếu DoA, xem V9/V10, giải trình, quyết định | CN-89–97 | Thể hiện rõ ranh giới 07.1/07.2/07.3 | DA-35, DA-36, TT-02 | V8 | V8 |
| H-14 | V9 | 08.1 (gộp) | Communication | PM, Tài chính, DanhGiaChiPhi, DonGia, DuToanChiPhi, NganSach, SoSanhPhuongAn | CN-103–110 | Nhiều lớp cùng tham gia tính toán | D-03 | V9 | V9 |
| H-15 | V10 | 09.1 | Sequence | Tổng hợp nguồn cung (V3, V5, V8) và nhu cầu (PM) song song; đối chiếu; chuyển kết quả | CN-113–115, 120–122 | Có fork song song trong P1 | D-V10-01 | Trưởng nhóm | Trưởng nhóm |

## 4. Câu hỏi cần trưởng nhóm chốt

Chi tiết các mã:

- Q-xx: II.3 §5.
- D-xx: `AUDIT_PHAN_II/10_Decision_Log.md`.
- D-V10-xx: V10 §14.
- P-xx, D-P3-01: `I_Phan_ra_chuc_nang/Bang_doi_chieu_PCCN.md`.

| Mã | Câu hỏi | Ảnh hưởng |
|---|---|---|
| D-P3-01 | PMO có tham gia V4 không (I.1.2 khác CN-37, 43) | II.1, UCD UC-03, PC-06 |
| P-01..P-12 | Sửa bảng Summary của HD-PCCN | PC-01..07 |
| Q-01 | Tên trạng thái của nhu cầu | DA-02, DA-06, H-02 |
| Q-02 | Một phương án có nhiều hồ sơ trình | LO-10, H-08, H-12 |
| Q-03 | YeuCauNguonLuc có là lớp riêng | LO-06 |
| Q-04 | Ứng viên tuyển ngoài có là NguonLuc | LO-05 |
| Q-08 | DoA có vẽ thành lớp | LO-10, LO-11 |
| D-03 | Gộp UC-08.1–08.3; 08.4 có gộp không | DA-40, DA-43, TT-03 |
| D-05 | UC-02.2 | TT-04 |
| D-06 | Ranh giới UC-01.2 và UC-01.3 | DA-12, UV-01 |
| D-11 | Ai đặc tả UC-05.2; CN-73 thuộc UC nào | TT-01, DA-27 |
| D-18 | Bỏ A3, A4 của V7 | DA-30 |
| TB-01 | Quy ước đánh số mục và chú thích hình | TB-06 |
| D-V10-01..07 | Phân bổ CN, actor và các điểm mở của V10 | V10-01 |
