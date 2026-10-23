## V2a — V2-Phần II .docx

| Vị trí (theo bản gốc) | Trước | Sau | Lý do |
|---|---|---|---|
| Bảng 1, dòng 3, cột 1 | Quản lý dự án (PM) / Resource Manager (RM) | Quản lý dự án (PM) | Lỗi: CN-01–CN-11 đều do PM thực hiện; hệ thống không phải actor |
| Bảng 1, dòng 4, cột 1 | Hệ thống quản lý nguồn lực (System) | Không có | Lỗi: CN-01–CN-11 đều do PM thực hiện; hệ thống không phải actor |
| Ảnh ở đoạn 12 |  | UCD_UC-01.png | Dùng UCD vùng UC-01 thống nhất (01.1–01.3), nguồn draw.io |
| Bảng 3, dòng 3, cột 1 | PM/RM xác định và hoàn thiện nhu cầu nguồn lực của dự án (phạm vi công việc, loại nguồn lực/kỹ năng, quy mô FTE) trước khi chuyển sang các bước xác nhận, đánh giá hoặc tìm kiếm. | PM xác định và hoàn thiện nhu cầu nguồn lực của dự án (phạm vi công việc, loại nguồn lực/kỹ năng, quy mô FTE theo giai đoạn, thời gian và mức tham gia %FTE), rồi chuyển RM xem xét tại UC-01.2. | Lỗi: CN-01–CN-11 đều do PM thực hiện; hệ thống không phải actor; thêm thời gian, %FTE (CN-07, CN-08) |
| Bảng 3, dòng 4, cột 1 | Quản lý dự án (PM) / Resource Manager (RM) | Quản lý dự án (PM) | Lỗi: CN-01–CN-11 đều do PM thực hiện; hệ thống không phải actor |
| Bảng 3, dòng 5, cột 1 | Hệ thống | Không có | Lỗi: CN-01–CN-11 đều do PM thực hiện; hệ thống không phải actor |
| Bảng 3, dòng 6, cột 1 | PM/RM khởi tạo yêu cầu bổ sung hoặc phân bổ nguồn lực mới cho dự án. | Dự án phát sinh công việc mới, hoặc thay đổi phạm vi, khối lượng, tiến độ làm nhu cầu nguồn lực phải cập nhật; PM khởi tạo nhu cầu. | Theo P1 I.1.3.2 “Bắt đầu khi” |
| Bảng 3, dòng 7, cột 1 | Dự án, kế hoạch giai đoạn hoặc công việc cần bổ sung nguồn lực đã được xác lập/phê duyệt ở Mục I. PM/RM đã đăng nhập vào hệ thống với quyền hạn phù hợp. | Dự án, kế hoạch giai đoạn và công việc cần nguồn lực đã được xác lập. | Bỏ điều kiện đăng nhập (xử lý kỹ thuật, không phải nghiệp vụ) |
| Bảng 3, dòng 8, cột 1 | Nhu cầu nguồn lực được xác định, lưu trữ vào cơ sở dữ liệu ở trạng thái “Đã xây dựng” và đủ thông tin sẵn sàng cho bước xác nhận (UC-01.2). | Nhu cầu nguồn lực đủ thông tin được chuyển RM xem xét, ở trạng thái “Chờ xác nhận”; đây là tiền điều kiện của UC-01.2. Nếu PM chỉ lưu (A2), nhu cầu ở trạng thái “Đang xây dựng”. | Thêm bước chuyển RM (CN-11); tên trạng thái theo QĐ-02 |
| Bảng 4, dòng 1 |  | 1 \| PM \| Chọn dự án; xem bối cảnh dự án, danh mục công việc và kế hoạch các giai đoạn (CN-01). | Lỗi: actor chỉ là PM; bỏ thao tác giao diện; thêm giai đoạn, %FTE (CN-07, CN-08) |
| Bảng 4, dòng 2 |  | 2 \| System \| Hiển thị thông tin dự án, danh mục công việc và các mốc thời gian liên quan. | Lỗi: actor chỉ là PM; bỏ thao tác giao diện; thêm giai đoạn, %FTE (CN-07, CN-08) |
| Bảng 4, dòng 3 |  | 3 \| PM \| Xác lập phạm vi công việc: chọn các công việc cần nguồn lực (CN-02). | Lỗi: actor chỉ là PM; bỏ thao tác giao diện; thêm giai đoạn, %FTE (CN-07, CN-08) |
| Bảng 4, dòng 4 |  | 4 \| System \| Kiểm tra thông tin dự án và phạm vi đã đủ để hiểu công việc, giai đoạn và thời gian thực hiện. | Lỗi: actor chỉ là PM; bỏ thao tác giao diện; thêm giai đoạn, %FTE (CN-07, CN-08) |
| Bảng 4, dòng 5 |  | 5 \| PM \| Xác định loại nguồn lực cần thiết cho từng công việc và yêu cầu chuyên môn, kỹ năng, chứng chỉ (một công việc có thể cần nhiều loại nguồn lực) (CN-04, CN-05). | Lỗi: actor chỉ là PM; bỏ thao tác giao diện; thêm giai đoạn, %FTE (CN-07, CN-08) |
| Bảng 4, dòng 6 |  | 6 \| PM \| Xác định quy mô nhu cầu của từng loại nguồn lực theo FTE, theo từng giai đoạn (CN-06). | Lỗi: actor chỉ là PM; bỏ thao tác giao diện; thêm giai đoạn, %FTE (CN-07, CN-08) |
| Bảng 4, dòng 7 |  | 7 \| PM \| Xác định thời điểm bắt đầu, kết thúc hoặc giai đoạn cần nguồn lực và mức tham gia %FTE của từng vị trí (CN-07, CN-08). | Lỗi: actor chỉ là PM; bỏ thao tác giao diện; thêm giai đoạn, %FTE (CN-07, CN-08) |
| Bảng 4, dòng 8 |  | 8 \| PM \| Rà soát toàn bộ nhu cầu theo tình trạng hiện tại của dự án và lưu nhu cầu (CN-09). | Lỗi: actor chỉ là PM; bỏ thao tác giao diện; thêm giai đoạn, %FTE (CN-07, CN-08) |
| Bảng 4, thêm sau dòng 8 |  | 11 \| System \| Ghi nhận nhu cầu ở trạng thái “Chờ xác nhận” để RM xem xét tại UC-01.2. | Thêm bước gửi RM (CN-11) |
| Bảng 4, thêm sau dòng 8 |  | 10 \| PM \| Chuyển nhu cầu đã hoàn thiện cho RM xem xét (CN-11). | Thêm bước gửi RM (CN-11) |
| Bảng 4, thêm sau dòng 8 |  | 9 \| System \| Lưu nhu cầu ở trạng thái “Đang xây dựng”. | Phân biệt lưu với đã gửi RM; tên trạng thái theo QĐ-02 |
| Bảng 5, dòng 1 |  | A1 \| Bước 4 \| Thông tin dự án chưa đủ để hiểu công việc, giai đoạn, thời gian; hoặc phạm vi công việc, mốc thời gian bị thiếu. \| Hệ thống chỉ rõ thông tin còn thiếu → PM yêu cầu bổ sung thông tin dự án hoặc điều chỉnh phạm vi; nhu cầu chưa được cố định cho đến khi có bổ sung (CN-03) → quay lại bước 3. | Mở rộng A1 cho trường hợp thông tin dự án chưa đủ (CN-03) |
| Bảng 5, dòng 2 |  | A2 \| Bước 8 \| PM chưa hoàn thiện nhu cầu, chỉ lưu để làm tiếp. \| Hệ thống lưu nhu cầu ở trạng thái “Đang xây dựng” (bước 9); UC kết thúc, chưa chuyển RM. Khi hoàn thiện, PM mở lại nhu cầu và thực hiện từ bước 8. | Lỗi: P1 không có giới hạn tổng nhu cầu ≤ 1 FTE (CN-06, CN-08, PCN-09); thay A2 cũ bằng nhánh lưu chưa gửi |
| Bảng 5, dòng 3 |  | E1 \| Bước 7 \| Mức tham gia nằm ngoài 0–100% FTE, hoặc thời điểm kết thúc trước thời điểm bắt đầu. \| Hệ thống chỉ rõ thông tin không hợp lệ → PM sửa → tiếp tục bước 7. | Bỏ lỗi kết nối CSDL (xử lý kỹ thuật); thay bằng kiểm tra nghiệp vụ theo thuật ngữ FTE ở P1 I.1.2 |
| Bảng 6, dòng 1 |  | CN-01, CN-02 \| PM tra cứu bối cảnh dự án, danh mục công việc, kế hoạch giai đoạn và lưu phạm vi công việc. \| Bước 1–3 | Đổi mã theo P1 |
| Bảng 6, dòng 2 |  | CN-03 \| PM yêu cầu bổ sung khi thông tin dự án chưa đủ; nhu cầu chưa được cố định cho đến khi có bổ sung. \| Bước 4, A1 | Lỗi: mã CN-V2-01 không có trong P1 |
| Bảng 6, dòng 3 |  | CN-04, CN-05; QT-01, QT-02 \| Nhu cầu gắn với công việc; mỗi công việc có một hoặc nhiều loại nguồn lực, kèm yêu cầu chuyên môn, kỹ năng. \| Bước 5 | Lỗi: RB-V2-03 (FTE ≤ quỹ thời gian chuẩn) không có trong P1 |
| Bảng 6, thêm sau dòng 3 |  | CN-09, CN-11; QT-04, QT-05 \| PM rà soát nhu cầu theo tình trạng dự án và chuyển nhu cầu đã hoàn thiện cho RM; nhu cầu phải được RM xác nhận trước khi sang V3/V4. \| Bước 8–11, A2 | Thêm căn cứ bước gửi RM |
| Bảng 6, thêm sau dòng 3 |  | CN-06, CN-07, CN-08; QT-02, QT-03 \| Quy mô theo FTE từng giai đoạn; thời gian hoặc giai đoạn; mức tham gia %FTE (0–100%) khi công việc không cần toàn thời gian. \| Bước 6, 7, E1 | Thêm căn cứ giai đoạn và %FTE |
| Đoạn 29 | Actor/Swimlane: 2 Swimlane gồm PM/RM (Quản lý dự án) và Hệ thống Quản lý Nguồn lực. | Actor/Swimlane: 2 swimlane gồm PM (Quản lý dự án) và Hệ thống. | Bỏ RM khỏi làn |
| Đoạn 31 | Đăng nhập hệ thống & Chọn phân vùng V2 (PM/RM) | Chọn dự án; xem bối cảnh, công việc, kế hoạch giai đoạn (PM) | AD vẽ lại theo luồng chính đã sửa; bỏ đăng nhập, nhấn nút, ghi log |
| Đoạn 32 | Nhấn "Tạo mới hồ sơ nhu cầu nguồn lực" (PM/RM) | Hiển thị thông tin dự án, công việc và các mốc thời gian (Hệ thống) | AD vẽ lại theo luồng chính đã sửa; bỏ đăng nhập, nhấn nút, ghi log |
| Đoạn 33 | Truy vấn danh mục Dự án & Công việc (Hệ thống) | Xác lập phạm vi công việc cần nguồn lực (PM) | AD vẽ lại theo luồng chính đã sửa; bỏ đăng nhập, nhấn nút, ghi log |
| Đoạn 34 | Hiển thị giao diện lập nhu cầu chi tiết (Hệ thống) | Kiểm tra thông tin dự án và phạm vi (Hệ thống) | AD vẽ lại theo luồng chính đã sửa; bỏ đăng nhập, nhấn nút, ghi log |
| Đoạn 35 | Chọn Dự án, Công việc & Mốc thời gian (PM/RM) | Xác định loại nguồn lực, yêu cầu chuyên môn, kỹ năng cho từng công việc (PM) | AD vẽ lại theo luồng chính đã sửa; bỏ đăng nhập, nhấn nút, ghi log |
| Đoạn 36 | Chọn Vị trí, Nhóm kỹ năng & Chứng chỉ yêu cầu (PM/RM) | Xác định quy mô FTE theo từng giai đoạn (PM) | AD vẽ lại theo luồng chính đã sửa; bỏ đăng nhập, nhấn nút, ghi log |
| Đoạn 37 | Nhập số lượng nhân sự & Định mức thời gian (% FTE) (PM/RM) | Xác định thời gian hoặc giai đoạn và mức tham gia %FTE của từng vị trí (PM) | AD vẽ lại theo luồng chính đã sửa; bỏ đăng nhập, nhấn nút, ghi log |
| Đoạn 38 | Rà soát thông tin & Bấm "Lưu nhu cầu" (PM/RM) | Rà soát toàn bộ nhu cầu và lưu (PM); Lưu nhu cầu, trạng thái “Đang xây dựng” (Hệ thống) | AD vẽ lại theo luồng chính đã sửa; bỏ đăng nhập, nhấn nút, ghi log |
| Đoạn 39 | Kiểm tra ràng buộc mốc thời gian & chỉ số FTE (Hệ thống) | Chuyển nhu cầu đã hoàn thiện cho RM xem xét (PM); Ghi nhận trạng thái “Chờ xác nhận” (Hệ thống) | AD vẽ lại theo luồng chính đã sửa; bỏ đăng nhập, nhấn nút, ghi log |
| Xóa đoạn 40 | Ghi nhận bản ghi nhu cầu vào CSDL, Cập nhật trạng thái "Đã xây dựng nội dung", Tạo Log vết thao tác, Gửi thông báo đến V2.2 (Hệ thống) |  | Gộp vào action ở trên; bỏ ghi log, thông báo kỹ thuật |
| Đoạn 42 | Node kiểm tra Ràng buộc mốc thời gian hợp lệ ?  [Không]: Báo lỗi & Điều chỉnh lại mốc thời gian; [Hợp lệ]: Kiểm tra tiếp FTE. | Decision “Đủ để hiểu công việc, giai đoạn, thời gian?”: [Chưa đủ] → A1, PM yêu cầu bổ sung hoặc điều chỉnh phạm vi, quay về merge trước bước 3; [Đủ] → bước 5. | Theo A1 đã sửa |
| Đoạn 43 | Node kiểm tra Chỉ số FTE <= 1.0/Nhân sự ?  [Vi phạm quá tải]: Cảnh báo & Tính toán lại FTE; [Đạt chuẩn]: Tiến hành lưu CSDL. | Decision “Thời gian và %FTE hợp lệ?”: [Không hợp lệ] → E1, quay về merge trước bước 7; [Hợp lệ] → bước 8. Decision “Nhu cầu đã hoàn thiện, chuyển RM?”: [Chưa] → A2, kết thúc; [Đã hoàn thiện] → bước 10. | Lỗi: bỏ decision FTE ≤ 1.0 (không có trong P1) |
| Đoạn 44 | Điểm kết thúc: Nút tròn viền kép (Bullseye). | Điểm kết thúc: nút tròn viền kép; một điểm sau khi lưu chưa gửi (A2), một điểm sau khi chuyển RM. |  |
| Ảnh ở đoạn 47 |  | AD_UC-01.1.png | AD vẽ lại bằng draw.io theo D đã sửa (AD_UC-01.1.drawio) |
| Bảng 8, dòng 3 |  | Công việc (Task/WorkItem) \| Không \| Phạm vi công việc được lưu là thuộc tính phamViCongViec của nhu cầu (CN-02); hệ thống không quản lý công việc như một đối tượng riêng. | Thống nhất tên lớp và vị trí thuộc tính với II.3 (Hình II.3-2) |
| Bảng 8, dòng 5 |  | Loại nguồn lực / Kỹ năng (ResourceType / Skill) \| Có \| Tách thành vị trí cần bố trí (ViTriCanBoTri: vai trò, số lượng, %FTE) và yêu cầu kỹ năng (YeuCauKyNang) tham chiếu danh mục KyNang dùng chung với V3. | Thống nhất tên lớp và vị trí thuộc tính với II.3 (Hình II.3-2) |
| Bảng 9, dòng 2 |  | (giữ) \| NhuCauNguonLuc \| (giữ) | Thống nhất tên lớp và vị trí thuộc tính với II.3 (Hình II.3-2) |
| Bảng 9, dòng 3 |  | (giữ) \| ViTriCanBoTri, YeuCauKyNang \| (giữ) | Thống nhất tên lớp và vị trí thuộc tính với II.3 (Hình II.3-2) |
| Bảng 9, dòng 4 |  | (giữ) \| ViTriCanBoTri \| Ghi quy mô (số lượng) và mức tham gia %FTE của vị trí theo giai đoạn. | Thống nhất tên lớp và vị trí thuộc tính với II.3 (Hình II.3-2) |
| Bảng 10, dòng 2 |  | ViTriCanBoTri \| Vị trí cần bố trí trong nhu cầu: vai trò, số lượng, %FTE, giai đoạn. \| UC-01.1 (bước 5–7) | Thống nhất tên lớp và vị trí thuộc tính với II.3 (Hình II.3-2) |
| Bảng 10, dòng 4 |  | YeuCauKyNang \| Kỹ năng và cấp độ mà vị trí đòi hỏi; tham chiếu danh mục KyNang (V3). \| UC-01.1 (bước 5) | Thống nhất tên lớp và vị trí thuộc tính với II.3 (Hình II.3-2) |
| Bảng 10, thêm sau dòng 1 |  | GiaiDoanDuAn \| Giai đoạn của dự án mà quy mô và thời gian nhu cầu gắn vào. \| CN-06, CN-07 | Thống nhất tên lớp và vị trí thuộc tính với II.3 (Hình II.3-2) |
| Bảng 11, dòng 1 |  | DuAn \| maDuAn, tenDuAn, ngayBatDau, ngayKetThuc, hangUuTien \| Định danh, mốc thời gian tổng thể và hạng ưu tiên của dự án. | Thống nhất tên lớp và vị trí thuộc tính với II.3 (Hình II.3-2) |
| Bảng 11, dòng 2 |  | ViTriCanBoTri \| maViTri, vaiTro, soLuong, tyLeFTE \| Vai trò, số lượng và mức tham gia %FTE của vị trí. | Thống nhất tên lớp và vị trí thuộc tính với II.3 (Hình II.3-2) |
| Bảng 11, dòng 3 |  | NhuCauNguonLuc \| maNhuCau, phamViCongViec, thoiGianBatDau, thoiGianKetThuc, trangThai \| Phạm vi công việc, thời gian và trạng thái của nhu cầu; số lượng, FTE thuộc từng vị trí. | Thống nhất tên lớp và vị trí thuộc tính với II.3 (Hình II.3-2); soLuongNhanSu, chiSoFTE chuyển sang ViTriCanBoTri |
| Bảng 11, dòng 4 |  | YeuCauKyNang \| capDoYeuCau, batBuoc \| Cấp độ yêu cầu và tính bắt buộc của kỹ năng. | Thống nhất tên lớp và vị trí thuộc tính với II.3 (Hình II.3-2) |
| Bảng 11, thêm sau dòng 1 |  | GiaiDoanDuAn \| maGiaiDoan, tenGiaiDoan, ngayBatDau, ngayKetThuc \| Giai đoạn của dự án. | Thống nhất tên lớp và vị trí thuộc tính với II.3 (Hình II.3-2) |
| Bảng 12, dòng 2 |  | ViTriCanBoTri \| ganGiaiDoan(giaiDoan), capNhatQuyMo(soLuong, tyLeFTE) \| Gắn vị trí với giai đoạn và cập nhật quy mô, mức tham gia. | Thống nhất tên lớp và vị trí thuộc tính với II.3 (Hình II.3-2) |
| Bảng 12, dòng 3 |  | NhuCauNguonLuc \| taoMoiNhuCau(), chinhSuaNhuCau(), chuyenRM(), capNhatTrangThai(trangThaiMoi) \| Khởi tạo, chỉnh sửa nhu cầu, chuyển RM xem xét và cập nhật trạng thái. | Thống nhất tên lớp và vị trí thuộc tính với II.3 (Hình II.3-2) |
| Bảng 12, dòng 4 |  | YeuCauKyNang \| datYeuCau(kyNang, capDo, batBuoc) \| Ghi kỹ năng, cấp độ và tính bắt buộc mà vị trí đòi hỏi. | Thống nhất tên lớp và vị trí thuộc tính với II.3 (Hình II.3-2) |
| Bảng 13, dòng 1 |  | DuAn \| Association \| NhuCauNguonLuc \| Một dự án có thể có nhiều nhu cầu nguồn lực. | Thống nhất tên lớp và vị trí thuộc tính với II.3 (Hình II.3-2) |
| Bảng 13, dòng 2 |  | NhuCauNguonLuc \| Composition (*--) \| ViTriCanBoTri \| Một nhu cầu gồm một hoặc nhiều vị trí cần bố trí. | Thống nhất tên lớp và vị trí thuộc tính với II.3 (Hình II.3-2) |
| Bảng 13, dòng 3 |  | ViTriCanBoTri \| Composition (*--) \| YeuCauKyNang \| Mỗi vị trí đòi hỏi các kỹ năng; YeuCauKyNang tham chiếu KyNang (V3). | Thống nhất tên lớp và vị trí thuộc tính với II.3 (Hình II.3-2) |
| Bảng 13, thêm sau dòng 3 |  | ViTriCanBoTri \| Association \| GiaiDoanDuAn \| Vị trí gắn với giai đoạn khi nhu cầu thay đổi theo giai đoạn (QT-29). | Thống nhất tên lớp và vị trí thuộc tính với II.3 (Hình II.3-2) |
| Bảng 14, dòng 1 |  | DuAn ── NhuCauNguonLuc \| 1 : 0..* \| Một dự án chưa có hoặc có nhiều nhu cầu. | Thống nhất tên lớp và vị trí thuộc tính với II.3 (Hình II.3-2) |
| Bảng 14, dòng 2 |  | NhuCauNguonLuc ── ViTriCanBoTri \| 1 : 1..* \| Nhu cầu nêu rõ vai trò, số lượng (P1 I.1.3.2). | Thống nhất tên lớp và vị trí thuộc tính với II.3 (Hình II.3-2) |
| Bảng 14, dòng 3 |  | ViTriCanBoTri ── YeuCauKyNang \| 1 : 0..* \| Một vị trí có thể đòi hỏi nhiều kỹ năng. | Thống nhất tên lớp và vị trí thuộc tính với II.3 (Hình II.3-2) |
| Bảng 14, thêm sau dòng 3 |  | ViTriCanBoTri ── GiaiDoanDuAn \| 0..* : 0..1 \| Vị trí có thể gắn với một giai đoạn hoặc dùng cho cả dự án. | Thống nhất tên lớp và vị trí thuộc tính với II.3 (Hình II.3-2) |
| Ảnh ở đoạn 60 |  | II3-2_Nhu_cau_va_nang_luc.png | Sơ đồ lớp theo mô hình thống nhất (Hình II.3-2, nguồn draw.io) |

