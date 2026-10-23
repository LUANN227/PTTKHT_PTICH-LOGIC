# Báo cáo rà soát Phần II

Ngày 22/10/2026. Thư mục `PHAN_II_RA_SOAT/` là bản mới. Mọi file đầu vào giữ nguyên:

- gói ChatGPT;
- bài thành viên;
- `PHAN_II_INTEGRATED/`.

Chưa commit, chưa push.

## 1. Sản phẩm

| File | Nội dung |
|---|---|
| `PTTKHTTT_PHAN_II_BAN_RA_SOAT.docx` | Bản Word Phần II, 41 trang, theo Outline. Chi tiết ở mục 2 |
| `II2_YEU_CAU_SUA_THEO_VUNG.md` (.docx) | Bảng sửa II.2 cho từng vùng hoặc thành viên, 4 cột. Chỉ ghi chỗ còn sai hoặc thiếu |
| `II4_RA_SOAT_VA_PHAN_CONG.md` (.docx) | Rà soát 20 sơ đồ II.4 hiện có, và bảng phân công vẽ lại |
| `DANH_SACH_CHO_QUYET_DINH.md` | QĐ-01 đến QĐ-20 cần trưởng nhóm chốt, có bảng đối chiếu mã cũ. File nội bộ, không đưa vào bản Word |
| `drawio/` | Nguồn `.drawio` của mọi hình trong bản Word, kèm PNG và SVG xuất từ chính file đó |
| `_cong_cu/` | Các script sinh hình và bản Word, cùng dữ liệu đầu vào (`du_lieu/`) |

## 2. Bản Word

### II.1

- UCD tổng quát (Hình II.1-1).
- Sơ đồ phân cấp hai tầng (Hình II.1-2). Đây là hình mới vẽ bằng draw.io, thay ảnh phân cấp của ChatGPT, vốn không có nguồn.
- Bảng 28 chức năng con có thêm hai cột: tác nhân và CN của Phần I.

### II.2

Mỗi vùng có:

- UCD vùng;
- FDS tóm tắt cho 16 UC không trọng tâm.

12 UC trọng tâm:

- **V2–V9, trừ V4 (9 UC):** để khung `[Cần bổ sung — tên thành viên]`. Mã, tên, tác nhân, phạm vi và CN đã điền sẵn. Thành viên chèn bản đã sửa theo file II.2.
- **V4, UC-03.3:** giữ đặc tả của bài V4. Ba chỗ còn phải sửa được đánh dấu đỏ:
  - nhánh CN-46;
  - căn cứ mốc 6 tháng;
  - AD chưa có nguồn draw.io.
- **V10:** đặc tả đầy đủ và hai AD draw.io.

### II.3

- Hình tổng quan các gói, và 5 hình cụm lớp với 48 lớp và 69 quan hệ.
- Bảng danh mục lớp.
- Bội số chưa đủ căn cứ để trống, chờ QĐ-05.

### II.4

Đi theo Outline: trạng thái, giao tiếp, tuần tự. Bản Word chỉ liệt kê các sơ đồ quyết định giữ hoặc sửa: 4 sơ đồ trạng thái, 3 sơ đồ giao tiếp, 10 sơ đồ tuần tự. Mỗi sơ đồ để một khung chờ ghi người vẽ.

Không chèn hình ChatGPT nào vào II.4, vì không hình nào có file nguồn.

### Không đưa vào bản Word

- bảng audit;
- trao đổi nội bộ;
- lớp YeuCauNguonLuc (chờ QĐ-11);
- công thức tỷ lệ vượt ngân sách (chờ QĐ-07);
- các mã "D07" và "D08–D09" không tra được trong Phần I.

## 3. Lỗi đã xác nhận trong gói ChatGPT

1. **FDS 08.2 ghi công thức tỷ lệ vượt ngân sách như quy tắc đã chốt, dẫn mã "D07".** Phần I không có công thức này. Chính `decisions.json` của ChatGPT (Q-07) cũng nói công thức chưa có căn cứ.
2. **FDS 09.1 dẫn mã "D08–D09".** Hai mã này không có trong Phần I hay trong danh sách quyết định.
3. **Bảng sửa V5 yêu cầu đổi thao tác thành `ghiNhanXacNhanPMO`.** Bài V5 đã dùng `ghiNhanXacNhanPM()`, đúng với CN, nên yêu cầu này sai.
4. **Bảng sửa V7 nói bài V7 có "hash".** Bài V7 không có từ này.
5. **README của gói nói có thư mục nguồn draw.io.** Gói zip chỉ có 2 file draw.io của thành viên (V8, V9), không có nguồn của:
   - hình phân cấp;
   - 19 hình II.4;
   - hình II.3.
6. **Sơ đồ II.4:**
   - Tác nhân vẽ bằng hộp.
   - Sơ đồ tuần tự không có thanh kích hoạt, và không có khung `alt` hay `loop` dù có điều kiện.
   - Sơ đồ trạng thái thiếu trạng thái kết thúc, và có nhãn bị cắt.
   - KetLuanKhaNangThamGia không phải vòng đời đối tượng.

Chi tiết ở `II4_RA_SOAT_VA_PHAN_CONG.md` mục 1–2.

## 4. Đính chính bản tích hợp ngày 20/10

Bảng kiểm UCD vùng ghi V4 thiếu PMO ở 03.3. Thực tế UCD gốc của V4 đã có PMO. Đã ghi đính chính trong bảng V4 của file II.2.

## 5. Tình trạng file nguồn

| Nhóm | Tình trạng |
|---|---|
| UCD tổng quát, phân cấp, 9 UCD vùng, 6 hình II.3, 2 AD V10 | **Có nguồn**, nằm trong `drawio/`. PNG trong Word xuất từ chính file `.drawio` và đã xem lại sau khi render |
| AD của 10 UC trọng tâm V2–V9 | Chưa có trong Word. Thành viên nộp `.drawio`. Riêng AD UC-03.3 của V4 chỉ có ảnh trong docx, không có nguồn |
| 17 sơ đồ II.4 đã chọn | Chưa có. Thành viên vẽ theo bảng phân công |
| Ảnh phân cấp, 19 hình II.4, ảnh II.3 của ChatGPT | **Không có nguồn.** Không dùng |
| `V8_nguon_nhung_3_trang.drawio`, `V9_AD_hien_co.drawio` (trong gói ChatGPT) | Có nguồn. Giữ nguyên, không sửa. Dùng để đối chiếu ở bảng V8, V9 |
| Bài Word của thành viên, Phần I FINAL | Giữ nguyên |

## 6. Việc trưởng nhóm cần làm trước

Bốn quyết định chặn nhiều việc nhất:

| Mã | Câu hỏi | Ảnh hưởng |
|---|---|---|
| QĐ-01 | PMO có tham gia V4 không | Hình II.1, UCD UC-03 và sơ đồ tuần tự miễn trừ |
| QĐ-05 | 7 bội số còn để trống | II.3 |
| QĐ-07 | Công thức tỷ lệ vượt ngân sách | Bài V9 |
| QĐ-10 | Phạm vi UC trọng tâm của V9 | Bài V9 |

QĐ-02 (tên trạng thái của nhu cầu) chặn sơ đồ trạng thái và sơ đồ tuần tự của V2b.

Đề xuất cho từng mục ở `DANH_SACH_CHO_QUYET_DINH.md`.
