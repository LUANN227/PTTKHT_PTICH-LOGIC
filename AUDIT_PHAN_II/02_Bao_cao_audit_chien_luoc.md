# 02. Báo cáo audit chiến lược

## 1. Kết luận chính

1. **Phần I đủ tốt để làm baseline.** Phần I có cấu trúc chặt: 9 vùng V2–V10, 129 CN, 57 QT ánh xạ 1–1 sang RB-02..RB-58, mỗi vùng có I.1 (nghiệp vụ), I.2 (yêu cầu), I.3 (hệ thống hỗ trợ). Không cần viết lại Phần I. Có một số lỗi cục bộ cần ghi nhận (mục 2.4), trong đó **thang cảnh báo 5 mức** là lỗi duy nhất ảnh hưởng nhiều UC.
2. **Cấu trúc 9 nhóm chức năng (UC-01..UC-09) bám đúng 9 vùng của Phần I.** Đây là xương sống truy vết: CN, QT, RB, I.3 đều chia theo V. Không có bằng chứng nghiệp vụ buộc phải đổi ranh giới phân hệ. Có cơ sở để **gom 9 nhóm thành 6 nhóm lớn khi trình bày** mà không sửa bài thành viên (xem 03).
3. **Vấn đề lớn nhất của Phần II không nằm ở số phân hệ mà ở chỗ các bài chưa dùng chung một mô hình đối tượng.** Cùng một khái niệm có nhiều tên (PhuongAnBoTri / PhuongAnNguonLuc / HoSoTrinhDuyet), cùng một tên mang nhiều nghĩa (PhanBoNguonLuc, KetQuaDanhGia, BoTieuChi), và vòng đời hai đối tượng trung tâm (Nhu cầu nguồn lực, Phương án bố trí) chưa ai sở hữu trọn vẹn.
4. **Ba UC quyết định mô hình lớp chưa có ai đặc tả:** UC-02.2 (hồ sơ năng lực, dùng chung cho V4, V5, V6, V10), UC-05.2 (đánh dấu nghi ngờ xung đột và rẽ nhánh sang V7 hoặc V8/V9) và UC-07.3 (phê duyệt, tạo Locked Baseline). Đây là các lỗ hổng nền tảng, không phải lỗi của thành viên nào.
5. **Truy vết mã yêu cầu bị đứt ở 5/9 bài.** B-V2a, B-V3, B-V5, B-V7, B-V9 trích mã không có trong Phần I (CN-V9-08, BR-V5-07, QT-04 của V7...). Nội dung phần lớn vẫn đúng nghiệp vụ, chỉ cần đổi mã (mức B), nhưng phải làm trước khi lập ma trận truy vết chính thức.
6. **Chất lượng bài làm không đều.** B-V4 và B-V6 tốt, dùng được làm mẫu. B-V2b, B-V5, B-V9 tốt về nội dung nhưng cần chỉnh phạm vi hoặc mã. B-V7 có phạm vi lấn sang UC khác và tự thêm nghiệp vụ. B-V8 thiếu sơ đồ trong repo và dùng include sai. B-V3 chọn UC gần với "quản lý danh mục", có nguy cơ bị coi là quá đơn giản theo OUTLINE.

## 2. Đánh giá Phần I

### 2.1. Mục tiêu và nhóm nghiệp vụ

[Nguồn: P1 I.1.1, I.1.3.1] Mục tiêu: đáp ứng nhu cầu nguồn lực của nhiều dự án dùng chung nguồn lực, qua chuỗi xác định nhu cầu → đánh giá năng lực → tìm kiếm/xếp hạng → đánh giá khả năng tham gia → lập phương án → xử lý xung đột → phê duyệt (song song đánh giá chi phí), cộng với theo dõi – dự báo chạy liên tục.

Các quan hệ giữa vùng được nêu rõ: nối tiếp V2→V6; rẽ nhánh từ V6 sang V7 hoặc V8+V9; V9 song song V8; quay lại V8→V6/V7 và V4→V2; dùng chung hồ sơ năng lực (V3) và lịch nguồn lực tập trung; V10 phản hồi liên tục.

### 2.2. Nghiệp vụ bắt buộc phải bao phủ

[Đối chiếu P1 I.2.1 với mức ưu tiên "Cao" và luồng chính I.1.3.1] Các nghiệp vụ không được thiếu trong Phần II:

