# Hướng dẫn phối hợp 9 skill (v1.0)

## Mục tiêu
Một gói triển khai cho Claude Code, giữ nguyên khả năng hoạt động độc lập và tham chiếu của từng skill. Tài liệu phối hợp này là **quy ước đề xuất**, không phải tiêu chuẩn IIBA/OMG/IEEE hay một tính năng bảo đảm của Claude.

## Nguyên tắc điều phối
**Chọn một skill chính theo sản phẩm đầu ra; gọi skill hỗ trợ khi có lý do chuyên môn.** Claude không cần nạp toàn bộ chín skill. Khi các skill có chỉ dẫn chồng chéo, ưu tiên thông tin dự án do người dùng cấp, tài liệu đã phê duyệt, yêu cầu hiện tại và ranh giới chuyên môn; không tự sửa dữ kiện đã chốt.

| Nếu yêu cầu là... | Skill chính | Hỗ trợ khi cần |
|---|---|---|
| Tôi phải bắt đầu BA dự án như thế nào? | BA Coach | Requirements |
| Phân tích/viết acceptance criteria cho tính năng | Requirements | BA Documentation |
| Vẽ use case hoặc sequence | UML | Requirements |
| Vẽ AS-IS/TO-BE có pool, lane, gateway | BPMN | Requirements |
| Sửa BRD dài và khó hiểu, giữ nguyên ý | BA Documentation | Requirements (chỉ khi nghĩa không rõ) |
| Kiểm tra lời tuyên bố của nhà cung cấp | Research & Evidence | Solution & Market (nếu cần chọn phương án) |
| Chọn phần mềm A/B hay tự xây | Solution & Market | Research & Evidence; Requirements |
| Viết bài tổng quan tài liệu học thuật | Academic Research | Research & Evidence |
| Luyện khai thác yêu cầu và nhận góp ý | Practice & Evaluation | Requirements |
| Kiểm thử chất lượng 9 skill | Practice & Evaluation | Các skill bị kiểm thử, không mặc định kích hoạt tất cả |

## Luật giải quyết vùng giao nhau
- **Requirements vs Documentation:** Nếu câu hỏi là *điều gì đúng/cần thiết* -> Requirements; nếu là *diễn đạt thế nào* -> Documentation. Khi vừa phân tích vừa viết, hoàn tất lập luận/yêu cầu trước rồi mới biên tập câu chữ.
- **BPMN vs UML Activity:** Quy trình xuyên vai trò/tổ chức và message flow -> BPMN; hành vi nội bộ của ca sử dụng/hệ thống cần diễn đạt bằng UML -> UML Activity. Không ép vẽ song song.
- **Research vs Market:** Nguồn có đáng tin? -> Research. Nên chọn phương án nào? -> Market, và chuyển các dữ kiện đáng ngờ sang Research.
- **Academic vs Documentation:** Học thuật ưu tiên yêu cầu phương pháp, tổng quan tài liệu và trích dẫn; Documentation dành cho tài liệu BA và truyền đạt tới stakeholder.
- **Coach vs Practice:** Coach giải thích phương pháp trong công việc; Practice tạo bài tập, phản hồi và chương trình đánh giá. Không bắt người dùng làm quiz nếu họ muốn Execute.

## Các ca minh họa phối hợp
**A. 'Sửa Use Case Specification này cho rõ, không đổi mã':** Documentation là chính; đọc tài liệu gốc và baseline. Requirements chỉ hỗ trợ khi có mâu thuẫn nghiệp vụ. Giữ ID, luồng chính/phụ, điều kiện, tên actor và trích dẫn.

**B. 'Phân tích quy trình duyệt đề nghị mua hàng và đề xuất tự động hóa':** BPMN là chính để mô hình người, máy, ngoại lệ và trách nhiệm. Requirements chỉ bổ sung nếu cần chuyển TO-BE thành đặc tả tính năng; Coach không tự chèn bài giảng.

**C. 'Chọn hệ thống CRM trên thị trường theo 5 tiêu chí':** Solution & Market là chính. Research xác thực thông tin giá/khả năng tích hợp, đánh dấu chưa xác minh thay vì tự tin suy đoán. Không đòi tạo BRD trước.

**D. 'Giúp tôi học cách tìm nguyên nhân gốc':** Coach chính; Practice hỗ trợ nếu người dùng muốn bài tập hoặc tự kiểm tra.

## Quy tắc cài đặt
- **Claude Code (khuyên dùng cho cấu hình tích hợp):** Giải nén toàn gói vào thư mục gốc của repository, để `.claude/skills/<ten-skill>/SKILL.md` và `CLAUDE.md` cùng cấp với `.claude`. Claude Code sẽ tìm skill theo cơ chế mô tả của Anthropic; `CLAUDE.md` là quy ước điều phối dự án đề xuất.
- **Cài đặt người dùng trên Claude Code:** Copy chín thư mục trong `.claude/skills/` tới `%USERPROFILE%\.claude\skills\` (Windows). Hướng dẫn phối hợp trong `CLAUDE.md` chỉ được dùng nếu đặt ở một vị trí Claude Code có nạp nó; không cần sao chép nguyên project root vào user folder.
- **Claude.ai:** Không dùng toàn bộ ZIP đa thư mục như thể nó là một skill. Tải lần lượt chín ZIP đơn ở `claude-ai-individual-zips/`; hiệu lực phối hợp từ `CLAUDE.md` trong gói này không tự áp dụng trên claude.ai. Bạn có thể đưa quy tắc phối hợp vào hướng dẫn dự án nếu phù hợp; cần kiểm tra thực tế.

## Hạn chế
Kiểm tra tĩnh không thể chứng minh activation đúng, tính ổn định của phối hợp hay chất lượng đầu ra. Chín skill vẫn có nhiều nội dung nguyên bản chồng lấn; phiên bản này chỉnh lại metadata để tăng phân biệt, không viết lại toàn bộ kỹ thuật chuyên sâu. Chưa chạy thử trên tài khoản Claude hoặc kiểm thử thực nghiệm end-to-end.