## V2b — V2-Phần II (2) - ban 22-10.docx

| Vị trí (theo bản gốc) | Trước | Sau | Lý do |
|---|---|---|---|
| Ảnh ở đoạn 7 |  | UCD_UC-01.png | Dùng UCD vùng UC-01 thống nhất (đủ 01.1–01.3), nguồn draw.io |
| Bảng 1, dòng 4, cột 1 | PM — tham gia khi nhu cầu chưa đủ điều kiện và được chuyển lại để bổ sung/điều chỉnh  | Không có (PM nhận nhu cầu được chuyển lại và xử lý ở UC-01.3) | PM không thao tác trong UC-01.2; việc PM bổ sung, điều chỉnh thuộc UC-01.3 (CN-14, CN-15) |
| Bảng 3, dòng 1, cột 2 | UC-01.3 | UC-01.2 | Lỗi: UC tự mở rộng chính nó; hình UCD vẽ 01.3 extend 01.2 |
| Bảng 4, dòng 5, cột 1 | PM | Không có | PM không thao tác trong UC-01.2; việc PM bổ sung, điều chỉnh thuộc UC-01.3 (CN-14, CN-15) |
| Bảng 4, dòng 6, cột 1 | Có nhu cầu nguồn lực đã hoàn thiện cần RM xem xét.  | PM chuyển nhu cầu đã hoàn thiện cho RM (kết thúc UC-01.1, CN-11); nhu cầu ở trạng thái “Chờ xác nhận”. | Ghi rõ sự kiện bắt đầu, nối với UC-01.1 (QĐ-02) |
| Bảng 4, dòng 8, cột 1 | Nhu cầu được xác nhận; trạng thái “đã xác nhận” là điều kiện để bàn giao sang V3 và V4.  / Nhu cầu được chuyển lại PM để bổ sung/điều chỉnh; nhu cầu chưa được xác nhận và không được bàn giao sang V3, V4.  | Nhu cầu được xác nhận; trạng thái “Đã xác nhận” là điều kiện để bàn giao sang V3 và V4 (QT-05, QT-12).<br>Hoặc: nhu cầu được chuyển lại PM, trạng thái “Cần tiếp tục hoàn thiện”; nhu cầu chưa được xác nhận và không được bàn giao sang V3, V4. | Đặt tên trạng thái theo QĐ-02 (CN-15: “cần tiếp tục hoàn thiện”) |
| Bảng 5, xóa dòng 8 | 8 \|  \| Kết thúc |  | Bỏ dòng “Kết thúc” không có tác nhân; điểm kết thúc thể hiện trên AD |
| Bảng 6, dòng 1 |  | A1 \| Bước 3 \| Nhu cầu chưa đủ điều kiện \| RM ghi nhận nội dung cần bổ sung, điều chỉnh.<br>Hệ thống chuyển lại nhu cầu cho PM, trạng thái “Cần tiếp tục hoàn thiện”.<br>Use case kết thúc; PM xử lý tiếp ở UC-01.3. | Lỗi: các bước PM điều chỉnh thuộc UC-01.3 (extend). Đây là luồng nghiệp vụ hợp lệ theo CN-14 nên đổi E1 thành A1 |
| Đoạn 22 | 3.1.2. Luồng chính | 3.2.2. Luồng chính | Lỗi đánh số: trùng số mục 3.1.x của UC-01.2 |
| Đoạn 23 | 3.1.3. Luồng thay thế / ngoại lệ | 3.2.3. Luồng thay thế / ngoại lệ | Lỗi đánh số: trùng số mục 3.1.x của UC-01.2 |
| Đoạn 27 | 3.1.4. Business Rules / yêu cầu liên quan | 3.2.4. Business Rules / yêu cầu liên quan | Lỗi đánh số: trùng số mục 3.1.x của UC-01.2 |
| Bảng 8, dòng 6, cột 1 | PM nhận yêu cầu bổ sung/điều chỉnh từ RM; hoặc nhận phản hồi từ V4 về việc không có ứng viên đáp ứng; hoặc nhận thông tin cung ứng, khoảng thiếu/dư từ V10 để xem xét lại nhu cầu. | (1) RM chuyển lại nhu cầu chưa đủ điều kiện (từ UC-01.2, quan hệ extend; CN-14); hoặc (2) PM nhận phản hồi từ V4 về việc không có ứng viên đáp ứng, hoặc thông tin cung ứng, khoảng thiếu/dư từ V10 để xem xét lại nhu cầu (CN-17). | QĐ-12: giữ đủ hai cách bắt đầu |
| Bảng 8, dòng 8, cột 1 | Nhu cầu nguồn lực được cập nhật theo nội dung điều chỉnh và chuyển trạng thái “Chờ xác nhận”  | Nhu cầu được điều chỉnh và gửi lại RM, trạng thái “Chờ xác nhận”.<br>Hoặc (A1): nhu cầu giữ nguyên trạng thái hiện tại. | Bổ sung hậu điều kiện của A1; gửi lại RM theo CN-11 |
| Bảng 9, dòng 1 |  | (giữ) \| (giữ) \| Tra cứu nhu cầu hiện tại và phản hồi đã được ghi nhận: yêu cầu bổ sung của RM, phản hồi V4 hoặc thông tin V10 (CN-15, CN-17). | Ghi rõ các loại phản hồi |
| Bảng 9, dòng 3 |  | (giữ) \| (giữ) \| Xem xét phản hồi, xác định nội dung nhu cầu cần điều chỉnh. | Lỗi: bước quá chung |
| Bảng 9, dòng 4 |  | (giữ) \| (giữ) \| Điều chỉnh loại nguồn lực, quy mô FTE, thời gian hoặc giai đoạn và mức tham gia %FTE của từng vị trí (CN-10). | Lỗi: bước quá chung; nêu các thông tin được điều chỉnh theo QT-02, QT-03 |
| Bảng 9, dòng 5 |  | (giữ) \| (giữ) \| Kiểm tra và lưu thông tin điều chỉnh. | Tách bước lưu khỏi bước gửi lại RM |
| Bảng 9, dòng 6 |  | 6 \| PM \| Gửi lại nhu cầu đã điều chỉnh cho RM xem xét (CN-11). | Thay dòng “Kết thúc”: sau khi sửa, nhu cầu phải quay lại RM (QT-05) |
| Bảng 9, thêm sau dòng 6 |  | 7 \| Hệ thống \| Ghi nhận nhu cầu ở trạng thái “Chờ xác nhận”; RM xem xét lại ở UC-01.2. | Kết thúc ở gửi lại RM |
| Bảng 10, dòng 1 |  | E1 \| Bước 5 \| Thông tin điều chỉnh chưa hợp lệ \| Hệ thống báo thông tin chưa hợp lệ; quay lại bước 4. | Đánh lại mã (UC-01.3 chỉ có một luồng ngoại lệ) |
| Bảng 10, thêm sau dòng 1 |  | A1 \| Bước 3 \| Phản hồi từ V4 hoặc V10 không làm thay đổi nhu cầu \| PM giữ nguyên nhu cầu hiện tại; use case kết thúc. | Lỗi: thiếu nhánh khi xem xét lại mà nhu cầu không đổi (CN-17 “xem xét lại”, QT-04 “rà soát”) |
| Bảng 12, dòng 2, cột 1 | Gồm 3 swimlane: RM, Hệ thống, PM. | Gồm 2 swimlane: RM và Hệ thống. | PM không thao tác trong UC-01.2; việc PM bổ sung, điều chỉnh thuộc UC-01.3 (CN-14, CN-15) |
| Bảng 12, dòng 3, cột 1 | Tiếp nhận nhu cầu nguồn lực cần xem xét; hiển thị thông tin nhu cầu nguồn lực; ghi nhận trạng thái nhu cầu “Chờ xác nhận”; xem xét nhu cầu nguồn lực; xác nhận nhu cầu đã đủ điều kiện; ghi nhận nội dung cần bổ sung/chỉnh lại; chuyển lại nhu cầu cần chỉnh; điều chỉnh nhu cầu theo phản hồi; gửi lại nhu cầu đã chỉnh; ghi nhận kết quả xác nhận và cập nhật trạng thái “Đã xác nhận”; bàn giao nhu cầu cho … | Tiếp nhận nhu cầu cần xem xét; hiển thị thông tin nhu cầu; xem xét nhu cầu; xác nhận nhu cầu; ghi nhận kết quả và cập nhật “Đã xác nhận”; bàn giao nhu cầu cho V3 và V4 (RM); chuyển nhu cầu sang V3 và V4 (Hệ thống); A1: ghi nhận nội dung cần bổ sung, chuyển lại PM. | Theo AD vẽ lại: bỏ các action của PM, bàn giao đặt ở làn RM (CN-16) |
| Bảng 12, dòng 5, cột 1 | Điểm hợp nhất hai nhánh sau khi RM xác nhận nhu cầu đủ điều kiện hoặc PM điều chỉnh và gửi lại nhu cầu. Hai nhánh hội tụ trước hoạt động ghi nhận kết quả xác nhận và cập nhật trạng thái “Đã xác nhận” theo sơ đồ hiện tại. | Không có. Nhánh “chưa đủ điều kiện” kết thúc UC-01.2; PM xử lý tiếp ở UC-01.3. | Lỗi: đoạn văn mô tả merge khác hình; sau khi bỏ action của PM thì không còn luồng quay lại |
| Bảng 12, dòng 8, cột 1 | Nhu cầu chưa đủ điều kiện → RM ghi nhận nội dung cần bổ sung/chỉnh lại → Hệ thống chuyển lại nhu cầu cần chỉnh → PM điều chỉnh nhu cầu theo phản hồi → PM gửi lại nhu cầu đã chỉnh → Hệ thống ghi nhận trạng thái “Chờ xác nhận” → RM tiếp tục xem xét. | Nhu cầu chưa đủ điều kiện → RM ghi nhận nội dung cần bổ sung, điều chỉnh → Hệ thống chuyển lại PM, trạng thái “Cần tiếp tục hoàn thiện” → kết thúc. | Theo A1 đã sửa |
| Bảng 12, dòng 9, cột 1 | Sau khi hệ thống bàn giao nhu cầu cho V3 và V4. | Hai điểm kết thúc: sau khi hệ thống chuyển nhu cầu sang V3 và V4; hoặc sau khi chuyển lại PM (A1). | Theo AD vẽ lại |
| Ảnh ở đoạn 33 |  | AD_UC-01.2.png | AD vẽ lại bằng draw.io theo D đã sửa |
| Bảng 13, dòng 1, cột 1 | PM bắt đầu tra cứu phản hồi và nhu cầu nguồn lực hiện tại. | PM bắt đầu khi RM chuyển lại nhu cầu, hoặc khi nhận phản hồi từ V4/V10. | QĐ-12: hai cách bắt đầu |
| Bảng 13, dòng 3, cột 1 | Tra cứu phản hồi và nhu cầu hiện tại; hiển thị nhu cầu hiện tại và phản hồi đã ghi nhận; xem xét phản hồi; điều chỉnh nhu cầu; cập nhật nhu cầu và chuyển trạng thái “Chờ xác nhận”. | Tra cứu nhu cầu và phản hồi; hiển thị nhu cầu và phản hồi; xem xét phản hồi; điều chỉnh loại nguồn lực, quy mô FTE, thời gian, %FTE; kiểm tra và lưu; gửi lại RM; ghi nhận trạng thái “Chờ xác nhận”; A1: giữ nguyên nhu cầu. | Theo D đã sửa |
| Bảng 13, dòng 4, cột 1 | “Thông tin điều chỉnh hợp lệ?” — được thực hiện sau khi PM điều chỉnh nhu cầu. | “Nhu cầu cần điều chỉnh?” sau khi PM xem xét phản hồi; “Thông tin hợp lệ?” sau khi hệ thống kiểm tra. | Thêm decision cho A1 |
| Bảng 13, dòng 5, cột 1 | Điểm hội tụ tại Decision thứ nhất khi thông tin điều chỉnh không hợp lệ quay lại để PM tiếp tục xử lý. Theo ký hiệu UML, vị trí này cần được xem xét lại: nếu chỉ có một luồng quay lại để sửa thông tin, có thể nối trực tiếp về hoạt động “Điều chỉnh nhu cầu” thay vì dùng Merge. | Một merge trước hoạt động “Điều chỉnh nhu cầu”, hợp nhất nhánh “Có” và nhánh quay lại khi thông tin chưa hợp lệ (E1). Không còn merge ngay trước điểm kết thúc. | Lỗi ký pháp: merge chỉ có một luồng ra final node |
| Bảng 13, dòng 7, cột 1 | Tại Decision “Thông tin điều chỉnh hợp lệ?”, nếu thông tin chưa hợp lệ thì quay lại bước xử lý điều chỉnh để PM sửa lại. | Thông tin chưa hợp lệ (E1) → quay lại merge trước “Điều chỉnh nhu cầu”. | Theo AD vẽ lại |
| Bảng 13, dòng 8, cột 1 | Nếu thông tin điều chỉnh hợp lệ, hệ thống cập nhật nhu cầu và chuyển trạng thái thành “Chờ xác nhận”. | Thông tin hợp lệ → PM gửi lại RM → hệ thống ghi nhận “Chờ xác nhận”. | Kết thúc ở gửi lại RM |
| Bảng 13, dòng 9, cột 1 | Sau khi hệ thống cập nhật nhu cầu và chuyển trạng thái “Chờ xác nhận”. | Sau khi hệ thống ghi nhận “Chờ xác nhận”; hoặc sau khi PM giữ nguyên nhu cầu (A1). | Theo AD vẽ lại |
| Ảnh ở đoạn 36 |  | AD_UC-01.3.png | AD vẽ lại bằng draw.io theo D đã sửa |
| Bảng 17, dòng 1, cột 1 | Biểu diễn nhu cầu nguồn lực của dự án, bao gồm loại nguồn lực, quy mô FTE, thời gian cần nguồn lực, tỷ lệ FTE và trạng thái xử lý. Đây là đối tượng trung tâm được RM xem xét, xác nhận hoặc chuyển lại để PM điều chỉnh.  | Biểu diễn nhu cầu nguồn lực của dự án: phạm vi công việc, thời gian cần nguồn lực và trạng thái xử lý. Gồm một hoặc nhiều ViTriCanBoTri. Đây là đối tượng trung tâm được RM xem xét, xác nhận hoặc chuyển lại để PM điều chỉnh. | Đồng bộ với II.3 (Hình II.3-2): loại nguồn lực, quy mô, %FTE thuộc từng vị trí cần bố trí |
| Bảng 17, thêm sau dòng 1 |  | ViTriCanBoTri \| Vị trí cần bố trí trong nhu cầu: loại nguồn lực/vai trò, số lượng (FTE) và mức tham gia %FTE. \| UC-01.1, UC-01.3; CN-04 đến CN-08 | Đồng bộ với II.3 (Hình II.3-2): loại nguồn lực, quy mô, %FTE thuộc từng vị trí cần bố trí |
| Bảng 18, dòng 3 |  | ViTriCanBoTri \| vaiTro \| Loại nguồn lực hoặc vai trò cần đáp ứng. | Đồng bộ với II.3 (Hình II.3-2): loại nguồn lực, quy mô, %FTE thuộc từng vị trí cần bố trí |
| Bảng 18, dòng 4 |  | ViTriCanBoTri \| soLuong \| Quy mô nguồn lực cần thiết, tính theo FTE. | Đồng bộ với II.3 (Hình II.3-2): loại nguồn lực, quy mô, %FTE thuộc từng vị trí cần bố trí |
| Bảng 18, dòng 5 |  | (giữ) \| thoiGianBatDau, thoiGianKetThuc \| (giữ) | Tên thuộc tính theo II.3 |
| Bảng 18, dòng 6 |  | ViTriCanBoTri \| tyLeFTE \| (giữ) | Đồng bộ với II.3 (Hình II.3-2): loại nguồn lực, quy mô, %FTE thuộc từng vị trí cần bố trí |
| Bảng 18, dòng 9 |  | (giữ) \| nguonPhanHoi \| (giữ) | Tên thuộc tính theo II.3 |
| Bảng 18, dòng 10 |  | (giữ) \| noiDung \| (giữ) | Tên thuộc tính theo II.3 |
| Bảng 18, dòng 11 |  | (giữ) \| thoiDiem \| (giữ) | Tên thuộc tính theo II.3 |
| Bảng 20, thêm sau dòng 1 |  | NhuCauNguonLuc \| Composition \| ViTriCanBoTri \| Nhu cầu gồm các vị trí cần bố trí; vị trí không tồn tại ngoài nhu cầu. | Đồng bộ với II.3 (Hình II.3-2): loại nguồn lực, quy mô, %FTE thuộc từng vị trí cần bố trí |
| Bảng 21, thêm sau dòng 1 |  | NhuCauNguonLuc – ViTriCanBoTri \| 1 : 1..* \| Nhu cầu phải thể hiện ít nhất một loại nguồn lực (QT-02). | Đồng bộ với II.3 (Hình II.3-2): loại nguồn lực, quy mô, %FTE thuộc từng vị trí cần bố trí |
| Ảnh ở đoạn 57 |  | II3-2_Nhu_cau_va_nang_luc.png | Sơ đồ lớp theo mô hình thống nhất (Hình II.3-2, nguồn draw.io) |

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

