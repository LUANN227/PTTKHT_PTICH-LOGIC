# Yêu cầu sửa II.2 theo vùng và thành viên

Bản rà soát ngày 22/10/2026. Mỗi bảng dành cho một thành viên hoặc một vùng. Chỉ ghi những chỗ **còn sai hoặc còn thiếu**; chỗ đã đúng không ghi lại.

## Cách đọc

Cột "Cách sửa" mở đầu bằng một trong ba nhãn:

- **[Lỗi]**: đã đối chiếu với nguồn và xác nhận là sai. Sửa ngay.
- **[Chờ QĐ-xx]**: cần trưởng nhóm quyết định trước. Mã QĐ tra trong `DANH_SACH_CHO_QUYET_DINH.md`. Chưa sửa phần phụ thuộc vào quyết định.
- **[Cần xác nhận]**: chưa đủ bằng chứng để kết luận. Thành viên kiểm tra lại và báo kết quả.

Căn cứ chung cho mọi bảng:

- Phần I: `[PTTKHT] I - PHÂN TÍCH YÊU CẦU FINAL.docx`, viết tắt là P1. Mã CN, QT, PCN lấy từ đây.
- Mã và tên UC theo HD-PCCN §1, không đổi.
- UCD cấp vùng chuẩn nằm ở `drawio/II.2_UCD_vung/UCD_UC-0x.drawio`.
- Tên lớp theo II.3 của bản Word này (Hình II.3-1 đến II.3-6).

**Nộp lại.** Mỗi thành viên nộp:

- bản Word phần của mình đã sửa;
- file `.drawio` của mọi sơ đồ mình vẽ (UCD, AD, sơ đồ lớp nếu có, sơ đồ II.4).

Ảnh PNG phải được xuất từ chính file `.drawio` đó. Ảnh không có file nguồn không được tính.

**Trước khi chèn vào bản chung.** Trưởng nhóm kiểm theo cột "Tiêu chí chấm đạt". Dòng nào chưa đạt thì chưa chèn vào bản Word chung.

---

## V2a — Nguyễn Thị Thùy Linh — UC-01.1 (trọng tâm)

| Chỗ cần sửa | Cách sửa | Nguồn đối chiếu | Tiêu chí chấm đạt |
|---|---|---|---|
| §2.1 bảng xác định UC: actor chính "PM / RM", actor phụ "System" | [Lỗi] Actor chính chỉ là PM. Bỏ System khỏi danh sách actor, vì hệ thống không phải actor. Không vẽ RM nối với 01.1 | CN-01–11 (tất cả do PM); P1 I.1.2 | D và UCD không còn RM, System là actor của 01.1 |
| §3.3 A2 và RB-V2-03 "FTE không vượt quỹ thời gian chuẩn"; decision "Chỉ số FTE ≤ 1.0/nhân sự" trên AD | [Lỗi] Xóa A2, RB-V2-03 và decision này. P1 không có giới hạn tổng nhu cầu ≤ 1 FTE. Quy mô nhu cầu tính theo FTE từng giai đoạn (CN-06). %FTE là mức tham gia của một vị trí, từ 0 đến 100% (CN-08, PCN-09) | CN-06, CN-08; PCN-09 | Nhu cầu "2 người toàn thời gian" không bị chặn. D, AD và bảng quy tắc không còn "≤ 1.0" |
| Cuối luồng chính và hậu điều kiện: không có bước gửi RM. AD có action "Gửi thông báo V2.2" nhưng D không có | [Lỗi] Thêm bước cuối "PM chuyển nhu cầu đã hoàn thiện cho RM xem xét" (CN-11), cả ở D lẫn AD, cùng một tên. Phân biệt "lưu nháp" với "đã gửi RM" | CN-11, CN-12 | D và AD có cùng bước gửi RM. Hậu điều kiện của 01.1 khớp tiền điều kiện của 01.2 |
| A1 (bước 4): hiện chỉ xét phạm vi công việc hoặc mốc thời gian thiếu | [Lỗi] Mở rộng A1 cho trường hợp **thông tin dự án** chưa đủ: PM yêu cầu bổ sung, nhu cầu chưa được cố định (CN-03). Sửa A1 hiện có, không tạo thêm một A1 thứ hai | CN-03 | A1 dẫn CN-03, có nhánh tương ứng trên AD |
| AD: decision "đủ thông tin" đặt sau action "Lưu" | [Lỗi] Đặt decision ngay sau action của bước 4, đúng thứ tự trong D | HD-MAU §4 | Thứ tự action trên AD trùng thứ tự bước trong D |
| Luồng chính bước 6–7: thiếu giai đoạn và %FTE theo từng vị trí | [Lỗi] Thêm bước xác định thời gian hoặc giai đoạn (CN-07) và mức tham gia %FTE (CN-08) cho từng vị trí | CN-07, CN-08; QT-02, QT-03 | Có ở D, AD và bảng quy tắc |
| E1 "lỗi kết nối CSDL"; các action "Đăng nhập", "Ghi log", "Nhấn…" trên AD | [Lỗi] Bỏ khỏi D và AD, vì đây là xử lý kỹ thuật, không phải nghiệp vụ | HD-MAU §3.3 | Không còn các từ "đăng nhập", "nhấn", "lỗi CSDL" |
| AD: hai action ở cuối nhánh không có luồng ra | [Lỗi] Nối về action sửa tương ứng, hoặc về final node | Ký pháp UML | Mọi node trên AD có luồng ra, trừ final node |
| Mã CN-V2-xx, RB-V2-xx trong bảng quy tắc | [Lỗi] Đổi sang mã của P1 (CN-01–11, QT-01–05) | P1 bảng CN, QT | Mọi mã tra được trong P1 |
| Tên trạng thái của nhu cầu: "Đã xây dựng" (D) và "Đã xây dựng nội dung" (AD) | [Chờ QĐ-02] Dùng đúng một bộ tên trạng thái chung cho V2 | CN-11, CN-13, CN-14 | Một tên cho một trạng thái, ở D, AD và sơ đồ trạng thái II.4 |
| Lớp `KyNangChuyenMon`, `CongViec`; thuộc tính `soLuongNhanSu`, `chiSoFTE` đặt ở NhuCauNguonLuc | [Lỗi] Dùng NhuCauNguonLuc, ViTriCanBoTri, YeuCauKyNang theo Hình II.3-2. Số lượng và tyLeFTE thuộc ViTriCanBoTri. Phạm vi công việc giữ là thuộc tính `phamViCongViec`, không tạo lớp CongViec | Hình II.3-2; CN-02, CN-06 | Tên lớp và vị trí thuộc tính trùng II.3 |

