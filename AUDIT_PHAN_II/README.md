# Bộ báo cáo audit Phần II

Thư mục này chứa kết quả rà soát Phần II (Thiết kế logic) của nhóm. Đây là tài liệu phân tích để trưởng nhóm quyết định, **không phải phiên bản chính thức** của bài làm. Không có tài liệu nguồn nào trong repository bị sửa, đổi tên, di chuyển hoặc xóa.

## Danh mục

| Số | Tài liệu | Dùng để |
|----|----------|---------|
| 01 | [Manifest và phạm vi nguồn](01_Manifest_va_pham_vi_nguon.md) | Biết đã đọc những gì, file nào thiếu, file nào chưa rõ trạng thái |
| 02 | [Báo cáo audit chiến lược](02_Bao_cao_audit_chien_luoc.md) | Đánh giá Phần I, phạm vi, cấu trúc phân hệ và chất lượng tổng thể Phần II |
| 03 | [So sánh phương án tổ chức hệ thống](03_So_sanh_phuong_an_to_chuc.md) | Chọn giữa giữ 9 phân hệ, gom nhóm trình bày, đổi ranh giới, đổi danh mục UC |
| 04 | [Danh mục UC và ma trận quan hệ](04_Danh_muc_UC_va_ma_tran_quan_he.md) | Tra cứu 28 UC: mục tiêu, actor, người làm, tình trạng, quan hệ, vấn đề |
| 05 | [Ma trận truy vết Phần I → Phần II](05_Ma_tran_truy_vet.md) | Kiểm tra CN/QT nào đã được đặc tả, CN nào chưa có chủ |
| 06 | [Audit theo thành viên](06_Audit_theo_thanh_vien.md) | Nhận xét từng bài: giữ gì, sửa gì, căn cứ, mức độ |
| 07 | [Báo cáo UC trọng tâm](07_Bao_cao_UC_trong_tam.md) | UC nền tảng, mức ảnh hưởng, điểm cần chốt |
| 08 | [Kế hoạch chỉnh sửa](08_Ke_hoach_chinh_sua.md) | Bảng việc giao trực tiếp cho từng thành viên |
| 09 | [Kế hoạch hoàn thiện V10](09_Ke_hoach_V10.md) | Hai UC V10, sơ đồ II.1 và II.3 |
| 10 | [Decision Log đề xuất](10_Decision_Log.md) | Các câu hỏi trưởng nhóm cần quyết định (tất cả ở trạng thái chờ quyết định) |
| 11 | [Executive Summary](11_Executive_Summary.md) | Đọc đầu tiên: trả lời 10 câu hỏi chính |

**Gợi ý thứ tự đọc:** 11 → 10 → 03 → 08, các tài liệu còn lại dùng để tra căn cứ.

## Quy ước dùng trong báo cáo

**Loại thông tin**

- **[Nguồn]**: nội dung được nêu trực tiếp trong tài liệu, có dẫn vị trí.
- **[Đối chiếu]**: kết luận rút ra khi so nhiều nguồn với nhau.
- **[Giả định]**: điều chưa xác minh được, cần trưởng nhóm hoặc thành viên xác nhận.
- **[Đề xuất]**: ý kiến của người phân tích, chưa được nhóm thông qua.

**Mức thay đổi**

- **A**: Giữ nguyên.
- **B**: Sửa diễn đạt, thuật ngữ, ký pháp hoặc mã tham chiếu; không đổi nghiệp vụ.
- **C**: Điều chỉnh một phần logic hoặc luồng xử lý.
- **D**: Thay đổi phạm vi UC, quan hệ giữa UC hoặc ranh giới phân hệ.
- **E**: Thiết kế lại UC hoặc cấu trúc nghiệp vụ.

**Ưu tiên công việc**: P1 (chặn việc khác, làm trước), P2 (cần trước khi vẽ II.3/II.4), P3 (trình bày, làm sau cùng).

**Cách gọi tên file nguồn** (viết tắt dùng trong toàn bộ báo cáo)

| Viết tắt | File |
|----------|------|
| P1 | `[PTTKHT] I - PHÂN TÍCH YÊU CẦU FINAL.docx` |
| HD-PCCN | `[PTTKHT] HOÀN THIỆN MỤC II - PHÂN TÍCH (THIẾT KẾ LOGIC).md` |
| HD-MAU | `[PTTKHT] HOÀN THIỆN MỤC II - PHÂN TÍCH (THIẾT KẾ LOGIC) (1).md` |
| OUTLINE | `Outline bài thảo luận.docx` |
| B-V2a | `V2-Phần II .docx` (Thùy Linh, UC-01.1) |
| B-V2b | `V2-Phần II (2).docx` (Tuấn Long, UC-01.2 và UC-01.3) |
| B-V3 | `V3- Phần 2.docx` (Lê Hoài Linh, UC-02.1) |
| B-V4 | `V4 - Phần II.docx` (Nguyễn Hoàng Linh, UC-03.3) |
| B-V5 | `NV05 I2 - I3.docx` (Nguyễn Hoàng Khánh Linh, UC-04.1) |
| B-V6 | `V6 - Phần II.docx` (Nguyễn Thi Thùy Linh, UC-05.1) |
| B-V7 | `MNV7_II_Thiết kế Logic.docx` (Lưu Thùy Linh, UC-06.2) |
| B-V8 | `MNV8 - Ngọc Linh.docx` (Ngọc Linh, UC-07.1) |
| B-V9 | `V9 - Phần II.docx` (Ngô Nhật Long, UC-08.1) |

Số mục trong bài thành viên (ví dụ "§3.3") theo đúng mẫu HD-MAU mà các bài đang dùng.
