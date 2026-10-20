# 06. Audit theo thành viên

Mỗi phần gồm: nhận xét chung, nội dung giữ nguyên, bảng lỗi. Loại lỗi: **NV** nghiệp vụ, **MH** mô hình hóa, **UML** ký pháp, **CC** câu chữ, **LT** nhất quán liên tài liệu, **CC-cứ** thiếu căn cứ. Mức A–E và ưu tiên P1–P3 theo README. Những mục phụ thuộc quyết định ghi mã D-xx (tài liệu 10); **không giao sửa mục đó trước khi trưởng nhóm quyết định**.

---

## 1. B-V2a — Thùy Linh — UC-01.1 Xây dựng và hoàn thiện nhu cầu

**Nhận xét chung:** Đủ 12 mục, luồng chính bám P1 I.1.3.2 bước 1–4. Điểm yếu: tự thêm quy tắc FTE, thiếu ba yêu cầu Cao/Trung bình (CN-03, CN-08, CN-11), lẫn chi tiết giao diện, AD có nhánh treo. Mức tổng: **C**.

**Giữ nguyên:** luồng bước 3, 5, 6 (chọn phạm vi, loại nguồn lực, quy mô); quyết định "không dùng include/extend" (§2.2); các lớp DuAn, CongViec, NhuCauNguonLuc và quan hệ DuAn◆–CongViec.

| # | Vị trí | Vấn đề | Loại | Căn cứ | Đề xuất sửa | Mức | Ưu tiên | Ảnh hưởng |
|---|--------|--------|------|--------|-------------|-----|---------|-----------|
| 1 | §3.3 A2, §3.4 RB-V2-03, AD decision "FTE ≤ 1.0/nhân sự" | Quy tắc không có trong P1. FTE của nhu cầu là quy mô (có thể 2,5 FTE cho một loại nguồn lực), không phải tải của một người | NV, CC-cứ | P1 QT-02, CN-06 | Bỏ A2 và decision FTE. Nếu muốn kiểm tra, chỉ kiểm tra %FTE trong khoảng 0–100% (PCN-09) | C | P1 | AD, class (tinhToanFTE) |
| 2 | §3.2 | Thiếu nhánh "thông tin chưa đủ → yêu cầu bổ sung, nhu cầu chưa cố định" | NV | CN-03, P1 I.1.3.2 điểm quyết định 1 | Thêm A: tại bước 4, thông tin chưa đủ → ghi nội dung cần bổ sung, nhu cầu giữ trạng thái chưa cố định | C | P2 | AD |
| 3 | §3.2 bước 6–7 | Thiếu thời điểm/giai đoạn và %FTE (mức tham gia) | NV | CN-07, CN-08, QT-03 | Thêm bước xác định giai đoạn và mức tham gia | C | P2 | Class: thêm thuộc tính, xem #7 |
| 4 | §3.2 bước 8, hậu điều kiện | Kết thúc ở "Đã xây dựng" và không gửi RM; UC-01.2 không có đầu vào | NV, LT | CN-11; X-01 | Thêm bước "PM chuyển nhu cầu hoàn thiện cho RM"; trạng thái sau = theo D-07 | C | P1 | B-V2b, state machine Nhu cầu |
| 5 | §2.1, UCD | Actor "PM/RM" gộp một hình nhân | NV, UML | P1 I.1.3.2: PM lập, RM xác nhận | Actor chính PM; RM không tham gia UC-01.1 | B | P2 | II.1 |
| 6 | §3.3 E1, AD "Đăng nhập", "Nhấn…", "Lỗi kết nối CSDL" | Thao tác giao diện, lỗi kỹ thuật | MH | HD-MAU §3.2 "không biến thành hướng dẫn thao tác giao diện" | Bỏ E1; đổi tên action theo nghiệp vụ | B | P3 | |
| 7 | §8, class | NhuCauNguonLuc thiếu giai đoạn, mức tham gia; KyNangChuyenMon chứa capDoYeuCau, coBatBuoc (thuộc tính của yêu cầu, không của kỹ năng) | MH | CN-05..08; X-10 | Tách lớp liên kết YeuCauKyNang (mucYeuCau, batBuoc); thêm thuộc tính mucThamGia, liên kết GiaiDoan (theo D-15) | C | P2 | II.3 |
| 8 | AD | Hai action "Điều chỉnh lại mốc thời gian", "Tính toán lại tỷ lệ FTE" không có luồng ra (nhánh treo) | UML | | Nối về hành động nhập tương ứng | B | P2 | |
| 9 | §3.4 | Mã CN-V2-01, RB-V2-03; CN-01 mô tả sai nội dung | LT | 05 §3 | Đổi mã theo bảng 05 | B | P1 | Ma trận truy vết |
| 10 | §5 | Bảng đối chiếu tick ✓ hết dù AD có nhánh treo | CC | | Đối chiếu lại sau khi sửa | B | P3 | |

