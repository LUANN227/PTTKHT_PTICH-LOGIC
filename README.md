# BA Skills Integrated v1.0 — 9 Agent Skills

**Phiên bản tích hợp:** 1.0, từ **9 skill gốc v0.1.0**. Không phải bản chứng nhận chất lượng hoặc đã chạy thử Claude.

## Cách dùng
- Claude Code: giải nén **nội dung** ZIP vào root repository; dùng 9 thư mục `.claude/skills/` và đọc `CLAUDE.md`.
- Claude.ai: sử dụng **từng ZIP riêng phiên bản tích hợp** trong `claude-ai-individual-zips/`; tham khảo `INTEGRATION_GUIDE.md` nếu cần quy tắc phối hợp trong project instructions.

Xem `INSTALL_WINDOWS.md`, `INTEGRATION_GUIDE.md` và `VALIDATION_REPORT.md`.

## Thay đổi so với các gói riêng
- Giữ nguyên nội dung chuyên môn, references, examples và tests của từng skill gốc.
- Chỉnh phần YAML `description` cho 9 skill để nhận diện phạm vi và trường hợp không kích hoạt rõ hơn.
- Thêm định tuyến ở `CLAUDE.md`, ma trận vùng chồng chéo, hướng dẫn cài Windows và các tình huống kiểm thử tích hợp.
- Không thay đổi logic nghiên cứu/đặc tả trong phần thân SKILL.md, không tự tuyên bố đã chạy đánh giá thực nghiệm.

## Dữ liệu dự án
Gói **không chứa** file, quyết định hay baseline riêng của Lạc Việt Consulting. Khi dùng phải cung cấp/tải lên nguồn tương ứng, không để skill tự đoán nghiệp vụ.
