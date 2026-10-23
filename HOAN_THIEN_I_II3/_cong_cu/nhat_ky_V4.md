## V4 — V4 - Phần II.docx

| Vị trí (theo bản gốc) | Trước | Sau | Lý do |
|---|---|---|---|
| Ảnh ở đoạn 11 |  | UCD_UC-03.png | Lỗi: UCD vùng chỉ có 03.3; dùng UCD vùng UC-03 đủ 03.1–03.4 (nguồn draw.io). PMO giữ ở 03.3, 03.4 theo QĐ-01 |
| Bảng 3, dòng 9, cột 1 | Phân loại và lý do loại được lưu; không lập shortlist. Mở rộng nguồn ứng viên thuộc UC-03.2; phản hồi V2 (CN-46) cần nhóm chốt UC phụ trách. | Phân loại và lý do loại được lưu; không lập shortlist. RM quay lại UC-03.2 để mở rộng sang nguồn kế tiếp theo thứ tự ưu tiên (CN-33, QT-18); khi đã thử các nguồn mà vẫn không có ứng viên đáp ứng, RM phản hồi về V2 ở UC-03.2 (CN-46), PM nhận ở UC-01.3 (CN-17). | Lỗi: thiếu hướng xử lý khi không còn ứng viên; CN-46 thuộc UC-03.2 theo II.1 (QĐ-18) |
| Bảng 5, dòng 3, cột 2 | Kỹ năng ứng viên chưa xác nhận hoặc đã quá 6 tháng kể từ lần đánh giá gần nhất. | Kỹ năng ứng viên chưa xác nhận hoặc đã quá 6 tháng kể từ lần đánh giá gần nhất (chu kỳ đánh giá lại định kỳ 6 tháng, CN-20). | Lỗi căn cứ: QT-15 chỉ nói “quá thời hạn cập nhật”; mốc 6 tháng lấy từ CN-20 |
| Bảng 5, dòng 8, cột 3 | Không lập shortlist; lưu phân loại và lý do loại; UC kết thúc. | Không lập shortlist; lưu phân loại và lý do loại; UC kết thúc. RM tìm tiếp ở nguồn kế tiếp (UC-03.2, CN-33); đã thử các nguồn mà vẫn không có ứng viên thì phản hồi V2 (UC-03.2, CN-46). | Lỗi: thiếu hướng xử lý khi không còn ứng viên; CN-46 thuộc UC-03.2 theo II.1 (QĐ-18) |
| Bảng 6, dòng 13, cột 1 | Cảnh báo độ tin cậy kỹ năng; quá hạn là quá 6 tháng. | Cảnh báo kỹ năng chưa xác nhận hoặc quá thời hạn cập nhật; mốc 6 tháng theo chu kỳ đánh giá lại định kỳ ở CN-20. | Lỗi căn cứ mốc 6 tháng |
| Bảng 6, thêm sau dòng 16 |  | CN-33, CN-46 \| Tìm theo thứ tự ưu tiên nguồn; phản hồi V2 khi đã thử các cách mà vẫn không có ứng viên (thuộc UC-03.2). \| E3 | Lỗi: thiếu hướng xử lý khi không còn ứng viên; CN-46 thuộc UC-03.2 theo II.1 (QĐ-18) |
| Đoạn 28 | Decision: đủ tiền điều kiện (E1, E2); cần miễn trừ ứng viên (A2); còn ứng viên đủ điều kiện (E3). | Decision: đủ tiền điều kiện (E1, E2); cần miễn trừ ứng viên (A2); còn ứng viên đủ điều kiện (E3). Merge: trước decision “còn ứng viên đủ điều kiện?”, hợp nhất nhánh không cần miễn trừ và nhánh sau khi PMO xử lý đề nghị miễn trừ. | Lỗi ký pháp: hai luồng vào thẳng một decision |
| Đoạn 29 | Điểm kết thúc: kết thúc sớm tại E1/E2 và E3; kết thúc chính sau khi lưu kết quả. | Điểm kết thúc: kết thúc sớm tại E1/E2 và E3 (lưu phân loại, RM tìm tiếp ở UC-03.2); kết thúc chính sau khi lưu kết quả. | Lỗi: thiếu hướng xử lý khi không còn ứng viên; CN-46 thuộc UC-03.2 theo II.1 (QĐ-18) |
| Ảnh ở đoạn 33 |  | AD_UC-03.3.png | AD vẽ lại bằng draw.io: tiêu đề theo tên UC, thêm merge trước decision, nhánh E3 rõ hướng xử lý |
| Bảng 8, 9, 10, 11, 12, 13, 14 | BoTieuChi, TieuChi, PhienDanhGia, KetQuaDanhGia, UngVien, KyNang | BoTieuChiPhuHop, TieuChiPhuHop, PhienTimKiem, KetQuaDanhGiaPhuHop, NguonLuc, NangLucKyNang | Lỗi: tên lớp trùng V3, V5; đồng bộ với II.3 (Hình II.3-3), ứng viên là NguonLuc, kỹ năng tham chiếu NangLucKyNang của V3 (66 chỗ) |
| Bảng 8, dòng 11 |  | (giữ) \| Không \| Là thuộc tính vaiTroShortlist (Chinh, ThayThe) của KetQuaDanhGiaPhuHop. | Shortlist là thuộc tính theo II.3 |
| Bảng 8, dòng 12 |  | (giữ) \| Không \| Tác nhân; người thực hiện, người phê duyệt là thuộc tính của DeNghiMienTru (nguoiPheDuyet, PCN-07). | Actor không phải lớp miền |
| Bảng 9, dòng 6 |  | (giữ) \| (giữ) \| Gán vaiTroShortlist (Chinh, ThayThe) cho các kết quả đủ điều kiện. | Shortlist là thuộc tính theo II.3 |
| Bảng 11, dòng 5 |  | (giữ) \| maNguonLuc, hoTen, loaiNguon \| loaiNguon: NoiBo, CongTacVienDoiTac, TuyenNgoai (QĐ-14); xung đột lợi ích ghi ở KetQuaDanhGiaPhuHop.coXungDotLoiIch. | Đồng bộ thuộc tính với II.3 |
| Bảng 10, xóa dòng 10 | Shortlist \| Danh sách chính và thay thế \| CN-41, QT-17 |  | Shortlist là thuộc tính vaiTroShortlist |
| Bảng 10, xóa dòng 11 | NguoiDung \| RM hoặc PMO thao tác \| PCN-07, QT-13 |  | Bỏ lớp NguoiDung: actor không phải lớp miền |
| Bảng 10, dòng 6 |  | NangLucKyNang \| Kỹ năng, mức thành thạo, trạng thái xác nhận của nguồn lực (lấy từ hồ sơ năng lực V3) \| CN-30, CN-36, QT-15 | Kỹ năng ứng viên tham chiếu hồ sơ năng lực V3 |
| Bảng 11, dòng 1 |  | (giữ) \| maNhuCau, phamViCongViec, thoiGianBatDau, thoiGianKetThuc, trangThai \| Nhu cầu từ V2; loại nguồn lực, quy mô, %FTE thuộc ViTriCanBoTri (II.3). | Đồng bộ thuộc tính với II.3 |
| Bảng 11, dòng 6 |  | (giữ) \| mucThanhThao, trangThaiXacNhan, ngayDanhGia, canCuXacNhan \| mucThanhThao thang 1 đến 5; quá 6 tháng kể từ ngayDanhGia thì cảnh báo (CN-20, CN-36). | Đồng bộ thuộc tính với II.3; sửa căn cứ mốc 6 tháng |
| Bảng 11, dòng 7 |  | (giữ) \| phanLoai, lyDoKhongDat, diemTong, thuHang, vaiTroShortlist, mucDapUng, khoangThieuNangLuc, coXungDotLoiIch \| (giữ) | Đồng bộ thuộc tính với II.3 (QĐ-15) |
| Bảng 11, dòng 9 |  | (giữ) \| lyDo, trangThai, nguoiPheDuyet, thoiDiemQuyetDinh \| (giữ) | Ghi người phê duyệt (QT-13, PCN-07) thay lớp NguoiDung |
| Bảng 11, xóa dòng 10 | Shortlist \| maShortlist, ngayLap \|   |  | Shortlist là thuộc tính |
| Bảng 11, xóa dòng 11 | NguoiDung \| maNguoiDung, hoTen, vaiTro \| vaiTro: RM, PMO. |  | Bỏ lớp NguoiDung |
| Bảng 12, xóa dòng 6 | Shortlist \| themUngVien(vaiTro) \| Gán ứng viên chính hoặc thay thế. |  | Shortlist là thuộc tính |
| Bảng 13, xóa dòng 4 | NguoiDung (RM) \| Association \| PhienTimKiem \| RM thực hiện phiên. |  | Bỏ lớp NguoiDung |
| Bảng 13, dòng 7 |  | (giữ) \| (giữ) \| (giữ) \| Kỹ năng của nguồn lực lấy từ hồ sơ năng lực V3 (HoSoNangLuc). | Không gắn kỹ năng trực tiếp vào ứng viên |
| Bảng 13, xóa dòng 11 | NguoiDung (PMO) \| Association \| DeNghiMienTru \| PMO phê duyệt. |  | Bỏ lớp NguoiDung |
| Bảng 13, xóa dòng 12 | PhienTimKiem \| Association \| Shortlist \| Phiên tạo shortlist. |  | Shortlist là thuộc tính |
| Bảng 13, xóa dòng 13 | Shortlist \| Association \| KetQuaDanhGiaPhuHop \| Shortlist gồm các kết quả được chọn. |  | Shortlist là thuộc tính |
| Bảng 14, xóa dòng 4 | NguoiDung (RM) – PhienTimKiem \| 1 – 0..* \| RM thực hiện nhiều phiên. |  | Bỏ lớp NguoiDung |
| Bảng 14, xóa dòng 11 | NguoiDung (PMO) – DeNghiMienTru \| 1 – 0..* \| PMO phê duyệt nhiều đề nghị. |  | Bỏ lớp NguoiDung |
| Bảng 14, xóa dòng 12 | PhienTimKiem – Shortlist \| 1 – 0..1 \| Không có shortlist khi không có ứng viên đạt. |  | Shortlist là thuộc tính |
| Bảng 14, xóa dòng 13 | Shortlist – KetQuaDanhGiaPhuHop \| 0..1 – 1..* \| Shortlist có tối thiểu một ứng viên chính (QT-17). |  | Shortlist là thuộc tính |
| Ảnh ở đoạn 56 |  | II3-3_Tim_kiem_kha_nang_tham_gia_lich.png | Sơ đồ lớp theo mô hình thống nhất (Hình II.3-3, nguồn draw.io) |
