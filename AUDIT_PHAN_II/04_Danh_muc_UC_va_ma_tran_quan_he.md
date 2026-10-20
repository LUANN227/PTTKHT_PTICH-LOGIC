# 04. Danh mục UC và ma trận quan hệ

## 1. Danh mục 28 UC

Cột "Actor (Phần I)" ghi actor theo P1 I.1.2 và I.3 khi khác với HD-PCCN. Cột "Tình trạng": **Đặc tả** = có Description + AD; **Lấn** = đang được mô tả bên trong bài của UC khác; **Chưa** = chưa có nội dung.

| Mã | Tên | Nhóm | Actor (Phần I) | Mục tiêu (rút gọn từ HD-PCCN) | Thành viên | Tình trạng | Vấn đề chính | Mức |
|----|-----|------|----------------|-------------------------------|-----------|-----------|--------------|-----|
| 01.1 | Xây dựng và hoàn thiện nhu cầu | V2 | PM (HD-PCCN ghi PM/RM) | Lập nhu cầu đủ thông tin để xác nhận | Thùy Linh | Đặc tả | Quy tắc FTE tự tạo; thiếu %FTE, giai đoạn, bước gửi RM (CN-11); mã CN-V2/RB-V2 | C |
| 01.2 | Xác nhận nhu cầu | V2 | RM (HD-PCCN ghi PM) | RM xác nhận hoặc trả lại | Tuấn Long | Đặc tả | Nhánh trả lại ghi là E1 nhưng là luồng thay thế; mô tả Merge sai so với hình | B |
| 01.3 | Điều chỉnh nhu cầu theo phản hồi | V2 | PM | Điều chỉnh khi có phản hồi từ bước sau | Tuấn Long | Đặc tả | Trigger gồm cả RM trả lại (chồng 01.2); quan hệ extend cần chốt | C |
| 02.1 | Quản lý tiêu chí đánh giá năng lực | V3 | RM; PMO duyệt tiêu chí tạm | Duy trì tiêu chí, thang 5 mức | Lê Hoài Linh | Đặc tả | Thiếu CN-19; "số cấp chưa xác định" trái CN-18; BR trống; RM là lớp | C |
| 02.2 | Đánh giá năng lực nguồn lực | V3 | RM, Nguồn lực | Đánh giá theo tiêu chí, khoảng thiếu | — | **Chưa** | Quyết định lớp HoSoNangLuc dùng chung | — |
| 02.3 | Xác nhận và cập nhật hồ sơ năng lực | V3 | RM, PMO | Xác nhận, lưu hồ sơ tập trung | — | Chưa | | — |
| 03.1 | Xác lập tiêu chí tìm kiếm và đánh giá | V4 | RM | Điều kiện bắt buộc, tiêu chí, trọng số theo nhu cầu | — | Chưa (B-V4 coi là tiền điều kiện) | | — |
| 03.2 | Tìm kiếm ứng viên | V4 | RM | Tìm theo thứ tự nguồn | — | Chưa | | — |
| 03.3 | Đánh giá, xếp hạng và lập shortlist | V4 | RM; PMO duyệt miễn trừ | Phân loại, chấm điểm, xếp hạng, shortlist | Nguyễn Hoàng Linh | Đặc tả | Tên lớp trùng V3 (BoTieuChi), trùng V5 (KetQuaDanhGia) | B |
| 03.4 | Điều chỉnh kết quả đánh giá | V4 | RM; PMO duyệt | Điều chỉnh có lý do, có duyệt | — | Chưa | PCCN gán sai CN-45, 46 vào đây | — |
| 04.1 | Đánh giá khả năng tham gia | V5 | RM | Kết luận 4 trạng thái cho từng ứng viên | Khánh Linh | Đặc tả | Tên UC hai chỗ khác nhau; mã BR-V5; swimlane; lớp trùng tên | B |
| 04.2 | Xử lý phương án tham gia một phần | V5 | RM, PM | RM đề xuất tỷ lệ, PM xác nhận | — | Chưa (nhắc trong B-V5 A4) | | — |
| 04.3 | Xử lý vượt tải ngoại lệ | V5 | RM, PMO, CEO | Phê duyệt có điều kiện | — | Chưa (nhắc trong B-V5 A5) | Phụ thuộc PI-1, PI-2 | — |
| 05.1 | Xây dựng phương án bố trí | V6 | RM; PM nhận | Phương án chính, thay thế, chấp nhận một phần | Nguyễn Thi Thùy Linh | Đặc tả | AD có quyết định PM (thuộc 05.2); lớp LichPhanBo trùng nghĩa V5 | B |
| 05.2 | Rà soát phương án bố trí | V6 | PM xác nhận; **RM đánh dấu và chuyển** | Xác nhận, đánh dấu nghi ngờ xung đột, rẽ nhánh | — | **Chưa** | Chứa CN-70, CN-72: điểm rẽ nhánh của toàn hệ thống | — |
| 06.1 | Phân tích và đánh giá xung đột | V7 | RM, PM | Xác định Mức, phân tích ảnh hưởng | — | **Lấn** (trong B-V7) | | — |
| 06.2 | Cân đối nguồn lực | V7 | RM, PM | Đàm phán, làm mịn, san bằng | Lưu Thùy Linh | Đặc tả | Lấn 06.1, 06.3; nhánh tự thêm; mã sai; UCD trái văn bản | C |
| 06.3 | Phân xử xung đột | V7 | PMO; CEO Mức 4–5 | Ra quyết định khi bế tắc | — | **Lấn** (B-V7 A1, thiếu nhánh CEO) | | — |
| 07.1 | Rà soát và đánh giá phương án | V8 | PMO; CEO Mức 4–5; RM phụ | Xác định cấp, rà soát, kết luận đủ cơ sở hay không | Ngọc Linh | Đặc tả (sơ đồ ở Drive) | include sai; lớp sao chép dữ liệu V9/V10 | C |
| 07.2 | Yêu cầu giải trình và hoàn thiện | V8 | PMO, RM | Vòng giải trình | — | **Lấn** (B-V8 A2) | | — |
| 07.3 | Phê duyệt phương án | V8 | PMO / CEO | Ra 4 loại quyết định, Locked Baseline | — | **Chưa** | Quyết định trạng thái cuối của Phương án | — |
| 07.4 | Phê duyệt ngoại lệ | V8 | PMO / CEO | Duyệt ngoại lệ có điều kiện hoàn trả | — | Chưa | | — |
| 08.1 | Tính và cập nhật chi phí phương án | V9 | PM, Tài chính (HD-PCCN ghi Tài chính/RM) | Dự toán, dự báo chi phí | Ngô Nhật Long | Đặc tả, **phạm vi nới cả V9** | Đổi tên UC; mã CN-V9; include ngược; UCD/AD ở Drive | D (nếu chấp nhận D-a) |
| 08.2 | Đối chiếu chi phí và ngân sách | V9 | PM, Tài chính | Chênh lệch, nguyên nhân | — | Lấn (B-V9 bước 6, A2) | | — |
| 08.3 | So sánh đánh đổi giữa phương án | V9 | PM | Chất lượng → chi phí → thời gian | — | Lấn (B-V9 A3) | | — |
| 08.4 | Xác định hướng xử lý và chuyển cấp ngân sách | V9 | PM; PMO ≤10%; CEO >10% | Hướng xử lý, chuyển cấp | — | Lấn một phần (B-V9 bước 7) | Thiếu người quyết định CN-128/129 | — |
| 09.1 | Tổng hợp và phân tích cung – cầu | V10 | **RM**; PM cung cấp nhu cầu (HD-PCCN ghi PMO) | Hiện trạng cung – cầu, thiếu/dư | V10 | Chưa | Xem 09 | — |
| 09.2 | Dự báo cung – cầu | V10 | **RM**; PM | Dự báo theo khoảng thời gian, chuyển kết quả | V10 | Chưa | Xem 09 | — |

