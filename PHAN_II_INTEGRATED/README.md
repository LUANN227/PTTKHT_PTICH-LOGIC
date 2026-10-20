# PHAN_II_INTEGRATED

Thư mục này là sản phẩm Phần II đã tích hợp. Đây là **bản đề xuất** trên nhánh làm việc riêng, chờ trưởng nhóm duyệt; chưa phải bản chính thức.

## Thứ tự đọc

Các phần đi theo thứ tự làm việc: phân rã chức năng → II.1 → UCD cấp vùng → V10 → II.3 → bảng giao việc.

| # | Thư mục / file | Nội dung |
|---|---|---|
| 1 | `I_Phan_ra_chuc_nang/` | Sơ đồ phân rã chức năng 9 vùng / 28 UC (`.drawio`, `.png`, `.svg`). `Bang_doi_chieu_PCCN.md`: đối chiếu từng chức năng với Phần I; điểm cần sửa trong HD-PCCN (P-01..P-12); mâu thuẫn D-P3-01 |
| 2 | `II.1_Use_Case_Tong_Quat/` | Sơ đồ ca sử dụng tổng quát (`.drawio`, `.png`, `.svg`); bảng kiểm |
| 3 | `II.2_UCD_cap_vung/` | UCD cấp vùng UC-01..UC-08 (`.drawio`, `.png`, `.svg`); bảng kiểm UCD vùng trong bài thành viên |
| 4 | `II.2_V10/` | V10: Description UC-09.1, 09.2; AD; UCD UC-09; lớp miền; điểm chưa xác định |
| 5 | `II.3_Domain_Class_Diagram/` | Sơ đồ lớp miền tổng quát, hình tổng quan tên lớp, ba khung nhìn A/B/C; danh mục và ánh xạ |
| 6 | `KE_HOACH_SUA_THANH_VIEN.md` | Bảng giao việc hợp nhất (9 loại việc), rà soát UC trọng tâm, kế hoạch sơ đồ hành vi, câu hỏi cần chốt |
| 7 | `QUY_UOC_PHAN_II.md` | Quy ước nghiệp vụ, UML, trình bày, file nguồn |
| – | `_cong_cu/` | Script sinh `.drawio` và khung nhìn II.3 |

## File nguồn của sơ đồ

| Loại sơ đồ | Nguồn chính | Mở bằng draw.io |
|---|---|---|
| Phân rã chức năng, II.1, UCD cấp vùng | `.drawio`: hình gốc, sửa trực tiếp từng hình | Có |
| AD UC-09.x, lớp V10, II.3 | `.puml` | `.drawio` cùng tên, chứa hình và mã PlantUML |

Không có hình nào chỉ tồn tại dưới dạng ảnh.

## Nguồn đã đọc

- Phần I: `[PTTKHT] I - PHÂN TÍCH YÊU CẦU FINAL.docx`.
- Hướng dẫn:
  - `Outline bài thảo luận.docx`;
  - HD-PCCN (`...THIẾT KẾ LOGIC).md`);
  - HD-MAU (`... (1).md`).
- Bài thành viên:
  - V2a, V3, V4, V5, V6, V7, V9: file trong repo.
  - V2b: bản mới `V2-Phan II 2 1.docx`, trưởng nhóm gửi.
  - V8: file trong repo, cùng 3 sơ đồ mới gửi.
  - V9: AD `4. Activity Diagram.drawio`, trưởng nhóm gửi; đã đọc và render.
- Audit `AUDIT_PHAN_II/`: chỉ dùng làm danh sách kiểm tra.

## Thiếu hoặc chưa kiểm tra được

- **Phần I không có sơ đồ phân rã chức năng.** Sơ đồ ở mục 1 được vẽ lại từ bảng HD-PCCN §1.
- Không có bảng phân công chính thức. HD-PCCN §5 chỉ là "đề xuất ban đầu".
- UCD và sơ đồ lớp của V9 chỉ có trên Drive, chưa kiểm tra được.
- Các file trưởng nhóm gửi chưa được thêm vào repo. Đang chờ trưởng nhóm đồng ý.

## Thay đổi đối với nguồn gốc

Không có. Không file nguồn nào bị sửa, đổi tên hoặc xóa.

## Cách tạo lại hình

```
# UCD, phân rã (.drawio)
python3 _cong_cu/gen_drawio.py .

# Khung nhìn II.3 (.puml)
python3 _cong_cu/tach_view_II3.py II.3_Domain_Class_Diagram

# PNG từ .puml (PlantUML 1.2023.13, layout smetana)
java -jar plantuml.jar -charset UTF-8 -tpng <file>.puml

# Bọc .puml thành .drawio
python3 _cong_cu/puml_to_drawio.py <file>.puml <file>.svg <file>.drawio
```

**Về bản xuất PNG/SVG của file `.drawio`.** Các bản này được xuất bằng bộ chuyển đổi drawio2svg trong Chromium, rồi xem lại từng hình. Khi đưa vào bài chính thức, nên xuất lại trực tiếp từ draw.io bằng File › Export as › PNG, nền trắng, tỷ lệ 200%.

Sau khi tạo lại hình, đối chiếu theo `QUY_UOC_PHAN_II.md` §6.
