# PTTKHT – Phân tích thiết kế logic (Lạc Việt Consulting)

Hệ thống quản lý và điều phối nguồn lực dự án. Repo chỉ giữ những gì đã chốt: bài gốc, bài đã sửa, quyết định, sơ đồ draw.io và bản tổng hợp cuối. Các bản rà soát, audit, bản tích hợp cũ đã bỏ (vẫn xem được trong lịch sử git).

## Thư mục

| Thư mục | Nội dung |
|---|---|
| `00_DE_BAI_VA_MAU/` | Outline bài thảo luận, hướng dẫn "Hoàn thiện mục II", mẫu FDS Summary và UC Description, hướng dẫn chốt FDS, bản PDF Phần II dùng làm chuẩn trình bày |
| `01_MUC_I/goc/` | Phần I bản FINAL, giữ nguyên |
| `01_MUC_I/da_sua/` | Phần I đã sửa theo các quyết định (QĐ-01, 02, 07, 21, 22; AD V4 có làn PMO) |
| `02_MUC_II_BAI_THANH_VIEN/goc/` | 9 bài Mục II của thành viên (V2a, V2b bản 22/10, V3–V9), giữ nguyên |
| `02_MUC_II_BAI_THANH_VIEN/da_sua/` | 9 bài đã sửa, hậu tố "(đã sửa)" |
| `03_QUYET_DINH_VA_SUA_DOI/` | `QUYET_DINH_VA_THAY_DOI.md` (mọi quyết định đã chốt), `NHAT_KY_SUA_BAI_GOC.md` (từng ô đã sửa: trước, sau, lý do) |
| `04_DRAWIO/` | Nguồn draw.io kèm PNG/SVG: `I/` (AD Phần I), `II.1/`, `II.2_UCD_vung/`, `II.2_AD/` (12 AD UC trọng tâm), `II.3/` (sơ đồ lớp). Sau này thêm `II.4/` |
| `05_TONG_HOP_CUOI/` | `PTTKHTTT_PHAN_I_II3_TONG_HOP.docx` và `.pdf`: Phần I, II.1–II.3, đề mục II.4 |
| `_cong_cu/` | Script sinh toàn bộ kết quả và dữ liệu (`du_lieu/`: catalogue, fds, v10) |

## Chạy lại

Cần Python 3 với `python-docx`, `docxcompose`, `Pillow`. Chạy từ thư mục gốc repo:

```sh
python3 _cong_cu/gen_phan_cap.py      # II.1 và UCD vùng -> 04_DRAWIO/II.1, II.2_UCD_vung
python3 _cong_cu/gen_ad.py            # AD UC trọng tâm V2–V9 -> 04_DRAWIO/II.2_AD (báo "CẢNH BÁO" nếu guard đè hình)
python3 _cong_cu/gen_ad_v10.py        # AD UC-09.1, 09.2
python3 _cong_cu/gen_p1_v4.py         # AD V4 của Phần I -> 04_DRAWIO/I
python3 _cong_cu/gen_ii3_drawio.py    # sơ đồ lớp II.3
sh _cong_cu/render/render_all.sh 04_DRAWIO   # xuất PNG/SVG (cần Node, Playwright Chromium và bundle d2s.js)
python3 _cong_cu/sua_bai_goc.py       # goc/ -> da_sua/ của 01 và 02, ghi lại nhật ký ở 03
python3 _cong_cu/tao_word_tong_hop.py # -> 05_TONG_HOP_CUOI/PTTKHTTT_PHAN_I_II3_TONG_HOP.docx
```

Muốn sửa câu chữ của một quyết định (trạng thái, công thức QĐ-07, đơn vị đơn giá), sửa `_cong_cu/quyet_dinh.py` rồi chạy lại hai lệnh cuối. Muốn sửa một ô trong bài thành viên, sửa job của bài đó trong `_cong_cu/sua_bai_goc.py`.

## Quy ước

- **II.2:** mỗi vùng có UCD vùng, rồi từng UC theo mã. UC trọng tâm có bảng UC Description 10 thành phần, nội dung lấy từ bài thành viên đã sửa, kèm Activity Diagram. UC khác có bảng FDS Summary.
- **Activity Diagram:** vẽ như AD Phần I. Decision và merge là hình thoi nhỏ, rỗng. Điều kiện chỉ ghi ở guard `[..]` cạnh đường ra. Nhánh dừng sớm dùng flow final (⊗); chỉ điểm kết thúc chính dùng ◉.
- **II.4:** chỉ vẽ cho UC trọng tâm, dùng tên lớp của II.3, giữ mạch UC → lớp → hành vi. Sơ đồ trạng thái dùng đúng miền giá trị ở Bảng II.3-2.
- Không tự đặt mã CN/QT, ngưỡng, công thức, actor hay trạng thái khi chưa có nguồn hoặc chưa được trưởng nhóm chốt.