## 2. Ma trận phụ thuộc giữa UC

Ký hiệu: **→** bàn giao dữ liệu/kết quả (luồng nghiệp vụ, không phải include); **↺** quay lại; **E** quan hệ extend có căn cứ; **R** chỉ tra cứu dữ liệu dùng chung. Chỉ ghi các quan hệ có căn cứ Phần I.

| Nguồn | Đích | Kiểu | Dữ liệu / điều kiện | Căn cứ P1 | Bài đã thể hiện? |
|-------|------|------|---------------------|-----------|------------------|
| 01.1 | 01.2 | → | Nhu cầu hoàn thiện, gửi RM | CN-11 | B-V2a **chưa** có bước gửi |
| 01.2 | 01.1 / 01.3 | ↺ | Nhu cầu chưa đủ điều kiện | CN-14 | B-V2b có (gán cho 01.3) |
| 01.2 | 02.2, 03.1 | → | Nhu cầu "đã xác nhận" | CN-16, QT-05 | B-V2b có |
| 03.x | 01.3 | ↺ | Không có ứng viên đáp ứng | CN-46, CN-17 | B-V4 để ngỏ; B-V2b có |
| 09.x | 01.3 | → | Khả năng cung ứng, thiếu/dư | CN-17, CN-122 | B-V2b có; V10 chưa |
| 02.1 | 02.2 | R | Bộ tiêu chí năng lực | CN-18, QT-06 | B-V3 có |
| 02.3 | 03.x, 04.1, 05.1, 09.x | R | Hồ sơ năng lực tập trung | CN-30, PCN-02 | Các bài tham chiếu nhưng **không ai định nghĩa** |
| 03.1 | 03.2, 03.3 | → | Bộ tiêu chí, trọng số theo nhu cầu | CN-32 | B-V4 có |
| 03.2 | 03.3 | → | Danh sách ứng viên | CN-33 | B-V4 có |
| 03.3 | 03.4 | E (đề xuất) | Cần điều chỉnh kết quả | CN-43 | Chưa |
| 03.3 / 03.4 | 04.1 | → | Shortlist | CN-45 | B-V4, B-V5 có |
| 04.1 | 04.2 | E (đề xuất) hoặc → | Ứng viên chỉ đáp ứng một phần | CN-53 | B-V5: "bàn giao", không dùng extend |
| 04.1 | 04.3 | E (đề xuất) hoặc → | Vượt tải ngoại lệ | CN-56 | B-V5: "bàn giao" |
| 04.1 | 06.1 | → | Hồ sơ xung đột lịch (trùng phân bổ cứng) | CN-55, QT-26 | B-V5 có; B-V7 **không** nhận đầu vào từ V5 |
| 04.1 | 05.1 | → | Kết luận khả năng tham gia + cờ rủi ro | CN-59 | B-V5, B-V6 có |
| 04.1 | 09.x | → | Cờ rủi ro quá tải | CN-50 | V10 chưa |
| 05.1 | 05.2 | → | Phương án gửi PM | CN-68 | B-V6 có |
| 05.2 | 05.1 | ↺ | PM yêu cầu điều chỉnh | CN-69 | B-V6 A4 có |
| 05.2 | 06.1 | → | Phương án có nghi ngờ xung đột | CN-72 | **Không ai** |
| 05.2 | 07.1, 08.1 | → | Phương án không nghi ngờ xung đột | CN-72 | **Không ai**; B-V8 có trigger |
| 06.1 | 06.2 | → | Điểm xung đột Mức ≥3 | CN-74 | B-V7 (gộp) |
| 06.3 | 06.2 | E | Hết 3 ngày hoặc bế tắc | CN-83 | B-V7 vẽ extend trên UCD, văn bản lại nói "không có" |
| 06.2 | 07.1, 08.1, 09.x | → | Phương án đã cân đối, nhật ký, đề xuất thay đổi | CN-88, CN-86 | B-V7 có |
| 08.x | 07.1 | → (song song) | Chi phí, chênh lệch, đánh đổi | CN-93, CN-112, RB-61 | B-V8, B-V9 vẽ thành **include** |
| 09.x | 07.1, 05.1, 06.1 | → | Cung – cầu, dự báo, nguồn cung còn lại | CN-122 | B-V8 vẽ thành **include** |
| 07.2 | 07.1 | E | Hồ sơ chưa đủ cơ sở | CN-95 | B-V8 có (ghi nhầm "07.2 extend 07.2") |
| 07.1 | 07.3 / 07.4 | → | Hồ sơ đủ cơ sở | CN-97 | B-V8 vẽ **include 07.3** (sai hướng) |
| 07.3 | 05.1 / 06.2 | ↺ | Yêu cầu chỉnh sửa | CN-101 | Chưa |
| 07.3 / 07.4 | 09.x | → | Locked Baseline (cam kết hiện có) | CN-100 | Chưa |

