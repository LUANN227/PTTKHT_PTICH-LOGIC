# II.3 — Sơ đồ lớp miền tổng quát: danh mục, ánh xạ và điểm chờ quyết định

- **File nguồn:** `II3_Lop_Mien_Tong_Quat.puml` (PlantUML, sửa được). Bản mở bằng draw.io: `II3_Lop_Mien_Tong_Quat.drawio`.
- **Khung nhìn để trình bày** (sinh tự động từ file nguồn bằng `../_cong_cu/tach_view_II3.py`, không sửa tay):
  - `II3_Tong_Quan_Ten_Lop`: chỉ tên lớp và liên kết, dùng làm hình chính trong bài;
  - `II3_View_A_V2-V4`, `II3_View_B_V5-V7`, `II3_View_C_V8-V10`: từng nhóm vùng, đủ thuộc tính; lớp vùng khác vẽ xám, chỉ ghi tên.
  - Ba khung nhìn phủ đủ 49 lớp (20 + 12 + 17); không lớp nào bị bỏ hoặc lặp.
- **Bản xuất:** `.png` để nhúng vào tài liệu, `.svg` để phóng to.
- **Quy ước của sơ đồ:** mỗi package tương ứng một vùng nghiệp vụ chịu trách nhiệm chính cho lớp đó. Sơ đồ chỉ ghi thuộc tính chính và ẩn thao tác, vì đây là mô hình miền. Lớp gắn `<<đề xuất>>` chưa đủ căn cứ ngoài bài của một thành viên.
- **Nguồn đã đọc:** bài V2a, V2b (bản mới nhất do trưởng nhóm gửi), V3, V4, V5, V6, V7, V8 (sơ đồ lớp mới gửi kèm), V9; bài V10 trong thư mục này; P1.

## 1. Danh mục lớp

Mức chắc chắn: **C** = có căn cứ trong P1; **TV** = chỉ có căn cứ trong bài thành viên; **Đ** = đề xuất tích hợp.

