# 01. Manifest và phạm vi nguồn

Ngày kiểm kê: 20/10/2026. Nhánh gốc: `main`, commit `37c4e18` ("Add files via upload", 20/10/2026). Repository có 14 file, không có thư mục con, không có quy tắc đóng góp riêng. `README.md` chỉ có tiêu đề repository.

Cách đọc: mọi file `.docx` được chuyển sang văn bản bằng pandoc và đọc toàn bộ; mọi hình nhúng trong file (UCD, AD, sơ đồ lớp, sơ đồ tuần tự) được mở và xem trực tiếp. Liên kết Google Drive trong một số bài **không mở được** từ môi trường audit, nên phần nội dung chỉ có ở Drive chưa được đánh giá.

## 1. Danh sách tài liệu

| # | Đường dẫn | Loại | Người phụ trách | Nội dung chính | Phiên bản / trạng thái | Ghi chú |
|---|-----------|------|-----------------|----------------|------------------------|---------|
| 1 | `[PTTKHT] I - PHÂN TÍCH YÊU CẦU FINAL.docx` | Phần I chính thức | Không ghi trong file; metadata "dodinhluan178" tạo 08/10/2026 | I.1 mô tả nghiệp vụ V2–V10, 6 vai trò, 9 AD quy trình, QT-01..57, thang cảnh báo 5 mức, DoA; I.2 CN-01..129, PCN-01..11, RB-01..62; I.3 mô tả bài toán theo V | Ghi "FINAL". Coi là baseline | Có vài đoạn trích dẫn bị cụt (xem 02, mục 2.4) |
| 2 | `[PTTKHT] HOÀN THIỆN MỤC II - PHÂN TÍCH (THIẾT KẾ LOGIC).md` (HD-PCCN) | Hướng dẫn / PCCN | Trưởng nhóm (giả định) | PCCN 9 nhóm UC-01..UC-09, 28 UC chi tiết, UC Description Summary, bảng ranh giới UC, tiêu chí và đề xuất UC trọng tâm, checklist | Bản "đề xuất ban đầu"; §9 nói phải thay mục 5 bằng phân công chính thức khi chốt | Không tìm thấy bản phân công chính thức trong repo |
| 3 | `[PTTKHT] HOÀN THIỆN MỤC II - PHÂN TÍCH (THIẾT KẾ LOGIC) (1).md` (HD-MAU) | Mẫu bài làm | Trưởng nhóm (giả định) | Khung 12 mục: UCD, UC Description/FDS, AD, đối chiếu, II.2+ đề xuất lớp | Không trùng file số 2 (hai nội dung khác nhau dù tên gần giống) | Nên đổi tên cho dễ phân biệt khi được phép |
| 4 | `Outline bài thảo luận.docx` (OUTLINE) | Yêu cầu học phần | Giảng viên (metadata "Han Minh Phuong") | Cấu trúc báo cáo I–III; II.1 UCD tổng quát, II.2 UCD chi tiết + UC Description "cho từng ca sử dụng" + AD, II.3 lớp miền, II.4 trạng thái/giao tiếp/tuần tự; yêu cầu UC cá nhân "không quá đơn giản (thêm, xóa danh mục)" | Cập nhật 09/09/2026 | Căn cứ cho Decision D-02, D-05 |
| 5 | `V2-Phần II .docx` (B-V2a) | Bài thành viên | Nguyễn Thị Thùy Linh ("Thùy Linh SN2") | UC-01.1 đủ 12 mục, UCD + AD + class nhúng | Đầy đủ khung | |
| 6 | `V2-Phần II (2).docx` (B-V2b) | Bài thành viên | Nguyễn Tuấn Long | UC-01.2 và UC-01.3: UCD, Description, 2 AD, mục 6 | **Thiếu mục 7–12** (bảng lớp còn để "..."). Tên file dễ nhầm là bản thứ hai của B-V2a | Không phải bản trùng: khác người, khác UC |
| 7 | `V3- Phần 2.docx` (B-V3) | Bài thành viên | Lê Hoài Linh | UC-02.1 đủ khung, UCD + AD + class nhúng | **§3.4 BR còn để trống mẫu** | |
| 8 | `V4 - Phần II.docx` (B-V4) | Bài thành viên | Nguyễn Hoàng Linh | UC-03.3 đủ 12 mục, UCD + AD + class nhúng; có link Drive phụ | Đầy đủ | |
| 9 | `NV05 I2 - I3.docx` (B-V5) | Bài thành viên | Nguyễn Hoàng Khánh Linh | UC-04.1 đủ khung, UCD (gồm 04.1–04.3) + AD + class nhúng | Đầy đủ; còn sót chữ hướng dẫn của mẫu ở §2.3, §4.2; §11 và §12 bị dính tiêu đề | Tên file "I2 - I3" không khớp nội dung (là Phần II) |
| 10 | `V6 - Phần II.docx` (B-V6) | Bài thành viên | Nguyễn Thi Thùy Linh | UC-05.1 đủ 12 mục, UCD + AD + class nhúng | Đầy đủ | Họ tên gần trùng B-V2a, cần xác minh có phải hai người khác nhau |
| 11 | `MNV7_II_Thiết kế Logic.docx` (B-V7) | Bài thành viên | Lưu Thùy Linh | UC-06.2 đủ 12 mục; **làm thêm II.4** (máy trạng thái dạng bảng, giao tiếp dạng chữ, sơ đồ tuần tự) và mục III ma trận kiểm soát | Vượt khung được giao | |
| 12 | `MNV8 - Ngọc Linh.docx` (B-V8) | Bài thành viên | Ngọc Linh | UC-07.1: Description, BR, lớp dạng bảng | **UCD, AD, class không nhúng**, chỉ có link Drive (không đọc được); §4 còn chữ mẫu | Chưa đánh giá được sơ đồ |
| 13 | `V9 - Phần II.docx` (B-V9) | Bài thành viên | Ngô Nhật Long | UC-08.1 (đổi tên thành "Đánh giá tác động chi phí và ngân sách của phương án bố trí nguồn lực"), Description, lớp đầy đủ, class nhúng | **UCD và AD chỉ có link Drive** | Chưa đánh giá được UCD, AD |
| 14 | `README.md` | Khác | | Chỉ có tiêu đề | | |