## 3. Mâu thuẫn xuyên UC

Mỗi mục ghi hai phía, hậu quả, đề xuất và quyết định liên quan (tài liệu 10).

### X-01. Trạng thái của Nhu cầu nguồn lực không thống nhất
- B-V2a §3.1, AD: sau UC-01.1 trạng thái "Đã xây dựng" / "Đã xây dựng nội dung".
- B-V2b §3.2.1: sau UC-01.3 là "Chờ xác nhận"; AD 01.2 cũng ghi "Chờ xác nhận" khi PM gửi lại.
- P1 CN-03: "chưa cố định"; QT-05: "đã xác nhận". P1 I.3.9 bước 2 còn có "nhu cầu dự kiến" cho V10.
- B-V7 tiền điều kiện: "phương án ... ở trạng thái 'đã xác nhận' từ V6/V10" (dùng nhầm trạng thái nhu cầu cho phương án).
- Hậu quả: không vẽ được State Machine cho Nhu cầu; UC-01.1 kết thúc ở trạng thái mà UC-01.2 không nhận (01.2 cần nhu cầu "đã hoàn thiện, gửi RM").
- [Đề xuất] Một bộ trạng thái chung: *Đang lập (chưa cố định)* → *Chờ xác nhận* (sau CN-11) → *Đã xác nhận* | *Cần bổ sung* (CN-14) → quay lại *Chờ xác nhận*. Nhãn mức chắc chắn cho V10 là thuộc tính riêng, không phải trạng thái. → D-07.