---

## 2. B-V2b — Tuấn Long — UC-01.2 Xác nhận nhu cầu, UC-01.3 Điều chỉnh nhu cầu theo phản hồi

**Nhận xét chung:** UC-01.2 đúng nghiệp vụ, đúng actor (RM, khác HD-PCCN nhưng đúng P1), BR đúng mã P1. AD 01.2 vẽ vòng lặp đúng. Phần lớp mới làm tới §6. UC-01.3 mỏng. Mức tổng: **B** cho 01.2, **C** cho 01.3.

**Giữ nguyên:** Description 01.2; AD 01.2 (hình); bảng BR 01.2; phân tích danh từ §6.1 (lập luận tốt về việc không tách lớp khi chưa có căn cứ).

| # | Vị trí | Vấn đề | Loại | Căn cứ | Đề xuất sửa | Mức | Ưu tiên | Ảnh hưởng |
|---|--------|--------|------|--------|-------------|-----|---------|-----------|
| 1 | §7–§12 | Chưa làm (còn "...") | MH | HD-MAU | Hoàn thiện; dùng lớp NhuCauNguonLuc chung (do B-V2a định nghĩa), thêm PhanHoiNhuCau nếu D-06 giữ | C | P2 | II.3 |
| 2 | §2.2 | "UC-01.3 extend UC-01.3" (tự trỏ) | CC | Hình UCD vẽ đúng 01.3→01.2 | Sửa đích thành UC-01.2 | B | P1 | |
| 3 | §3.1.3 | Nhánh "nhu cầu không đủ điều kiện" ghi E1, nhưng là luồng nghiệp vụ bình thường; §3.1.4 lại gọi là "A1" | CC | HD-MAU §3.3 | Đổi thành A1 | B | P3 | |
| 4 | §4.1 dòng Merge | Mô tả nói hai nhánh hội tụ trước "Đã xác nhận" – sai so với hình (hình đúng: quay lại trước "Xem xét") | CC | Hình AD 01.2 | Sửa câu mô tả theo hình | B | P3 | |
| 5 | UC-01.3 trigger, UCD extend | Gồm cả "PM nhận yêu cầu bổ sung từ RM", chồng với 01.2; nếu 01.3 extend 01.2 thì phản hồi từ V4/V10 (sau khi đã xác nhận) không có điểm mở rộng hợp lệ | MH, LT | HD-PCCN §3; X-09 | **Chờ D-06** | C/D | P1 | B-V2a |
| 6 | UC-01.3 luồng chính bước 3–4 | "Xem xét phản hồi", "Điều chỉnh nguồn lực" quá chung; không phân biệt nguồn phản hồi (V4: không có ứng viên; V10: thiếu/dư) | NV | CN-17 | Ghi rõ PM xem từng loại phản hồi và điều chỉnh loại/quy mô/thời gian/mức tham gia; thêm A "PM giữ nguyên nhu cầu" (không phải phản hồi nào cũng dẫn tới điều chỉnh) | C | P2 | |
| 7 | UC-01.3 E2 | "Thông tin điều chỉnh chưa hợp lệ" không nêu tiêu chí | CC-cứ | | Nêu kiểm tra theo QT-02, QT-03 | B | P3 | |
| 8 | Trạng thái "Chờ xác nhận" | Chưa thống nhất với B-V2a | LT | X-01 | Theo D-07 | B | P1 | |
| 9 | §4.2 AD 01.3, mô tả Merge | Thành viên đã tự ghi "cần xem xét lại" về Merge | UML | | Nối nhánh "Không" thẳng về "Điều chỉnh nhu cầu", bỏ decision rỗng | B | P3 | |

