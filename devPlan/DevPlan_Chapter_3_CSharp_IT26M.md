# KẾ HOẠCH BÀI GIẢNG VÀ PHÁT TRIỂN SLIDE BÀI GIẢNG ĐẠI HỌC
## HỌC PHẦN: KỸ THUẬT LẬP TRÌNH / LẬP TRÌNH C# & .NET
### CHƯƠNG 3: INTRODUCTION TO C# APP PROGRAMMING (LẬP TRÌNH ỨNG DỤNG C# CĂN BẢN)
**Đối tượng:** Lớp IT26M (Khóa 2026 -- Khoa Công nghệ Thông tin)  
**Thời lượng:** 01 buổi (03 tiết = 150 phút, kết hợp lý thuyết sư phạm và thực hành phòng máy)  
**Tài liệu tham khảo chính:** Textbook *Visual C# How to Program (6th Edition)* (Deitel & Deitel) -- Chapter 3: *Introduction to C# App Programming* (Trang 105--145)  
**Định dạng sản phẩm:** Slide LaTeX Beamer $\to$ Biên dịch PDF chuẩn học thuật quốc tế (XeLaTeX, font Arial/Consolas, tỷ lệ 16:9)  
**Thư mục lưu trữ:** `Slides_CShape/` và `Slides/slideChapter_03.pdf`

---

## I. MỤC TIÊU BÀI HỌC (COURSE LEARNING OUTCOMES - CLOs)

Kết thúc buổi học 3 tiết này, sinh viên lớp IT26M đạt được 5 chuẩn đầu ra:

| Mã CLO | Mô tả chuẩn đầu ra môn học | Thang đo Bloom |
| :--- | :--- | :--- |
| **CLO 3.1** | Giải thích được kiến trúc một ứng dụng Console C#, vai trò của phương thức khởi nhập `static void Main()`, chỉ thị `using System;`, khối lệnh `{}` và các quy ước định danh PascalCase / camelCase. | Level 2 (Understand) |
| **CLO 3.2** | Vận dụng thành thạo các phương thức xuất dữ liệu (`Console.Write`, `Console.WriteLine`), bảng ký tự thoát (Escape Sequences: `\n`, `\t`, `\\`, `\"`) và kỹ thuật Nội suy chuỗi hiện đại C# 6 (String Interpolation `$"{...}"`). | Level 3 (Apply) |
| **CLO 3.3** | Khai báo và sử dụng biến số nguyên `int`, chuyển đổi kiểu dữ liệu bằng `int.Parse()`, thấu hiểu mô hình ô nhớ RAM (địa chỉ, tên, kiểu, kích thước) và phân biệt cơ chế đọc không phá hủy (non-destructive) vs ghi đè phá hủy (destructive). | Level 3 (Apply) |
| **CLO 3.4** | Làm chủ các toán tử số học (`+`, `-`, `*`, `/`, `%`), phân biệt phép chia số nguyên (truncation) và phép chia lấy dư, áp dụng quy tắc thứ tự ưu tiên toán tử (precedence rules) để chuyển đổi chuẩn xác biểu thức đại số sang C#. | Level 3 (Apply) |
| **CLO 3.5** | Phân tích và xây dựng cấu trúc rẽ nhánh ra quyết định với câu lệnh `if`, kết hợp bảng toán tử quan hệ (`<`, `<=`, `>`, `>=`) và bình đẳng (`==`, `!=`), phòng tránh lỗi cú pháp dấu chấm phẩy `;` sau điều kiện. | Level 4 (Analyze / Create) |

---

## II. MA TRẬN PHÂN BỔ THỜI GIAN & TIẾN TRÌNH DẠY HỌC (3 TIẾT = 150 PHÚT)