### X-02. Một tên, nhiều nghĩa: PhanBoNguonLuc
- B-V5: PhanBoNguonLuc = bản ghi **trên lịch nguồn lực**, loại cứng/mềm, thời gian hiệu lực.
- B-V9: PhanBoNguonLuc = **dòng của phương án** (loaiNguonLuc, soLuong, mucThamGia, /chiPhi).
- B-V6: dòng phương án là ChiTietBoTri; bản ghi lịch là LichPhanBo.
- Hậu quả: khi ghép II.3 sẽ có hai lớp cùng tên khác cấu trúc; Sequence Diagram của V8 (tạo Locked Baseline → phân bổ cứng) không biết đối tượng nào được tạo.
- [Đề xuất] **ChiTietBoTri** = dòng phương án (V6, V9 dùng chung). **PhanBoNguonLuc** = bản ghi trên lịch nguồn lực tập trung, có loại cứng/mềm (V5, V6, V7, V8, V10 dùng chung). Locked Baseline biến các ChiTietBoTri thành PhanBoNguonLuc loại cứng. → D-09.

### X-03. Một tên, nhiều nghĩa: KetQuaDanhGia và BoTieuChi
- KetQuaDanhGia: B-V4 = kết quả phù hợp của ứng viên trong một phiên; B-V5 = kết luận khả năng tham gia; V3 (chưa làm) sẽ có kết quả đánh giá năng lực. B-V6 gọi kết luận V5 là KhaNangThamGia.
- BoTieuChi: B-V3 = bộ tiêu chí năng lực chung; B-V4 = bộ điều kiện + tiêu chí + trọng số **cho một nhu cầu**. HD-PCCN §3 đã nói đây là hai thứ khác nhau (UC-02.1↔UC-03.1).
- [Đề xuất] Đổi tên (mức B): KetQuaDanhGiaNangLuc (V3), KetQuaDanhGiaPhuHop (V4), KetLuanKhaNangThamGia (V5, V6 dùng lại); BoTieuChiNangLuc (V3), BoTieuChiPhuHop (V4).

### X-04. Phương án bố trí có ba tên và không ai sở hữu vòng đời
- B-V6 PhuongAnBoTri (trangThai "đang xây dựng"); B-V7 PhuongAnNguonLuc (trangThaiXungDot); B-V8 PhuongAnBoTri + HoSoTrinhDuyet; B-V9 PhuongAnBoTri "dùng lại từ V8".
- P1 cần: đang xây dựng (QT-31), PM xác nhận (CN-69), nghi ngờ xung đột (QT-30), đã cân đối (CN-88), chờ phê duyệt, yêu cầu chỉnh sửa / từ chối / phê duyệt / duyệt ngoại lệ (CN-97), Locked Baseline (CN-99), có phiên bản (CN-102).
- Hậu quả: State Machine quan trọng nhất của hệ thống (II.4.1) không có chủ; B-V7 đã vẽ máy trạng thái cho DiemXungDotNguonLuc thay vì Phương án.
- [Đề xuất] Một lớp **PhuongAnBoTri** duy nhất (V6 định nghĩa), có thuộc tính phienBan, trangThai theo danh sách trên. HoSoTrinhDuyet (V8) giữ được như một lớp riêng chỉ khi cần lưu nhiều lần trình; nếu không thì là trạng thái của PhuongAnBoTri. → D-10.

