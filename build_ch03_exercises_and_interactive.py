# -*- coding: utf-8 -*-
"""
Build Chapter 3 Exercises and Interactive Exercises.
"""

import json

EXERCISES_CH3 = [
    # 3.1
    {
        "id": "3.1",
        "category": "self-review",
        "title": "Self-Review 3.1: Điền vào chỗ trống các khái niệm nền tảng",
        "description": "Củng cố các khái niệm cú pháp cơ bản của ứng dụng Console trong C#.",
        "question": "Điền từ hoặc cụm từ thích hợp vào chỗ trống trong các phát biểu sau:\n"
                    "a) Một _______ bắt đầu thân của mọi phương thức, và một _______ kết thúc thân của mọi phương thức.\n"
                    "b) Hầu hết các câu lệnh trong C# kết thúc bằng một dấu _______.\n"
                    "c) Câu lệnh _______ được sử dụng để đưa ra quyết định (rẽ nhánh).\n"
                    "d) Ký hiệu _______ bắt đầu một dòng chú thích đơn (single-line comment).\n"
                    "e) Dòng trống, ký tự dấu cách và ký tự _______ được gọi là khoảng trắng (whitespace).\n"
                    "f) Các _______ là những từ ngữ được dành riêng cho ngôn ngữ C# sử dụng.\n"
                    "g) Mọi ứng dụng C# đều bắt đầu thực thi tại phương thức _______.\n"
                    "h) Các phương thức _______ và _______ của lớp Console dùng để hiển thị thông tin ra màn hình.\n"
                    "i) Tính năng _______ cho phép bạn nhúng trực tiếp giá trị biến vào bên trong một chuỗi ký tự bằng dấu $.",
        "solution": "Đáp án chuẩn mực theo Giáo trình Deitel (trang 139):\n\n"
                    "a) **left brace ({)** (ngoặc nhọn mở), **right brace (})** (ngoặc nhọn đóng).\n"
                    "b) **semicolon (;)** (dấu chấm phẩy).\n"
                    "c) **if** (câu lệnh điều kiện if).\n"
                    "d) **//** (hai dấu gạch chéo liền nhau).\n"
                    "e) **tab characters** (ký tự tab, cùng với newline - ký tự xuống dòng).\n"
                    "f) **Keywords** (từ khóa / reserved words).\n"
                    "g) **Main** (phương thức Main viết hoa chữ M).\n"
                    "h) **Console.WriteLine** và **Console.Write**.\n"
                    "i) **string interpolation** (định dạng chuỗi nội suy với ký tự tiền tố $).",
        "hints": "Xem lại Mục 3.2 đến 3.5 trong giáo trình Deitel: cấu trúc Welcome1, escape sequences, và string interpolation.",
        "image": "images/fig3_01_welcome1_app.png"
    },
    # 3.2
    {
        "id": "3.2",
        "category": "self-review",
        "title": "Self-Review 3.2: Nhận định Đúng / Sai và giải thích kỹ thuật",
        "description": "Kiểm tra sự thấu hiểu về hành vi của trình biên dịch, toán tử và tính năng chuỗi trong C#.",
        "question": "Xác định các phát biểu sau là Đúng (True) hay Sai (False). Nếu Sai, hãy giải thích rõ lý do kỹ thuật:\n"
                    "a) Chú thích (Comments) khiến máy tính hiển thị văn bản đứng sau dấu // lên màn hình khi ứng dụng chạy.\n"
                    "b) C# xem hai biến number và NuMbEr là hoàn toàn giống nhau (identical).\n"
                    "c) Toán tử chia lấy dư (%) chỉ có thể được sử dụng với các toán hạng kiểu số nguyên.\n"
                    "d) Các toán tử số học *, /, %, + và - đều có cùng một mức độ ưu tiên tính toán.\n"
                    "e) Một chuỗi nội suy (interpolated string) bắt buộc phải bắt đầu bằng ký tự $ đặt ngay trước chuỗi.",
        "solution": "Phân tích và lời giải chuẩn mực theo Giáo trình Deitel (trang 140):\n\n"
                    "a) **False (Sai)**. Chú thích không làm máy tính thực hiện bất kỳ hành động nào và bị trình biên dịch bỏ qua hoàn toàn. Chúng chỉ dùng để giải thích mã nguồn cho con người đọc.\n"
                    "b) **False (Sai)**. C# là ngôn ngữ phân biệt hoa thường (case-sensitive), do đó `number` và `NuMbEr` là hai biến hoàn toàn khác nhau trong bộ nhớ.\n"
                    "c) **False (Sai)**. Trong C#, toán tử chia lấy dư `%` có thể áp dụng cho cả số thực dấu phẩy động (float, double), ví dụ: `7.5 % 2.0 = 1.5`.\n"
                    "d) **False (Sai)**. Các toán tử `*`, `/`, `%` có cùng mức độ ưu tiên cao hơn, còn `+` và `-` có mức độ ưu tiên thấp hơn.\n"
                    "e) **True (Đúng)**. Chuỗi nội suy bắt buộc phải có ký tự tiền tố `$` đứng ngay trước dấu mở ngoặc kép `$\"...\"`.",
        "hints": "Phân biệt tính nhạy chữ hoa/thường, cơ chế toán tử % trên số thực trong C#, và thứ tự ưu tiên nhân chia trước cộng trừ sau.",
        "image": "images/fig3_19_operator_precedence.png"
    },
    # 3.3
    {
        "id": "3.3",
        "category": "self-review",
        "title": "Self-Review 3.3: Viết câu lệnh thực thi các tác vụ cơ bản",
        "description": "Thực hành viết các câu lệnh khai báo biến, nhập xuất dữ liệu và so sánh điều kiện.",
        "question": "Viết câu lệnh C# chuẩn xác để hoàn thành mỗi tác vụ sau:\n"
                    "a) Khai báo các biến c, thisIsAVariable, q76354 và number thuộc kiểu dữ liệu int.\n"
                    "b) In câu nhắc yêu cầu người dùng nhập một số nguyên: \"Enter an integer: \".\n"
                    "c) Đọc một số nguyên từ bàn phím và gán kết quả cho biến value kiểu int.\n"
                    "d) Nếu biến number khác 7, hiển thị thông báo \"The variable number is not equal to 7\".\n"
                    "e) In chuỗi \"This is a C# app\" trên cùng một dòng trong cửa sổ console.\n"
                    "f) In chuỗi \"This is a C# app\" trên hai dòng, dòng thứ nhất kết thúc bằng C# sử dụng Console.WriteLine.\n"
                    "g) Sử dụng String Interpolation để hiển thị tổng của hai biến x và y.",
        "solution": "Mã nguồn câu lệnh chuẩn mực theo Giáo trình Deitel (trang 140):\n\n"
                    "```csharp\n"
                    "// a) Khai bao 4 bien kieu int\n"
                    "int c;\n"
                    "int thisIsAVariable;\n"
                    "int q76354;\n"
                    "int number;\n\n"
                    "// b) Cau nhac nhap so nguyen khong xuong dong\n"
                    "Console.Write(\"Enter an integer: \");\n\n"
                    "// c) Nhap chuoi va ep kieu sang int\n"
                    "int value = int.Parse(Console.ReadLine());\n\n"
                    "// d) Kiem tra dieu kien khac 7\n"
                    "if (number != 7)\n"
                    "{\n"
                    "   Console.WriteLine(\"The variable number is not equal to 7\");\n"
                    "}\n\n"
                    "// e) In tren mot dong\n"
                    "Console.WriteLine(\"This is a C# app\");\n\n"
                    "// f) In tren hai dong bang ky tu thoat \\n\n"
                    "Console.WriteLine(\"This is a C#\\napp\");\n\n"
                    "// g) String Interpolation tinh tong\n"
                    "Console.WriteLine($\"The sum of {x} and {y} is {x + y}\");\n"
                    "```",
        "hints": "Sử dụng int.Parse(Console.ReadLine()), toán tử khác !=, ký tự thoát \\n và cú pháp nội suy $.",
        "image": "images/fig3_14_addition_part1.png"
    },
    # 3.4
    {
        "id": "3.4",
        "category": "self-review",
        "title": "Self-Review 3.4: Phát hiện và sửa lỗi cú pháp trong câu lệnh",
        "description": "Rèn luyện kỹ năng phân tích lỗi cú pháp (Syntax Errors) và lỗi logic thường gặp.",
        "question": "Chỉ ra lỗi và sửa lại cho đúng trong mỗi đoạn mã lệnh C# sau:\n\n"
                    "a)\n"
                    "```csharp\n"
                    "if (c < 7);\n"
                    "{\n"
                    "   Console.WriteLine(\"c is less than 7\");\n"
                    "}\n"
                    "```\n\n"
                    "b)\n"
                    "```csharp\n"
                    "if (c => 7)\n"
                    "{\n"
                    "   Console.WriteLine(\"c is equal to or greater than 7\");\n"
                    "}\n"
                    "```",
        "solution": "Phân tích lỗi và phương án sửa chuẩn theo Giáo trình Deitel (trang 140):\n\n"
                    "a) **Lỗi:** Dấu chấm phẩy `;` đặt ngay sau dấu đóng ngoặc đơn của mệnh đề điều kiện `(c < 7)`. Dấu chấm phẩy này tạo thành một câu lệnh rỗng, khiến khối lệnh in phía sau luôn luôn được thực thi dù `c` có nhỏ hơn 7 hay không!\n"
                    "   **Khắc phục:** Xóa bỏ dấu chấm phẩy sau `(c < 7)`:\n"
                    "   ```csharp\n"
                    "   if (c < 7)\n"
                    "   {\n"
                    "      Console.WriteLine(\"c is less than 7\");\n"
                    "   }\n"
                    "   ```\n\n"
                    "b) **Lỗi:** Toán tử quan hệ viết sai thứ tự `=>`. Trong C#, toán tử lớn hơn hoặc bằng bắt buộc phải là `>=` (dấu `=>` dành riêng cho biểu thức lambda).\n"
                    "   **Khắc phục:** Đổi `=>` thành `>=`:\n"
                    "   ```csharp\n"
                    "   if (c >= 7)\n"
                    "   {\n"
                    "      Console.WriteLine(\"c is equal to or greater than 7\");\n"
                    "   }\n"
                    "   ```",
        "hints": "Không bao giờ đặt dấu chấm phẩy ngay sau biểu thức if; toán tử lớn hơn hoặc bằng là >= chứ không phải =>.",
        "image": "images/fig3_09_syntax_error_ide.png"
    },
    # 3.5
    {
        "id": "3.5",
        "category": "self-review",
        "title": "Self-Review 3.5: Các bước giải thuật tính tích của ba số nguyên",
        "description": "Thiết kế giải thuật và viết các dòng lệnh đơn lẻ tính tích 3 số nhập từ bàn phím.",
        "question": "Viết các khai báo biến, câu lệnh và chú thích thực hiện từng bước sau:\n"
                    "a) Viết chú thích nói rằng ứng dụng sẽ tính tích của ba số nguyên.\n"
                    "b) Khai báo các biến x, y, z và result thuộc kiểu int.\n"
                    "c) In câu nhắc yêu cầu người dùng nhập số nguyên thứ nhất.\n"
                    "d) Đọc số nguyên thứ nhất từ bàn phím và lưu vào biến x.\n"
                    "e) In câu nhắc và đọc số nguyên thứ hai lưu vào biến y.\n"
                    "f) In câu nhắc và đọc số nguyên thứ ba lưu vào biến z.\n"
                    "g) Tính tích của ba số x, y, z và gán kết quả cho biến result.\n"
                    "h) Hiển thị thông báo \"Product is \" kèm giá trị biến result sử dụng String Interpolation.",
        "solution": "Mã lệnh từng bước chuẩn mực theo Giáo trình Deitel (trang 140):\n\n"
                    "```csharp\n"
                    "// a) Chú thích mô tả mục đích chương trình\n"
                    "// Calculating the product of three integers\n\n"
                    "// b) Khai báo 4 biến số nguyên\n"
                    "int x; int y; int z; int result;\n\n"
                    "// c & d) Nhập số thứ nhất\n"
                    "Console.Write(\"Enter first integer: \");\n"
                    "x = int.Parse(Console.ReadLine());\n\n"
                    "// e) Nhập số thứ hai\n"
                    "Console.Write(\"Enter second integer: \");\n"
                    "y = int.Parse(Console.ReadLine());\n\n"
                    "// f) Nhập số thứ ba\n"
                    "Console.Write(\"Enter third integer: \");\n"
                    "z = int.Parse(Console.ReadLine());\n\n"
                    "// g) Tính tích ba số nguyên\n"
                    "result = x * y * z;\n\n"
                    "// h) Xuất kết quả bằng String Interpolation\n"
                    "Console.WriteLine($\"Product is {result}\");\n"
                    "```",
        "hints": "Áp dụng kỹ thuật nhập liệu với int.Parse(Console.ReadLine()) và toán tử nhân * lặp lại cho 3 toán hạng.",
        "image": "images/fig3_14_addition_part2.png"
    },
    # 3.6
    {
        "id": "3.6",
        "category": "self-review",
        "title": "Self-Review 3.6: Ứng dụng hoàn chỉnh Product.cs",
        "description": "Ghép nối các câu lệnh ở Bài 3.5 thành một ứng dụng C# hoàn chỉnh có thể biên dịch và chạy được.",
        "question": "Từ các câu lệnh đã viết ở Exercise 3.5, hãy đóng gói thành một chương trình C# hoàn chỉnh có tên lớp là Product, chứa phương thức Main và sử dụng không gian tên System. Chạy thử chương trình với ba số nguyên: 10, 20 và 30.",
        "solution": "Mã nguồn hoàn chỉnh `Product.cs` theo Giáo trình Deitel (Hình 3.24, trang 141):\n\n"
                    "```csharp\n"
                    "// Exercise 3.6: Product.cs\n"
                    "// Calculating the product of three integers.\n"
                    "using System;\n\n"
                    "class Product\n"
                    "{\n"
                    "   static void Main()\n"
                    "   {\n"
                    "      int x;      // Lưu số nguyên thứ nhất do người dùng nhập\n"
                    "      int y;      // Lưu số nguyên thứ hai do người dùng nhập\n"
                    "      int z;      // Lưu số nguyên thứ ba do người dùng nhập\n"
                    "      int result; // Lưu tích của ba số\n\n"
                    "      Console.Write(\"Enter first integer: \");\n"
                    "      x = int.Parse(Console.ReadLine());\n\n"
                    "      Console.Write(\"Enter second integer: \");\n"
                    "      y = int.Parse(Console.ReadLine());\n\n"
                    "      Console.Write(\"Enter third integer: \");\n"
                    "      z = int.Parse(Console.ReadLine());\n\n"
                    "      result = x * y * z; // Thực hiện phép nhân trong bộ nhớ\n\n"
                    "      Console.WriteLine($\"Product is {result}\");\n"
                    "   } // kết thúc Main\n"
                    "} // kết thúc class Product\n"
                    "```\n\n"
                    "**Kết quả chạy thử mẫu:**\n"
                    "```text\n"
                    "Enter first integer: 10\n"
                    "Enter second integer: 20\n"
                    "Enter third integer: 30\n"
                    "Product is 6000\n"
                    "```",
        "hints": "Tạo dự án Console App trong Visual Studio, dán đoạn mã trên vào Program.cs và bấm Ctrl+F5 để chạy.",
        "image": "images/fig3_20_polynomial_evaluation.png"
    },
    # 3.7
    {
        "id": "3.7",
        "category": "exercises",
        "title": "Exercise 3.7: Điền từ còn thiếu vào các nhận định nâng cao",
        "description": "Các khái niệm nâng cao về chỉ thị using, loại chú thích và thứ tự ngoặc lồng nhau.",
        "question": "Điền từ hoặc cụm từ thích hợp vào chỗ trống:\n"
                    "a) Mỗi chỉ thị using xác định một _______ chứa các lớp mà ứng dụng C# có thể sử dụng.\n"
                    "b) Các ký hiệu _______ và _______ được dùng cho chú thích nhiều dòng (delimited comments).\n"
                    "c) Các phép tính toán trong C# thường được thực hiện bởi các câu lệnh _______.\n"
                    "d) Các toán tử số học có cùng mức độ ưu tiên với phép nhân (*) là phép chia (/) và phép _______.\n"
                    "e) Khi các cặp ngoặc đơn trong biểu thức số học lồng nhau, cặp ngoặc _______ sẽ được tính toán trước tiên.\n"
                    "f) Một vị trí trong bộ nhớ máy tính có thể chứa các giá trị khác nhau tại các thời điểm trong khi ứng dụng chạy được gọi là một _______.",
        "solution": "Đáp án chuẩn theo Giáo trình Deitel (trang 141):\n\n"
                    "a) **namespace** (không gian tên, ví dụ: System).\n"
                    "b) **/* ** và ** */** (cặp ký hiệu mở và đóng chú thích khối nhiều dòng).\n"
                    "c) **assignment** (câu lệnh gán / tính toán số học).\n"
                    "d) **remainder (%)** (phép chia lấy dư).\n"
                    "e) **innermost** (cặp ngoặc đơn nằm trong cùng nhất).\n"
                    "f) **variable** (biến số).",
        "hints": "Nhớ lại: namespace gom nhóm các lớp; ngoặc trong cùng tính trước; biến lưu trữ giá trị khả biến trong RAM.",
        "image": "images/fig3_18_arithmetic_operators.png"
    },
    # 3.8
    {
        "id": "3.8",
        "category": "exercises",
        "title": "Exercise 3.8: Viết câu lệnh in bảng tab và nhúng dấu ngoặc kép",
        "description": "Ứng dụng ký tự thoát \\t và \\\" trong thực tế định dạng văn bản.",
        "question": "Viết các câu lệnh C# thực hiện mỗi yêu cầu sau:\n"
                    "a) In dòng chữ \"Roll Number    Student Name    Grade\" trên một dòng đơn, phân cách các cột bằng tab stop.\n"
                    "b) In ra màn hình ký tự dấu ngoặc kép đôi (\") bên trong một chuỗi văn bản.\n"
                    "c) Khai báo một biến kiểu chuỗi có tên là courseName và khởi tạo giá trị ban đầu là \"C# Programming\".",
        "solution": "Mã nguồn câu lệnh C# chuẩn xác:\n\n"
                    "```csharp\n"
                    "// a) In tieu de bang bang ky tu thoat \\t\n"
                    "Console.WriteLine(\"Roll Number\\tStudent Name\\tGrade\");\n\n"
                    "// b) In ky tu ngoac kep doi bang \\\"\n"
                    "Console.WriteLine(\"He said: \\\"C# is awesome!\\\"\");\n\n"
                    "// c) Khai bao va khoi tao bien kieu string\n"
                    "string courseName = \"C# Programming\";\n"
                    "```",
        "hints": "Sử dụng \\t cho tab ngang và \\\" cho dấu ngoặc kép đôi.",
        "image": "images/fig3_12_escape_sequences_table.png"
    },
    # 3.9
    {
        "id": "3.9",
        "category": "exercises",
        "title": "Exercise 3.9: Nhận định Đúng / Sai về tên biến, IntelliSense và void",
        "description": "Đánh giá tính hợp lệ của quy tắc đặt tên định danh và cơ chế IntelliSense.",
        "question": "Xác định Đúng (True) hay Sai (False). Nếu Sai, hãy giải thích rõ lý do:\n"
                    "a) IntelliSense liệt kê các mục bắt đầu bằng hoặc chứa các chữ cái mà người dùng đã gõ.\n"
                    "b) Các tên sau đây đều là tên biến hợp lệ trong C#: _under_bar_, m928134, t5, j7, her_sales, his_account_total, a, b, c, z và z2.\n"
                    "c) Một biểu thức số học C# hợp lệ không chứa dấu ngoặc đơn luôn luôn được tính toán tuần tự từ trái sang phải.\n"
                    "d) Từ khóa void chỉ ra rằng phương thức Main sẽ không trả về bất kỳ giá trị nào sau khi hoàn thành nhiệm vụ.",
        "solution": "Phân tích chuẩn xác theo Giáo trình Deitel (trang 141):\n\n"
                    "a) **True (Đúng)**. IntelliSense hỗ trợ tìm kiếm mờ (fuzzy search), hiển thị cả thành viên bắt đầu hoặc chứa chuỗi ký tự vừa gõ.\n"
                    "b) **True (Đúng)**. Tất cả các tên này đều hợp lệ vì bắt đầu bằng chữ cái hoặc dấu gạch dưới `_`, và chỉ chứa chữ cái, chữ số, dấu gạch dưới.\n"
                    "c) **False (Sai)**. Biểu thức không có ngoặc vẫn phải tuân thủ thứ tự ưu tiên của toán tử: các toán tử `*`, `/`, `%` được tính trước các toán tử `+`, `-` dù chúng đứng sau trong biểu thức!\n"
                    "d) **True (Đúng)**. Từ khóa `void` biểu thị kiểu trả về rỗng, phương thức kết thúc mà không truyền giá trị về cho hệ điều hành.",
        "hints": "Nhớ rằng nhân chia luôn được ưu tiên tính trước cộng trừ dù không có ngoặc đơn; tên biến bắt đầu bằng dấu gạch dưới là hoàn toàn hợp lệ.",
        "image": "images/fig3_02_keywords_table.png"
    },
    # 3.10
    {
        "id": "3.10",
        "category": "exercises",
        "title": "Exercise 3.10: Dự đoán kết quả hiển thị của String Interpolation",
        "description": "Rèn luyện khả năng đọc hiểu mã nguồn và cơ chế tính toán trong chuỗi nội suy $.",
        "question": "Giả sử biến x = 2 và y = 3, hãy cho biết mỗi câu lệnh sau đây sẽ in ra màn hình nội dung gì:\n"
                    "a) Console.WriteLine($\"x = {x}\");\n"
                    "b) Console.WriteLine($\"Value of {x} + {x} is {x + x}\");\n"
                    "c) Console.Write(\"x =\");\n"
                    "d) Console.WriteLine($\"{x + y} = {y + x}\");",
        "solution": "Kết quả hiển thị chính xác trên màn hình Console:\n\n"
                    "a) `x = 2`\n"
                    "b) `Value of 2 + 2 is 4`\n"
                    "c) `x =` (không xuống dòng)\n"
                    "d) `5 = 5`\n\n"
                    "**Giải thích:** Các biểu thức `{x + x}` và `{x + y}` bên trong cặp ngoặc nhọn của chuỗi nội suy được tính toán tự động thành các số nguyên (4 và 5) trước khi chuyển đổi sang chuỗi và ghép vào dòng văn bản.",
        "hints": "Thay thế x bằng 2, y bằng 3 và tính toán các phép toán số học bên trong { }.",
        "image": "images/fig3_13_welcome4_interpolation.png"
    },
    # 3.11
    {
        "id": "3.11",
        "category": "exercises",
        "title": "Exercise 3.11: Xác định câu lệnh làm thay đổi giá trị biến (Ghi đè phá hủy)",
        "description": "Phân biệt giữa thao tác đọc không phá hủy và thao tác ghi đè phá hủy ô nhớ.",
        "question": "Trong các câu lệnh C# sau đây, câu lệnh nào làm thay đổi giá trị của một biến (thao tác Destructive Write)?\n"
                    "a) p = i + j + k + 7;\n"
                    "b) Console.WriteLine(\"variables whose values are modified\");\n"
                    "c) Console.WriteLine(\"a = 5\");\n"
                    "d) value = int.Parse(Console.ReadLine());",
        "solution": "Phân tích và đáp án chuẩn mực theo Giáo trình Deitel (trang 142):\n\n"
                    "- **Câu a)**: **CÓ thay đổi**. Biến `p` nằm ở vế trái của toán tử gán `=` sẽ nhận giá trị mới từ tổng `i + j + k + 7`, giá trị cũ của `p` bị xóa vĩnh viễn (Destructive Write). Các biến `i`, `j`, `k` chỉ bị đọc nên không đổi.\n"
                    "- **Câu b)**: **KHÔNG thay đổi**. Chỉ là câu lệnh in một chuỗi văn bản cố định ra màn hình console.\n"
                    "- **Câu c)**: **KHÔNG thay đổi**. Mặc dù có chữ `a = 5` nhưng đây chỉ là ký tự bên trong chuỗi, không phải câu lệnh gán biến.\n"
                    "- **Câu d)**: **CÓ thay đổi**. Biến `value` nhận giá trị số nguyên mới do người dùng nhập từ bàn phím thông qua toán tử gán `=`, giá trị cũ trong ô nhớ bị ghi đè hoàn toàn.",
        "hints": "Chỉ các câu lệnh có toán tử gán = với biến ở vế trái mới làm thay đổi ô nhớ của biến đó.",
        "image": "images/fig3_15_memory_number1.png"
    },
    # 3.12
    {
        "id": "3.12",
        "category": "exercises",
        "title": "Exercise 3.12: Chuyển đổi biểu thức toán học sang mã lệnh C#",
        "description": "Viết biểu thức C# tương đương cho các công thức đại số toán học.",
        "question": "Chuyển các biểu thức toán học sau sang mã lệnh C# chuẩn xác:\n"
                    "a) Tích của m và n chia cho 2: (m * n) / 2\n"
                    "b) Biểu thức tính diện tích hình thang: area = (a + b) * h / 2\n"
                    "c) Biểu thức tính giá trị đa thức bậc 3: y = a * x^3 + 7",
        "solution": "Mã lệnh C# tương đương chuẩn mực:\n\n"
                    "```csharp\n"
                    "// a) Tich m va n chia 2 (neu can so thuc thi dung 2.0)\n"
                    "int result1 = (m * n) / 2;\n\n"
                    "// b) Dien tich hinh thang (can ngoac don de cong a + b truoc)\n"
                    "double area = (a + b) * h / 2.0;\n\n"
                    "// c) Da thuc bac 3 (khong dung dau mu ^ vi ^ la phep toan XOR)\n"
                    "int y = a * x * x * x + 7;\n"
                    "```",
        "hints": "Luôn dùng ngoặc đơn để chỉ rõ thứ tự ưu tiên; lũy thừa x^3 viết thành x * x * x.",
        "image": "images/fig3_20_polynomial_evaluation.png"
    },
    # 3.14
    {
        "id": "3.14",
        "category": "exercises",
        "title": "Exercise 3.14: Ứng dụng tính toán Hình tròn (Circle)",
        "description": "Viết ứng dụng Console cho phép nhập bán kính r (kiểu int) và tính đường kính, chu vi, diện tích.",
        "question": "Viết một ứng dụng C# cho phép người dùng nhập vào bán kính của một hình tròn (số nguyên r kiểu int) và in ra màn hình:\n"
                    "- Đường kính (Diameter = 2 * r)\n"
                    "- Chu vi (Circumference = 2 * Math.PI * r)\n"
                    "- Diện tích (Area = Math.PI * r * r)\n"
                    "Sử dụng hằng số Math.PI và định dạng chuỗi nội suy $.",
        "solution": "Mã nguồn hoàn chỉnh `Circle.cs`:\n\n"
                    "```csharp\n"
                    "using System;\n\n"
                    "class Circle\n"
                    "{\n"
                    "   static void Main()\n"
                    "   {\n"
                    "      Console.Write(\"Nhap ban kinh hinh tron (so nguyen): \");\n"
                    "      int r = int.Parse(Console.ReadLine());\n\n"
                    "      int diameter = 2 * r;\n"
                    "      double circumference = 2 * Math.PI * r;\n"
                    "      double area = Math.PI * r * r;\n\n"
                    "      Console.WriteLine($\"Duong kinh (Diameter): {diameter}\");\n"
                    "      Console.WriteLine($\"Chu vi (Circumference): {circumference:F2}\");\n"
                    "      Console.WriteLine($\"Dien tich (Area): {area:F2}\");\n"
                    "   }\n"
                    "}\n"
                    "```",
        "hints": "Sử dụng Math.PI có sẵn trong không gian tên System; r * r để tính r bình phương.",
        "image": "images/fig3_26_multiplication_table.png"
    },
    # 3.25
    {
        "id": "3.25",
        "category": "exercises",
        "title": "Exercise 3.25: Vẽ các hình khối bằng ký tự hoa thị (*)",
        "description": "Viết ứng dụng vẽ hình hộp chữ nhật, oval, mũi tên và hình thoi bằng các dấu sao.",
        "question": "Viết một ứng dụng Console C# sử dụng các câu lệnh Console.WriteLine để in ra 4 hình đồ họa đặt cạnh nhau: Hình hộp chữ nhật, Hình Oval, Mũi tên hướng lên, và Hình thoi (Diamond) như minh họa tại Hình 3.25 trong giáo trình Deitel.",
        "solution": "Mã nguồn hoàn chỉnh `Shapes.cs` theo Giáo trình Deitel:\n\n"
                    "```csharp\n"
                    "using System;\n\n"
                    "class Shapes\n"
                    "{\n"
                    "   static void Main()\n"
                    "   {\n"
                    "      Console.WriteLine(\"*********     ***       *        *    \");\n"
                    "      Console.WriteLine(\"*       *   *     *    ***      * *   \");\n"
                    "      Console.WriteLine(\"*       *  *       *  *****    *   *  \");\n"
                    "      Console.WriteLine(\"*       *  *       *    *     *     * \");\n"
                    "      Console.WriteLine(\"*       *  *       *    *    *       *\");\n"
                    "      Console.WriteLine(\"*       *  *       *    *     *     * \");\n"
                    "      Console.WriteLine(\"*       *  *       *    *      *   *  \");\n"
                    "      Console.WriteLine(\"*       *   *     *     *       * *   \");\n"
                    "      Console.WriteLine(\"*********     ***       *        *    \");\n"
                    "   }\n"
                    "}\n"
                    "```",
        "hints": "Mỗi dòng lệnh Console.WriteLine in ra một lát cắt ngang của cả 4 hình cùng một lúc.",
        "image": "images/fig3_25_shapes_output.png"
    },
    # 3.26
    {
        "id": "3.26",
        "category": "exercises",
        "title": "Exercise 3.26: Bảng tính bình phương và lập phương từ 0 đến 10",
        "description": "In bảng số nguyên gồm 3 cột: number, square, cube từ 0 đến 10 sử dụng tab \\t.",
        "question": "Viết một ứng dụng C# tính và hiển thị bình phương (x^2) và lập phương (x^3) của các số từ 0 đến 10. Bảng in ra phải có tiêu đề ba cột: number, square, cube được căn chỉnh thẳng hàng bằng ký tự thoát \\t.",
        "solution": "Mã nguồn hoàn chỉnh `SquaresAndCubes.cs` theo Giáo trình Deitel:\n\n"
                    "```csharp\n"
                    "using System;\n\n"
                    "class SquaresAndCubes\n"
                    "{\n"
                    "   static void Main()\n"
                    "   {\n"
                    "      Console.WriteLine(\"number\\tsquare\\tcube\");\n"
                    "      Console.WriteLine($\"0\\t{0*0}\\t{0*0*0}\");\n"
                    "      Console.WriteLine($\"1\\t{1*1}\\t{1*1*1}\");\n"
                    "      Console.WriteLine($\"2\\t{2*2}\\t{2*2*2}\");\n"
                    "      Console.WriteLine($\"3\\t{3*3}\\t{3*3*3}\");\n"
                    "      Console.WriteLine($\"4\\t{4*4}\\t{4*4*4}\");\n"
                    "      Console.WriteLine($\"5\\t{5*5}\\t{5*5*5}\");\n"
                    "      Console.WriteLine($\"6\\t{6*6}\\t{6*6*6}\");\n"
                    "      Console.WriteLine($\"7\\t{7*7}\\t{7*7*7}\");\n"
                    "      Console.WriteLine($\"8\\t{8*8}\\t{8*8*8}\");\n"
                    "      Console.WriteLine($\"9\\t{9*9}\\t{9*9*9}\");\n"
                    "      Console.WriteLine($\"10\\t{10*10}\\t{10*10*10}\");\n"
                    "   }\n"
                    "}\n"
                    "```",
        "hints": "Sử dụng String Interpolation $ kết hợp ký tự thoát \\t để căn thẳng các cột số.",
        "image": "images/fig3_26_multiplication_table.png"
    }
]