| Lớp | Ý nghĩa | Vùng chịu trách nhiệm | Căn cứ chính | Mức |
|---|---|---|---|---|
| DuAn | Dự án dùng nguồn lực, có hạng ưu tiên | V2 (dùng chung) | P1 I.1.1; xếp hạng ưu tiên (V7, RB-59 Mức 3) | C |
| GiaiDoanDuAn | Giai đoạn của dự án | V2/V6 | QT-29 (phân bổ theo giai đoạn); bài V6 | C |
| NhuCauNguonLuc | Nhu cầu nguồn lực do PM lập, RM xác nhận | V2 | CN-01..17, RB-06 | C |
| ViTriCanBoTri | Vị trí (vai trò, số lượng, %FTE) trong nhu cầu | V2 | P1 I.1.3.6 đầu vào ("vai trò, số lượng, kỹ năng, thời gian, mức độ tham gia"); CN-60 | C |
| YeuCauKyNang | Kỹ năng mà vị trí đòi hỏi | V2 | P1 I.1.3.6 đầu vào; bài V2a (KyNangChuyenMon) | C |
| PhanHoiNhuCau | Phản hồi từ V4/V10 để PM xem lại nhu cầu | V2 | CN-17 | C |
| YeuCauNguonLuc | Yêu cầu nguồn lực của dự án mới hoặc mở rộng, có khung thời gian, gửi V5 | V5 | CN-127 | Đ (Q-03) |
| NguonLuc | Người có thể bố trí: nội bộ, cộng tác viên/đối tác, tuyển ngoài | V3 (dùng chung) | P1 I.1.1 (thứ tự huy động) | C |
| KyNang | Danh mục kỹ năng | V3 | CN-18..; bài V3, V4 | C |
| HoSoNangLuc | Hồ sơ năng lực tập trung (Skill Matrix) | V3 | P1 I.1.3.3 kết quả; PCN-02; CN-29, 30 | C |
| NangLucKyNang | Mức thành thạo một kỹ năng, trạng thái xác nhận | V3 | P1 I.1.3.3 ("đã xác nhận hoặc tự khai báo") | C |
| BoTieuChiNangLuc | Bộ tiêu chí đánh giá năng lực chung | V3 | CN-18, QT-01 | C |
| TieuChiNangLuc | Một tiêu chí năng lực | V3 | QT-01 | C |
| MucDoNangLuc | Mức của tiêu chí và điều kiện công nhận | V3 | QT-02..04. Số mức do P1 quy định, xem Q-07 | C |
| BoTieuChiPhuHop | Bộ điều kiện bắt buộc, tiêu chí, trọng số cho một nhu cầu | V4 | CN-32, QT-19 | C |
| TieuChiPhuHop | Điều kiện bắt buộc hoặc tiêu chí có trọng số | V4 | CN-32, 34 | C |
| PhienTimKiem | Một lần tìm kiếm và đánh giá cho một nhu cầu | V4 | CN-33, 44 | C |
| KetQuaDanhGiaPhuHop | Phân loại, điểm, thứ hạng, vai trò shortlist của một nguồn lực | V4 | CN-34, 38, 39, 41 | C |
| DiemTieuChi | Điểm theo từng tiêu chí | V4 | CN-38 | C |
| DeNghiMienTru | Đề nghị miễn trừ điều kiện bắt buộc, PMO duyệt | V4 | CN-37, QT-13 | C |
| LichNguonLuc | Lịch nguồn lực tập trung của một nguồn lực | V5 (dùng chung) | PCN-02 | C |
| PhanBoNguonLuc | Bản ghi phân bổ cứng hoặc mềm trên lịch | V5 | P1 I.1.2 (thuật ngữ); CN-49 | C |
| KetLuanKhaNangThamGia | Kết luận 4 trạng thái, mức sử dụng, cờ rủi ro | V5 | P1 I.1.3.5; CN-50, 59 | C |
| DeXuatThamGiaMotPhan | Tỷ lệ, thời gian đề xuất khi chỉ tham gia được một phần | V5 | CN-53 (UC-04.2) | C |
| HoSoVuotTaiNgoaiLe | Trường hợp vượt tải chuyển cấp theo DoA | V5 | CN-56 (UC-04.3) | C |
| PhuongAnBoTri | Phương án chính hoặc thay thế, có phiên bản và trạng thái | V6 | CN-62, 65; P1 I.1.3.8 bước 5 (phiên bản) | C |
| ChiTietBoTri | Một dòng bố trí: người, vị trí, giai đoạn, tỷ lệ | V6 | CN-62, QT-29 | C |
| RuiRoViTri | Rủi ro và biện pháp của vị trí rủi ro cao | V6 | CN-64..66 | C |
| DiemXungDot | Điểm vượt ngưỡng công suất, có Mức cảnh báo | V7 | CN-74; RB-59 | C |
| NhatKyXuLyXungDot | Nhật ký mọi điểm xung đột, đàm phán, phân xử | V7 | CN-87 | C |
| PhanXuXungDot | Hồ sơ chuyển cấp và quyết định phân xử của PMO/CEO | V7 | P1 I.1.2 (PMO "tiếp nhận hồ sơ chuyển cấp và phân xử"); UC-06.3 | C |
| DeXuatThayDoi | Đề xuất thay đổi tiến độ/phạm vi kèm phương án đã cân đối | V7 | P1 I.1.3.7 kết quả ("đề xuất thay đổi (nếu có)") | Đ (Q-09) |
| HoSoTrinhDuyet | Một lần trình duyệt phương án: mức rủi ro, cấp thẩm quyền | V8 | CN-89..91; P1 I.1.3.8 | C |
| YeuCauGiaiTrinh | Yêu cầu RM giải trình, hoàn thiện | V8 | CN-95 (UC-07.2) | C |
| QuyetDinhPheDuyet | Quyết định (phê duyệt, yêu cầu chỉnh sửa, từ chối, duyệt ngoại lệ), lý do, điều kiện, người, thời điểm | V8 | P1 I.1.3.8 kết quả, bước 5; CN-99, 101 | C |
| DonGia, DuToanChiPhi, DuBaoChiPhi, ChiPhiThucTe, NganSach, DanhGiaChiPhi, NguyenNhanVuot, HuongXuLy, SoSanhPhuongAn, ChiTietSoSanh | Giữ theo bài V9 | V9 | CN-103..112; P1 I.1.3.9 | C (theo bài V9; công thức chờ D-20) |
| KetQuaDuBao, TongHopNguonCung, NhuCauDuBao, DongDoiChieuCungCau | Xem bài V10 | V10 | CN-113..126 | C |

## 2. Quan hệ và bội số chính

Ghi đủ trong file `.puml`. Bảng này chỉ nêu các quan hệ dễ gây tranh luận.