### X-05. Include dùng để mô tả luồng dữ liệu liên vùng
- B-V8 §2.2: UC-07.1 `<<include>>` UC-08 và UC-09, và `<<include>>` UC-07.3.
- B-V9 §2.2: UC-07.1 `<<include>>` UC-08.1 ("theo UCD của V8").
- P1 I.1.3.1 và RB-61: V9 **chạy song song** và cung cấp thông tin; V10 chạy liên tục. HD-MAU §2.2: "Không tự thêm include/extend chỉ để mô tả trình tự".
- Hậu quả: include nghĩa là 07.1 gọi thực hiện toàn bộ 08.1 mỗi lần rà soát – sai với nghiệp vụ song song; 07.1 include 07.3 nghĩa là mọi lần rà soát đều phê duyệt.
- [Đề xuất] Bỏ ba include (mức B/D nhẹ). Thể hiện V9, V10 là nguồn dữ liệu trong Description (tiền điều kiện, bước 4). 07.2 `<<extend>>` 07.1 thì giữ.

### X-06. Ngưỡng quá tải diễn đạt bốn kiểu
- B-V2a: FTE ≤ 1.0/nhân sự (không có căn cứ).
- B-V5: 70–85%, >85%, >90% kéo dài (đúng P1).
- B-V6: tổng >100% → nghi ngờ (đúng QT-27, CN-70, nhưng gán cho UC-05.2).
- B-V7: Mức 3 >120% hoặc Rank 1; E1 "<20% quá tải" → PM tự đàm phán (trái QT-33).
- Gốc: PI-1 (khoảng 100–120% không có mức).
- [Đề xuất] Trưởng nhóm chốt cách đọc thang 5 mức (D-04) trước khi sửa V5, V6, V7, V8.

### X-07. UC-05.2 bị bỏ trống nhưng các UC hai đầu đều giả định nó tồn tại
- B-V6 §3.4: "việc đối chiếu và đánh dấu thuộc UC-05.2 (CN-70)"; bước 10: "Việc xem xét tiếp theo thuộc UC-05.2".
- B-V7 trigger: "Hệ thống tự động phát System Alert khi ghi nhận quá tải Mức 3 từ V6/V10".
- B-V8 trigger: hồ sơ từ V6 "không có nghi ngờ xung đột".
- Hậu quả: không ai mô tả ai đánh dấu nghi ngờ, theo tiêu chí gì, và rẽ nhánh V7/V8+V9 ra sao. Đây là điểm rẽ nhánh duy nhất của luồng chính.
- [Đề xuất] Giao UC-05.2 (D-11). Lưu ý P1 I.1.3.6 bước 4–5: PM xác nhận **trước**, RM đối chiếu lịch và đánh dấu **sau**; UC-05.2 có hai actor PM và RM.

### X-08. Đầu vào V7 thiếu nguồn từ V5
- P1: V7 bắt đầu từ V6 (nghi ngờ xung đột) **hoặc** hồ sơ xung đột lịch từ V5, hoặc biến động đột xuất (I.1.3.7).
- B-V5 A3 chuyển V7; B-V7 chỉ nhận từ "V6/V10".
- [Đề xuất] B-V7 (hoặc người làm UC-06.1) bổ sung trigger từ V5. Mức C.

### X-09. RM trả lại nhu cầu: thuộc 01.2, 01.1 hay 01.3?
- B-V2b: UC-01.3 trigger gồm "PM nhận yêu cầu bổ sung/điều chỉnh từ RM"; UCD vẽ 01.3 `<<extend>>` 01.2.
- HD-PCCN §3: 01.3 "chỉ điều chỉnh khi có phản hồi hoặc kết quả từ các bước sau".
- P1 CN-14 (RM chuyển lại) thuộc bước xác nhận; CN-17 (V4, V10) là phản hồi bước sau.
- Hậu quả: nếu 01.3 extend 01.2 thì phản hồi từ V4/V10 (xảy ra sau khi đã xác nhận, ngoài 01.2) không có điểm mở rộng hợp lệ.
- → D-06.