---

## 3. B-V3 — Lê Hoài Linh — UC-02.1 Quản lý tiêu chí đánh giá năng lực

**Nhận xét chung:** Bài gọn, AD sạch, nhánh A1 (ngừng áp dụng thay vì xóa) và hậu điều kiện "không làm thay đổi đánh giá cũ" là ý tốt. Hai vấn đề lớn: UC đang trượt về dạng "thêm/sửa/ngừng danh mục" (OUTLINE cảnh báo UC quá đơn giản), và bỏ mất nhánh nghiệp vụ thật duy nhất của UC (CN-19). UC trọng tâm đề xuất cho V3 là UC-02.2 (HD-PCCN §5), chưa ai làm. Mức tổng: **C**, có thể **D** tùy D-05.

**Giữ nguyên:** AD (cấu trúc và nhánh); A1 ngừng áp dụng; E2; lớp TieuChiDanhGia, NhatKyThayDoi.

| # | Vị trí | Vấn đề | Loại | Căn cứ | Đề xuất sửa | Mức | Ưu tiên | Ảnh hưởng |
|---|--------|--------|------|--------|-------------|-----|---------|-----------|
| 1 | Toàn UC | Thiếu tiêu chí tạm cho kỹ năng chưa có tiêu chí, ở trạng thái chờ PMO/Quản lý danh mục duyệt, chỉ dùng sau khi duyệt | NV | CN-19, P1 I.1.4 ghi chú cuối, I.3.2 bước 5 | Thêm luồng: RM đề xuất tiêu chí tạm → trạng thái chờ duyệt → PMO duyệt/từ chối; thêm actor phụ PMO | C | P1 | UCD, AD, class (trạng thái tiêu chí) |
| 2 | §7 MucDo "số cấp chưa xác định (Q-04)" | Trái P1: thang 5 mức đã cố định | NV, LT | CN-18, QT-07, PCN-09 | MucDo cố định 5 mức (1 mới bắt đầu … 5 chuyên gia); có thể là kiểu liệt kê thay vì lớp | B | P2 | II.3 |
| 3 | §3.4 | Bảng BR còn trống mẫu | CC-cứ | | Điền CN-18, CN-19, QT-06, QT-07, PCN-07 | B | P1 | Truy vết |
| 4 | §7 nguồn "QT-01..04", "mục 04" | Mã sai (QT-01 thuộc V2) | LT | 05 §3 | Đổi theo bảng 05 | B | P1 | |
| 5 | §6, §7 | RM là lớp miền | MH | X-13 | Bỏ lớp RM; người thực hiện là thuộc tính của NhatKyThayDoi (theo D-14) | B | P2 | |
| 6 | §3.3 E1, E3 | Kiểm tra quyền và lỗi lưu là cơ chế chung, không phải nghiệp vụ | MH | HD-MAU §3.3 | Bỏ hoặc gộp thành một ghi chú chung | B | P3 | |
| 7 | Chọn UC | UC-02.1 khác đề xuất UC-02.2; UC-02.2 (năng lực, khoảng thiếu, hồ sơ dùng chung) chưa ai làm | MH | HD-PCCN §5; OUTLINE | **Chờ D-05** | D | P1 | Lớp HoSoNangLuc cho V4, V5, V6, V10 |

---

## 4. B-V4 — Nguyễn Hoàng Linh — UC-03.3 Đánh giá, xếp hạng và lập shortlist

**Nhận xét chung:** Bài tốt nhất về mức bám P1: đủ CN-34..42, QT-12..20 đúng mã, nhánh A1–A5, E1–E3 có căn cứ, ghi rõ vùng ngoài phạm vi (QT-20), tự đánh dấu điểm cần nhóm chốt (CN-46). AD và class rõ. Nên dùng làm **bài mẫu** cho nhóm. Mức tổng: **A/B**.