## V2b — Nguyễn Tuấn Long — UC-01.2, UC-01.3 (trọng tâm); UCD vùng UC-01

| Chỗ cần sửa | Cách sửa | Nguồn đối chiếu | Tiêu chí chấm đạt |
|---|---|---|---|
| UCD cấp vùng UC-01: thiếu 01.1 và PM–01.1 | [Lỗi] Vẽ một UCD vùng đủ 01.1–01.3, theo `UCD_UC-01.drawio`. V2a không vẽ lại | HD-PCCN §1; CN-01–17 | Đủ ba UC; PM nối 01.1 và 01.3; RM nối 01.2; 01.3 extend 01.2 |
| §2.2 bảng quan hệ: "UC-01.3 extend UC-01.3" | [Lỗi] Sửa thành "UC-01.3 extend UC-01.2" | UCD của chính bài | Bảng và hình cùng một quan hệ |
| 01.2 E1: có các bước PM điều chỉnh nhu cầu | [Lỗi] Trong 01.2, nhánh "chưa đủ điều kiện" dừng ở "RM chuyển lại PM kèm nội dung cần bổ sung" (CN-14). Việc PM sửa thuộc 01.3. Đổi mã E1 thành A1, vì đây là luồng nghiệp vụ hợp lệ | CN-14; HD-PCCN §3 | D và AD 01.2 không còn action của PM. Nhu cầu không chuyển "đã xác nhận" ngay sau khi PM sửa |
| 01.2 §4.1: đoạn văn mô tả điểm merge khác với hình | [Lỗi] Sửa đoạn văn theo hình: luồng quay về trước bước "RM xem xét" | AD 01.2 của bài | Văn bản mô tả đúng hình |
| 01.2: action bàn giao V3/V4 đặt ở làn Hệ thống | [Lỗi] Đặt ở làn RM: RM bàn giao, hệ thống ghi nhận (CN-16) | CN-16 | Làn trên AD trùng actor trong D |
| 01.3 trigger: chỉ có "RM trả lại" | [Chờ QĐ-12] Ghi đủ hai cách bắt đầu: RM trả lại (extend từ 01.2); PM nhận phản hồi từ V4 hoặc V10 (CN-17). Không bỏ nhánh V4/V10 | CN-14, CN-17 | D và AD có đủ hai cách bắt đầu |
| 01.3 bước 3–4 "Xem xét phản hồi", "Điều chỉnh nguồn lực" quá chung | [Lỗi] Ghi rõ PM sửa loại, quy mô, thời gian, %FTE; thêm A "PM giữ nguyên nhu cầu, ghi lý do". Sau khi sửa, gửi lại RM xem xét | CN-10, CN-15, CN-17 | Có ít nhất một A; có trên AD; kết thúc ở gửi lại RM |
| 01.3: merge ngay trước final node | [Lỗi] Bỏ merge, nối thẳng vào final node | Ký pháp UML | Không còn merge chỉ có một luồng ra final |
| Lớp: quyMoFTE, tyLeFTE, loaiNguonLuc đặt ở NhuCauNguonLuc | [Lỗi] Chuyển sang ViTriCanBoTri | Hình II.3-2 | Thuộc tính trùng II.3 |
| Đánh số mục "3.1.2–3.1.4" trong phần 01.3 | [Lỗi] Đổi thành 3.2.2–3.2.4 | – | Không trùng số mục với 01.2 |

## V3 — Lê Hoài Linh — UC-02.1 (trọng tâm); UCD vùng UC-02

