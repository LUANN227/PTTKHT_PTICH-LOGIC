## V8 — MNV8 - Ngọc Linh.docx

| Vị trí (theo bản gốc) | Trước | Sau | Lý do |
|---|---|---|---|
| Bảng 1, dòng 4, cột 1 | RM (người lập phương án) | Không có trong UC-07.1. RM chỉ tham gia ở UC-07.2 Yêu cầu giải trình và hoàn thiện phương án (CN-96) | UCD_UC-07: RM chỉ nối với UC-07.2; CN-89–94 không có RM |
| Bảng 1, dòng 5, cột 1 | UC-05 (V6), UC-06 (V7), UC-08 (V9 - Chi phí), UC-09 (V10 - Dự báo) | UC-07.2 (extend); UC-07.3, UC-07.4 (bước quyết định sau rà soát). Dữ liệu tham chiếu: hồ sơ từ UC-05 (V6), UC-06 (V7); thông tin từ UC-08 (V9), UC-09 (V10) | V9, V10 là nguồn dữ liệu tham chiếu, không phải UC được include |
| Bảng 2, xóa dòng 1 | UC-07.1 \| <<include>> \| UC-08 (V9) \| Khi thực hiện rà soát và đánh giá phương án, hệ thống bắt buộc phải tích hợp dữ liệu chi phí và chênh lệch ngân sách từ V9 (chạy song song)  |  | Bỏ include: V9, V10 là dữ liệu tham chiếu (CN-93, CN-94); 07.1 không include 07.3 |
| Bảng 2, xóa dòng 2 | UC-07.1 \| <<include>>  \| UC-09 (V10) \| Khi rà soát, hệ thống bắt buộc tra cứu thông tin tổng hợp cung - cầu và kết quả dự báo từ V10 |  | Bỏ include: V9, V10 là dữ liệu tham chiếu (CN-93, CN-94); 07.1 không include 07.3 |
| Bảng 2, xóa dòng 3 | UC-07.1 \| <<include>> \| UC-07.3 \| Khi cấp thẩm quyền (PMO đối với Mức 1–3) xác nhận hồ sơ đã đủ cơ sở ra quyết định  |  | Bỏ include: V9, V10 là dữ liệu tham chiếu (CN-93, CN-94); 07.1 không include 07.3 |
| Bảng 2, dòng 4 |  | UC-07.2 \| (giữ) \| UC-07.1 \| (giữ) | Sửa UC đích: 07.2 mở rộng 07.1 (UCD_UC-07) |
| Xóa đoạn 9 | Vẽ Use Case Diagram chi tiết cho UC được giao, thể hiện: |  | Bỏ chữ hướng dẫn của mẫu |
| Xóa đoạn 10 | Actor |  | Bỏ chữ hướng dẫn của mẫu |
| Xóa đoạn 11 | Use Case |  | Bỏ chữ hướng dẫn của mẫu |
| Xóa đoạn 12 | Association |  | Bỏ chữ hướng dẫn của mẫu |
| Xóa đoạn 13 | <<include>> / <<extend>> nếu thực sự có |  | Bỏ chữ hướng dẫn của mẫu |
| Xóa đoạn 14 | Ranh giới hệ thống |  | Bỏ chữ hướng dẫn của mẫu |
| Thêm ảnh sau đoạn 8 |  | UCD_UC-07.png | Bài chưa có hình UCD; dùng UCD vùng UC-07 (nguồn draw.io), có 07.4, không có UC ngoài vùng |
| Bảng 3, dòng 5, cột 1 | RM (Người lập phương án) | Không có trong UC-07.1. RM chỉ tham gia ở UC-07.2 Yêu cầu giải trình và hoàn thiện phương án (CN-96) | Như bảng 2.1 |
| Bảng 4, dòng 4 |  | (giữ) \| (giữ) \| Hiển thị thông tin chi phí, chênh lệch ngân sách và đánh đổi từ V9; thông tin tổng hợp cung – cầu và kết quả dự báo từ V10 để cấp thẩm quyền xem cùng hồ sơ. \| (giữ) | Bỏ «include»: đây là xem dữ liệu V9, V10 (CN-93, CN-94) |
| Bảng 4, dòng 5 |  | (giữ) \| (giữ) \| Cấp thẩm quyền đánh giá các yếu tố rủi ro và kết luận hồ sơ đủ hay chưa đủ cơ sở ra quyết định. Chưa đủ: luồng A2. \| (giữ) | Bước 5 là điểm rẽ nhánh; quyết định chính thức thuộc UC-07.3, 07.4 (CN-97) |
| Bảng 5, dòng 1, cột 4 | CN-91; Hoạt động 1; DoA (Chuyển cấp)  | CN-91; QT-41, QT-42; Hoạt động 1 | Thêm mã quy tắc của P1 cho ngưỡng và hạn chuyển cấp |
| Bảng 5, dòng 2 |  | (giữ) \| (giữ) \| Cấp thẩm quyền phát hiện điểm bất hợp lý, rủi ro hoặc thiếu thông tin, kết luận hồ sơ chưa đủ cơ sở ra quyết định \| 1. Cấp thẩm quyền lập danh sách nội dung cần giải trình, bổ sung gửi RM là người đề xuất phương án.<br>2. Hệ thống chuyển hồ sơ sang UC-07.2 (extend). UC-07.1 kết thúc.<br>Việc RM giải trình, cập nhật hồ sơ và nhánh sau giải trình (rà soát lại hoặc trả về V6/V7) đư… | 07.1 không có action của RM; A2 dừng ở chuyển UC-07.2 (CN-95, CN-96) |
| Xóa đoạn 19 | Nguyên tắc: mô tả luồng nghiệp vụ, không biến thành hướng dẫn thao tác giao diện. |  | Bỏ chữ hướng dẫn của mẫu |
| Xóa đoạn 23 | Không tạo flow chỉ vì muốn “đủ bảng”; chỉ đưa những nhánh có căn cứ từ nghiệp vụ. |  | Bỏ chữ hướng dẫn của mẫu |
| Bảng 6, dòng 5, cột 2 | Thực hiện ở Bước 4 của Luồng chính (<<include>> UC-08). | Thực hiện ở Bước 4 của Luồng chính. | Bỏ «include» UC-08 |
| Bảng 6, dòng 6, cột 2 | Thực hiện ở Bước 4 của Luồng chính (<<include>> UC-09). | Thực hiện ở Bước 4 của Luồng chính. | Bỏ «include» UC-09 |
| Bảng 6, dòng 7, cột 0 | DoA (Chuyển cấp) | QT-42 | Dùng mã quy tắc của P1 (QT-42 = DoA chuyển cấp) |
| Bảng 6, thêm sau dòng 7 |  | QT-41 \| Quá tải trên 110% kéo dài quá 2 tuần bắt buộc CEO/Managing Director phê duyệt ngoại lệ. \| Điều kiện chạm Mức 4–5 ở Luồng thay thế A1. | Ngưỡng dùng ở A1 có nguồn QT-41 |
| Bảng 6, thêm sau dòng 6 |  | CN-95 \| Hệ thống cho phép PMO/Quản lý danh mục yêu cầu giải trình hoặc bổ sung thông tin gửi tới RM là người đề xuất phương án. \| Điểm chuyển sang UC-07.2 ở Luồng thay thế A2. | A2 dựa trên CN-95 |
| Đoạn 27 | Xác định trước: | Thành phần AD UC-07.1: điểm bắt đầu (PMO tiếp nhận hồ sơ); ba làn PMO/Quản lý danh mục, Cấp thẩm quyền (PMO Mức 1–3 hoặc CEO Mức 4–5) và Hệ thống; các action bước 1–6; decision “Mức rủi ro?” ([Mức 1–3] / [Mức 4–5 (A1)]) và “Đủ cơ sở ra quyết định?” ([Đủ] / [Chưa đủ (A2)]); một merge sau nhánh chuyển cấp; hai điểm kết thúc (chuyển UC-07.3/07.4 hoặc chuyển UC-07.2). Không có fork/join. | Mục 4.1 chỉ còn khung mẫu; ghi thành phần theo AD đã vẽ lại |
| Xóa đoạn 28 | Điểm bắt đầu |  | Bỏ chữ hướng dẫn của mẫu |
| Xóa đoạn 29 | Actor/Swimlane nếu cần |  | Bỏ chữ hướng dẫn của mẫu |
| Xóa đoạn 30 | Các Activity/Action |  | Bỏ chữ hướng dẫn của mẫu |
| Xóa đoạn 31 | Decision/Merge |  | Bỏ chữ hướng dẫn của mẫu |
| Xóa đoạn 32 | Fork/Join nếu có |  | Bỏ chữ hướng dẫn của mẫu |
| Xóa đoạn 33 | Điều kiện các nhánh |  | Bỏ chữ hướng dẫn của mẫu |
| Xóa đoạn 34 | Điểm kết thúc |  | Bỏ chữ hướng dẫn của mẫu |
| Xóa đoạn 36 | Vẽ Activity Diagram tương ứng với Use Case Description. |  | Bỏ chữ hướng dẫn của mẫu |
| Xóa đoạn 37 | AD phải thể hiện được: |  | Bỏ chữ hướng dẫn của mẫu |
| Xóa đoạn 38 | Luồng chính |  | Bỏ chữ hướng dẫn của mẫu |
| Xóa đoạn 39 | Luồng thay thế |  | Bỏ chữ hướng dẫn của mẫu |
| Xóa đoạn 40 | Luồng ngoại lệ |  | Bỏ chữ hướng dẫn của mẫu |
| Xóa đoạn 41 | Các điều kiện rẽ nhánh tương ứng với Description. |  | Bỏ chữ hướng dẫn của mẫu |
| Thêm ảnh sau đoạn 35 |  | AD_UC-07.1.png | AD vẽ lại khớp D: bỏ “PMO tự phê duyệt”, “Ra quyết định”, vòng RM giải trình; có A1 chuyển cấp |
| Bảng 7, dòng 1, cột 2 | PMO, CEO (actor chính) và RM (actor phụ). | PMO, CEO (actor chính). RM không tham gia UC-07.1, chỉ ở UC-07.2. | Khớp UCD và AD mới |
| Bảng 7, dòng 2, cột 2 | Include V9 (CN-93) và V10 (CN-94); Extend UC-07.2 khi cần giải trình (CN-95, CN-96). | Không có include. UC-07.2 extend UC-07.1 khi cần giải trình (CN-95). | Bỏ include V9, V10 |
| Bảng 7, dòng 4, cột 2 | Bao phủ 100% từ CN-89 đến CN-94 | Bao phủ CN-89 đến CN-94; CN-95 ở luồng A2. | Ghi đúng phạm vi |
| Bảng 8, dòng 3 |  | (giữ) \| Chưa (chờ QĐ-19) \| Giữ DoA ở dạng quy tắc (CN-90, QT-40–42); kết quả đối chiếu ghi ở thuộc tính capThamQuyen của HoSoTrinhDuyet. | QĐ-19 chưa chốt; không tạo lớp DoA |
| Bảng 8, dòng 4 |  | Thông tin chi phí V9 \| Không (tham chiếu) \| Dùng lớp DanhGiaChiPhi của V9 (Hình II.3-5); V8 chỉ xem, không sao chép (CN-93). | Không nhân bản dữ liệu V9 |
| Bảng 8, dòng 5 |  | Thông tin dự báo V10 \| Không (tham chiếu) \| Dùng lớp KetQuaDuBao của V10 (Hình II.3-6); V8 chỉ xem, không sao chép (CN-94). | Không nhân bản dữ liệu V10 |
| Bảng 9, dòng 2 |  | (giữ) \| HoSoTrinhDuyet \| (giữ) | DoA là quy tắc, không phải lớp |
| Bảng 9, dòng 4 |  | (giữ) \| DanhGiaChiPhi (V9) \| (giữ) | Khớp sơ đồ lớp II.3 (Hình II.3-4, II.3-5, II.3-6) |
| Bảng 9, dòng 5 |  | (giữ) \| KetQuaDuBao (V10) \| (giữ) | Khớp sơ đồ lớp II.3 (Hình II.3-4, II.3-5, II.3-6) |
| Bảng 10, xóa dòng 3 | MaTranPhanQuyenDoA \| Chứa định mức quy tắc phân quyền DoA (Mức 1–3 so với Mức 4–5) và các ngưỡng rủi ro. \| CN-90, DoA (I.1.3.8) |  | DoA giữ ở dạng quy tắc (chờ QĐ-19) |
| Bảng 10, dòng 4 |  | DanhGiaChiPhi (V9, tham chiếu) \| Lớp của V9; hồ sơ V8 tham chiếu khi rà soát. \| CN-93; Hình II.3-5 | Khớp sơ đồ lớp II.3 (Hình II.3-4, II.3-5, II.3-6) |
| Bảng 10, dòng 5 |  | KetQuaDuBao (V10, tham chiếu) \| Lớp của V10; hồ sơ V8 tham chiếu khi rà soát. \| CN-94; Hình II.3-6 | Khớp sơ đồ lớp II.3 (Hình II.3-4, II.3-5, II.3-6) |
| Bảng 11, dòng 1 |  | (giữ) \| maHoSo / ngayTrinh / mucRuiRo / capThamQuyen / trangThaiXuLy / ngayChuyenCap \| (giữ) | Khớp sơ đồ lớp II.3 (Hình II.3-4, II.3-5, II.3-6) |
| Bảng 11, dòng 2 |  | (giữ) \| maPhuongAn / phienBan / loaiPhuongAn / trangThai (chi tiết phân bổ ở ChiTietBoTri; xung đột ở DiemXungDot) \| Lớp của V6; V8 đọc khi rà soát. | Khớp sơ đồ lớp II.3 (Hình II.3-4, II.3-5, II.3-6) |
| Bảng 11, xóa dòng 3 | MaTranPhanQuyenDoA \| CapThamQuyen (PMO, CEO)NguongQuaTai (>110%)NguongThoiGian (>2 tuần)ThoiHanChuyenCapMax (1 ngày) \| Cấu hình quy tắc kiểm soát DoA. |  | DoA giữ ở dạng quy tắc (chờ QĐ-19) |
| Bảng 11, xóa dòng 4 | ThongTinChiPhi \| MaChiPhiNganSachDuToanChenhLechNganSachPhuongAnDanhDoi \| Chứa dữ liệu tài chính tích hợp từ V9. |  | Thuộc tính thuộc lớp DanhGiaChiPhi của V9 |
| Bảng 11, xóa dòng 5 | ThongTinDuBao \| MaDuBaoTongCungTongCauKetQuaDuBao \| Chứa dữ liệu cung - cầu tích hợp từ V10. |  | Thuộc tính thuộc lớp KetQuaDuBao của V10 |
| Bảng 11, dòng 6 |  | (giữ) \| noiDungCanLamRo / ngayYeuCau / trangThai \| (giữ) | Khớp sơ đồ lớp II.3 (Hình II.3-4, II.3-5, II.3-6) |
| Bảng 12, dòng 5 |  | HoSoTrinhDuyet \| (giữ) \| (giữ) | DoA là quy tắc; kết quả ghi vào capThamQuyen |
| Bảng 12, dòng 6 |  | DanhGiaChiPhi (V9) \| (giữ) \| (giữ) | Khớp sơ đồ lớp II.3 (Hình II.3-4, II.3-5, II.3-6) |
| Bảng 12, dòng 7 |  | KetQuaDuBao (V10) \| (giữ) \| (giữ) | Khớp sơ đồ lớp II.3 (Hình II.3-4, II.3-5, II.3-6) |
| Bảng 13, dòng 1 |  | PhuongAnBoTri \| (giữ) \| HoSoTrinhDuyet \| Mỗi hồ sơ trình duyệt gắn với một phương án; một phương án có thể được trình lại sau khi trả về V6/V7 (CN-101). | Khớp sơ đồ lớp II.3 (Hình II.3-4, II.3-5, II.3-6) |
| Bảng 13, xóa dòng 2 | HoSoTrinhDuyet \| Association \| MaTranPhanQuyenDoA \| Hồ sơ trình duyệt đối chiếu với Ma trận DoA để xác định thẩm quyền (PMO hay CEO). |  | DoA giữ ở dạng quy tắc (chờ QĐ-19) |
| Bảng 13, dòng 3 |  | (giữ) \| Association (tham chiếu) \| DanhGiaChiPhi \| (giữ) | Khớp sơ đồ lớp II.3 (Hình II.3-4, II.3-5, II.3-6) |
| Bảng 13, dòng 4 |  | (giữ) \| Association (tham chiếu) \| KetQuaDuBao \| (giữ) | Khớp sơ đồ lớp II.3 (Hình II.3-4, II.3-5, II.3-6) |
| Bảng 13, dòng 5 |  | (giữ) \| Composition \| (giữ) \| Hồ sơ chưa đủ cơ sở có thể có nhiều đợt yêu cầu giải trình (CN-95). | Khớp sơ đồ lớp II.3 (Hình II.3-4, II.3-5, II.3-6) |
| Bảng 14, dòng 1 |  | PhuongAnBoTri — HoSoTrinhDuyet \| 1 : 0..* \| Một phương án có thể có nhiều lần trình (CN-101, CN-102 lưu phiên bản phương án); mỗi hồ sơ thuộc một phương án. | Khớp sơ đồ lớp II.3 (Hình II.3-4, II.3-5, II.3-6) |
| Bảng 14, xóa dòng 2 | HoSoTrinhDuyet — MaTranPhanQuyenDoA \| * : 1 \| Nhiều hồ sơ trình duyệt cùng đối chiếu chung 1 bộ quy tắc Ma trận DoA hệ thống. |  | DoA giữ ở dạng quy tắc (chờ QĐ-19) |
| Bảng 14, dòng 3 |  | HoSoTrinhDuyet — DanhGiaChiPhi \| 0..* : 0..* \| Tham chiếu kết quả đánh giá chi phí của V9. | Khớp sơ đồ lớp II.3 (Hình II.3-4, II.3-5, II.3-6) |
| Bảng 14, dòng 4 |  | HoSoTrinhDuyet — KetQuaDuBao \| 0..* : 0..1 \| Tham chiếu kết quả dự báo của V10. | Khớp sơ đồ lớp II.3 (Hình II.3-4, II.3-5, II.3-6) |
| Xóa đoạn 60 | Vẽ Domain/Class Diagram trong phạm vi UC được giao, làm cơ sở cho phần mô hình hóa cấu trúc tĩnh II.3. |  | Bỏ chữ hướng dẫn của mẫu |
| Thêm ảnh sau đoạn 59 |  | II3-4_Phuong_an_xung_dot_phe_duyet.png | Bài chưa có sơ đồ lớp trong Word; dùng Hình II.3-4 (nguồn draw.io) |
| Xóa đoạn 62 | ❗❗ AD + UC + Class: [PTTKHTTT] MNV8 |  | Ghi chú nội bộ về quyền sửa file draw.io, không thuộc nội dung báo cáo |
| Xóa đoạn 63 | (đã cấp quyền chỉnh sửa, leader có thể sửa trực tiếp vào draw io) |  | Ghi chú nội bộ |