| Nghiệp vụ | CN chính | UC phụ trách (HD-PCCN) | Đã có đặc tả? |
|-----------|----------|------------------------|---------------|
| Lập và xác nhận nhu cầu | CN-02, 04, 06–08, 11, 13, 14, 16 | 01.1, 01.2 | Có (B-V2a, B-V2b) |
| Đánh giá năng lực, lưu hồ sơ năng lực | CN-21, 23, 24, 26, 27, 29, 30 | 02.2, 02.3 | **Chưa** |
| Tiêu chí, tìm kiếm, chấm điểm, shortlist | CN-31–34, 38, 39, 41, 45 | 03.1–03.3 | Có 03.3 (B-V4); 03.1, 03.2 chưa |
| Đánh giá khả năng tham gia | CN-47–51, 55, 59 | 04.1 | Có (B-V5) |
| Lập phương án | CN-62, 64, 69, 70, 72 | 05.1, 05.2 | 05.1 có (B-V6); **05.2 chưa** (gồm CN-70, 72) |
| Xử lý xung đột | CN-74, 77, 78, 80, 81, 84, 88 | 06.1–06.3 | Có một phần trong B-V7 |
| Phê duyệt, Locked Baseline, lưu vết | CN-89–91, 97, 99, 102 | 07.1, 07.3 | 07.1 có (B-V8); **07.3 chưa** |
| Chi phí – ngân sách | CN-104–106, 108, 112 | 08.1, 08.2 | Có (B-V9) |
| Theo dõi – dự báo | CN-113–115, 118–120, 122 | 09.1, 09.2 | **Chưa** (V10) |

### 2.3. Quy tắc ảnh hưởng vòng đời đối tượng và phân bổ nguồn lực

[Nguồn: P1 I.1.4, I.2.3] Các quy tắc sau quyết định trạng thái và liên kết lớp, cần được mọi bài dùng thống nhất:

- Nhu cầu: "chưa cố định" khi thiếu thông tin (CN-03); chỉ nhu cầu "đã xác nhận" mới sang V3/V4 (QT-05, QT-12). V10 còn dùng "nhu cầu dự kiến" và nhãn mức chắc chắn (QT-55, CN-117).
- Năng lực: trạng thái đã xác nhận / tự khai báo / cần kiểm chứng (CN-24); chứng chỉ hết hiệu lực (CN-25); quá hạn 6 tháng (RB-16).
- Khả năng tham gia: đầy đủ / một phần / không / chờ xác nhận (CN-51); nhãn "dữ liệu chưa đủ rõ" (QT-24).
- Phân bổ: phân bổ cứng (đã cam kết) và phân bổ mềm (giữ chỗ) trên **một** lịch nguồn lực tập trung (PCN-02); tổng ≤ 100% (QT-27, QT-32).
- Phương án: "đang xây dựng" tối đa 3 ngày (QT-31); có/không nghi ngờ xung đột (QT-30); quyết định phê duyệt / yêu cầu chỉnh sửa / từ chối / duyệt ngoại lệ (CN-97); Locked Baseline (CN-99).
- Xung đột: dưới Mức 3 chỉ theo dõi, từ Mức 3 xử lý chính thức (QT-33); hạn 3 ngày đàm phán, 1 ngày phân xử (QT-36).
- Thẩm quyền: DoA PMO Mức 1–3, CEO Mức 4–5 (QT-40); ngưỡng ngân sách 10% (QT-51).

### 2.4. Vấn đề trong Phần I (ghi nhận riêng, không viết lại)

