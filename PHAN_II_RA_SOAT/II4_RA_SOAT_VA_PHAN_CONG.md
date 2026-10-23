# II.4: rà soát sơ đồ hiện có và phân công vẽ lại

Bản rà soát ngày 22/10/2026. Đầu vào gồm:

- 19 hình II.4 trong `PTTKHTTT_PHAN_II.pdf` của ChatGPT (trang 53–74): 6 sơ đồ trạng thái, 4 sơ đồ giao tiếp và 9 sơ đồ tuần tự;
- mục II.4 trong bài V7 (`MNV7_II_Thiết kế Logic.docx`): một bảng trạng thái, một danh sách thông điệp giao tiếp và một ảnh sơ đồ tuần tự.

Các thành viên khác chưa nộp sơ đồ II.4.

Cách đọc nhãn **[Chờ QĐ-xx]** giống file `II2_YEU_CAU_SUA_THEO_VUNG.md`. Mã QĐ tra trong `DANH_SACH_CHO_QUYET_DINH.md`.

## 1. Lỗi chung của 19 hình ChatGPT

Các lỗi này đã kiểm trên từng trang PDF và áp dụng cho mọi dòng ở mục 2.

1. **Không có file nguồn.** Gói zip không có file `.drawio` hay mã nguồn nào cho II.4. README của gói nói có thư mục draw.io, nhưng thư mục đó không có trong gói. Vì vậy không có hình nào được chèn thẳng vào bản Word. Sơ đồ nào được giữ thì phải vẽ lại bằng draw.io.
2. **Sơ đồ tuần tự sai ký hiệu:**
   - Tác nhân vẽ bằng hộp chữ nhật, không vẽ hình người.
   - Không có thanh kích hoạt.
   - Thông điệp trả về vẽ nét liền, không phải nét đứt.
   - Điều kiện được ghi trong ngoặc vuông trên thông điệp, ví dụ "[Đủ cơ sở]", nhưng không có khung `alt`, `opt` hay `loop`. Vì vậy sơ đồ không thể hiện nhánh còn lại.
3. **Sơ đồ giao tiếp sai ký hiệu:** tác nhân vẽ bằng hộp chữ nhật. Thông điệp đi và thông điệp hiển thị bị ghép chung trên một nhãn, ví dụ "1. … → 1.2. … ←".
4. **Sơ đồ trạng thái sai ký hiệu:** hầu hết không có trạng thái kết thúc, và một số nhãn bị cắt ở mép hình (V2, V5).

## 2. Bảng rà soát

Quyết định có năm loại: **Giữ**, **Sửa**, **Gộp-thay thế**, **Bỏ** và **Chờ quyết định**. "Giữ" chỉ có nghĩa là giữ nội dung; hình vẫn phải vẽ lại vì lỗi 1.

### II.4.1. Sơ đồ trạng thái

