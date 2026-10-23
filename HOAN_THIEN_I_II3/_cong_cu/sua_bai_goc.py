"""Sửa trực tiếp bài Word gốc của từng thành viên (và Phần I) theo các lỗi đã xác nhận và các
quyết định đã chốt. Bản gốc giữ nguyên; bản sửa ghi vào bai_goc_da_sua/ với hậu tố "(đã sửa)".
Mọi thay đổi được ghi nhật ký vào NHAT_KY_SUA_BAI_GOC.md.

    python3 sua_bai_goc.py <thư mục bài gốc> <thư mục HOAN_THIEN_I_II3> [mã bài ...]

Thư mục bài gốc chứa đúng tên file như trên nhánh main (bản V2b lấy bản Nguyễn Tuấn Long tải lên
ngày 22/10, đặt tên "V2-Phần II (2) - ban 22-10.docx").
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx_sua import Sua, log_md  # noqa: E402

JOBS = {}


def job(code, src):
    def wrap(fn):
        JOBS[code] = (src, fn)
        return fn
    return wrap


def img(root, *parts):
    return os.path.join(root, "drawio", *parts)


# ====================================================================== V2a
@job("V2a", "V2-Phần II .docx")
def v2a(s, root):
    why_actor = "Lỗi: CN-01–CN-11 đều do PM thực hiện; hệ thống không phải actor"
    s.cell(1, 3, 1, "Quản lý dự án (PM)", why_actor)
    s.cell(1, 4, 1, "Không có", why_actor)
    s.image(12, img(root, "II.2_UCD_vung", "UCD_UC-01.png"), 14,
            "Dùng UCD vùng UC-01 thống nhất (01.1–01.3), nguồn draw.io")
    # 3.1 Thông tin chung
    s.cell(3, 3, 1, "PM xác định và hoàn thiện nhu cầu nguồn lực của dự án (phạm vi công việc, loại "
                    "nguồn lực/kỹ năng, quy mô FTE theo giai đoạn, thời gian và mức tham gia %FTE), rồi "
                    "chuyển RM xem xét tại UC-01.2.", why_actor + "; thêm thời gian, %FTE (CN-07, CN-08)")
    s.cell(3, 4, 1, "Quản lý dự án (PM)", why_actor)
    s.cell(3, 5, 1, "Không có", why_actor)
    s.cell(3, 6, 1, "Dự án phát sinh công việc mới, hoặc thay đổi phạm vi, khối lượng, tiến độ làm nhu cầu "
                    "nguồn lực phải cập nhật; PM khởi tạo nhu cầu.", "Theo P1 I.1.3.2 “Bắt đầu khi”")
    s.cell(3, 7, 1, "Dự án, kế hoạch giai đoạn và công việc cần nguồn lực đã được xác lập.",
           "Bỏ điều kiện đăng nhập (xử lý kỹ thuật, không phải nghiệp vụ)")
    s.cell(3, 8, 1, "Nhu cầu nguồn lực đủ thông tin được chuyển RM xem xét, ở trạng thái “Chờ xác nhận”; "
                    "đây là tiền điều kiện của UC-01.2. Nếu PM chỉ lưu (A2), nhu cầu ở trạng thái “Đang xây dựng”.",
           "Thêm bước chuyển RM (CN-11); tên trạng thái theo QĐ-02")
    # 3.2 Luồng chính
    rows = [
        ("1", "PM", "Chọn dự án; xem bối cảnh dự án, danh mục công việc và kế hoạch các giai đoạn (CN-01)."),
        ("2", "System", "Hiển thị thông tin dự án, danh mục công việc và các mốc thời gian liên quan."),
        ("3", "PM", "Xác lập phạm vi công việc: chọn các công việc cần nguồn lực (CN-02)."),
        ("4", "System", "Kiểm tra thông tin dự án và phạm vi đã đủ để hiểu công việc, giai đoạn và thời gian "
                        "thực hiện."),
        ("5", "PM", "Xác định loại nguồn lực cần thiết cho từng công việc và yêu cầu chuyên môn, kỹ năng, "
                    "chứng chỉ (một công việc có thể cần nhiều loại nguồn lực) (CN-04, CN-05)."),
        ("6", "PM", "Xác định quy mô nhu cầu của từng loại nguồn lực theo FTE, theo từng giai đoạn (CN-06)."),
        ("7", "PM", "Xác định thời điểm bắt đầu, kết thúc hoặc giai đoạn cần nguồn lực và mức tham gia %FTE "
                    "của từng vị trí (CN-07, CN-08)."),
        ("8", "PM", "Rà soát toàn bộ nhu cầu theo tình trạng hiện tại của dự án và lưu nhu cầu (CN-09)."),
    ]
    for r, v in enumerate(rows, 1):
        s.row(4, r, v, "Lỗi: actor chỉ là PM; bỏ thao tác giao diện; thêm giai đoạn, %FTE (CN-07, CN-08)")
    s.add_row(4, 8, ["11", "System", "Ghi nhận nhu cầu ở trạng thái “Chờ xác nhận” để RM xem xét tại UC-01.2."],
              "Thêm bước gửi RM (CN-11)")
    s.add_row(4, 8, ["10", "PM", "Chuyển nhu cầu đã hoàn thiện cho RM xem xét (CN-11)."], "Thêm bước gửi RM (CN-11)")
    s.add_row(4, 8, ["9", "System", "Lưu nhu cầu ở trạng thái “Đang xây dựng”."],
              "Phân biệt lưu với đã gửi RM; tên trạng thái theo QĐ-02")
    # 3.3 Luồng thay thế / ngoại lệ
    s.row(5, 1, ["A1", "Bước 4",
                 "Thông tin dự án chưa đủ để hiểu công việc, giai đoạn, thời gian; hoặc phạm vi công việc, mốc "
                 "thời gian bị thiếu.",
                 "Hệ thống chỉ rõ thông tin còn thiếu → PM yêu cầu bổ sung thông tin dự án hoặc điều chỉnh phạm "
                 "vi; nhu cầu chưa được cố định cho đến khi có bổ sung (CN-03) → quay lại bước 3."],
          "Mở rộng A1 cho trường hợp thông tin dự án chưa đủ (CN-03)")
    s.row(5, 2, ["A2", "Bước 8",
                 "PM chưa hoàn thiện nhu cầu, chỉ lưu để làm tiếp.",
                 "Hệ thống lưu nhu cầu ở trạng thái “Đang xây dựng” (bước 9); UC kết thúc, chưa chuyển RM. Khi "
                 "hoàn thiện, PM mở lại nhu cầu và thực hiện từ bước 8."],
          "Lỗi: P1 không có giới hạn tổng nhu cầu ≤ 1 FTE (CN-06, CN-08, PCN-09); thay A2 cũ bằng nhánh lưu chưa gửi")
    s.row(5, 3, ["E1", "Bước 7",
                 "Mức tham gia nằm ngoài 0–100% FTE, hoặc thời điểm kết thúc trước thời điểm bắt đầu.",
                 "Hệ thống chỉ rõ thông tin không hợp lệ → PM sửa → tiếp tục bước 7."],
          "Bỏ lỗi kết nối CSDL (xử lý kỹ thuật); thay bằng kiểm tra nghiệp vụ theo thuật ngữ FTE ở P1 I.1.2")
    # 3.4 Quy tắc
    s.row(6, 1, ["CN-01, CN-02", "PM tra cứu bối cảnh dự án, danh mục công việc, kế hoạch giai đoạn và lưu phạm "
                 "vi công việc.", "Bước 1–3"], "Đổi mã theo P1")
    s.row(6, 2, ["CN-03", "PM yêu cầu bổ sung khi thông tin dự án chưa đủ; nhu cầu chưa được cố định cho đến khi "
                 "có bổ sung.", "Bước 4, A1"], "Lỗi: mã CN-V2-01 không có trong P1")
    s.row(6, 3, ["CN-04, CN-05; QT-01, QT-02", "Nhu cầu gắn với công việc; mỗi công việc có một hoặc nhiều loại "
                 "nguồn lực, kèm yêu cầu chuyên môn, kỹ năng.", "Bước 5"],
          "Lỗi: RB-V2-03 (FTE ≤ quỹ thời gian chuẩn) không có trong P1")
    s.add_row(6, 3, ["CN-09, CN-11; QT-04, QT-05", "PM rà soát nhu cầu theo tình trạng dự án và chuyển nhu cầu "
                     "đã hoàn thiện cho RM; nhu cầu phải được RM xác nhận trước khi sang V3/V4.", "Bước 8–11, A2"],
              "Thêm căn cứ bước gửi RM")
    s.add_row(6, 3, ["CN-06, CN-07, CN-08; QT-02, QT-03", "Quy mô theo FTE từng giai đoạn; thời gian hoặc giai "
                     "đoạn; mức tham gia %FTE (0–100%) khi công việc không cần toàn thời gian.", "Bước 6, 7, E1"],
              "Thêm căn cứ giai đoạn và %FTE")
    # 4.1 Thành phần AD (viết lại theo AD mới)
    s.par(29, "Actor/Swimlane: 2 swimlane gồm PM (Quản lý dự án) và Hệ thống.", "Bỏ RM khỏi làn")
    acts = ["Chọn dự án; xem bối cảnh, công việc, kế hoạch giai đoạn (PM)",
            "Hiển thị thông tin dự án, công việc và các mốc thời gian (Hệ thống)",
            "Xác lập phạm vi công việc cần nguồn lực (PM)",
            "Kiểm tra thông tin dự án và phạm vi (Hệ thống)",
            "Xác định loại nguồn lực, yêu cầu chuyên môn, kỹ năng cho từng công việc (PM)",
            "Xác định quy mô FTE theo từng giai đoạn (PM)",
            "Xác định thời gian hoặc giai đoạn và mức tham gia %FTE của từng vị trí (PM)",
            "Rà soát toàn bộ nhu cầu và lưu (PM); Lưu nhu cầu, trạng thái “Đang xây dựng” (Hệ thống)",
            "Chuyển nhu cầu đã hoàn thiện cho RM xem xét (PM); Ghi nhận trạng thái “Chờ xác nhận” (Hệ thống)"]
    for i, a in zip(range(31, 40), acts):
        s.par(i, a, "AD vẽ lại theo luồng chính đã sửa; bỏ đăng nhập, nhấn nút, ghi log")
    s.del_par(40, "Gộp vào action ở trên; bỏ ghi log, thông báo kỹ thuật")
    s.par(42, "Decision “Đủ để hiểu công việc, giai đoạn, thời gian?”: [Chưa đủ] → A1, PM yêu cầu bổ sung hoặc "
              "điều chỉnh phạm vi, quay về merge trước bước 3; [Đủ] → bước 5.", "Theo A1 đã sửa")
    s.par(43, "Decision “Thời gian và %FTE hợp lệ?”: [Không hợp lệ] → E1, quay về merge trước bước 7; [Hợp lệ] → "
              "bước 8. Decision “Nhu cầu đã hoàn thiện, chuyển RM?”: [Chưa] → A2, kết thúc; [Đã hoàn thiện] → "
              "bước 10.", "Lỗi: bỏ decision FTE ≤ 1.0 (không có trong P1)")
    s.par(44, "Điểm kết thúc: nút tròn viền kép; một điểm sau khi lưu chưa gửi (A2), một điểm sau khi chuyển RM.")
    s.image(47, img(root, "II.2_AD", "AD_UC-01.1.png"), 15,
            "AD vẽ lại bằng draw.io theo D đã sửa (AD_UC-01.1.drawio)")
    # II.2+ Lớp
    why_cls = "Thống nhất tên lớp và vị trí thuộc tính với II.3 (Hình II.3-2)"
    s.row(8, 3, ["Công việc (Task/WorkItem)", "Không",
                 "Phạm vi công việc được lưu là thuộc tính phamViCongViec của nhu cầu (CN-02); hệ thống không quản "
                 "lý công việc như một đối tượng riêng."], why_cls)
    s.row(8, 5, ["Loại nguồn lực / Kỹ năng (ResourceType / Skill)", "Có",
                 "Tách thành vị trí cần bố trí (ViTriCanBoTri: vai trò, số lượng, %FTE) và yêu cầu kỹ năng "
                 "(YeuCauKyNang) tham chiếu danh mục KyNang dùng chung với V3."], why_cls)
    s.row(9, 2, [None, "NhuCauNguonLuc", None], why_cls)
    s.row(9, 3, [None, "ViTriCanBoTri, YeuCauKyNang", None], why_cls)
    s.row(9, 4, [None, "ViTriCanBoTri", "Ghi quy mô (số lượng) và mức tham gia %FTE của vị trí theo giai đoạn."],
          why_cls)
    s.row(10, 2, ["ViTriCanBoTri", "Vị trí cần bố trí trong nhu cầu: vai trò, số lượng, %FTE, giai đoạn.",
                  "UC-01.1 (bước 5–7)"], why_cls)
    s.row(10, 4, ["YeuCauKyNang", "Kỹ năng và cấp độ mà vị trí đòi hỏi; tham chiếu danh mục KyNang (V3).",
                  "UC-01.1 (bước 5)"], why_cls)
    s.add_row(10, 1, ["GiaiDoanDuAn", "Giai đoạn của dự án mà quy mô và thời gian nhu cầu gắn vào.",
                      "CN-06, CN-07"], why_cls)
    s.row(11, 1, ["DuAn", "maDuAn, tenDuAn, ngayBatDau, ngayKetThuc, hangUuTien",
                  "Định danh, mốc thời gian tổng thể và hạng ưu tiên của dự án."], why_cls)
    s.row(11, 2, ["ViTriCanBoTri", "maViTri, vaiTro, soLuong, tyLeFTE",
                  "Vai trò, số lượng và mức tham gia %FTE của vị trí."], why_cls)
    s.row(11, 3, ["NhuCauNguonLuc", "maNhuCau, phamViCongViec, thoiGianBatDau, thoiGianKetThuc, trangThai",
                  "Phạm vi công việc, thời gian và trạng thái của nhu cầu; số lượng, FTE thuộc từng vị trí."],
          why_cls + "; soLuongNhanSu, chiSoFTE chuyển sang ViTriCanBoTri")
    s.row(11, 4, ["YeuCauKyNang", "capDoYeuCau, batBuoc", "Cấp độ yêu cầu và tính bắt buộc của kỹ năng."],
          why_cls)
    s.add_row(11, 1, ["GiaiDoanDuAn", "maGiaiDoan, tenGiaiDoan, ngayBatDau, ngayKetThuc",
                      "Giai đoạn của dự án."], why_cls)
    s.row(12, 2, ["ViTriCanBoTri", "ganGiaiDoan(giaiDoan), capNhatQuyMo(soLuong, tyLeFTE)",
                  "Gắn vị trí với giai đoạn và cập nhật quy mô, mức tham gia."], why_cls)
    s.row(12, 3, ["NhuCauNguonLuc", "taoMoiNhuCau(), chinhSuaNhuCau(), chuyenRM(), capNhatTrangThai(trangThaiMoi)",
                  "Khởi tạo, chỉnh sửa nhu cầu, chuyển RM xem xét và cập nhật trạng thái."], why_cls)
    s.row(12, 4, ["YeuCauKyNang", "datYeuCau(kyNang, capDo, batBuoc)",
                  "Ghi kỹ năng, cấp độ và tính bắt buộc mà vị trí đòi hỏi."], why_cls)
    s.row(13, 1, ["DuAn", "Association", "NhuCauNguonLuc", "Một dự án có thể có nhiều nhu cầu nguồn lực."], why_cls)
    s.row(13, 2, ["NhuCauNguonLuc", "Composition (*--)", "ViTriCanBoTri",
                  "Một nhu cầu gồm một hoặc nhiều vị trí cần bố trí."], why_cls)
    s.row(13, 3, ["ViTriCanBoTri", "Composition (*--)", "YeuCauKyNang",
                  "Mỗi vị trí đòi hỏi các kỹ năng; YeuCauKyNang tham chiếu KyNang (V3)."], why_cls)
    s.add_row(13, 3, ["ViTriCanBoTri", "Association", "GiaiDoanDuAn",
                      "Vị trí gắn với giai đoạn khi nhu cầu thay đổi theo giai đoạn (QT-29)."], why_cls)
    s.row(14, 1, ["DuAn ── NhuCauNguonLuc", "1 : 0..*", "Một dự án chưa có hoặc có nhiều nhu cầu."], why_cls)
    s.row(14, 2, ["NhuCauNguonLuc ── ViTriCanBoTri", "1 : 1..*", "Nhu cầu nêu rõ vai trò, số lượng (P1 I.1.3.2)."],
          why_cls)
    s.row(14, 3, ["ViTriCanBoTri ── YeuCauKyNang", "1 : 0..*", "Một vị trí có thể đòi hỏi nhiều kỹ năng."],
          why_cls)
    s.add_row(14, 3, ["ViTriCanBoTri ── GiaiDoanDuAn", "0..* : 0..1",
                      "Vị trí có thể gắn với một giai đoạn hoặc dùng cho cả dự án."], why_cls)
    s.image(60, img(root, "II.3", "II3-2_Nhu_cau_va_nang_luc.png"), 15,
            "Sơ đồ lớp theo mô hình thống nhất (Hình II.3-2, nguồn draw.io)")


# ====================================================================== V2b
@job("V2b", "V2-Phần II (2) - ban 22-10.docx")
def v2b(s, root):
    s.image(7, img(root, "II.2_UCD_vung", "UCD_UC-01.png"), 14,
            "Dùng UCD vùng UC-01 thống nhất (đủ 01.1–01.3), nguồn draw.io")
    no_pm = "PM không thao tác trong UC-01.2; việc PM bổ sung, điều chỉnh thuộc UC-01.3 (CN-14, CN-15)"
    s.cell(1, 4, 1, "Không có (PM nhận nhu cầu được chuyển lại và xử lý ở UC-01.3)", no_pm)
    s.cell(3, 1, 2, "UC-01.2", "Lỗi: UC tự mở rộng chính nó; hình UCD vẽ 01.3 extend 01.2")
    # 3.1 UC-01.2
    s.cell(4, 5, 1, "Không có", no_pm)
    s.cell(4, 6, 1, "PM chuyển nhu cầu đã hoàn thiện cho RM (kết thúc UC-01.1, CN-11); nhu cầu ở trạng thái "
                    "“Chờ xác nhận”.", "Ghi rõ sự kiện bắt đầu, nối với UC-01.1 (QĐ-02)")
    s.cell(4, 8, 1, "Nhu cầu được xác nhận; trạng thái “Đã xác nhận” là điều kiện để bàn giao sang V3 và V4 "
                    "(QT-05, QT-12).\nHoặc: nhu cầu được chuyển lại PM, trạng thái “Cần tiếp tục hoàn thiện”; "
                    "nhu cầu chưa được xác nhận và không được bàn giao sang V3, V4.",
           "Đặt tên trạng thái theo QĐ-02 (CN-15: “cần tiếp tục hoàn thiện”)")
    s.del_row(5, 8, "Bỏ dòng “Kết thúc” không có tác nhân; điểm kết thúc thể hiện trên AD")
    s.row(6, 1, ["A1", "Bước 3", "Nhu cầu chưa đủ điều kiện",
                 "RM ghi nhận nội dung cần bổ sung, điều chỉnh.\nHệ thống chuyển lại nhu cầu cho PM, trạng "
                 "thái “Cần tiếp tục hoàn thiện”.\nUse case kết thúc; PM xử lý tiếp ở UC-01.3."],
          "Lỗi: các bước PM điều chỉnh thuộc UC-01.3 (extend). Đây là luồng nghiệp vụ hợp lệ theo CN-14 nên "
          "đổi E1 thành A1")
    # 3.2 UC-01.3
    for i, h in [(22, "3.2.2. Luồng chính"), (23, "3.2.3. Luồng thay thế / ngoại lệ"),
                 (27, "3.2.4. Business Rules / yêu cầu liên quan")]:
        s.par(i, h, "Lỗi đánh số: trùng số mục 3.1.x của UC-01.2")
    s.cell(8, 6, 1, "(1) RM chuyển lại nhu cầu chưa đủ điều kiện (từ UC-01.2, quan hệ extend; CN-14); hoặc "
                    "(2) PM nhận phản hồi từ V4 về việc không có ứng viên đáp ứng, hoặc thông tin cung ứng, "
                    "khoảng thiếu/dư từ V10 để xem xét lại nhu cầu (CN-17).",
           "QĐ-12: giữ đủ hai cách bắt đầu")
    s.cell(8, 8, 1, "Nhu cầu được điều chỉnh và gửi lại RM, trạng thái “Chờ xác nhận”.\nHoặc (A1): nhu cầu "
                    "giữ nguyên trạng thái hiện tại.", "Bổ sung hậu điều kiện của A1; gửi lại RM theo CN-11")
    s.row(9, 1, [None, None, "Tra cứu nhu cầu hiện tại và phản hồi đã được ghi nhận: yêu cầu bổ sung của RM, "
                 "phản hồi V4 hoặc thông tin V10 (CN-15, CN-17)."], "Ghi rõ các loại phản hồi")
    s.row(9, 3, [None, None, "Xem xét phản hồi, xác định nội dung nhu cầu cần điều chỉnh."],
          "Lỗi: bước quá chung")
    s.row(9, 4, [None, None, "Điều chỉnh loại nguồn lực, quy mô FTE, thời gian hoặc giai đoạn và mức tham gia "
                 "%FTE của từng vị trí (CN-10)."], "Lỗi: bước quá chung; nêu các thông tin được điều chỉnh "
          "theo QT-02, QT-03")
    s.row(9, 5, [None, None, "Kiểm tra và lưu thông tin điều chỉnh."],
          "Tách bước lưu khỏi bước gửi lại RM")
    s.row(9, 6, ["6", "PM", "Gửi lại nhu cầu đã điều chỉnh cho RM xem xét (CN-11)."],
          "Thay dòng “Kết thúc”: sau khi sửa, nhu cầu phải quay lại RM (QT-05)")
    s.add_row(9, 6, ["7", "Hệ thống", "Ghi nhận nhu cầu ở trạng thái “Chờ xác nhận”; RM xem xét lại ở UC-01.2."],
              "Kết thúc ở gửi lại RM")
    s.row(10, 1, ["E1", "Bước 5", "Thông tin điều chỉnh chưa hợp lệ",
                  "Hệ thống báo thông tin chưa hợp lệ; quay lại bước 4."],
          "Đánh lại mã (UC-01.3 chỉ có một luồng ngoại lệ)")
    s.add_row(10, 1, ["A1", "Bước 3", "Phản hồi từ V4 hoặc V10 không làm thay đổi nhu cầu",
                      "PM giữ nguyên nhu cầu hiện tại; use case kết thúc."],
              "Lỗi: thiếu nhánh khi xem xét lại mà nhu cầu không đổi (CN-17 “xem xét lại”, QT-04 “rà soát”)")
    # 4. Activity Diagram
    s.cell(12, 2, 1, "Gồm 2 swimlane: RM và Hệ thống.", no_pm)
    s.cell(12, 3, 1, "Tiếp nhận nhu cầu cần xem xét; hiển thị thông tin nhu cầu; xem xét nhu cầu; xác nhận nhu "
                     "cầu; ghi nhận kết quả và cập nhật “Đã xác nhận”; bàn giao nhu cầu cho V3 và V4 (RM); "
                     "chuyển nhu cầu sang V3 và V4 (Hệ thống); A1: ghi nhận nội dung cần bổ sung, chuyển lại PM.",
           "Theo AD vẽ lại: bỏ các action của PM, bàn giao đặt ở làn RM (CN-16)")
    s.cell(12, 5, 1, "Không có. Nhánh “chưa đủ điều kiện” kết thúc UC-01.2; PM xử lý tiếp ở UC-01.3.",
           "Lỗi: đoạn văn mô tả merge khác hình; sau khi bỏ action của PM thì không còn luồng quay lại")
    s.cell(12, 8, 1, "Nhu cầu chưa đủ điều kiện → RM ghi nhận nội dung cần bổ sung, điều chỉnh → Hệ thống "
                     "chuyển lại PM, trạng thái “Cần tiếp tục hoàn thiện” → kết thúc.", "Theo A1 đã sửa")
    s.cell(12, 9, 1, "Hai điểm kết thúc: sau khi hệ thống chuyển nhu cầu sang V3 và V4; hoặc sau khi chuyển lại "
                     "PM (A1).", "Theo AD vẽ lại")
    s.image(33, img(root, "II.2_AD", "AD_UC-01.2.png"), 15, "AD vẽ lại bằng draw.io theo D đã sửa")
    s.cell(13, 1, 1, "PM bắt đầu khi RM chuyển lại nhu cầu, hoặc khi nhận phản hồi từ V4/V10.",
           "QĐ-12: hai cách bắt đầu")
    s.cell(13, 3, 1, "Tra cứu nhu cầu và phản hồi; hiển thị nhu cầu và phản hồi; xem xét phản hồi; điều chỉnh "
                     "loại nguồn lực, quy mô FTE, thời gian, %FTE; kiểm tra và lưu; gửi lại RM; ghi nhận trạng "
                     "thái “Chờ xác nhận”; A1: giữ nguyên nhu cầu.", "Theo D đã sửa")
    s.cell(13, 4, 1, "“Nhu cầu cần điều chỉnh?” sau khi PM xem xét phản hồi; “Thông tin hợp lệ?” sau khi hệ "
                     "thống kiểm tra.", "Thêm decision cho A1")
    s.cell(13, 5, 1, "Một merge trước hoạt động “Điều chỉnh nhu cầu”, hợp nhất nhánh “Có” và nhánh quay lại "
                     "khi thông tin chưa hợp lệ (E1). Không còn merge ngay trước điểm kết thúc.",
           "Lỗi ký pháp: merge chỉ có một luồng ra final node")
    s.cell(13, 7, 1, "Thông tin chưa hợp lệ (E1) → quay lại merge trước “Điều chỉnh nhu cầu”.", "Theo AD vẽ lại")
    s.cell(13, 8, 1, "Thông tin hợp lệ → PM gửi lại RM → hệ thống ghi nhận “Chờ xác nhận”.",
           "Kết thúc ở gửi lại RM")
    s.cell(13, 9, 1, "Sau khi hệ thống ghi nhận “Chờ xác nhận”; hoặc sau khi PM giữ nguyên nhu cầu (A1).",
           "Theo AD vẽ lại")
    s.image(36, img(root, "II.2_AD", "AD_UC-01.3.png"), 15, "AD vẽ lại bằng draw.io theo D đã sửa")
    # Đề xuất lớp
    why_cls = "Đồng bộ với II.3 (Hình II.3-2): loại nguồn lực, quy mô, %FTE thuộc từng vị trí cần bố trí"
    s.cell(17, 1, 1, "Biểu diễn nhu cầu nguồn lực của dự án: phạm vi công việc, thời gian cần nguồn lực và "
                     "trạng thái xử lý. Gồm một hoặc nhiều ViTriCanBoTri. Đây là đối tượng trung tâm được RM xem "
                     "xét, xác nhận hoặc chuyển lại để PM điều chỉnh.", why_cls)
    s.add_row(17, 1, ["ViTriCanBoTri", "Vị trí cần bố trí trong nhu cầu: loại nguồn lực/vai trò, số lượng (FTE) "
                      "và mức tham gia %FTE.", "UC-01.1, UC-01.3; CN-04 đến CN-08"], why_cls)
    s.row(18, 3, ["ViTriCanBoTri", "vaiTro", "Loại nguồn lực hoặc vai trò cần đáp ứng."], why_cls)
    s.row(18, 4, ["ViTriCanBoTri", "soLuong", "Quy mô nguồn lực cần thiết, tính theo FTE."], why_cls)
    s.row(18, 5, [None, "thoiGianBatDau, thoiGianKetThuc", None], "Tên thuộc tính theo II.3")
    s.row(18, 6, ["ViTriCanBoTri", "tyLeFTE", None], why_cls)
    s.row(18, 9, [None, "nguonPhanHoi", None], "Tên thuộc tính theo II.3")
    s.row(18, 10, [None, "noiDung", None], "Tên thuộc tính theo II.3")
    s.row(18, 11, [None, "thoiDiem", None], "Tên thuộc tính theo II.3")
    s.add_row(20, 1, ["NhuCauNguonLuc", "Composition", "ViTriCanBoTri",
                      "Nhu cầu gồm các vị trí cần bố trí; vị trí không tồn tại ngoài nhu cầu."], why_cls)
    s.add_row(21, 1, ["NhuCauNguonLuc – ViTriCanBoTri", "1 : 1..*",
                      "Nhu cầu phải thể hiện ít nhất một loại nguồn lực (QT-02)."], why_cls)
    s.image(57, img(root, "II.3", "II3-2_Nhu_cau_va_nang_luc.png"), 15,
            "Sơ đồ lớp theo mô hình thống nhất (Hình II.3-2, nguồn draw.io)")


# ====================================================================== V3
@job("V3", "V3- Phần 2.docx")
def v3(s, root):
    pmo = "Lỗi: thiếu luồng tiêu chí tạm do PMO/Quản lý danh mục phê duyệt (CN-19)"
    s.cell(1, 4, 1, "PMO/Quản lý danh mục (phê duyệt tiêu chí tạm, CN-19)", pmo)
    s.par(8, "RM là tác nhân chính của UC-02.1; PMO/Quản lý danh mục tham gia khi phê duyệt tiêu chí tạm "
             "(CN-19). Không có include hay extend.", pmo)
    s.image(9, img(root, "II.2_UCD_vung", "UCD_UC-02.png"), 14,
            "Lỗi: UCD vùng chỉ có 02.1; dùng UCD vùng UC-02 đủ 02.1–02.3 (nguồn draw.io)")
    s.par(10, "RM và PMO/Quản lý danh mục kết nối với UC-02.1 bằng association; UCD vùng thể hiện thêm "
              "UC-02.2 và UC-02.3 cùng tác nhân Nguồn lực.", pmo)
    s.cell(3, 5, 1, "PMO/Quản lý danh mục (phê duyệt tiêu chí tạm)", pmo)
    s.cell(3, 6, 1, "RM có yêu cầu quản lý bộ tiêu chí: thêm tiêu chí, điều chỉnh mức độ hoặc điều kiện, ngừng "
                    "áp dụng tiêu chí, hoặc đề xuất tiêu chí tạm cho kỹ năng chưa có tiêu chí",
           "Bổ sung tình huống của CN-19")
    s.cell(3, 7, 1, "Danh mục kỹ năng và bộ tiêu chí hiện hành của V3 (thang 5 mức, CN-18) tra cứu được",
           "Bỏ điều kiện đăng nhập/phân quyền: không phải điều kiện nghiệp vụ (HD-MAU §3.3)")
    s.row(4, 2, [None, None, "Hệ thống cung cấp bộ tiêu chí hiện hành gồm kỹ năng, tiêu chí, thang 5 mức "
                 "(1 mới bắt đầu … 5 chuyên gia) và điều kiện"],
          "Bỏ kiểm tra quyền (HD-MAU §3.3); ghi thang 5 mức theo CN-18")
    s.row(4, 8, [None, None, "Hệ thống cập nhật bộ tiêu chí ở trạng thái sẵn sàng sử dụng"],
          "Bỏ “thông báo kết quả”: không phải bước nghiệp vụ, AD không có")
    s.del_row(5, 3, "Bỏ E1 “không có quyền”: kiểm tra quyền là cơ chế chung, không phải luồng nghiệp vụ")
    s.row(5, 4, ["E1", None, None, None], "Đánh lại mã sau khi bỏ E1, E3 cũ")
    s.row(5, 5, ["A3", "Bước 3", "Kỹ năng cần đánh giá chưa có tiêu chí.",
                 "RM đề xuất tiêu chí tạm; hệ thống ghi tiêu chí tạm ở trạng thái chờ phê duyệt. PMO/Quản lý "
                 "danh mục phê duyệt hoặc từ chối; tiêu chí tạm chỉ được dùng sau khi được duyệt. UC kết thúc."],
          "Thay E3 “lưu không thành công” (lỗi kỹ thuật, bỏ theo HD-MAU §3.3) bằng luồng CN-19 còn thiếu")
    s.row(6, 1, ["CN-18", "Hệ thống cho phép RM duy trì danh sách kỹ năng cần đánh giá, tiêu chí đánh giá và thang "
                 "mức độ thành thạo 5 mức.", "Cơ sở của toàn UC; bước 2, 3, 5."],
          "Lỗi: bảng quy tắc còn để trống")
    s.row(6, 2, ["CN-19", "Hệ thống cho phép RM đề xuất tiêu chí tạm cho kỹ năng chưa có tiêu chí; tiêu chí tạm "
                 "chờ PMO/Quản lý danh mục phê duyệt và chỉ được dùng sau khi được duyệt.", "Cơ sở của A3."],
          "Lỗi: bảng quy tắc còn để trống")
    s.add_row(6, 2, ["QT-08", "Kinh nghiệm thực tế có thể làm căn cứ khi doanh nghiệp chấp nhận; chứng chỉ hoặc "
                     "bằng cấp chỉ là một căn cứ, không mặc định là thành thạo.",
                     "Ràng buộc nội dung điều kiện công nhận của từng mức (bước 3, 4)."], "Điền quy tắc liên quan")
    s.add_row(6, 2, ["QT-07", "Kỹ năng phải được phân biệt với mức độ thành thạo; một nguồn lực có thể có nhiều "
                     "kỹ năng ở các mức khác nhau.", "Tiêu chí gắn với kỹ năng, mức độ tách riêng (bước 3)."],
              "Điền quy tắc liên quan")
    s.add_row(6, 2, ["QT-06", "Đánh giá năng lực phải dựa trên tiêu chí xác định trước.",
                     "Lý do bộ tiêu chí phải sẵn sàng trước khi đánh giá; tiêu chí tạm chưa duyệt không được dùng."],
              "Điền quy tắc liên quan")
    # 4. AD
    s.cell(7, 2, 1, "Ba làn: RM, Hệ thống, PMO/Quản lý danh mục.", pmo)
    s.cell(7, 3, 1, "RM: yêu cầu quản lý tiêu chí; xác định nội dung thay đổi; xem xét và xác nhận lưu; hủy thay "
                    "đổi (A2). Hệ thống: cung cấp bộ tiêu chí; kiểm tra tính hợp lệ; xử lý theo loại yêu cầu; "
                    "ngừng áp dụng thay vì xóa (A1); lưu thay đổi; cập nhật bộ tiêu chí sẵn sàng sử dụng; ghi "
                    "tiêu chí tạm chờ phê duyệt (A3). PMO/Quản lý danh mục: phê duyệt hoặc từ chối tiêu chí tạm.",
           "Theo AD vẽ lại")
    s.cell(7, 4, 1, "Kỹ năng chưa có tiêu chí? (A3) · Hợp lệ? (E1, quay lại bước 3) · Ngừng áp dụng tiêu chí "
                    "đang dùng? (A1, nhập lại trước bước 6) · Xác nhận lưu? (A2). Hai merge: trước bước 3 và "
                    "trước bước 6.", "Bỏ “Có quyền?”, “Lưu thành công?”; thêm A3")
    s.cell(7, 7, 1, "Bộ tiêu chí sẵn sàng sử dụng (luồng chính); hủy thay đổi (A2); PMO/Quản lý danh mục phê "
                    "duyệt hoặc từ chối tiêu chí tạm (A3).", "Theo AD vẽ lại")
    for i in (27, 28, 29):
        s.del_par(i, "Chú giải màu của hình cũ; AD vẽ lại theo ký pháp UML chuẩn, không dùng màu")
    s.image(30, img(root, "II.2_AD", "AD_UC-02.1.png"), 16,
            "AD vẽ lại bằng draw.io: bỏ E1/E3, nối A1 về trước bước 6, thêm làn PMO và A3")
    s.par(31, "Luồng chính đi qua hai làn RM và Hệ thống đến bộ tiêu chí sẵn sàng sử dụng; A1 nhập lại trước "
              "bước 6; E1 quay lại bước xác định nội dung; A2 và A3 kết thúc riêng, A3 đi qua làn PMO/Quản lý "
              "danh mục.", "Theo AD vẽ lại")
    s.par(35, "Kết quả đối chiếu dựa trên bước 1–8 và các nhánh A1, A2, A3, E1 ở mục 3; AD ở mục 4.2 dùng đúng "
              "thứ tự và điều kiện rẽ nhánh đó.", "Theo D đã sửa")
    # Đề xuất lớp
    cls = "Đồng bộ tên lớp với II.3 (Hình II.3-2)"
    no_src = "Bỏ: không có trong Phần I (II.3 không giữ lớp này)"
    s.row(9, 1, [None, "Không", "Tác nhân, không phải lớp miền."], "Lỗi: actor không phải lớp miền")
    s.row(9, 2, [None, "Không", "Là thao tác của RM trên bộ tiêu chí, không cần lưu thành đối tượng riêng."],
          no_src)
    s.row(9, 8, [None, "Không", "Phần I không yêu cầu lưu lịch sử thay đổi bộ tiêu chí thành đối tượng riêng."],
          no_src)
    s.row(10, 1, [None, "Không thuộc lớp miền", None], "RM là tác nhân")
    s.row(9, 6, [None, "Không", "Là thuộc tính dieuKienCongNhan của MucDoNangLuc (II.3)."],
          "Gộp lớp DieuKien thành thuộc tính, theo II.3")
    s.cell_replace(10, 4, 2, "E2", "E1", "Đánh lại mã ngoại lệ")
    s.cell_replace(13, 9, 2, "E2", "E1", "Đánh lại mã ngoại lệ")
    for r, c in [(3, "TieuChiNangLuc"), (4, "TieuChiNangLuc"), (5, "TieuChiNangLuc"), (7, "BoTieuChiNangLuc")]:
        s.row(10, r, [None, c, None], cls)
    s.row(10, 6, [None, "BoTieuChiNangLuc", "Bộ tiêu chí giữ trạng thái thay đổi (bước 6, A2)."], no_src)
    s.row(10, 8, [None, "Không thuộc lớp miền", "Lưu người thực hiện, thời điểm là chức năng hệ thống (bước 7)."],
          no_src)
    s.del_row(11, 1, "Lỗi: actor không phải lớp miền")
    s.del_row(11, 2, no_src)
    s.row(11, 3, ["BoTieuChiNangLuc", None, "UC-02.1 (đầu ra); CN-18, QT-06"], cls)
    s.row(11, 4, ["TieuChiNangLuc", "Một tiêu chí dùng để đánh giá năng lực; có thể là tiêu chí tạm chờ phê duyệt",
                  "UC-02.1; CN-18, CN-19"], cls)
    s.row(11, 5, ["MucDoNangLuc", "Mức đánh giá của một tiêu chí theo thang 5 mức; kèm điều kiện công nhận mức",
                  "UC-02.1; CN-18, QT-07"], "Thang 5 mức theo CN-18 (không còn “chưa xác định”)")
    s.del_row(11, 6, "Điều kiện là thuộc tính dieuKienCongNhan của MucDoNangLuc (II.3)")
    s.row(11, 7, ["KyNang", None, "UC-02.1; CN-18, QT-07"], cls)
    s.del_row(11, 8, no_src)
    for r in range(1, 7):
        s.del_row(12, r, "Lớp đã bỏ (RM, YeuCauQuanLyTieuChi)")
    for r in (7, 9):
        s.row(12, r, ["BoTieuChiNangLuc", None, None], cls)
    s.row(12, 8, ["BoTieuChiNangLuc", None, None], cls)
    s.row(12, 10, ["BoTieuChiNangLuc", None, None], cls)
    for r in (11, 12, 13):
        s.row(12, r, ["TieuChiNangLuc", None, None], cls)
    s.row(12, 14, ["TieuChiNangLuc", None, "Chờ phê duyệt (tiêu chí tạm), đang áp dụng hoặc ngừng áp dụng."],
          "Bổ sung trạng thái của CN-19")
    for r in (15, 16, 18):
        s.row(12, r, ["MucDoNangLuc", None, None], cls)
    s.row(12, 17, ["MucDoNangLuc", None, "Thứ tự mức, từ 1 (mới bắt đầu) đến 5 (chuyên gia)."], "Thang 5 mức theo CN-18")
    s.row(12, 19, ["MucDoNangLuc", "dieuKienCongNhan", "Điều kiện hoặc căn cứ công nhận mức đó (kinh nghiệm, "
                   "chứng chỉ, QT-08)."], "Gộp lớp DieuKien thành thuộc tính, theo II.3")
    s.del_row(12, 20, "Gộp vào dieuKienCongNhan")
    s.del_row(12, 21, "Gộp vào dieuKienCongNhan")
    for r in range(24, 28):
        s.del_row(12, r, no_src)
    s.del_row(13, 1, "Lớp RM đã bỏ")
    s.row(13, 2, ["BoTieuChiNangLuc", None, None], cls)
    s.row(13, 3, ["BoTieuChiNangLuc", None, "RM hủy thay đổi (A2)."], cls)
    s.row(13, 4, ["BoTieuChiNangLuc", None, None], cls)
    s.row(13, 5, ["BoTieuChiNangLuc", None, None], cls)
    for r in (6, 7, 8, 9):
        s.row(13, r, ["TieuChiNangLuc", None, None], cls)
    s.row(13, 10, ["MucDoNangLuc", None, None], cls)
    s.row(13, 11, ["TieuChiNangLuc", "pheDuyetTieuChiTam()", "PMO/Quản lý danh mục duyệt hoặc từ chối tiêu chí "
                   "tạm (A3)."], "Thay thao tác của lớp DieuKien đã gộp; bổ sung CN-19")
    s.del_row(13, 12, no_src)
    s.del_row(14, 1, "Lớp RM đã bỏ")
    s.del_row(14, 2, no_src)
    s.row(14, 3, ["BoTieuChiNangLuc", None, "TieuChiNangLuc", None], cls)
    s.row(14, 4, ["TieuChiNangLuc", "Composition", "MucDoNangLuc", "Tiêu chí gồm các mức độ."], cls)
    s.del_row(14, 5, "Lớp DieuKien đã gộp")
    s.row(14, 6, ["TieuChiNangLuc", None, "KyNang", "Tiêu chí có thể gắn với một kỹ năng."],
          "Bỏ [CẦN XÁC NHẬN]: đã chốt ở II.3")
    s.del_row(14, 7, no_src)
    s.del_row(15, 1, "Lớp RM đã bỏ")
    s.del_row(15, 2, no_src)
    s.row(15, 3, ["BoTieuChiNangLuc – TieuChiNangLuc", None, "Bộ tiêu chí cần ít nhất một tiêu chí để sẵn sàng "
                  "sử dụng."], "Bỏ [CẦN XÁC NHẬN]: đã chốt ở II.3")
    s.row(15, 4, ["TieuChiNangLuc – MucDoNangLuc", None, None], cls)
    s.del_row(15, 5, "Lớp DieuKien đã gộp")
    s.row(15, 6, ["TieuChiNangLuc – KyNang", None, "Tiêu chí gắn tối đa một kỹ năng; một kỹ năng có thể có "
                  "nhiều tiêu chí."], "Bỏ [CẦN XÁC NHẬN]: đã chốt ở II.3")
    s.del_row(15, 7, no_src)
    s.par(55, "Một bộ tiêu chí gồm nhiều tiêu chí; mỗi tiêu chí có các mức độ thành thạo kèm điều kiện công nhận",
          "Theo II.3")
    s.image(56, img(root, "II.3", "II3-2_Nhu_cau_va_nang_luc.png"), 15,
            "Sơ đồ lớp theo mô hình thống nhất (Hình II.3-2, nguồn draw.io)")
    s.par(57, "TieuChiNangLuc là lớp trung tâm của UC-02.1. MucDoNangLuc dùng thang 5 mức theo CN-18.",
          "Thang 5 mức đã có trong CN-18")


# ====================================================================== V4
@job("V4", "V4 - Phần II.docx")
def v4(s, root):
    s.image(11, img(root, "II.2_UCD_vung", "UCD_UC-03.png"), 14,
            "Lỗi: UCD vùng chỉ có 03.3; dùng UCD vùng UC-03 đủ 03.1–03.4 (nguồn draw.io). PMO giữ ở 03.3, "
            "03.4 theo QĐ-01")
    e3 = "Lỗi: thiếu hướng xử lý khi không còn ứng viên; CN-46 thuộc UC-03.2 theo II.1 (QĐ-18)"
    s.cell(3, 9, 1, "Phân loại và lý do loại được lưu; không lập shortlist. RM quay lại UC-03.2 để mở rộng sang "
                    "nguồn kế tiếp theo thứ tự ưu tiên (CN-33, QT-18); khi đã thử các nguồn mà vẫn không có ứng "
                    "viên đáp ứng, RM phản hồi về V2 ở UC-03.2 (CN-46), PM nhận ở UC-01.3 (CN-17).", e3)
    s.cell(5, 3, 2, "Kỹ năng ứng viên chưa xác nhận hoặc đã quá 6 tháng kể từ lần đánh giá gần nhất (chu kỳ "
                    "đánh giá lại định kỳ 6 tháng, CN-20).",
           "Lỗi căn cứ: QT-15 chỉ nói “quá thời hạn cập nhật”; mốc 6 tháng lấy từ CN-20")
    s.cell(5, 8, 3, "Không lập shortlist; lưu phân loại và lý do loại; UC kết thúc. RM tìm tiếp ở nguồn kế tiếp "
                    "(UC-03.2, CN-33); đã thử các nguồn mà vẫn không có ứng viên thì phản hồi V2 (UC-03.2, "
                    "CN-46).", e3)
    s.cell(6, 13, 1, "Cảnh báo kỹ năng chưa xác nhận hoặc quá thời hạn cập nhật; mốc 6 tháng theo chu kỳ đánh "
                     "giá lại định kỳ ở CN-20.", "Lỗi căn cứ mốc 6 tháng")
    s.add_row(6, 16, ["CN-33, CN-46", "Tìm theo thứ tự ưu tiên nguồn; phản hồi V2 khi đã thử các cách mà vẫn "
                      "không có ứng viên (thuộc UC-03.2).", "E3"], e3)
    s.par(28, "Decision: đủ tiền điều kiện (E1, E2); cần miễn trừ ứng viên (A2); còn ứng viên đủ điều kiện (E3). "
              "Merge: trước decision “còn ứng viên đủ điều kiện?”, hợp nhất nhánh không cần miễn trừ và nhánh "
              "sau khi PMO xử lý đề nghị miễn trừ.", "Lỗi ký pháp: hai luồng vào thẳng một decision")
    s.par(29, "Điểm kết thúc: kết thúc sớm tại E1/E2 và E3 (lưu phân loại, RM tìm tiếp ở UC-03.2); kết thúc "
              "chính sau khi lưu kết quả.", e3)
    s.image(33, img(root, "II.2_AD", "AD_UC-03.3.png"), 15,
            "AD vẽ lại bằng draw.io: tiêu đề theo tên UC, thêm merge trước decision, nhánh E3 rõ hướng xử lý")
    # Đề xuất lớp: tên theo II.3
    s.rename([8, 9, 10, 11, 12, 13, 14],
             [("BoTieuChi", "BoTieuChiPhuHop"), ("TieuChi", "TieuChiPhuHop"), ("PhienDanhGia", "PhienTimKiem"),
              ("KetQuaDanhGia", "KetQuaDanhGiaPhuHop"), ("UngVien", "NguonLuc"), ("KyNang", "NangLucKyNang")],
             "Lỗi: tên lớp trùng V3, V5; đồng bộ với II.3 (Hình II.3-3), ứng viên là NguonLuc, kỹ năng tham "
             "chiếu NangLucKyNang của V3")
    s.row(8, 11, [None, "Không", "Là thuộc tính vaiTroShortlist (Chinh, ThayThe) của KetQuaDanhGiaPhuHop."],
          "Shortlist là thuộc tính theo II.3")
    s.row(8, 12, [None, "Không", "Tác nhân; người thực hiện, người phê duyệt là thuộc tính của DeNghiMienTru "
                  "(nguoiPheDuyet, PCN-07)."], "Actor không phải lớp miền")
    s.row(9, 6, [None, None, "Gán vaiTroShortlist (Chinh, ThayThe) cho các kết quả đủ điều kiện."],
          "Shortlist là thuộc tính theo II.3")
    s.row(11, 5, [None, "maNguonLuc, hoTen, loaiNguon",
                  "loaiNguon: NoiBo, CongTacVienDoiTac, TuyenNgoai (QĐ-14); xung đột lợi ích ghi ở "
                  "KetQuaDanhGiaPhuHop.coXungDotLoiIch."], "Đồng bộ thuộc tính với II.3")
    s.del_row(10, 10, "Shortlist là thuộc tính vaiTroShortlist")
    s.del_row(10, 11, "Bỏ lớp NguoiDung: actor không phải lớp miền")
    s.row(10, 6, ["NangLucKyNang", "Kỹ năng, mức thành thạo, trạng thái xác nhận của nguồn lực (lấy từ hồ sơ "
                  "năng lực V3)", "CN-30, CN-36, QT-15"], "Kỹ năng ứng viên tham chiếu hồ sơ năng lực V3")
    s.row(11, 1, [None, "maNhuCau, phamViCongViec, thoiGianBatDau, thoiGianKetThuc, trangThai",
                  "Nhu cầu từ V2; loại nguồn lực, quy mô, %FTE thuộc ViTriCanBoTri (II.3)."],
          "Đồng bộ thuộc tính với II.3")
    s.row(11, 6, [None, "mucThanhThao, trangThaiXacNhan, ngayDanhGia, canCuXacNhan",
                  "mucThanhThao thang 1 đến 5; quá 6 tháng kể từ ngayDanhGia thì cảnh báo (CN-20, CN-36)."],
          "Đồng bộ thuộc tính với II.3; sửa căn cứ mốc 6 tháng")
    s.row(11, 7, [None, "phanLoai, lyDoKhongDat, diemTong, thuHang, vaiTroShortlist, mucDapUng, "
                  "khoangThieuNangLuc, coXungDotLoiIch", None], "Đồng bộ thuộc tính với II.3 (QĐ-15)")
    s.row(11, 9, [None, "lyDo, trangThai, nguoiPheDuyet, thoiDiemQuyetDinh", None],
          "Ghi người phê duyệt (QT-13, PCN-07) thay lớp NguoiDung")
    s.del_row(11, 10, "Shortlist là thuộc tính")
    s.del_row(11, 11, "Bỏ lớp NguoiDung")
    s.del_row(12, 6, "Shortlist là thuộc tính")
    s.del_row(13, 4, "Bỏ lớp NguoiDung")
    s.row(13, 7, [None, None, None, "Kỹ năng của nguồn lực lấy từ hồ sơ năng lực V3 (HoSoNangLuc)."],
          "Không gắn kỹ năng trực tiếp vào ứng viên")
    s.del_row(13, 11, "Bỏ lớp NguoiDung")
    s.del_row(13, 12, "Shortlist là thuộc tính")
    s.del_row(13, 13, "Shortlist là thuộc tính")
    s.del_row(14, 4, "Bỏ lớp NguoiDung")
    s.del_row(14, 11, "Bỏ lớp NguoiDung")
    s.del_row(14, 12, "Shortlist là thuộc tính")
    s.del_row(14, 13, "Shortlist là thuộc tính")
    s.image(56, img(root, "II.3", "II3-3_Tim_kiem_kha_nang_tham_gia_lich.png"), 16,
            "Sơ đồ lớp theo mô hình thống nhất (Hình II.3-3, nguồn draw.io)")


# ====================================================================== V5
@job("V5", "NV05 I2 - I3.docx")
def v5(s, root):
    name = "Thống nhất một tên UC theo II.1"
    s.cell(0, 4, 1, "Đánh giá khả năng tham gia", name)
    for i in (9, 11, 12, 13, 14, 15, 34, 35, 36, 37, 38, 39):
        s.del_par(i, "Xóa chữ mẫu của biểu mẫu")
    s.image(10, img(root, "II.2_UCD_vung", "UCD_UC-04.png"), 14,
            "Lỗi: tiêu đề “PHÂN HỆ V5”, RM chỉ nối 04.1; dùng UCD vùng UC-04 (nguồn draw.io)")
    s.cell(3, 6, 1, "PM gửi yêu cầu nguồn lực của dự án mới hoặc dự án mở rộng phạm vi, kèm khung thời gian "
                    "(CN-127); RM tiếp nhận cùng shortlist từ V4 (CN-47).", "QĐ-11: giữ CN-127 là đầu vào của 04.1")
    s.cell(3, 8, 1, "Kết luận và căn cứ được ghi nhận cho từng ứng viên trong shortlist. Kết luận đáp ứng đầy đủ "
                    "được bàn giao V6, cờ rủi ro quá tải Mức 2 đi kèm sang V6 và V10; xung đột phân bổ cứng chuyển "
                    "V7; đáp ứng một phần chuyển UC-04.2; vượt tải ngoại lệ chuyển UC-04.3. Ứng viên có dữ liệu "
                    "chưa đủ rõ giữ trạng thái chờ xác nhận, không bàn giao như kết luận đủ căn cứ.",
           "Bổ sung đích của cờ Mức 2 (CN-50)")
    flow = "Lỗi: D xét từng ứng viên nhưng không có vòng lặp; mọi nhánh phải qua ghi nhận kết luận (CN-51) " \
           "rồi mới rẽ; đánh số lại cho trùng AD"
    steps = [
        ("1", "RM", "Tiếp nhận yêu cầu nguồn lực, khung thời gian và shortlist ứng viên đã qua V4 (CN-47, "
                    "CN-127). Yêu cầu gấp thì xử lý theo A6."),
        ("2", "Hệ thống", "Kiểm tra tính đầy đủ của yêu cầu và shortlist. Thiếu thông tin cần thiết thì "
                          "chuyển A1."),
        ("3", "Hệ thống", "Với từng ứng viên: tra cứu năng lực chuẩn, lịch, thời gian nghỉ, phân bổ cứng và "
                          "phân bổ mềm trong khung thời gian; kiểm tra độ mới, độ rõ của dữ liệu (CN-48). "
                          "Dữ liệu chưa đủ rõ thì chuyển A2."),
        ("4", "RM", "Xác định năng lực khả dụng thực tế: năng lực chuẩn trừ thời gian nghỉ, thời gian không "
                    "tính phí và phân bổ cứng (CN-49, QT-21)."),
        ("5", "RM", "Đối chiếu mức sử dụng với ngưỡng bền vững 70–85%; trên 85% thì xem riêng phần đang chờ "
                    "xác nhận; trên 90% kéo dài liên tục trên 2 tuần thì gắn cờ rủi ro quá tải Mức 2. Cờ đi "
                    "kèm kết luận sang V6, V10 và không tự kích hoạt V7 (CN-50, QT-22)."),
        ("6", "RM", "Ghi nhận kết luận theo một trong bốn trạng thái: đáp ứng đầy đủ, đáp ứng một phần, không "
                    "thể tham gia, chờ xác nhận; kèm căn cứ đánh giá (CN-51)."),
        ("7", "Hệ thống", "Lưu kết luận và căn cứ của ứng viên. Còn ứng viên trong shortlist thì quay lại "
                          "bước 3."),
        ("8", "RM", "Tổng hợp kết luận của từng ứng viên để bàn giao (CN-59)."),
    ]
    for r, v in enumerate(steps, 1):
        s.row(4, r, list(v), flow)
    s.add_row(4, 8, ["9", "Hệ thống", "Chuyển hồ sơ theo kết luận: đáp ứng đầy đủ sang V6; trùng phân bổ "
                     "cứng sang V7 (A3); đáp ứng một phần sang UC-04.2 (A4); vượt tải ngoại lệ sang UC-04.3 (A5)."],
              flow)
    s.row(5, 1, [None, "2", None, None], "Đánh số theo D đã sửa")
    s.row(5, 2, [None, "3", None, "Gắn nhãn “dữ liệu chưa đủ rõ”. RM chọn: chờ xác nhận trong 2 ngày làm việc; "
                 "hoặc không chờ thì coi như chưa có dữ liệu và yêu cầu xác nhận ngay (CN-52, QT-24). Kết luận "
                 "của ứng viên là “chờ xác nhận”, không bàn giao như kết luận đủ căn cứ; tiếp tục bước 6."],
          "Lỗi: thiếu nhánh “không chờ” theo CN-52; bỏ mã BR-V5-08")
    s.row(5, 3, [None, "9", None, "RM ghi nhận xung đột trong kết luận; ở bước 9 hồ sơ xung đột được chuyển V7 "
                 "(CN-55, QT-26). V5 không quyết định ưu tiên giữa các dự án."],
          "Rẽ nhánh sau khi đã ghi nhận kết luận (CN-51)")
    s.row(5, 4, [None, "9", "Kết luận đáp ứng một phần", "Chuyển UC-04.2: RM đề xuất tỷ lệ phân bổ và khung thời "
                 "gian (CN-53); PM xác nhận hoặc không xác nhận phân bổ một phần là không ảnh hưởng nghiêm trọng; "
                 "không xác nhận thì RM ghi nhận từ chối kèm hướng xử lý (CN-54, QT-23)."],
          "Rẽ nhánh sau khi đã ghi nhận kết luận (CN-51)")
    s.row(5, 5, [None, "9", "Vượt tải ngoại lệ: nguồn lực quan trọng bị nhiều phần giữ chỗ mềm cùng khóa",
                 "Chuyển UC-04.3 theo Ma trận phân quyền: PMO/Quản lý danh mục phê duyệt Mức 2–3, CEO/Managing "
                 "Director khi chạm Mức 4–5 (CN-56, CN-57, QT-25)."],
          "Ghi điều kiện theo CN-56; rẽ nhánh sau khi đã ghi nhận kết luận")
    s.row(5, 6, [None, "1", "Yêu cầu gấp có thời hạn dưới 24–48 giờ",
                 "RM đánh giá nhanh dựa trên phân bổ cứng, ghi nhận rủi ro và tiếp tục theo dõi (CN-58); UC kết "
                 "thúc."], "QĐ-04: ghi đúng như Phần I, không tự chọn 24 hay 48 giờ")
    codes = "Lỗi: mã BR-V5 không tra được trong Phần I; đổi theo mã QT/CN của Phần I"
    rules = [
        ("QT-20, CN-59", None),
        ("QT-26, CN-55", None),
        ("QT-21, CN-49", None),
        ("QT-22, CN-50", None),
        ("CN-50", None),
        ("QT-22, CN-50", "Mức sử dụng trên 90% kéo dài liên tục trên 2 tuần được gắn cờ rủi ro quá tải Mức 2; cờ "
                         "đi kèm kết luận sang V6, V10 và không tự kích hoạt V7."),
        ("QT-24, CN-52", None),
        ("CN-52", "Nếu không chờ xác nhận thì coi như chưa có dữ liệu và yêu cầu xác nhận ngay."),
        ("QT-23, CN-53, CN-54", None),
        ("QT-25, CN-56, CN-57", None),
        ("CN-58", "Yêu cầu gấp có thời hạn dưới 24–48 giờ được đánh giá nhanh dựa trên phân bổ cứng, ghi nhận "
                  "rủi ro và tiếp tục theo dõi."),
    ]
    for r, (c, t) in enumerate(rules, 1):
        s.row(6, r, [c, t, None], codes)
    s.cell(7, 4, 1, "Yêu cầu gấp? (A6) · Đủ thông tin? (A1) · Dữ liệu đủ rõ? (A2) · Chờ xác nhận? (A2: chờ hoặc "
                    "không chờ) · Còn ứng viên cần đánh giá? (vòng lặp từng ứng viên). Merge: trước bước 2, trước "
                    "bước 3 (vòng lặp), trước bước 6.", flow)
    s.cell(7, 6, 1, "Theo A1–A6 tại mục 3.3 và QT-20–QT-26, CN-47–CN-59 tại mục 3.4", codes)
    s.cell(7, 7, 1, "Sau khi chuyển hồ sơ theo kết luận (bước 9); hoặc sau đánh giá nhanh yêu cầu gấp (A6).",
           "Theo AD vẽ lại: mọi nhánh kết thúc bằng final node")
    s.image(40, img(root, "II.2_AD", "AD_UC-04.1.png"), 16,
            "AD vẽ lại bằng draw.io: action RM ở làn RM, có vòng lặp ứng viên, đủ hai nhánh A2, rẽ nhánh sau "
            "ghi nhận kết luận")
    s.cell(8, 5, 0, "Khớp các quy tắc QT-20–QT-26, CN-47–CN-59", codes)
    # Đề xuất lớp
    cls = "Lỗi: KetQuaDanhGia trùng tên lớp kết quả của V4; đồng bộ với II.3 (Hình II.3-3)"
    s.rename([10, 11, 12, 13, 14, 15], [("KetQuaDanhGia", "KetLuanKhaNangThamGia")], cls)
    nocls = "II.3 không giữ lớp YeuCauXacNhan: ngày yêu cầu, hạn xác nhận, lý do chờ là thuộc tính của " \
            "KetLuanKhaNangThamGia"
    s.row(9, 6, [None, "Không", "Ngày yêu cầu, hạn xác nhận (2 ngày làm việc) và lý do chờ là thuộc tính của "
                 "KetLuanKhaNangThamGia."], nocls)
    s.row(10, 6, [None, "KetLuanKhaNangThamGia", "Theo dõi hạn xác nhận 2 ngày làm việc (CN-52)."], nocls)
    for t, r, c in [(11, 1, "QĐ-11; CN-47, CN-127"), (11, 2, "CN-48, CN-49"), (11, 3, "CN-48, CN-52; QT-24"),
                    (11, 4, "CN-48, CN-55"), (11, 5, "CN-50, CN-51, CN-59"), (11, 7, "CN-53, CN-54; QT-23"),
                    (11, 8, "CN-56, CN-57; QT-25")]:
        s.cell(t, r, 2, c, codes)
    s.del_row(11, 6, nocls)
    s.row(12, 5, [None, "trangThaiKhaNang, mucSuDung, thoiGianTrong, coRuiRoQuaTai, ngayYeuCauXacNhan, hanXacNhan, "
                  "lyDoChoXacNhan, canCuDanhGia", "Kết luận, cờ rủi ro Mức 2, theo dõi chờ xác nhận và căn cứ."],
          "Đồng bộ thuộc tính với II.3; nhận thuộc tính của YeuCauXacNhan")
    s.del_row(12, 6, nocls)
    s.row(13, 10, ["KetLuanKhaNangThamGia", "capNhatTrangThaiXacNhan()", None], nocls)
    s.row(14, 3, [None, None, None, "Mỗi nguồn lực có một lịch tổng hợp hiện hành."], "QĐ-05: NguonLuc–LichNguonLuc 1–1")
    s.del_row(14, 5, nocls)
    s.row(15, 3, [None, "1 — 1", "Mỗi nguồn lực có một lịch tổng hợp hiện hành (QĐ-05)."],
          "QĐ-05: NguonLuc–LichNguonLuc 1–1")
    s.del_row(15, 5, nocls)
    s.row(15, 6, [None, "1 — 0..*", "Một kết luận có thể có nhiều lần đề xuất một phần khi PM không xác nhận."],
          "Lỗi: bảng để hai lựa chọn; chọn theo II.3")
    s.row(15, 7, [None, "1 — 0..*", "Kết luận bình thường không có hồ sơ vượt tải; một kết luận có thể có nhiều "
                  "lần chuyển cấp."], "Lỗi: bảng để hai lựa chọn; chọn theo II.3")
    s.par(61, "11. Xác định multiplicity", "Lỗi: tiêu đề mục 11 dính mục 12")
    s.del_par(64, "Xóa chữ mẫu")
    s.add_par(64, "12. Domain/Class Diagram đề xuất", "Tách mục 12", like=61)
    s.image(65, img(root, "II.3", "II3-3_Tim_kiem_kha_nang_tham_gia_lich.png"), 16,
            "Sơ đồ lớp theo mô hình thống nhất (Hình II.3-3, nguồn draw.io): bội số đặt đúng đầu")


# ====================================================================== V6
@job("V6", "V6 - Phần II.docx")
def v6(s, root):
    s.image(11, img(root, "II.2_UCD_vung", "UCD_UC-05.png"), 14,
            "Lỗi: UCD vùng chỉ có 05.1, association có mũi tên; dùng UCD vùng UC-05 (nguồn draw.io)")
    s.cell(4, 6, 2, "Lưu phương án chính ở trạng thái \"đang xây dựng\"; bắt đầu tính thời hạn tối đa 3 ngày làm "
                    "việc (CN-73, QT-31).", "QĐ-13: CN-73 thuộc 05.1, theo dõi như một sự kiện của trạng thái")
    s.row(5, 5, [None, "Bước 9", "Trước khi gửi PM, phương án đã ở trạng thái \"đang xây dựng\" quá 3 ngày làm việc",
                 "RM ghi lý do và báo cáo PMO (CN-73, QT-31); tiếp tục bước 9."],
          "QĐ-13: kiểm tra một lần như sự kiện theo dõi, không lặp ở mọi bước; thêm vào AD")
    s.add_row(6, 12, ["CN-73", "Theo dõi thời hạn 3 ngày làm việc của phương án \"đang xây dựng\"; quá hạn thì ghi "
                      "lý do, báo cáo PMO", "Bước 6, E1"], "QĐ-13")
    s.par(21, "Điểm bắt đầu: RM tiếp nhận nhu cầu và danh sách ứng viên khả dụng, hoặc nhận phản hồi điều chỉnh từ "
              "UC-05.2 (A4). Điểm kết thúc: hệ thống ghi nhận việc gửi và chuyển phương án cho PM (sang UC-05.2).",
          "Lỗi: 05.1 kết thúc ở gửi PM (CN-68); PM xác nhận thuộc 05.2 (CN-69)")
    s.par(22, "Swimlane: RM, Hệ thống. PM không có action trong UC-05.1.", "Bỏ làn PM theo CN-68, CN-69")
    s.par(23, "Decision: bắt đầu từ phản hồi điều chỉnh (A4); có ứng viên đáp ứng đầy đủ (A3); có vị trí chỉ một "
              "ứng viên đạt (A1); dự án gấp, chưa đủ thời gian (A2); quá 3 ngày làm việc ở \"đang xây dựng\" (E1).",
          "Theo AD vẽ lại")
    s.image(39, img(root, "II.2_AD", "AD_UC-05.1.png"), 15,
            "AD vẽ lại bằng draw.io: bỏ decision “PM phê duyệt?”, A4 nối về trước bước 5, thêm E1 và bước 10")
    s.cell(7, 6, 0, "Các Alternative/Exceptional Flow trong UCD được thể hiện trên AD (A1 đến A4 và E1 bằng nhánh)",
           "Theo AD vẽ lại")
    cls = "Lỗi: lớp lịch thứ hai và trùng tên kết luận V5; dùng PhanBoNguonLuc, KetLuanKhaNangThamGia (II.3)"
    s.rename([8, 9, 10, 11, 12, 13, 14], [("LichPhanBo", "PhanBoNguonLuc"),
                                          ("KhaNangThamGia", "KetLuanKhaNangThamGia")], cls)
    s.row(10, 7, [None, "Phân bổ hiện tại của nguồn lực (thuộc LichNguonLuc, V5)", "CN-61, V5, V10"], cls)
    s.row(11, 7, [None, "loaiPhanBo, tuNgay, denNgay, tyLe, trangThaiXacNhan", "Phân bổ cứng hoặc mềm hiện tại"],
          "Đồng bộ thuộc tính với II.3")
    s.row(11, 8, [None, "trangThaiKhaNang, mucSuDung, thoiGianTrong, coRuiRoQuaTai", "Kết luận từ V5"],
          "Đồng bộ thuộc tính với II.3")
    s.row(11, 10, [None, "vaiTroDuocGan, tyLeThamGia, tuNgay, denNgay", None], "Đồng bộ thuộc tính với II.3")
    s.row(13, 7, [None, None, "HoSoNangLuc, LichNguonLuc", "Năng lực và lịch tổng hợp; phân bổ hiện tại nằm "
                  "trong LichNguonLuc"], cls)
    s.row(13, 8, ["PhanBoNguonLuc", None, None, None], cls)
    s.row(14, 8, ["NguonLuc và LichNguonLuc; LichNguonLuc và PhanBoNguonLuc", "1 và 1; 1 và 0..*",
                  "Một lịch tổng hợp cho mỗi người (QĐ-05), gồm các phân bổ ở nhiều dự án"], cls)
    s.image(60, img(root, "II.3", "II3-4_Phuong_an_xung_dot_phe_duyet.png"), 16,
            "Sơ đồ lớp theo mô hình thống nhất (Hình II.3-4, nguồn draw.io)")


# ====================================================================== V7
@job("V7", "MNV7_II_Thiết kế Logic.docx")
def v7(s, root):
    sc = "Lỗi phạm vi: phân tích ngưỡng thuộc UC-06.1, phân xử thuộc UC-06.3 (extend); PMO không thao tác " \
         "trong UC-06.2"
    code = "Lỗi: dùng nhầm mã CN-01..14, QT-01..08 của V2; đổi theo mã V7 trong Phần I"
    s.cell(1, 4, 1, "Không có (PMO/Quản lý danh mục, CEO/Managing Director phân xử ở UC-06.3)", sc)
    s.row(2, 1, [None, None, None, "RM điều phối đàm phán, làm mịn, san bằng, ghi nhật ký và bàn giao phương án "
                 "(CN-79–CN-82, CN-87, CN-88)."], sc)
    s.row(2, 2, [None, None, None, "PM các dự án liên quan đàm phán chia sẻ, thay thế hoặc điều chỉnh nhu cầu "
                 "(CN-78); cùng RM lập đề xuất thay đổi khi bế tắc hoàn toàn (CN-82)."], code)
    s.row(2, 3, ["UC-06.3", "<<extend>>", "UC-06.2", "Hết 3 ngày làm việc chưa thống nhất hoặc bế tắc thì RM "
                 "chuyển hồ sơ sang phân xử (CN-83, QT-36)."], "Lỗi UCD: bỏ include 06.1, thêm 06.3 extend 06.2")
    s.row(2, 4, ["UC-06.1", "Không dùng include", "UC-06.2", "UC-06.1 cung cấp danh sách điểm xung đột Mức 3 trở "
                 "lên; đây là trình tự nghiệp vụ."], "Lỗi UCD: bỏ include 06.1")
    s.image(9, img(root, "II.2_UCD_vung", "UCD_UC-06.png"), 14, "Dùng UCD vùng UC-06 thống nhất (nguồn draw.io)")
    s.cell(3, 3, 1, "RM điều phối các PM liên quan đàm phán chia sẻ, thay thế hoặc điều chỉnh nhu cầu nguồn lực; "
                    "làm mịn hoặc san bằng nguồn lực; lập đề xuất thay đổi khi bế tắc hoàn toàn; ghi nhật ký và "
                    "bàn giao phương án đã cân đối cho V8, V9, V10.", sc)
    s.cell(3, 5, 1, "Không có (PMO/Quản lý danh mục, CEO/Managing Director phân xử ở UC-06.3)", sc)
    s.cell(3, 6, 1, "Có điểm xung đột Mức 3 trở lên cần xử lý chính thức từ UC-06.1. Nguồn kích hoạt: phương án "
                    "nghi ngờ xung đột từ V6 (CN-72) hoặc hồ sơ xung đột lịch từ V5 (CN-55).",
           "Lỗi: nguồn kích hoạt là V6, V5; V10 chỉ cung cấp thông tin (CN-75)")
    s.cell(3, 7, 1, "(1) Đã có danh sách điểm xung đột, đánh giá ảnh hưởng và kịch bản cân đối từ UC-06.1 "
                    "(CN-74–CN-77). (2) Lịch nguồn lực tập trung, kế hoạch tiến độ (đường găng, khoảng dự trữ) và "
                    "xếp hạng danh mục tra cứu được; thông tin thiếu/dư từ V10 dùng để tham khảo (CN-75).",
           "Bước 1–2 cũ chuyển thành tiền điều kiện; sửa nguồn")
    s.cell(3, 8, 1, "Phương án đã cân đối, nhật ký xử lý xung đột và đề xuất thay đổi (nếu có) được bàn giao V8, "
                    "V9, V10 (CN-88); nhật ký lưu tối thiểu 3 năm (PCN-06).",
           "Lỗi: Phần I quy định lưu tối thiểu 3 năm (PCN-06), không phải “vĩnh viễn”")
    s.cell(3, 9, 1, "Hết 3 ngày làm việc chưa thống nhất hoặc bế tắc: RM chuyển hồ sơ sang UC-06.3 (CN-83). Bế "
                    "tắc hoàn toàn: đề xuất lùi mốc tiến độ gốc hoặc cắt giảm phạm vi đi kèm phương án sang V8 rà "
                    "soát (CN-82, CN-86).", sc)
    steps = [
        ("1", "RM", "Chọn điểm xung đột cần cân đối từ danh sách của UC-06.1; mở phiên đàm phán với PM các dự án "
                    "liên quan (CN-79)."),
        ("2", "Hệ thống", "Hiển thị điểm xung đột, kịch bản cân đối, đường găng, khoảng dự trữ và xếp hạng danh "
                          "mục; theo dõi hạn đàm phán 3 ngày làm việc (CN-79, QT-36)."),
        ("3", "PM", "PM các dự án liên quan đàm phán chia sẻ, thay thế hoặc điều chỉnh nhu cầu nguồn lực; ưu tiên "
                    "phân bổ cứng đã cam kết trước, ngang nhau thì xét xếp hạng danh mục và giá trị kinh doanh "
                    "(CN-78, QT-34)."),
        ("4", "RM", "Ghi nhận phương án được thống nhất (CN-79)."),
        ("5", "RM", "Còn khoảng dự trữ: làm mịn nguồn lực, điều chỉnh thời điểm phân bổ trong khoảng dự trữ, không "
                    "tự thay đổi ngày hoàn thành khi chưa qua kiểm soát thay đổi (CN-80, QT-35)."),
        ("6", "Hệ thống", "Ghi điều chỉnh trên phương án; kiểm tra tổng tỷ lệ phân bổ của mỗi người trên các dự "
                          "án không quá 100% công suất chuẩn (QT-32)."),
        ("7", "RM", "Ghi nhật ký xử lý xung đột: điểm xung đột, đàm phán, điều chỉnh (CN-87, QT-38)."),
        ("8", "RM", "Hoàn thiện phương án đã cân đối, kèm đề xuất thay đổi nếu có, và bàn giao V8, V9, V10 "
                    "(CN-88)."),
        ("9", "Hệ thống", "Lưu nhật ký (tối thiểu 3 năm, PCN-06) và chuyển phương án sang V8, V9, V10."),
    ]
    for r, v in enumerate(steps, 1):
        s.row(4, r, list(v), "Lỗi: bước 1–2 cũ thuộc UC-06.1; bước 3 PM đàm phán (CN-78), RM điều phối (CN-79); "
                             "bỏ “vĩnh viễn”; mã theo Phần I")
    s.del_row(4, 10, "Gộp vào bước 8–9")
    s.row(5, 1, ["A1", "3–4", "Hết 3 ngày làm việc chưa thống nhất hoặc bế tắc",
                 "RM chuyển hồ sơ chuyển cấp sang UC-06.3 (CN-83, QT-36); UC-06.2 kết thúc. Việc phân xử của "
                 "PMO/Quản lý danh mục hoặc CEO/Managing Director thuộc UC-06.3."], sc)
    s.row(5, 2, ["A2", "5", "Hết khoảng dự trữ, chưa bế tắc hoàn toàn",
                 "RM san bằng nguồn lực trong hạn mức công suất (CN-81); phương án ảnh hưởng đường găng, tiến độ "
                 "hoặc phạm vi thì PM liên quan đánh giá tác động. Tiếp tục bước 6."],
          "Tách nhánh san bằng (CN-81)")
    s.row(5, 3, ["A3", "5", "Bế tắc hoàn toàn: khoảng dự trữ bằng 0, không có người thay thế, không thể thuê ngoài",
                 "RM và PM lập đề xuất lùi mốc tiến độ gốc hoặc cắt giảm phạm vi (CN-82, QT-37); đề xuất đi kèm "
                 "phương án sang V8 rà soát trước (CN-86, QT-39). Tiếp tục bước 6."],
          "Lỗi: bỏ “Fallback, thuê ngoài khẩn” không có trong Phần I; dùng điều kiện bế tắc của QT-37")
    s.del_row(5, 4, "Lỗi: tỷ lệ 50/50 và cơ chế job-sharing không có trong Phần I")
    s.row(5, 5, [None, "1", "Điểm xung đột dưới Mức 3 (không quá 120% và không thuộc dự án Hạng ưu tiên 1)",
                 "Chỉ ghi nhận để theo dõi; UC kết thúc (QT-33)."],
          "Lỗi: “< 20%”, “chuyển PM tự đàm phán” không có trong Phần I")
    rules = [
        ("CN-78", "PM các dự án liên quan đàm phán chia sẻ, thay thế hoặc điều chỉnh nhu cầu nguồn lực.", "Bước 3"),
        ("CN-79", "RM điều phối, ghi nhận phương án thống nhất hoặc yêu cầu chuyển cấp; theo dõi hạn 3 ngày làm "
                  "việc.", "Bước 1, 2, 4; A1"),
        ("CN-80", "Làm mịn trong khoảng dự trữ, không tự thay đổi ngày hoàn thành.", "Bước 5"),
        ("CN-81", "San bằng nguồn lực trong hạn mức công suất khi hết khoảng dự trữ.", "A2"),
        ("CN-82", "Đề xuất lùi mốc tiến độ gốc hoặc cắt giảm phạm vi khi bế tắc hoàn toàn.", "A3"),
        ("CN-83", "Chuyển hồ sơ chuyển cấp đến PMO/Quản lý danh mục khi hết hạn đàm phán hoặc bế tắc.",
         "A1 (sang UC-06.3)"),
        ("CN-86, CN-87, CN-88", "Đề xuất thay đổi qua V8 rà soát; ghi nhật ký xử lý xung đột; bàn giao phương án "
                                "cho V8, V9, V10.", "Bước 7–9; A3"),
        ("QT-32", "Tổng tỷ lệ phân bổ của một người trên tất cả dự án không quá 100% công suất chuẩn.", "Bước 6"),
        ("QT-33", "Chỉ xử lý chính thức từ Mức 3 (trên 120% hoặc dự án Hạng ưu tiên 1); dưới ngưỡng chỉ theo dõi.",
         "E1"),
        ("QT-34", "Ưu tiên phân bổ cứng đã cam kết trước; ngang nhau thì xét xếp hạng danh mục và giá trị kinh "
                  "doanh.", "Bước 3"),
        ("QT-35", "Làm mịn chỉ trong khoảng dự trữ, không tự lùi ngày hoàn thành khi chưa qua kiểm soát thay đổi.",
         "Bước 5"),
        ("QT-36", "PM tự đàm phán tối đa 3 ngày làm việc; PMO quyết định trong 1 ngày làm việc; Mức 4–5 chuyển "
                  "CEO/Managing Director.", "Bước 2; A1"),
        ("QT-37", "Bế tắc hoàn toàn buộc chọn lùi mốc tiến độ gốc hoặc cắt giảm phạm vi.", "A3"),
        ("QT-38, QT-39; PCN-06", "Ghi mọi điểm xung đột, đàm phán, phân xử vào nhật ký, lưu tối thiểu 3 năm; đề "
                                 "xuất thay đổi qua V8 rà soát trước.", "Bước 7, 9; A3"),
    ]
    for r, v in enumerate(rules, 1):
        s.row(6, r, list(v), code)
    s.par(21, "• Điểm bắt đầu: RM chọn điểm xung đột cần cân đối từ danh sách của UC-06.1.", sc)
    s.par(22, "• Swimlanes: RM, PM, Hệ thống. PMO/Quản lý danh mục không có action trong UC-06.2.", sc)
    s.par(24, "   - Mức 3 trở lên? (Không → E1 chỉ theo dõi, kết thúc.)", "Lỗi: “< 20%”; theo QT-33")
    s.par(25, "   - Kết quả đàm phán? (Quá 3 ngày làm việc hoặc bế tắc → A1 chuyển UC-06.3; Thống nhất → ghi "
              "nhận.)", "Guard theo CN-79")
    s.par(26, "   - Còn khoảng dự trữ? (Còn → làm mịn; Hết → Bế tắc hoàn toàn? Không → A2 san bằng; Có → A3 đề "
              "xuất thay đổi.) Ba nhánh hội tụ ở một merge trước bước 6.",
          "Lỗi: các nhánh làm mịn, san bằng, bế tắc nối nhầm; tách nhánh có guard")
    s.par(27, "• Điểm kết thúc: E1 (theo dõi), A1 (chuyển UC-06.3) hoặc kết thúc chính sau khi lưu nhật ký và "
              "chuyển phương án sang V8, V9, V10.", "Bỏ “vĩnh viễn”")
    s.image(30, img(root, "II.2_AD", "AD_UC-06.2.png"), 16,
            "AD vẽ lại bằng draw.io: mỗi nhánh tới đúng action, làn trùng actor trong D, guard theo CN-79")
    s.row(7, 1, [None, None, "RM, PM. PMO/Quản lý danh mục phân xử ở UC-06.3."], sc)
    s.row(7, 2, [None, None, "Association; UC-06.3 extend UC-06.2."], sc)
    s.row(7, 3, [None, None, "9 bước trên AD khớp bước 1–9 của luồng chính; các nhánh A1, A2, A3, E1."],
          "Theo D đã sửa")
    s.row(7, 4, [None, None, "PhuongAnBoTri, DiemXungDot, NhatKyXuLyXungDot, DeXuatThayDoi, PhanXuXungDot."],
          "Tên lớp theo II.3")
    s.row(7, 5, [None, None, "Chọn điểm xung đột → đàm phán → làm mịn, san bằng hoặc đề xuất thay đổi → ghi nhật "
                 "ký → bàn giao."], "Theo D đã sửa")
    s.row(7, 6, [None, None, "A1 (hết hạn hoặc bế tắc), A2 (san bằng), A3 (bế tắc hoàn toàn), E1 (dưới Mức 3)."],
          "Theo D đã sửa")
    s.row(7, 7, [None, None, "Bắt đầu khi chọn điểm xung đột; kết thúc sau khi lưu nhật ký và chuyển phương án "
                 "sang V8, V9, V10."], "Bỏ “vĩnh viễn”")
    # Đề xuất lớp
    cls = "Lỗi: tên lớp tiếng Anh, lớp kỹ thuật; đồng bộ với II.3 (Hình II.3-4)"
    s.rename([8, 9, 10, 11, 12, 13, 14, 16, 17],
             [("DiemXungDotNguonLuc", "DiemXungDot"), ("ConflictLog", "NhatKyXuLyXungDot"),
              ("ChangeRequest", "DeXuatThayDoi"), ("PhuongAnNguonLuc", "PhuongAnBoTri"),
              ("QuyetDinhPhanXu", "PhanXuXungDot")], cls)
    s.row(8, 1, ["Phương án bố trí (PhuongAnBoTri)", "Có", "Phương án từ V6 được cân đối và bàn giao V8, V9, V10."],
          cls)
    s.row(8, 2, ["Điểm xung đột (DiemXungDot)", "Có", "Điểm vượt ngưỡng công suất của một nguồn lực, mức cảnh báo "
                 "theo thang 5 mức (CN-74)."], cls)
    s.row(8, 3, [None, "Không", "Kịch bản thuộc phân tích ở UC-06.1 (CN-77); kết quả được ghi vào phương án và "
                 "nhật ký."], sc)
    s.row(8, 4, [None, "Không", "Ghi thành dòng NhatKyXuLyXungDot loại “đàm phán” (CN-79, QT-38)."], cls)
    s.row(8, 5, ["Hồ sơ chuyển cấp và quyết định phân xử (PhanXuXungDot)", "Có", "Một lớp; thuộc UC-06.3 "
                 "(CN-83–CN-85)."], cls)
    s.del_row(8, 6, "Gộp vào PhanXuXungDot")
    s.row(8, 7, ["Nhật ký xử lý xung đột (NhatKyXuLyXungDot)", "Có", "Ghi mọi điểm xung đột, đàm phán và phân "
                 "xử; lưu tối thiểu 3 năm (CN-87, QT-38, PCN-06)."], "Bỏ “vĩnh viễn”, “Audit Trail”")
    s.row(8, 8, ["Đề xuất thay đổi (DeXuatThayDoi)", "Có", "Lùi mốc tiến độ gốc hoặc cắt giảm phạm vi (CN-82, "
                 "CN-86)."], cls)
    beh = [
        ("Ghi nhận điểm xung đột cần cân đối", "DiemXungDot", "Lấy từ UC-06.1 (CN-74)."),
        ("Phân tích đường găng, khoảng dự trữ", "Không thuộc UC-06.2", "Thuộc UC-06.1 (CN-77)."),
        ("Làm mịn, san bằng", "PhuongAnBoTri", "Điều chỉnh thời điểm, tỷ lệ trên các dòng bố trí (CN-80, CN-81)."),
        ("Ghi nhận thỏa thuận đàm phán", "NhatKyXuLyXungDot", "Theo dõi hạn 3 ngày làm việc (CN-79)."),
        ("Chuyển hồ sơ chuyển cấp", "PhanXuXungDot", "Sang UC-06.3 (CN-83)."),
        ("Ghi quyết định phân xử", "PhanXuXungDot", "PMO hoặc CEO quyết định; lớp chỉ ghi nhận (UC-06.3, CN-84, "
                                                    "CN-85)."),
        ("Lập đề xuất thay đổi", "DeXuatThayDoi", "Lùi mốc tiến độ gốc hoặc cắt giảm phạm vi (CN-82)."),
        ("Ghi nhật ký", "NhatKyXuLyXungDot", "Lưu tối thiểu 3 năm (CN-87, QT-38, PCN-06)."),
    ]
    for r, v in enumerate(beh, 1):
        s.row(9, r, list(v), "Mã theo Phần I; bỏ “vĩnh viễn”, “không cho sửa/xóa”; phạm vi UC-06.2")
    s.row(10, 1, ["PhuongAnBoTri", "Phương án bố trí được cân đối, bàn giao V8, V9, V10.", "CN-88; II.3 (V6)"], cls)
    s.row(10, 2, ["DiemXungDot", "Điểm vượt ngưỡng công suất, mức cảnh báo theo thang 5 mức.", "CN-74; QT-33"], cls)
    s.del_row(10, 3, "Kịch bản thuộc UC-06.1")
    s.del_row(10, 4, "Ghi thành nhật ký")
    s.row(10, 5, ["PhanXuXungDot", "Hồ sơ chuyển cấp và quyết định phân xử.", "CN-83–CN-85; QT-36"], cls)
    s.del_row(10, 6, "Gộp vào PhanXuXungDot")
    s.row(10, 7, ["NhatKyXuLyXungDot", "Nhật ký mọi điểm xung đột, đàm phán, phân xử; lưu tối thiểu 3 năm.",
                  "CN-87; QT-38; PCN-06"], "Bỏ “vĩnh viễn”")
    s.row(10, 8, ["DeXuatThayDoi", "Đề xuất lùi mốc tiến độ gốc hoặc cắt giảm phạm vi.",
                  "CN-82, CN-86; QT-37, QT-39"], cls)
    s.row(11, 1, ["PhuongAnBoTri", "maPhuongAn, phienBan, loaiPhuongAn, trangThai", "Phương án được cân đối."], cls)
    s.row(11, 2, ["DiemXungDot", "maXungDot, mucSuDung, mucCanhBao", "Mức sử dụng và mức cảnh báo (thang 5 mức)."],
          cls)
    s.del_row(11, 3, "Kịch bản thuộc UC-06.1")
    s.del_row(11, 4, "Ghi thành nhật ký")
    s.row(11, 5, ["PhanXuXungDot", "ngayChuyenCap, lyDoBeTac, capPhanXu, noiDungQuyetDinh",
                  "Hồ sơ chuyển cấp và quyết định (UC-06.3)."], cls)
    s.del_row(11, 6, "Gộp vào PhanXuXungDot")
    s.row(11, 7, ["NhatKyXuLyXungDot", "thoiDiem, noiDung, loaiXuLy", "loaiXuLy: đàm phán, làm mịn, san bằng, phân "
                  "xử; lưu tối thiểu 3 năm (PCN-06)."], "Bỏ “vĩnh viễn”, auditTrailHash")
    s.row(11, 8, ["DeXuatThayDoi", "loaiThayDoi, noiDung", "loaiThayDoi: lùi mốc tiến độ gốc, cắt giảm phạm vi."],
          cls)
    s.row(12, 1, ["PhuongAnBoTri", "lamMin(), sanBang(), banGiao()", "CN-80, CN-81, CN-88."], cls)
    s.row(12, 2, ["DiemXungDot", "capNhatTrangThai()", "Cập nhật tình trạng xử lý của điểm xung đột."], cls)
    s.del_row(12, 3, "Kịch bản thuộc UC-06.1")
    s.row(12, 4, ["NhatKyXuLyXungDot", "ghiNhan(loaiXuLy, noiDung)", "Ghi đàm phán, điều chỉnh, phân xử (CN-79, "
                  "CN-87)."], cls)
    s.row(12, 5, ["PhanXuXungDot", "chuyenCap()", "RM chuyển hồ sơ sang UC-06.3 (CN-83)."], cls)
    s.row(12, 6, ["PhanXuXungDot", "ghiQuyetDinh()", "Người quyết định là PMO hoặc CEO; lớp chỉ ghi nhận (CN-84, "
                  "CN-85)."], cls)
    s.del_row(12, 7, "Gộp vào NhatKyXuLyXungDot.ghiNhan; bỏ “vĩnh viễn”")
    s.row(12, 8, ["DeXuatThayDoi", "lapDeXuat(), chuyenV8()", "CN-82, CN-86."], cls)
    s.row(13, 1, ["PhuongAnBoTri", "Association", "DiemXungDot", "Phương án có các điểm xung đột cần cân đối."], cls)
    s.del_row(13, 2, "Kịch bản thuộc UC-06.1")
    s.row(13, 3, ["DiemXungDot", "Composition", "NhatKyXuLyXungDot", "Mỗi điểm xung đột có các dòng nhật ký xử lý "
                  "(QT-38)."], cls)
    s.del_row(13, 4, "Gộp vào PhanXuXungDot")
    s.row(13, 5, ["DiemXungDot", "Association", "PhanXuXungDot", "Điểm xung đột được chuyển cấp có một hồ sơ phân "
                  "xử."], cls)
    s.del_row(13, 6, "Thay bằng quan hệ DiemXungDot–NhatKyXuLyXungDot")
    s.row(13, 7, ["PhuongAnBoTri", "Association", "DeXuatThayDoi", "Phương án có thể kèm đề xuất thay đổi khi bế "
                  "tắc hoàn toàn."], cls)
    s.row(14, 1, ["PhuongAnBoTri — DiemXungDot", "1 : 0..*", "Một phương án có không hoặc nhiều điểm xung đột."],
          cls)
    s.del_row(14, 2, "Kịch bản thuộc UC-06.1")
    s.row(14, 3, ["DiemXungDot — NhatKyXuLyXungDot", "1 : 1..*", "Ít nhất có dòng ghi nhận điểm xung đột "
                  "(QT-38)."], cls)
    s.del_row(14, 4, "Gộp vào PhanXuXungDot")
    s.row(14, 5, ["DiemXungDot — PhanXuXungDot", "1 : 0..1", "Chỉ khi hết hạn đàm phán hoặc bế tắc."], cls)
    s.del_row(14, 6, "Thay bằng DiemXungDot–NhatKyXuLyXungDot")
    s.row(14, 7, ["PhuongAnBoTri — DeXuatThayDoi", "1 : 0..*", "Đề xuất chỉ có khi bế tắc hoàn toàn."], cls)
    s.image(51, img(root, "II.3", "II3-4_Phuong_an_xung_dot_phe_duyet.png"), 16,
            "Sơ đồ lớp theo mô hình thống nhất (Hình II.3-4, nguồn draw.io)")
    # III. Ma trận kiểm soát
    for r, c in [(1, "QT-32"), (2, "QT-34"), (3, "QT-35"), (4, "QT-36"), (5, "QT-33"), (6, "QT-37")]:
        s.cell(16, r, 0, c, code)
    s.row(16, 2, [None, "Tranh chấp: ưu tiên phân bổ cứng đã cam kết trước; ngang nhau thì xét xếp hạng danh mục và "
                  "giá trị kinh doanh.", None, None], "Theo QT-34")
    s.row(16, 7, ["QT-38; PCN-06", "Mọi điểm xung đột, đàm phán và phân xử được ghi vào nhật ký xử lý xung đột.",
                  "Lưu tối thiểu 3 năm", "Bước 7, 9; lớp NhatKyXuLyXungDot"], "Bỏ “vĩnh viễn”")
    s.row(17, 2, [None, "Khối lượng làm thêm giờ khẩn cấp (Mức 5) nếu có", None, None],
          "Bỏ “thuê ngoài khẩn cấp”: không có trong Phần I")


@job("V8", "MNV8 - Ngọc Linh.docx")
def v8(s, root):
    mau = "Bỏ chữ hướng dẫn của mẫu"
    rm = ("Không có trong UC-07.1. RM chỉ tham gia ở UC-07.2 Yêu cầu giải trình và hoàn thiện phương án "
          "(CN-96)")
    s.cell(1, 4, 1, rm, "UCD_UC-07: RM chỉ nối với UC-07.2; CN-89–94 không có RM")
    s.cell(1, 5, 1, "UC-07.2 (extend); UC-07.3, UC-07.4 (bước quyết định sau rà soát). Dữ liệu tham chiếu: "
           "hồ sơ từ UC-05 (V6), UC-06 (V7); thông tin từ UC-08 (V9), UC-09 (V10)",
           "V9, V10 là nguồn dữ liệu tham chiếu, không phải UC được include")
    inc = "Bỏ include: V9, V10 là dữ liệu tham chiếu (CN-93, CN-94); 07.1 không include 07.3"
    for r in (1, 2, 3):
        s.del_row(2, r, inc)
    s.row(2, 4, ["UC-07.2", None, "UC-07.1", None], "Sửa UC đích: 07.2 mở rộng 07.1 (UCD_UC-07)")
    for i in (9, 10, 11, 12, 13, 14):
        s.del_par(i, mau)
    s.add_image(8, img(root, "II.2_UCD_vung", "UCD_UC-07.png"), 16,
                "Bài chưa có hình UCD; dùng UCD vùng UC-07 (nguồn draw.io), có 07.4, không có UC ngoài vùng")
    s.cell(3, 5, 1, rm, "Như bảng 2.1")
    s.row(4, 4, [None, None, "Hiển thị thông tin chi phí, chênh lệch ngân sách và đánh đổi từ V9; thông tin tổng "
                 "hợp cung – cầu và kết quả dự báo từ V10 để cấp thẩm quyền xem cùng hồ sơ.", None],
          "Bỏ «include»: đây là xem dữ liệu V9, V10 (CN-93, CN-94)")
    s.row(4, 5, [None, None, "Cấp thẩm quyền đánh giá các yếu tố rủi ro và kết luận hồ sơ đủ hay chưa đủ cơ sở ra "
                 "quyết định. Chưa đủ: luồng A2.", None],
          "Bước 5 là điểm rẽ nhánh; quyết định chính thức thuộc UC-07.3, 07.4 (CN-97)")
    s.cell(5, 1, 4, "CN-91; QT-41, QT-42; Hoạt động 1", "Thêm mã quy tắc của P1 cho ngưỡng và hạn chuyển cấp")
    s.row(5, 2, [None, None, "Cấp thẩm quyền phát hiện điểm bất hợp lý, rủi ro hoặc thiếu thông tin, kết luận hồ "
                 "sơ chưa đủ cơ sở ra quyết định",
                 "1. Cấp thẩm quyền lập danh sách nội dung cần giải trình, bổ sung gửi RM là người đề xuất phương án.\n"
                 "2. Hệ thống chuyển hồ sơ sang UC-07.2 (extend). UC-07.1 kết thúc.\n"
                 "Việc RM giải trình, cập nhật hồ sơ và nhánh sau giải trình (rà soát lại hoặc trả về V6/V7) được "
                 "mô tả trong UC-07.2.",
                 "CN-95, CN-96, CN-101; Hoạt động 3"],
          "07.1 không có action của RM; A2 dừng ở chuyển UC-07.2 (CN-95, CN-96)")
    s.del_par(19, mau)
    s.del_par(23, mau)
    s.cell(6, 5, 2, "Thực hiện ở Bước 4 của Luồng chính.", "Bỏ «include» UC-08")
    s.cell(6, 6, 2, "Thực hiện ở Bước 4 của Luồng chính.", "Bỏ «include» UC-09")
    s.cell(6, 7, 0, "QT-42", "Dùng mã quy tắc của P1 (QT-42 = DoA chuyển cấp)")
    s.add_row(6, 7, ["QT-41", "Quá tải trên 110% kéo dài quá 2 tuần bắt buộc CEO/Managing Director phê duyệt ngoại lệ.",
                     "Điều kiện chạm Mức 4–5 ở Luồng thay thế A1."], "Ngưỡng dùng ở A1 có nguồn QT-41")
    s.add_row(6, 6, ["CN-95", "Hệ thống cho phép PMO/Quản lý danh mục yêu cầu giải trình hoặc bổ sung thông tin gửi tới "
                     "RM là người đề xuất phương án.", "Điểm chuyển sang UC-07.2 ở Luồng thay thế A2."],
              "A2 dựa trên CN-95")
    s.par(27, "Thành phần AD UC-07.1: điểm bắt đầu (PMO tiếp nhận hồ sơ); ba làn PMO/Quản lý danh mục, Cấp thẩm "
          "quyền (PMO Mức 1–3 hoặc CEO Mức 4–5) và Hệ thống; các action bước 1–6; decision “Mức rủi ro?” "
          "([Mức 1–3] / [Mức 4–5 (A1)]) và “Đủ cơ sở ra quyết định?” ([Đủ] / [Chưa đủ (A2)]); một merge sau "
          "nhánh chuyển cấp; hai điểm kết thúc (chuyển UC-07.3/07.4 hoặc chuyển UC-07.2). Không có fork/join.",
          "Mục 4.1 chỉ còn khung mẫu; ghi thành phần theo AD đã vẽ lại")
    for i in (28, 29, 30, 31, 32, 33, 34, 36, 37, 38, 39, 40, 41):
        s.del_par(i, mau)
    s.add_image(35, img(root, "II.2_AD", "AD_UC-07.1.png"), 16,
                "AD vẽ lại khớp D: bỏ “PMO tự phê duyệt”, “Ra quyết định”, vòng RM giải trình; có A1 chuyển cấp")
    s.cell(7, 1, 2, "PMO, CEO (actor chính). RM không tham gia UC-07.1, chỉ ở UC-07.2.", "Khớp UCD và AD mới")
    s.cell(7, 2, 2, "Không có include. UC-07.2 extend UC-07.1 khi cần giải trình (CN-95).", "Bỏ include V9, V10")
    s.cell(7, 4, 2, "Bao phủ CN-89 đến CN-94; CN-95 ở luồng A2.", "Ghi đúng phạm vi")
    # II.2+ lớp
    cls = "Khớp sơ đồ lớp II.3 (Hình II.3-4, II.3-5, II.3-6)"
    s.row(8, 3, [None, "Chưa (chờ QĐ-19)", "Giữ DoA ở dạng quy tắc (CN-90, QT-40–42); kết quả đối chiếu ghi ở thuộc "
                 "tính capThamQuyen của HoSoTrinhDuyet."], "QĐ-19 chưa chốt; không tạo lớp DoA")
    s.row(8, 4, ["Thông tin chi phí V9", "Không (tham chiếu)", "Dùng lớp DanhGiaChiPhi của V9 (Hình II.3-5); V8 chỉ "
                 "xem, không sao chép (CN-93)."], "Không nhân bản dữ liệu V9")
    s.row(8, 5, ["Thông tin dự báo V10", "Không (tham chiếu)", "Dùng lớp KetQuaDuBao của V10 (Hình II.3-6); V8 chỉ "
                 "xem, không sao chép (CN-94)."], "Không nhân bản dữ liệu V10")
    s.row(9, 2, [None, "HoSoTrinhDuyet", None], "DoA là quy tắc, không phải lớp")
    s.row(9, 4, [None, "DanhGiaChiPhi (V9)", None], cls)
    s.row(9, 5, [None, "KetQuaDuBao (V10)", None], cls)
    s.del_row(10, 3, "DoA giữ ở dạng quy tắc (chờ QĐ-19)")
    s.row(10, 4, ["DanhGiaChiPhi (V9, tham chiếu)", "Lớp của V9; hồ sơ V8 tham chiếu khi rà soát.", "CN-93; Hình II.3-5"],
          cls)
    s.row(10, 5, ["KetQuaDuBao (V10, tham chiếu)", "Lớp của V10; hồ sơ V8 tham chiếu khi rà soát.",
                  "CN-94; Hình II.3-6"], cls)
    s.row(11, 1, [None, "maHoSo / ngayTrinh / mucRuiRo / capThamQuyen / trangThaiXuLy / ngayChuyenCap", None], cls)
    s.row(11, 2, [None, "maPhuongAn / phienBan / loaiPhuongAn / trangThai (chi tiết phân bổ ở ChiTietBoTri; xung đột "
                  "ở DiemXungDot)", "Lớp của V6; V8 đọc khi rà soát."], cls)
    s.del_row(11, 3, "DoA giữ ở dạng quy tắc (chờ QĐ-19)")
    s.del_row(11, 4, "Thuộc tính thuộc lớp DanhGiaChiPhi của V9")
    s.del_row(11, 5, "Thuộc tính thuộc lớp KetQuaDuBao của V10")
    s.row(11, 6, [None, "noiDungCanLamRo / ngayYeuCau / trangThai", None], cls)
    s.row(12, 5, ["HoSoTrinhDuyet", None, None], "DoA là quy tắc; kết quả ghi vào capThamQuyen")
    s.row(12, 6, ["DanhGiaChiPhi (V9)", None, None], cls)
    s.row(12, 7, ["KetQuaDuBao (V10)", None, None], cls)
    s.row(13, 1, ["PhuongAnBoTri", None, "HoSoTrinhDuyet", "Mỗi hồ sơ trình duyệt gắn với một phương án; một phương "
                  "án có thể được trình lại sau khi trả về V6/V7 (CN-101)."], cls)
    s.del_row(13, 2, "DoA giữ ở dạng quy tắc (chờ QĐ-19)")
    s.row(13, 3, [None, "Association (tham chiếu)", "DanhGiaChiPhi", None], cls)
    s.row(13, 4, [None, "Association (tham chiếu)", "KetQuaDuBao", None], cls)
    s.row(13, 5, [None, "Composition", None, "Hồ sơ chưa đủ cơ sở có thể có nhiều đợt yêu cầu giải trình (CN-95)."], cls)
    s.row(14, 1, ["PhuongAnBoTri — HoSoTrinhDuyet", "1 : 0..*", "Một phương án có thể có nhiều lần trình (CN-101, "
                  "CN-102 lưu phiên bản phương án); mỗi hồ sơ thuộc một phương án."], cls)
    s.del_row(14, 2, "DoA giữ ở dạng quy tắc (chờ QĐ-19)")
    s.row(14, 3, ["HoSoTrinhDuyet — DanhGiaChiPhi", "0..* : 0..*", "Tham chiếu kết quả đánh giá chi phí của V9."], cls)
    s.row(14, 4, ["HoSoTrinhDuyet — KetQuaDuBao", "0..* : 0..1", "Tham chiếu kết quả dự báo của V10."], cls)
    s.del_par(60, mau)
    s.add_image(59, img(root, "II.3", "II3-4_Phuong_an_xung_dot_phe_duyet.png"), 16,
                "Bài chưa có sơ đồ lớp trong Word; dùng Hình II.3-4 (nguồn draw.io)")
    s.del_par(62, "Ghi chú nội bộ về quyền sửa file draw.io, không thuộc nội dung báo cáo")
    s.del_par(63, "Ghi chú nội bộ")


@job("V9", "V9 - Phần II.docx")
def v9(s, root):
    ten = "Tính và cập nhật chi phí phương án"
    qd10 = "QĐ-10: 08.1 đúng tên và phạm vi CN-103–107 (bảng II.1); đối chiếu, so sánh, hướng xử lý thuộc FDS 08.2–08.4"
    for t, r in ((0, 4), (1, 2), (3, 2)):
        s.cell(t, r, 1, ten, qd10)
    s.cell(1, 5, 1, "UC-08.2 Đối chiếu chi phí và ngân sách (dùng kết quả chi phí của 08.1); UC-08.3, UC-08.4. "
           "Kết quả V9 được chuyển cho V8 và V10 ở UC-08.4 (CN-112)", qd10)
    s.row(2, 1, ["UC-08.1", "Không có include/extend", "—", "V8 xem thông tin chi phí của V9 (CN-93) và V9 chuyển kết quả "
                 "cho V8, V10 (CN-112) là luồng dữ liệu, không phải include."],
          "Bỏ include UC-07.1 → UC-08.1: không có trên UCD_UC-07, UCD_UC-08")
    s.par(6, "Trong V9 không có include/extend. Các UC 08.2–08.4 dùng kết quả của 08.1 theo trình tự nghiệp vụ.",
          "Bỏ mã RB-V9 không có trong Phần I")
    s.del_par(8, "Thay đường dẫn Drive bằng hình trong bài")
    s.add_image(7, img(root, "II.2_UCD_vung", "UCD_UC-08.png"), 16, "UCD vùng UC-08 (nguồn draw.io)")
    s.cell(3, 3, 1, "PM xác định phương án cần đánh giá chi phí và lượng hóa các yếu tố tạo chi phí; Tài chính cung cấp "
           "đơn giá, tính chi phí dự toán, cập nhật dự báo khi có dữ liệu thực tế hoặc thay đổi và tính lại phần chi phí "
           "bị ảnh hưởng. Kết quả chi phí là đầu vào của UC-08.2. UC không đối chiếu ngân sách và không quyết định "
           "phương án.", qd10)
    s.cell(3, 6, 1, "PM bắt đầu đánh giá chi phí cho một phương án bố trí mới hoặc có thay đổi về người, số lượng, thời "
           "gian, mức độ tham gia (CN-103, CN-107).", qd10)
    s.cell(3, 7, 1, "Có phương án bố trí và phạm vi công việc tương ứng (CN-103).",
           "Ngân sách thuộc 08.2; bỏ điều kiện phân quyền (mẫu FDS)")
    s.cell(3, 8, 1, "Chi phí dự toán, dự báo (phân biệt hai loại, QT-49) và phần chi phí bị ảnh hưởng được lưu, sẵn sàng "
           "cho UC-08.2. Không tạo Locked Baseline (thuộc V8, CN-99).", qd10 + "; bỏ ghi tài khoản")
    steps = [
        ("1", "PM", "Chọn phương án bố trí nguồn lực cần đánh giá chi phí và ghi lý do (CN-103)."),
        ("2", "System", "Hiển thị phương án, phạm vi công việc liên quan, nhân sự, số lượng, thời gian và mức độ tham gia "
         "(CN-103, CN-104)."),
        ("3", "PM", "Lượng hóa, xác nhận các yếu tố tạo chi phí: nhân sự, số lượng, thời gian, mức độ tham gia (CN-104)."),
        ("4", "Tài chính", "Cung cấp hoặc cập nhật đơn giá áp dụng; ghi nhận chi phí thực tế nếu đã phát sinh (CN-105, "
         "CN-106)."),
        ("5", "Tài chính", "Tính chi phí dự toán của phương án; khi có dữ liệu thực tế hoặc thay đổi thì cập nhật dự báo "
         "chi phí, lưu tách dự toán và dự báo (CN-106; QT-49)."),
        ("6", "PM", "Xem kết quả chi phí dự toán, dự báo của phương án (CN-104, CN-106)."),
        ("7", "System", "Lưu kết quả chi phí (dự toán, dự báo, phần bị ảnh hưởng), sẵn sàng cho UC-08.2 Đối chiếu chi phí "
         "và ngân sách."),
    ]
    for i, v in enumerate(steps, 1):
        s.row(4, i, list(v), qd10 + "; mã CN theo Phần I")
    s.del_row(4, 8, "Ghi tài khoản là yêu cầu chung (PCN-07), không phải bước nghiệp vụ")
    s.row(5, 1, [None, None, None, None, "Hệ thống xác định phần chi phí bị ảnh hưởng; Tài chính tính lại và cập nhật "
                 "dự báo (CN-107; QT-48). Tiếp bước 5."], "Mã theo Phần I; CN-107 giao việc tính lại cho Tài chính")
    s.del_row(5, 2, "Đối chiếu, tỷ lệ vượt, gắn cấp thuộc UC-08.2, 08.4 (QĐ-10); công thức chờ QĐ-07")
    s.del_row(5, 3, "So sánh phương án thuộc UC-08.3 (QĐ-10)")
    s.row(5, 4, [None, None, None, None, "Hệ thống đánh dấu dữ liệu thiếu, yêu cầu Tài chính bổ sung (CN-105), không tự "
                 "suy đoán; UC kết thúc, chưa có kết luận chính thức về chi phí."], "Thêm mã CN; khớp nhánh E1 trên AD")
    s.row(5, 5, [None, "1", "Chưa có phương án hoặc phạm vi công việc.", "không có phương án hoặc phạm vi công việc",
                 "Hệ thống không bắt đầu đánh giá; UC kết thúc (CN-103)."],
          "Bỏ kiểm tra quyền (mẫu FDS); ngân sách thuộc 08.2")
    rules = [
        ("CN-103", "PM xác định phương án cần đánh giá chi phí và lý do, dựa trên phương án bố trí và phạm vi công việc.",
         "Bước 1, 2; E2"),
        ("CN-104", "PM lượng hóa yếu tố tạo chi phí: nhân sự, số lượng, thời gian, mức độ tham gia.", "Bước 2, 3"),
        ("CN-105", "Tài chính cung cấp thông tin chi phí, gồm đơn giá.", "Bước 4; E1"),
        ("CN-106", "Tài chính tính chi phí dự toán, cập nhật dự báo khi có dữ liệu thực tế hoặc thay đổi; phân biệt hai "
         "loại.", "Bước 4, 5"),
        ("CN-107", "Tài chính tính lại phần chi phí bị ảnh hưởng khi thay đổi người, số lượng, thời gian, mức độ tham gia.",
         "A1"),
        ("QT-48", "Thay đổi người, số lượng, thời gian hoặc mức độ tham gia có thể làm thay đổi chi phí và phải được xem "
         "xét lại.", "Điều kiện rẽ nhánh A1"),
        ("QT-49", "Phải phân biệt dự toán (chi phí dự kiến) và dự báo (ước tính được cập nhật).", "Bước 5"),
        ("CN-108", "Đối chiếu chi phí dự kiến với ngân sách — thuộc UC-08.2.", "Đầu ra bước 7 (ngoài UC)"),
        ("CN-99, CN-112", "Locked Baseline thuộc V8; chuyển kết quả cho V8, V10 thuộc UC-08.4.", "Ngoài phạm vi UC"),
    ]
    for i, v in enumerate(rules, 1):
        s.row(6, i, list(v), "Đổi mã CN-V9/RB-V9/PCN-V9 sang mã Phần I; giữ quy tắc thuộc 08.1 (QĐ-10)")
    for r in range(10, 19):
        s.del_row(6, r, "Quy tắc thuộc 08.2–08.4 hoặc mã không có trong Phần I")
    s.del_par(17, "Thay đường dẫn Drive bằng hình trong bài")
    s.add_image(16, img(root, "II.2_AD", "AD_UC-08.1.png"), 16,
                "AD vẽ lại theo phạm vi 08.1; có nhánh E1, E2, A1; Tài chính có làn riêng (CN-105–107)")
    s.cell(7, 2, 2, "Association PM, Tài chính – UC-08.1; không có include/extend.", "Bỏ include")
    s.cell(7, 3, 2, "AD khớp bước 1 đến 7; A1 là nhánh trước bước 5.", "Theo D mới")
    s.cell(7, 4, 2, "Phương án, yếu tố chi phí, đơn giá, chi phí thực tế, dự toán, dự báo.", "Theo phạm vi 08.1")
    s.cell(7, 5, 2, "Đơn giá trước dự toán; dự báo cập nhật sau khi có chi phí thực tế hoặc thay đổi.", "Theo D mới")
    s.cell(7, 6, 2, "A1, E1, E2 đều là decision riêng.", "Theo D mới")
    s.cell(7, 7, 2, "Kết thúc sớm E1, E2; kết thúc chính sau bước 7.", "Theo D mới")
    # II.2+ lớp: giữ phạm vi cả vùng V9 cho II.3, đổi mã và khớp Hình II.3-5
    cls = "Khớp sơ đồ lớp II.3 (Hình II.3-5)"
    s.rename(range(8, 15), [
        ("CN-V9-11, 13, 14; RB-V9-07, 08", "CN-108; QT-51"), ("CN-V9-01 đến 05", "CN-103, CN-104"),
        ("CN-V9-03 đến 05", "CN-104"), ("CN-V9-09, 10, RB-V9-03", "CN-106, CN-107, QT-48"),
        ("CN-V9-09, 10", "CN-106, CN-107"), ("CN-V9-11 đến 14", "CN-108"), ("CN-V9-11, 12, RB-V9-04", "CN-108, QT-47"),
        ("CN-V9-11, 12", "CN-108"), ("CN-V9-13, 14", "CN-108"), ("CN-V9-16 đến 18", "CN-110"),
        ("CN-V9-16, RB-V9-06", "CN-110, QT-50"), ("CN-V9-19 đến 22", "CN-111"), ("CN-V9-08, QT-03", "CN-106, QT-49"),
        ("CN-V9-15, RB-V9-05", "CN-109"), ("CN-V9-01, RB-V9-02", "CN-103"), ("CN-V9-02, RB-V9-02", "CN-103"),
        ("CN-V9-01", "CN-103"), ("CN-V9-02", "CN-103"), ("CN-V9-06", "CN-105"), ("CN-V9-07", "CN-106"),
        ("CN-V9-08", "CN-106"), ("CN-V9-09", "CN-106"), ("CN-V9-12", "CN-108"), ("CN-V9-15", "CN-109"),
        ("RB-V9-02", "CN-103"), ("RB-V9-03", "QT-48"), ("RB-V9-04", "QT-47"), ("RB-V9-05", "CN-109"),
        ("RB-V9-06", "QT-50"), ("RB-V9-07, 08", "QT-51"), ("RB-V9-09, 10", "CN-97, CN-99"), ("QT-03", "QT-49"),
        ("PCN-V9-05, 04", "PCN-07, PCN-08"), ("PCN-V9-05", "PCN-07"),
    ], "Đổi mã riêng của bài sang mã Phần I")
    s.row(8, 2, [None, "Không (dùng chung)", "Phạm vi công việc lấy từ DuAn, GiaiDoanDuAn và nhu cầu của phương án "
                 "(Hình II.3-2); không tạo lớp riêng."], cls)
    s.row(8, 3, ["Chi tiết bố trí (dòng phương án)", "Có (dùng chung)", "Vai trò, tỷ lệ tham gia, thời gian của từng dòng "
                 "phương án (CN-104); dùng lớp ChiTietBoTri của V6 (Hình II.3-4)."], "Dòng phương án dùng ChiTietBoTri")
    s.row(8, 13, [None, "Chưa (chờ QĐ-19)", "Ngưỡng 10% giữ ở dạng quy tắc QT-51; cấp xử lý ghi ở thuộc tính capXuLy của "
                  "DanhGiaChiPhi."], "QĐ-19 chưa chốt")
    s.row(8, 14, [None, "Không", "Là actor; người thực hiện được ghi theo PCN-07, không cần lớp miền riêng."],
          "Bỏ NguoiDung (thống nhất II.3)")
    s.cell(8, 16, 2, "Thuộc V8 (CN-97, CN-99).", "Đổi mã")
    s.row(9, 1, [None, "ChiTietBoTri", "Lớp nắm vai trò, tỷ lệ, thời gian; chi phí tính từ đơn giá."], cls)
    s.row(9, 9, ["Xác định cấp xử lý theo ngưỡng", "DanhGiaChiPhi", "Ngưỡng 10% là quy tắc QT-51 (chờ QĐ-19)."], cls)
    s.del_row(10, 2, "CongViec không là lớp riêng (Hình II.3-2)")
    s.row(10, 3, ["ChiTietBoTri", "Dòng phương án: vai trò, tỷ lệ tham gia, thời gian (lớp của V6)", None], cls)
    s.del_row(10, 12, "Ngưỡng giữ ở dạng quy tắc (QĐ-19)")
    s.del_row(10, 15, "Bỏ NguoiDung")
    s.del_row(11, 2, "CongViec không là lớp riêng")
    s.row(11, 3, ["ChiTietBoTri", "vaiTroDuocGan, tyLeThamGia, tuNgay, denNgay", "Lớp của V6 (Hình II.3-4); V9 dùng để "
                  "tính chi phí theo đơn giá. Đơn vị mức tham gia chưa chốt (Q-03)."], cls)
    s.row(11, 9, [None, "thoiDiem, chiPhiDuKienTaiThoiDiem, nganSachConLaiTaiThoiDiem, chenhLech, tyLeVuot, "
                  "trangThaiNganSach, capXuLy",
                  "Lưu giá trị chốt tại thời điểm đánh giá để kết quả không đổi khi đơn giá hoặc ngân sách thay đổi sau "
                  "đó. tyLeVuot = chenhLech / nganSachConLai khi vượt [Chờ xác nhận QĐ-07]; chưa tính khi ngân sách còn "
                  "lại ≤ 0. trangThaiNganSach: TrongNganSach, VuotNganSach. capXuLy: KhongCan, QuanLyDanhMuc, CEO (gắn "
                  "cấp xử lý, chưa phải phê duyệt)."], cls + "; công thức chờ QĐ-07")
    s.del_row(11, 12, "Ngưỡng giữ ở dạng quy tắc (QĐ-19)")
    s.del_row(11, 15, "Bỏ NguoiDung")
    s.row(12, 1, ["ChiTietBoTri", None, None], cls)
    s.row(12, 7, [None, "kiemTraTienDieuKien(), danhDauThieuDuLieu(), doiChieuNganSach(), xacDinhTrangThai(), "
                  "xacDinhCapXuLy()", None], "Gắn cấp xử lý, không phải phê duyệt")
    s.del_row(12, 8, "Ngưỡng giữ ở dạng quy tắc (QĐ-19)")
    s.del_row(13, 1, "CongViec không là lớp riêng")
    s.row(13, 2, [None, None, "ChiTietBoTri", "Dòng phương án không tồn tại khi thiếu phương án."], cls)
    s.row(13, 3, ["ChiTietBoTri", None, None, "Mỗi dòng phương án áp dụng một đơn giá."], cls)
    s.row(13, 11, ["DuAn", None, "NganSach", "Ngân sách được duyệt cho dự án (QT-47)."], cls)
    s.del_row(13, 15, "Ngưỡng giữ ở dạng quy tắc (QĐ-19)")
    for r in range(19, 24):
        s.del_row(13, r, "Bỏ NguoiDung")
    s.del_row(14, 1, "CongViec không là lớp riêng")
    s.row(14, 2, ["PhuongAnBoTri – ChiTietBoTri", None, None], cls)
    s.row(14, 3, ["ChiTietBoTri – DonGia", "0..* – 1", "Mỗi dòng phương án áp dụng đúng một đơn giá."], cls)
    s.row(14, 11, ["DuAn – NganSach", "1 – 0..*", "Ngân sách được duyệt cho dự án."], cls)
    s.cell_replace(14, 15, 2, "(A3)", "(UC-08.3)", "A3 cũ đã chuyển sang FDS 08.3")
    for r in range(18, 23):
        s.del_row(14, r, "Bỏ NguoiDung")
    s.del_par(32, "Ghi chú tải file PDF, không thuộc nội dung báo cáo")
    s.image(35, img(root, "II.3", "II3-5_Chi_phi_ngan_sach.png"), 16,
            "Sơ đồ lớp theo mô hình thống nhất (Hình II.3-5, nguồn draw.io)")


@job("P1", "[PTTKHT] I - PHÂN TÍCH YÊU CẦU FINAL.docx")
def p1(s, root):
    qd01 = ("QĐ-01: CN-37, CN-43 (V4) giao PMO/Quản lý danh mục phê duyệt miễn trừ và điều chỉnh xếp hạng, shortlist; "
            "bảng vai trò và bảng V4 chưa ghi")
    s.cell_replace(0, 5, 1, "Xác nhận kết quả đánh giá năng lực ở cấp cuối khi có tranh chấp.",
                   "Xác nhận kết quả đánh giá năng lực ở cấp cuối khi có tranh chấp. Phê duyệt tiêu chí tạm cho kỹ năng "
                   "chưa có tiêu chí. Phê duyệt miễn trừ điều kiện bắt buộc và điều chỉnh xếp hạng, shortlist của RM.",
                   qd01 + "; CN-19 (V3) phê duyệt tiêu chí tạm")
    s.cell(0, 5, 2, "V3, V4, V5, V7, V8, V9", qd01)
    s.cell(4, 1, 1, "RM; PMO/Quản lý danh mục phê duyệt miễn trừ điều kiện bắt buộc và điều chỉnh xếp hạng, shortlist "
           "(CN-37, CN-43)", qd01)
    s.cell_replace(13, 35, 1, " (Nguồn V6 ghi nhận là )", "", "Bỏ cụm chú thích còn dở, không có nội dung")


def main(src, root, only):
    out = os.path.join(root, "bai_goc_da_sua")
    os.makedirs(out, exist_ok=True)
    logs = []
    for code, (fname, fn) in JOBS.items():
        if only and code not in only:
            continue
        s = Sua(os.path.join(src, fname), code)
        fn(s, root)
        base, ext = os.path.splitext(fname)
        log = s.apply(os.path.join(out, f"{base.strip()} (đã sửa){ext}"))
        logs.append(log_md(f"{code} — {fname}", log))
    with open(os.path.join(root, "_cong_cu", f"nhat_ky_{'_'.join(only) or 'tat_ca'}.md"), "w",
              encoding="utf-8") as f:
        f.write("\n".join(logs))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3:])