| # | Vị trí | Vấn đề | Loại | Ảnh hưởng Phần II |
|---|--------|--------|------|-------------------|
| PI-1 | I.1.3.7 thang 5 mức; RB-59 | Mức 2 là 85–100%, Mức 3 là trên 120%: **khoảng 100–120% không thuộc mức nào**. Mức 4 (trên 110% kéo dài 2 tuần) chồng lên khoảng này. Mức 3 còn có điều kiện "dự án Hạng ưu tiên 1 bất kể %" nên một dự án ưu tiên 1 ở 50% cũng thành "quá tải". | Mâu thuẫn quy tắc | Cao. Ảnh hưởng V5 (cờ rủi ro), V6 (đánh dấu >100%), V7 (ngưỡng kích hoạt), V8 (DoA). B-V7 đã tự diễn giải thành "<20% quá tải" → xem D-04 |
| PI-2 | I.1.3.5 "Trường hợp đặc biệt"; CN-57; QT-25 | PMO phê duyệt vượt tải ngoại lệ "ở Mức 2–3", nhưng thang 5 mức nói Mức 2 chỉ "theo dõi", không cần phê duyệt | Mâu thuẫn nhẹ | UC-04.3 |
| PI-3 | I.1.2 so với HD-PCCN §2 | Phần I: V10 do **RM** thực hiện, PM cung cấp nhu cầu; PMO không tham gia V10. HD-PCCN ghi actor UC-09.x là "PMO/Portfolio Manager" | Mâu thuẫn giữa hai tài liệu nhóm | Trực tiếp ảnh hưởng V10 và II.1 → D-08 |
| PI-4 | I.3.9 bước 9 | Câu "Tiêu chí 'đáng kể' theo4; chạy sau cập nhật lịch tuần của V5 theo." bị cụt (đã kiểm tra trong file gốc, không phải lỗi chuyển đổi) | Câu chữ | Tiêu chí "thay đổi đáng kể" của V10 chưa định nghĩa → ghi giả định trong 09 |
| PI-5 | QT-30 "(Nguồn V6 ghi nhận là )"; RB-14 "và6"; PCN-01, 04, 08, 10, 11 cột căn cứ bắt đầu bằng "; " | Dấu vết trích dẫn bị xóa dở | Câu chữ | Không ảnh hưởng nghiệp vụ |
| PI-6 | I.3.8 | Hai bước cùng đánh số 8 | Câu chữ | Không |
| PI-7 | I.1.2 so với HD-PCCN §2 | HD-PCCN ghi actor UC-01.2 là PM (Phần I: RM xác nhận, CN-13), UC-01.1 là PM/RM (Phần I: PM), UC-08.1 là "Tài chính/RM" (Phần I: PM + Tài chính, RM không tham gia V9), UC-08.4 là "Tài chính/PMO/CEO" (Phần I: PM xác định hướng xử lý, CN-111) | Mâu thuẫn actor | B-V2b và B-V9 đã theo Phần I (đúng). Cần sửa HD-PCCN khi làm II.1 |
| PI-8 | HD-PCCN §2 cột CN | CN-91..94 gán cho cả UC-07.1 và UC-07.2; CN-42..46 gán cho UC-03.4 trong khi CN-42 (xem khoảng thiếu), CN-45 (bàn giao V5), CN-46 (phản hồi V2) không phải "điều chỉnh kết quả"; CN-118..120 (lập dự báo, đối chiếu dự báo) gán cho UC-09.1 trong khi ranh giới nói UC-09.2 mới là dự báo; CN-55, CN-59, CN-127 không gán cho UC nào | Ánh xạ PCCN chưa chuẩn | Đề xuất bảng ánh xạ lại trong 05 |

Tất cả các vấn đề trên đều sửa được bằng ghi chú hoặc quyết định, không cần đổi cấu trúc Phần I.

## 3. Phạm vi Phần II so với Phần I

### 3.1. Nội dung Phần II chưa có căn cứ trong Phần I (mở rộng phạm vi)

| Bài | Nội dung | Căn cứ Phần I | Đánh giá |
|-----|----------|---------------|----------|
| B-V2a A2 | "FTE ≤ 1.0 trên mỗi nhân sự" (RB-V2-03) | Không có. QT-02 chỉ yêu cầu lượng hóa FTE theo giai đoạn; FTE của nhu cầu là quy mô, có thể > 1 | Quy tắc tự tạo, cần bỏ |
| B-V7 A3 | Overtime khẩn cấp, thuê ngoài khẩn cấp do PMO và Tài chính duyệt | Mức 5 có "làm thêm giờ khẩn cấp tối đa 2 tuần" nhưng thuộc V8/CEO (RB-59); Tài chính không duyệt ở V7 | Tự thêm |
| B-V7 A4 | Hai dự án Rank 1: chia 50-50, job-sharing, nhân sự cấp thấp hỗ trợ | Không có | Tự thêm |
| B-V7 E1 | Dưới Mức 3: "chuyển cho các PM tự đàm phán nội bộ" | QT-33: dưới ngưỡng chỉ ghi nhận để theo dõi | Trái Phần I |
| B-V7 A2 | "Hệ thống hỗ trợ tổ chức họp khẩn phân tích tam giác ràng buộc" | Không có | Tự thêm, lại mang tính thao tác |
| B-V9 | Chi phí thực tế (ChiPhiThucTe), ngân sách còn lại = duyệt − phát sinh | CN-106 có nhắc "khi có dữ liệu thực tế"; công thức "còn lại" không có | Có căn cứ một phần; công thức là giả định |
| B-V3 | Lớp YeuCauQuanLyTieuChi với bước "RM xác nhận lưu" | Không có, nhưng là chi tiết hợp lý của UC quản lý | Chấp nhận được, nhưng thiếu nghiệp vụ thật CN-19 |

### 3.2. Nội dung Phần I bị bỏ sót trong Phần II