| Vùng/UC/đối tượng | Sơ đồ hiện có | Đánh giá | Quyết định đề xuất | Căn cứ | Người thực hiện tiếp |
|---|---|---|---|---|---|
| V2 / UC-01.1–01.3 / NhuCauNguonLuc | ChatGPT, tr. 53 | Đối tượng có vòng đời thật, gồm gửi, trả lại và xác nhận. Lỗi: tên trạng thái "Chờ xác nhận", "Cần điều chỉnh" chưa thống nhất với tên trong CN; nhãn "Phản hồi V4, V10 hoặc t…" bị cắt; không có trạng thái kết thúc | **Sửa** [Chờ QĐ-02 cho tên trạng thái] | CN-03, CN-11, CN-13, CN-14, CN-17 | V2b (Nguyễn Tuấn Long) |
| V3 / UC-02.2–02.3 / NangLucKyNang | ChatGPT, tr. 55 | Có ba trạng thái: Tự khai báo, Cần kiểm chứng, Đã xác nhận. Vòng đời đơn giản; đánh giá lại định kỳ (CN-20) chỉ quay về Cần kiểm chứng | **Chờ quyết định** (QĐ-17). Nếu giữ: thêm sự kiện đánh giá lại 6 tháng và trạng thái kết thúc | CN-20, CN-28 | V3 (Lê Hoài Linh), nếu giữ |
| V5 / UC-04.1 / KetLuanKhaNangThamGia | ChatGPT, tr. 56 | Các "trạng thái" là kết quả phân loại (có thể tham gia, tham gia một phần, chưa đủ rõ), đi qua một nút quyết định. Đây không phải vòng đời đối tượng. Hai nhãn bị cắt | **Bỏ**. Nhánh phân loại đã có trong AD 04.1 | CN-47–CN-52 | – |
| V6 / UC-05.1–05.2 / PhuongAnBoTri | ChatGPT, tr. 57 | Vòng đời dừng ở "Đã rà soát". Còn thiếu các trạng thái sau khi phương án sang V7 và V8: trình duyệt, phê duyệt, xác lập Locked Baseline | **Sửa**. Nối tiếp tới phê duyệt và Locked Baseline | CN-60–CN-73, CN-99; QT-31 | V6 (Nguyễn Thi Thùy Linh) chủ trì, V8 (Ngọc Linh) góp các trạng thái sau khi trình |
| V7 / UC-06.1–06.3 / DiemXungDot | ChatGPT, tr. 58 và bảng 8 dòng của V7 | Có hai bản cho cùng một đối tượng. Bản của V7 dùng sự kiện, guard và hành động, nhưng: tên trạng thái bằng tiếng Anh; ghi "ghiVetVinhVien" trong khi PCN-06 ghi thời hạn lưu; chưa có hình draw.io. Bản ChatGPT có tên tiếng Việt nhưng chữ quá nhỏ | **Gộp-thay thế**. Lấy bản V7 làm gốc, dùng tên trạng thái tiếng Việt, đối chiếu điều kiện chuyển với thang 5 mức và QT-33–QT-39 | CN-74–CN-88; QT-33–QT-39; PCN-06 | V7 (Lưu Thùy Linh) |
| V8 / UC-07.1–07.4 / HoSoTrinhDuyet | ChatGPT, tr. 59 | Vòng đời đủ: tiếp nhận, rà soát, giải trình, quyết định, phê duyệt hoặc từ chối hoặc trả lập lại. Không có trạng thái kết thúc | **Giữ** nội dung, vẽ lại, thêm trạng thái kết thúc | CN-89–CN-102; QT-40–QT-46 | V8 (Ngọc Linh) |

### II.4.2. Sơ đồ giao tiếp

| Vùng/UC/đối tượng | Sơ đồ hiện có | Đánh giá | Quyết định đề xuất | Căn cứ | Người thực hiện tiếp |
|---|---|---|---|---|---|
| V3 / UC-02.1 / tra cứu bộ tiêu chí | ChatGPT, tr. 61 | Chỉ đọc một danh mục qua hai lớp. Sơ đồ tuần tự 02.1 đã có bước đọc tiêu chí, nên hình này không thêm thông tin | **Bỏ** | CN-18, CN-19 | – |
| V4 / UC-03.3 / tra cứu căn cứ đánh giá ứng viên | ChatGPT, tr. 62 | Đây là truy vấn thật trên nhiều lớp. Thiếu KetQuaDanhGiaPhuHop và TieuChiPhuHop, là hai lớp chứa khoảng thiếu và căn cứ (Hình II.3-3) | **Sửa** | CN-34–CN-42; QT-15, QT-16 | V4 (Nguyễn Hoàng Linh) |
| V7 / UC-06.x / thông tin xung đột | 6 thông điệp trong bài V7 | Dùng các lớp kỹ thuật không có trong II.3 (Controller, CPMAnalysisService). Thông điệp 6 "startSLACountdownTimer" là thao tác ghi, không phải truy vấn | **Chờ quyết định** (QĐ-17). Nếu giữ: chỉ giữ thông điệp đọc, dùng lớp II.3 | CN-74–CN-77 | V7 (Lưu Thùy Linh), nếu giữ |
| V9 / UC-08.3 / so sánh phương án | ChatGPT, tr. 63 | Đúng loại truy vấn. Chưa dùng SoSanhPhuongAn và ChiTietSoSanh là hai lớp V9 trong Hình II.3-5 | **Sửa** | CN-110; QT-50 | V9 (Ngô Nhật Long) |
| V10 / UC-09.1 / tình trạng cung cầu | ChatGPT, tr. 64 | Đúng loại truy vấn, đúng lớp KetQuaDuBao và DongDoiChieuCungCau | **Giữ** nội dung, sửa ký hiệu và vẽ lại | CN-123; PCN-08 | Trưởng nhóm |