| Chỗ cần sửa | Cách sửa | Nguồn đối chiếu | Tiêu chí chấm đạt |
|---|---|---|---|
| Toàn UC 02.1: thiếu luồng tiêu chí tạm | [Lỗi] Thêm A "RM đề xuất tiêu chí tạm cho kỹ năng chưa có tiêu chí → PMO duyệt hoặc từ chối". Tiêu chí đang chờ duyệt chưa được dùng. Thêm làn PMO trên AD | CN-19 | D, AD và bảng quy tắc có CN-19. Không nhánh nào dùng tiêu chí chưa duyệt |
| §7 "số mức chưa xác định"; bảng quy tắc còn ô trống; mã "QT-01..04" | [Lỗi] Ghi thang 5 mức theo CN-18. Điền bảng quy tắc bằng CN-18, CN-19, QT-06–11. QT-01–04 là quy tắc của V2, bỏ khỏi bài này | CN-18; QT-06–11 | Không còn ô trống; mỗi mã dẫn đúng nội dung |
| A1 "Ngừng áp dụng thay vì xóa": hộp nét đứt không có luồng ra | [Lỗi] Nối A1 về "Lưu thay đổi" hoặc về final node | Ký pháp UML | Mọi node có luồng ra |
| Bước 8 có "thông báo kết quả cho RM", AD không có | [Lỗi] Bỏ khỏi D, vì thông báo không phải bước nghiệp vụ. Nếu giữ thì thêm vào AD | HD-MAU §4 | D và AD trùng nhau |
| E1 "không có quyền", E3 "lưu không thành công"; decision "Có quyền?", "Lưu thành công?" | [Lỗi] Bỏ ở cả D và AD | HD-MAU §3.3 | Không còn kiểm tra quyền, lỗi lưu |
| UCD cấp vùng UC-02: chỉ có 02.1 | [Lỗi] Vẽ đủ 02.1–02.3 theo `UCD_UC-02.drawio`. RM nối cả ba; PMO nối 02.1 và 02.3; Nguồn lực nối 02.2 | CN-18–30 | Khớp `UCD_UC-02.drawio` |
| Sơ đồ lớp: lớp `RM`; lớp `Yeucauquanlytieuchi`, `Nhatkythaydoi` | [Lỗi] Bỏ lớp RM, vì actor không phải lớp miền. Hai lớp còn lại không có trong P1, bỏ. Dùng BoTieuChiNangLuc, TieuChiNangLuc, MucDoNangLuc, KyNang, NangLucKyNang theo Hình II.3-2 | Hình II.3-2; CN-18, CN-19, CN-23 | Tên lớp trùng II.3. Hai người khác nhau có cùng kỹ năng với mức khác nhau, dùng chung danh mục KyNang |
| UC cá nhân của V3 là 02.1 hay 02.2 | [Chờ QĐ-03] Giữ 02.1 cho tới khi có quyết định. Không bỏ phần 02.1 đã làm | HD-PCCN §5; Outline | UC cá nhân được ghi bằng mã và tên trong bài |

FDS tóm tắt 02.2, 02.3 trong bản Word đã đối chiếu CN-20–30, không có lỗi. V3 chỉ cần đọc và báo nếu thấy khác bài.

## V4 — Nguyễn Hoàng Linh — UC-03.3 (trọng tâm); UCD vùng UC-03

**Đính chính.** UCD gốc UC-03.3 của V4 **đã có** PMO nối với 03.3. Bảng kiểm UCD vùng trong bản tích hợp ngày 20/10 ghi "chưa có PMO", ghi như vậy là sai. Bỏ yêu cầu thêm PMO vào hình 03.3.