**Giữ nguyên:** toàn bộ Description; AD; cấu trúc lớp PhienDanhGia–KetQuaDanhGia–DiemTieuChi–Shortlist–DeNghiMienTru.

| # | Vị trí | Vấn đề | Loại | Căn cứ | Đề xuất sửa | Mức | Ưu tiên | Ảnh hưởng |
|---|--------|--------|------|--------|-------------|-----|---------|-----------|
| 1 | §7 BoTieuChi, KetQuaDanhGia | Trùng tên với lớp khác nghĩa ở V3, V5 | LT | X-03 | Đổi thành BoTieuChiPhuHop, KetQuaDanhGiaPhuHop | B | P2 | II.3 |
| 2 | §7 UngVien–KyNang | KyNang gắn trực tiếp UngVien, trong khi P1 nói năng lực lấy từ hồ sơ năng lực tập trung V3 | MH, LT | PCN-02; X-10 | Tham chiếu NangLucKyNang của HoSoNangLuc; quan hệ UngVien–NguonLuc theo D-12 | C | P2 | II.3 |
| 3 | §7 NguoiDung | Lớp người dùng trong miền | MH | X-13 | Theo D-14 | B | P3 | |
| 4 | §3.4 CN-42 "(chỉ xem; xem mục 1)" | Ghi chú tham chiếu không rõ | CC | | Bỏ "xem mục 1" | B | P3 | |
| 5 | Hậu điều kiện "phản hồi V2 cần nhóm chốt" | Đúng là điểm mở | LT | CN-46 | **Chờ D-16** | — | | |
| 6 | AD decision "Cần miễn trừ ứng viên?" | Xử lý như một quyết định chung, trong khi phân loại là theo từng ứng viên | UML | | Ghi chú "lặp cho từng ứng viên Không đạt" hoặc dùng expansion region; mức nhỏ | B | P3 | |

---

## 5. B-V5 — Khánh Linh — UC-04.1 Đánh giá khả năng tham gia

**Nhận xét chung:** Luồng chính và các nhánh A1–A4 bám sát P1 I.1.3.5; phân biệt đúng V5 không quyết định ưu tiên. Lớp miền có chú thích loại trừ UI/API/Repository – tốt. Vấn đề chủ yếu là mã, tên UC, swimlane và tên lớp. Mức tổng: **B**.

**Giữ nguyên:** luồng chính §3.2; A1–A4; danh sách lớp NguonLuc, LichNguonLuc, PhanBoNguonLuc, DeXuatThamGiaMotPhan, HoSoVuotTaiNgoaiLe.

| # | Vị trí | Vấn đề | Loại | Căn cứ | Đề xuất sửa | Mức | Ưu tiên | Ảnh hưởng |
|---|--------|--------|------|--------|-------------|-----|---------|-----------|
| 1 | §1 "Đánh giá năng lực khả dụng của nguồn lực" vs §2.1 "Đánh giá khả năng tham gia" | Tên UC không nhất quán | CC | HD-PCCN | Dùng "Đánh giá khả năng tham gia" | B | P1 | |
| 2 | §3.4, §7 | Mã BR-V5-xx, CN-V5-xx, C-V5-01 | LT | 05 §3 | Đổi mã | B | P1 | |
| 3 | §3.3 A6 "không tự chốt 24 hoặc 48 giờ" | P1 đã ghi "dưới 24–48 giờ" | NV | CN-58, I.1.3.5 | Ghi đúng "dưới 24–48 giờ" theo P1; nếu muốn một con số → D-17 | B | P2 | |
| 4 | AD | Hai làn RM/Hệ thống nhưng hầu hết hành động của RM (bước 6 "RM ghi nhận kết luận", A2…) nằm trong làn Hệ thống | UML | | Chuyển hành động về đúng làn | B | P2 | |
| 5 | AD | Các nhánh A3, A4, A5, "Chờ xác nhận" kết thúc bằng hộp chữ, không có nút kết thúc; không thể hiện việc lặp cho từng ứng viên trong shortlist | UML | | Thêm flow final/activity final; ghi chú lặp theo ứng viên | B | P2 | |
| 6 | §2.1, actor phụ PMO/CEO | Actor của UC-04.3 đưa vào UC-04.1 | MH | | Actor phụ 04.1 chỉ có PM nếu 04.2 tách; PMO/CEO thuộc 04.3 | B | P3 | II.1 |
| 7 | §7 KetQuaDanhGia | Trùng tên với V4 | LT | X-03 | Đổi thành KetLuanKhaNangThamGia (B-V6 đang gọi KhaNangThamGia) | B | P2 | II.3 |
| 8 | §10 vs hình | Văn bản: LichNguonLuc–PhanBoNguonLuc; hình: NguonLuc–PhanBoNguonLuc | MH | | Thống nhất một cách; đề xuất PhanBoNguonLuc gắn NguonLuc và DuAn, LichNguonLuc là tập hợp theo kỳ (theo D-09) | B | P2 | |
| 9 | §7 YeuCauNguonLuc | Có thể trùng NhuCauNguonLuc | LT | X-11 | **Chờ D-13** | — | | |
| 10 | §2.3, §4.2 | Còn sót chữ hướng dẫn của mẫu; §11 dính tiêu đề §12 | CC | | Xóa chữ mẫu, tách mục | B | P3 | |