## 2. Danh mục UC theo nguồn

[Nguồn: HD-PCCN §1, §2] Có **9 nhóm chức năng** UC-01..UC-09 ứng với 9 vùng nghiệp vụ V2..V10 và **28 UC chi tiết** (3+3+4+3+2+3+4+4+2). Con số "khoảng 27 UC" trong đề bài lệch 1 so với nguồn; báo cáo dùng 28.

## 3. Phân bổ bài làm (suy ra từ tiêu đề từng bài)

| Vùng | Thành viên | UC đã làm | UC đề xuất trong HD-PCCN §5 | Khớp? |
|------|-----------|-----------|-----------------------------|-------|
| V2 | Thùy Linh (B-V2a) | UC-01.1 | UC-01.1 | Khớp |
| V2 | Tuấn Long (B-V2b) | UC-01.2, UC-01.3 | UC-01.3 | Làm thêm UC-01.2 |
| V3 | Lê Hoài Linh | UC-02.1 | UC-02.2 | **Khác** |
| V4 | Nguyễn Hoàng Linh | UC-03.3 | UC-03.3 | Khớp |
| V5 | Khánh Linh | UC-04.1 | UC-04.1 / UC-04.2 | Khớp (một UC) |
| V6 | Nguyễn Thi Thùy Linh | UC-05.1 | UC-05.1 | Khớp |
| V7 | Lưu Thùy Linh | UC-06.2 (lấn sang 06.1, 06.3) | UC-06.1 / UC-06.2 | Khớp một phần |
| V8 | Ngọc Linh | UC-07.1 (lấn sang 07.2) | UC-07.1 / UC-07.3 | **Thiếu UC-07.3** |
| V9 | Ngô Nhật Long | UC-08.1 mở rộng ra cả V9 | UC-08.3 / UC-08.4 | **Khác**, phạm vi bị nới |
| V10 | Chưa có bài | UC-09.1, UC-09.2 (theo HD-PCCN §1) | UC-09.2 | Chưa làm |

[Giả định] Không có tài liệu phân công chính thức trong repo (HD-PCCN §9 yêu cầu thay mục 5 bằng phân công chính thức). Bảng trên dựa vào tiêu đề bài làm. Nếu nhóm đã giao khác, các kết luận về "lệch phân công" cần đối chiếu lại.

## 4. Nguồn còn thiếu và giới hạn phân tích

| Thiếu | Ảnh hưởng tới audit |
|-------|---------------------|
| Bản phân công UC chính thức | Không xác định chắc UC-02.1 (V3) và UC-08.1 mở rộng (V9) là được giao hay tự chọn |
| Sơ đồ trên Drive của B-V8 (UCD, AD, class) và B-V9 (UCD, AD) | Không kiểm tra được ký pháp và độ khớp Description–AD của hai bài này |
| Mục 7–12 của B-V2b | Chưa có đề xuất lớp cho UC-01.2/01.3 |
| Tài liệu nguồn từng vùng mà Phần I trích (QT-V2-01, QT-V7-04...) | Nhiều bài dùng mã cũ kiểu "CN-V9-08", "BR-V5-07", "QT-04". Không có tài liệu này nên chỉ ánh xạ được theo nội dung, chưa ánh xạ chắc chắn theo mã |
| Danh sách "Q-02, Q-03, Q-04" mà B-V3, B-V9 nhắc tới | Không biết đây là câu hỏi mở nào; trong Phần I các điểm đó đã được chốt (xem 02) |
| Bài V10, II.1, II.3 tổng hợp | Là việc chưa làm; xem 09 |

## 5. File trùng, nhiều phiên bản, trạng thái chưa rõ

- Không có file trùng nội dung. Hai cặp tên dễ nhầm: `V2-Phần II .docx` / `V2-Phần II (2).docx` (hai người khác nhau) và hai file `HOÀN THIỆN MỤC II` (PCCN và mẫu).
- B-V8 và B-V9 phụ thuộc Drive; bản trong repo không tự đầy đủ.
- B-V7 chứa nội dung II.4 chưa được giao; trạng thái "nháp tham khảo" hay "bài nộp" chưa rõ.
- Ba bài B-V2a, B-V6, B-V7 có họ tên người làm gần giống nhau (Thùy Linh). Cần xác nhận để tránh giao việc nhầm người.