| Chỗ cần sửa | Cách sửa | Nguồn đối chiếu | Tiêu chí chấm đạt |
|---|---|---|---|
| UCD cấp vùng UC-03: chỉ có 03.3 | [Lỗi] Vẽ đủ 03.1–03.4 theo `UCD_UC-03.drawio`. RM nối cả bốn; PMO nối 03.3 và 03.4 | CN-31–46; CN-37, CN-43 | Khớp `UCD_UC-03.drawio`. PMO ở 03.3, 03.4 phụ thuộc QĐ-01 nhưng không xóa khỏi hình |
| E3 (bước 5) và hậu điều kiện "không có ứng viên đạt": chưa có phản hồi về V2 | [Lỗi] Thêm hướng xử lý theo thứ tự: chưa thử hết nguồn thì quay lại tìm kiếm nguồn kế tiếp (03.2, CN-33); đã thử các cách mà vẫn không có ứng viên thì RM gửi phản hồi về V2 (CN-46), V2 nhận ở 01.3 (CN-17) | CN-33, CN-46, CN-17 | Có nhánh CN-46 ở D và AD. Không phản hồi V2 khi chưa xét thứ tự ưu tiên nguồn |
| A3 và bảng quy tắc: "quá 6 tháng là quá hạn", dẫn QT-15 | [Lỗi] Giữ mốc 6 tháng nhưng ghi đúng căn cứ: đánh giá lại định kỳ 6 tháng ở CN-20. QT-15 chỉ nói "quá thời hạn cập nhật" | CN-20, CN-36; QT-15 | Mốc 6 tháng dẫn CN-20 |
| AD: hai luồng (nhánh "không" và nhánh sau PMO duyệt) cùng đi thẳng vào decision "Còn ứng viên đủ điều kiện?" | [Lỗi] Thêm merge node trước decision | Ký pháp UML | Mỗi decision chỉ có một luồng vào |
| AD: tiêu đề "Chỉ ứng viên đủ điều kiện mới được chấm điểm…" | [Lỗi] Đặt tiêu đề "UC-03.3 Đánh giá, xếp hạng và lập shortlist ứng viên" | HD-PCCN §1 | Tiêu đề trùng tên UC |
| AD chỉ có dạng ảnh, không có file `.drawio` | [Lỗi] Vẽ lại hoặc xuất AD sang `.drawio`, rồi nộp file nguồn. Bản Word chung đang để chỗ trống cho hình này | Yêu cầu nộp nguồn | Có `AD_UC-03.3.drawio`; PNG trong Word xuất từ file đó |
| Sơ đồ lớp: tên lớp trùng V3, V5; lớp `NguoiDung`, `Shortlist`; kỹ năng gắn trực tiếp vào ứng viên | [Lỗi] Dùng BoTieuChiPhuHop, TieuChiPhuHop, PhienTimKiem, KetQuaDanhGiaPhuHop, DiemTieuChi, DeNghiMienTru (Hình II.3-3). Kỹ năng của ứng viên tham chiếu NangLucKyNang (V3). Bỏ NguoiDung. Shortlist là thuộc tính `vaiTroShortlist` | Hình II.3-2, II.3-3; CN-30 | Tên lớp trùng II.3; không có bộ tiêu chí năng lực thứ hai ở V4 |
| Bảng vai trò Phần I (I.1.2) không có PMO ở V4 | [Chờ QĐ-01] Không sửa I FINAL. Giữ PMO trên UCD 03.3, 03.4 theo CN-37, CN-43 | P1 I.1.2; CN-37, CN-43 | Quyết định được ghi lại; sơ đồ không mất hành vi phê duyệt có nguồn |

## V5 — Nguyễn Hoàng Khánh Linh — UC-04.1 (trọng tâm); UCD vùng UC-04

| Chỗ cần sửa | Cách sửa | Nguồn đối chiếu | Tiêu chí chấm đạt |
|---|---|---|---|
| AD: rẽ nhánh sang 04.2/04.3 trước action "RM ghi nhận kết luận" | [Lỗi] Mọi nhánh đi qua "Ghi nhận kết luận theo bốn trạng thái" (CN-51) rồi mới rẽ: đáp ứng một phần sang 04.2, vượt tải ngoại lệ sang 04.3 | CN-51, CN-53, CN-56 | Mọi ứng viên có trạng thái và căn cứ trước khi bàn giao |
| A2 dữ liệu lịch chưa đủ rõ: AD thiếu nhánh "không chờ" | [Lỗi] Thêm cả hai nhánh: chờ xác nhận trong 2 ngày làm việc; hoặc không chờ thì coi như chưa có dữ liệu và yêu cầu xác nhận ngay. Kết quả lúc này là "chờ xác nhận", không phải kết luận hoàn tất | CN-52; QT-24 | D và AD có đủ hai nhánh; nhánh thiếu dữ liệu không bàn giao như kết luận đủ căn cứ |
| Bước 3–7: D xét từng ứng viên, AD không có vòng lặp | [Lỗi] Thêm vòng "Còn ứng viên cần đánh giá?" trên AD | CN-48–51 | Shortlist nhiều người cho ra kết luận riêng từng người |
| Cờ rủi ro quá tải | [Lỗi] Ghi rõ: trên 90% kéo dài liên tục trên 2 tuần thì gắn cờ Mức 2; cờ đi kèm kết luận sang V6, V10 và không tự kích hoạt V7 | CN-50; QT-22 | Không có nhánh nào tự chuyển V7 vì cờ Mức 2 |
| Action của RM đặt ở làn Hệ thống; một nhánh kết thúc bằng hộp chữ | [Lỗi] Đưa action RM về làn RM; hệ thống chỉ tính, tra cứu hỗ trợ. Thay hộp chữ bằng final node | CN-48–51 | Làn trùng actor trong D; không có nhánh kết thúc bằng hộp chữ |
| Ghi chú trên AD đánh số bước khác D (bước 6/7) | [Lỗi] Thống nhất số bước | – | Số bước trên AD trùng D |
| A6 yêu cầu gấp: "không tự chốt 24 hoặc 48 giờ" | [Chờ QĐ-04] Ghi đúng như P1: "thời hạn dưới 24–48 giờ"; đánh giá nhanh dựa trên phân bổ cứng (CN-58). Không tự chọn 24 hay 48 làm điều kiện số | CN-58 | Không có ngưỡng số tự đặt |
| Mã BR-V5, CN-V5; tên UC ở §1 khác §2.1 | [Lỗi] Đổi mã theo P1; dùng tên "Đánh giá khả năng tham gia" ở mọi chỗ | P1; HD-PCCN §1 | Mã tra được trong P1; một tên UC |
| UCD vùng: tiêu đề "PHÂN HỆ V5"; RM chỉ nối 04.1 | [Lỗi] Đặt tiêu đề "UC-04 Đánh giá khả năng tham gia (V5)"; nối RM với 04.2 và 04.3 | `UCD_UC-04.drawio`; CN-53, CN-56 | Khớp `UCD_UC-04.drawio` |
| Sơ đồ lớp: lớp `KetQuaDanhGia` trùng tên với kết quả của V4; lớp `YeuCauXacNhan` | [Lỗi] Đổi KetQuaDanhGia thành KetLuanKhaNangThamGia. Bản chung không có lớp YeuCauXacNhan: ngày yêu cầu, hạn xác nhận, lý do chờ xác nhận là thuộc tính của KetLuanKhaNangThamGia. Phương thức `ghiNhanXacNhanPM()` đã đúng người xác nhận (CN-54), giữ nguyên | Hình II.3-3; CN-52, CN-54 | Tên lớp trùng II.3; vẫn theo dõi được hạn 2 ngày làm việc |
| Sơ đồ lớp: hai bội số ghi sát nhau ở một đầu đường ("1 0..*"); bảng bội số để hai lựa chọn "1 — 0..* hoặc 1 — 0..1" cho KetQuaDanhGia–HoSoVuotTaiNgoaiLe | [Lỗi] Đặt mỗi bội số ở đúng đầu của nó. Chọn 1 — 0..*: kết luận bình thường không có hồ sơ vượt tải, một kết luận có thể có nhiều lần chuyển cấp | Hình II.3-3; CN-56, CN-57 | Bảng và hình cùng một bội số, đọc được đầu nào là của lớp nào |
| Lớp `YeuCauNguonLuc` (CN-127) | [Chờ QĐ-11] Bản chung chưa vẽ lớp này. Giữ CN-127 là bước tiếp nhận trong 04.1 | CN-47, CN-127 | Theo quyết định |
| §11 lẫn với §12; còn chữ mẫu | [Lỗi] Tách hai mục, xóa chữ mẫu | HD-MAU | Không còn chữ mẫu |