---

## 6. B-V6 — Nguyễn Thi Thùy Linh — UC-05.1 Xây dựng phương án bố trí

**Nhận xét chung:** Bài tốt, bám P1 I.1.3.6 bước 1–3 và các trường hợp đặc biệt, mã CN/QT đúng baseline, ranh giới với 05.2 và 06.1 được ghi rõ. Lớp PhuongAnBoTri–ChiTietBoTri–ViTriCanBoTri–RuiRoViTri là xương sống tốt cho II.3. Mức tổng: **B**.

**Giữ nguyên:** Description §3; nhánh A1–A3, E1; lớp PhuongAnBoTri, ChiTietBoTri, RuiRoViTri, GiaiDoanDuAn.

| # | Vị trí | Vấn đề | Loại | Căn cứ | Đề xuất sửa | Mức | Ưu tiên | Ảnh hưởng |
|---|--------|--------|------|--------|-------------|-----|---------|-----------|
| 1 | AD cuối | Có quyết định "PM phê duyệt?" – là nội dung UC-05.2; dùng chữ "phê duyệt" cho PM (P1: PM "xác nhận") | MH, CC | CN-69; HD-PCCN §3 | Kết thúc AD tại "Gửi phương án cho PM"; nhánh A4 thể hiện bằng điểm bắt đầu thứ hai hoặc ghi chú | B | P2 | Ranh giới 05.2 |
| 2 | AD "Nhận phản hồi chỉnh sửa (Quay lại cập nhật)" rồi kết thúc | Nhãn nói quay lại nhưng luồng đi tới kết thúc | UML | | Theo #1 | B | P2 | |
| 3 | §7 LichPhanBo, KhaNangThamGia | Trùng nghĩa với PhanBoNguonLuc, KetQuaDanhGia của V5 | LT | X-02, X-03 | Dùng tên chung theo D-09 | B | P2 | II.3 |
| 4 | §7 NhuCauNguonLuc◆ViTriCanBoTri | Cấu trúc nhu cầu theo vị trí chưa khớp với B-V2a (nhu cầu có soLuong, chiSoFTE, kỹ năng) | LT | X-11 | **Chờ D-15** | — | | V2, V4, V5 |
| 5 | §11 NguonLuc–HoSoNangLuc 1–1 với thuộc tính dạng chuỗi | Hồ sơ năng lực cần chi tiết theo kỹ năng | MH | CN-23, CN-24 | Tham chiếu lớp HoSoNangLuc chung (D-05) | B | P3 | |
| 6 | §3.4 QT-31 bước 6 | Hạn 3 ngày gắn với 05.1 là hợp lý (PCCN gán CN-73 cho 05.2) | LT | | Giữ; cập nhật PCCN | A | | HD-PCCN |
| 7 | Thiếu thứ tự P1 | P1: PM xác nhận trước, RM đánh dấu nghi ngờ sau; B-V6 đúng nhưng không ai làm phần sau | LT | X-07 | Không phải lỗi của B-V6; xem D-11 | — | | |