# ============================================================================
# 2. INTERACTIVE EXERCISES DATA FOR CHAPTER 3
# ============================================================================
INTERACTIVE_CH3 = {
    "3.1": {
        "mode": "fill-blank",
        "title": "Self-Review 3.1: Điền vào chỗ trống các khái niệm nền tảng",
        "items": [
            {
                "id": "a1",
                "label": "a1)",
                "prefix": "Một",
                "suffix": "bắt đầu thân của mọi phương thức trong C# (ví dụ: { ).",
                "acceptable": ["left brace", "leftbrace", "ngoac nhon mo", "ngoặc nhọn mở", "dau ngoac nhon mo", "dấu ngoặc nhọn mở", "{"],
                "correctAnswer": "left brace ({) - dấu ngoặc nhọn mở",
                "explanation": "Mục 3.2.7: Dấu ngoặc nhọn mở { bắt đầu khối mã lệnh của phương thức hoặc lớp."
            },
            {
                "id": "a2",
                "label": "a2)",
                "prefix": "Một",
                "suffix": "kết thúc thân của mọi phương thức trong C# (ví dụ: } ).",
                "acceptable": ["right brace", "rightbrace", "ngoac nhon dong", "ngoặc nhọn đóng", "dau ngoac nhon dong", "dấu ngoặc nhọn đóng", "}"],
                "correctAnswer": "right brace (}) - dấu ngoặc nhọn đóng",
                "explanation": "Mục 3.2.7: Dấu ngoặc nhọn đóng } kết thúc khối mã lệnh."
            },
            {
                "id": "b",
                "label": "b)",
                "prefix": "Hầu hết các câu lệnh thực thi trong C# kết thúc bằng một dấu",
                "suffix": "(statement terminator).",
                "acceptable": ["semicolon", "cham phay", "chấm phẩy", "dau cham phay", "dấu chấm phẩy", ";"],
                "correctAnswer": "semicolon (;) - dấu chấm phẩy",
                "explanation": "Mục 3.2.6: Dấu chấm phẩy ; là ký tự kết thúc câu lệnh bắt buộc trong C#."
            },
            {
                "id": "c",
                "label": "c)",
                "prefix": "Câu lệnh",
                "suffix": "được sử dụng để đưa ra quyết định rẽ nhánh logic trong chương trình.",
                "acceptable": ["if", "if statement", "cau lenh if", "câu lệnh if"],
                "correctAnswer": "if - câu lệnh điều kiện if",
                "explanation": "Mục 3.9: Cấu trúc điều khiển rẽ nhánh if cho phép đưa ra quyết định dựa trên điều kiện boolean."
            },
            {
                "id": "d",
                "label": "d)",
                "prefix": "Ký hiệu",
                "suffix": "bắt đầu một dòng chú thích đơn (single-line comment).",
                "acceptable": ["//", "hai dau gach cheo", "hai dấu gạch chéo", "double slash"],
                "correctAnswer": "// - hai dấu gạch chéo liền nhau",
                "explanation": "Mục 3.2.1: Ký hiệu // mở đầu chú thích một dòng, trình biên dịch bỏ qua đến cuối dòng."
            },
            {
                "id": "e",
                "label": "e)",
                "prefix": "Dòng trống, ký tự dấu cách và ký tự",
                "suffix": "được gọi chung là khoảng trắng (whitespace).",
                "acceptable": ["tab", "dau tab", "dấu tab", "tab character", "newline", "xuong dong", "xuống dòng"],
                "correctAnswer": "tab (cùng với newline - ký tự xuống dòng)",
                "explanation": "Mục 3.2.3: Whitespace bao gồm dấu cách (space), phím tab và ký tự xuống dòng (newline)."
            },
            {
                "id": "f",
                "label": "f)",
                "prefix": "Các",
                "suffix": "là những từ ngữ được dành riêng cho ngôn ngữ C# quy định ý nghĩa đặc biệt.",
                "acceptable": ["keywords", "tu khoa", "từ khóa", "reserved words", "tu danh rieng", "từ dành riêng"],
                "correctAnswer": "Keywords (từ khóa / reserved words)",
                "explanation": "Mục 3.2: Các từ khóa như class, static, void, int, if... được dành riêng cho cú pháp C#."
            },
            {
                "id": "g",
                "label": "g)",
                "prefix": "Mọi ứng dụng C# đều bắt đầu thực thi tại phương thức",
                "suffix": "(Điểm khởi nhập Entry Point).",
                "acceptable": ["main", "main()", "phuong thuc main", "phương thức main"],
                "correctAnswer": "Main (viết hoa chữ M)",
                "explanation": "Mục 3.2.5: Phương thức static void Main() là điểm khởi nhập duy nhất của ứng dụng C#."
            },
            {
                "id": "h",
                "label": "h)",
                "prefix": "Hai phương thức của lớp Console dùng để xuất dữ liệu ra màn hình là Console.Write và",
                "suffix": ".",
                "acceptable": ["console.writeline", "writeline", "console.writeline()", "writeline()"],
                "correctAnswer": "Console.WriteLine (hoặc Console.Write)",
                "explanation": "Mục 3.2.6 & 3.4.1: Write và WriteLine là hai phương thức xuất văn bản chuẩn mực."
            },
            {
                "id": "i",
                "label": "i)",
                "prefix": "Tính năng",
                "suffix": "cho phép bạn nhúng trực tiếp giá trị biến vào bên trong chuỗi ký tự bằng dấu tiền tố $.",
                "acceptable": ["string interpolation", "interpolation", "noi suy chuoi", "nội suy chuỗi", "dinh dang chuoi noi suy", "định dạng chuỗi nội suy"],
                "correctAnswer": "string interpolation (định dạng chuỗi nội suy)",
                "explanation": "Mục 3.5: Tính năng $\"Hello {name}\" nhúng trực tiếp biểu thức vào chuỗi ký tự."
            }
        ]
    },

    "3.2": {
        "mode": "true-false",
        "title": "Self-Review 3.2: Nhận định Đúng / Sai và giải thích kỹ thuật",
        "items": [
            {
                "id": "a",
                "label": "a)",
                "statement": "Chú thích (Comments) khiến máy tính hiển thị văn bản đứng sau dấu // lên màn hình khi ứng dụng chạy.",
                "correct": False,
                "explanation": "Sai (False). Chú thích hoàn toàn không gây ra bất kỳ hành động nào và bị trình biên dịch bỏ qua; chỉ phục vụ tài liệu hóa mã nguồn cho người đọc."
            },
            {
                "id": "b",
                "label": "b)",
                "statement": "C# xem hai biến number và NuMbEr là hoàn toàn giống nhau (identical).",
                "correct": False,
                "explanation": "Sai (False). Ngôn ngữ C# phân biệt chữ hoa chữ thường (case-sensitive), do đó number và NuMbEr là hai ô nhớ biến hoàn toàn độc lập."
            },
            {
                "id": "c",
                "label": "c)",
                "statement": "Toán tử chia lấy dư (%) chỉ có thể được sử dụng với các toán hạng kiểu số nguyên.",
                "correct": False,
                "explanation": "Sai (False). Trong C#, toán tử chia lấy dư % hoạt động hoàn hảo trên cả số thực dấu phẩy động (float, double), ví dụ: 7.5 % 2.0 = 1.5."
            },
            {
                "id": "d",
                "label": "d)",
                "statement": "Các toán tử số học *, /, %, + và - đều có cùng một mức độ ưu tiên tính toán.",
                "correct": False,
                "explanation": "Sai (False). Nhân (*), chia (/), và chia lấy dư (%) có cùng mức ưu tiên cao hơn cộng (+) và trừ (-)."
            },
            {
                "id": "e",
                "label": "e)",
                "statement": "Một chuỗi nội suy (interpolated string) bắt buộc phải bắt đầu bằng ký tự $ đặt ngay trước chuỗi.",
                "correct": True,
                "explanation": "Đúng (True). Ký tự $ đặt ngay trước dấu mở ngoặc kép báo hiệu cho trình biên dịch kích hoạt cơ chế String Interpolation."
            }
        ]
    },

    "3.4": {
        "mode": "fill-blank",
        "title": "Self-Review 3.4: Phát hiện và sửa lỗi cú pháp",
        "items": [
            {
                "id": "a",
                "label": "a)",
                "prefix": "Trong câu lệnh if (c < 7); { Console.WriteLine(...); }, lỗi cú pháp là dấu",
                "suffix": "đặt ngay sau mệnh đề điều kiện tạo thành câu lệnh rỗng.",
                "acceptable": ["cham phay", "chấm phẩy", "semicolon", ";", "dau cham phay", "dấu chấm phẩy"],
                "correctAnswer": "dấu chấm phẩy (semicolon ;) sau (c < 7)",
                "explanation": "Dấu chấm phẩy sau if kết thúc câu lệnh if ngay lập tức, khiến khối lệnh { ... } phía sau luôn luôn bị chạy!"
            },
            {
                "id": "b",
                "label": "b)",
                "prefix": "Trong câu lệnh if (c => 7), toán tử quan hệ đúng theo chuẩn C# phải là",
                "suffix": "(lớn hơn hoặc bằng).",
                "acceptable": [">=", "lon hon hoac bang", "lớn hơn hoặc bằng", "greater than or equal"],
                "correctAnswer": ">= (dấu lớn hơn đứng trước dấu bằng)",
                "explanation": "Trong C#, toán tử so sánh lớn hơn hoặc bằng là >=, còn => là lambda operator."
            }
        ]
    },

    "3.7": {
        "mode": "fill-blank",
        "title": "Exercise 3.7: Điền từ còn thiếu vào các nhận định nâng cao",
        "items": [
            {
                "id": "a",
                "label": "a)",
                "prefix": "Mỗi chỉ thị using xác định một",
                "suffix": "chứa các lớp mà ứng dụng C# có thể sử dụng (ví dụ: System).",
                "acceptable": ["namespace", "khong gian ten", "không gian tên"],
                "correctAnswer": "namespace (không gian tên)",
                "explanation": "Chỉ thị using nạp một namespace chứa các lớp thư viện vào phạm vi mã nguồn."
            },
            {
                "id": "b",
                "label": "b)",
                "prefix": "Cặp ký hiệu dùng cho chú thích nhiều dòng (delimited comments) trong C# là /* và",
                "suffix": ".",
                "acceptable": ["*/", "dau sao va gach cheo"],
                "correctAnswer": "*/ (dấu sao và gạch chéo đóng)",
                "explanation": "Chú thích khối nhiều dòng bắt đầu bằng /* và kết thúc bằng */."
            },
            {
                "id": "c",
                "label": "c)",
                "prefix": "Các toán tử số học có cùng mức độ ưu tiên với phép nhân (*) là phép chia (/) và phép",
                "suffix": "(ký hiệu %).",
                "acceptable": ["chia lay du", "chia lấy dư", "remainder", "modulus", "%", "phan du", "phần dư"],
                "correctAnswer": "chia lấy dư (%) - remainder / modulus",
                "explanation": "Ba toán tử *, /, % có cùng mức độ ưu tiên cao trong các phép toán số học."
            },
            {
                "id": "d",
                "label": "d)",
                "prefix": "Khi các cặp ngoặc đơn trong biểu thức số học lồng nhau, cặp ngoặc nằm ở vị trí",
                "suffix": "sẽ được tính toán trước tiên.",
                "acceptable": ["trong cung", "trong cùng", "innermost", "ben trong", "bên trong"],
                "correctAnswer": "trong cùng nhất (innermost)",
                "explanation": "Quy tắc ngoặc đơn: Cặp ngoặc nằm trong cùng luôn được ưu tiên thực thi đầu tiên."
            },
            {
                "id": "e",
                "label": "e)",
                "prefix": "Một vị trí trong bộ nhớ RAM có tên định danh và chứa giá trị thay đổi được gọi là",
                "suffix": ".",
                "acceptable": ["bien", "biến", "variable", "bien so", "biến số"],
                "correctAnswer": "biến (variable)",
                "explanation": "Mỗi biến đại diện cho một vị trí ô nhớ trong RAM có tên, kiểu, kích thước và giá trị."
            }
        ]
    },

    "3.9": {
        "mode": "true-false",
        "title": "Exercise 3.9: Nhận định Đúng / Sai về tên biến, IntelliSense và void",
        "items": [
            {
                "id": "a",
                "label": "a)",
                "statement": "IntelliSense liệt kê các mục bắt đầu bằng hoặc chứa các chữ cái mà người dùng đã gõ.",
                "correct": True,
                "explanation": "Đúng (True). IntelliSense hỗ trợ tìm kiếm mờ (fuzzy search), hiển thị cả thành viên bắt đầu hoặc chứa chuỗi ký tự vừa gõ."
            },
            {
                "id": "b",
                "label": "b)",
                "statement": "Các tên sau đây đều là tên biến hợp lệ trong C#: _under_bar_, m928134, t5, j7, her_sales, his_account_total, a, b, c, z và z2.",
                "correct": True,
                "explanation": "Đúng (True). Tất cả các tên này đều hợp lệ vì bắt đầu bằng chữ cái hoặc dấu gạch dưới _, và chỉ chứa chữ cái, chữ số, dấu gạch dưới."
            },
            {
                "id": "c",
                "label": "c)",
                "statement": "Một biểu thức số học C# hợp lệ không chứa dấu ngoặc đơn luôn luôn được tính toán tuần tự từ trái sang phải.",
                "correct": False,
                "explanation": "Sai (False). Biểu thức không có ngoặc vẫn phải tuân thủ thứ tự ưu tiên của toán tử: *, /, % luôn được tính trước +, -."
            },
            {
                "id": "d",
                "label": "d)",
                "statement": "Từ khóa void chỉ ra rằng phương thức Main sẽ không trả về bất kỳ giá trị nào sau khi hoàn thành nhiệm vụ.",
                "correct": True,
                "explanation": "Đúng (True). Từ khóa void quy định kiểu trả về rỗng, phương thức không trả dữ liệu về hệ điều hành."
            }
        ]
    },

    "3.10": {
        "mode": "fill-blank",
        "title": "Exercise 3.10: Dự đoán kết quả hiển thị của String Interpolation",
        "items": [
            {
                "id": "a",
                "label": "a)",
                "prefix": "Với x = 2, lệnh Console.WriteLine($\"x = {x}\"); in ra dòng chữ:",
                "suffix": ".",
                "acceptable": ["x = 2", "x=2"],
                "correctAnswer": "x = 2",
                "explanation": "{x} được thay thế bằng giá trị 2."
            },
            {
                "id": "b",
                "label": "b)",
                "prefix": "Với x = 2, lệnh Console.WriteLine($\"Value of {x} + {x} is {x + x}\"); in ra:",
                "suffix": ".",
                "acceptable": ["value of 2 + 2 is 4", "value of 2+2 is 4"],
                "correctAnswer": "Value of 2 + 2 is 4",
                "explanation": "{x} là 2, {x + x} tính toán thành 4."
            },
            {
                "id": "c",
                "label": "c)",
                "prefix": "Với x = 2, y = 3, lệnh Console.WriteLine($\"{x + y} = {y + x}\"); in ra:",
                "suffix": ".",
                "acceptable": ["5 = 5", "5=5"],
                "correctAnswer": "5 = 5",
                "explanation": "{x + y} là 5 và {y + x} cũng là 5."
            }
        ]
    },

    "3.11": {
        "mode": "fill-blank",
        "title": "Exercise 3.11: Xác định câu lệnh làm thay đổi giá trị biến (Destructive Write)",
        "items": [
            {
                "id": "a",
                "label": "a)",
                "prefix": "Câu lệnh p = i + j + k + 7; có làm thay đổi giá trị của biến nào không? (Trả lời 'co' hoặc 'khong'):",
                "suffix": ".",
                "acceptable": ["co", "có", "yes", "p"],
                "correctAnswer": "Có (làm thay đổi biến p qua phép gán =)",
                "explanation": "Biến p ở vế trái toán tử gán nhận giá trị mới, ghi đè giá trị cũ."
            },
            {
                "id": "b",
                "label": "b)",
                "prefix": "Câu lệnh Console.WriteLine(\"a = 5\"); có làm thay đổi giá trị của biến nào không? (Trả lời 'co' hoặc 'khong'):",
                "suffix": ".",
                "acceptable": ["khong", "không", "no"],
                "correctAnswer": "Không (chỉ in chuỗi ký tự cố định ra màn hình)",
                "explanation": "\"a = 5\" chỉ là chuỗi văn bản thuần túy, không có biến nào bị gán."
            },
            {
                "id": "c",
                "label": "c)",
                "prefix": "Câu lệnh value = int.Parse(Console.ReadLine()); có làm thay đổi giá trị của biến value không? (Trả lời 'co' hoặc 'khong'):",
                "suffix": ".",
                "acceptable": ["co", "có", "yes"],
                "correctAnswer": "Có (ghi giá trị số nguyên mới vào biến value)",
                "explanation": "Biến value nhận giá trị nhập từ người dùng thông qua toán tử gán =."
            }
        ]
    }
}

# Export snippets to files for merging
with open("js/exercises_ch03_snippet.json", "w", encoding="utf-8") as f:
    json.dump(EXERCISES_CH3, f, ensure_ascii=False, indent=2)

with open("js/interactive_ch03_snippet.json", "w", encoding="utf-8") as f:
    json.dump(INTERACTIVE_CH3, f, ensure_ascii=False, indent=2)

print("Generated exercises and interactive snippets for Chapter 3 successfully!")