## V6 — Nguyễn Thi Thùy Linh — UC-05.1 (trọng tâm); UCD vùng UC-05

| Chỗ cần sửa | Cách sửa | Nguồn đối chiếu | Tiêu chí chấm đạt |
|---|---|---|---|
| Phần cuối AD có decision "PM phê duyệt?" | [Lỗi] 05.1 kết thúc ở "RM gửi phương án cho PM xem xét" (CN-68). Việc PM xác nhận hoặc yêu cầu sửa thuộc 05.2; phê duyệt chính thức thuộc V8 | CN-68, CN-69; HD-PCCN §3 | AD 05.1 không có action của PM, không tạo Locked Baseline |
| Nhánh nhận phản hồi kết thúc luôn; A4 trong D quay lại bước 5 | [Lỗi] Nối nhánh trên AD về action của bước 5 (sửa phương án) | HD-MAU §4 | Không kết thúc ở "Nhận phản hồi" |
| E1 quá hạn 3 ngày làm việc: có trong D, không có trên AD | [Chờ QĐ-13] Nếu giữ CN-73 ở 05.1 (như bảng II.1 đang ghi) thì thêm vào AD như một sự kiện theo dõi trạng thái "đang xây dựng", không chèn kiểm tra lặp ở mọi action | CN-73; QT-31 | D và AD trùng nhau |
| Bước 10 của D không có trên AD | [Lỗi] Thêm action tương ứng | – | Mọi bước của D có trên AD |
| UCD vùng: chỉ có 05.1; association có mũi tên | [Lỗi] Thêm 05.2 (PM, RM); bỏ mũi tên trên association | `UCD_UC-05.drawio` | Khớp `UCD_UC-05.drawio` |
| Sơ đồ lớp: `LichPhanBo`, `KhaNangThamGia` | [Lỗi] Dùng PhanBoNguonLuc (V5) và KetLuanKhaNangThamGia (V5). ChiTietBoTri gắn người, vị trí, giai đoạn, tỷ lệ và thời gian. Không tạo lịch nguồn lực thứ hai ở V6 | Hình II.3-4; CN-61, CN-62; QT-29 | Cùng một vị trí có thể bố trí tỷ lệ khác nhau theo giai đoạn |
| Lần trình và phiên bản phương án | [Chờ QĐ-05] Thống nhất với V8 cách phân biệt "sửa hồ sơ" và "trình lại"; chưa cố định 1 phương án : 1 hồ sơ | CN-96, CN-101, CN-102 | V6 và V8 dùng cùng định danh phiên bản |

FDS tóm tắt 05.2 trong bản Word đã có đủ các hướng: PM xác nhận hoặc yêu cầu sửa; RM đối chiếu lịch; chuyển V7 hoặc V8/V9. V6 đọc lại, không cần viết thêm.

## V7 — Lưu Thùy Linh — UC-06.2 (trọng tâm); UCD vùng UC-06