---

## 7. B-V7 — Lưu Thùy Linh — UC-06.2 Cân đối nguồn lực

**Nhận xét chung:** Bài đầu tư nhiều, hiểu kỹ thuật làm mịn/san bằng, lớp DiemXungDot–BienBanDamPhan–HoSoLeoThang–QuyetDinhPhanXu–ChangeRequest có giá trị. Nhưng: (1) phạm vi gồm cả 06.1 và 06.3; (2) có nhánh tự thêm và một nhánh trái P1; (3) mã yêu cầu dùng nhầm mã V2; (4) UCD trái với văn bản; (5) làm sang II.4 và trộn lớp kỹ thuật. Đây là bài **cần sửa nhiều nhất**, nhưng không cần làm lại từ đầu. Mức tổng: **C**.

**Giữ nguyên:** luồng chính bước 3–8 (đàm phán, làm mịn, san bằng) sau khi đổi mã; A2 bế tắc hoàn toàn (bỏ câu "họp khẩn"); bảng bàn giao V8/V9/V10 (§III.2); các lớp miền (trừ phần kỹ thuật); nội dung II.4 giữ làm **bản nháp** cho giai đoạn sau.

| # | Vị trí | Vấn đề | Loại | Căn cứ | Đề xuất sửa | Mức | Ưu tiên | Ảnh hưởng |
|---|--------|--------|------|--------|-------------|-----|---------|-----------|
| 1 | §3.4, §III.1 | CN-01..14, QT-01..08, RB-01..05 là mã V2 trong P1 | LT | X-12; 05 §3 | Đổi mã toàn bộ theo bảng 05 | B | P1 | Truy vết |
| 2 | §3.3 E1 | Dưới Mức 3: "chuyển PM tự đàm phán" – trái QT-33 ("chỉ ghi nhận để theo dõi"); "<20% quá tải" là diễn giải riêng | NV | QT-33, PI-1 | Ghi "dưới Mức 3: ghi nhận theo dõi, kết thúc"; ngưỡng theo D-04 | C | P1 | AD |
| 3 | §3.3 A3, A4 | Overtime/thuê ngoài do PMO + Tài chính duyệt; chia 50-50, job-sharing – không có trong P1 | NV, CC-cứ | P1 I.1.3.7 | Bỏ A3, A4 (hoặc đưa lên D-18 nếu nhóm muốn giữ) | C | P1 | AD, class |
| 4 | Bước 1–2, A1 | Gồm 06.1 (xác định Mức, phân tích CPM) và 06.3 (PMO phân xử) | MH | HD-PCCN §3 | Bước 1–2 thành tiền điều kiện "đã có điểm xung đột Mức ≥3 từ UC-06.1"; A1 rút gọn thành "chuyển UC-06.3" (extend) | D (nhẹ) | P1 | UCD |
| 5 | UCD | Hình có `<<include>>` 06.1 và `<<extend>>` 06.3 + actor CEO, trong khi §2.2 ghi "không có include/extend" và không có CEO | UML, LT | | Thống nhất: bỏ include 06.1 (là tuần tự), giữ extend 06.3 nếu theo #4; CEO thuộc 06.3 | B | P1 | |
| 6 | Tiền điều kiện, trigger | "phương án ... 'đã xác nhận' từ V6/V10", "System Alert … từ V6/V10" | NV, LT | P1 I.1.3.7: từ V6, **V5**, biến động đột xuất | Sửa nguồn vào: V6 (nghi ngờ xung đột), V5 (xung đột lịch); V10 chỉ cung cấp thông tin thiếu/dư (CN-75) | C | P1 | X-08 |
| 7 | Thiếu | Nhánh CEO Mức 4–5 (CN-85) và CCB (CN-86) | NV | | Thuộc 06.3; trong 06.2 chỉ ghi chuyển | C | P2 | |
| 8 | Bước 3 actor "RM" nhưng nội dung là các PM đàm phán | | CC | CN-78, CN-79 | Actor PM (đàm phán), RM (điều phối, ghi nhận) | B | P2 | |
| 9 | AD | Rối luồng: decision "Thành công trong 3 ngày?" hai nhánh chéo; Leveling và Deadlock nối sai vào các action tạo Change Request | UML | | Vẽ lại phần giữa AD sau khi sửa #2–#4 | C | P2 | |
| 10 | §12, II.4 | Lớp kỹ thuật (ConflictController, CPMAnalysisService), thuộc tính auditTrailHash, thao tác xuatFile…() | MH | X-13 | Bỏ khỏi lớp miền; giữ cho III (thiết kế) | B | P2 | |
| 11 | §7 PhuongAnNguonLuc | Tên khác PhuongAnBoTri của V6/V8/V9 | LT | X-04 | Dùng PhuongAnBoTri | B | P2 | |
| 12 | Thuật ngữ | "Rank 1", "Deadlock Protocol", "phán quyết cưỡng chế", "Change Request", "Conflict Log" | CC | P1 dùng "Hạng ưu tiên 1", "bế tắc hoàn toàn", "quyết định phân xử", "đề xuất thay đổi", "nhật ký xử lý xung đột" | Dùng thuật ngữ P1 | B | P3 | |
| 13 | II.4 State Machine | Vẽ cho DiemXungDotNguonLuc; vẫn hữu ích nhưng chưa được giao, và tên trạng thái phụ thuộc #2–#4 | MH | | Giữ làm nháp; chỉ hoàn thiện sau khi chốt II.3 (D-19) | — | P3 | |

