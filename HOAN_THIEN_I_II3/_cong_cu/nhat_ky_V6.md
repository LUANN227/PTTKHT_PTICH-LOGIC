## V6 — V6 - Phần II.docx

| Vị trí (theo bản gốc) | Trước | Sau | Lý do |
|---|---|---|---|
| Ảnh ở đoạn 11 |  | UCD_UC-05.png | Lỗi: UCD vùng chỉ có 05.1, association có mũi tên; dùng UCD vùng UC-05 (nguồn draw.io) |
| Bảng 4, dòng 6, cột 2 | Lưu phương án chính ở trạng thái "đang xây dựng". | Lưu phương án chính ở trạng thái "đang xây dựng"; bắt đầu tính thời hạn tối đa 3 ngày làm việc (CN-73, QT-31). | QĐ-13: CN-73 thuộc 05.1, theo dõi như một sự kiện của trạng thái |
| Bảng 5, dòng 5 |  | (giữ) \| Bước 9 \| Trước khi gửi PM, phương án đã ở trạng thái "đang xây dựng" quá 3 ngày làm việc \| RM ghi lý do và báo cáo PMO (CN-73, QT-31); tiếp tục bước 9. | QĐ-13: kiểm tra một lần như sự kiện theo dõi, không lặp ở mọi bước; thêm vào AD |
| Bảng 6, thêm sau dòng 12 |  | CN-73 \| Theo dõi thời hạn 3 ngày làm việc của phương án "đang xây dựng"; quá hạn thì ghi lý do, báo cáo PMO \| Bước 6, E1 | QĐ-13 |
| Đoạn 21 | Điểm bắt đầu: RM tiếp nhận nhu cầu và danh sách ứng viên khả dụng. Điểm kết thúc: PM nhận phương án để xem xét. | Điểm bắt đầu: RM tiếp nhận nhu cầu và danh sách ứng viên khả dụng, hoặc nhận phản hồi điều chỉnh từ UC-05.2 (A4). Điểm kết thúc: hệ thống ghi nhận việc gửi và chuyển phương án cho PM (sang UC-05.2). | Lỗi: 05.1 kết thúc ở gửi PM (CN-68); PM xác nhận thuộc 05.2 (CN-69) |
| Đoạn 22 | Swimlane: RM, Hệ thống, PM. | Swimlane: RM, Hệ thống. PM không có action trong UC-05.1. | Bỏ làn PM theo CN-68, CN-69 |
| Đoạn 23 | Decision: có ứng viên đáp ứng đầy đủ; có vị trí chỉ một ứng viên đạt; dự án gấp, chưa đủ thời gian. | Decision: bắt đầu từ phản hồi điều chỉnh (A4); có ứng viên đáp ứng đầy đủ (A3); có vị trí chỉ một ứng viên đạt (A1); dự án gấp, chưa đủ thời gian (A2); quá 3 ngày làm việc ở "đang xây dựng" (E1). | Theo AD vẽ lại |
| Ảnh ở đoạn 39 |  | AD_UC-05.1.png | AD vẽ lại bằng draw.io: bỏ decision “PM phê duyệt?”, A4 nối về trước bước 5, thêm E1 và bước 10 |
| Bảng 7, dòng 6, cột 0 | Các Alternative/Exceptional Flow trong UCD được thể hiện trên AD (A1 đến A3 bằng nhánh, A4 và E1 bằng ghi chú) | Các Alternative/Exceptional Flow trong UCD được thể hiện trên AD (A1 đến A4 và E1 bằng nhánh) | Theo AD vẽ lại |
| Bảng 8, 9, 10, 11, 12, 13, 14 | LichPhanBo, KhaNangThamGia | PhanBoNguonLuc, KetLuanKhaNangThamGia | Lỗi: lớp lịch thứ hai và trùng tên kết luận V5; dùng PhanBoNguonLuc, KetLuanKhaNangThamGia (II.3) (12 chỗ) |
| Bảng 10, dòng 7 |  | (giữ) \| Phân bổ hiện tại của nguồn lực (thuộc LichNguonLuc, V5) \| CN-61, V5, V10 | Lỗi: lớp lịch thứ hai và trùng tên kết luận V5; dùng PhanBoNguonLuc, KetLuanKhaNangThamGia (II.3) |
| Bảng 11, dòng 7 |  | (giữ) \| loaiPhanBo, tuNgay, denNgay, tyLe, trangThaiXacNhan \| Phân bổ cứng hoặc mềm hiện tại | Đồng bộ thuộc tính với II.3 |
| Bảng 11, dòng 8 |  | (giữ) \| trangThaiKhaNang, mucSuDung, thoiGianTrong, coRuiRoQuaTai \| Kết luận từ V5 | Đồng bộ thuộc tính với II.3 |
| Bảng 11, dòng 10 |  | (giữ) \| vaiTroDuocGan, tyLeThamGia, tuNgay, denNgay \| (giữ) | Đồng bộ thuộc tính với II.3 |
| Bảng 13, dòng 7 |  | (giữ) \| (giữ) \| HoSoNangLuc, LichNguonLuc \| Năng lực và lịch tổng hợp; phân bổ hiện tại nằm trong LichNguonLuc | Lỗi: lớp lịch thứ hai và trùng tên kết luận V5; dùng PhanBoNguonLuc, KetLuanKhaNangThamGia (II.3) |
| Bảng 13, dòng 8 |  | PhanBoNguonLuc \| (giữ) \| (giữ) \| (giữ) | Lỗi: lớp lịch thứ hai và trùng tên kết luận V5; dùng PhanBoNguonLuc, KetLuanKhaNangThamGia (II.3) |
| Bảng 14, dòng 8 |  | NguonLuc và LichNguonLuc; LichNguonLuc và PhanBoNguonLuc \| 1 và 1; 1 và 0..* \| Một lịch tổng hợp cho mỗi người (QĐ-05), gồm các phân bổ ở nhiều dự án | Lỗi: lớp lịch thứ hai và trùng tên kết luận V5; dùng PhanBoNguonLuc, KetLuanKhaNangThamGia (II.3) |
| Ảnh ở đoạn 60 |  | II3-4_Phuong_an_xung_dot_phe_duyet.png | Sơ đồ lớp theo mô hình thống nhất (Hình II.3-4, nguồn draw.io) |