| Chỗ cần sửa | Cách sửa | Nguồn đối chiếu | Tiêu chí chấm đạt |
|---|---|---|---|
| E1 "dưới ngưỡng" ghi "< 20%", "chuyển PM tự đàm phán" | [Lỗi] Ghi "dưới Mức 3 (không quá 120% và không thuộc dự án Hạng ưu tiên 1): chỉ ghi nhận để theo dõi, kết thúc" ở cả D và AD | QT-33 | Không còn "< 20%" |
| A3 tỷ lệ 50/50, A4 thuê ngoài khẩn | [Lỗi] Bỏ tỷ lệ 50/50 và chức năng thuê ngoài khẩn, vì P1 không có. Giữ tham chiếu làm thêm giờ khẩn cấp Mức 5 nếu cần, dẫn đúng thang 5 mức | P1 I.1.3.7, thang 5 mức; QT-37 | Không có tỷ lệ hay chức năng tự đặt |
| Bước 1–2 và A1 chứa nội dung của 06.1 (phân tích) và 06.3 (phân xử) | [Lỗi] Bước 1–2 chuyển thành tiền điều kiện ("đã có danh sách điểm xung đột từ 06.1"). A1 chỉ ghi "hết hạn hoặc bế tắc → chuyển 06.3" | HD-PCCN §3; CN-74, CN-83 | D và AD 06.2 không có bước phân tích ngưỡng hay phân xử |
| AD: các nhánh làm mịn, san bằng, bế tắc nối nhầm vào action "đề xuất thay đổi"; làm mịn rồi luôn san bằng | [Lỗi] Tách thành các nhánh có guard, mỗi nhánh tới đúng action của nó rồi mới hội tụ | CN-80, CN-81, CN-82, CN-86 | Đi thử từng nhánh không gặp action sai; làm mịn không tự đổi ngày hoàn thành |
| Bước 3 actor RM, AD đặt ở làn PM | [Lỗi] PM đàm phán (CN-78), RM điều phối và ghi nhận (CN-79). Sửa đúng câu bị gán nhầm, không dời toàn bộ sang RM | CN-78, CN-79 | Làn trùng actor trong D |
| Decision thời hạn đàm phán khó hiểu | [Lỗi] Ghi guard theo CN-79: "quá 3 ngày làm việc hoặc bế tắc" | CN-79; QT-36 | Không có số ngày khác P1 |
| Tiền điều kiện: thiếu nguồn V5; coi V10 là nguồn kích hoạt | [Lỗi] Nguồn kích hoạt là V6 (CN-72) và V5 (CN-55); V10 chỉ cung cấp thông tin (CN-75) | CN-55, CN-72, CN-75 | Tiền điều kiện đúng nguồn |
| Dùng nhầm mã CN-01..14 của V2 | [Lỗi] Đổi sang CN-74–88, QT-32–39 | P1 | Mọi mã thuộc V7 |
| UCD vùng: `include` 06.1 | [Lỗi] Bỏ include. Thêm "06.3 extend 06.2" | `UCD_UC-06.drawio` | Khớp `UCD_UC-06.drawio` |
| Lớp ConflictLog, ChangeRequest, KichBanCanDoi, DiemXungDotNguonLuc | [Lỗi] Đổi thành DiemXungDot, NhatKyXuLyXungDot, PhanXuXungDot, DeXuatThayDoi (Hình II.3-4). Bỏ lớp kỹ thuật | Hình II.3-4; CN-86, CN-87; QT-39 | Tên lớp trùng II.3 |
| Bước 10, bảng quy tắc, sơ đồ lớp: "ghi vết vĩnh viễn", "không cho sửa/xóa" | [Lỗi] P1 quy định lưu nhật ký xử lý xung đột tối thiểu 3 năm (PCN-06), không phải vĩnh viễn. Sửa câu, không thêm yêu cầu kỹ thuật | PCN-06; CN-87; QT-38 | Không còn "vĩnh viễn" |
| II.4 nháp của V7 (Sequence, State) | [Cần xác nhận] Kiểm tra trong sơ đồ nháp: người ra quyết định (PMO, CEO) phải là bên gửi thông điệp quyết định; đối tượng hồ sơ chỉ ghi nhận. Trạng thái phải là trạng thái của đối tượng, không phải tên thao tác | CN-84, CN-85 | Không đối tượng dữ liệu nào tự quyết định |
| Khoảng 100–120% trên thang 5 mức | [Chờ QĐ-06] Không tự gán khoảng này vào một mức | Thang 5 mức; QT-33 | Không có quy tắc phân loại mới |

## V8 — Ngọc Linh — UC-07.1 (trọng tâm); UCD vùng UC-07

Kiểm tra trên ba hình mới: `[PTTKHTTT] MNV8-UC-07.1.drawio.png`, `MNV8-AD UC-07.1.drawio.png` và hình sơ đồ lớp. Ba ảnh này có nhúng nguồn draw.io (`V8_nguon_nhung_3_trang.drawio`).

