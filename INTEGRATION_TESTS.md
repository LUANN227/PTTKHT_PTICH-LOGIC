# Integration acceptance tests — chưa chạy Claude

Chạy mỗi trường hợp với input giống nhau để kiểm tra khi bật 9 skill; so sánh với baseline nếu cần. Quan sát skill chính, có tràn phạm vi không, tài liệu có đọc được không và có tự thêm metadata vô ích không.

| ID | Prompt ngắn | Skill chính mong đợi | Điều kiện đạt |
|---|---|---|---|
| I01 | 'Giải thích nên phân tích vấn đề trước khi chọn giải pháp như thế nào' | Coach | Giải thích theo bối cảnh, không đòi đủ 9 tài liệu |
| I02 | 'Viết acceptance criteria cho yêu cầu đăng ký nghỉ phép đã cho' | Requirements | Tiêu chí quan sát được, không tự bịa policy |
| I03 | 'Review use case diagram có actor sai ranh giới' | UML | Bắt lỗi UML và nghiệp vụ riêng |
| I04 | 'Vẽ BPMN AS-IS quy trình duyệt, có 2 pool' | BPMN | Phân biệt message vs sequence flows |
| I05 | 'Viết lại BRD nhưng giữ ID và baseline' | Documentation | Không đổi nghĩa, ID, quyết định |
| I06 | 'Nguồn A và B mâu thuẫn về phiên bản tiêu chuẩn' | Research | Kiểm tra scope/date; không bịa phiên bản |
| I07 | 'Build or buy phần mềm; cần so sánh chi phí' | Solution | Có cả phương án không xây, phân biệt ước lượng |
| I08 | 'Viết tổng quan nghiên cứu theo chủ đề' | Academic | Tổng hợp chứ không tóm tắt hàng loạt |
| I09 | 'Ra bài tập khai thác yêu cầu để tôi trả lời' | Practice | Không cho đáp án ngay nếu không yêu cầu |
| I10 | 'Chỉ sửa lỗi chính tả đoạn này' | Documentation hoặc không cần skill | Không áp đặt workflow, không sửa nghiệp vụ |
| I11 | 'Kiểm tra tuyên bố vendor rồi đề xuất giải pháp' | Solution + Research | Không khẳng định vendor khi chưa xác minh |
| I12 | 'Phân tích BPMN, rồi chuyển thành yêu cầu' | BPMN + Requirements | Rõ phần quy trình và hành vi hệ thống |
| I13 | 'Tôi có hai file baseline không khớp, hãy chỉnh' | Skill theo đầu ra | Nêu mâu thuẫn, không tự ý thay nguồn thẩm quyền |
| I14 | 'Tóm tắt đoạn tiếng Anh giao tiếp thường ngày' | Không skill BA | Không tự kích hoạt BA workflow |
| I15 | 'Đánh giá độ tốt của hệ thống 9 skill này' | Practice | Không tuyên bố đã test nếu chưa chạy |

Trạng thái: **test plan only**, chưa có logs, passes hay đánh giá thực nghiệm.