| Quan hệ | Bội số | Căn cứ |
|---|---|---|
| NhuCauNguonLuc ◆ ViTriCanBoTri | 1 – 1..* | Nhu cầu nêu rõ vai trò, số lượng (P1 I.1.3.6) |
| ViTriCanBoTri – GiaiDoanDuAn | 0..* – 0..1 | QT-29 phân bổ theo giai đoạn. Vị trí có thể dùng cho cả dự án. Q-05 |
| NguonLuc – HoSoNangLuc | 1 – 1 | PCN-02: một nơi lưu |
| NguonLuc – LichNguonLuc | 1 – 1 | PCN-02: lịch tập trung. Bài V5 ghi 0..*, xem Q-06 |
| PhuongAnBoTri ◆ ChiTietBoTri | 1 – 1..* | Bài V6, V9 |
| ChiTietBoTri – PhanBoNguonLuc | 0..1 – 0..1 | Khi phương án thành Locked Baseline, dòng bố trí trở thành phân bổ cứng ("cam kết nguồn lực hiện có", P1 I.1.3.8). Trước đó chưa có phân bổ cứng |
| PhuongAnBoTri – HoSoTrinhDuyet | 1 – 0..* | Bị yêu cầu chỉnh sửa thì về V6/V7 rồi trình lại (CN-101). Bài V8 ghi 1:1, xem Q-02 |
| HoSoTrinhDuyet – QuyetDinhPheDuyet | 1 – 0..1 | Mỗi lần trình có tối đa một quyết định chính thức |
| HoSoTrinhDuyet – DanhGiaChiPhi / KetQuaDuBao | tham chiếu | V8 xem thông tin của V9, V10 (CN-93, 94). Không sao chép thành lớp riêng |
| KetQuaDanhGiaPhuHop – KetLuanKhaNangThamGia | 1 – 0..1 | Chỉ ứng viên trong shortlist được đánh giá khả năng tham gia (CN-45, V5) |

## 3. Ánh xạ lớp của thành viên sang lớp tổng quát

