# -*- coding: utf-8 -*-
"""
Build Chapter 4 Exercises and Interactive Workspaces.
Based on Deitel & Deitel Chapter 4 (p. 178-181)
"""

import json

EXERCISES_CH4 = [
    # 4.1
    {
        "id": "4.1",
        "category": "self-review",
        "title": "Self-Review 4.1: Điền vào chỗ trống các khái niệm nền tảng OOP C#",
        "description": "Củng cố các khái niệm cốt lõi: lớp, đối tượng, từ khóa, bổ từ truy cập và kiểu tiền tệ decimal.",
        "question": "Điền từ hoặc cụm từ thích hợp vào chỗ trống trong các phát biểu sau:\n"
                    "a) Ký tự định dạng _______ được sử dụng để hiển thị các giá trị số dưới định dạng tiền tệ (monetary format).\n"
                    "b) Mọi khai báo lớp đều bắt đầu bằng từ khóa _______ theo sau ngay là tên của lớp.\n"
                    "c) Toán tử _______ tạo ra một đối tượng của lớp được chỉ định ở bên phải từ khóa.\n"
                    "d) Mỗi tham số trong danh sách tham số của phương thức phải chỉ định cả _______ và _______.\n"
                    "e) Kiểu trả về _______ biểu thị rằng phương thức sẽ không trả về bất kỳ dữ liệu nào khi hoàn tất nhiệm vụ.\n"
                    "f) Khi mỗi đối tượng của một lớp duy trì bản sao dữ liệu riêng của một thuộc tính, thuộc tính đó được gọi là một _______.\n"
                    "g) Đối với một _______, trình biên dịch C# tự động sinh ra một biến thể hiện private ẩn cùng các bộ truy cập set và get.\n"
                    "h) Các biến thuộc kiểu dữ liệu _______ thường được sử dụng chuyên dụng để biểu diễn các số tiền trong tài chính.\n"
                    "i) Phương thức _______ của kiểu decimal chuyển đổi một chuỗi văn bản thành một giá trị kiểu decimal.\n"
                    "j) Từ khóa public là một _______ (quy định phạm vi truy cập).",
        "solution": "Đáp án chuẩn mực theo Giáo trình Deitel (trang 179):\n\n"
                    "a) **C** (Ký tự định dạng tiền tệ Currency).\n"
                    "b) **class** (từ khóa khai báo lớp).\n"
                    "c) **new** (toán tử cấp phát bộ nhớ trên Heap và khởi tạo đối tượng).\n"
                    "d) **type** (kiểu dữ liệu) và **name** (tên tham số).\n"
                    "e) **void** (kiểu không trả về giá trị).\n"
                    "f) **instance variable** (biến thể hiện / trường dữ liệu field).\n"
                    "g) **auto-implemented property** (thuộc tính tự động `{ get; set; }`).\n"
                    "h) **decimal** (kiểu số thực 128-bit độ chính xác cao 28-29 chữ số).\n"
                    "i) **Parse** (phương thức `decimal.Parse`).\n"
                    "j) **access modifier** (bổ từ truy cập / công cụ sửa đổi phạm vi).",
        "hints": "Xem lại Mục 4.2 đến 4.9 trong giáo trình Deitel: cấu trúc lớp Account, toán tử new, auto-properties và kiểu decimal.",
        "image": "images/fig4_03_uml_account.png"
    },
    # 4.2
    {
        "id": "4.2",
        "category": "self-review",
        "title": "Self-Review 4.2: Nhận định Đúng / Sai và phân tích kỹ thuật",
        "description": "Kiểm tra sự thấu hiểu về quy ước đặt tên, cơ chế thuộc tính, khởi tạo biến và phạm vi truy cập trong C#.",
        "question": "Xác định các phát biểu sau là Đúng (True) hay Sai (False). Nếu Sai, hãy giải thích rõ lý do kỹ thuật:\n"
                    "a) Theo quy ước, tên phương thức bắt đầu bằng chữ cái thường và các từ tiếp theo viết hoa chữ cái đầu.\n"
                    "b) Bộ truy cập get của một thuộc tính cho phép phía client sửa đổi giá trị của biến thể hiện tương ứng.\n"
                    "c) Tất cả các biến thể hiện đều được khởi tạo mặc định là null.\n"
                    "d) Cặp ngoặc đơn rỗng () theo sau tên phương thức biểu thị phương thức đó không yêu cầu bất kỳ tham số nào.\n"
                    "e) Số lượng đối số trong lời gọi phương thức bắt buộc phải khớp với số lượng tham số trong khai báo phương thức.\n"
                    "f) Các biến hoặc phương thức được khai báo với bổ từ private chỉ có thể truy cập bởi các thành viên trong cùng lớp.\n"
                    "g) Các biến được khai báo trong thân của một phương thức cụ thể được gọi là biến thể hiện và dùng được ở mọi nơi trong lớp.\n"
                    "h) Một khai báo thuộc tính bắt buộc phải chứa cả hai bộ truy cập get và set.\n"
                    "i) Thân của mọi phương thức hoặc thuộc tính đều được bao bọc bởi cặp ngoặc nhọn mở và đóng { }.\n"
                    "j) Các biến cục bộ được tự động khởi tạo giá trị mặc định khi khai báo.",
        "solution": "Phân tích và lời giải chuẩn mực theo Giáo trình Deitel (trang 179):\n\n"
                    "a) **False (Sai)**. Theo quy ước chuẩn C#, tên phương thức sử dụng PascalCase: viết hoa chữ cái đầu tiên của mọi từ cấu thành (ví dụ: `SetName`, `DisplayAccount`).\n"
                    "b) **False (Sai)**. Bộ truy cập `get` dùng để ĐỌC (retrieve) giá trị; bộ truy cập `set` mới cho phép SỬA ĐỔI (modify) giá trị.\n"
                    "c) **False (Sai)**. Biến thể hiện kiểu số được khởi tạo là `0`, kiểu `bool` là `false`, chỉ có các kiểu tham chiếu (reference types) mới khởi tạo là `null`.\n"
                    "d) **True (Đúng)**. Cặp ngoặc đơn rỗng `()` chỉ ra phương thức không nhận tham số đầu vào.\n"
                    "e) **True (Đúng)**. Số lượng và kiểu của đối số phải tương thích hoàn toàn với danh sách tham số.\n"
                    "f) **True (Đúng)**. Bổ từ `private` bảo toàn nguyên lý đóng gói (Encapsulation), ngăn chặn truy cập trực tiếp từ bên ngoài.\n"
                    "g) **False (Sai)**. Các biến khai báo trong thân phương thức là Biến cục bộ (Local Variables) và chỉ tồn tại trong nội bộ phương thức đó.\n"
                    "h) **False (Sai)**. Thuộc tính có thể chỉ có `get` (chỉ đọc - read-only), chỉ có `set` (chỉ ghi), hoặc kết hợp `private set`.\n"
                    "i) **True (Đúng)**. Cặp ngoặc nhọn `{ }` phân định khối mã lệnh (block).\n"
                    "j) **False (Sai)**. Biến thể hiện mới được khởi tạo mặc định; biến cục bộ KHÔNG có giá trị mặc định và C# báo lỗi biên dịch nếu đọc biến cục bộ chưa gán giá trị.",
        "hints": "Phân biệt PascalCase vs camelCase, chức năng get/set, giá trị mặc định của biến thể hiện vs biến cục bộ.",
        "image": "images/fig4_04_conceptual_object.png"
    },
    # 4.3
    {
        "id": "4.3",
        "category": "self-review",
        "title": "Self-Review 4.3: Phân biệt Biến cục bộ (Local Variables) vs Biến thể hiện (Instance Variables)",
        "description": "Phân tích chuyên sâu về vòng đời, vị trí khai báo, phạm vi hoạt động và cơ chế khởi tạo ô nhớ trong RAM.",
        "question": "Trình bày sự khác biệt căn bản giữa một Biến cục bộ (Local Variable) và một Biến thể hiện (Instance Variable) trên 4 phương diện kỹ thuật:\n"
                    "1) Vị trí khai báo trong tệp mã nguồn C#.\n"
                    "2) Phạm vi hoạt động (Scope) và khả năng nhìn thấy (Visibility).\n"
                    "3) Vòng đời sinh mệnh (Lifetime) và phân vùng bộ nhớ (Stack vs Heap).\n"
                    "4) Cơ chế gán giá trị mặc định (Default Initialization).",
        "solution": "Phân tích chuẩn mực theo Giáo trình Deitel (trang 179 - Mục 4.4.3):\n\n"
                    "1) **Vị trí khai báo:**\n"
                    "   - *Biến thể hiện:* Được khai báo trong thân lớp, bên ngoài mọi phương thức (thường có bổ từ `private`).\n"
                    "   - *Biến cục bộ:* Được khai báo bên trong thân của một phương thức cụ thể hoặc trong danh sách tham số của hàm.\n\n"
                    "2) **Phạm vi hoạt động:**\n"
                    "   - *Biến thể hiện:* Có thể được truy cập bởi toàn bộ các phương thức bên trong lớp đó.\n"
                    "   - *Biến cục bộ:* Chỉ tồn tại và được nhìn thấy duy nhất trong khối lệnh `{ }` bao bọc nó.\n\n"
                    "3) **Vòng đời & Bộ nhớ:**\n"
                    "   - *Biến thể hiện:* Được cấp phát trên Managed Heap cùng với đối tượng khi gọi toán tử `new`, tồn tại chừng nào đối tượng còn được tham chiếu.\n"
                    "   - *Biến cục bộ:* Được cấp phát trên Stack khi phương thức được gọi, và lập tức bị xóa sổ khỏi bộ nhớ khi phương thức kết thúc.\n\n"
                    "4) **Giá trị mặc định:**\n"
                    "   - *Biến thể hiện:* Được C# tự động khởi tạo mặc định (`0` cho số, `false` cho boolean, `null` cho tham chiếu).\n"
                    "   - *Biến cục bộ:* Không có giá trị mặc định; nếu cố tình đọc biến cục bộ chưa gán, trình biên dịch C# sẽ báo lỗi CS0165 ngay lập tức.",
        "hints": "Vẽ bảng so sánh 4 tiêu chí: Vị trí, Phạm vi (Scope), Vùng nhớ (Heap vs Stack), Giá trị mặc định.",
        "image": "images/fig4_02_account_class.png"
    },
    # 4.4
    {
        "id": "4.4",
        "category": "self-review",
        "title": "Self-Review 4.4: Bản chất của Tham số Phương thức: Parameter vs Argument",
        "description": "Làm rõ vai trò truyền dữ liệu vào phương thức và phân biệt rạch ròi giữa Tham số hình thức và Đối số thực tế.",
        "question": "Giải thích mục đích của Tham số phương thức (Method Parameter). Điểm khác biệt bản chất giữa Tham số (Parameter) và Đối số (Argument) là gì?",
        "solution": "Phân tích chuẩn mực theo Giáo trình Deitel (trang 179 - Mục 4.4.1):\n\n"
                    "1) **Mục đích của Tham số:**\n"
                    "   - Cho phép phương thức tiếp nhận dữ liệu đầu vào từ nơi gọi để thực hiện nhiệm vụ được giao.\n"
                    "   - Giúp phương thức trở nên tổng quát, linh hoạt và tái sử dụng được với các tập dữ liệu khác nhau.\n\n"
                    "2) **Phân biệt Parameter vs Argument:**\n"
                    "   - **Tham số (Parameter / Formal Parameter):** Là biến được khai báo trong phần đầu (header) của phương thức (ví dụ: `accountName` trong `public void SetName(string accountName)`).\n"
                    "   - **Đối số (Argument / Actual Argument):** Là giá trị thực tế hoặc biểu thức được truyền vào phương thức khi thực hiện lời gọi hàm (ví dụ: `theName` trong `myAccount.SetName(theName)`). Khi hàm chạy, giá trị của đối số được sao chép vào cho tham số sử dụng.",
        "hints": "Tham số là biến khai báo ở định nghĩa hàm; đối số là giá trị thực tế truyền vào khi gọi hàm.",
        "image": "images/fig4_01_accounttest_app.png"
    },
    # 4.5
    {
        "id": "4.5",
        "category": "exercise",
        "title": "Exercise 4.5: Mục đích của Hàm tạo (Constructor) trong Lập trình Hướng đối tượng",
        "description": "Phân tích vai trò của Constructor trong việc bảo toàn trạng thái hợp lệ của đối tượng ngay khi khai sinh.",
        "question": "Mục đích của Hàm tạo (Constructor) là gì? Tại sao Hàm tạo trong C# không bao giờ có kiểu dữ liệu trả về?",
        "solution": "Lời giải kỹ thuật theo Giáo trình Deitel (trang 180 - Mục 4.8):\n\n"
                    "1) **Mục đích của Constructor:**\n"
                    "   - Khởi tạo trạng thái ban đầu hợp lệ cho các biến thể hiện của đối tượng ngay khi đối tượng được sinh ra bằng toán tử `new`.\n"
                    "   - Ngăn chặn việc đối tượng rơi vào trạng thái rỗng hoặc dữ liệu rác không nhất quán (inconsistent state).\n"
                    "   - Thực hiện các thiết lập cần thiết (như mở kết nối, cấp phát tài nguyên) trước khi đối tượng phục vụ các yêu cầu tác vụ.\n\n"
                    "2) **Tại sao Constructor không có kiểu trả về:**\n"
                    "   - Constructor không phải là một phương thức thông thường. Nhiệm vụ của nó là cấu hình vùng nhớ đối tượng vừa được toán tử `new` cấp phát trên Heap.\n"
                    "   - Toán tử `new` luôn tự động trả về một tham chiếu (reference) trỏ tới đối tượng mới được tạo; do đó constructor không cần và không được phép chỉ định bất kỳ kiểu trả về nào (kể cả `void`).",
        "hints": "Constructor đảm bảo đối tượng sinh ra ở trạng thái hợp lệ; toán tử new đã đảm nhận việc trả về tham chiếu đối tượng.",
        "image": "images/fig4_08_account_constructor.png"
    },
    # 4.6
    {
        "id": "4.6",
        "category": "exercise",
        "title": "Exercise 4.6: Cơ chế Cấp phát Đối tượng: Toán tử new và Kiểu Giá trị",
        "description": "Khảo sát cơ chế cấp phát bộ nhớ của C# đối với Kiểu Tham chiếu và Kiểu Giá trị.",
        "question": "Giải thích cách một chương trình C# cấp phát bộ nhớ cho các biến thuộc Kiểu Giá trị (Value Types) so với Kiểu Tham chiếu (Reference Types) tạo bằng new.",
        "solution": "Phân tích bộ nhớ theo Giáo trình Deitel (Mục 4.3.2):\n\n"
                    "1) **Kiểu Giá trị (Value Types - int, double, bool, struct):**\n"
                    "   - Được cấp phát trực tiếp trên ngăn xếp **Stack** khi khai báo (ví dụ: `int x = 10;`).\n"
                    "   - Ô nhớ của biến chứa trực tiếp dữ liệu thô, không cần gọi toán tử `new` (trừ một số trường hợp khởi tạo struct).\n"
                    "   - Khi gán biến này cho biến khác, hệ thống sao chép toàn bộ giá trị nhị phân độc lập.\n\n"
                    "2) **Kiểu Tham chiếu (Reference Types - class, string, array):**\n"
                    "   - Bắt buộc phải dùng toán tử `new` để máy ảo CLR cấp phát vùng nhớ trên **Managed Heap** chứa dữ liệu đối tượng.\n"
                    "   - Biến tham chiếu trên Stack chỉ lưu địa chỉ trỏ tới đối tượng trên Heap. Nếu chưa gọi `new`, biến mang giá trị `null`.",
        "hints": "So sánh Stack (lưu giá trị trực tiếp) và Heap (cấp phát bởi new, biến chỉ giữ tham chiếu địa chỉ).",
        "image": "images/fig4_04_conceptual_object.png"
    },
    # 4.7
    {
        "id": "4.7",
        "category": "exercise",
        "title": "Exercise 4.7: Hàm tạo Mặc định (Default Constructor) và Quy tắc Thu hồi của C#",
        "description": "Hiểu rõ cơ chế tự động cung cấp và tự động loại bỏ Default Constructor của trình biên dịch C#.",
        "question": "Hàm tạo mặc định (Default Constructor) là gì? Điều gì sẽ xảy ra với hàm tạo mặc định khi bạn tự định nghĩa một hàm tạo có tham số trong lớp?",
        "solution": "Lời giải chuẩn xác theo Giáo trình Deitel (Mục 4.8.2):\n\n"
                    "1) **Định nghĩa:**\n"
                    "   - Hàm tạo mặc định là constructor công khai không có tham số (`public ClassName()`), có thân hàm rỗng, do trình biên dịch C# tự động tạo ra cho một lớp nếu lớp đó không có bất kỳ constructor nào.\n"
                    "   - Nó khởi tạo các biến thể hiện về giá trị mặc định của hệ thống (`0`, `false`, `null`).\n\n"
                    "2) **Quy tắc thu hồi:**\n"
                    "   - Một khi lập trình viên đã tự tay khai báo BẤT KỲ một constructor nào (dù có 1 hay nhiều tham số), trình biên dịch C# sẽ **LẬP TỨC THU HỒI VÀ KHÔNG SINH RA** hàm tạo mặc định nữa!\n"
                    "   - Khi đó, nếu phía client cố tình gọi `new ClassName()` mà không truyền tham số, chương trình sẽ báo lỗi biên dịch **CS7036: There is no argument given that corresponds to the required parameter**.\n"
                    "   - Muốn vừa gọi được constructor có tham số, vừa gọi được không tham số, lập trình viên bắt buộc phải tự tay viết cả hai constructor (Constructor Overloading).",
        "hints": "Nhớ nguyên tắc: Có constructor tự viết -> C# xóa default constructor; muốn dùng cả hai phải tự overload.",
        "image": "images/fig4_10_uml_constructor.png"
    },
    # 4.8
    {
        "id": "4.8",
        "category": "exercise",
        "title": "Exercise 4.8: Ưu điểm của Thuộc tính (Properties) trong C# so với C++ và Java",
        "description": "So sánh thiết kế ngôn ngữ C# Properties với các phương thức getter/setter truyền thống.",
        "question": "Mục đích của các bộ truy cập get và set trong Thuộc tính C# là gì? Thuộc tính C# mang lại ưu điểm vượt trội nào về cú pháp so với các phương thức get/set của Java hoặc C++?",
        "solution": "Phân tích theo Giáo trình Deitel (Mục 4.6):\n\n"
                    "1) **Mục đích của get và set:**\n"
                    "   - Bộ truy cập `get`: Thực thi khi client đọc thuộc tính, trả về giá trị biến thể hiện hoặc kết quả tính toán.\n"
                    "   - Bộ truy cập `set`: Thực thi khi client gán dữ liệu cho thuộc tính, sử dụng từ khóa ngữ cảnh `value` để nhận giá trị mới và có thể thực hiện kiểm tra tính hợp lệ (Data Validation).\n\n"
                    "2) **Ưu điểm vượt trội của C# Properties:**\n"
                    "   - **Cú pháp tự nhiên, thanh lịch:** Trong Java/C++, lập trình viên phải gọi hàm dài dòng: `account.setName(\"Jane\");` và `account.getName();`. Trong C#, ta viết hệt như thao tác với biến thông thường: `account.Name = \"Jane\";` và `Console.WriteLine(account.Name);`.\n"
                    "   - **Bảo toàn 100% nguyên lý đóng gói:** Mặc dù cú pháp nhìn như truy cập biến trực tiếp, nhưng bên dưới máy ảo vẫn thực thi mã lệnh của `get`/`set`, cho phép bảo vệ dữ liệu, kiểm tra hợp lệ hoặc chỉ cho phép đọc (`private set`).\n"
                    "   - **Hỗ trợ Auto-Properties:** Cú pháp `{ get; set; }` siêu ngắn gọn không cần khai báo backing field.",
        "hints": "Cú pháp tự nhiên như biến thô nhưng bên dưới vẫn chạy logic get/set an toàn; từ khóa ngữ cảnh value.",
        "image": "images/fig4_06_account_properties.png"
    },
    # 4.9
    {
        "id": "4.9",
        "category": "project",
        "title": "Exercise 4.9: Nâng cấp lớp Account với Phương thức Rút tiền Withdraw",
        "description": "Cài đặt phương thức Withdraw có cơ chế kiểm tra thấu chi tài khoản (overdraft protection) theo bài tập 4.9 giáo trình.",
        "question": "Nâng cấp lớp Account (Hình 4.11) để bổ sung phương thức Withdraw rút tiền từ tài khoản. Đảm bảo rằng số tiền rút không được vượt quá số dư hiện có. Nếu vượt quá, số dư không thay đổi và in ra thông báo: \"Withdrawal amount exceeded account balance.\". Nâng cấp tệp AccountTest (Hình 4.12) để kiểm thử phương thức Withdraw.",
        "solution": "Mã nguồn cài đặt phương thức Withdraw chuẩn mực:\n\n"
                    "```csharp\n"
                    "// Bo sung vao lop Account.cs\n"
                    "public void Withdraw(decimal withdrawalAmount)\n"
                    "{\n"
                    "   if (withdrawalAmount > 0.0m)\n"
                    "   {\n"
                    "      if (withdrawalAmount <= Balance)\n"
                    "      {\n"
                    "         Balance = Balance - withdrawalAmount; // Tru tien hop le\n"
                    "      }\n"
                    "      else\n"
                    "      {\n"
                    "         Console.WriteLine(\"Withdrawal amount exceeded account balance.\");\n"
                    "      }\n"
                    "   }\n"
                    "}\n"
                    "```",
        "hints": "Kiểm tra 2 điều kiện: số tiền rút phải dương, và withdrawalAmount <= Balance. Nếu lớn hơn thì in cảnh báo và không trừ tiền.",
        "image": "images/fig4_11_account_balance_p2.png"
    },
    # 4.10
    {
        "id": "4.10",
        "category": "project",
        "title": "Exercise 4.10: Thiết kế Lớp Quản lý Hồ sơ Sinh viên (Student Record Class)",
        "description": "Tạo lớp Student quản lý mã sinh viên, họ tên và điểm 3 môn học, kiểm tra điểm không âm, tính tổng và phần trăm.",
        "question": "Tạo lớp Student bao gồm: Id (string), Name (string), và điểm 3 môn thi: Score1, Score2, Score3 (decimal). Cung cấp Constructor khởi tạo 5 giá trị. Thuộc tính cho điểm số phải kiểm tra: nếu giá trị gán là số âm thì giữ nguyên điểm cũ. Xây dựng hai phương thức GetAggregate() tính tổng điểm 3 môn, và GetPercentage() tính tỷ lệ phần trăm (tổng / 50 * 100). Viết chương trình StudentRecordTest kiểm thử toàn bộ tính năng.",
        "solution": "Mã nguồn lớp Student.cs chuẩn mực:\n\n"
                    "```csharp\n"
                    "public class Student\n"
                    "{\n"
                    "   public string Id { get; set; }\n"
                    "   public string Name { get; set; }\n"
                    "   private decimal score1;\n"
                    "   private decimal score2;\n"
                    "   private decimal score3;\n\n"
                    "   public Student(string id, string name, decimal s1, decimal s2, decimal s3)\n"
                    "   {\n"
                    "      Id = id;\n"
                    "      Name = name;\n"
                    "      Score1 = s1;\n"
                    "      Score2 = s2;\n"
                    "      Score3 = s3;\n"
                    "   }\n\n"
                    "   public decimal Score1\n"
                    "   {\n"
                    "      get { return score1; }\n"
                    "      set { if (value >= 0.0m) score1 = value; }\n"
                    "   }\n\n"
                    "   public decimal Score2\n"
                    "   {\n"
                    "      get { return score2; }\n"
                    "      set { if (value >= 0.0m) score2 = value; }\n"
                    "   }\n\n"
                    "   public decimal Score3\n"
                    "   {\n"
                    "      get { return score3; }\n"
                    "      set { if (value >= 0.0m) score3 = value; }\n"
                    "   }\n\n"
                    "   public decimal GetAggregate() => Score1 + Score2 + Score3;\n"
                    "   public decimal GetPercentage() => (GetAggregate() / 50.0m) * 100.0m;\n"
                    "}\n"
                    "```",
        "hints": "Sử dụng backing field cho 3 điểm thi để validate value >= 0.0m trong bộ truy cập set; phương thức tính toán trả về decimal.",
        "image": "images/fig4_14_uml_balance.png"
    },
    # 4.11
    {
        "id": "4.11",
        "category": "project",
        "title": "Exercise 4.11: Thiết kế Lớp Quản lý Tài sản Doanh nghiệp (Asset Class)",
        "description": "Tạo lớp Asset gồm tên tài sản, giá trị và tỷ lệ khấu hao, kiểm tra dữ liệu không âm, tính giá trị sau khấu hao.",
        "question": "Tạo lớp Asset gồm: AssetName (string), AssetValue (decimal), DepreciationRate (decimal - tỷ lệ khấu hao từ 0.0 đến 1.0). Constructor khởi tạo 3 giá trị. Validation: nếu giá trị hoặc tỷ lệ khấu hao âm thì giữ nguyên giá trị cũ. Viết ứng dụng AssetTest tạo 2 tài sản, hiển thị số tiền khấu hao và giá trị còn lại, sau đó tăng giá trị tài sản thêm 5% và hiển thị lại.",
        "solution": "Mã nguồn lớp Asset.cs chuẩn mực:\n\n"
                    "```csharp\n"
                    "public class Asset\n"
                    "{\n"
                    "   public string AssetName { get; set; }\n"
                    "   private decimal assetValue;\n"
                    "   private decimal depreciationRate;\n\n"
                    "   public Asset(string name, decimal val, decimal rate)\n"
                    "   {\n"
                    "      AssetName = name;\n"
                    "      AssetValue = val;\n"
                    "      DepreciationRate = rate;\n"
                    "   }\n\n"
                    "   public decimal AssetValue\n"
                    "   {\n"
                    "      get => assetValue;\n"
                    "      set { if (value >= 0.0m) assetValue = value; }\n"
                    "   }\n\n"
                    "   public decimal DepreciationRate\n"
                    "   {\n"
                    "      get => depreciationRate;\n"
                    "      set { if (value >= 0.0m && value <= 1.0m) depreciationRate = value; }\n"
                    "   }\n\n"
                    "   public decimal GetDepreciationAmount() => AssetValue * DepreciationRate;\n"
                    "   public decimal GetDepreciatedValue() => AssetValue - GetDepreciationAmount();\n"
                    "}\n"
                    "```",
        "hints": "Data validation trong set accessor; phương thức tính khấu hao = AssetValue * DepreciationRate.",
        "image": "images/fig4_13_format_specifiers.png"
    },
    # 4.12
    {
        "id": "4.12",
        "category": "project",
        "title": "Exercise 4.12: Thiết kế Lớp Coaching với Auto-Implemented Properties",
        "description": "Áp dụng thuộc tính tự động để thiết kế lớp đào tạo học phần ngắn gọn và thanh lịch.",
        "question": "Tạo lớp Coaching bao gồm 4 thuộc tính tự động: CourseName (string), InstructorName (string), TuitionFee (decimal), DurationWeeks (int). Viết Constructor và chương trình kiểm thử CoachingTest hiển thị thông tin học phần với định dạng học phí tiền tệ chuẩn :C.",
        "solution": "Mã nguồn lớp Coaching.cs sử dụng Auto-Properties:\n\n"
                    "```csharp\n"
                    "public class Coaching\n"
                    "{\n"
                    "   public string CourseName { get; set; }\n"
                    "   public string InstructorName { get; set; }\n"
                    "   public decimal TuitionFee { get; set; }\n"
                    "   public int DurationWeeks { get; set; }\n\n"
                    "   public Coaching(string course, string instructor, decimal fee, int weeks)\n"
                    "   {\n"
                    "      CourseName = course;\n"
                    "      InstructorName = instructor;\n"
                    "      TuitionFee = fee;\n"
                    "      DurationWeeks = weeks;\n"
                    "   }\n"
                    "}\n"
                    "```",
        "hints": "Sử dụng cú pháp { get; set; } cho cả 4 thuộc tính để mã nguồn ngắn gọn tối đa.",
        "image": "images/fig4_07_uml_properties.png"
    },
    # 4.13
    {
        "id": "4.13",
        "category": "project",
        "title": "Exercise 4.13: Tái cấu trúc Mã nguồn: Phương thức Dùng chung DisplayAccount (DRY)",
        "description": "Áp dụng nguyên lý Don't Repeat Yourself để loại bỏ mã in tài khoản lặp lại 4 lần trong AccountTest.",
        "question": "Trong tệp AccountTest.cs (Hình 4.12), câu lệnh hiển thị tên và số dư tài khoản bị lặp lại nhiều lần. Khai báo phương thức tĩnh DisplayAccount nhận vào tham số là một đối tượng Account và in thông tin định dạng :C. Thay thế tất cả các câu lệnh in lặp trong Main bằng lời gọi đến DisplayAccount.",
        "solution": "Phương thức tĩnh DisplayAccount chuẩn mực theo Exercise 4.13 Deitel:\n\n"
                    "```csharp\n"
                    "public static void DisplayAccount(Account accountToDisplay)\n"
                    "{\n"
                    "   Console.WriteLine($\"{accountToDisplay.Name}'s balance: {accountToDisplay.Balance:C}\");\n"
                    "}\n\n"
                    "// Trong Main, thay vi lap lai Console.WriteLine, ta goi:\n"
                    "DisplayAccount(account1);\n"
                    "DisplayAccount(account2);\n"
                    "```",
        "hints": "Phương thức static nhận đối số kiểu Account; sử dụng string interpolation với định dạng :C.",
        "image": "images/fig4_12_accounttest_balance_p1.png"
    },
    # 4.14
    {
        "id": "4.14",
        "category": "making-a-difference",
        "title": "Exercise 4.14: Ứng dụng Y tế Số: Bộ Tính Nhịp Tim Mục Tiêu (HeartRates Calculator)",
        "description": "Xây dựng ứng dụng y tế số tính tuổi, nhịp tim tối đa và dải nhịp tim mục tiêu theo khuyến cáo của Hiệp hội Tim mạch Hoa Kỳ (AHA).",
        "question": "Theo AHA, nhịp tim tối đa = 220 - tuổi. Dải nhịp tim mục tiêu an toàn khi tập thể thao là từ 50% đến 85% nhịp tim tối đa. Tạo lớp HeartRates gồm: FirstName, LastName, BirthYear, CurrentYear. Constructor nhận dữ liệu này. Cung cấp các thuộc tính tính: Tuổi (Age), Nhịp tim tối đa (MaxHeartRate), Nhịp tim mục tiêu tối thiểu (MinTargetRate = 50%) và tối đa (MaxTargetRate = 85%). Viết app kiểm thử nhập thông tin và in kết quả sức khỏe.",
        "solution": "Mã nguồn lớp HeartRates.cs y tế số:\n\n"
                    "```csharp\n"
                    "public class HeartRates\n"
                    "{\n"
                    "   public string FirstName { get; set; }\n"
                    "   public string LastName { get; set; }\n"
                    "   public int BirthYear { get; set; }\n"
                    "   public int CurrentYear { get; set; }\n\n"
                    "   public HeartRates(string firstName, string lastName, int birthYear, int currentYear)\n"
                    "   {\n"
                    "      FirstName = firstName;\n"
                    "      LastName = lastName;\n"
                    "      BirthYear = birthYear;\n"
                    "      CurrentYear = currentYear;\n"
                    "   }\n\n"
                    "   public int Age => CurrentYear - BirthYear;\n"
                    "   public int MaxHeartRate => 220 - Age;\n"
                    "   public double MinTargetRate => MaxHeartRate * 0.50;\n"
                    "   public double MaxTargetRate => MaxHeartRate * 0.85;\n"
                    "}\n"
                    "```",
        "hints": "Sử dụng expression-bodied properties (=>) để tính tuổi và dải nhịp tim mục tiêu 50%-85%.",
        "image": "images/fig4_13_format_specifiers.png"
    },
    # 4.15
    {
        "id": "4.15",
        "category": "making-a-difference",
        "title": "Exercise 4.15: Số hóa Hồ sơ Sức khỏe Cá nhân (Computerization of Health Records - HealthProfile)",
        "description": "Thiết kế hồ sơ sức khỏe điện tử EHR hoàn chỉnh tính BMI, tuổi, nhịp tim mục tiêu và phân loại thể trạng y tế.",
        "question": "Tạo lớp HealthProfile bao gồm: Họ tên, Giới tính, Ngày tháng năm sinh, Chiều cao (cm) và Cân nặng (kg). Xây dựng các phương thức/thuộc tính tính: Tuổi, Nhịp tim tối đa, Dải nhịp tim mục tiêu, và Chỉ số khối cơ thể BMI = weight / (heightInMeters * heightInMeters). Hiển thị bảng phân loại chuẩn WHO: Gầy (< 18.5), Bình thường (18.5-24.9), Thừa cân (25-29.9), Béo phì (>= 30).",
        "solution": "Mã nguồn lớp HealthProfile.cs chuẩn y tế quốc tế:\n\n"
                    "```csharp\n"
                    "public class HealthProfile\n"
                    "{\n"
                    "   public string Name { get; set; }\n"
                    "   public string Gender { get; set; }\n"
                    "   public int BirthYear { get; set; }\n"
                    "   public int CurrentYear { get; set; }\n"
                    "   public double HeightCm { get; set; }\n"
                    "   public double WeightKg { get; set; }\n\n"
                    "   public HealthProfile(string name, string gender, int birthYear, int currentYear, double height, double weight)\n"
                    "   {\n"
                    "      Name = name;\n"
                    "      Gender = gender;\n"
                    "      BirthYear = birthYear;\n"
                    "      CurrentYear = currentYear;\n"
                    "      HeightCm = height;\n"
                    "      WeightKg = weight;\n"
                    "   }\n\n"
                    "   public int Age => CurrentYear - BirthYear;\n"
                    "   public int MaxHeartRate => 220 - Age;\n"
                    "   public double BMI\n"
                    "   {\n"
                    "      get\n"
                    "      {\n"
                    "         double heightM = HeightCm / 100.0;\n"
                    "         return WeightKg / (heightM * heightM);\n"
                    "      }\n"
                    "   }\n"
                    "}\n"
                    "```",
        "hints": "Tính chiều cao ra mét (HeightCm / 100.0) trước khi tính BMI; kết hợp với công thức nhịp tim AHA.",
        "image": "images/fig4_13_format_specifiers.png"
    }
]