| Chỗ cần sửa | Cách sửa | Nguồn đối chiếu | Tiêu chí chấm đạt |
|---|---|---|---|
| UCD vùng: include toàn vùng UC-08, UC-09; "07.3 include 07.1"; thiếu 07.4 | [Lỗi] Bỏ UC ngoài vùng và hai include. Thêm 07.4. Giữ "07.2 extend 07.1" | `UCD_UC-07.drawio`; CN-89–102 | Khớp `UCD_UC-07.drawio`. Thông tin V9, V10 là dữ liệu tham chiếu, không phải UC |
| AD: "Cho phép PMO tự phê duyệt phương án", "Ra quyết định" | [Lỗi] Đổi thành "PMO đối chiếu DoA, xác định cấp thẩm quyền" (CN-90) và "Kết luận hồ sơ đủ hoặc chưa đủ cơ sở". Quyết định chính thức thuộc 07.3, 07.4 | CN-90, CN-97; P1 I.1.3.8 | 07.1 không có quyết định phê duyệt |
| A2 có bước RM giải trình; AD có vòng "gửi yêu cầu giải trình → RM" | [Lỗi] A2 và AD dừng ở "chuyển UC-07.2" (extend). Không có action của RM trong 07.1 | CN-95, CN-96 | 07.1 không còn action của RM |
| Bước 4 "<<include>> V9/V10" | [Lỗi] Ghi "PMO xem thông tin chi phí (V9) và dự báo (V10)" | CN-93, CN-94 | D không còn chữ "include" |
| A1 chuyển cấp CEO | [Lỗi] Đặt guard "Mức 4–5" và ghi hạn 1 ngày làm việc | CN-91; QT-42 | Guard và hạn đúng P1 |
| Sơ đồ lớp: ThongTinChiPhi, ThongTinDuBao sao chép dữ liệu V9, V10 | [Lỗi] Tham chiếu DanhGiaChiPhi (V9) và KetQuaDuBao (V10), không tạo bản sao | Hình II.3-5, II.3-6; CN-93, CN-94 | Dữ liệu vẫn thuộc V9, V10 |
| Sơ đồ lớp: YeuCauGiaiTrinh 0..1 trong khi D cho phép nhiều đợt | [Lỗi] Một hồ sơ có 0..* yêu cầu giải trình | Hình II.3-4; CN-95 | Bảng, hình và D cùng bội số |
| Sơ đồ lớp: MaTranPhanQuyenDoA; HoSoTrinhDuyet–PhuongAnBoTri 1:1 | [Chờ QĐ-05, QĐ-19] Chưa ép 1:1. DoA giữ ở dạng quy tắc cho tới khi có quyết định | CN-101, CN-102 | Theo quyết định |
| UC cá nhân 07.1 hay 07.3 | [Chờ QĐ-03] Giữ 07.1 | HD-PCCN §5 | Theo quyết định |

FDS tóm tắt 07.2, 07.3, 07.4 trong bản Word đã đối chiếu CN-95–102 và QT-40–46, không có lỗi. Các ngưỡng "trên 110% kéo dài trên 2 tuần" và "2 ngày làm việc" đều có nguồn (QT-41, QT-43).

## V9 — Ngô Nhật Long — UC-08.1 (trọng tâm); UCD vùng UC-08

| Chỗ cần sửa | Cách sửa | Nguồn đối chiếu | Tiêu chí chấm đạt |
|---|---|---|---|
| D và AD 08.1 mang phạm vi cả vùng (tính, đối chiếu, so sánh, hướng xử lý); tiêu đề AD là tên vùng | [Chờ QĐ-10] Đề xuất: giữ 08.1 đúng tên "Tính và cập nhật chi phí phương án" (CN-103–107). Phần đối chiếu, so sánh, hướng xử lý chuyển sang FDS 08.2–08.4, đã có trong bản Word. Dùng lại nội dung đã viết, không viết lại cả bài | HD-PCCN §1; CN-103–112, 128, 129 | Tên và phạm vi 08.1 đúng mã; không hành vi nào thuộc hai UC |
| Bước 6 "Đối chiếu ngân sách" ở làn Hệ thống | [Lỗi] Tài chính và PM đối chiếu, hệ thống tính và hiển thị hỗ trợ | CN-108 | Làn trùng actor |
| Bước 7, A2 "gắn cấp ≤ 10% / > 10%" | [Lỗi] Gắn cấp không phải phê duyệt. Hoặc dừng rõ ở "chuyển 08.4"; hoặc, nếu QĐ-10 chọn gộp, thêm làn PMO, CEO và bước ra quyết định (CN-128, CN-129) | QT-51; CN-111, CN-128, CN-129 | Không coi gắn cấp là đã duyệt |
| E1 "yêu cầu Tài chính bổ sung" có trong D, không có trên AD | [Lỗi] Thêm nhánh trên AD. Thiếu dữ liệu thì chưa kết luận chính thức | CN-105, CN-106 | D và AD cùng kết quả và người cần bổ sung |
| E2 "không có quyền"; bước 8 ghi tài khoản thực hiện | [Lỗi] Bỏ phần quyền và ghi tài khoản khỏi luồng | HD-MAU §3.3 | Không còn kiểm tra quyền |
| Công thức tỷ lệ vượt ở A2 | [Chờ QĐ-07] Ghi công thức hiện có là giả định chờ duyệt. Chưa tính khi ngân sách còn lại ≤ 0. Chưa tự chọn cấp duyệt từ tỷ lệ chưa xác định | QT-51 | Có công thức, đơn vị và trường hợp biên đã duyệt trước khi tính minh họa |
| Mã CN-V9, RB-V9, PCN-V9; include ngược từ 07.1 | [Lỗi] Đổi mã theo P1; bỏ include | P1 | Mã tra được trong P1 |
| UCD vùng và sơ đồ lớp chỉ có link Drive | [Lỗi] Chèn hình vào bài và nộp `.drawio`. Đối chiếu với `UCD_UC-08.drawio` | `UCD_UC-08.drawio` | Bài có hình; có file nguồn |
| Lớp PhanBoNguonLuc (dùng cho dòng phương án), NguoiDung, NguongPheDuyetNganSach | [Lỗi] Dòng phương án dùng ChiTietBoTri; bỏ NguoiDung. Ngưỡng 10% giữ là quy tắc (QĐ-19) | Hình II.3-5 | Từ một lần đánh giá truy được số liệu chi phí và ngân sách tại thời điểm đó |

