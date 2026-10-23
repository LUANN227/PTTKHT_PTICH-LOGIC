## V9 — V9 - Phần II.docx

| Vị trí (theo bản gốc) | Trước | Sau | Lý do |
|---|---|---|---|
| Bảng 0, dòng 4, cột 1 | Đánh giá tác động chi phí và ngân sách của phương án bố trí nguồn lực | Tính và cập nhật chi phí phương án | QĐ-10: 08.1 đúng tên và phạm vi CN-103–107 (bảng II.1); đối chiếu, so sánh, hướng xử lý thuộc FDS 08.2–08.4 |
| Bảng 1, dòng 2, cột 1 | Đánh giá tác động chi phí và ngân sách của phương án bố trí nguồn lực | Tính và cập nhật chi phí phương án | QĐ-10: 08.1 đúng tên và phạm vi CN-103–107 (bảng II.1); đối chiếu, so sánh, hướng xử lý thuộc FDS 08.2–08.4 |
| Bảng 3, dòng 2, cột 1 | Đánh giá tác động chi phí và ngân sách của phương án bố trí nguồn lực | Tính và cập nhật chi phí phương án | QĐ-10: 08.1 đúng tên và phạm vi CN-103–107 (bảng II.1); đối chiếu, so sánh, hướng xử lý thuộc FDS 08.2–08.4 |
| Bảng 1, dòng 5, cột 1 | UC-07.1 Rà soát và đánh giá phương án (V8, nhận kết quả V9); UC-09 (V10, nhận thông tin liên quan) | UC-08.2 Đối chiếu chi phí và ngân sách (dùng kết quả chi phí của 08.1); UC-08.3, UC-08.4. Kết quả V9 được chuyển cho V8 và V10 ở UC-08.4 (CN-112) | QĐ-10: 08.1 đúng tên và phạm vi CN-103–107 (bảng II.1); đối chiếu, so sánh, hướng xử lý thuộc FDS 08.2–08.4 |
| Bảng 2, dòng 1 |  | UC-08.1 \| Không có include/extend \| — \| V8 xem thông tin chi phí của V9 (CN-93) và V9 chuyển kết quả cho V8, V10 (CN-112) là luồng dữ liệu, không phải include. | Bỏ include UC-07.1 → UC-08.1: không có trên UCD_UC-07, UCD_UC-08 |
| Đoạn 6 | Trong V9 không có include/extend nào khác. Với V10 chỉ có luồng chuyển dữ liệu (RB-V9-11), không phải quan hệ UC của UC này. | Trong V9 không có include/extend. Các UC 08.2–08.4 dùng kết quả của 08.1 theo trình tự nghiệp vụ. | Bỏ mã RB-V9 không có trong Phần I |
| Xóa đoạn 8 | https://drive.google.com/file/d/1rrTOpuAWxmBxj9CjM1G84sIg2HGOnHI-/view?usp=sharing |  | Thay đường dẫn Drive bằng hình trong bài |
| Thêm ảnh sau đoạn 7 |  | UCD_UC-08.png | UCD vùng UC-08 (nguồn draw.io) |
| Bảng 3, dòng 3, cột 1 | PM cùng Tài chính xác định chi phí dự toán/dự báo của phương án, đối chiếu với ngân sách được duyệt và phần còn lại, ghi nhận nguyên nhân vượt, so sánh đánh đổi khi có nhiều phương án và ghi nhận hướng xử lý, để cung cấp thông tin cho V8 và V10. UC chỉ cung cấp thông tin, không quyết định phương án. | PM xác định phương án cần đánh giá chi phí và lượng hóa các yếu tố tạo chi phí; Tài chính cung cấp đơn giá, tính chi phí dự toán, cập nhật dự báo khi có dữ liệu thực tế hoặc thay đổi và tính lại phần chi phí bị ảnh hưởng. Kết quả chi phí là đầu vào của UC-08.2. UC không đối chiếu ngân sách và không quyết định phương án. | QĐ-10: 08.1 đúng tên và phạm vi CN-103–107 (bảng II.1); đối chiếu, so sánh, hướng xử lý thuộc FDS 08.2–08.4 |
| Bảng 3, dòng 6, cột 1 | PM bắt đầu đánh giá một phương án bố trí nguồn lực mới hoặc có thay đổi, hoặc có từ hai phương án cần so sánh, hoặc có dấu hiệu vượt ngân sách. | PM bắt đầu đánh giá chi phí cho một phương án bố trí mới hoặc có thay đổi về người, số lượng, thời gian, mức độ tham gia (CN-103, CN-107). | QĐ-10: 08.1 đúng tên và phạm vi CN-103–107 (bảng II.1); đối chiếu, so sánh, hướng xử lý thuộc FDS 08.2–08.4 |
| Bảng 3, dòng 7, cột 1 | (1) Có phương án bố trí và phạm vi công việc tương ứng (RB-V9-02). (2) Có ngân sách được duyệt cho phần việc cần kiểm tra. (3) PM, Tài chính được phân quyền (PCN-V9-04). | Có phương án bố trí và phạm vi công việc tương ứng (CN-103). | Ngân sách thuộc 08.2; bỏ điều kiện phân quyền (mẫu FDS) |
| Bảng 3, dòng 8, cột 1 | Chi phí dự toán/dự báo, chênh lệch, trạng thái ngân sách, cấp xử lý, nguyên nhân vượt (nếu có) và hướng xử lý được lưu kèm tài khoản thực hiện (PCN-V9-05). Kết quả sẵn sàng chuyển V8 và V10 (RB-V9-11). Không tạo Locked Baseline (RB-V9-10). | Chi phí dự toán, dự báo (phân biệt hai loại, QT-49) và phần chi phí bị ảnh hưởng được lưu, sẵn sàng cho UC-08.2. Không tạo Locked Baseline (thuộc V8, CN-99). | QĐ-10: 08.1 đúng tên và phạm vi CN-103–107 (bảng II.1); đối chiếu, so sánh, hướng xử lý thuộc FDS 08.2–08.4; bỏ ghi tài khoản |
| Bảng 4, dòng 1 |  | 1 \| PM \| Chọn phương án bố trí nguồn lực cần đánh giá chi phí và ghi lý do (CN-103). | QĐ-10: 08.1 đúng tên và phạm vi CN-103–107 (bảng II.1); đối chiếu, so sánh, hướng xử lý thuộc FDS 08.2–08.4; mã CN theo Phần I |
| Bảng 4, dòng 2 |  | 2 \| System \| Hiển thị phương án, phạm vi công việc liên quan, nhân sự, số lượng, thời gian và mức độ tham gia (CN-103, CN-104). | QĐ-10: 08.1 đúng tên và phạm vi CN-103–107 (bảng II.1); đối chiếu, so sánh, hướng xử lý thuộc FDS 08.2–08.4; mã CN theo Phần I |
| Bảng 4, dòng 3 |  | 3 \| PM \| Lượng hóa, xác nhận các yếu tố tạo chi phí: nhân sự, số lượng, thời gian, mức độ tham gia (CN-104). | QĐ-10: 08.1 đúng tên và phạm vi CN-103–107 (bảng II.1); đối chiếu, so sánh, hướng xử lý thuộc FDS 08.2–08.4; mã CN theo Phần I |
| Bảng 4, dòng 4 |  | 4 \| Tài chính \| Cung cấp hoặc cập nhật đơn giá áp dụng; ghi nhận chi phí thực tế nếu đã phát sinh (CN-105, CN-106). | QĐ-10: 08.1 đúng tên và phạm vi CN-103–107 (bảng II.1); đối chiếu, so sánh, hướng xử lý thuộc FDS 08.2–08.4; mã CN theo Phần I |
| Bảng 4, dòng 5 |  | 5 \| Tài chính \| Tính chi phí dự toán của phương án; khi có dữ liệu thực tế hoặc thay đổi thì cập nhật dự báo chi phí, lưu tách dự toán và dự báo (CN-106; QT-49). | QĐ-10: 08.1 đúng tên và phạm vi CN-103–107 (bảng II.1); đối chiếu, so sánh, hướng xử lý thuộc FDS 08.2–08.4; mã CN theo Phần I |
| Bảng 4, dòng 6 |  | 6 \| PM \| Xem kết quả chi phí dự toán, dự báo của phương án (CN-104, CN-106). | QĐ-10: 08.1 đúng tên và phạm vi CN-103–107 (bảng II.1); đối chiếu, so sánh, hướng xử lý thuộc FDS 08.2–08.4; mã CN theo Phần I |
| Bảng 4, dòng 7 |  | 7 \| System \| Lưu kết quả chi phí (dự toán, dự báo, phần bị ảnh hưởng), sẵn sàng cho UC-08.2 Đối chiếu chi phí và ngân sách. | QĐ-10: 08.1 đúng tên và phạm vi CN-103–107 (bảng II.1); đối chiếu, so sánh, hướng xử lý thuộc FDS 08.2–08.4; mã CN theo Phần I |
| Bảng 4, xóa dòng 8 | 8 \| System \| Lưu kết quả, cung cấp cho V8 và V10 (RB-V9-11), ghi lại tài khoản thực hiện (PCN-V9-05). |  | Ghi tài khoản là yêu cầu chung (PCN-07), không phải bước nghiệp vụ |
| Bảng 5, dòng 1 |  | (giữ) \| (giữ) \| (giữ) \| (giữ) \| Hệ thống xác định phần chi phí bị ảnh hưởng; Tài chính tính lại và cập nhật dự báo (CN-107; QT-48). Tiếp bước 5. | Mã theo Phần I; CN-107 giao việc tính lại cho Tài chính |
| Bảng 5, xóa dòng 2 | A2 \| 6 \| Chi phí dự kiến vượt phần ngân sách còn lại. \| vượt ngân sách còn lại \| PM và Tài chính ghi nguyên nhân vượt (CN-V9-15; RB-V9-05). Hệ thống xác định tỷ lệ vượt = (chi phí dự kiến − ngân sách còn lại) / ngân sách còn lại: không quá 10% thì cấp Quản lý danh mục, trên 10% thì cấp CEO/Managing Director (RB-V9-07, 08). Tiếp bước 7. |  | Đối chiếu, tỷ lệ vượt, gắn cấp thuộc UC-08.2, 08.4 (QĐ-10); công thức chờ QĐ-07 |
| Bảng 5, xóa dòng 3 | A3 \| 6 đến 7 \| Có từ hai phương án cùng cần đánh giá. \| từ hai phương án trở lên \| Hệ thống so sánh theo thứ tự: đạt yêu cầu chất lượng tối thiểu, rồi chi phí, rồi thời gian (CN-V9-16 đến 18; RB-V9-06). Tiếp bước 7 (PM ghi nhận hướng xử lý sau khi xem kết quả so sánh). |  | So sánh phương án thuộc UC-08.3 (QĐ-10) |
| Bảng 5, dòng 4 |  | (giữ) \| (giữ) \| (giữ) \| (giữ) \| Hệ thống đánh dấu dữ liệu thiếu, yêu cầu Tài chính bổ sung (CN-105), không tự suy đoán; UC kết thúc, chưa có kết luận chính thức về chi phí. | Thêm mã CN; khớp nhánh E1 trên AD |
| Bảng 5, dòng 5 |  | (giữ) \| 1 \| Chưa có phương án hoặc phạm vi công việc. \| không có phương án hoặc phạm vi công việc \| Hệ thống không bắt đầu đánh giá; UC kết thúc (CN-103). | Bỏ kiểm tra quyền (mẫu FDS); ngân sách thuộc 08.2 |
| Bảng 6, dòng 1 |  | CN-103 \| PM xác định phương án cần đánh giá chi phí và lý do, dựa trên phương án bố trí và phạm vi công việc. \| Bước 1, 2; E2 | Đổi mã CN-V9/RB-V9/PCN-V9 sang mã Phần I; giữ quy tắc thuộc 08.1 (QĐ-10) |
| Bảng 6, dòng 2 |  | CN-104 \| PM lượng hóa yếu tố tạo chi phí: nhân sự, số lượng, thời gian, mức độ tham gia. \| Bước 2, 3 | Đổi mã CN-V9/RB-V9/PCN-V9 sang mã Phần I; giữ quy tắc thuộc 08.1 (QĐ-10) |
| Bảng 6, dòng 3 |  | CN-105 \| Tài chính cung cấp thông tin chi phí, gồm đơn giá. \| Bước 4; E1 | Đổi mã CN-V9/RB-V9/PCN-V9 sang mã Phần I; giữ quy tắc thuộc 08.1 (QĐ-10) |
| Bảng 6, dòng 4 |  | CN-106 \| Tài chính tính chi phí dự toán, cập nhật dự báo khi có dữ liệu thực tế hoặc thay đổi; phân biệt hai loại. \| Bước 4, 5 | Đổi mã CN-V9/RB-V9/PCN-V9 sang mã Phần I; giữ quy tắc thuộc 08.1 (QĐ-10) |
| Bảng 6, dòng 5 |  | CN-107 \| Tài chính tính lại phần chi phí bị ảnh hưởng khi thay đổi người, số lượng, thời gian, mức độ tham gia. \| A1 | Đổi mã CN-V9/RB-V9/PCN-V9 sang mã Phần I; giữ quy tắc thuộc 08.1 (QĐ-10) |
| Bảng 6, dòng 6 |  | QT-48 \| Thay đổi người, số lượng, thời gian hoặc mức độ tham gia có thể làm thay đổi chi phí và phải được xem xét lại. \| Điều kiện rẽ nhánh A1 | Đổi mã CN-V9/RB-V9/PCN-V9 sang mã Phần I; giữ quy tắc thuộc 08.1 (QĐ-10) |
| Bảng 6, dòng 7 |  | QT-49 \| Phải phân biệt dự toán (chi phí dự kiến) và dự báo (ước tính được cập nhật). \| Bước 5 | Đổi mã CN-V9/RB-V9/PCN-V9 sang mã Phần I; giữ quy tắc thuộc 08.1 (QĐ-10) |
| Bảng 6, dòng 8 |  | CN-108 \| Đối chiếu chi phí dự kiến với ngân sách — thuộc UC-08.2. \| Đầu ra bước 7 (ngoài UC) | Đổi mã CN-V9/RB-V9/PCN-V9 sang mã Phần I; giữ quy tắc thuộc 08.1 (QĐ-10) |
| Bảng 6, dòng 9 |  | CN-99, CN-112 \| Locked Baseline thuộc V8; chuyển kết quả cho V8, V10 thuộc UC-08.4. \| Ngoài phạm vi UC | Đổi mã CN-V9/RB-V9/PCN-V9 sang mã Phần I; giữ quy tắc thuộc 08.1 (QĐ-10) |
| Bảng 6, xóa dòng 10 | PCN-V9-05 \| Ghi nhận tài khoản thay đổi chi phí, dự báo, ngân sách. \| Bước 8 |  | Quy tắc thuộc 08.2–08.4 hoặc mã không có trong Phần I |
| Bảng 6, xóa dòng 11 | RB-V9-02 \| Đánh giá dựa trên phương án và phạm vi công việc. \| Tiền điều kiện, E2 |  | Quy tắc thuộc 08.2–08.4 hoặc mã không có trong Phần I |
| Bảng 6, xóa dòng 12 | RB-V9-03 \| Thay đổi làm ảnh hưởng chi phí thì tính lại. \| Điều kiện rẽ nhánh A1 |  | Quy tắc thuộc 08.2–08.4 hoặc mã không có trong Phần I |
| Bảng 6, xóa dòng 13 | RB-V9-04 \| Đối chiếu với ngân sách được duyệt và phần còn lại. \| Ràng buộc bước 6 |  | Quy tắc thuộc 08.2–08.4 hoặc mã không có trong Phần I |
| Bảng 6, xóa dòng 14 | RB-V9-05 \| Vượt ngân sách phải xác định nguyên nhân và hướng xử lý. \| A2 |  | Quy tắc thuộc 08.2–08.4 hoặc mã không có trong Phần I |
| Bảng 6, xóa dòng 15 | RB-V9-06 \| Thứ tự so sánh: chất lượng tối thiểu, chi phí, thời gian. \| A3 |  | Quy tắc thuộc 08.2–08.4 hoặc mã không có trong Phần I |
| Bảng 6, xóa dòng 16 | RB-V9-07, 08 \| Ngưỡng 10% quyết định cấp Quản lý danh mục hoặc CEO/MD. \| Điều kiện rẽ nhánh A2 |  | Quy tắc thuộc 08.2–08.4 hoặc mã không có trong Phần I |
| Bảng 6, xóa dòng 17 | RB-V9-09, 11 \| Quyết định ở V8; kết quả chuyển V8 và V10. \| Bước 7, 8 (giới hạn đầu ra) |  | Quy tắc thuộc 08.2–08.4 hoặc mã không có trong Phần I |
| Bảng 6, xóa dòng 18 | RB-V9-10 \| Không tạo Locked Baseline. \| Ngoài phạm vi UC |  | Quy tắc thuộc 08.2–08.4 hoặc mã không có trong Phần I |
| Xóa đoạn 17 | https://drive.google.com/file/d/1VKcpw1lXUzIkKd_Gc3u5Nlv9TyPFbLSu/view?usp=sharing |  | Thay đường dẫn Drive bằng hình trong bài |
| Thêm ảnh sau đoạn 16 |  | AD_UC-08.1.png | AD vẽ lại theo phạm vi 08.1; có nhánh E1, E2, A1; Tài chính có làn riêng (CN-105–107) |
| Bảng 7, dòng 2, cột 2 | Association; <<include>> từ UC-07.1 đến UC-08.1. | Association PM, Tài chính – UC-08.1; không có include/extend. | Bỏ include |
| Bảng 7, dòng 3, cột 2 | AD khớp bước 1 đến 8; bước 4 vẽ thành hai action riêng (đơn giá, chi phí thực tế). | AD khớp bước 1 đến 7; A1 là nhánh trước bước 5. | Theo D mới |
| Bảng 7, dòng 4, cột 2 | Phương án, công việc, yếu tố chi phí, đơn giá, dự toán, dự báo, ngân sách, chênh lệch, nguyên nhân vượt, hướng xử lý, kết quả so sánh. | Phương án, yếu tố chi phí, đơn giá, chi phí thực tế, dự toán, dự báo. | Theo phạm vi 08.1 |
| Bảng 7, dòng 5, cột 2 | Dự toán trước đối chiếu ngân sách; so sánh phương án trước khi ghi nhận hướng xử lý. | Đơn giá trước dự toán; dự báo cập nhật sau khi có chi phí thực tế hoặc thay đổi. | Theo D mới |
| Bảng 7, dòng 6, cột 2 | A1, A2, A3, E1, E2 đều là decision riêng. | A1, E1, E2 đều là decision riêng. | Theo D mới |
| Bảng 7, dòng 7, cột 2 | Kết thúc sớm E1, E2; kết thúc chính sau bước 8. | Kết thúc sớm E1, E2; kết thúc chính sau bước 7. | Theo D mới |
| Bảng 8, 9, 10, 11, 12, 13, 14 | CN-V9-11, 13, 14; RB-V9-07, 08, CN-V9-01 đến 05, CN-V9-03 đến 05, CN-V9-09, 10, RB-V9-03, CN-V9-09, 10, CN-V9-11 đến 14, CN-V9-11, 12, RB-V9-04, CN-V9-11, 12, CN-V9-13, 14, CN-V9-16 đến 18, CN-V9-16, RB-V9-06, CN-V9-19 đến 22, CN-V9-08, QT-03, CN-V9-15, RB-V9-05, CN-V9-01, RB-V9-02, CN-V9-02, RB-V9-02, CN-V9-01, CN-V9-02, CN-V9-06, CN-V9-07, CN-V9-08, CN-V9-09, CN-V9-12, CN-V9-15, RB-V9-02, RB-V9-… | CN-108; QT-51, CN-103, CN-104, CN-104, CN-106, CN-107, QT-48, CN-106, CN-107, CN-108, CN-108, QT-47, CN-108, CN-108, CN-110, CN-110, QT-50, CN-111, CN-106, QT-49, CN-109, CN-103, CN-103, CN-103, CN-103, CN-105, CN-106, CN-106, CN-106, CN-108, CN-109, CN-103, QT-48, QT-47, CN-109, QT-50, QT-51, CN-97, CN-99, QT-49, PCN-07, PCN-08, PCN-07 | Đổi mã riêng của bài sang mã Phần I (52 chỗ) |
| Bảng 8, dòng 2 |  | (giữ) \| Không (dùng chung) \| Phạm vi công việc lấy từ DuAn, GiaiDoanDuAn và nhu cầu của phương án (Hình II.3-2); không tạo lớp riêng. | Khớp sơ đồ lớp II.3 (Hình II.3-5) |
| Bảng 8, dòng 3 |  | Chi tiết bố trí (dòng phương án) \| Có (dùng chung) \| Vai trò, tỷ lệ tham gia, thời gian của từng dòng phương án (CN-104); dùng lớp ChiTietBoTri của V6 (Hình II.3-4). | Dòng phương án dùng ChiTietBoTri |
| Bảng 8, dòng 13 |  | (giữ) \| Chưa (chờ QĐ-19) \| Ngưỡng 10% giữ ở dạng quy tắc QT-51; cấp xử lý ghi ở thuộc tính capXuLy của DanhGiaChiPhi. | QĐ-19 chưa chốt |
| Bảng 8, dòng 14 |  | (giữ) \| Không \| Là actor; người thực hiện được ghi theo PCN-07, không cần lớp miền riêng. | Bỏ NguoiDung (thống nhất II.3) |
| Bảng 8, dòng 16, cột 2 | Thuộc V8 (CN-97, CN-99). | Thuộc V8 (CN-97, CN-99). | Đổi mã |
| Bảng 9, dòng 1 |  | (giữ) \| ChiTietBoTri \| Lớp nắm vai trò, tỷ lệ, thời gian; chi phí tính từ đơn giá. | Khớp sơ đồ lớp II.3 (Hình II.3-5) |
| Bảng 9, dòng 9 |  | Xác định cấp xử lý theo ngưỡng \| DanhGiaChiPhi \| Ngưỡng 10% là quy tắc QT-51 (chờ QĐ-19). | Khớp sơ đồ lớp II.3 (Hình II.3-5) |
| Bảng 10, xóa dòng 2 | CongViec \| Phạm vi công việc của phương án \| CN-103 |  | CongViec không là lớp riêng (Hình II.3-2) |
| Bảng 10, dòng 3 |  | ChiTietBoTri \| Dòng phương án: vai trò, tỷ lệ tham gia, thời gian (lớp của V6) \| (giữ) | Khớp sơ đồ lớp II.3 (Hình II.3-5) |
| Bảng 10, xóa dòng 12 | NguongPheDuyetNganSach \| Ngưỡng 10% và cấp xử lý \| QT-51 |  | Ngưỡng giữ ở dạng quy tắc (QĐ-19) |
| Bảng 10, xóa dòng 15 | NguoiDung \| PM hoặc Tài chính thao tác \| PCN-07, PCN-08 |  | Bỏ NguoiDung |
| Bảng 11, xóa dòng 2 | CongViec \| maCongViec, tenCongViec, phamVi \| Phạm vi mà phương án thực hiện. |  | CongViec không là lớp riêng |
| Bảng 11, dòng 3 |  | ChiTietBoTri \| vaiTroDuocGan, tyLeThamGia, tuNgay, denNgay \| Lớp của V6 (Hình II.3-4); V9 dùng để tính chi phí theo đơn giá. Đơn vị mức tham gia chưa chốt (Q-03). | Khớp sơ đồ lớp II.3 (Hình II.3-5) |
| Bảng 11, dòng 9 |  | (giữ) \| thoiDiem, chiPhiDuKienTaiThoiDiem, nganSachConLaiTaiThoiDiem, chenhLech, tyLeVuot, trangThaiNganSach, capXuLy \| Lưu giá trị chốt tại thời điểm đánh giá để kết quả không đổi khi đơn giá hoặc ngân sách thay đổi sau đó. tyLeVuot = chenhLech / nganSachConLai khi vượt [Chờ xác nhận QĐ-07]; chưa tính khi ngân sách còn lại ≤ 0. trangThaiNganSach: TrongNganSach, VuotNganSach. capXuLy: KhongCan, … | Khớp sơ đồ lớp II.3 (Hình II.3-5); công thức chờ QĐ-07 |
| Bảng 11, xóa dòng 12 | NguongPheDuyetNganSach \| tyLeNguong, capDuoiNguong, capTrenNguong \| 10%; Quản lý danh mục; CEO/MD. |  | Ngưỡng giữ ở dạng quy tắc (QĐ-19) |
| Bảng 11, xóa dòng 15 | NguoiDung \| maNguoiDung, hoTen, vaiTro \| vaiTro: PM, TaiChinh. |  | Bỏ NguoiDung |
| Bảng 12, dòng 1 |  | ChiTietBoTri \| (giữ) \| (giữ) | Khớp sơ đồ lớp II.3 (Hình II.3-5) |
| Bảng 12, dòng 7 |  | (giữ) \| kiemTraTienDieuKien(), danhDauThieuDuLieu(), doiChieuNganSach(), xacDinhTrangThai(), xacDinhCapXuLy() \| (giữ) | Gắn cấp xử lý, không phải phê duyệt |
| Bảng 12, xóa dòng 8 | NguongPheDuyetNganSach \| xacDinhCap(tyLeVuot) \| Trả cấp xử lý theo ngưỡng 10%. |  | Ngưỡng giữ ở dạng quy tắc (QĐ-19) |
| Bảng 13, xóa dòng 1 | PhuongAnBoTri \| Association \| CongViec \| Phương án gắn với phạm vi công việc (CN-103). |  | CongViec không là lớp riêng |
| Bảng 13, dòng 2 |  | (giữ) \| (giữ) \| ChiTietBoTri \| Dòng phương án không tồn tại khi thiếu phương án. | Khớp sơ đồ lớp II.3 (Hình II.3-5) |
| Bảng 13, dòng 3 |  | ChiTietBoTri \| (giữ) \| (giữ) \| Mỗi dòng phương án áp dụng một đơn giá. | Khớp sơ đồ lớp II.3 (Hình II.3-5) |
| Bảng 13, dòng 11 |  | DuAn \| (giữ) \| NganSach \| Ngân sách được duyệt cho dự án (QT-47). | Khớp sơ đồ lớp II.3 (Hình II.3-5) |
| Bảng 13, xóa dòng 15 | DanhGiaChiPhi \| Dependency \| NguongPheDuyetNganSach \| Chỉ tra ngưỡng khi xác định cấp, không lưu lâu dài. |  | Ngưỡng giữ ở dạng quy tắc (QĐ-19) |
| Bảng 13, xóa dòng 19 | NguoiDung (PM) \| Association \| DanhGiaChiPhi \| PM thực hiện đánh giá. |  | Bỏ NguoiDung |
| Bảng 13, xóa dòng 20 | NguoiDung (Tài chính) \| Association \| DonGia \| Tài chính cập nhật đơn giá (PCN-07). |  | Bỏ NguoiDung |
| Bảng 13, xóa dòng 21 | NguoiDung (Tài chính) \| Association \| ChiPhiThucTe \| Tài chính ghi nhận chi phí thực tế (PCN-07). |  | Bỏ NguoiDung |
| Bảng 13, xóa dòng 22 | NguoiDung \| Association \| DuBaoChiPhi \| Ghi lại tài khoản cập nhật dự báo (PCN-07). |  | Bỏ NguoiDung |
| Bảng 13, xóa dòng 23 | NguoiDung \| Association \| SoSanhPhuongAn \| Ghi lại tài khoản thực hiện so sánh. |  | Bỏ NguoiDung |
| Bảng 14, xóa dòng 1 | PhuongAnBoTri – CongViec \| * – 1..* \| Phương án gắn với phạm vi công việc (CN-103). |  | CongViec không là lớp riêng |
| Bảng 14, dòng 2 |  | PhuongAnBoTri – ChiTietBoTri \| (giữ) \| (giữ) | Khớp sơ đồ lớp II.3 (Hình II.3-5) |
| Bảng 14, dòng 3 |  | ChiTietBoTri – DonGia \| 0..* – 1 \| Mỗi dòng phương án áp dụng đúng một đơn giá. | Khớp sơ đồ lớp II.3 (Hình II.3-5) |
| Bảng 14, dòng 11 |  | DuAn – NganSach \| 1 – 0..* \| Ngân sách được duyệt cho dự án. | Khớp sơ đồ lớp II.3 (Hình II.3-5) |
| Bảng 14, xóa dòng 18 | NguoiDung (PM) – DanhGiaChiPhi \| 1 – 0..* \| PM thực hiện nhiều lần đánh giá. |  | Bỏ NguoiDung |
| Bảng 14, xóa dòng 19 | NguoiDung (Tài chính) – DonGia \| 1 – 0..* \| Tài chính cập nhật nhiều đơn giá. |  | Bỏ NguoiDung |
| Bảng 14, xóa dòng 20 | NguoiDung (Tài chính) – ChiPhiThucTe \| 1 – 0..* \| Tài chính ghi nhận nhiều khoản chi phí thực tế. |  | Bỏ NguoiDung |
| Bảng 14, xóa dòng 21 | NguoiDung – DuBaoChiPhi \| 1 – 0..* \| Một tài khoản cập nhật nhiều dự báo. |  | Bỏ NguoiDung |
| Bảng 14, xóa dòng 22 | NguoiDung – SoSanhPhuongAn \| 1 – 0..* \| Một tài khoản thực hiện nhiều lần so sánh. |  | Bỏ NguoiDung |
| Xóa đoạn 32 | PhuongAnBoTri Cost Management Framework-2026-10-14-161441.pdf tải về để xem rõ bản vẽ |  | Ghi chú tải file PDF, không thuộc nội dung báo cáo |
| Ảnh ở đoạn 35 |  | II3-5_Chi_phi_ngan_sach.png | Sơ đồ lớp theo mô hình thống nhất (Hình II.3-5, nguồn draw.io) |
