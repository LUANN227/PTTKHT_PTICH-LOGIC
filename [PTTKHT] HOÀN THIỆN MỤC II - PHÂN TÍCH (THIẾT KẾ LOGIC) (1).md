## **II.2 — Mô hình hóa chức năng \+ II.2+ — Đề xuất lớp cho II.3**

### 1\. Thông tin phân công

| Nội dung | Thông tin |
| ----- | ----- |
| Thành viên | ... |
| Vùng nghiệp vụ | V... |
| UC trọng tâm | UC-... |
| Tên UC | ... |

# 2\. Use Case Diagram chi tiết

## 2.1. Xác định UC

| Nội dung | Thông tin |
| ----- | ----- |
| Mã UC | UC-... |
| Tên UC | ... |
| Actor chính | ... |
| Actor phụ | ... |
| UC liên quan | ... |

## 2.2. Quan hệ UC

Chỉ ghi các quan hệ có căn cứ từ nghiệp vụ và mô hình hóa thực sự cần thiết.

| UC nguồn | Quan hệ | UC đích | Giải thích |
| ----- | ----- | ----- | ----- |
| ... | \<\<include\>\> / \<\<extend\>\> / ... | ... | ... |

> Không tự thêm include / extend chỉ để mô tả trình tự nghiệp vụ. Nếu không có quan hệ phù hợp thì ghi Không có.

## 2.3. Use Case Diagram

Vẽ Use Case Diagram chi tiết cho UC được giao, thể hiện:

* Actor  
* Use Case  
* Association  
* \<\<include\>\> / \<\<extend\>\> nếu thực sự có  
* Ranh giới hệ thống

# 3\. Use Case Description / FDS chi tiết

## 3.1. Thông tin chung

| Trường | Nội dung |
| ----- | ----- |
| Mã UC | UC-... |
| Tên UC | ... |
| Mục tiêu | ... |
| Actor chính | ... |
| Actor phụ | ... |
| Trigger | ... |
| Tiền điều kiện | ... |
| Hậu điều kiện | ... |

## 3.2. Luồng chính

| Bước | Actor/System | Mô tả |
| ----- | ----- | ----- |
| 1 | Actor | ... |
| 2 | System | ... |
| 3 | Actor | ... |
| ... | ... | ... |

Nguyên tắc: mô tả luồng nghiệp vụ, không biến thành hướng dẫn thao tác giao diện.

## 3.3. Luồng thay thế / ngoại lệ

| Mã | Tại bước | Điều kiện | Xử lý |
| ----- | ----- | ----- | ----- |
| A1 | Bước ... | ... | ... |
| E1 | Bước ... | ... | ... |

* A: Alternative Flow  
* E: Exceptional Flow

Không tạo flow chỉ vì muốn “đủ bảng”; chỉ đưa những nhánh có căn cứ từ nghiệp vụ.

## 3.4. Business Rules / yêu cầu liên quan

| ID | Nội dung | Vai trò trong UC |
| ----- | ----- | ----- |
| CN-... | ... | ... |
| RB-... | ... | ... |

Chỉ dẫn các CN/RB thực sự tác động đến UC, không copy toàn bộ CN của V.

# 4\. Activity Diagram

## 4.1. Xác định thành phần Activity Diagram

Xác định trước:

* Điểm bắt đầu  
* Actor/Swimlane nếu cần  
* Các Activity/Action  
* Decision/Merge  
* Fork/Join nếu có  
* Điều kiện các nhánh  
* Điểm kết thúc

## 4.2. Activity Diagram

Vẽ Activity Diagram tương ứng với Use Case Description.

AD phải thể hiện được:

* Luồng chính  
* Luồng thay thế  
* Luồng ngoại lệ  
* Các điều kiện rẽ nhánh tương ứng với Description.

# 5\. ĐỐI CHIẾU UC — UCD — AD

| Kiểm tra | Kết quả |
| ----- | ----- |
| Actor trong UCD có trên Use Case Diagram | ✓ / ✗ |
| Quan hệ trong UCD có trên Use Case Diagram | ✓ / ✗ |
| Mỗi Activity/Action có sự kiện tương ứng trong UCD | ✓ / ✗ |
| Các Object trên AD xuất hiện trong UCD | ✓ / ✗ |
| Thứ tự sự kiện trong UCD khớp thứ tự hoạt động AD | ✓ / ✗ |
| Các Alternative/Exceptional Flow trong UCD được thể hiện trên AD | ✓ / ✗ |
| Điểm bắt đầu/kết thúc của UCD và AD nhất quán | ✓ / ✗ |

# **II.2+ — ĐỀ XUẤT LỚP CHO II.3**

## 6\. Phân tích văn bản để xác định lớp

### 6.1. Danh từ / đối tượng nghiệp vụ

| Danh từ / cụm danh từ | Có phải lớp? | Giải thích |
| ----- | ----- | ----- |
| ... | Có/Không | ... |

### 6.2. Động từ / hành vi nghiệp vụ

| Hành vi | Lớp thực hiện | Giải thích |
| ----- | ----- | ----- |
| ... | ... | ... |

## 7\. Xác định lớp miền

| Lớp | Ý nghĩa nghiệp vụ | Nguồn xác định |
| ----- | ----- | ----- |
| ... | ... | UC/CN/RB/... |

## 8\. Xác định thuộc tính

| Lớp | Thuộc tính | Ý nghĩa |
| ----- | ----- | ----- |
| ... | ... | ... |

## 9\. Xác định thao tác

| Lớp | Operation | Ý nghĩa |
| ----- | ----- | ----- |
| ... | ... | ... |

## 10\. Xác định quan hệ giữa các lớp

| Lớp A | Quan hệ | Lớp B | Giải thích |
| ----- | ----- | ----- | ----- |
| ... | Association/... | ... | ... |

## 11\. Xác định multiplicity

| Quan hệ | Multiplicity | Căn cứ nghiệp vụ |
| ----- | ----- | ----- |
| ... | 1..\* / 0..1 / ... | ... |

## 12\. Domain/Class Diagram đề xuất

Vẽ Domain/Class Diagram trong phạm vi UC được giao, làm cơ sở cho phần mô hình hóa cấu trúc tĩnh II.3.