| Thành viên | Lớp trong bài | Lớp trong II.3 | Xử lý | Lý do ngắn |
|---|---|---|---|---|
| V2a | DuAn | DuAn | Giữ | |
| V2a | CongViec | NhuCauNguonLuc.phamViCongViec | Hợp nhất thành thuộc tính | P1 dùng "phạm vi, khối lượng, tiến độ" làm căn cứ nhu cầu, không có khái niệm công việc có vòng đời riêng. Q-05 |
| V2a | NhuCauNguonLuc | NhuCauNguonLuc | Giữ, bỏ `chiSoFTE` và `soLuongNhanSu` khỏi lớp nhu cầu | Số lượng và %FTE thuộc từng vị trí (ViTriCanBoTri) |
| V2a | KyNangChuyenMon | YeuCauKyNang + KyNang | Tách | Yêu cầu kỹ năng của vị trí khác với danh mục kỹ năng |
| V2b | NhuCauNguonLuc | NhuCauNguonLuc | Giữ; `quyMoFTE`, `tyLeFTE`, `loaiNguonLuc` chuyển về ViTriCanBoTri | Như trên |
| V2b | PhanHoiNhuCau | PhanHoiNhuCau | Giữ | CN-17 |
| V3 | RM | (bỏ) | Loại | Là actor |
| V3 | Yeucauquanlytieuchi | (bỏ) | Loại khỏi mô hình miền | Là thao tác của UC-02.1, không có vòng đời nghiệp vụ trong P1. Q-07 |
| V3 | Botieuchi / Tieuchidanhgia / Mucdo / Dieukien | BoTieuChiNangLuc / TieuChiNangLuc / MucDoNangLuc (dieuKienCongNhan) | Đổi tên; gộp DieuKien vào MucDo | Phân biệt với bộ tiêu chí V4. QT-03, 04 gắn điều kiện với mức |
| V3 | Kynang | KyNang | Giữ | |
| V3 | Nhatkythaydoi | (bỏ) | Loại | Bài tự ghi "đề xuất, chưa có trong V3" |
| V4 | NhuCauNguonLuc | NhuCauNguonLuc | Hợp nhất | Thuộc V2 |
| V4 | BoTieuChi / TieuChi | BoTieuChiPhuHop / TieuChiPhuHop | Đổi tên | Khác bộ tiêu chí năng lực V3 |
| V4 | PhienDanhGia | PhienTimKiem | Đổi tên | Tránh trùng "đánh giá" của V3, V5 |
| V4 | UngVien | NguonLuc | Hợp nhất | "Ứng viên" là vai trò của nguồn lực trong một lần tìm kiếm. Thuộc tính `nguonUngVien` thành `NguonLuc.loaiNguon`. `coXungDotLoiIch` thành thuộc tính của KetQuaDanhGiaPhuHop. Q-04 |
| V4 | KyNang (có mucThanhThao) | NangLucKyNang | Đổi tên | Là năng lực của người, không phải danh mục |
| V4 | KetQuaDanhGia | KetQuaDanhGiaPhuHop | Đổi tên | |
| V4 | DiemTieuChi, DeNghiMienTru | Giữ | | |
| V4 | Shortlist | KetQuaDanhGiaPhuHop.vaiTroShortlist | Hợp nhất thành thuộc tính | Bài đã có vaiTroShortlist; lớp Shortlist chỉ còn mã và ngày |
| V4 | NguoiDung | (bỏ) | Loại | Là actor |
| V5 | YeuCauNguonLuc | YeuCauNguonLuc `<<đề xuất>>` | Giữ có điều kiện | Q-03 |
| V5 | NguonLuc, LichNguonLuc, PhanBoNguonLuc | Giữ | | |
| V5 | KetQuaDanhGia | KetLuanKhaNangThamGia | Đổi tên | Trùng tên lớp V4 |
| V5 | YeuCauXacNhan | KetLuanKhaNangThamGia.trangThaiKhaNang = "chờ xác nhận" | Hợp nhất | Bài tự ghi "lớp đề xuất nếu cần" |
| V5 | DeXuatThamGiaMotPhan, HoSoVuotTaiNgoaiLe | Giữ | | UC-04.2, 04.3 |
| V6 | DuAn, GiaiDoanDuAn, NhuCauNguonLuc, ViTriCanBoTri, NguonLuc, HoSoNangLuc, PhuongAnBoTri, ChiTietBoTri, RuiRoViTri | Giữ | | |
| V6 | LichPhanBo | PhanBoNguonLuc | Hợp nhất | Cùng là phân bổ trên lịch tập trung (PCN-02) |
| V6 | KhaNangThamGia | KetLuanKhaNangThamGia | Hợp nhất | Là kết luận của V5 |
| V7 | PhuongAnNguonLuc | PhuongAnBoTri | Hợp nhất | Cùng phương án; trạng thái xung đột thành trạng thái phương án |
| V7 | DiemXungDotNguonLuc | DiemXungDot | Giữ; bỏ freeFloat/totalFloat/CPM | Không có trong P1 |
| V7 | KichBanCanDoi | (bỏ) | Loại | P1 mô tả làm mịn/san bằng là hoạt động, không có đối tượng "kịch bản" |
| V7 | BienBanDamPhan | NhatKyXuLyXungDot (loaiXuLy = đàm phán) | Hợp nhất | CN-87 ghi đàm phán vào nhật ký |
| V7 | HoSoLeoThang + QuyetDinhPhanXu | PhanXuXungDot | Hợp nhất | Một lần chuyển cấp có một quyết định (bài V7: 1–0..1) |
| V7 | ConflictLog | NhatKyXuLyXungDot | Đổi tên | Tên tiếng Việt; bỏ auditTrailHash (kỹ thuật) |
| V7 | ChangeRequest | DeXuatThayDoi `<<đề xuất>>` | Đổi tên | Q-09 |
| V8 | HoSoTrinhDuyet, PhuongAnBoTri, YeuCauGiaiTrinh | Giữ | | |
| V8 | MaTranPhanQuyenDoA | (bỏ khỏi sơ đồ) | Thành quy tắc nghiệp vụ; kết quả lưu ở HoSoTrinhDuyet.mucRuiRo, capThamQuyen | DoA là quy tắc (P1 I.1.2), không có vòng đời nghiệp vụ. Q-08 |
| V8 | ThongTinChiPhi | DanhGiaChiPhi (V9) | Hợp nhất, V8 tham chiếu | Dữ liệu thuộc V9 (RB-61) |
| V8 | ThongTinDuBao | KetQuaDuBao (V10) | Hợp nhất, V8 tham chiếu | Dữ liệu thuộc V10 (CN-94, 122) |
| V8 | (chưa có) | QuyetDinhPheDuyet | Thêm | P1 I.1.3.8 bước 5: quyết định được lưu vết; UC-07.3, 07.4 |
| V9 | PhanBoNguonLuc | ChiTietBoTri | Hợp nhất | Là dòng của phương án, không phải bản ghi trên lịch |
| V9 | CongViec | NganSach – DuAn | Hợp nhất | Q-05 |
| V9 | NguongPheDuyetNganSach | (bỏ khỏi sơ đồ) | Thành quy tắc (ngưỡng 10%, P1 I.1.2); kết quả ở DanhGiaChiPhi.capPheDuyet | Q-08 |
| V9 | NguoiDung | (bỏ) | Loại | Là actor |
| V9 | Các lớp còn lại | Giữ | | |