### II.4.3. Sơ đồ tuần tự

| Vùng/UC/đối tượng | Sơ đồ hiện có | Đánh giá | Quyết định đề xuất | Căn cứ | Người thực hiện tiếp |
|---|---|---|---|---|---|
| V2 / UC-01.1 / tạo nhu cầu | Chưa có | UC-01.1 là UC trọng tâm của V2a và là thao tác ghi dữ liệu, nhưng chưa có sơ đồ tương tác nào | **Vẽ mới** | CN-01–CN-09, CN-11 | V2a (Nguyễn Thị Thùy Linh) |
| V2 / UC-01.2 / xác nhận và bàn giao | ChatGPT, tr. 66 | Luồng đúng. Chưa có khung `alt` cho nhánh trả lại PM bổ sung | **Sửa** [Chờ QĐ-02 cho tên trạng thái ghi ở bước 6] | CN-12–CN-14, CN-16 | V2b (Nguyễn Tuấn Long) |
| V3 / UC-02.1 / đề nghị và duyệt tiêu chí tạm | ChatGPT, tr. 67 | Có PMO duyệt. Chưa có khung `alt` cho duyệt và từ chối | **Sửa** [Chờ QĐ-03] | CN-18, CN-19 | V3 (Lê Hoài Linh) |
| V4 / UC-03.3 / xét miễn trừ điều kiện bắt buộc | ChatGPT, tr. 68 | PMO duyệt miễn trừ, nên phụ thuộc QĐ-01. Chưa có khung `alt` | **Sửa** [Chờ QĐ-01] | CN-34–CN-37; QT-13, QT-14 | V4 (Nguyễn Hoàng Linh) |
| V5 / UC-04.1 / ghi kết luận khả năng tham gia | ChatGPT, tr. 69 | Chưa có khung `loop` cho "từng ứng viên". Chưa có bước PM gửi yêu cầu (CN-127) | **Sửa** [Chờ QĐ-11] | CN-47–CN-52, CN-59, CN-127 | V5 (Nguyễn Hoàng Khánh Linh) |
| V6 / UC-05.1 / lập và gửi phương án | ChatGPT, tr. 70 | Luồng đúng. Thiếu nhánh quá 3 ngày | **Sửa** [Chờ QĐ-13] | CN-60–CN-68, CN-73 | V6 (Nguyễn Thi Thùy Linh) |
| V7 / UC-06.2 / cân đối và bàn giao | ChatGPT, tr. 71 và ảnh trong bài V7 | Có hai bản. Bản V7 thể hiện đàm phán và leo thang PMO, sát QT hơn. Bản ChatGPT có phần bàn giao sang V6, V8 | **Gộp-thay thế**. Lấy bản V7 làm gốc, thêm bước bàn giao của bản ChatGPT | CN-78–CN-82, CN-86–CN-88 | V7 (Lưu Thùy Linh) |
| V8 / UC-07.1 / rà soát hồ sơ | ChatGPT, tr. 72 | Truy vết ghi CN-89–96, nhưng CN-95, CN-96 thuộc UC-07.2. Chưa có khung `alt` cho kết luận đủ cơ sở và cần giải trình; nhánh giải trình chỉ dừng ở việc chuyển sang 07.2 | **Sửa** [Chờ QĐ-03] | CN-89–CN-94 | V8 (Ngọc Linh) |
| V9 / UC-08.1 / tính dự toán | ChatGPT, tr. 73 | Đúng phạm vi CN-103–CN-107. Chưa có nhánh thiếu đơn giá | **Sửa** [Chờ QĐ-10] | CN-103–CN-107 | V9 (Ngô Nhật Long) |
| V10 / UC-09.2 / lưu kết quả dự báo | ChatGPT, tr. 74 | Có chữ "từng nhu cầu" nhưng không có khung `loop`. Không thấy ghi DongDoiChieuCungCau dù nhãn bước 5 có nhắc | **Sửa** [Chờ QĐ-08] | CN-116–CN-119, CN-125, CN-126 | Trưởng nhóm |