---

## 8. B-V8 — Ngọc Linh — UC-07.1 Rà soát và đánh giá phương án

**Nhận xét chung:** Luồng chính và A1 (chuyển cấp CEO trong 1 ngày) đúng P1, mã CN đúng baseline. Sơ đồ UCD, AD, class chỉ có trên Drive nên chưa kiểm tra được. Vấn đề: dùng include sai, A2 chứa toàn bộ UC-07.2, lớp sao chép dữ liệu V9/V10. Mức tổng: **C**.

**Giữ nguyên:** luồng chính bước 1–6; A1; bảng BR CN-89..94; lớp HoSoTrinhDuyet (nếu D-10 giữ), YeuCauGiaiTrinh.

| # | Vị trí | Vấn đề | Loại | Căn cứ | Đề xuất sửa | Mức | Ưu tiên | Ảnh hưởng |
|---|--------|--------|------|--------|-------------|-----|---------|-----------|
| 1 | Toàn bài | UCD, AD, class không nằm trong file nộp | MH | HD-MAU | Xuất hình và chèn vào file | B | P1 | Không audit được |
| 2 | §2.2 | include UC-08, UC-09 (V9 chạy song song, V10 liên tục); include UC-07.3 (sai hướng); "UC-07.2 extend UC-07.2" | UML, NV | X-05 | Bỏ ba include; sửa thành "UC-07.2 extend UC-07.1" | B/D | P1 | B-V9 |
| 3 | §3.3 A2 | Mô tả trọn vòng giải trình (thuộc 07.2) | MH | HD-PCCN §3 | A2 dừng ở "chuyển UC-07.2"; nội dung còn lại để UC-07.2 | C | P2 | |
| 4 | §3.2 bước 3 "CEO đối với Mức 4–5" | Đúng; nhưng actor chính ghi cả PMO và CEO, cần thể hiện CEO chỉ tham gia sau chuyển cấp | CC | | Actor chính PMO; CEO là actor phụ (kích hoạt qua A1) | B | P3 | II.1 |
| 5 | §7 ThongTinChiPhi, ThongTinDuBao | Sao chép dữ liệu của V9, V10 thành lớp riêng | MH, LT | X-14 | Liên kết tới DanhGiaChiPhi (V9), KetQuaDuBao (V10) | C | P2 | II.3 |
| 6 | §7 MaTranPhanQuyenDoA | Lớp cấu hình | MH | X-13 | Theo D-14 | B | P3 | |
| 7 | §8 PhuongAnBoTri thuộc tính DanhSachPhanBo, DanhSachXungDot | Thuộc tính dạng danh sách thay cho liên kết | MH | | Thay bằng liên kết tới ChiTietBoTri, DiemXungDot | B | P2 | |
| 8 | §9 tên lớp ThongTinChiPhiV9 / ThongTinChiPhi không thống nhất | | CC | | Thống nhất tên | B | P3 | |
| 9 | §5 "Bao phủ 100% CN-89 đến CN-94" | Đúng, nhưng bảng đối chiếu không theo mẫu 7 dòng | CC | HD-MAU §5 | Dùng đủ 7 dòng kiểm tra | B | P3 | |

