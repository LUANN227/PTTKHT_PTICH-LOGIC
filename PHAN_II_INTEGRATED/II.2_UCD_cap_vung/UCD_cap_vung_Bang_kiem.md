# UCD cấp vùng UC-01 đến UC-09: sơ đồ đề xuất và bảng kiểm bài thành viên

## 1. Sơ đồ đề xuất

Thư mục này có 8 UCD cấp vùng, từ `UCD_UC-01` đến `UCD_UC-08`. UCD UC-09 nằm ở `../II.2_V10/UCD_UC-09`.

Mỗi sơ đồ có ba file:

- `.drawio`: **nguồn chính**, gồm hình gốc draw.io sửa trực tiếp được.
- `.png` và `.svg`: bản xuất.

Thành viên có thể mở file `.drawio`, sửa rồi chèn vào bài, hoặc dùng làm mẫu để đối chiếu với sơ đồ đã vẽ.

Quy tắc chung của các sơ đồ:

- Ranh giới đặt tên theo chức năng cấp vùng, ví dụ "UC-03 Tìm kiếm và đánh giá mức độ phù hợp (V4)".
- Bên trong có đủ UC con theo HD-PCCN §1.
- Actor chính đặt bên trái, actor phụ đặt bên phải.
- Association không có mũi tên.
- `include`/`extend` chỉ dùng ở 4 chỗ theo `QUY_UOC_PHAN_II.md` §3:
  - 01.3 extend 01.2 (chờ D-06);
  - 06.3 extend 06.2;
  - 07.2 extend 07.1;
  - 09.1 include 09.2.
- Không vẽ UC của vùng khác, vì bàn giao dữ liệu giữa các vùng không phải quan hệ UC.

### Căn cứ từng association

| UC | Actor | Căn cứ P1 |
|---|---|---|
| 01.1 | PM | CN-01–09, 11 |
| 01.2 | RM | CN-12–14, 16 |
| 01.3 | PM | CN-10, 15, 17 |
| 02.1 | RM; PMO | CN-18, 19; CN-19 (PMO duyệt tiêu chí tạm) |
| 02.2 | RM; Nguồn lực | CN-20, 22–27; CN-21 |
| 02.3 | RM; PMO | CN-29, 30; CN-28 |
| 03.1, 03.2 | RM | CN-31–33 |
| 03.3 | RM; PMO | CN-34–41; CN-37 (D-P3-01) |
| 03.4 | RM; PMO | CN-43 (D-P3-01) |
| 04.1 | RM; PM | CN-47–52, 55, 58, 59; CN-127 (P-05) |
| 04.2 | RM; PM | CN-53; CN-54 |
| 04.3 | RM; PMO; CEO | CN-56; CN-57 |
| 05.1 | RM | CN-60–68 |
| 05.2 | PM; RM | CN-69; CN-70–73 |
| 06.1 | RM; PM | CN-74, 75, 77; CN-76 |
| 06.2 | RM; PM | CN-79–81; CN-78, 82 |
| 06.3 | RM; PMO; CEO | CN-83; CN-84; CN-85 |
| 07.1 | PMO; CEO | CN-89–91; CN-92–94 |
| 07.2 | PMO; RM | CN-95; CN-96 |
| 07.3, 07.4 | PMO; CEO | CN-97, 98: "cấp có thẩm quyền theo DoA" (PMO Mức 1–3, CEO Mức 4–5) |
| 08.1 | PM; Tài chính | CN-103, 104; CN-105–107 |
| 08.2 | PM; Tài chính | CN-108, 109 |
| 08.3 | PM | CN-110 |
| 08.4 | PM; PMO; CEO | CN-111, 112; CN-129; CN-128 |
| 09.1 | RM; PM | CN-113, 115, 120–122, 124; CN-114, 123 (D-V10-01) |
| 09.2 | RM | CN-116–119, 125, 126 |

### Đối chiếu với II.1

Mỗi actor nối với một UC con trên UCD cấp vùng cũng phải nối với UC cấp vùng tương ứng trong II.1. Bảng dưới kiểm tra điều đó.

