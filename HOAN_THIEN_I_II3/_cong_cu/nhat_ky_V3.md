## V3 — V3- Phần 2.docx

| Vị trí (theo bản gốc) | Trước | Sau | Lý do |
|---|---|---|---|
| Bảng 1, dòng 4, cột 1 | không có | PMO/Quản lý danh mục (phê duyệt tiêu chí tạm, CN-19) | Lỗi: thiếu luồng tiêu chí tạm do PMO/Quản lý danh mục phê duyệt (CN-19) |
| Đoạn 8 | RM là tác nhân duy nhất của UC-02.1, không có include hay extend | RM là tác nhân chính của UC-02.1; PMO/Quản lý danh mục tham gia khi phê duyệt tiêu chí tạm (CN-19). Không có include hay extend. | Lỗi: thiếu luồng tiêu chí tạm do PMO/Quản lý danh mục phê duyệt (CN-19) |
| Ảnh ở đoạn 9 |  | UCD_UC-02.png | Lỗi: UCD vùng chỉ có 02.1; dùng UCD vùng UC-02 đủ 02.1–02.3 (nguồn draw.io) |
| Đoạn 10 | RM kết nối trực tiếp với UC-02.1 bằng association không có actor phụ và không có quan hệ giữa cac UC | RM và PMO/Quản lý danh mục kết nối với UC-02.1 bằng association; UCD vùng thể hiện thêm UC-02.2 và UC-02.3 cùng tác nhân Nguồn lực. | Lỗi: thiếu luồng tiêu chí tạm do PMO/Quản lý danh mục phê duyệt (CN-19) |
| Bảng 3, dòng 5, cột 1 | Không có | PMO/Quản lý danh mục (phê duyệt tiêu chí tạm) | Lỗi: thiếu luồng tiêu chí tạm do PMO/Quản lý danh mục phê duyệt (CN-19) |
| Bảng 3, dòng 6, cột 1 | RM có yêu cầu quản lý bộ tiêu chí: thêm tiêu chí, điều chỉnh mức độ hoặc điều kiện hoặc ngừng áp dụng tiêu chí | RM có yêu cầu quản lý bộ tiêu chí: thêm tiêu chí, điều chỉnh mức độ hoặc điều kiện, ngừng áp dụng tiêu chí, hoặc đề xuất tiêu chí tạm cho kỹ năng chưa có tiêu chí | Bổ sung tình huống của CN-19 |
| Bảng 3, dòng 7, cột 1 | RM đã đăng nhập bằng tài khoản cá nhân và có vai trò RM; bộ kỹ năng/ tiêu chí hiện hành của V3 truy cập được | Danh mục kỹ năng và bộ tiêu chí hiện hành của V3 (thang 5 mức, CN-18) tra cứu được | Bỏ điều kiện đăng nhập/phân quyền: không phải điều kiện nghiệp vụ (HD-MAU §3.3) |
| Bảng 4, dòng 2 |  | (giữ) \| (giữ) \| Hệ thống cung cấp bộ tiêu chí hiện hành gồm kỹ năng, tiêu chí, thang 5 mức (1 mới bắt đầu … 5 chuyên gia) và điều kiện | Bỏ kiểm tra quyền (HD-MAU §3.3); ghi thang 5 mức theo CN-18 |
| Bảng 4, dòng 8 |  | (giữ) \| (giữ) \| Hệ thống cập nhật bộ tiêu chí ở trạng thái sẵn sàng sử dụng | Bỏ “thông báo kết quả”: không phải bước nghiệp vụ, AD không có |
| Bảng 5, xóa dòng 3 | E1 \| Bước 2 \| Tài khoản không có vai trò RM. \| Hệ thống từ chối yêu cầu; UC kết thúc. |  | Bỏ E1 “không có quyền”: kiểm tra quyền là cơ chế chung, không phải luồng nghiệp vụ |
| Bảng 5, dòng 4 |  | E1 \| (giữ) \| (giữ) \| (giữ) | Đánh lại mã sau khi bỏ E1, E3 cũ |
| Bảng 5, dòng 5 |  | A3 \| Bước 3 \| Kỹ năng cần đánh giá chưa có tiêu chí. \| RM đề xuất tiêu chí tạm; hệ thống ghi tiêu chí tạm ở trạng thái chờ phê duyệt. PMO/Quản lý danh mục phê duyệt hoặc từ chối; tiêu chí tạm chỉ được dùng sau khi được duyệt. UC kết thúc. | Thay E3 “lưu không thành công” (lỗi kỹ thuật, bỏ theo HD-MAU §3.3) bằng luồng CN-19 còn thiếu |
| Bảng 6, dòng 1 |  | CN-18 \| Hệ thống cho phép RM duy trì danh sách kỹ năng cần đánh giá, tiêu chí đánh giá và thang mức độ thành thạo 5 mức. \| Cơ sở của toàn UC; bước 2, 3, 5. | Lỗi: bảng quy tắc còn để trống |
| Bảng 6, dòng 2 |  | CN-19 \| Hệ thống cho phép RM đề xuất tiêu chí tạm cho kỹ năng chưa có tiêu chí; tiêu chí tạm chờ PMO/Quản lý danh mục phê duyệt và chỉ được dùng sau khi được duyệt. \| Cơ sở của A3. | Lỗi: bảng quy tắc còn để trống |
| Bảng 6, thêm sau dòng 2 |  | QT-08 \| Kinh nghiệm thực tế có thể làm căn cứ khi doanh nghiệp chấp nhận; chứng chỉ hoặc bằng cấp chỉ là một căn cứ, không mặc định là thành thạo. \| Ràng buộc nội dung điều kiện công nhận của từng mức (bước 3, 4). | Điền quy tắc liên quan |
| Bảng 6, thêm sau dòng 2 |  | QT-07 \| Kỹ năng phải được phân biệt với mức độ thành thạo; một nguồn lực có thể có nhiều kỹ năng ở các mức khác nhau. \| Tiêu chí gắn với kỹ năng, mức độ tách riêng (bước 3). | Điền quy tắc liên quan |
| Bảng 6, thêm sau dòng 2 |  | QT-06 \| Đánh giá năng lực phải dựa trên tiêu chí xác định trước. \| Lý do bộ tiêu chí phải sẵn sàng trước khi đánh giá; tiêu chí tạm chưa duyệt không được dùng. | Điền quy tắc liên quan |
| Bảng 7, dòng 2, cột 1 | Hai làn: RM và Hệ thống. | Ba làn: RM, Hệ thống, PMO/Quản lý danh mục. | Lỗi: thiếu luồng tiêu chí tạm do PMO/Quản lý danh mục phê duyệt (CN-19) |
| Bảng 7, dòng 3, cột 1 | RM: yêu cầu quản lý tiêu chí; xác định nội dung thay đổi; xem xét / và xác nhận lưu. Hệ thống: kiểm tra quyền; kiểm tra tính hợp lệ; / xử lý theo loại yêu cầu; lưu và ghi nhật ký; cập nhật bộ tiêu chí / sẵn sàng sử dụng. | RM: yêu cầu quản lý tiêu chí; xác định nội dung thay đổi; xem xét và xác nhận lưu; hủy thay đổi (A2). Hệ thống: cung cấp bộ tiêu chí; kiểm tra tính hợp lệ; xử lý theo loại yêu cầu; ngừng áp dụng thay vì xóa (A1); lưu thay đổi; cập nhật bộ tiêu chí sẵn sàng sử dụng; ghi tiêu chí tạm chờ phê duyệt (A3). PMO/Quản lý danh mục: phê duyệt hoặc từ chối tiêu chí tạm. | Theo AD vẽ lại |
| Bảng 7, dòng 4, cột 1 | Có quyền? (E1) · Hợp lệ? (E2, quay lại bước 3) · Yêu cầu ngừng / áp dụng tiêu chí? (A1, nhập lại luồng chính) · RM xác nhận lưu? / (A2) · Lưu thành công? (E3). | Kỹ năng chưa có tiêu chí? (A3) · Hợp lệ? (E1, quay lại bước 3) · Ngừng áp dụng tiêu chí đang dùng? (A1, nhập lại trước bước 6) · Xác nhận lưu? (A2). Hai merge: trước bước 3 và trước bước 6. | Bỏ “Có quyền?”, “Lưu thành công?”; thêm A3 |
| Bảng 7, dòng 7, cột 1 | Bộ tiêu chí sẵn sàng sử dụng (luồng chính); hủy thay đổi (A2); / từ chối yêu cầu (E1); lưu không thành công (E3). | Bộ tiêu chí sẵn sàng sử dụng (luồng chính); hủy thay đổi (A2); PMO/Quản lý danh mục phê duyệt hoặc từ chối tiêu chí tạm (A3). | Theo AD vẽ lại |
| Xóa đoạn 27 | Nét đứt: luồng thay thế (A) |  | Chú giải màu của hình cũ; AD vẽ lại theo ký pháp UML chuẩn, không dùng màu |
| Xóa đoạn 28 | Viền cảnh báo: luồng ngoại lệ (E) |  | Chú giải màu của hình cũ; AD vẽ lại theo ký pháp UML chuẩn, không dùng màu |
| Xóa đoạn 29 | Viền xanh: kết quả |  | Chú giải màu của hình cũ; AD vẽ lại theo ký pháp UML chuẩn, không dùng màu |
| Ảnh ở đoạn 30 |  | AD_UC-02.1.png | AD vẽ lại bằng draw.io: bỏ E1/E3, nối A1 về trước bước 6, thêm làn PMO và A3 |
| Đoạn 31 | Luồng chính đi dọc hai làn đến bộ tiêu chí sẵn sàng sử dụng, A1 nhập lại luồng chính, A2 và E1-E3 kết thúc riêng, E2 quay lại bước xác định nội dung | Luồng chính đi qua hai làn RM và Hệ thống đến bộ tiêu chí sẵn sàng sử dụng; A1 nhập lại trước bước 6; E1 quay lại bước xác định nội dung; A2 và A3 kết thúc riêng, A3 đi qua làn PMO/Quản lý danh mục. | Theo AD vẽ lại |
| Đoạn 35 | Kết quả đối chiều dựa trên bước 1-8 và các nhánh A1, A2, E1-E3 ở mục 3; AD ở mục 4.2 dùng đúng thứ tự và điều kiện rẽ nhánh đó | Kết quả đối chiếu dựa trên bước 1–8 và các nhánh A1, A2, A3, E1 ở mục 3; AD ở mục 4.2 dùng đúng thứ tự và điều kiện rẽ nhánh đó. | Theo D đã sửa |
| Bảng 9, dòng 1 |  | (giữ) \| Không \| Tác nhân, không phải lớp miền. | Lỗi: actor không phải lớp miền |
| Bảng 9, dòng 2 |  | (giữ) \| Không \| Là thao tác của RM trên bộ tiêu chí, không cần lưu thành đối tượng riêng. | Bỏ: không có trong Phần I (II.3 không giữ lớp này) |
| Bảng 9, dòng 8 |  | (giữ) \| Không \| Phần I không yêu cầu lưu lịch sử thay đổi bộ tiêu chí thành đối tượng riêng. | Bỏ: không có trong Phần I (II.3 không giữ lớp này) |
| Bảng 10, dòng 1 |  | (giữ) \| Không thuộc lớp miền \| (giữ) | RM là tác nhân |
| Bảng 9, dòng 6 |  | (giữ) \| Không \| Là thuộc tính dieuKienCongNhan của MucDoNangLuc (II.3). | Gộp lớp DieuKien thành thuộc tính, theo II.3 |
| Bảng 10, dòng 4, cột 2 | E2 | E1 | Đánh lại mã ngoại lệ |
| Bảng 13, dòng 9, cột 2 | E2 | E1 | Đánh lại mã ngoại lệ |
| Bảng 10, dòng 3 |  | (giữ) \| TieuChiNangLuc \| (giữ) | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 10, dòng 4 |  | (giữ) \| TieuChiNangLuc \| (giữ) | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 10, dòng 5 |  | (giữ) \| TieuChiNangLuc \| (giữ) | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 10, dòng 7 |  | (giữ) \| BoTieuChiNangLuc \| (giữ) | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 10, dòng 6 |  | (giữ) \| BoTieuChiNangLuc \| Bộ tiêu chí giữ trạng thái thay đổi (bước 6, A2). | Bỏ: không có trong Phần I (II.3 không giữ lớp này) |
| Bảng 10, dòng 8 |  | (giữ) \| Không thuộc lớp miền \| Lưu người thực hiện, thời điểm là chức năng hệ thống (bước 7). | Bỏ: không có trong Phần I (II.3 không giữ lớp này) |
| Bảng 11, xóa dòng 1 | RM \| Người quản lý nguồn lực thực hiện UC \| UC-02.1; mục 04 ( người quản lý nguồn lực) |  | Lỗi: actor không phải lớp miền |
| Bảng 11, xóa dòng 2 | Yeucauquanlytieuchi \| Yêu cầu thêm, điều chỉnh hoặc ngừng áp dụng tiêu chí \| UC-02.1 (đầu vào: yêu cầu quản lý) |  | Bỏ: không có trong Phần I (II.3 không giữ lớp này) |
| Bảng 11, dòng 3 |  | BoTieuChiNangLuc \| (giữ) \| UC-02.1 (đầu ra); CN-18, QT-06 | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 11, dòng 4 |  | TieuChiNangLuc \| Một tiêu chí dùng để đánh giá năng lực; có thể là tiêu chí tạm chờ phê duyệt \| UC-02.1; CN-18, CN-19 | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 11, dòng 5 |  | MucDoNangLuc \| Mức đánh giá của một tiêu chí theo thang 5 mức; kèm điều kiện công nhận mức \| UC-02.1; CN-18, QT-07 | Thang 5 mức theo CN-18 (không còn “chưa xác định”) |
| Bảng 11, xóa dòng 6 | Dieukien \| Điều kiện hoặc căn cứ công nhận một mức độ \| UC-02.1; QT-03, QT-04 |  | Điều kiện là thuộc tính dieuKienCongNhan của MucDoNangLuc (II.3) |
| Bảng 11, dòng 7 |  | KyNang \| (giữ) \| UC-02.1; CN-18, QT-07 | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 11, xóa dòng 8 | Nhatkythaydoi \| Bản ghi lịch sử thay đổi bộ tiêu chí \| Đề xuất, chưa có trong V3 |  | Bỏ: không có trong Phần I (II.3 không giữ lớp này) |
| Bảng 12, xóa dòng 1 | RM \| maRM \| Mã định danh RM. |  | Lớp đã bỏ (RM, YeuCauQuanLyTieuChi) |
| Bảng 12, xóa dòng 2 | RM \| hoTen \| Họ tên RM. |  | Lớp đã bỏ (RM, YeuCauQuanLyTieuChi) |
| Bảng 12, xóa dòng 3 | YeuCauQuanLyTieuChi \| maYeuCau \| Mã định danh yêu cầu. |  | Lớp đã bỏ (RM, YeuCauQuanLyTieuChi) |
| Bảng 12, xóa dòng 4 | YeuCauQuanLyTieuChi \| loaiYeuCau \| Thêm, điều chỉnh hoặc ngừng áp dụng. |  | Lớp đã bỏ (RM, YeuCauQuanLyTieuChi) |
| Bảng 12, xóa dòng 5 | YeuCauQuanLyTieuChi \| noiDung \| Nội dung thay đổi RM đề xuất. |  | Lớp đã bỏ (RM, YeuCauQuanLyTieuChi) |
| Bảng 12, xóa dòng 6 | YeuCauQuanLyTieuChi \| trangThai \| Chờ xác nhận, đã xác nhận hoặc đã hủy. |  | Lớp đã bỏ (RM, YeuCauQuanLyTieuChi) |
| Bảng 12, dòng 7 |  | BoTieuChiNangLuc \| (giữ) \| (giữ) | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 12, dòng 9 |  | BoTieuChiNangLuc \| (giữ) \| (giữ) | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 12, dòng 8 |  | BoTieuChiNangLuc \| (giữ) \| (giữ) | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 12, dòng 10 |  | BoTieuChiNangLuc \| (giữ) \| (giữ) | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 12, dòng 11 |  | TieuChiNangLuc \| (giữ) \| (giữ) | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 12, dòng 12 |  | TieuChiNangLuc \| (giữ) \| (giữ) | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 12, dòng 13 |  | TieuChiNangLuc \| (giữ) \| (giữ) | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 12, dòng 14 |  | TieuChiNangLuc \| (giữ) \| Chờ phê duyệt (tiêu chí tạm), đang áp dụng hoặc ngừng áp dụng. | Bổ sung trạng thái của CN-19 |
| Bảng 12, dòng 15 |  | MucDoNangLuc \| (giữ) \| (giữ) | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 12, dòng 16 |  | MucDoNangLuc \| (giữ) \| (giữ) | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 12, dòng 18 |  | MucDoNangLuc \| (giữ) \| (giữ) | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 12, dòng 17 |  | MucDoNangLuc \| (giữ) \| Thứ tự mức, từ 1 (mới bắt đầu) đến 5 (chuyên gia). | Thang 5 mức theo CN-18 |
| Bảng 12, dòng 19 |  | MucDoNangLuc \| dieuKienCongNhan \| Điều kiện hoặc căn cứ công nhận mức đó (kinh nghiệm, chứng chỉ, QT-08). | Gộp lớp DieuKien thành thuộc tính, theo II.3 |
| Bảng 12, xóa dòng 20 | DieuKien \| noiDung \| Nội dung điều kiện. |  | Gộp vào dieuKienCongNhan |
| Bảng 12, xóa dòng 21 | DieuKien \| loaiCanCu \| Loại căn cứ: chứng chỉ, kinh nghiệm hoặc khác. |  | Gộp vào dieuKienCongNhan |
| Bảng 12, xóa dòng 24 | NhatKyThayDoi \| maNhatKy \| Mã định danh bản ghi. |  | Bỏ: không có trong Phần I (II.3 không giữ lớp này) |
| Bảng 12, xóa dòng 25 | NhatKyThayDoi \| nguoiThucHien \| RM thực hiện thay đổi. |  | Bỏ: không có trong Phần I (II.3 không giữ lớp này) |
| Bảng 12, xóa dòng 26 | NhatKyThayDoi \| thoiDiem \| Thời điểm thay đổi. |  | Bỏ: không có trong Phần I (II.3 không giữ lớp này) |
| Bảng 12, xóa dòng 27 | NhatKyThayDoi \| noiDung \| Nội dung thay đổi. |  | Bỏ: không có trong Phần I (II.3 không giữ lớp này) |
| Bảng 13, xóa dòng 1 | RM \| guiYeuCauQuanLy() \| Gửi yêu cầu quản lý tiêu chí. |  | Lớp RM đã bỏ |
| Bảng 13, dòng 2 |  | BoTieuChiNangLuc \| (giữ) \| (giữ) | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 13, dòng 3 |  | BoTieuChiNangLuc \| (giữ) \| RM hủy thay đổi (A2). | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 13, dòng 4 |  | BoTieuChiNangLuc \| (giữ) \| (giữ) | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 13, dòng 5 |  | BoTieuChiNangLuc \| (giữ) \| (giữ) | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 13, dòng 6 |  | TieuChiNangLuc \| (giữ) \| (giữ) | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 13, dòng 7 |  | TieuChiNangLuc \| (giữ) \| (giữ) | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 13, dòng 8 |  | TieuChiNangLuc \| (giữ) \| (giữ) | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 13, dòng 9 |  | TieuChiNangLuc \| (giữ) \| (giữ) | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 13, dòng 10 |  | MucDoNangLuc \| (giữ) \| (giữ) | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 13, dòng 11 |  | TieuChiNangLuc \| pheDuyetTieuChiTam() \| PMO/Quản lý danh mục duyệt hoặc từ chối tiêu chí tạm (A3). | Thay thao tác của lớp DieuKien đã gộp; bổ sung CN-19 |
| Bảng 13, xóa dòng 12 | NhatKyThayDoi \| ghiNhan() \| Ghi nhật ký mỗi lần lưu thay đổi. |  | Bỏ: không có trong Phần I (II.3 không giữ lớp này) |
| Bảng 14, xóa dòng 1 | RM \| Association \| YeuCauQuanLyTieuChi \| RM gửi yêu cầu quản lý. |  | Lớp RM đã bỏ |
| Bảng 14, xóa dòng 2 | YeuCauQuanLyTieuChi \| Association \| BoTieuChi \| Yêu cầu áp dụng cho một bộ tiêu chí. |  | Bỏ: không có trong Phần I (II.3 không giữ lớp này) |
| Bảng 14, dòng 3 |  | BoTieuChiNangLuc \| (giữ) \| TieuChiNangLuc \| (giữ) | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 14, dòng 4 |  | TieuChiNangLuc \| Composition \| MucDoNangLuc \| Tiêu chí gồm các mức độ. | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 14, xóa dòng 5 | TieuChiDanhGia \| Association \| DieuKien \| Tiêu chí có các điều kiện. |  | Lớp DieuKien đã gộp |
| Bảng 14, dòng 6 |  | TieuChiNangLuc \| (giữ) \| KyNang \| Tiêu chí có thể gắn với một kỹ năng. | Bỏ [CẦN XÁC NHẬN]: đã chốt ở II.3 |
| Bảng 14, xóa dòng 7 | BoTieuChi \| Association \| NhatKyThayDoi \| Mỗi lần thay đổi bộ tiêu chí được ghi lại. |  | Bỏ: không có trong Phần I (II.3 không giữ lớp này) |
| Bảng 15, xóa dòng 1 | RM – YeuCauQuanLyTieuChi \| 1 – 0..* \| Một RM có thể gửi nhiều yêu cầu; mỗi yêu cầu do một RM gửi. |  | Lớp RM đã bỏ |
| Bảng 15, xóa dòng 2 | YeuCauQuanLyTieuChi – BoTieuChi \| 0..* – 1 \| Mỗi yêu cầu áp dụng cho một bộ tiêu chí; một bộ có thể có nhiều yêu cầu. |  | Bỏ: không có trong Phần I (II.3 không giữ lớp này) |
| Bảng 15, dòng 3 |  | BoTieuChiNangLuc – TieuChiNangLuc \| (giữ) \| Bộ tiêu chí cần ít nhất một tiêu chí để sẵn sàng sử dụng. | Bỏ [CẦN XÁC NHẬN]: đã chốt ở II.3 |
| Bảng 15, dòng 4 |  | TieuChiNangLuc – MucDoNangLuc \| (giữ) \| (giữ) | Đồng bộ tên lớp với II.3 (Hình II.3-2) |
| Bảng 15, xóa dòng 5 | TieuChiDanhGia – DieuKien \| 1 – 0..* \| Tiêu chí có thể có hoặc không có điều kiện. |  | Lớp DieuKien đã gộp |
| Bảng 15, dòng 6 |  | TieuChiNangLuc – KyNang \| (giữ) \| Tiêu chí gắn tối đa một kỹ năng; một kỹ năng có thể có nhiều tiêu chí. | Bỏ [CẦN XÁC NHẬN]: đã chốt ở II.3 |
| Bảng 15, xóa dòng 7 | BoTieuChi – NhatKyThayDoi \| 1 – 0..* \| Mỗi thay đổi tạo một bản ghi; bộ mới chưa có bản ghi nào. |  | Bỏ: không có trong Phần I (II.3 không giữ lớp này) |
| Đoạn 55 | Một bộ tiêu chí gồm nhiều tiêu chí; mỗi tiêu chí có mức độ và điều kiện | Một bộ tiêu chí gồm nhiều tiêu chí; mỗi tiêu chí có các mức độ thành thạo kèm điều kiện công nhận | Theo II.3 |
| Ảnh ở đoạn 56 |  | II3-2_Nhu_cau_va_nang_luc.png | Sơ đồ lớp theo mô hình thống nhất (Hình II.3-2, nguồn draw.io) |
| Đoạn 57 | TieuChiDanhGia là lớp trung tâm của UC-02.1. Số cấp của MucDo chưa xác định (Q-04), nên thuộc tính thuTu chưa giới hạn số mức. | TieuChiNangLuc là lớp trung tâm của UC-02.1. MucDoNangLuc dùng thang 5 mức theo CN-18. | Thang 5 mức đã có trong CN-18 |