## V7 — MNV7_II_Thiết kế Logic.docx

| Vị trí (theo bản gốc) | Trước | Sau | Lý do |
|---|---|---|---|
| Bảng 1, dòng 4, cột 1 | PMO / Quản lý danh mục (phê duyệt phán quyết cưỡng chế) | Không có (PMO/Quản lý danh mục, CEO/Managing Director phân xử ở UC-06.3) | Lỗi phạm vi: phân tích ngưỡng thuộc UC-06.1, phân xử thuộc UC-06.3 (extend); PMO không thao tác trong UC-06.2 |
| Bảng 2, dòng 1 |  | (giữ) \| (giữ) \| (giữ) \| RM điều phối đàm phán, làm mịn, san bằng, ghi nhật ký và bàn giao phương án (CN-79–CN-82, CN-87, CN-88). | Lỗi phạm vi: phân tích ngưỡng thuộc UC-06.1, phân xử thuộc UC-06.3 (extend); PMO không thao tác trong UC-06.2 |
| Bảng 2, dòng 2 |  | (giữ) \| (giữ) \| (giữ) \| PM các dự án liên quan đàm phán chia sẻ, thay thế hoặc điều chỉnh nhu cầu (CN-78); cùng RM lập đề xuất thay đổi khi bế tắc hoàn toàn (CN-82). | Lỗi: dùng nhầm mã CN-01..14, QT-01..08 của V2; đổi theo mã V7 trong Phần I |
| Bảng 2, dòng 3 |  | UC-06.3 \| <<extend>> \| UC-06.2 \| Hết 3 ngày làm việc chưa thống nhất hoặc bế tắc thì RM chuyển hồ sơ sang phân xử (CN-83, QT-36). | Lỗi UCD: bỏ include 06.1, thêm 06.3 extend 06.2 |
| Bảng 2, dòng 4 |  | UC-06.1 \| Không dùng include \| UC-06.2 \| UC-06.1 cung cấp danh sách điểm xung đột Mức 3 trở lên; đây là trình tự nghiệp vụ. | Lỗi UCD: bỏ include 06.1 |
| Ảnh ở đoạn 9 |  | UCD_UC-06.png | Dùng UCD vùng UC-06 thống nhất (nguồn draw.io) |
| Bảng 3, dòng 3, cột 1 | Dựa trên kết quả phát hiện quá tải Mức 3 (>120% công suất hoặc dự án Rank 1) từ UC-06.1, RM và PM đàm phán chia sẻ công suất (% FTE), thực hiện kỹ thuật Resource Smoothing (trong Float) hoặc Resource Leveling (san bằng công suất 100%), và kích hoạt Deadlock Protocol khi bế tắc hoàn toàn để làm sạch xung đột trước khi chuyển sang phê duyệt. | RM điều phối các PM liên quan đàm phán chia sẻ, thay thế hoặc điều chỉnh nhu cầu nguồn lực; làm mịn hoặc san bằng nguồn lực; lập đề xuất thay đổi khi bế tắc hoàn toàn; ghi nhật ký và bàn giao phương án đã cân đối cho V8, V9, V10. | Lỗi phạm vi: phân tích ngưỡng thuộc UC-06.1, phân xử thuộc UC-06.3 (extend); PMO không thao tác trong UC-06.2 |
| Bảng 3, dòng 5, cột 1 | PMO / Quản lý danh mục (phê duyệt phán quyết cưỡng chế) | Không có (PMO/Quản lý danh mục, CEO/Managing Director phân xử ở UC-06.3) | Lỗi phạm vi: phân tích ngưỡng thuộc UC-06.1, phân xử thuộc UC-06.3 (extend); PMO không thao tác trong UC-06.2 |
| Bảng 3, dòng 6, cột 1 | Hệ thống tự động phát System Alert khi ghi nhận nhân sự phân bổ quá tải Mức 3 từ V6/V10, hoặc RM/PM chủ động kích hoạt phiên cân đối. | Có điểm xung đột Mức 3 trở lên cần xử lý chính thức từ UC-06.1. Nguồn kích hoạt: phương án nghi ngờ xung đột từ V6 (CN-72) hoặc hồ sơ xung đột lịch từ V5 (CN-55). | Lỗi: nguồn kích hoạt là V6, V5; V10 chỉ cung cấp thông tin (CN-75) |
| Bảng 3, dòng 7, cột 1 | (1) Nhu cầu và phương án phân bổ sơ bộ ở trạng thái 'đã xác nhận' từ V6/V10.(2) Lịch nguồn lực tập trung (Resource Calendar), cấu trúc tiến độ CPM (Critical Path, Free/Total Float) và Xếp hạng ưu tiên danh mục (Portfolio Rank) đã sẵn sàng. | (1) Đã có danh sách điểm xung đột, đánh giá ảnh hưởng và kịch bản cân đối từ UC-06.1 (CN-74–CN-77). (2) Lịch nguồn lực tập trung, kế hoạch tiến độ (đường găng, khoảng dự trữ) và xếp hạng danh mục tra cứu được; thông tin thiếu/dư từ V10 dùng để tham khảo (CN-75). | Bước 1–2 cũ chuyển thành tiền điều kiện; sửa nguồn |
| Bảng 3, dòng 8, cột 1 | Phương án nguồn lực được làm sạch xung đột kỹ thuật (>100% công suất); Conflict Log lưu vết vĩnh viễn; dự thảo Change Request được khởi tạo nếu san bằng lùi tiến độ; dữ liệu sẵn sàng chuyển giao cho V8, V9, V10. | Phương án đã cân đối, nhật ký xử lý xung đột và đề xuất thay đổi (nếu có) được bàn giao V8, V9, V10 (CN-88); nhật ký lưu tối thiểu 3 năm (PCN-06). | Lỗi: Phần I quy định lưu tối thiểu 3 năm (PCN-06), không phải “vĩnh viễn” |
| Bảng 3, dòng 9, cột 1 | Khi bế tắc đàm phán quá 3 ngày: PMO ban hành Quyết định phân xử cưỡng chế trong SLA 1 ngày. Khi bế tắc nguồn lực hoàn toàn (Deadlock Protocol): Khởi tạo Change Request Lùi Baseline tiến độ hoặc Cắt giảm phạm vi (Scope Reduction) đính kèm Conflict Log chuyển V8 rà soát. | Hết 3 ngày làm việc chưa thống nhất hoặc bế tắc: RM chuyển hồ sơ sang UC-06.3 (CN-83). Bế tắc hoàn toàn: đề xuất lùi mốc tiến độ gốc hoặc cắt giảm phạm vi đi kèm phương án sang V8 rà soát (CN-82, CN-86). | Lỗi phạm vi: phân tích ngưỡng thuộc UC-06.1, phân xử thuộc UC-06.3 (extend); PMO không thao tác trong UC-06.2 |
| Bảng 4, dòng 1 |  | 1 \| RM \| Chọn điểm xung đột cần cân đối từ danh sách của UC-06.1; mở phiên đàm phán với PM các dự án liên quan (CN-79). | Lỗi: bước 1–2 cũ thuộc UC-06.1; bước 3 PM đàm phán (CN-78), RM điều phối (CN-79); bỏ “vĩnh viễn”; mã theo Phần I |
| Bảng 4, dòng 2 |  | 2 \| Hệ thống \| Hiển thị điểm xung đột, kịch bản cân đối, đường găng, khoảng dự trữ và xếp hạng danh mục; theo dõi hạn đàm phán 3 ngày làm việc (CN-79, QT-36). | Lỗi: bước 1–2 cũ thuộc UC-06.1; bước 3 PM đàm phán (CN-78), RM điều phối (CN-79); bỏ “vĩnh viễn”; mã theo Phần I |
| Bảng 4, dòng 3 |  | 3 \| PM \| PM các dự án liên quan đàm phán chia sẻ, thay thế hoặc điều chỉnh nhu cầu nguồn lực; ưu tiên phân bổ cứng đã cam kết trước, ngang nhau thì xét xếp hạng danh mục và giá trị kinh doanh (CN-78, QT-34). | Lỗi: bước 1–2 cũ thuộc UC-06.1; bước 3 PM đàm phán (CN-78), RM điều phối (CN-79); bỏ “vĩnh viễn”; mã theo Phần I |
| Bảng 4, dòng 4 |  | 4 \| RM \| Ghi nhận phương án được thống nhất (CN-79). | Lỗi: bước 1–2 cũ thuộc UC-06.1; bước 3 PM đàm phán (CN-78), RM điều phối (CN-79); bỏ “vĩnh viễn”; mã theo Phần I |
| Bảng 4, dòng 5 |  | 5 \| RM \| Còn khoảng dự trữ: làm mịn nguồn lực, điều chỉnh thời điểm phân bổ trong khoảng dự trữ, không tự thay đổi ngày hoàn thành khi chưa qua kiểm soát thay đổi (CN-80, QT-35). | Lỗi: bước 1–2 cũ thuộc UC-06.1; bước 3 PM đàm phán (CN-78), RM điều phối (CN-79); bỏ “vĩnh viễn”; mã theo Phần I |
| Bảng 4, dòng 6 |  | 6 \| Hệ thống \| Ghi điều chỉnh trên phương án; kiểm tra tổng tỷ lệ phân bổ của mỗi người trên các dự án không quá 100% công suất chuẩn (QT-32). | Lỗi: bước 1–2 cũ thuộc UC-06.1; bước 3 PM đàm phán (CN-78), RM điều phối (CN-79); bỏ “vĩnh viễn”; mã theo Phần I |
| Bảng 4, dòng 7 |  | 7 \| RM \| Ghi nhật ký xử lý xung đột: điểm xung đột, đàm phán, điều chỉnh (CN-87, QT-38). | Lỗi: bước 1–2 cũ thuộc UC-06.1; bước 3 PM đàm phán (CN-78), RM điều phối (CN-79); bỏ “vĩnh viễn”; mã theo Phần I |
| Bảng 4, dòng 8 |  | 8 \| RM \| Hoàn thiện phương án đã cân đối, kèm đề xuất thay đổi nếu có, và bàn giao V8, V9, V10 (CN-88). | Lỗi: bước 1–2 cũ thuộc UC-06.1; bước 3 PM đàm phán (CN-78), RM điều phối (CN-79); bỏ “vĩnh viễn”; mã theo Phần I |
| Bảng 4, dòng 9 |  | 9 \| Hệ thống \| Lưu nhật ký (tối thiểu 3 năm, PCN-06) và chuyển phương án sang V8, V9, V10. | Lỗi: bước 1–2 cũ thuộc UC-06.1; bước 3 PM đàm phán (CN-78), RM điều phối (CN-79); bỏ “vĩnh viễn”; mã theo Phần I |
| Bảng 4, xóa dòng 10 | 10 \| System \| Tự động ghi vết toàn bộ diễn biến đàm phán, biên bản thỏa thuận vào Nhật ký xử lý xung đột (Conflict Log) vĩnh viễn, chốt phương án nguồn lực đã cân đối và xuất file bàn giao sang V8, V9, V10. |  | Gộp vào bước 8–9 |
| Bảng 5, dòng 1 |  | A1 \| 3–4 \| Hết 3 ngày làm việc chưa thống nhất hoặc bế tắc \| RM chuyển hồ sơ chuyển cấp sang UC-06.3 (CN-83, QT-36); UC-06.2 kết thúc. Việc phân xử của PMO/Quản lý danh mục hoặc CEO/Managing Director thuộc UC-06.3. | Lỗi phạm vi: phân tích ngưỡng thuộc UC-06.1, phân xử thuộc UC-06.3 (extend); PMO không thao tác trong UC-06.2 |
| Bảng 5, dòng 2 |  | A2 \| 5 \| Hết khoảng dự trữ, chưa bế tắc hoàn toàn \| RM san bằng nguồn lực trong hạn mức công suất (CN-81); phương án ảnh hưởng đường găng, tiến độ hoặc phạm vi thì PM liên quan đánh giá tác động. Tiếp tục bước 6. | Tách nhánh san bằng (CN-81) |
| Bảng 5, dòng 3 |  | A3 \| 5 \| Bế tắc hoàn toàn: khoảng dự trữ bằng 0, không có người thay thế, không thể thuê ngoài \| RM và PM lập đề xuất lùi mốc tiến độ gốc hoặc cắt giảm phạm vi (CN-82, QT-37); đề xuất đi kèm phương án sang V8 rà soát trước (CN-86, QT-39). Tiếp tục bước 6. | Lỗi: bỏ “Fallback, thuê ngoài khẩn” không có trong Phần I; dùng điều kiện bế tắc của QT-37 |
| Bảng 5, xóa dòng 4 | A4 \| 5, 7 \| Hai dự án xung đột đồng cấp Rank 1. \| Áp dụng cơ chế chia sẻ công suất song song (Part-time 50-50 / Job-sharing) kết hợp bố trí nhân sự cấp thấp hơn hỗ trợ dưới sự hướng dẫn của chuyên gia. |  | Lỗi: tỷ lệ 50/50 và cơ chế job-sharing không có trong Phần I |
| Bảng 5, dòng 5 |  | (giữ) \| 1 \| Điểm xung đột dưới Mức 3 (không quá 120% và không thuộc dự án Hạng ưu tiên 1) \| Chỉ ghi nhận để theo dõi; UC kết thúc (QT-33). | Lỗi: “< 20%”, “chuyển PM tự đàm phán” không có trong Phần I |
| Bảng 6, dòng 1 |  | CN-78 \| PM các dự án liên quan đàm phán chia sẻ, thay thế hoặc điều chỉnh nhu cầu nguồn lực. \| Bước 3 | Lỗi: dùng nhầm mã CN-01..14, QT-01..08 của V2; đổi theo mã V7 trong Phần I |
| Bảng 6, dòng 2 |  | CN-79 \| RM điều phối, ghi nhận phương án thống nhất hoặc yêu cầu chuyển cấp; theo dõi hạn 3 ngày làm việc. \| Bước 1, 2, 4; A1 | Lỗi: dùng nhầm mã CN-01..14, QT-01..08 của V2; đổi theo mã V7 trong Phần I |
| Bảng 6, dòng 3 |  | CN-80 \| Làm mịn trong khoảng dự trữ, không tự thay đổi ngày hoàn thành. \| Bước 5 | Lỗi: dùng nhầm mã CN-01..14, QT-01..08 của V2; đổi theo mã V7 trong Phần I |
| Bảng 6, dòng 4 |  | CN-81 \| San bằng nguồn lực trong hạn mức công suất khi hết khoảng dự trữ. \| A2 | Lỗi: dùng nhầm mã CN-01..14, QT-01..08 của V2; đổi theo mã V7 trong Phần I |
| Bảng 6, dòng 5 |  | CN-82 \| Đề xuất lùi mốc tiến độ gốc hoặc cắt giảm phạm vi khi bế tắc hoàn toàn. \| A3 | Lỗi: dùng nhầm mã CN-01..14, QT-01..08 của V2; đổi theo mã V7 trong Phần I |
| Bảng 6, dòng 6 |  | CN-83 \| Chuyển hồ sơ chuyển cấp đến PMO/Quản lý danh mục khi hết hạn đàm phán hoặc bế tắc. \| A1 (sang UC-06.3) | Lỗi: dùng nhầm mã CN-01..14, QT-01..08 của V2; đổi theo mã V7 trong Phần I |
| Bảng 6, dòng 7 |  | CN-86, CN-87, CN-88 \| Đề xuất thay đổi qua V8 rà soát; ghi nhật ký xử lý xung đột; bàn giao phương án cho V8, V9, V10. \| Bước 7–9; A3 | Lỗi: dùng nhầm mã CN-01..14, QT-01..08 của V2; đổi theo mã V7 trong Phần I |
| Bảng 6, dòng 8 |  | QT-32 \| Tổng tỷ lệ phân bổ của một người trên tất cả dự án không quá 100% công suất chuẩn. \| Bước 6 | Lỗi: dùng nhầm mã CN-01..14, QT-01..08 của V2; đổi theo mã V7 trong Phần I |
| Bảng 6, dòng 9 |  | QT-33 \| Chỉ xử lý chính thức từ Mức 3 (trên 120% hoặc dự án Hạng ưu tiên 1); dưới ngưỡng chỉ theo dõi. \| E1 | Lỗi: dùng nhầm mã CN-01..14, QT-01..08 của V2; đổi theo mã V7 trong Phần I |
| Bảng 6, dòng 10 |  | QT-34 \| Ưu tiên phân bổ cứng đã cam kết trước; ngang nhau thì xét xếp hạng danh mục và giá trị kinh doanh. \| Bước 3 | Lỗi: dùng nhầm mã CN-01..14, QT-01..08 của V2; đổi theo mã V7 trong Phần I |
| Bảng 6, dòng 11 |  | QT-35 \| Làm mịn chỉ trong khoảng dự trữ, không tự lùi ngày hoàn thành khi chưa qua kiểm soát thay đổi. \| Bước 5 | Lỗi: dùng nhầm mã CN-01..14, QT-01..08 của V2; đổi theo mã V7 trong Phần I |
| Bảng 6, dòng 12 |  | QT-36 \| PM tự đàm phán tối đa 3 ngày làm việc; PMO quyết định trong 1 ngày làm việc; Mức 4–5 chuyển CEO/Managing Director. \| Bước 2; A1 | Lỗi: dùng nhầm mã CN-01..14, QT-01..08 của V2; đổi theo mã V7 trong Phần I |
| Bảng 6, dòng 13 |  | QT-37 \| Bế tắc hoàn toàn buộc chọn lùi mốc tiến độ gốc hoặc cắt giảm phạm vi. \| A3 | Lỗi: dùng nhầm mã CN-01..14, QT-01..08 của V2; đổi theo mã V7 trong Phần I |
| Bảng 6, dòng 14 |  | QT-38, QT-39; PCN-06 \| Ghi mọi điểm xung đột, đàm phán, phân xử vào nhật ký, lưu tối thiểu 3 năm; đề xuất thay đổi qua V8 rà soát trước. \| Bước 7, 9; A3 | Lỗi: dùng nhầm mã CN-01..14, QT-01..08 của V2; đổi theo mã V7 trong Phần I |
| Đoạn 21 | • Điểm bắt đầu (Initial Node): RM chọn điểm xung đột quá tải Mức 3 từ danh sách cảnh báo hệ thống. | • Điểm bắt đầu: RM chọn điểm xung đột cần cân đối từ danh sách của UC-06.1. | Lỗi phạm vi: phân tích ngưỡng thuộc UC-06.1, phân xử thuộc UC-06.3 (extend); PMO không thao tác trong UC-06.2 |
| Đoạn 22 | • Swimlanes (4 Làn vai trò): Quản lý nguồn lực (RM), Quản lý dự án (PM), Hệ thống (System), PMO / Quản lý danh mục. | • Swimlanes: RM, PM, Hệ thống. PMO/Quản lý danh mục không có action trong UC-06.2. | Lỗi phạm vi: phân tích ngưỡng thuộc UC-06.1, phân xử thuộc UC-06.3 (extend); PMO không thao tác trong UC-06.2 |
| Đoạn 24 |    - Đủ ngưỡng Mức 3 (>120% / Rank 1)? (Nếu không -> Luồng E1 kết thúc sớm; Nếu có -> Phân tích CPM/Float). |    - Mức 3 trở lên? (Không → E1 chỉ theo dõi, kết thúc.) | Lỗi: “< 20%”; theo QT-33 |
| Đoạn 25 |    - Đàm phán thành công trong 03 ngày? (Nếu bế tắc -> Luồng A1 leo thang PMO; Nếu thành công -> Cân đối kỹ thuật). |    - Kết quả đàm phán? (Quá 3 ngày làm việc hoặc bế tắc → A1 chuyển UC-06.3; Thống nhất → ghi nhận.) | Guard theo CN-79 |
| Đoạn 26 |    - Total Float > 0? (Nếu có Float -> Resource Smoothing; Nếu hết Float -> Resource Leveling / Deadlock Protocol). |    - Còn khoảng dự trữ? (Còn → làm mịn; Hết → Bế tắc hoàn toàn? Không → A2 san bằng; Có → A3 đề xuất thay đổi.) Ba nhánh hội tụ ở một merge trước bước 6. | Lỗi: các nhánh làm mịn, san bằng, bế tắc nối nhầm; tách nhánh có guard |
| Đoạn 27 | • Điểm kết thúc (Activity Final Node): Kết thúc sớm (E1) hoặc Kết thúc chính (sau khi lưu Conflict Log vĩnh viễn và xuất dữ liệu bàn giao V8/V9/V10). | • Điểm kết thúc: E1 (theo dõi), A1 (chuyển UC-06.3) hoặc kết thúc chính sau khi lưu nhật ký và chuyển phương án sang V8, V9, V10. | Bỏ “vĩnh viễn” |
| Ảnh ở đoạn 30 |  | AD_UC-06.2.png | AD vẽ lại bằng draw.io: mỗi nhánh tới đúng action, làn trùng actor trong D, guard theo CN-79 |
| Bảng 7, dòng 1 |  | (giữ) \| (giữ) \| RM, PM. PMO/Quản lý danh mục phân xử ở UC-06.3. | Lỗi phạm vi: phân tích ngưỡng thuộc UC-06.1, phân xử thuộc UC-06.3 (extend); PMO không thao tác trong UC-06.2 |
| Bảng 7, dòng 2 |  | (giữ) \| (giữ) \| Association; UC-06.3 extend UC-06.2. | Lỗi phạm vi: phân tích ngưỡng thuộc UC-06.1, phân xử thuộc UC-06.3 (extend); PMO không thao tác trong UC-06.2 |
| Bảng 7, dòng 3 |  | (giữ) \| (giữ) \| 9 bước trên AD khớp bước 1–9 của luồng chính; các nhánh A1, A2, A3, E1. | Theo D đã sửa |
| Bảng 7, dòng 4 |  | (giữ) \| (giữ) \| PhuongAnBoTri, DiemXungDot, NhatKyXuLyXungDot, DeXuatThayDoi, PhanXuXungDot. | Tên lớp theo II.3 |
| Bảng 7, dòng 5 |  | (giữ) \| (giữ) \| Chọn điểm xung đột → đàm phán → làm mịn, san bằng hoặc đề xuất thay đổi → ghi nhật ký → bàn giao. | Theo D đã sửa |
| Bảng 7, dòng 6 |  | (giữ) \| (giữ) \| A1 (hết hạn hoặc bế tắc), A2 (san bằng), A3 (bế tắc hoàn toàn), E1 (dưới Mức 3). | Theo D đã sửa |
| Bảng 7, dòng 7 |  | (giữ) \| (giữ) \| Bắt đầu khi chọn điểm xung đột; kết thúc sau khi lưu nhật ký và chuyển phương án sang V8, V9, V10. | Bỏ “vĩnh viễn” |
| Bảng 8, 9, 10, 11, 12, 13, 14, 16, 17 | DiemXungDotNguonLuc, ConflictLog, ChangeRequest, PhuongAnNguonLuc, QuyetDinhPhanXu | DiemXungDot, NhatKyXuLyXungDot, DeXuatThayDoi, PhuongAnBoTri, PhanXuXungDot | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) (47 chỗ) |
| Bảng 8, dòng 1 |  | Phương án bố trí (PhuongAnBoTri) \| Có \| Phương án từ V6 được cân đối và bàn giao V8, V9, V10. | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) |
| Bảng 8, dòng 2 |  | Điểm xung đột (DiemXungDot) \| Có \| Điểm vượt ngưỡng công suất của một nguồn lực, mức cảnh báo theo thang 5 mức (CN-74). | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) |
| Bảng 8, dòng 3 |  | (giữ) \| Không \| Kịch bản thuộc phân tích ở UC-06.1 (CN-77); kết quả được ghi vào phương án và nhật ký. | Lỗi phạm vi: phân tích ngưỡng thuộc UC-06.1, phân xử thuộc UC-06.3 (extend); PMO không thao tác trong UC-06.2 |
| Bảng 8, dòng 4 |  | (giữ) \| Không \| Ghi thành dòng NhatKyXuLyXungDot loại “đàm phán” (CN-79, QT-38). | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) |
| Bảng 8, dòng 5 |  | Hồ sơ chuyển cấp và quyết định phân xử (PhanXuXungDot) \| Có \| Một lớp; thuộc UC-06.3 (CN-83–CN-85). | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) |
| Bảng 8, xóa dòng 6 | Quyết định phân xử (PhanXuXungDot) \| Có \| Thực thể lưu phán quyết cưỡng chế từ PMO/CEO theo Portfolio Rank, khống chế SLA 01 ngày. |  | Gộp vào PhanXuXungDot |
| Bảng 8, dòng 7 |  | Nhật ký xử lý xung đột (NhatKyXuLyXungDot) \| Có \| Ghi mọi điểm xung đột, đàm phán và phân xử; lưu tối thiểu 3 năm (CN-87, QT-38, PCN-06). | Bỏ “vĩnh viễn”, “Audit Trail” |
| Bảng 8, dòng 8 |  | Đề xuất thay đổi (DeXuatThayDoi) \| Có \| Lùi mốc tiến độ gốc hoặc cắt giảm phạm vi (CN-82, CN-86). | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) |
| Bảng 9, dòng 1 |  | Ghi nhận điểm xung đột cần cân đối \| DiemXungDot \| Lấy từ UC-06.1 (CN-74). | Mã theo Phần I; bỏ “vĩnh viễn”, “không cho sửa/xóa”; phạm vi UC-06.2 |
| Bảng 9, dòng 2 |  | Phân tích đường găng, khoảng dự trữ \| Không thuộc UC-06.2 \| Thuộc UC-06.1 (CN-77). | Mã theo Phần I; bỏ “vĩnh viễn”, “không cho sửa/xóa”; phạm vi UC-06.2 |
| Bảng 9, dòng 3 |  | Làm mịn, san bằng \| PhuongAnBoTri \| Điều chỉnh thời điểm, tỷ lệ trên các dòng bố trí (CN-80, CN-81). | Mã theo Phần I; bỏ “vĩnh viễn”, “không cho sửa/xóa”; phạm vi UC-06.2 |
| Bảng 9, dòng 4 |  | Ghi nhận thỏa thuận đàm phán \| NhatKyXuLyXungDot \| Theo dõi hạn 3 ngày làm việc (CN-79). | Mã theo Phần I; bỏ “vĩnh viễn”, “không cho sửa/xóa”; phạm vi UC-06.2 |
| Bảng 9, dòng 5 |  | Chuyển hồ sơ chuyển cấp \| PhanXuXungDot \| Sang UC-06.3 (CN-83). | Mã theo Phần I; bỏ “vĩnh viễn”, “không cho sửa/xóa”; phạm vi UC-06.2 |
| Bảng 9, dòng 6 |  | Ghi quyết định phân xử \| PhanXuXungDot \| PMO hoặc CEO quyết định; lớp chỉ ghi nhận (UC-06.3, CN-84, CN-85). | Mã theo Phần I; bỏ “vĩnh viễn”, “không cho sửa/xóa”; phạm vi UC-06.2 |
| Bảng 9, dòng 7 |  | Lập đề xuất thay đổi \| DeXuatThayDoi \| Lùi mốc tiến độ gốc hoặc cắt giảm phạm vi (CN-82). | Mã theo Phần I; bỏ “vĩnh viễn”, “không cho sửa/xóa”; phạm vi UC-06.2 |
| Bảng 9, dòng 8 |  | Ghi nhật ký \| NhatKyXuLyXungDot \| Lưu tối thiểu 3 năm (CN-87, QT-38, PCN-06). | Mã theo Phần I; bỏ “vĩnh viễn”, “không cho sửa/xóa”; phạm vi UC-06.2 |
| Bảng 10, dòng 1 |  | PhuongAnBoTri \| Phương án bố trí được cân đối, bàn giao V8, V9, V10. \| CN-88; II.3 (V6) | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) |
| Bảng 10, dòng 2 |  | DiemXungDot \| Điểm vượt ngưỡng công suất, mức cảnh báo theo thang 5 mức. \| CN-74; QT-33 | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) |
| Bảng 10, xóa dòng 3 | KichBanCanDoi \| Lưu trữ các kịch bản mô phỏng kỹ thuật (Resource Smoothing / Resource Leveling). \| CN-05, CN-08, CN-09 |  | Kịch bản thuộc UC-06.1 |
| Bảng 10, xóa dòng 4 | BienBanDamPhan \| Quản lý diễn biến thương lượng % FTE giữa các PM, đếm ngược SLA đàm phán 03 ngày. \| CN-06, CN-07; QT-04 |  | Ghi thành nhật ký |
| Bảng 10, dòng 5 |  | PhanXuXungDot \| Hồ sơ chuyển cấp và quyết định phân xử. \| CN-83–CN-85; QT-36 | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) |
| Bảng 10, xóa dòng 6 | PhanXuXungDot \| Lưu phán quyết cưỡng chế từ PMO/CEO theo Portfolio Rank, khống chế SLA 01 ngày. \| CN-12; QT-02, QT-04 |  | Gộp vào PhanXuXungDot |
| Bảng 10, dòng 7 |  | NhatKyXuLyXungDot \| Nhật ký mọi điểm xung đột, đàm phán, phân xử; lưu tối thiểu 3 năm. \| CN-87; QT-38; PCN-06 | Bỏ “vĩnh viễn” |
| Bảng 10, dòng 8 |  | DeXuatThayDoi \| Đề xuất lùi mốc tiến độ gốc hoặc cắt giảm phạm vi. \| CN-82, CN-86; QT-37, QT-39 | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) |
| Bảng 11, dòng 1 |  | PhuongAnBoTri \| maPhuongAn, phienBan, loaiPhuongAn, trangThai \| Phương án được cân đối. | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) |
| Bảng 11, dòng 2 |  | DiemXungDot \| maXungDot, mucSuDung, mucCanhBao \| Mức sử dụng và mức cảnh báo (thang 5 mức). | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) |
| Bảng 11, xóa dòng 3 | KichBanCanDoi \| maKichBan, loaiKichBan (Smoothing, Leveling), floatSuDung, ngayHoanThanhMoi, coThayDoiBaseline \| Cấu hình tham số mô phỏng kịch bản cân đối kỹ thuật. |  | Kịch bản thuộc UC-06.1 |
| Bảng 11, xóa dòng 4 | BienBanDamPhan \| maBienBan, danhSachPM, tyLeFTEShare, nhanSuThayTheId, thoiHanDamPhanMax (3d), trangThaiDamPhan \| Quản lý diễn biến đàm phán thương lượng % FTE và đếm ngược. |  | Ghi thành nhật ký |
| Bảng 11, dòng 5 |  | PhanXuXungDot \| ngayChuyenCap, lyDoBeTac, capPhanXu, noiDungQuyetDinh \| Hồ sơ chuyển cấp và quyết định (UC-06.3). | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) |
| Bảng 11, xóa dòng 6 | PhanXuXungDot \| maPhanXu, pmoId, portfolioRankApDung, noiDungPhanXu, ngayBanHanh, thoiHanSLAMax (1d) \| Chứa nội dung phán quyết cưỡng chế từ PMO theo Portfolio Rank. |  | Gộp vào PhanXuXungDot |
| Bảng 11, dòng 7 |  | NhatKyXuLyXungDot \| thoiDiem, noiDung, loaiXuLy \| loaiXuLy: đàm phán, làm mịn, san bằng, phân xử; lưu tối thiểu 3 năm (PCN-06). | Bỏ “vĩnh viễn”, auditTrailHash |
| Bảng 11, dòng 8 |  | DeXuatThayDoi \| loaiThayDoi, noiDung \| loaiThayDoi: lùi mốc tiến độ gốc, cắt giảm phạm vi. | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) |
| Bảng 12, dòng 1 |  | PhuongAnBoTri \| lamMin(), sanBang(), banGiao() \| CN-80, CN-81, CN-88. | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) |
| Bảng 12, dòng 2 |  | DiemXungDot \| capNhatTrangThai() \| Cập nhật tình trạng xử lý của điểm xung đột. | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) |
| Bảng 12, xóa dòng 3 | KichBanCanDoi \| chayMoPhongSmoothing(), chayMoPhongLeveling() \| Thuật toán mô phỏng dời lịch trong Float hoặc san bằng công suất. |  | Kịch bản thuộc UC-06.1 |
| Bảng 12, dòng 4 |  | NhatKyXuLyXungDot \| ghiNhan(loaiXuLy, noiDung) \| Ghi đàm phán, điều chỉnh, phân xử (CN-79, CN-87). | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) |
| Bảng 12, dòng 5 |  | PhanXuXungDot \| chuyenCap() \| RM chuyển hồ sơ sang UC-06.3 (CN-83). | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) |
| Bảng 12, dòng 6 |  | PhanXuXungDot \| ghiQuyetDinh() \| Người quyết định là PMO hoặc CEO; lớp chỉ ghi nhận (CN-84, CN-85). | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) |
| Bảng 12, xóa dòng 7 | NhatKyXuLyXungDot \| ghiVetVinhVien(), truyXuatLichSu() \| Tự động ghi vết Audit Log vĩnh viễn và cho phép tra cứu lịch sử. |  | Gộp vào NhatKyXuLyXungDot.ghiNhan; bỏ “vĩnh viễn” |
| Bảng 12, dòng 8 |  | DeXuatThayDoi \| lapDeXuat(), chuyenV8() \| CN-82, CN-86. | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) |
| Bảng 13, dòng 1 |  | PhuongAnBoTri \| Association \| DiemXungDot \| Phương án có các điểm xung đột cần cân đối. | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) |
| Bảng 13, xóa dòng 2 | DiemXungDot \| Association \| KichBanCanDoi \| Một điểm xung đột có thể chạy thử nhiều kịch bản cân đối (Smoothing / Leveling). |  | Kịch bản thuộc UC-06.1 |
| Bảng 13, dòng 3 |  | DiemXungDot \| Composition \| NhatKyXuLyXungDot \| Mỗi điểm xung đột có các dòng nhật ký xử lý (QT-38). | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) |
| Bảng 13, xóa dòng 4 | BienBanDamPhan \| Association \| HoSoLeoThang \| Đàm phán bế tắc quá 3 ngày sẽ khởi tạo 1 hồ sơ leo thang gửi PMO. |  | Gộp vào PhanXuXungDot |
| Bảng 13, dòng 5 |  | DiemXungDot \| Association \| PhanXuXungDot \| Điểm xung đột được chuyển cấp có một hồ sơ phân xử. | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) |
| Bảng 13, xóa dòng 6 | DiemXungDot \| Composition \| NhatKyXuLyXungDot \| Bắt buộc mỗi điểm xung đột phải khởi tạo duy nhất 1 Nhật ký ghi vết (Conflict Log) vĩnh viễn. |  | Thay bằng quan hệ DiemXungDot–NhatKyXuLyXungDot |
| Bảng 13, dòng 7 |  | PhuongAnBoTri \| Association \| DeXuatThayDoi \| Phương án có thể kèm đề xuất thay đổi khi bế tắc hoàn toàn. | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) |
| Bảng 14, dòng 1 |  | PhuongAnBoTri — DiemXungDot \| 1 : 0..* \| Một phương án có không hoặc nhiều điểm xung đột. | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) |
| Bảng 14, xóa dòng 2 | DiemXungDot — KichBanCanDoi \| 1 : 0..* \| Một điểm xung đột có thể tạo nhiều kịch bản mô phỏng để so sánh. |  | Kịch bản thuộc UC-06.1 |
| Bảng 14, dòng 3 |  | DiemXungDot — NhatKyXuLyXungDot \| 1 : 1..* \| Ít nhất có dòng ghi nhận điểm xung đột (QT-38). | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) |
| Bảng 14, xóa dòng 4 | BienBanDamPhan — HoSoLeoThang \| 1 : 0..1 \| Khi đàm phán bế tắc quá 3 ngày mới tạo 1 hồ sơ leo thang gửi PMO. |  | Gộp vào PhanXuXungDot |
| Bảng 14, dòng 5 |  | DiemXungDot — PhanXuXungDot \| 1 : 0..1 \| Chỉ khi hết hạn đàm phán hoặc bế tắc. | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) |
| Bảng 14, xóa dòng 6 | DiemXungDot — NhatKyXuLyXungDot \| 1 : 1 \| Quan hệ Composition 1:1 bắt buộc tự động lưu vết vĩnh viễn (PCN-04). |  | Thay bằng DiemXungDot–NhatKyXuLyXungDot |
| Bảng 14, dòng 7 |  | PhuongAnBoTri — DeXuatThayDoi \| 1 : 0..* \| Đề xuất chỉ có khi bế tắc hoàn toàn. | Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4) |
| Ảnh ở đoạn 51 |  | II3-4_Phuong_an_xung_dot_phe_duyet.png | Sơ đồ lớp theo mô hình thống nhất (Hình II.3-4, nguồn draw.io) |
| Bảng 16, dòng 1, cột 0 | QT-01 (RB-01) | QT-32 | Lỗi: dùng nhầm mã CN-01..14, QT-01..08 của V2; đổi theo mã V7 trong Phần I |
| Bảng 16, dòng 2, cột 0 | QT-02 | QT-34 | Lỗi: dùng nhầm mã CN-01..14, QT-01..08 của V2; đổi theo mã V7 trong Phần I |
| Bảng 16, dòng 3, cột 0 | QT-03 (RB-02) | QT-35 | Lỗi: dùng nhầm mã CN-01..14, QT-01..08 của V2; đổi theo mã V7 trong Phần I |
| Bảng 16, dòng 4, cột 0 | QT-04 (RB-03) | QT-36 | Lỗi: dùng nhầm mã CN-01..14, QT-01..08 của V2; đổi theo mã V7 trong Phần I |
| Bảng 16, dòng 5, cột 0 | QT-05 (RB-04) | QT-33 | Lỗi: dùng nhầm mã CN-01..14, QT-01..08 của V2; đổi theo mã V7 trong Phần I |
| Bảng 16, dòng 6, cột 0 | QT-07 | QT-37 | Lỗi: dùng nhầm mã CN-01..14, QT-01..08 của V2; đổi theo mã V7 trong Phần I |
| Bảng 16, dòng 2 |  | (giữ) \| Tranh chấp: ưu tiên phân bổ cứng đã cam kết trước; ngang nhau thì xét xếp hạng danh mục và giá trị kinh doanh. \| (giữ) \| (giữ) | Theo QT-34 |
| Bảng 16, dòng 7 |  | QT-38; PCN-06 \| Mọi điểm xung đột, đàm phán và phân xử được ghi vào nhật ký xử lý xung đột. \| Lưu tối thiểu 3 năm \| Bước 7, 9; lớp NhatKyXuLyXungDot | Bỏ “vĩnh viễn” |
| Bảng 17, dòng 2 |  | (giữ) \| Khối lượng làm thêm giờ khẩn cấp (Mức 5) nếu có \| (giữ) \| (giữ) | Bỏ “thuê ngoài khẩn cấp”: không có trong Phần I |

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
| Bảng 14, dòng 15, cột 2 | (A3) | (UC-08.3) | A3 cũ đã chuyển sang FDS 08.3 |
| Bảng 14, xóa dòng 18 | NguoiDung (PM) – DanhGiaChiPhi \| 1 – 0..* \| PM thực hiện nhiều lần đánh giá. |  | Bỏ NguoiDung |
| Bảng 14, xóa dòng 19 | NguoiDung (Tài chính) – DonGia \| 1 – 0..* \| Tài chính cập nhật nhiều đơn giá. |  | Bỏ NguoiDung |
| Bảng 14, xóa dòng 20 | NguoiDung (Tài chính) – ChiPhiThucTe \| 1 – 0..* \| Tài chính ghi nhận nhiều khoản chi phí thực tế. |  | Bỏ NguoiDung |
| Bảng 14, xóa dòng 21 | NguoiDung – DuBaoChiPhi \| 1 – 0..* \| Một tài khoản cập nhật nhiều dự báo. |  | Bỏ NguoiDung |
| Bảng 14, xóa dòng 22 | NguoiDung – SoSanhPhuongAn \| 1 – 0..* \| Một tài khoản thực hiện nhiều lần so sánh. |  | Bỏ NguoiDung |
| Xóa đoạn 32 | PhuongAnBoTri Cost Management Framework-2026-10-14-161441.pdf tải về để xem rõ bản vẽ |  | Ghi chú tải file PDF, không thuộc nội dung báo cáo |
| Ảnh ở đoạn 35 |  | II3-5_Chi_phi_ngan_sach.png | Sơ đồ lớp theo mô hình thống nhất (Hình II.3-5, nguồn draw.io) |