- Toàn bộ V10 (14 CN) – chưa làm.
- V3 phần đánh giá năng lực (CN-20..30) – chưa ai làm; B-V3 chỉ làm tiêu chí và **bỏ qua CN-19** (tiêu chí tạm cần PMO duyệt), là nhánh nghiệp vụ duy nhất làm UC-02.1 không còn là thao tác danh mục.
- CN-70, CN-72 (đánh dấu nghi ngờ xung đột, chuyển V7 hoặc V8+V9) – không ai đặc tả; B-V6 đẩy sang UC-05.2.
- CN-97..102 (ra quyết định, Locked Baseline, trả về V6/V7, lưu vết) – không ai đặc tả.
- CN-85 (CEO quyết định xung đột Mức 4–5), CN-86 (CCB) – B-V7 không có nhánh CEO dù UCD vẽ actor CEO.
- CN-128, CN-129 (PMO/CEO quyết định vượt ngân sách) – B-V9 chỉ ghi "cấp xử lý", không có người quyết định.
- CN-127 (PM gửi yêu cầu nguồn lực cho V5) – không gán UC.

### 3.3. Trùng lặp, chồng chéo

- B-V7 (UC-06.2) chứa phát hiện ngưỡng, phân tích CPM (UC-06.1) và PMO phân xử (UC-06.3).
- B-V8 (UC-07.1) chứa vòng giải trình của RM (UC-07.2).
- B-V9 đổi tên UC-08.1 thành cả nhóm V9, chứa 08.2, 08.3, một phần 08.4.
- B-V6 AD chứa quyết định của PM (thuộc UC-05.2); B-V2b UC-01.2 chứa hành động "PM điều chỉnh nhu cầu" trùng với UC-01.3.
- Kiểm tra quá tải: B-V2a (FTE), B-V5 (mức sử dụng), B-V6 (tổng >100%), B-V7 (Mức 3) dùng bốn cách diễn đạt ngưỡng khác nhau.

Việc lấn phạm vi ở B-V7, B-V8, B-V9 **có một mặt tích cực**: nó cho thấy các UC con trong V7, V8, V9 gắn rất chặt với nhau. Đây là căn cứ khi cân nhắc phương án D trong tài liệu 03.

## 4. Đánh giá cấu trúc phân hệ hiện tại

[Đối chiếu] 9 nhóm UC-01..UC-09 trùng 1–1 với 9 vùng của Phần I nên mọi CN đều có "nhà". Điểm yếu không phải ở số nhóm mà ở:

- Một số nhóm rất mỏng (V6 chỉ 2 UC, V10 chỉ 2 UC) trong khi các nhóm khác 4 UC.
- Ranh giới giữa nhóm được thiết kế theo **người thực hiện và thời điểm** (đúng với nghiệp vụ) nhưng các đối tượng dữ liệu lại xuyên nhóm (Phương án đi qua V6, V7, V8, V9, V10). Vì vậy mô hình lớp II.3 phải được xây ở mức toàn hệ thống, không ghép từ 9 mảnh.
- Sơ đồ II.1 tổng quát với 9 UC lớn và 6 actor vẫn đọc được; gom thành 6 nhóm sẽ gọn hơn nhưng không bắt buộc.

Chi tiết so sánh phương án: tài liệu 03.

## 5. Chất lượng tổng thể Phần II

| Tiêu chí | Đánh giá | Ghi chú |
|----------|----------|---------|
| Đúng mẫu HD-MAU | Khá | 7/9 bài đủ 12 mục; B-V2b thiếu 7–12; B-V8 thiếu sơ đồ trong repo |
| Đúng nghiệp vụ Phần I | Khá | Phần lớn đúng; sai lệch tập trung ở B-V2a (quy tắc FTE), B-V7 (nhánh tự thêm, E1) |
| Đúng phạm vi UC | Trung bình | B-V7, B-V8, B-V9 lấn UC khác; B-V6 đẩy CN-70 sang UC không ai làm |
| Truy vết mã | Yếu | 5/9 bài dùng mã ngoài baseline |
| Ký pháp UML | Trung bình | include/extend sai ở B-V8, B-V9, B-V7 (UCD trái với văn bản); AD có nhánh treo ở B-V2a, B-V5; class dồn thao tác vào ô thuộc tính ở B-V9 |
| Nhất quán thuật ngữ, lớp | Yếu | Xem 04 mục 3 và 07 |
| Tách nghiệp vụ khỏi kỹ thuật | Trung bình | B-V2a (đăng nhập, nút, lỗi CSDL), B-V7 (Controller, Service, hash, xuất file) |

Nội dung nên giữ nguyên làm chuẩn tham chiếu: B-V4 toàn bài; B-V6 Description và AD; B-V2b UC-01.2 và AD 01.2; B-V5 luồng chính và nhánh A1–A4; B-V9 bảng lớp (sau khi đổi tên PhanBoNguonLuc); B-V8 luồng chính và A1. Chi tiết: tài liệu 06.