## 4. Kết luận cho các cặp khái niệm cần kiểm tra

| Cặp | Kết luận | Căn cứ |
|---|---|---|
| ChiTietBoTri ↔ PhanBoNguonLuc | **Khác nhau, giữ riêng** | Một bên là dòng đề xuất trong phương án; bên kia là bản ghi cứng/mềm trên lịch tập trung. Liên kết khi Locked Baseline |
| PhuongAnBoTri ↔ HoSoTrinhDuyet | **Khác nhau, giữ riêng** | Một phương án có thể trình nhiều lần (CN-101); hồ sơ có mức rủi ro, cấp thẩm quyền riêng |
| UngVien ↔ NguonLuc | **Hợp nhất** (mức trung bình) | Q-04: ứng viên tuyển ngoài có phải là NguonLuc không |
| YeuCauNguonLuc ↔ NhuCauNguonLuc | **Chưa đủ căn cứ** | P1 I.1.2 tách "xác định nhu cầu" và "gửi yêu cầu nguồn lực kèm khung thời gian" (CN-127), nhưng không định nghĩa quan hệ. Q-03 |
| GiaiDoanDuAn ↔ ViTriCanBoTri | **Khác nhau** | Một bên là thời gian của dự án, bên kia là chỗ cần người |
| Kết quả đánh giá năng lực / phù hợp / khả năng tham gia | **Ba khái niệm khác nhau** | V3 lưu NangLucKyNang và HoSoNangLuc; V4 lưu KetQuaDanhGiaPhuHop; V5 lưu KetLuanKhaNangThamGia |
| BoTieuChiNangLuc ↔ BoTieuChiPhuHop | **Khác nhau** | Một bên dùng chung để đánh giá năng lực (QT-01); bên kia lập riêng cho từng nhu cầu (CN-32) |
| KyNang / YeuCauKyNang / NangLucKyNang | **Ba lớp** | Danh mục / yêu cầu của vị trí / năng lực của người |
| ThongTinChiPhi ↔ DanhGiaChiPhi | **Hợp nhất vào V9** | RB-61 |
| ThongTinDuBao ↔ KetQuaDuBao | **Hợp nhất vào V10** | CN-122 |
| Lớp actor, người dùng, cấu hình, kỹ thuật | **Loại khỏi sơ đồ miền** | Đề bài yêu cầu sơ đồ lớp miền nghiệp vụ (Outline II.3) |

## 5. Điểm chưa đủ căn cứ cần trưởng nhóm quyết định

| Mã | Câu hỏi | Đề xuất | Ảnh hưởng |
|---|---|---|---|
| Q-01 | Trạng thái của NhuCauNguonLuc. Bản V2 mới dùng "Chờ xác nhận", "Đã xác nhận"; V2a dùng "Đã xây dựng" | Chốt một bộ trạng thái duy nhất cho V2, V4, V10 (D-07) | II.4 state diagram |
| Q-02 | Một phương án có thể có nhiều hồ sơ trình (V8 vẽ 1:1)? | 1 – 0..* | V8 sửa bội số |
| Q-03 | YeuCauNguonLuc (CN-127) có phải lớp riêng không? | Giữ `<<đề xuất>>` đến khi chốt | V5, V2 |
| Q-04 | Ứng viên tuyển ngoài có là NguonLuc không? | Có, phân biệt bằng `loaiNguon` | V4, V3 |
| Q-05 | Có cần lớp CongViec (V2a, V9) không? | Không. Dùng GiaiDoanDuAn + phamViCongViec | V2a, V9 |
| Q-06 | Lịch nguồn lực: một lịch/người (PCN-02) hay nhiều bản ghi theo kỳ (bài V5)? | Một lịch/người, nhiều PhanBoNguonLuc | V5 |
| Q-07 | Số mức của thang năng lực, và có lưu yêu cầu thay đổi tiêu chí không? | Theo CN-18; không lưu yêu cầu | V3 |
| Q-08 | DoA và ngưỡng 10% có vẽ thành lớp không? | Không; ghi trong quy tắc | V8, V9 |
| Q-09 | DeXuatThayDoi (V7) có giữ không? | Giữ `<<đề xuất>>` | V7, V8 |