## P1 — [PTTKHT] I - PHÂN TÍCH YÊU CẦU FINAL.docx

| Vị trí (theo bản gốc) | Trước | Sau | Lý do |
|---|---|---|---|
| Bảng 0, dòng 5, cột 1 | Xác nhận kết quả đánh giá năng lực ở cấp cuối khi có tranh chấp. | Xác nhận kết quả đánh giá năng lực ở cấp cuối khi có tranh chấp. Phê duyệt tiêu chí tạm cho kỹ năng chưa có tiêu chí. Phê duyệt miễn trừ điều kiện bắt buộc và điều chỉnh xếp hạng, shortlist của RM. | QĐ-01: CN-37, CN-43 (V4) giao PMO/Quản lý danh mục phê duyệt miễn trừ và điều chỉnh xếp hạng, shortlist; bảng vai trò và bảng V4 chưa ghi; CN-19 (V3) phê duyệt tiêu chí tạm |
| Bảng 0, dòng 5, cột 2 | V3, V5, V7, V8, V9 | V3, V4, V5, V7, V8, V9 | QĐ-01: CN-37, CN-43 (V4) giao PMO/Quản lý danh mục phê duyệt miễn trừ và điều chỉnh xếp hạng, shortlist; bảng vai trò và bảng V4 chưa ghi |
| Bảng 4, dòng 1, cột 1 | RM | RM; PMO/Quản lý danh mục phê duyệt miễn trừ điều kiện bắt buộc và điều chỉnh xếp hạng, shortlist (CN-37, CN-43) | QĐ-01: CN-37, CN-43 (V4) giao PMO/Quản lý danh mục phê duyệt miễn trừ và điều chỉnh xếp hạng, shortlist; bảng vai trò và bảng V4 chưa ghi |
| Bảng 13, dòng 35, cột 1 |  (Nguồn V6 ghi nhận là ) |  | Bỏ cụm chú thích còn dở, không có nội dung |