### X-10. Ứng viên, Nguồn lực, Hồ sơ năng lực, Kỹ năng
- B-V4: UngVien (có nguonUngVien gồm tuyển ngoài) — KyNang gắn với UngVien.
- B-V5, B-V6: NguonLuc; B-V6 NguonLuc 1–1 HoSoNangLuc (thuộc tính kyNang dạng chuỗi).
- B-V2a: KyNangChuyenMon chứa capDoYeuCau, coBatBuoc (là thuộc tính của **yêu cầu**, không phải của kỹ năng).
- B-V3: KyNang (maKyNang, tenKyNang) gắn với tiêu chí.
- [Đề xuất] Danh mục **KyNang** dùng chung (V3). **YeuCauKyNang** (lớp liên kết NhuCau–KyNang: mức yêu cầu, bắt buộc) cho V2. **NangLucKyNang** (lớp liên kết HoSoNangLuc–KyNang: mức thành thạo, trạng thái xác nhận, ngày đánh giá) cho V3, V4 dùng lại. UngVien có là lớp riêng hay không → D-12.

### X-11. "Yêu cầu nguồn lực" (V5) và "Nhu cầu nguồn lực" (V2)
- B-V5 lớp YeuCauNguonLuc (khungThoiGian, vaiTroYeuCau). P1 CN-127: PM gửi yêu cầu nguồn lực kèm khung thời gian cho V5.
- B-V4, B-V6 dùng NhuCauNguonLuc đã xác nhận làm đầu vào; B-V6 thêm ViTriCanBoTri là thành phần của nhu cầu.
- [Giả định] Có thể "yêu cầu" chính là nhu cầu đã xác nhận (hoặc một dòng/vị trí của nó). P1 không nói rõ. → D-13.

### X-12. Mã yêu cầu ngoài baseline
- B-V2a (CN-V2-01, RB-V2-03), B-V3 (QT-01..04, Q-04), B-V5 (BR-V5-01..14, CN-V5-xx, C-V5-01), B-V7 (CN-01..14, QT-01..08, RB-01..05, PCN-04), B-V9 (CN-V9-xx, RB-V9-xx, PCN-V9-xx, Q-02, Q-03).
- Đặc biệt nguy hiểm: B-V7 dùng "CN-01..CN-14" và "QT-01..QT-08" là **mã có thật trong P1 nhưng thuộc V2** (CN-01 = PM tra cứu bối cảnh dự án; QT-01 = nhu cầu gắn công việc). Người đọc sẽ truy vết nhầm.
- [Đề xuất] Đổi mã theo bảng ánh xạ trong 05 mục 3 (mức B, ưu tiên P1).

### X-13. Lớp kỹ thuật, actor trong mô hình lớp miền
- RM là lớp (B-V3); NguoiDung (B-V4, B-V9); ConflictController, CPMAnalysisService, auditTrailHash, xuatFileBanGiaoV8V9V10() (B-V7); MaTranPhanQuyenDoA, NguongPheDuyetNganSach (B-V8, B-V9) là cấu hình quy tắc.
- [Đề xuất] Chốt quy ước (D-14): actor không thành lớp; "người thực hiện" (PCN-07) là thuộc tính hoặc liên kết tới một lớp NhanSu/NguoiDung duy nhất; lớp cấu hình ngưỡng chỉ giữ nếu nhóm muốn thể hiện DoA trong II.3.

### X-14. Dữ liệu V9, V10 bị sao chép thành lớp riêng trong V8
- B-V8: ThongTinChiPhi (NganSachDuToan, ChenhLechNganSach...) và ThongTinDuBao (TongCung, TongCau...).
- B-V9 đã có DanhGiaChiPhi; V10 sẽ có kết quả dự báo.
- [Đề xuất] V8 liên kết tới DanhGiaChiPhi (V9) và KetQuaDuBao (V10), bỏ hai lớp sao chép. Mức B–C.