---

## 9. B-V9 — Ngô Nhật Long — UC-08.1 (đã đổi tên thành cả nhóm V9)

**Nhận xét chung:** Nội dung nghiệp vụ tốt, bám đúng P1 I.1.3.9 (actor PM + Tài chính, thứ tự so sánh, ngưỡng 10%, không tạo Locked Baseline). Mô hình lớp chi tiết nhất nhóm, có lập luận lưu giá trị chốt tại thời điểm đánh giá. Vấn đề: đổi phạm vi UC, mã ngoài baseline, include ngược, UCD/AD ở Drive, ký pháp class. Mức tổng: **B**, hoặc **D** nếu không chấp nhận D-a.

**Giữ nguyên:** Description; A1–A3; E1; bảng lớp §7–§11 (trừ đổi tên PhanBoNguonLuc).

| # | Vị trí | Vấn đề | Loại | Căn cứ | Đề xuất sửa | Mức | Ưu tiên | Ảnh hưởng |
|---|--------|--------|------|--------|-------------|-----|---------|-----------|
| 1 | §1, §2.1 tên UC | UC-08.1 được đổi tên và mở rộng gồm 08.2, 08.3, một phần 08.4 | MH | HD-PCCN §1 | **Chờ D-03 (phương án D-a)**. Nếu chấp nhận: giữ, chỉ ghi chú "gộp 08.1–08.3". Nếu không: tách lại | D | P1 | 03 |
| 2 | §3.4, khắp bài | Mã CN-V9-xx, RB-V9-xx, PCN-V9-xx, Q-02, Q-03 | LT | 05 §3 | Đổi mã | B | P1 | |
| 3 | §2.2 | include từ UC-07.1 | UML, NV | X-05 | Bỏ | B | P1 | B-V8 |
| 4 | §2.3, §4 | UCD và AD chỉ có link Drive | MH | | Chèn hình | B | P1 | |
| 5 | §7 PhanBoNguonLuc | Là dòng phương án, trùng tên với bản ghi lịch V5 | LT | X-02 | Dùng ChiTietBoTri (V6) | B | P2 | II.3 |
| 6 | Hình class | Thao tác và thuộc tính chung một ngăn ("maSoSanh; thoiDiem; soSanh()"), hình rất khó đọc | UML | | Tách 3 ngăn; xuất hình lớn hơn | B | P2 | |
| 7 | Bước 7, A2 | Có "cấp xử lý" nhưng không có actor quyết định (PMO ≤10%, CEO >10%) | NV | CN-128, CN-129 | Nếu 08.4 tách riêng: A2 chuyển 08.4. Nếu không: thêm nhánh | C | P2 | |
| 8 | §8 PhanBoNguonLuc "mucThamGia giả định % (Q-03)" | P1 đã chốt %FTE | LT | PCN-09 | Bỏ ghi chú giả định | B | P3 | |
| 9 | §8 NganSach "/conLai = duyệt trừ phát sinh", A2 công thức tỷ lệ vượt | Công thức là giả định, P1 không định nghĩa | CC-cứ | QT-51 | Ghi rõ "[giả định]" hoặc đưa D-20 | B | P3 | |
| 10 | §7 NguoiDung, NguongPheDuyetNganSach | Lớp người dùng, lớp cấu hình | MH | X-13 | Theo D-14 | B | P3 | |
| 11 | Định dạng | Toàn văn bản bị tô màu nền (`mark`) | CC | | Bỏ tô | B | P3 | |
