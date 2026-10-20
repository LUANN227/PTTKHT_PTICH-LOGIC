# II.1 — Sơ đồ ca sử dụng tổng quát: bảng kiểm

- **File nguồn:** `II1_UC_Tong_Quat.drawio`. Đây là hình gốc draw.io, sửa trực tiếp được. Sinh lại bằng `../_cong_cu/gen_drawio.py`.
- **Bản xuất:** `II1_UC_Tong_Quat.png` và `.svg`.
- **Căn cứ cấp UC:** sơ đồ phân rã chức năng `../I_Phan_ra_chuc_nang/` (cấp 1 của cây).

## Cách tổ chức đã chọn

Sơ đồ có 9 ca sử dụng cấp vùng, từ UC-01 đến UC-09. Mã và tên giữ đúng theo HD-PCCN §1, và mỗi ca sử dụng ứng với một vùng V2–V10 của Phần I.

Lý do chọn cách này:

1. Outline chỉ yêu cầu "sơ đồ ca sử dụng tổng quát" cho II.1. UC chi tiết thuộc II.2 ("sơ đồ ca sử dụng chi tiết").
2. Ánh xạ 1–1 với vùng V của Phần I giữ được khả năng truy vết.
3. Không phải đổi mã hay tiêu đề trong bài nào.

Phương án gom thành 6 chức năng lớn (audit, tài liệu 03) chỉ khác ở cách trình bày, không có lợi thêm về nghiệp vụ, và phải giải thích thêm một lớp ánh xạ. Vì vậy không dùng. 

## Actor

Actor và association lấy theo cột "Tham gia tại" của P1 I.1.2. Có một ngoại lệ: PMO–UC-03 được thêm theo CN-37 và CN-43 (D-P3-01, `../I_Phan_ra_chuc_nang/Bang_doi_chieu_PCCN.md` §5).

| Actor | Tham gia (P1 I.1.2) | Nối với | Ghi chú |
|---|---|---|---|
| PM | V2, V5, V6, V7, V9, V10 | UC-01, 04, 05, 06, 08, 09 | |
| RM | V2–V8, V10 | UC-01 đến 07, 09 | |
| Nguồn lực | V3 | UC-02 | |
| Tài chính | V9 | UC-08 | |
| PMO/Quản lý danh mục | V3, V5, V7, V8, V9 | UC-02, **03**, 04, 06, 07, 08 | UC-03 theo CN-37, 43; chờ D-P3-01 |
| CEO/Managing Director | V5, V7, V8, V9 | UC-04, 06, 07, 08 | |

Không có CCB, "Hệ thống" hay "Người dùng" làm actor. P1 không có các vai trò này.

## Quan hệ giữa các ca sử dụng

Không có `include`, `extend` hay generalization giữa UC-01 đến UC-09. Quan hệ giữa các vùng trong P1 I.1.3.1 đều là bàn giao dữ liệu: nối tiếp, rẽ nhánh, song song, dùng chung, phản hồi. Đó không phải việc một UC gọi hành vi của UC khác.

Vì vậy quan hệ `<<include>> UC-08` và `<<include>> UC-09` trên UCD của V8 là sai, và đã đưa vào bảng giao việc.

## Kiểm tra chéo

| Kiểm tra | Kết quả |
|---|---|
| 9 mã và tên khớp HD-PCCN §1 | ✓ |
| Mỗi vùng V2–V10 có đúng một UC cấp vùng | ✓ |
| Actor khớp P1 I.1.2 | ✓ |
| Association khớp cột "Tham gia tại" | ✓ 25 association theo I.1.2, cộng PMO–UC-03 (D-P3-01): tổng 26 |
| Tên hệ thống | ✓ "Hệ thống quản lý và điều phối nguồn lực dự án - Lạc Việt Consulting" (theo đề tài) |
| UCD cấp vùng của thành viên khớp II.1 | ✗ V8 có UC-08, UC-09 trong UCD vùng; V5 thiếu RM ở 04.2, 04.3 (bảng giao việc UV-04, UV-07) |
| Actor của 9 UCD cấp vùng đề xuất là tập con của actor trong II.1 | ✓ (`../II.2_UCD_cap_vung/UCD_cap_vung_Bang_kiem.md` §1) |
| Hình sau khi render: không nhãn bị che, không đường cắt qua UC | ✓ đã xem lại |

## Chênh lệch giữa HD-PCCN và P1 về actor

II.1 theo P1. Các điểm dưới đây cần sửa trong HD-PCCN, không sửa trong II.1:

- UC-01.2: HD-PCCN ghi PM, P1 ghi RM (CN-12, 13).
- UC-09.x: HD-PCCN ghi PMO, P1 ghi RM (D-V10-02).
- UC-08.1: HD-PCCN ghi Tài chính/RM. P1 V9 không có RM (I.1.2).