## V10 — Trưởng nhóm — UC-09.1, UC-09.2

Bản Word dùng UC Description V10 do ChatGPT sửa (`v10.json`). Đã đối chiếu với P1:

- I.1.3.10;
- dòng 41 phần tổng quan: V10 phản hồi cho V2, V6, V7, V8 và PM;
- CN-113–126, QT-52–57, PCN-03.

AD đã vẽ lại dạng draw.io gốc. Hai chỗ khác bản ChatGPT:

- thêm merge node khi hai luồng cùng vào một action;
- đặt final node trong làn Hệ thống.

| Chỗ cần sửa | Cách sửa | Nguồn đối chiếu | Tiêu chí chấm đạt |
|---|---|---|---|
| 09.1 bảng quy tắc dẫn "D08–D09" | [Lỗi] Đã bỏ trong bản Word, vì hai mã này không có trong P1 hay danh sách quyết định. Giữ QT-53–54 | P1 | Không còn mã không tra được |
| 09.1 E1 và 09.2 E1: chính sách dự báo một phần khi dữ liệu thiếu | [Chờ QĐ-08] Bản Word dừng trước dự báo chính thức và không coi danh sách nhu cầu rỗng là cầu bằng 0 | QT-55; CN-113, CN-116 | Theo quyết định |
| 09.1 bước 8: điều kiện chuyển kết quả | [Chờ QĐ-09] Giữ quyết định của RM (CN-121). Chốt câu ở I.3.9 bước 7 là điều kiện bắt buộc chuyển hay căn cứ để RM cân nhắc | CN-121; I.3.9 bước 7 | Theo quyết định |

## Việc chung và giao diện liên vùng — Trưởng nhóm

| Chỗ cần sửa | Cách sửa | Nguồn đối chiếu | Tiêu chí chấm đạt |
|---|---|---|---|
| V2 ↔ V4: phản hồi "không có ứng viên đáp ứng" | [Lỗi] V4 gửi (03.3, CN-46), V2 nhận (01.3, CN-17). Hai bài phải dùng cùng tên thông tin và cùng điểm vào | CN-17, CN-46 | Nhánh gửi ở V4 và trigger ở V2 trùng tên |
| V5 → V7: xung đột lịch; cờ Mức 2 | [Lỗi] V5 chỉ chuyển hồ sơ xung đột (CN-55). Cờ Mức 2 đi sang V6, V10, không kích hoạt V7 | CN-50, CN-55; QT-26 | V5 và V7 dùng cùng điều kiện chuyển |
| V6 → V7 / V8, V9: rẽ nhánh theo nghi ngờ xung đột | [Lỗi] V6 (05.2, CN-72) chuyển V7 khi có nghi ngờ, sang V8, V9 khi không có. V7 nhận ở 06.1 | CN-72, CN-88 | Điểm rẽ trùng nhau ở V6 và V7 |
| V8 → V6/V7: hồ sơ trả về khi yêu cầu chỉnh sửa | [Chờ QĐ-05] Hướng trả về đã rõ (CN-101). Còn chờ cách đánh phiên bản phương án và lần trình | CN-101, CN-102 | V6, V7, V8 dùng cùng định danh |
| V8, V9 → V10: cam kết đã duyệt, thông tin chi phí | [Lỗi] V10 chỉ nhận cam kết đã xác lập Locked Baseline (CN-100). Chi phí V9 chỉ là căn cứ bổ sung, không dùng để dự báo (CN-124, QT-57) | CN-100, CN-124; QT-57 | Không bài nào dùng chi phí V9 làm đầu vào dự báo |
| FDS tóm tắt 08.2 trong bản Word: công thức tỷ lệ vượt ghi như quy tắc đã chốt, dẫn mã "D07" | [Lỗi] Đã bỏ công thức và mã D07 khỏi FDS 08.2 trong bản Word; ghi "cách tính tỷ lệ vượt chờ QĐ-07". Ngưỡng 10% giữ theo QT-51 | QT-47, QT-51 | FDS không chứa công thức chưa duyệt |
| Bảng Summary của HD-PCCN (P-01..P-12) | [Chờ QĐ-18] Sửa sau khi trưởng nhóm duyệt | `Bang_doi_chieu_PCCN.md` | HD-PCCN khớp bảng II.1 |
