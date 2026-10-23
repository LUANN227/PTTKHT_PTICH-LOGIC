## V5 — NV05 I2 - I3.docx

| Vị trí (theo bản gốc) | Trước | Sau | Lý do |
|---|---|---|---|
| Bảng 0, dòng 4, cột 1 | Đánh giá năng lực khả dụng của nguồn lực  | Đánh giá khả năng tham gia | Thống nhất một tên UC theo II.1 |
| Xóa đoạn 9 | Vẽ Use Case Diagram chi tiết cho UC được giao, thể hiện: |  | Xóa chữ mẫu của biểu mẫu |
| Xóa đoạn 11 | Actor |  | Xóa chữ mẫu của biểu mẫu |
| Xóa đoạn 12 | Use Case |  | Xóa chữ mẫu của biểu mẫu |
| Xóa đoạn 13 | Association |  | Xóa chữ mẫu của biểu mẫu |
| Xóa đoạn 14 | <<include>> / <<extend>> nếu thực sự có |  | Xóa chữ mẫu của biểu mẫu |
| Xóa đoạn 15 | Ranh giới hệ thống |  | Xóa chữ mẫu của biểu mẫu |
| Xóa đoạn 34 | Vẽ Activity Diagram tương ứng với Use Case Description. |  | Xóa chữ mẫu của biểu mẫu |
| Xóa đoạn 35 | AD phải thể hiện được: |  | Xóa chữ mẫu của biểu mẫu |
| Xóa đoạn 36 | Luồng chính |  | Xóa chữ mẫu của biểu mẫu |
| Xóa đoạn 37 | Luồng thay thế |  | Xóa chữ mẫu của biểu mẫu |
| Xóa đoạn 38 | Luồng ngoại lệ |  | Xóa chữ mẫu của biểu mẫu |
| Xóa đoạn 39 | Các điều kiện rẽ nhánh tương ứng với Description. |  | Xóa chữ mẫu của biểu mẫu |
| Ảnh ở đoạn 10 |  | UCD_UC-04.png | Lỗi: tiêu đề “PHÂN HỆ V5”, RM chỉ nối 04.1; dùng UCD vùng UC-04 (nguồn draw.io) |
| Bảng 3, dòng 6, cột 1 | RM tiếp nhận yêu cầu nguồn lực có khung thời gian và shortlist đã được xác định từ V4.  | PM gửi yêu cầu nguồn lực của dự án mới hoặc dự án mở rộng phạm vi, kèm khung thời gian (CN-127); RM tiếp nhận cùng shortlist từ V4 (CN-47). | QĐ-11: giữ CN-127 là đầu vào của 04.1 |
| Bảng 3, dòng 8, cột 1 | Kết quả đánh giá và căn cứ được ghi nhận theo từng ứng viên. Kết quả thông thường được bàn giao V6; xung đột phân bổ cứng được chuyển V7; trường hợp tham gia một phần hoặc vượt tải ngoại lệ được chuyển sang luồng xử lý tương ứng. Hồ sơ chưa đủ căn cứ vẫn giữ trạng thái chờ xác nhận.  | Kết luận và căn cứ được ghi nhận cho từng ứng viên trong shortlist. Kết luận đáp ứng đầy đủ được bàn giao V6, cờ rủi ro quá tải Mức 2 đi kèm sang V6 và V10; xung đột phân bổ cứng chuyển V7; đáp ứng một phần chuyển UC-04.2; vượt tải ngoại lệ chuyển UC-04.3. Ứng viên có dữ liệu chưa đủ rõ giữ trạng thái chờ xác nhận, không bàn giao như kết luận đủ căn cứ. | Bổ sung đích của cờ Mức 2 (CN-50) |
| Bảng 4, dòng 1 |  | 1 \| RM \| Tiếp nhận yêu cầu nguồn lực, khung thời gian và shortlist ứng viên đã qua V4 (CN-47, CN-127). Yêu cầu gấp thì xử lý theo A6. | Lỗi: D xét từng ứng viên nhưng không có vòng lặp; mọi nhánh phải qua ghi nhận kết luận (CN-51) rồi mới rẽ; đánh số lại cho trùng AD |
| Bảng 4, dòng 2 |  | 2 \| Hệ thống \| Kiểm tra tính đầy đủ của yêu cầu và shortlist. Thiếu thông tin cần thiết thì chuyển A1. | Lỗi: D xét từng ứng viên nhưng không có vòng lặp; mọi nhánh phải qua ghi nhận kết luận (CN-51) rồi mới rẽ; đánh số lại cho trùng AD |
| Bảng 4, dòng 3 |  | 3 \| Hệ thống \| Với từng ứng viên: tra cứu năng lực chuẩn, lịch, thời gian nghỉ, phân bổ cứng và phân bổ mềm trong khung thời gian; kiểm tra độ mới, độ rõ của dữ liệu (CN-48). Dữ liệu chưa đủ rõ thì chuyển A2. | Lỗi: D xét từng ứng viên nhưng không có vòng lặp; mọi nhánh phải qua ghi nhận kết luận (CN-51) rồi mới rẽ; đánh số lại cho trùng AD |
| Bảng 4, dòng 4 |  | 4 \| RM \| Xác định năng lực khả dụng thực tế: năng lực chuẩn trừ thời gian nghỉ, thời gian không tính phí và phân bổ cứng (CN-49, QT-21). | Lỗi: D xét từng ứng viên nhưng không có vòng lặp; mọi nhánh phải qua ghi nhận kết luận (CN-51) rồi mới rẽ; đánh số lại cho trùng AD |
| Bảng 4, dòng 5 |  | 5 \| RM \| Đối chiếu mức sử dụng với ngưỡng bền vững 70–85%; trên 85% thì xem riêng phần đang chờ xác nhận; trên 90% kéo dài liên tục trên 2 tuần thì gắn cờ rủi ro quá tải Mức 2. Cờ đi kèm kết luận sang V6, V10 và không tự kích hoạt V7 (CN-50, QT-22). | Lỗi: D xét từng ứng viên nhưng không có vòng lặp; mọi nhánh phải qua ghi nhận kết luận (CN-51) rồi mới rẽ; đánh số lại cho trùng AD |
| Bảng 4, dòng 6 |  | 6 \| RM \| Ghi nhận kết luận theo một trong bốn trạng thái: đáp ứng đầy đủ, đáp ứng một phần, không thể tham gia, chờ xác nhận; kèm căn cứ đánh giá (CN-51). | Lỗi: D xét từng ứng viên nhưng không có vòng lặp; mọi nhánh phải qua ghi nhận kết luận (CN-51) rồi mới rẽ; đánh số lại cho trùng AD |
| Bảng 4, dòng 7 |  | 7 \| Hệ thống \| Lưu kết luận và căn cứ của ứng viên. Còn ứng viên trong shortlist thì quay lại bước 3. | Lỗi: D xét từng ứng viên nhưng không có vòng lặp; mọi nhánh phải qua ghi nhận kết luận (CN-51) rồi mới rẽ; đánh số lại cho trùng AD |
| Bảng 4, dòng 8 |  | 8 \| RM \| Tổng hợp kết luận của từng ứng viên để bàn giao (CN-59). | Lỗi: D xét từng ứng viên nhưng không có vòng lặp; mọi nhánh phải qua ghi nhận kết luận (CN-51) rồi mới rẽ; đánh số lại cho trùng AD |
| Bảng 4, thêm sau dòng 8 |  | 9 \| Hệ thống \| Chuyển hồ sơ theo kết luận: đáp ứng đầy đủ sang V6; trùng phân bổ cứng sang V7 (A3); đáp ứng một phần sang UC-04.2 (A4); vượt tải ngoại lệ sang UC-04.3 (A5). | Lỗi: D xét từng ứng viên nhưng không có vòng lặp; mọi nhánh phải qua ghi nhận kết luận (CN-51) rồi mới rẽ; đánh số lại cho trùng AD |
| Bảng 5, dòng 1 |  | (giữ) \| 2 \| (giữ) \| (giữ) | Đánh số theo D đã sửa |
| Bảng 5, dòng 2 |  | (giữ) \| 3 \| (giữ) \| Gắn nhãn “dữ liệu chưa đủ rõ”. RM chọn: chờ xác nhận trong 2 ngày làm việc; hoặc không chờ thì coi như chưa có dữ liệu và yêu cầu xác nhận ngay (CN-52, QT-24). Kết luận của ứng viên là “chờ xác nhận”, không bàn giao như kết luận đủ căn cứ; tiếp tục bước 6. | Lỗi: thiếu nhánh “không chờ” theo CN-52; bỏ mã BR-V5-08 |
| Bảng 5, dòng 3 |  | (giữ) \| 9 \| (giữ) \| RM ghi nhận xung đột trong kết luận; ở bước 9 hồ sơ xung đột được chuyển V7 (CN-55, QT-26). V5 không quyết định ưu tiên giữa các dự án. | Rẽ nhánh sau khi đã ghi nhận kết luận (CN-51) |
| Bảng 5, dòng 4 |  | (giữ) \| 9 \| Kết luận đáp ứng một phần \| Chuyển UC-04.2: RM đề xuất tỷ lệ phân bổ và khung thời gian (CN-53); PM xác nhận hoặc không xác nhận phân bổ một phần là không ảnh hưởng nghiêm trọng; không xác nhận thì RM ghi nhận từ chối kèm hướng xử lý (CN-54, QT-23). | Rẽ nhánh sau khi đã ghi nhận kết luận (CN-51) |
| Bảng 5, dòng 5 |  | (giữ) \| 9 \| Vượt tải ngoại lệ: nguồn lực quan trọng bị nhiều phần giữ chỗ mềm cùng khóa \| Chuyển UC-04.3 theo Ma trận phân quyền: PMO/Quản lý danh mục phê duyệt Mức 2–3, CEO/Managing Director khi chạm Mức 4–5 (CN-56, CN-57, QT-25). | Ghi điều kiện theo CN-56; rẽ nhánh sau khi đã ghi nhận kết luận |
| Bảng 5, dòng 6 |  | (giữ) \| 1 \| Yêu cầu gấp có thời hạn dưới 24–48 giờ \| RM đánh giá nhanh dựa trên phân bổ cứng, ghi nhận rủi ro và tiếp tục theo dõi (CN-58); UC kết thúc. | QĐ-04: ghi đúng như Phần I, không tự chọn 24 hay 48 giờ |
| Bảng 6, dòng 1 |  | QT-20, CN-59 \| (giữ) \| (giữ) | Lỗi: mã BR-V5 không tra được trong Phần I; đổi theo mã QT/CN của Phần I |
| Bảng 6, dòng 2 |  | QT-26, CN-55 \| (giữ) \| (giữ) | Lỗi: mã BR-V5 không tra được trong Phần I; đổi theo mã QT/CN của Phần I |
| Bảng 6, dòng 3 |  | QT-21, CN-49 \| (giữ) \| (giữ) | Lỗi: mã BR-V5 không tra được trong Phần I; đổi theo mã QT/CN của Phần I |
| Bảng 6, dòng 4 |  | QT-22, CN-50 \| (giữ) \| (giữ) | Lỗi: mã BR-V5 không tra được trong Phần I; đổi theo mã QT/CN của Phần I |
| Bảng 6, dòng 5 |  | CN-50 \| (giữ) \| (giữ) | Lỗi: mã BR-V5 không tra được trong Phần I; đổi theo mã QT/CN của Phần I |
| Bảng 6, dòng 6 |  | QT-22, CN-50 \| Mức sử dụng trên 90% kéo dài liên tục trên 2 tuần được gắn cờ rủi ro quá tải Mức 2; cờ đi kèm kết luận sang V6, V10 và không tự kích hoạt V7. \| (giữ) | Lỗi: mã BR-V5 không tra được trong Phần I; đổi theo mã QT/CN của Phần I |
| Bảng 6, dòng 7 |  | QT-24, CN-52 \| (giữ) \| (giữ) | Lỗi: mã BR-V5 không tra được trong Phần I; đổi theo mã QT/CN của Phần I |
| Bảng 6, dòng 8 |  | CN-52 \| Nếu không chờ xác nhận thì coi như chưa có dữ liệu và yêu cầu xác nhận ngay. \| (giữ) | Lỗi: mã BR-V5 không tra được trong Phần I; đổi theo mã QT/CN của Phần I |
| Bảng 6, dòng 9 |  | QT-23, CN-53, CN-54 \| (giữ) \| (giữ) | Lỗi: mã BR-V5 không tra được trong Phần I; đổi theo mã QT/CN của Phần I |
| Bảng 6, dòng 10 |  | QT-25, CN-56, CN-57 \| (giữ) \| (giữ) | Lỗi: mã BR-V5 không tra được trong Phần I; đổi theo mã QT/CN của Phần I |
| Bảng 6, dòng 11 |  | CN-58 \| Yêu cầu gấp có thời hạn dưới 24–48 giờ được đánh giá nhanh dựa trên phân bổ cứng, ghi nhận rủi ro và tiếp tục theo dõi. \| (giữ) | Lỗi: mã BR-V5 không tra được trong Phần I; đổi theo mã QT/CN của Phần I |
| Bảng 7, dòng 4, cột 1 | Đủ thông tin? Dữ liệu đủ rõ/đủ mới? Có xung đột phân bổ cứng? Đáp ứng một phần? Có vượt tải ngoại lệ?  | Yêu cầu gấp? (A6) · Đủ thông tin? (A1) · Dữ liệu đủ rõ? (A2) · Chờ xác nhận? (A2: chờ hoặc không chờ) · Còn ứng viên cần đánh giá? (vòng lặp từng ứng viên). Merge: trước bước 2, trước bước 3 (vòng lặp), trước bước 6. | Lỗi: D xét từng ứng viên nhưng không có vòng lặp; mọi nhánh phải qua ghi nhận kết luận (CN-51) rồi mới rẽ; đánh số lại cho trùng AD |
| Bảng 7, dòng 6, cột 1 | Theo A1–A6 tại mục 3.3 và BR-V5-01 đến BR-V5-14 tại mục 3.4  | Theo A1–A6 tại mục 3.3 và QT-20–QT-26, CN-47–CN-59 tại mục 3.4 | Lỗi: mã BR-V5 không tra được trong Phần I; đổi theo mã QT/CN của Phần I |
| Bảng 7, dòng 7, cột 1 | Kết quả được lưu và bàn giao; hoặc hồ sơ được chuyển nhánh; trường hợp dữ liệu chưa rõ kết thúc ở trạng thái chờ xác nhận, không được coi là kết quả đánh giá hoàn tất  | Sau khi chuyển hồ sơ theo kết luận (bước 9); hoặc sau đánh giá nhanh yêu cầu gấp (A6). | Theo AD vẽ lại: mọi nhánh kết thúc bằng final node |
| Ảnh ở đoạn 40 |  | AD_UC-04.1.png | AD vẽ lại bằng draw.io: action RM ở làn RM, có vòng lặp ứng viên, đủ hai nhánh A2, rẽ nhánh sau ghi nhận kết luận |
| Bảng 8, dòng 5, cột 0 | Khớp các quy tắc nghiệp vụ BR-V5-01 đến BR-V5-14 | Khớp các quy tắc QT-20–QT-26, CN-47–CN-59 | Lỗi: mã BR-V5 không tra được trong Phần I; đổi theo mã QT/CN của Phần I |
| Bảng 10, 11, 12, 13, 14, 15 | KetQuaDanhGia | KetLuanKhaNangThamGia | Lỗi: KetQuaDanhGia trùng tên lớp kết quả của V4; đồng bộ với II.3 (Hình II.3-3) (18 chỗ) |
| Bảng 9, dòng 6 |  | (giữ) \| Không \| Ngày yêu cầu, hạn xác nhận (2 ngày làm việc) và lý do chờ là thuộc tính của KetLuanKhaNangThamGia. | II.3 không giữ lớp YeuCauXacNhan: ngày yêu cầu, hạn xác nhận, lý do chờ là thuộc tính của KetLuanKhaNangThamGia |
| Bảng 10, dòng 6 |  | (giữ) \| KetLuanKhaNangThamGia \| Theo dõi hạn xác nhận 2 ngày làm việc (CN-52). | II.3 không giữ lớp YeuCauXacNhan: ngày yêu cầu, hạn xác nhận, lý do chờ là thuộc tính của KetLuanKhaNangThamGia |
| Bảng 11, dòng 1, cột 2 | CN-V5-01; nghiệp vụ V5 | QĐ-11; CN-47, CN-127 | Lỗi: mã BR-V5 không tra được trong Phần I; đổi theo mã QT/CN của Phần I |
| Bảng 11, dòng 2, cột 2 | CN-V5-02/03; C-V5-01 | CN-48, CN-49 | Lỗi: mã BR-V5 không tra được trong Phần I; đổi theo mã QT/CN của Phần I |
| Bảng 11, dòng 3, cột 2 | CN-V5-02; BR-V5-07/08 | CN-48, CN-52; QT-24 | Lỗi: mã BR-V5 không tra được trong Phần I; đổi theo mã QT/CN của Phần I |
| Bảng 11, dòng 4, cột 2 | CN-V5-02/03; BR-V5-02/05 | CN-48, CN-55 | Lỗi: mã BR-V5 không tra được trong Phần I; đổi theo mã QT/CN của Phần I |
| Bảng 11, dòng 5, cột 2 | CN-V5-04/05/10 | CN-50, CN-51, CN-59 | Lỗi: mã BR-V5 không tra được trong Phần I; đổi theo mã QT/CN của Phần I |
| Bảng 11, dòng 7, cột 2 | CN-V5-07; BR-V5-09 đến BR-V5-11 | CN-53, CN-54; QT-23 | Lỗi: mã BR-V5 không tra được trong Phần I; đổi theo mã QT/CN của Phần I |
| Bảng 11, dòng 8, cột 2 | CN-V5-09; BR-V5-12/13 | CN-56, CN-57; QT-25 | Lỗi: mã BR-V5 không tra được trong Phần I; đổi theo mã QT/CN của Phần I |
| Bảng 11, xóa dòng 6 | YeuCauXacNhan \| Theo dõi dữ liệu chưa rõ/chờ xác nhận; là lớp đề xuất nếu cần quản lý vòng đời xác nhận. \| CN-V5-06; BR-V5-07/08 |  | II.3 không giữ lớp YeuCauXacNhan: ngày yêu cầu, hạn xác nhận, lý do chờ là thuộc tính của KetLuanKhaNangThamGia |
| Bảng 12, dòng 5 |  | (giữ) \| trangThaiKhaNang, mucSuDung, thoiGianTrong, coRuiRoQuaTai, ngayYeuCauXacNhan, hanXacNhan, lyDoChoXacNhan, canCuDanhGia \| Kết luận, cờ rủi ro Mức 2, theo dõi chờ xác nhận và căn cứ. | Đồng bộ thuộc tính với II.3; nhận thuộc tính của YeuCauXacNhan |
| Bảng 12, xóa dòng 6 | YeuCauXacNhan \| maYeuCauXN, lyDo, ngayTao, hanXacNhan, trangThai \| Theo dõi yêu cầu xác minh và hạn xác nhận. |  | II.3 không giữ lớp YeuCauXacNhan: ngày yêu cầu, hạn xác nhận, lý do chờ là thuộc tính của KetLuanKhaNangThamGia |
| Bảng 13, dòng 10 |  | KetLuanKhaNangThamGia \| capNhatTrangThaiXacNhan() \| (giữ) | II.3 không giữ lớp YeuCauXacNhan: ngày yêu cầu, hạn xác nhận, lý do chờ là thuộc tính của KetLuanKhaNangThamGia |
| Bảng 14, dòng 3 |  | (giữ) \| (giữ) \| (giữ) \| Mỗi nguồn lực có một lịch tổng hợp hiện hành. | QĐ-05: NguonLuc–LichNguonLuc 1–1 |
| Bảng 14, xóa dòng 5 | KetLuanKhaNangThamGia \| Association \| YeuCauXacNhan \| Kết quả có thể có các yêu cầu xác nhận gắn kèm; giữ lớp riêng nếu hệ thống lưu vòng đời xác nhận. |  | II.3 không giữ lớp YeuCauXacNhan: ngày yêu cầu, hạn xác nhận, lý do chờ là thuộc tính của KetLuanKhaNangThamGia |
| Bảng 15, dòng 3 |  | (giữ) \| 1 — 1 \| Mỗi nguồn lực có một lịch tổng hợp hiện hành (QĐ-05). | QĐ-05: NguonLuc–LichNguonLuc 1–1 |
| Bảng 15, xóa dòng 5 | KetLuanKhaNangThamGia — YeuCauXacNhan \| 1 — 0..*  \| Một kết quả có thể phát sinh nhiều yêu cầu xác minh.  |  | II.3 không giữ lớp YeuCauXacNhan: ngày yêu cầu, hạn xác nhận, lý do chờ là thuộc tính của KetLuanKhaNangThamGia |
| Bảng 15, dòng 6 |  | (giữ) \| 1 — 0..* \| Một kết luận có thể có nhiều lần đề xuất một phần khi PM không xác nhận. | Lỗi: bảng để hai lựa chọn; chọn theo II.3 |
| Bảng 15, dòng 7 |  | (giữ) \| 1 — 0..* \| Kết luận bình thường không có hồ sơ vượt tải; một kết luận có thể có nhiều lần chuyển cấp. | Lỗi: bảng để hai lựa chọn; chọn theo II.3 |
| Đoạn 61 | 11. Xác định multiplicity12. Domain/Class Diagram đề xuất | 11. Xác định multiplicity | Lỗi: tiêu đề mục 11 dính mục 12 |
| Xóa đoạn 64 | Vẽ Domain/Class Diagram trong phạm vi UC được giao, làm cơ sở cho phần mô hình hóa cấu trúc tĩnh II.3. |  | Xóa chữ mẫu |
| Thêm sau đoạn 64 |  | 12. Domain/Class Diagram đề xuất | Tách mục 12 |
| Ảnh ở đoạn 65 |  | II3-3_Tim_kiem_kha_nang_tham_gia_lich.png | Sơ đồ lớp theo mô hình thống nhất (Hình II.3-3, nguồn draw.io): bội số đặt đúng đầu |