```text
========================================================================================
TIẾT 1 (50'): CẤU TRÚC CONSOLE APP, WELCOME1 ĐẾN WELCOME4, INTELLISENSE & ERROR LIST
- 05': Khởi động buổi học, công bố 5 CLOs (CLO 3.1 - 3.5), kết nối từ GUI (Chương 2) sang Mã nguồn (Chương 3)
- 15': Kiến trúc ứng dụng Console: Phân tích chi tiết Welcome1.cs (using, class, Main, WriteLine)
- 10': Thao tác Visual Studio: Tạo Console Application, IntelliSense, Parameter Info, Biên dịch & Chạy Ctrl+F5
- 10': Xử lý lỗi biên dịch: Syntax Errors, Error List window, giải mã thông báo lỗi
- 10': [THỰC HÀNH 1 & CHECKPOINT 1] Gõ mã Welcome1, Welcome2 (Console.Write), trắc nghiệm củng cố Tiết 1
----------------------------------------------------------------------------------------
TIẾT 2 (50'): ESCAPE SEQUENCES, STRING INTERPOLATION, BIẾN, BỘ NHỚ & PHÉP TOÁN SỐ HỌC
- 10': Ký tự thoát Escape Sequences (Welcome3.cs, bảng \n, \t, \r, \\, \") & Nội suy chuỗi C# 6 (Welcome4.cs)
- 15': Ứng dụng tính tổng Addition.cs: Khai báo biến int, nhập bàn phím Console.ReadLine(), int.Parse()
- 10': Bản chất Bộ nhớ máy tính: Ô nhớ RAM, tên biến, kiểu, đọc không phá hủy vs ghi đè phá hủy
- 10': Các toán tử số học (+, -, *, /, %), phép chia nguyên (truncation), toán tử chia dư (%) và thứ tự ưu tiên
- 05': [THỰC HÀNH 2 & CHECKPOINT 2] Case Study đa thức bậc 2 y = ax^2 + bx + c & Trắc nghiệm Tiết 2
----------------------------------------------------------------------------------------
TIẾT 3 (50'): CÂU LỆNH IF, TOÁN TỬ SO SÁNH, CASE STUDY COMPARISON & ĐỒ ÁN THỰC HÀNH
- 15': Cấu trúc điều khiển rẽ nhánh: Câu lệnh if, toán tử quan hệ (<, <=, >, >=) và bình đẳng (==, !=)
- 10': Case Study Comparison.cs: Cấu trúc so sánh 2 số nguyên, phân biệt sống còn giữa '=' và '=='
- 10': Lỗi kinh điển: Dấu chấm phẩy ';' sau điều kiện if, khối lệnh { } khi có nhiều câu lệnh
- 10': [THỰC HÀNH 3] Hands-on Lab: Lập trình hoàn chỉnh ứng dụng Comparison, kiểm thử các bộ test
- 05': Tổng kết checklist chuẩn đầu ra, giới thiệu các bài tập lớn (Shapes, Table, Car-Pool) & dặn dò
========================================================================================
```

---

## III. BẢN ĐỒ HÌNH ẢNH & TÀI NGUYÊN TRÍCH XUẤT TỪ SÁCH GIÁO KHOA

Tất cả các hình ảnh được trích xuất và lưu trữ tại `Slides_CShape/images/`:

| Mã file hình ảnh | Trang SGK | Tên hình trong SGK | Nội dung & Vai trò trong bài giảng |
| :--- | :---: | :--- | :--- |
| `fig3_01_welcome1_app.png` | Trang 3 (107) | Fig. 3.1: Welcome1.cs | Chương trình đầu tiên hiển thị dòng chữ trên màn hình console |
| `fig3_02_keywords_table.png` | Trang 6 (110) | Fig. 3.2: Keywords table | Bảng 77 từ khóa chuẩn và các từ khóa ngữ cảnh trong C# |
| `fig3_03_new_console_project.png` | Trang 9 (113) | Fig. 3.3: New Project dialog | Hộp thoại New Project, chọn mẫu Console Application |
| `fig3_04_ide_console_app.png` | Trang 9 (113) | Fig. 3.4: Open console app in IDE | Giao diện IDE soạn thảo mã nguồn và Solution Explorer |
| `fig3_05_intellisense_typing.png` | Trang 10 (114)| Fig. 3.5: IntelliSense typing | Danh sách gợi ý tự động IntelliSense khi gõ từ "Con" |
| `fig3_06_intellisense_members.png`| Trang 11 (115)| Fig. 3.6: IntelliSense members| Danh sách thành viên (methods, properties) của lớp Console |
| `fig3_07_parameter_info.png` | Trang 12 (116)| Fig. 3.7: Parameter Info | Cửa sổ hướng dẫn tham số của phương thức Console.WriteLine |
| `fig3_08_executing_welcome1.png` | Trang 12 (116)| Fig. 3.8: Executing Welcome1 | Cửa sổ Command Prompt hiển thị kết quả chạy Welcome1 |
| `fig3_09_syntax_error_ide.png` | Trang 13 (117)| Fig. 3.9: Syntax error IDE | Đường gợn sóng đỏ báo lỗi cú pháp và cửa sổ Error List |
| `fig3_10_welcome2_app.png` | Trang 14 (118)| Fig. 3.10: Welcome2.cs | Xuất một dòng văn bản bằng nhiều lệnh Console.Write |
| `fig3_11_welcome3_app.png` | Trang 15 (119)| Fig. 3.11: Welcome3.cs | Xuất nhiều dòng văn bản bằng một lệnh với ký tự thoát \n |
| `fig3_12_escape_sequences_table.png`| Trang 16 (120)| Fig. 3.12: Escape sequences | Bảng tra cứu ký tự thoát: \n, \t, \r, \\, \" |
| `fig3_13_welcome4_interpolation.png`| Trang 16 (120)| Fig. 3.13: Welcome4.cs | Nội suy chuỗi C# 6 (String Interpolation $"...") |
| `fig3_14_addition_part1.png` | Trang 17 (121)| Fig. 3.14: Addition.cs Part 1 | Khai báo biến, nhập liệu từ bàn phím và ép kiểu int.Parse |
| `fig3_14_addition_part2.png` | Trang 18 (122)| Fig. 3.14: Addition.cs Part 2 | Tính tổng hai số, hiển thị kết quả và màn hình thực thi |
| `fig3_15_memory_number1.png` | Trang 21 (125)| Fig. 3.15: Memory number1 | Ô nhớ RAM sau khi đọc giá trị cho biến number1 (45) |
| `fig3_16_memory_number2.png` | Trang 21 (125)| Fig. 3.16: Memory number2 | Các ô nhớ RAM sau khi đọc giá trị cho biến number2 (72) |
| `fig3_17_memory_sum.png` | Trang 22 (126)| Fig. 3.17: Memory sum | Ô nhớ sum sau khi tính và lưu kết quả (117) |
| `fig3_18_arithmetic_operators.png`| Trang 22 (126)| Fig. 3.18: Arithmetic operators | Bảng toán tử số học: +, -, *, /, % |
| `fig3_19_operator_precedence.png` | Trang 23 (127)| Fig. 3.19: Operator precedence | Bảng thứ tự ưu tiên của các toán tử số học |
| `fig3_20_polynomial_evaluation.png`| Trang 25 (129)| Fig. 3.20: Polynomial eval | Sơ đồ đánh giá đa thức bậc hai ax^2 + bx + c từng bước |
| `fig3_21_relational_operators.png`| Trang 26 (130)| Fig. 3.21: Relational operators| Bảng toán tử so sánh quan hệ (<, <=, >, >=) và bình đẳng (==, !=)|
| `fig3_22_comparison_output.png` | Trang 28 (132)| Fig. 3.22: Comparison output | Kết quả thực thi chương trình so sánh hai số nguyên |
| `fig3_23_precedence_summary.png` | Trang 30 (134)| Fig. 3.23: Precedence summary | Bảng tổng kết thứ tự ưu tiên và kết hợp của tất cả toán tử |