# Interactive Workspace Data for Chapter 4
INTERACTIVE_CH4 = {
    "4.1": {
        "mode": "fill-blank",
        "title": "Self-Review 4.1: Điền vào chỗ trống các khái niệm nền tảng OOP C#",
        "items": [
            {
                "id": "a",
                "label": "a)",
                "prefix": "Ký tự định dạng",
                "suffix": "được sử dụng để hiển thị các giá trị số dưới định dạng tiền tệ quốc tế (Currency).",
                "acceptable": ["c", "c format specifier", ":c", "ky tu c", "ký tự c", "currency"],
                "correctAnswer": "C (hoặc :C) - định dạng tiền tệ Currency",
                "explanation": "Mục 4.9.2: Ký tự định dạng C hiển thị số theo tiền tệ chuẩn kèm 2 chữ số thập phân."
            },
            {
                "id": "b",
                "label": "b)",
                "prefix": "Mọi khai báo lớp đều bắt đầu bằng từ khóa",
                "suffix": "theo sau ngay là tên của lớp.",
                "acceptable": ["class", "tu khoa class", "từ khóa class"],
                "correctAnswer": "class (từ khóa khai báo lớp)",
                "explanation": "Mục 4.3: Từ khóa class là bắt buộc để bắt đầu định nghĩa một lớp đối tượng trong C#."
            },
            {
                "id": "c",
                "label": "c)",
                "prefix": "Toán tử",
                "suffix": "tạo ra một đối tượng của lớp được chỉ định ở bên phải từ khóa trên Managed Heap.",
                "acceptable": ["new", "toan tu new", "toán tử new"],
                "correctAnswer": "new (toán tử khởi tạo đối tượng)",
                "explanation": "Mục 4.3.1: Toán tử new cấp phát bộ nhớ trên Heap và gọi constructor của lớp."
            },
            {
                "id": "d1",
                "label": "d1)",
                "prefix": "Mỗi tham số trong phương thức phải chỉ định cả",
                "suffix": "(ví dụ: string, int) và tên tham số.",
                "acceptable": ["type", "kieu du lieu", "kiểu dữ liệu", "kieu", "kiểu"],
                "correctAnswer": "type (kiểu dữ liệu)",
                "explanation": "Mục 4.4.1: Mỗi tham số bắt buộc phải có kiểu dữ liệu (type) và tên tham số (name)."
            },
            {
                "id": "d2",
                "label": "d2)",
                "prefix": "Mỗi tham số trong phương thức phải chỉ định cả kiểu dữ liệu và",
                "suffix": "(tên định danh của tham số).",
                "acceptable": ["name", "ten", "tên", "ten tham so", "tên tham số"],
                "correctAnswer": "name (tên tham số)",
                "explanation": "Mục 4.4.1: Tên tham số dùng để nhận giá trị đối số truyền vào."
            },
            {
                "id": "e",
                "label": "e)",
                "prefix": "Kiểu trả về",
                "suffix": "biểu thị rằng phương thức sẽ không trả về bất kỳ dữ liệu nào khi hoàn tất nhiệm vụ.",
                "acceptable": ["void", "tu khoa void", "từ khóa void"],
                "correctAnswer": "void (không trả về giá trị)",
                "explanation": "Mục 4.4.1: Kiểu void chỉ ra phương thức chỉ thực hiện hành động chứ không sinh kết quả trả về."
            },
            {
                "id": "f",
                "label": "f)",
                "prefix": "Khi mỗi đối tượng của một lớp duy trì bản sao dữ liệu riêng của một thuộc tính, nó được gọi là một",
                "suffix": "(Field).",
                "acceptable": ["instance variable", "bien the hien", "biến thể hiện", "field", "truong du lieu", "trường dữ liệu"],
                "correctAnswer": "instance variable (biến thể hiện / field)",
                "explanation": "Mục 4.4: Biến thể hiện thuộc về từng đối tượng cụ thể được tạo ra từ lớp."
            },
            {
                "id": "g",
                "label": "g)",
                "prefix": "Đối với một",
                "suffix": ", trình biên dịch C# tự động sinh ra một biến thể hiện private ẩn cùng các bộ get/set.",
                "acceptable": ["auto-implemented property", "auto implemented property", "thuoc tinh tu dong", "thuộc tính tự động", "auto property", "auto-property"],
                "correctAnswer": "auto-implemented property (thuộc tính tự động)",
                "explanation": "Mục 4.7: Cú pháp { get; set; } giúp C# tự động tạo backing field và logic get/set."
            },
            {
                "id": "h",
                "label": "h)",
                "prefix": "Các biến thuộc kiểu dữ liệu 128-bit",
                "suffix": "thường được sử dụng chuyên dụng để biểu diễn các số tiền trong tài chính.",
                "acceptable": ["decimal", "kieu decimal", "kiểu decimal"],
                "correctAnswer": "decimal (kiểu số thực tài chính chính xác cao)",
                "explanation": "Mục 4.9: Kiểu decimal loại bỏ hoàn toàn sai số làm tròn nhị phân của double/float."
            },
            {
                "id": "i",
                "label": "i)",
                "prefix": "Phương thức",
                "suffix": "của kiểu decimal chuyển đổi một chuỗi văn bản thành một giá trị số kiểu decimal.",
                "acceptable": ["parse", "decimal.parse", "parse()", "decimal.parse()"],
                "correctAnswer": "Parse (decimal.Parse)",
                "explanation": "Mục 4.9.2: decimal.Parse() chuyển đổi chuỗi chuỗi ký tự thành số thực decimal."
            },
            {
                "id": "j",
                "label": "j)",
                "prefix": "Từ khóa public hoặc private được gọi là một",
                "suffix": "(quy định phạm vi truy cập).",
                "acceptable": ["access modifier", "bo tu truy cap", "bổ từ truy cập", "access specifier"],
                "correctAnswer": "access modifier (bổ từ truy cập)",
                "explanation": "Mục 4.4: Access modifiers kiểm soát quyền truy cập thành viên của lớp."
            }
        ]
    },
    "4.2": {
        "mode": "true-false",
        "title": "Self-Review 4.2: Nhận định Đúng / Sai và phân tích kỹ thuật",
        "items": [
            {
                "id": "a",
                "label": "a)",
                "statement": "Theo quy ước, tên phương thức trong C# bắt đầu bằng chữ cái thường và các từ tiếp theo viết hoa chữ cái đầu.",
                "correct": False,
                "explanation": "Sai (False). C# quy định tên phương thức dùng PascalCase: viết hoa chữ cái đầu tiên của mọi từ (ví dụ: SetName, GetName, Main)."
            },
            {
                "id": "b",
                "label": "b)",
                "statement": "Bộ truy cập get của một thuộc tính cho phép phía client sửa đổi giá trị của biến thể hiện tương ứng.",
                "correct": False,
                "explanation": "Sai (False). Bộ truy cập get dùng để ĐỌC dữ liệu; bộ truy cập set mới dùng để SỬA ĐỔI dữ liệu."
            },
            {
                "id": "c",
                "label": "c)",
                "statement": "Tất cả các biến thể hiện đều được khởi tạo mặc định là null.",
                "correct": False,
                "explanation": "Sai (False). Kiểu số nguyên int/decimal khởi tạo là 0, kiểu bool là false, chỉ kiểu tham chiếu mới khởi tạo là null."
            },
            {
                "id": "d",
                "label": "d)",
                "statement": "Cặp ngoặc đơn rỗng () theo sau tên phương thức biểu thị phương thức đó không yêu cầu bất kỳ tham số nào.",
                "correct": True,
                "explanation": "Đúng (True). Cặp ngoặc đơn rỗng () xác định danh sách tham số của phương thức là rỗng."
            },
            {
                "id": "e",
                "label": "e)",
                "statement": "Số lượng đối số trong lời gọi phương thức bắt buộc phải khớp với số lượng tham số trong khai báo phương thức.",
                "correct": True,
                "explanation": "Đúng (True). C# yêu cầu số lượng và kiểu của đối số phải tương thích với danh sách tham số."
            },
            {
                "id": "f",
                "label": "f)",
                "statement": "Các biến hoặc phương thức được khai báo với bổ từ private chỉ có thể truy cập bởi các thành viên trong cùng lớp.",
                "correct": True,
                "explanation": "Đúng (True). Đây là nguyên lý ẩn giấu thông tin (Information Hiding) và đóng gói trong OOP."
            },
            {
                "id": "g",
                "label": "g)",
                "statement": "Các biến được khai báo trong thân của một phương thức cụ thể được gọi là biến thể hiện và dùng được ở mọi nơi trong lớp.",
                "correct": False,
                "explanation": "Sai (False). Biến khai báo trong thân hàm là Biến cục bộ (Local Variable) và chỉ dùng được trong nội bộ hàm đó."
            },
            {
                "id": "h",
                "label": "h)",
                "statement": "Một khai báo thuộc tính bắt buộc phải chứa cả hai bộ truy cập get và set.",
                "correct": False,
                "explanation": "Sai (False). Thuộc tính có thể chỉ có get (read-only), chỉ có set, hoặc kết hợp private set."
            },
            {
                "id": "i",
                "label": "i)",
                "statement": "Thân của mọi phương thức hoặc thuộc tính đều được bao bọc bởi cặp ngoặc nhọn mở và đóng { }.",
                "correct": True,
                "explanation": "Đúng (True). Cặp ngoặc nhọn { } phân định khối mã lệnh (block) thực thi."
            },
            {
                "id": "j",
                "label": "j)",
                "statement": "Các biến cục bộ được tự động khởi tạo giá trị mặc định khi khai báo.",
                "correct": False,
                "explanation": "Sai (False). Chỉ có biến thể hiện mới được C# khởi tạo mặc định; biến cục bộ chưa gán giá trị sẽ gây lỗi biên dịch nếu đọc."
            }
        ]
    },
    "4.9": {
        "mode": "csharp-code",
        "title": "Exercise 4.9: Nâng cấp lớp Account với Phương thức Rút tiền Withdraw",
        "checklist": [
            { "id": "step1", "text": "Khai báo phương thức public void Withdraw(decimal withdrawalAmount) trong lớp Account" },
            { "id": "step2", "text": "Kiểm tra điều kiện withdrawalAmount > 0.0m để đảm bảo số tiền rút là số dương" },
            { "id": "step3", "text": "Kiểm tra withdrawalAmount <= Balance: nếu hợp lệ thì Balance = Balance - withdrawalAmount" },
            { "id": "step4", "text": "Nếu vượt quá số dư, in dòng thông báo: 'Withdrawal amount exceeded account balance.' và không đổi số dư" },
            { "id": "step5", "text": "Viết mã kiểm thử trong AccountTest thử rút tiền hợp lệ và thử rút thấu chi" }
        ],
        "codeKeywords": ["Withdraw", "decimal", "Balance", "Withdrawal amount exceeded account balance.", "Console.WriteLine"],
        "sampleCode": """public void Withdraw(decimal withdrawalAmount)
{
   if (withdrawalAmount > 0.0m)
   {
      if (withdrawalAmount <= Balance)
      {
         Balance = Balance - withdrawalAmount;
      }
      else
      {
         Console.WriteLine("Withdrawal amount exceeded account balance.");
      }
   }
}"""
    },
    "4.13": {
        "mode": "csharp-code",
        "title": "Exercise 4.13: Tái cấu trúc Mã nguồn: Phương thức Dùng chung DisplayAccount",
        "checklist": [
            { "id": "step1", "text": "Khai báo phương thức tĩnh public static void DisplayAccount(Account accountToDisplay)" },
            { "id": "step2", "text": "Sử dụng String Interpolation $ kết hợp định dạng tiền tệ :C để in tên và số dư" },
            { "id": "step3", "text": "Thay thế các dòng in tài khoản lặp đi lặp lại trong Main bằng lời gọi DisplayAccount(account1), DisplayAccount(account2)" },
            { "id": "step4", "text": "Chạy thử để kiểm tra kết quả in ra màn hình hoàn toàn trùng khớp với Hình 4.12" }
        ],
        "codeKeywords": ["DisplayAccount", "Account", "accountToDisplay", "Console.WriteLine", ":C", "Balance"],
        "sampleCode": """public static void DisplayAccount(Account accountToDisplay)
{
   Console.WriteLine($"{accountToDisplay.Name}'s balance: {accountToDisplay.Balance:C}");
}"""
    },
    "4.14": {
        "mode": "csharp-code",
        "title": "Exercise 4.14: Ứng dụng Y tế Số: Bộ Tính Nhịp Tim Mục Tiêu (HeartRates Calculator)",
        "checklist": [
            { "id": "step1", "text": "Khai báo các thuộc tính: FirstName, LastName, BirthYear, CurrentYear" },
            { "id": "step2", "text": "Xây dựng Constructor nhận 4 tham số khởi tạo đối tượng HeartRates" },
            { "id": "step3", "text": "Tính Tuổi: Age = CurrentYear - BirthYear" },
            { "id": "step4", "text": "Tính Nhịp tim tối đa theo AHA: MaxHeartRate = 220 - Age" },
            { "id": "step5", "text": "Tính Dải nhịp tim mục tiêu: 50% đến 85% nhịp tim tối đa" },
            { "id": "step6", "text": "Chạy thử kiểm tra nhập thông tin cá nhân và hiển thị dải nhịp tim an toàn" }
        ],
        "codeKeywords": ["HeartRates", "BirthYear", "CurrentYear", "Age", "MaxHeartRate", "220", "0.50", "0.85"],
        "sampleCode": """public class HeartRates
{
   public string FirstName { get; set; }
   public string LastName { get; set; }
   public int BirthYear { get; set; }
   public int CurrentYear { get; set; }

   public HeartRates(string fName, string lName, int bYear, int cYear)
   {
      FirstName = fName;
      LastName = lName;
      BirthYear = bYear;
      CurrentYear = cYear;
   }

   public int Age => CurrentYear - BirthYear;
   public int MaxHeartRate => 220 - Age;
   public double MinTargetRate => MaxHeartRate * 0.50;
   public double MaxTargetRate => MaxHeartRate * 0.85;
}"""
    }
}

with open(r"js\exercises_ch04_snippet.json", "w", encoding="utf-8") as f:
    json.dump(EXERCISES_CH4, f, ensure_ascii=False, indent=2)

with open(r"js\interactive_ch04_snippet.json", "w", encoding="utf-8") as f:
    json.dump(INTERACTIVE_CH4, f, ensure_ascii=False, indent=2)

print(f"Generated js/exercises_ch04_snippet.json ({len(EXERCISES_CH4)} exercises)")
print(f"Generated js/interactive_ch04_snippet.json ({len(INTERACTIVE_CH4)} interactive configs)")
