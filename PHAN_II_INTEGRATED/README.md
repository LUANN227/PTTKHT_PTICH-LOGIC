# PHAN_II_INTEGRATED

Thư mục này là sản phẩm Phần II đã tích hợp, gồm II.1, II.2 của V10, II.3, bảng giao việc và quy ước. Đây là bản đề xuất trên nhánh làm việc riêng, chờ trưởng nhóm duyệt; chưa phải bản chính thức.

## Nội dung

| Thư mục / file | Nội dung |
|---|---|
| `II.1_Use_Case_Tong_Quat/` | Sơ đồ ca sử dụng tổng quát: `.puml` (nguồn), `.png`, `.svg`; bảng kiểm |
| `II.2_V10/` | V10: Description UC-09.1, 09.2; AD; UCD cấp vùng; lớp miền; giao tiếp vùng; điểm chưa xác định |
| `II.3_Domain_Class_Diagram/` | Sơ đồ lớp miền tổng quát (`.puml`, `.png`, `.svg`); danh mục và ánh xạ |
| `KE_HOACH_SUA_THANH_VIEN.md` | Bảng giao việc V2–V10 |
| `QUY_UOC_PHAN_II.md` | Quy ước |

## Nguồn đã đọc

- Phần I: `[PTTKHT] I - PHÂN TÍCH YÊU CẦU FINAL.docx`.
- Hướng dẫn: `Outline bài thảo luận.docx`, HD-PCCN (`...THIẾT KẾ LOGIC).md`), HD-MAU (`... (1).md`).
- Bài thành viên:
  - V2a, V3, V4, V5, V6, V7, V9: file trong repo.
  - V2b: bản mới `V2-Phan II 2 1.docx`, trưởng nhóm gửi.
  - V8: file trong repo, cùng 3 sơ đồ mới gửi.
- Audit `AUDIT_PHAN_II/`: chỉ dùng làm danh sách kiểm tra.

## Thiếu hoặc chưa kiểm tra được

- Không có bảng phân công chính thức. HD-PCCN §5 chỉ là "đề xuất ban đầu".
- Hình UCD, AD và lớp của V9 chỉ có trên Drive.
- Hai file mới (bản V2b mới, 3 sơ đồ V8) chưa được thêm vào repo. Đang chờ trưởng nhóm đồng ý.

## Thay đổi đối với nguồn gốc

Không có. Không file nguồn nào bị sửa, đổi tên hoặc xóa.

## Cách kiểm tra

Chạy lệnh sau để tạo lại hình:

```
java -jar plantuml.jar -charset UTF-8 -tpng <file>.puml
```

Phiên bản PlantUML đã dùng: 1.2023.13, layout smetana.

Sau đó đối chiếu theo `QUY_UOC_PHAN_II.md` §6.