Tổng hợp:

| Loại sơ đồ | Giữ hoặc sửa | Gộp | Bỏ | Chờ quyết định | Vẽ mới |
|---|---|---|---|---|---|
| Trạng thái | 3 | 1 | 1 | 1 | – |
| Giao tiếp | 3 | – | 1 | 1 | – |
| Tuần tự | 8 | 1 | – | – | 1 |

UC-01.3 và UC-09.1 không có sơ đồ tuần tự riêng:

- 01.3 đã nằm trong sơ đồ trạng thái NhuCauNguonLuc (nhánh "Cần điều chỉnh").
- 09.1 có sơ đồ giao tiếp.

## 3. Bảng phân công

Mỗi thành viên có ít nhất một sơ đồ tương tác cho UC trọng tâm của mình.

Sơ đồ có dòng "[Chờ QĐ-xx]" chỉ bắt đầu vẽ sau khi trưởng nhóm chốt mã đó. Sơ đồ ghi "nếu giữ" chỉ làm khi QĐ-17 chọn giữ.

| Thành viên/vùng | UC hoặc đối tượng | Loại sơ đồ cần làm | Lý do cần sơ đồ | Đầu vào phải ổn định | File nguồn cần bàn giao | Tiêu chí nghiệm thu |
|---|---|---|---|---|---|---|
| V2a – Nguyễn Thị Thùy Linh | UC-01.1 | Tuần tự | Ghi nhu cầu mới, gồm kiểm tra dữ liệu bắt buộc và FTE ≤ 1,0 | D và AD 01.1 đã sửa theo file II.2; lớp NhuCauNguonLuc, ViTriCanBoTri, YeuCauKyNang (Hình II.3-2) | `SEQ_UC-01.1.drawio` | Mọi bước của luồng chính D có thông điệp tương ứng. A1 nằm trong khung `alt`. Chỉ dùng lớp trong II.3 |
| V2b – Nguyễn Tuấn Long | NhuCauNguonLuc | Trạng thái | Nhu cầu đi qua nhiều lần gửi, trả lại và xác nhận | QĐ-02 | `SM_NhuCauNguonLuc.drawio` | Mỗi chuyển trạng thái ghi sự kiện và guard có CN. Có trạng thái đầu và kết thúc. Tên trạng thái theo QĐ-02 |
| V2b – Nguyễn Tuấn Long | UC-01.2 | Tuần tự | Ghi xác nhận và bàn giao cho V3, V4 | QĐ-02; D 01.2 | `SEQ_UC-01.2.drawio` | Có khung `alt` cho xác nhận và trả lại. Tên trạng thái khớp sơ đồ trạng thái |
| V3 – Lê Hoài Linh | UC-02.1 | Tuần tự | Ghi tiêu chí tạm và PMO duyệt | QĐ-03 | `SEQ_UC-02.1.drawio` | Có khung `alt` cho duyệt và từ chối. Lớp BoTieuChiNangLuc, TieuChiNangLuc |
| V3 – Lê Hoài Linh | NangLucKyNang | Trạng thái (nếu giữ) | Có kiểm chứng và đánh giá lại định kỳ | QĐ-17 | `SM_NangLucKyNang.drawio` | Có sự kiện đánh giá lại 6 tháng (CN-20). Có trạng thái kết thúc |
| V4 – Nguyễn Hoàng Linh | UC-03.3 | Giao tiếp | Truy vấn căn cứ của ứng viên qua nhiều lớp | Hình II.3-3 | `COM_UC-03.3.drawio` | Có HoSoNangLuc, NangLucKyNang, KetQuaDanhGiaPhuHop, TieuChiPhuHop. Tác nhân vẽ bằng hình người. Thông điệp đánh số 1, 1.1, 1.1.1 |
| V4 – Nguyễn Hoàng Linh | UC-03.3 | Tuần tự | Ghi đề nghị miễn trừ và kết quả duyệt | QĐ-01 | `SEQ_UC-03.3_mien_tru.drawio` | Người duyệt đúng QĐ-01. Có khung `alt` cho duyệt và từ chối |
| V5 – Nguyễn Hoàng Khánh Linh | UC-04.1 | Tuần tự | Ghi kết luận cho từng ứng viên | QĐ-11 | `SEQ_UC-04.1.drawio` | Có khung `loop` theo ứng viên và khung `alt` theo ba loại kết luận. Bước tiếp nhận yêu cầu theo QĐ-11 |
| V6 – Nguyễn Thi Thùy Linh | PhuongAnBoTri | Trạng thái | Phương án đi qua V6, V7, V8 trước khi xác lập Locked Baseline | QĐ-13; trạng thái sau khi trình do V8 cung cấp | `SM_PhuongAnBoTri.drawio` | Đi tới Locked Baseline (CN-99). V8 đã xác nhận phần trạng thái của V8 |
| V6 – Nguyễn Thi Thùy Linh | UC-05.1 | Tuần tự | Ghi phương án và các dòng bố trí | QĐ-13 | `SEQ_UC-05.1.drawio` | Có khung `opt` cho nhánh quá 3 ngày. Lớp PhuongAnBoTri, ChiTietBoTri, RuiRoViTri |
| V7 – Lưu Thùy Linh | DiemXungDot | Trạng thái | Xung đột qua đàm phán, phân xử và đề xuất thay đổi | Thang 5 mức; QT-33–QT-39 | `SM_DiemXungDot.drawio` | Một bản duy nhất. Tên trạng thái tiếng Việt. Mỗi guard có QT hoặc CN. Thời hạn lưu theo PCN-06 |
| V7 – Lưu Thùy Linh | UC-06.2 | Tuần tự | Ghi kết quả cân đối, leo thang PMO và bàn giao | – | `SEQ_UC-06.2.drawio` | Có khung `alt` cho thống nhất và hết 3 ngày. Có bước bàn giao sang V6, V8. Chỉ dùng lớp II.3 |
| V7 – Lưu Thùy Linh | UC-06.x | Giao tiếp (nếu giữ) | Truy vấn thông tin điểm xung đột | QĐ-17 | `COM_UC-06.x.drawio` | Chỉ có thông điệp đọc. Không dùng Controller hay Service |
| V8 – Ngọc Linh | HoSoTrinhDuyet | Trạng thái | Hồ sơ có nhiều vòng giải trình và quyết định | – | `SM_HoSoTrinhDuyet.drawio` | Có trạng thái kết thúc. Nhánh trả lập lại khớp sơ đồ PhuongAnBoTri |
| V8 – Ngọc Linh | UC-07.1 | Tuần tự | Ghi kết luận rà soát và yêu cầu giải trình | QĐ-03 | `SEQ_UC-07.1.drawio` | Có khung `alt` cho đủ cơ sở và cần giải trình; nhánh giải trình kết thúc bằng chuyển UC-07.2 |
| V9 – Ngô Nhật Long | UC-08.1 | Tuần tự | Ghi dự toán chi phí | QĐ-10 | `SEQ_UC-08.1.drawio` | Đúng phạm vi CN-103–CN-107. Có nhánh thiếu đơn giá. Không dùng công thức tỷ lệ vượt khi QĐ-07 chưa chốt |
| V9 – Ngô Nhật Long | UC-08.3 | Giao tiếp | Truy vấn số liệu nhiều phương án | Hình II.3-5 | `COM_UC-08.3.drawio` | Có SoSanhPhuongAn và ChiTietSoSanh |
| Trưởng nhóm (V10) | UC-09.1 | Giao tiếp | Truy vấn cung cầu theo phạm vi và quyền | – | `COM_UC-09.1.drawio` | Tác nhân vẽ bằng hình người. Thông điệp đánh số lồng nhau |
| Trưởng nhóm (V10) | UC-09.2 | Tuần tự | Ghi kết quả dự báo theo từng nhu cầu | QĐ-08 | `SEQ_UC-09.2.drawio` | Có khung `loop` theo nhu cầu. Có bước ghi DongDoiChieuCungCau |

**Quy ước file.**

- Mọi file đặt trong `drawio/II.4/` với tiền tố `SM_` (trạng thái), `COM_` (giao tiếp) hoặc `SEQ_` (tuần tự).
- Ảnh PNG phải xuất từ chính file `.drawio` đó.
- Tên lớp, tên thuộc tính và thao tác phải có trong II.3. Lớp nào cần thêm thì báo trưởng nhóm, không tự thêm.