| Vùng | Actor trên UCD cấp vùng | Actor nối UC-0x trong II.1 | Kết quả |
|---|---|---|---|
| UC-01 | PM, RM | PM, RM | Khớp |
| UC-02 | RM, Nguồn lực, PMO | RM, Nguồn lực, PMO | Khớp |
| UC-03 | RM, PMO | RM, PMO | Khớp. PMO là bổ sung theo D-P3-01 |
| UC-04 | RM, PM, PMO, CEO | PM, RM, PMO, CEO | Khớp |
| UC-05 | RM, PM | PM, RM | Khớp |
| UC-06 | RM, PM, PMO, CEO | PM, RM, PMO, CEO | Khớp |
| UC-07 | PMO, CEO, RM | RM, PMO, CEO | Khớp |
| UC-08 | PM, Tài chính, PMO, CEO | PM, Tài chính, PMO, CEO | Khớp |
| UC-09 | RM, PM | PM, RM | Khớp |

Đã render và xem lại từng hình. Kết quả kiểm tra hình:

- Không có đường association nào cắt qua UC khác.
- Không có nhãn bị che.
- Chữ không tràn khỏi hình elip.

## 2. Bảng kiểm UCD cấp vùng trong bài thành viên

Kiểm tra trên file bài hiện có. V2b và V8 dùng bản mới trưởng nhóm gửi.

Viết tắt trong bảng:

- Đ = đạt.
- K = không đạt.
- "–" = không có sơ đồ để kiểm tra.

| Vùng / bài | Đã có UCD cấp vùng | Đủ UC con | Mã, tên đúng | Actor, quan hệ đúng | Có trong bài nộp | Khớp II.1 | Việc cần làm (mã trong bảng giao việc) |
|---|---|---|---|---|---|---|---|
| UC-01 / V2a | K, chỉ UCD của 01.1 | K | Đ | K: RM nối 01.1 | Đ | K | V2b vẽ UCD UC-01; V2a bỏ RM (UV-01) |
| UC-01 / V2b | K, có 01.2 và 01.3 | K, thiếu 01.1 | Đ | Đ: extend 01.3 → 01.2 | Đ | Đ | Thêm 01.1 và PM–01.1 (UV-01) |
| UC-02 / V3 | K, chỉ 02.1 | K | Đ | K: thiếu PMO, Nguồn lực | Đ | K | Vẽ đủ 02.1–02.3 (UV-02) |
| UC-03 / V4 | K, chỉ 03.3 | K | Đ | Đ cho 03.3; chưa có PMO | Đ | Đ, sau D-P3-01 | Vẽ đủ 03.1–03.4 (UV-03) |
| UC-04 / V5 | Đ | Đ | K: tiêu đề "PHÂN HỆ V5" | K: RM chỉ nối 04.1 | Đ | Đ | Đổi tiêu đề; nối RM–04.2, 04.3 (UV-04) |
| UC-05 / V6 | K, chỉ 05.1 | K | Đ | K: association vẽ mũi tên | Đ | Đ | Thêm 05.2; bỏ mũi tên (UV-05) |
| UC-06 / V7 | Đ | Đ | Đ | K: `include` 06.1 | Đ | Đ | Bỏ include 06.1; thêm extend 06.3 → 06.2 (UV-06) |
| UC-07 / V8 (hình mới) | K | K, thiếu 07.4 | Đ | K: include UC-08, UC-09; include 07.3–07.1 | Đ (ảnh rời) | K | Bỏ UC ngoài vùng; thêm 07.4; extend 07.2 → 07.1 (UV-07) |
| UC-08 / V9 | – (chỉ có link Drive) | – | – | – | K | – | Chèn hình vào bài; đối chiếu `UCD_UC-08.drawio` (UV-08) |
| UC-09 / V10 | Đ | Đ | Đ | Đ | Đ | Đ | – |

**Nghiệm thu chung:** UCD trong bài trùng về nội dung với sơ đồ đề xuất cùng mã. Cụ thể:

- cùng UC con;
- cùng mã, cùng tên;
- cùng tập actor;
- cùng quan hệ.

Bố cục có thể khác. Nếu khác về nội dung, thành viên phải ghi căn cứ.
