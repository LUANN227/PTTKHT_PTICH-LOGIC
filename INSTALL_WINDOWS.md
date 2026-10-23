# Cài trên Windows

## Claude Code với repository dự án
1. Giải nén ZIP tích hợp vào **thư mục gốc của repo**, không vào một thư mục con tên `ba-skills-integrated-v1.0`.
2. Xác nhận `<repo>\.claude\skills\ba-coach-workflow\SKILL.md` và tám thư mục kỹ năng còn lại.
3. Xác nhận `<repo>\CLAUDE.md`; nếu đã có `CLAUDE.md`, **không ghi đè**: ghép các quy tắc phối hợp có liên quan, giữ quy ước cũ.
4. Mở Claude Code tại root repo. Yêu cầu ví dụ: `Hãy giúp tôi phân tích stakeholder và viết acceptance criteria cho một chức năng đăng ký nghỉ phép.`
5. Kiểm tra đầu ra; việc nhận diện và phối hợp còn phụ thuộc phiên bản và cấu hình Claude Code.

## Claude.ai
Từ `claude-ai-individual-zips/`, sử dụng lần lượt từng file ZIP tương ứng trong phần custom Skills tại Settings > Features khi tài khoản hỗ trợ. Chín ZIP tách biệt **không có** một bộ router trung tâm chạy tự động. Hướng dẫn chung `INTEGRATION_GUIDE.md` có thể được đưa vào hướng dẫn dự án khi phù hợp.

## Tránh xung đột
Nếu máy đã có một skill cùng tên, sao lưu phiên bản cũ; đừng giải nén đè một cách mù quáng. Không bỏ toàn bộ 9 skill trong một thư mục chứa duy nhất SKILL.md.

Nguồn kiến trúc: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