---

## IV. CẤU TRÚC CHI TIẾT 45 SLIDE BÀI GIẢNG BEAMER

```text
SLIDE 01: [BÌA] Kỹ thuật Lập trình C# & .NET - Chương 3: Lập trình Ứng dụng C# Căn bản
SLIDE 02: [CLOs] 5 Chuẩn đầu ra bài học (Course Learning Outcomes) & Thang đo Bloom
SLIDE 03: [AGENDA] Lộ trình bài học 3 tiết tích hợp lý thuyết & thực hành phòng máy
SLIDE 04: [KIẾN TRÚC] Khái niệm Ứng dụng Console (Console Application) vs GUI
SLIDE 05: [CODE STUDY 1] Ứng dụng đầu tiên: Welcome1.cs (Hình 3.1)
SLIDE 06: [CÚ PHÁP] Chú thích (Comments //, /* */) & Chỉ thị using System
SLIDE 07: [ĐỊNH DANH] Khai báo lớp (class), Quy tắc PascalCase & Bảng từ khóa C# (Hình 3.2)
SLIDE 08: [HÀM MAIN] Điểm khởi nhập static void Main(), Cặp ngoặc nhọn {} & Khối lệnh
SLIDE 09: [XUẤT DỮ LIỆU] Phương thức Console.WriteLine() & Dấu chấm phẩy kết thúc lệnh
SLIDE 10: [IDE WORKFLOW] Tạo dự án Console Application trong Visual Studio (Hình 3.3, 3.4)
SLIDE 11: [TRỢ THỦ CODE] Tính năng IntelliSense & Parameter Info của IDE (Hình 3.5, 3.6, 3.7)
SLIDE 12: [CHẠY THỬ] Biên dịch & Thực thi ứng dụng Run Mode (Ctrl+F5) (Hình 3.8)
SLIDE 13: [GỠ LỖI CÚ PHÁP] Lỗi cú pháp (Syntax Errors), Gạch sóng đỏ & Cửa sổ Error List (Hình 3.9)
SLIDE 14: [CODE STUDY 2] Biến thể Welcome2.cs: Xuất 1 dòng bằng nhiều lệnh (Hình 3.10)
SLIDE 15: [CHECKPOINT 1] Câu hỏi củng cố kiến thức Tiết 1 & Thực hành phòng máy
SLIDE 16: [CODE STUDY 3] Xuất nhiều dòng bằng một lệnh: Welcome3.cs (Hình 3.11)
SLIDE 17: [BẢNG TRA CỨU] Các ký tự thoát thông dụng (Escape Sequences: \n, \t, \r, \\, \") (Hình 3.12)
SLIDE 18: [C# 6 FEATURE] Kỹ thuật Nội suy chuỗi (String Interpolation $"...") (Welcome4.cs - Hình 3.13)
SLIDE 19: [CODE STUDY 4] Ứng dụng tính tổng hai số nguyên: Addition.cs (Hình 3.14 Part 1)
SLIDE 20: [BIẾN SỐ] Khai báo biến kiểu int, Tên định danh camelCase & Vùng nhớ
SLIDE 21: [NHẬP LIỆU] Nhập chuỗi bằng Console.ReadLine() & Ép kiểu int.Parse()
SLIDE 22: [GÁN GIÁ TRỊ] Toán tử gán (=), Biểu thức vế phải và gán vào vế trái
SLIDE 23: [BỘ NHỚ RAM] Khái niệm ô nhớ: Tên, Kiểu, Địa chỉ và Giá trị (Hình 3.15, 3.16)
SLIDE 24: [CƠ CHẾ BỘ NHỚ] Đọc không phá hủy (Non-destructive) vs Ghi đè phá hủy (Destructive) (Hình 3.17)
SLIDE 25: [TOÁN TỬ SỐ HỌC] 5 Toán tử cơ bản (+, -, *, /, %) trong C# (Hình 3.18)
SLIDE 26: [CHIA NGUYÊN] Phép chia nguyên loại bỏ phần thập phân (Truncation) & Phép chia dư (%)
SLIDE 27: [THỨ TỰ ƯU TIÊN] Quy tắc ưu tiên toán tử số học (Precedence Rules) (Hình 3.19)
SLIDE 28: [NGOẶC ĐƠN] Kỹ thuật nhóm biểu thức bằng dấu ngoặc () & Tránh lỗi nhập nhằng
SLIDE 29: [CASE STUDY TOÁN] Chuyển đổi công thức đại số sang C#: Đa thức bậc 2 ax^2+bx+c (Hình 3.20)
SLIDE 30: [CHECKPOINT 2] Câu hỏi củng cố kiến thức Tiết 2 & Thực hành Addition.cs
SLIDE 31: [RẼ NHÁNH] Ra quyết định trong phần mềm: Câu lệnh điều kiện đơn if
SLIDE 32: [TOÁN TỬ SO SÁNH] Bảng toán tử quan hệ (<, <=, >, >=) & bình đẳng (==, !=) (Hình 3.21)
SLIDE 33: [LỖI KINH ĐIỂN 1] Phân biệt sống còn giữa Toán tử gán (=) và Toán tử so sánh bằng (==)
SLIDE 34: [CODE STUDY 5] Ứng dụng so sánh hai số nguyên: Comparison.cs (Hình 3.22)
SLIDE 35: [PHÂN TÍCH CODE] Cơ chế thực thi từng nhánh if và kết quả màn hình console
SLIDE 36: [LỖI KINH ĐIỂN 2] Cạm bẫy dấu chấm phẩy ';' sau biểu thức điều kiện if(...)
SLIDE 37: [KHỐI LỆNH] Khối lệnh compound statement với cặp dấu ngoặc nhọn { }
SLIDE 38: [TỔNG KẾT TOÁN TỬ] Bảng thứ tự ưu tiên và tính kết hợp đầy đủ các toán tử (Hình 3.23)
SLIDE 39: [CLEAN CODE] Chuẩn mực viết code C# chuyên nghiệp (Microsoft Coding Conventions)
SLIDE 40: [HANDS-ON LAB 3] Thực hành tự viết chương trình Comparison.cs & kiểm thử dữ liệu biên
SLIDE 41: [ĐỒ ÁN 1] Khảo sát bài tập vẽ hình bằng dấu hoa thị (Shapes with Asterisks - Hình 3.25)
SLIDE 42: [ĐỒ ÁN 2] Khảo sát bài tập in bảng nhân cửu chương (Multiplication Table - Hình 3.26)
SLIDE 43: [ĐỒ ÁN THỰC TẾ] Making a Difference: Ứng dụng tính chi phí tiết kiệm đi chung xe (Car-Pool)
SLIDE 44: [CHECKLIST CLOs] Tổng kết đánh giá 5 Chuẩn đầu ra bài học CLO 3.1 - 3.5
SLIDE 45: [TỰ HỌC & HOMEWORK] Bài tập về nhà, tự học MSDN & Giới thiệu Chương 4 (Classes & Objects)
```
