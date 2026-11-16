# -*- coding: utf-8 -*-
"""
Generate complete 45-slide pedagogical script for Chapter 3:
Thầy giáo (Người 1) & Đại diện sinh viên IT26M (Người 2).
"""

import json
import os

SCRIPTS_DATA = [
    (1, "KỸ THUẬT LẬP TRÌNH / C# - CHƯƠNG 3: LẬP TRÌNH ỨNG DỤNG C# CƠ BẢN",
     "Chào mừng tất cả các em sinh viên lớp IT26M Khóa 2026 đến với buổi học hôm nay! Chúng ta chính thức bước vào Chương 3: Lập trình Ứng dụng C# Cơ bản - Introduction to C# App Programming. Bài giảng được biên soạn chuẩn mực theo giáo trình quốc tế danh tiếng Visual C# How to Program của tác giả Deitel. Nếu như ở hai chương đầu, các em đã nắm vững bức tranh toàn cảnh về kiến trúc máy tính và làm quen với môi trường Visual Studio IDE, thì bắt đầu từ chương này, chúng ta sẽ bắt tay vào viết những dòng mã lệnh C# đầu tiên: từ ứng dụng dòng lệnh Console, kỹ thuật định dạng chuỗi, quản lý biến trong ô nhớ RAM, cho đến các toán tử số học và cấu trúc rẽ nhánh ra quyết định if.",
     "Dạ chào thầy! Cả lớp IT26M chúng em rất háo hức với bài học hôm nay ạ. Chúng em đều mong muốn hiểu rõ bản chất từng câu lệnh C# hoạt động như thế nào, làm sao để nhập xuất dữ liệu chuẩn xác và cách máy tính phân bổ ô nhớ khi khai báo biến. Chúng em đã mở sẵn Visual Studio và sẵn sàng thực hành cùng thầy ạ!"),

    (2, "Mục tiêu Bài học & Chuẩn đầu ra (CLOs)",
     "Để đảm bảo chất lượng đào tạo đại học chuẩn kiểm định quốc tế, bài học Chương 3 hướng tới 5 chuẩn đầu ra cốt lõi theo thang đo Bloom. Thứ nhất (CLO 3.1), giải thích cấu trúc cơ bản của ứng dụng Console, vai trò phương thức Main, lớp, chú thích và từ khóa C#. Thứ hai (CLO 3.2), sử dụng thành thạo Console.Write, Console.WriteLine, các ký tự thoát Escape Sequences và tính năng nội suy chuỗi String Interpolation $. Thứ ba (CLO 3.3), khai báo biến, phân tích kiểu dữ liệu số nguyên int, kỹ thuật đọc bàn phím với Console.ReadLine và ép kiểu int.Parse. Thứ tư (CLO 3.4), vẽ sơ đồ và giải thích bản chất biến là các vị trí ô nhớ trong RAM, phân biệt ghi đè phá hủy và đọc không phá hủy. Và thứ năm (CLO 3.5), áp dụng toán tử số học, quy tắc ưu tiên và cấu trúc rẽ nhánh if cùng các toán tử quan hệ để giải quyết bài toán so sánh logic.",
     "Dạ thưa thầy, 5 chuẩn đầu ra này bao quát trọn vẹn từ cú pháp cơ bản đến bản chất kiến trúc máy tính bên dưới. Lớp chúng em nhìn thấy rõ mục tiêu cần đạt được sau 3 tiết học hôm nay ạ!"),

    (3, "Tiến trình Bài học 3 Tiết (150 Phút Tích hợp)",
     "Buổi học của chúng ta được thiết kế theo phương pháp sư phạm tích hợp trong 150 phút liên tục. Tiết 1 dành 50 phút đi sâu vào Nền tảng ứng dụng Console: cấu trúc Welcome1.cs, phương thức Main, từ khóa, tạo project trong Visual Studio và các trợ lý thông minh IntelliSense. Tiết 2 dành 50 phút khai phá Kỹ thuật định dạng chuỗi: phân biệt Write và WriteLine, bảng Escape Sequences, String Interpolation $, giải quyết lỗi cú pháp và thực hành Lab 1. Tiết 3 dành 50 phút bùng nổ với Biến, Bộ nhớ RAM, Toán tử số học, Phân tích mã nguồn Addition.cs, Cấu trúc rẽ nhánh if, Toán tử so sánh trong Comparison.cs và thực hành Lab 2.",
     "Dạ, sự phân bổ 3 tiết rất liền mạch và khoa học ạ! Cứ sau mỗi phần kiến thức trọng tâm là chúng em lại được bắt tay vào bài tập thực hành trên máy tính để khắc sâu bài học ngay tại lớp."),

    (4, "Tổng quan Ứng dụng Console (Console Applications) vs GUI",
     "Trước khi viết code, chúng ta cần phân biệt: Ứng dụng Console là gì? Đây là các chương trình chạy trong giao diện dòng lệnh văn bản (Text-only Mode), không có nút bấm, thanh cuộn hay đồ họa chuột phức tạp. Các em hãy chú ý: Tại sao một kỹ sư phần mềm hiện đại vẫn phải học Console thật vững? Bởi vì Console tập trung 100% vào tư duy thuật toán, cấu trúc điều khiển, xử lý luồng dữ liệu mà không bị phân tán bởi việc căn chỉnh giao diện kéo thả. Hơn nữa, hầu hết các hệ thống backend, dịch vụ đám mây, script tự động hóa và DevOps hiện nay đều vận hành dưới dạng Console Services!",
     "Dạ thưa thầy, vậy học vững Console chính là xây dựng móng nhà kiên cố về tư duy thuật toán trước khi bước lên lập trình giao diện phức tạp đúng không ạ?"),

    (5, "Chương trình C# đầu tiên: Welcome1.cs",
     "Chính xác! Các em hãy nhìn lên Slide 5: Đây là chương trình C# kinh điển đầu tiên Welcome1.cs, tương ứng với Hình 3.1 trong giáo trình Deitel. Mã nguồn cực kỳ tinh gọn với 13 dòng: Dòng 1-3 là các chú thích tài liệu. Dòng 5 khai báo lớp public class Welcome1. Dòng 8 là phương thức public static void Main(). Và dòng 10 là câu lệnh xuất văn bản Console.WriteLine(\"Welcome to C# Programming!\"). Khi chạy, chương trình in ra đúng chuỗi văn bản này trên màn hình Console đen trắng.",
     "Dạ thưa thầy, nhìn thì ngắn gọn nhưng từng từ khóa như public, static, void, class đều có ý nghĩa rất sâu sắc. Thầy có thể giải phẫu chi tiết từng thành phần để chúng em nắm chắc bản chất không ạ?"),

    (6, "Giải phẫu Welcome1.cs: Chú thích (Comments) & Dòng trống",
     "Chắc chắn rồi! Nhìn vào Slide 6, các dòng bắt đầu bằng hai dấu gạch chéo // được gọi là Chú thích một dòng (Single-line comments). Trình biên dịch C# sẽ hoàn toàn bỏ qua mọi ký tự nằm sau dấu // cho đến hết dòng. Ngoài ra, C# còn hỗ trợ chú thích nhiều dòng nằm giữa /* và */, cùng chú thích tài liệu XML bắt đầu bằng ///. Các dòng trống (Blank lines) và khoảng trắng cũng được trình biên dịch bỏ qua. Thầy lưu ý cả lớp IT26M: Chú thích không làm tăng kích thước file thực thi và không làm chậm chương trình! Hãy viết chú thích thật rõ ràng để đồng đội và chính mình sau này dễ dàng bảo trì mã nguồn!",
     "Dạ thưa thầy, vậy trong đồ án môn học, việc viết chú thích đầy đủ giải thích ý nghĩa các khối lệnh cũng là một tiêu chí quan trọng để đánh giá điểm thực hành đúng không ạ?"),

    (7, "Giải phẫu Welcome1.cs: Khai báo Lớp (class Welcome1)",
     "Tiếp theo ở Slide 7 là từ khóa class. C# là một ngôn ngữ thuần hướng đối tượng, nghĩa là mọi mã lệnh muốn thực thi đều bắt buộc phải nằm bên trong một Lớp (Class). Cú pháp khai báo gồm từ khóa class theo sau là tên lớp do chúng ta tự đặt, ở đây là Welcome1. Theo chuẩn công nghiệp Microsoft và Deitel, tên lớp bắt buộc phải tuân thủ quy ước PascalCase, tức là viết hoa chữ cái đầu tiên của mỗi từ cấu thành. Khối thân lớp được bao bọc bởi cặp dấu ngoặc nhọn mở { và đóng }. Cặp ngoặc nhọn này tạo thành một khối mã (Block) có phạm vi rõ ràng.",
     "Dạ thưa thầy, tên tệp mã nguồn Welcome1.cs có bắt buộc phải trùng 100% với tên lớp Welcome1 bên trong như trong Java không ạ?"),

    (8, "Phương thức Main: Điểm khởi nhập (Entry Point) của ứng dụng",
     "Slide 8 mô tả thành phần quan trọng nhất: Phương thức Main! Trong mọi ứng dụng Console hoặc Windows C#, Main chính là Điểm khởi nhập duy nhất (Starting Point / Entry Point) mà máy ảo .NET CLR sẽ tìm đến và kích hoạt đầu tiên khi ứng dụng được khởi chạy. Cú pháp chuẩn là static void Main(). Từ khóa static biểu thị đây là một phương thức tĩnh, CLR có thể gọi trực tiếp mà không cần khởi tạo đối tượng của lớp. Từ khóa void chỉ ra rằng phương thức này không trả về giá trị nào cho hệ điều hành khi kết thúc.",
     "Dạ, vậy chữ M trong Main trong C# bắt buộc phải viết hoa đúng không thầy, khác với ngôn ngữ Java và C++ dùng chữ m thường ạ?"),

    (9, "Câu lệnh Console.WriteLine và Chuỗi ký tự (String Literals)",
     "Tại dòng 10 trên Slide 9, chúng ta gặp câu lệnh Console.WriteLine(\"Welcome to C# Programming!\");. Ở đây, Console là một lớp tiện ích tích hợp sẵn trong không gian tên System, chuyên quản lý các thao tác nhập xuất tiêu chuẩn. WriteLine là một phương thức của lớp Console, có nhiệm vụ in chuỗi ký tự bên trong cặp ngoặc kép ra màn hình, sau đó tự động đưa con trỏ xuống đầu dòng tiếp theo. Chuỗi ký tự nằm trong cặp ngoặc kép được gọi là Chuỗi ký tự cố định (String Literal). Cuối câu lệnh C# luôn bắt buộc phải có dấu chấm phẩy ; để kết thúc lệnh.",
     "Dạ thưa thầy, nếu chúng em quên dấu chấm phẩy ở cuối câu lệnh Console.WriteLine thì trình biên dịch sẽ phản ứng như thế nào ạ?"),

    (10, "Từ khóa C# (Keywords / Reserved Words)",
     "Slide 10 giới thiệu Bảng các Từ khóa C# theo Hình 3.2 giáo trình Deitel. Từ khóa là các từ ngữ được ngôn ngữ C# quy định sẵn ý nghĩa đặc biệt và giữ chỗ trước (Reserved). Ví dụ như class, static, void, int, if, else, return, using... Vì đã được hệ thống đăng ký, các em tuyệt đối không được sử dụng từ khóa để đặt tên cho biến, tên lớp hay tên phương thức, trừ khi các em thêm tiền tố @ ở phía trước, nhưng đây là điều tối kỵ trong thực tế công nghiệp!",
     "Dạ, chúng em sẽ ghi nhớ danh sách từ khóa này và tuyệt đối không đặt tên biến trùng với các từ khóa hệ thống để tránh xung đột cú pháp ạ."),

    (11, "Tạo dự án Console App trong Visual Studio",
     "Slide 11 minh họa quy trình tạo một dự án Console trong Visual Studio (Hình 3.3 Deitel). Thao tác chuẩn gồm 4 bước: File -> New -> Project (hoặc Ctrl+Shift+N). Chọn ngôn ngữ Visual C# -> chọn Windows -> chọn mẫu 'Console Application'. Đặt tên dự án là Welcome1, chọn vị trí lưu trữ và luôn tích chọn 'Create directory for solution'. Sau khi nhấn OK, Visual Studio sẽ tự động sinh cấu trúc tệp tin Program.cs chuẩn mực.",
     "Dạ thưa thầy, khi tích chọn 'Create directory for solution', toàn bộ tệp mã nguồn và cấu hình dự án sẽ được gom chung vào một thư mục gốc rất gọn gàng và dễ nộp bài đúng không ạ?"),

    (12, "Môi trường soạn thảo mã nguồn & Cửa sổ Editor",
     "Quan sát Slide 12 (Hình 3.4 Deitel), màn hình soạn thảo mã nguồn C# hiện lên với tính năng Tô màu cú pháp (Syntax Highlighting): từ khóa có màu xanh dương, chuỗi ký tự màu nâu đỏ, chú thích màu xanh lá cây, tên lớp màu xanh lơ. Bên lề trái có hiển thị số dòng (Line Numbers) giúp chúng ta dễ dàng định vị lỗi khi biên dịch. Ngoài ra, các nút dấu cộng trừ cho phép đóng mở (Outlining / Collapsing) các khối mã lệnh.",
     "Dạ, giao diện tô màu trực quan thế này giúp chúng em phát hiện ngay những lỗi sai chính tả hoặc thiếu ngoặc kép ngay từ lúc đang gõ code ạ!"),

    (13, "Trợ lý mã nguồn thông minh: IntelliSense Auto-Completion",
     "Slide 13 mô tả tính năng IntelliSense - trợ thủ đắc lực nhất của lập trình viên Visual Studio (Hình 3.5 & 3.6). Khi các em vừa gõ vài ký tự đầu, ví dụ gõ Con, một danh sách gợi ý sẽ bật lên ngay lập tức hiển thị từ Console. Các em chỉ cần nhấn phím Tab hoặc Enter là IDE sẽ tự động điền trọn vẹn tên lớp. Khi gõ dấu chấm . sau Console, danh sách toàn bộ các thành viên như Write, WriteLine, ReadLine sẽ hiện ra kèm biểu tượng chú giải chi tiết!",
     "Dạ thưa thầy, tính năng tự động hoàn thành này giúp chúng em gõ code nhanh hơn gấp 3 lần và không bao giờ lo bị gõ sai tên hàm ạ!"),

    (14, "Tính năng Parameter Info & Xem tài liệu nhanh",
     "Tiếp theo ở Slide 14 (Hình 3.7 Deitel), khi các em mở ngoặc đơn sau tên phương thức, ví dụ Console.WriteLine(, tính năng Parameter Info sẽ xuất hiện dạng tooltip hướng dẫn: phương thức này nhận những tham số gì, kiểu dữ liệu nào và cung cấp bao nhiêu phiên bản nạp chồng (Overloads). Tính năng này giúp các em lập trình chính xác mà không cần phải tra cứu tài liệu MSDN trên trình duyệt.",
     "Dạ, các mũi tên lên xuống trên tooltip Parameter Info còn cho phép duyệt qua tất cả 18 phiên bản nạp chồng của Console.WriteLine cực kỳ tiện lợi ạ!"),

    (15, "Biên dịch & Chạy ứng dụng Console đầu tiên",
     "Slide 15 chỉ dẫn thao tác chạy ứng dụng (Hình 3.8 Deitel). Các em nhấn phím tắt kinh điển Ctrl + F5 (Start Without Debugging). Màn hình Command Prompt màu đen sẽ bật lên, hiển thị dòng chữ 'Welcome to C# Programming!' và thông báo 'Press any key to continue...'. Thầy lưu ý: Nếu bấm F5 thay vì Ctrl+F5, cửa sổ console có thể biến mất ngay lập tức sau khi chạy xong khiến các em không kịp quan sát kết quả!",
     "Dạ thưa thầy, cả lớp chúng em đã thực hành bấm Ctrl + F5 và cửa sổ console đã hiển thị thành công dòng chữ chào mừng rồi ạ!"),

    (16, "Lỗi cú pháp (Syntax Errors) & Error List trong Visual Studio",
     "Chúng ta bước sang Tiết 2 với Slide 16 (Hình 3.9 Deitel): Lỗi cú pháp (Syntax Errors). Khi các em gõ sai quy tắc ngôn ngữ, ví dụ quên dấu chấm phẩy, viết sai tên Console hoặc thiếu ngoặc kép, Visual Studio sẽ ngay lập tức gạch chân lượn sóng màu đỏ dưới đoạn mã đó. Đồng thời, cửa sổ Error List ở phía dưới sẽ hiển thị mã lỗi (ví dụ CS1002: ; expected), chỉ rõ số dòng và số cột bị lỗi. Trình biên dịch sẽ từ chối dịch mã nguồn sang file .exe cho đến khi toàn bộ lỗi cú pháp được khắc phục.",
     "Dạ thưa thầy, khi nhấp đúp chuột vào một dòng báo lỗi trong cửa sổ Error List, con trỏ soạn thảo sẽ tự động nhảy ngay đến vị trí bị lỗi trong mã nguồn đúng không ạ?"),

    (17, "Biến thể xuất văn bản: Welcome2.cs với Console.Write",
     "Nhìn vào Slide 17 (Hình 3.10 Deitel), chúng ta tìm hiểu chương trình Welcome2.cs. Trong chương trình này, tác giả Deitel sử dụng hai câu lệnh liên tiếp: dòng 10 gọi Console.Write(\"Welcome to \"); và dòng 11 gọi Console.WriteLine(\"C# Programming!\");. Mặc dù được viết trên hai dòng lệnh độc lập, nhưng kết quả hiển thị trên màn hình console lại nằm trọn vẹn trên cùng một dòng văn bản!",
     "Dạ thưa thầy, tại sao hai câu lệnh riêng biệt lại in kết quả trên cùng một dòng được ạ? Cơ chế bên dưới của Console.Write khác gì WriteLine ạ?"),

    (18, "Phân biệt cơ chế hiển thị: Console.Write vs Console.WriteLine",
     "Slide 18 phân tích sâu sự khác biệt kỹ thuật giữa hai phương thức này. Phương thức Console.Write xuất chuỗi ký tự ra màn hình nhưng giữ nguyên con trỏ văn bản tại vị trí ngay sau ký tự cuối cùng vừa in. Trong khi đó, Console.WriteLine sau khi xuất xong sẽ tự động gửi thêm ký tự xuống dòng (Newline / Carriagereturn), đẩy con trỏ xuống đầu dòng tiếp theo. Việc phối hợp linh hoạt hai phương thức này là chìa khóa để thiết kế các câu lệnh nhắc nhập liệu chuyên nghiệp.",
     "Dạ em hiểu rồi! Thường khi in câu nhắc người dùng nhập dữ liệu, ví dụ 'Nhập số: ', chúng ta sẽ dùng Console.Write để con trỏ chờ nhập ngay cạnh câu nhắc đúng không thầy?"),

    (19, "Xuất văn bản nhiều dòng: Welcome3.cs & Ký tự thoát Escape Sequences",
     "Tại Slide 19 (Hình 3.11 Deitel), chúng ta xem xét Welcome3.cs: Chỉ với một câu lệnh Console.WriteLine duy nhất nhưng có thể in ra hai dòng văn bản khác nhau! Bí quyết nằm ở ký tự thoát \\n trong chuỗi \"Welcome to\\nC# Programming!\". Dấu gạch chéo ngược \\ được gọi là Ký tự thoát (Escape Character), báo hiệu cho trình biên dịch rằng ký tự đi liền sau nó mang một ý nghĩa điều khiển đặc biệt.",
     "Dạ thưa thầy, vậy ký tự \\ kết hợp với chữ n sẽ tạo thành một mã điều khiển xuống dòng, thay vì in ra hai ký tự gạch chéo và n trên màn hình đúng không ạ?"),

    (20, "Bảng tổng hợp Escape Sequences thông dụng trong C#",
     "Slide 20 tổng kết Bảng các Ký tự thoát thường gặp theo Hình 3.12 Deitel: \\n là xuống dòng (Newline). \\t là phím Tab ngang, giúp căn lề cột thẳng thớm. \\r là về đầu dòng (Carriage return). \\\\ dùng để in ra chính dấu gạch chéo ngược. Và \\\" dùng để in ra dấu ngoặc kép bên trong một chuỗi ký tự mà không làm đóng chuỗi. Các em cần ghi nhớ bảng này vì sẽ dùng liên tục trong các bài kiểm tra và dự án thực tế!",
     "Dạ thưa thầy, nếu em muốn in đường dẫn thư mục Windows như C:\\Program Files thì em phải viết hai dấu gạch chéo liên tiếp C:\\\\Program Files đúng không ạ?"),

    (21, "Định dạng chuỗi hiện đại: Welcome4.cs & String Interpolation ($)",
     "Bước sang Slide 21 (Hình 3.13 Deitel), chúng ta đến với một tính năng cực kỳ hiện đại của C#: Định dạng chuỗi nội suy (String Interpolation) được kích hoạt bởi ký tự dollar $. Trong Welcome4.cs, câu lệnh Console.WriteLine($\"Welcome to {person}!\"); cho phép chúng ta nhúng trực tiếp tên biến person vào trong chuỗi ký tự thông qua cặp ngoặc nhọn { }.",
     "Dạ thưa thầy, cú pháp với dấu $ này nhìn trong sáng và tự nhiên hơn rất nhiều so với cách dùng phép cộng chuỗi truyền thống ạ!"),

    (22, "Cơ chế hoạt động của Toán tử nội suy chuỗi $",
     "Slide 22 phân tích cơ chế nội tại của String Interpolation. Khi đặt ký tự $ ngay trước dấu mở ngoặc kép của chuỗi, trình biên dịch C# sẽ phân tích cú pháp và tự động chuyển đổi các biểu thức nằm trong cặp ngoặc nhọn thành giá trị chuỗi tương ứng tại thời điểm thực thi. Các em có thể đặt vào trong ngoặc nhọn không chỉ tên biến, mà còn có thể là biểu thức tính toán, phép gọi phương thức hoặc toán tử ba ngôi!",
     "Dạ, ví dụ ta có thể viết ${\"Lớp \" + classId} hoặc ${x * 2} ngay trong chuỗi mà không cần tạo biến phụ, rất tiện lợi thầy ạ!"),

    (23, "So sánh 3 phương pháp định dạng chuỗi trong C#",
     "Slide 23 đặt lên bàn cân 3 phương pháp định dạng chuỗi qua các thời kỳ: Cách 1 là Nối chuỗi bằng dấu cộng (+) cổ điển - rất dễ nhầm lẫn và tốn bộ nhớ khi cộng nhiều chuỗi. Cách 2 là String.Format với chỉ mục số {0}, {1} - tương đối rườm rà. Và Cách 3 là String Interpolation $ - trực quan, dễ đọc, giảm thiểu tối đa sai sót và có hiệu năng tối ưu nhất. Thầy khuyến nghị cả lớp IT26M từ nay về sau luôn ưu tiên sử dụng cú pháp $!",
     "Dạ thưa thầy, vậy trong tất cả các bài tập và đồ án của lớp IT26M, chúng em sẽ thống nhất dùng chuẩn String Interpolation $ theo khuyến nghị của thầy ạ!"),

    (24, "Bài tập nhanh Củng cố Cú pháp & Format chuỗi (Checkpoint 1)",
     "Tại Slide 24, chúng ta có một bài tập trắc nghiệm ngắn để củng cố kiến thức: Cho biến int x = 10, y = 20; câu lệnh Console.WriteLine($\"{x} + {y} = {x + y}\"); sẽ in ra kết quả gì? Đáp án chính xác là '10 + 20 = 30'. Các em thấy rằng biểu thức x + y nằm trong ngoặc nhọn được tính toán tự động và chuyển thành chuỗi 30 rất kỳ diệu!",
     "Dạ thưa thầy, bài tập checkpoint này rất trực quan, giúp chúng em khẳng định chắc chắn rằng biểu thức toán học bên trong { } sẽ được tính toán trước rồi mới ghép vào chuỗi ạ!"),

    (25, "Hands-on Lab 1: Xây dựng & Tùy biến thông điệp chào mừng IT26M",
     "Kết thúc Tiết 2 với bài thực hành Lab 1 tại Slide 25: Mỗi sinh viên tự mở Visual Studio, tạo dự án WelcomeIT26M, khai báo biến tên sinh viên và mã sinh viên, sau đó sử dụng cả Escape Sequences (\\n, \\t) và String Interpolation ($) để in ra một danh thiếp điện tử chuyên nghiệp trên màn hình Console. Thầy cho các em 10 phút để hoàn thành bài lab này tại máy!",
     "Dạ vâng ạ! Cả lớp chúng em đang bắt tay vào viết code bài Lab 1 ngay đây ạ, chúng em sẽ tùy biến màu sắc và khung viền cho danh thiếp thật ấn tượng!"),

    (26, "Bài toán thực tế: Nhập xuất dữ liệu & Phép cộng (Addition.cs)",
     "Chào mừng các em bước vào Tiết 3 với Slide 26! Bây giờ chúng ta sẽ nâng cấp ứng dụng Console từ việc chỉ in văn bản cố định sang mức độ tương tác hai chiều với người dùng qua chương trình Addition.cs. Ứng dụng này sẽ cho phép người dùng nhập vào hai số nguyên từ bàn phím, chương trình tính tổng và in kết quả ra màn hình.",
     "Dạ thưa thầy, đây chính là mô hình cốt lõi của mọi phần mềm: tiếp nhận dữ liệu đầu vào, xử lý tính toán trong bộ nhớ và xuất kết quả đầu ra đúng không ạ?"),

    (27, "Phân tích mã nguồn Addition.cs: Khai báo Biến và Kiểu int",
     "Slide 27 phân tích phần 1 của Addition.cs (Hình 3.14). Tại dòng 10, chúng ta thấy câu lệnh khai báo biến: int number1;. Ở đây, int là kiểu dữ liệu số nguyên (Integer) 32-bit trong C#, có thể lưu trữ các giá trị từ âm 2 tỷ đến dương 2 tỷ. number1 là tên định danh của biến (Variable Identifier). C# yêu cầu mọi biến đều phải được khai báo rõ ràng kiểu dữ liệu trước khi sử dụng.",
     "Dạ thưa thầy, quy tắc đặt tên biến trong C# có gì cần lưu ý để viết code chuẩn công nghiệp không ạ?"),

    (28, "Kỹ thuật nhập dữ liệu: Console.ReadLine & int.Parse",
     "Slide 28 phân tích kỹ thuật nhập liệu cốt lõi tại dòng 15: number1 = int.Parse(Console.ReadLine());. Phương thức Console.ReadLine() sẽ tạm dừng chương trình, chờ người dùng gõ văn bản từ bàn phím và nhấn Enter, sau đó trả về toàn bộ dòng văn bản đó dưới dạng Chuỗi (string). Vì kiểu chuỗi không thể tham gia trực tiếp vào phép cộng số học, chúng ta phải đưa chuỗi đó qua phương thức int.Parse() để chuyển đổi thành một số nguyên int.",
     "Dạ thưa thầy, nếu không có hàm int.Parse mà lấy trực tiếp chuỗi từ ReadLine đem cộng lại thì dấu cộng sẽ thực hiện nối chuỗi chứ không phải cộng số học đúng không ạ?"),

    (29, "Cơ chế phân tích cú pháp kiểu dữ liệu: int.Parse vs int.TryParse",
     "Tại Slide 29, thầy muốn mở rộng một kiến thức rất quan trọng trong công nghiệp: Sự khác biệt giữa int.Parse và int.TryParse. Nếu người dùng nhập vào chữ 'abc' thay vì số, int.Parse sẽ ném ra ngoại lệ FormatException và làm sập chương trình. Để xử lý an toàn, trong các dự án thực tế sau này, chúng ta sẽ sử dụng phương thức int.TryParse để kiểm tra xem dữ liệu nhập vào có hợp lệ hay không trước khi chuyển đổi!",
     "Dạ, kiến thức mở rộng về TryParse này cực kỳ giá trị cho chúng em khi làm các ứng dụng thực tế có yêu cầu chống crash khi người dùng nhập sai ạ!"),

    (30, "Khái niệm Bộ nhớ: Biến là ô nhớ định danh trong RAM",
     "Slide 30 minh họa Khái niệm Bộ nhớ máy tính (Hình 3.15 Deitel). Khi câu lệnh int number1 = 45; được thực thi, hệ điều hành và CLR sẽ cấp phát một ô nhớ 4 byte trong bộ nhớ RAM, gán nhãn tên ô nhớ đó là number1 và nạp giá trị nhị phân tương ứng với số 45 vào bên trong ô nhớ đó. Mọi biến trong C# thực chất đều là tên gọi đại diện cho một vị trí địa chỉ trong bộ nhớ RAM!",
     "Dạ thưa thầy, sơ đồ trực quan này giúp chúng em hiểu rõ mối liên kết giữa tên biến trong mã nguồn C# và các byte vật lý trong thanh RAM của máy tính ạ!"),

    (31, "Cơ chế Ghi đè phá hủy vs Đọc không phá hủy",
     "Slide 31 giải thích hai nguyên lý tương tác bộ nhớ kinh điển (Hình 3.16 & 3.17 Deitel): Nguyên lý thứ nhất là Đọc không phá hủy (Non-destructive Read): khi CPU đọc giá trị từ biến number1 để tính toán, giá trị 45 trong ô nhớ vẫn còn nguyên vẹn. Nhưng Nguyên lý thứ hai là Ghi đè phá hủy (Destructive Write): nếu các em gán number1 = 99;, thì giá trị cũ 45 sẽ bị ghi đè và mất vĩnh viễn, nhường chỗ cho giá trị mới 99!",
     "Dạ thưa thầy, sự phân biệt này giải thích vì sao ta có thể dùng biến number1 nhiều lần trong nhiều phép tính khác nhau mà giá trị của nó không hề bị hao hụt hay biến mất ạ!"),

    (32, "Bảng các Toán tử số học cơ bản trong C# (+, -, *, /, %)",
     "Slide 32 tổng hợp Bảng các Toán tử số học trong C# theo Hình 3.18 Deitel: Phép cộng (+), phép trừ (-), phép nhân (*), phép chia (/), và phép chia lấy phần dư (%). Các em lưu ý: trong lập trình, ký hiệu nhân là dấu sao *, tuyệt đối không dùng chữ x; ký hiệu chia là dấu gạch chéo /, không dùng dấu hai chấm!",
     "Dạ, chúng em sẽ luôn nhớ dùng dấu * cho phép nhân và / cho phép chia khi viết biểu thức toán học trong C# ạ."),

    (33, "Phép chia nguyên (Integer Division) và Toán tử chia lấy dư (%)",
     "Slide 33 nhấn mạnh một cạm bẫy mà 90% sinh viên năm nhất đều mắc phải: Phép chia số nguyên (Integer Division). Trong C#, nếu cả tử số và mẫu số đều là kiểu số nguyên int, ví dụ 7 / 4, thì kết quả sẽ là 1 chứ không phải 1.75! Phần thập phân bị cắt bỏ hoàn toàn. Còn toán tử chia lấy dư 7 % 4 sẽ trả về phần dư là 3. Muốn có kết quả 1.75, ít nhất một trong hai toán hạng phải là số thực (7.0 / 4)!",
     "Dạ thưa thầy, đây thực sự là bài học xương máu! Đã có rất nhiều bài tập tính điểm trung bình ra sai kết quả chỉ vì chia nguyên 2 số int mà quên ép kiểu sang double ạ!"),

    (34, "Thứ tự ưu tiên của các toán tử số học (Operator Precedence)",
     "Slide 34 mô tả Bảng Thứ tự ưu tiên toán tử theo Hình 3.19 Deitel: Mức ưu tiên cao nhất là biểu thức trong cặp ngoặc đơn (). Tiếp theo là các toán tử nhân (*), chia (/), và chia lấy dư (%). Mức ưu tiên thấp hơn là cộng (+) và trừ (-). Nếu các toán tử có cùng mức độ ưu tiên đứng cạnh nhau, chúng sẽ được tính toán tuần tự từ trái sang phải (Left-to-Right Associativity).",
     "Dạ thưa thầy, để tránh nhầm lẫn khi viết các công thức phức tạp, chúng em nên chủ động dùng cặp ngoặc đơn để chỉ rõ thứ tự tính toán đúng không ạ?"),

    (35, "Tính toán biểu thức đại số phức tạp & Đa thức bậc 2",
     "Tại Slide 35 (Hình 3.20 Deitel), chúng ta thực hành chuyển đổi biểu thức đại số y = a*x^2 + b*x + c sang mã lệnh C#. Trong C# không có toán tử mũ ^ cho số học, do đó biểu thức phải được viết là: y = a * x * x + b * x + c;. Dựa vào quy tắc ưu tiên, các phép nhân a*x*x và b*x sẽ được thực hiện trước, sau đó mới đến các phép cộng, đảm bảo kết quả chính xác tuyệt đối.",
     "Dạ, nếu lỡ tay gõ dấu mũ ^ trong C# thì đó lại là phép toán bitwise XOR chứ không phải lũy thừa, rất nguy hiểm nếu không nắm chắc cú pháp ạ!"),

    (36, "Ra quyết định trong C#: Cấu trúc rẽ nhánh if",
     "Chúng ta sang Slide 36: Cấu trúc điều khiển if! Mọi chương trình thông minh đều cần khả năng ra quyết định dựa trên điều kiện thực tế. Cú pháp cơ bản là: if (điều_kiện) câu_lệnh;. Biểu thức điều kiện bên trong ngoặc đơn bắt buộc phải trả về giá trị kiểu boolean (true hoặc false). Nếu điều kiện đúng (true), câu lệnh sẽ được thực thi; nếu sai (false), câu lệnh bị bỏ qua.",
     "Dạ thưa thầy, khác với ngôn ngữ C ngày xưa cho phép dùng số 0 và 1 làm điều kiện, trong C# điều kiện bắt buộc phải là kiểu bool đúng không ạ?"),

    (37, "Bảng các Toán tử quan hệ và Toán tử bằng",
     "Slide 37 tổng hợp Bảng các Toán tử quan hệ và bằng theo Hình 3.21 Deitel: Bằng nhau (==), khác nhau (!=), lớn hơn (>), nhỏ hơn (<), lớn hơn hoặc bằng (>=), nhỏ hơn hoặc bằng (<=). Thầy đặc biệt lưu ý: Toán tử so sánh bằng trong C# là hai dấu bằng liền nhau ==, còn một dấu bằng đơn = là toán tử gán giá trị!",
     "Dạ thưa thầy, nếu viết nhầm if (x = y) thì trình biên dịch C# sẽ báo lỗi ngay vì phép gán không trả về kiểu boolean, giúp chúng ta phòng tránh được lỗi nghiêm trọng ạ!"),

    (38, "Mã nguồn mẫu: Comparison.cs (Phần 1 - Nhập liệu)",
     "Slide 38 trình bày phần 1 của chương trình Comparison.cs (Hình 3.21). Chương trình yêu cầu người dùng nhập vào hai số nguyên number1 và number2 qua bàn phím bằng Console.ReadLine() và int.Parse(). Đây là bước thu thập dữ liệu đầu vào chuẩn bị cho quá trình so sánh logic.",
     "Dạ, phần nhập liệu này sử dụng đúng cấu trúc chuẩn của Addition.cs mà chúng em vừa học ở slide trước, rất quen thuộc và dễ hiểu ạ!"),

    (39, "Mã nguồn mẫu: Comparison.cs (Phần 2 - 6 Câu lệnh if)",
     "Slide 39 là trái tim của Comparison.cs với 6 câu lệnh if độc lập: if (number1 == number2), if (number1 != number2), if (number1 < number2), if (number1 > number2), if (number1 <= number2), và if (number1 >= number2). Mỗi câu lệnh if kiểm tra một mối quan hệ logic và in ra thông báo tương ứng nếu điều kiện thỏa mãn.",
     "Dạ thưa thầy, vì đây là các câu lệnh if độc lập nên máy tính sẽ lần lượt kiểm tra cả 6 điều kiện, và có thể có nhiều câu lệnh if cùng thỏa mãn một lúc đúng không ạ?"),

    (40, "Kết quả thực thi ứng dụng Comparison.cs",
     "Slide 40 hiển thị kết quả thực thi của Comparison.cs qua hai kịch bản chạy thử (Hình 3.22 Deitel): Kịch bản 1 khi nhập 777 và 777, chương trình in ra '777 == 777', '777 <= 777', và '777 >= 777'. Kịch bản 2 khi nhập 35 và 80, chương trình in ra '35 != 80', '35 < 80', và '35 <= 80'.",
     "Dạ, kết quả chạy thử hoàn toàn khớp với dự đoán logic! Cả ba thông báo thỏa mãn đều được in ra màn hình rất rõ ràng ạ!"),

    (41, "Bảng tổng hợp Thứ tự ưu tiên toàn diện các toán tử",
     "Slide 41 tổng kết Bảng Thứ tự ưu tiên toàn diện của tất cả các toán tử đã học trong Chương 3 (Hình 3.23 Deitel): Cao nhất là cặp ngoặc đơn (), kế đến là nhân chia lấy dư (*, /, %), tiếp theo là cộng trừ (+, -), sau đó đến các toán tử quan hệ (<, <=, >, >=), kế tiếp là toán tử bằng (==, !=), và cuối cùng có mức ưu tiên thấp nhất là toán tử gán (=).",
     "Dạ thưa thầy, bảng tổng kết này rất trực quan và có hệ thống! Nhìn vào đây chúng em thấy rõ phép gán luôn có độ ưu tiên thấp nhất để mọi phép tính toán và so sánh hoàn tất xong mới gán kết quả vào biến ạ!"),

    (42, "Các lỗi lập trình kinh điển cần tránh",
     "Slide 42 điểm mặt các lỗi phổ biến nhất của sinh viên: Lỗi 1: Đặt dấu chấm phẩy ngay sau mệnh đề điều kiện của if, ví dụ if (x == y); Console.WriteLine(...); - dấu chấm phẩy tạo thành một câu lệnh rỗng khiến lệnh in luôn luôn bị chạy dù x có bằng y hay không! Lỗi 2: Nhầm lẫn dấu gán = với dấu so sánh bằng ==. Lỗi 3: Đặt dấu cách giữa các toán tử hai ký tự như = =, ! =, < =.",
     "Dạ, lỗi đặt dấu chấm phẩy sau if là lỗi logic cực kỳ khó phát hiện nếu không được thầy cảnh báo trước, chúng em sẽ ghi chú lại thật cẩn thận ạ!"),

    (43, "Bài tập rèn luyện tư duy: Vẽ hình & Bảng bình phương lập phương",
     "Slide 43 giới thiệu hai bài tập rèn luyện tư duy kinh điển trong giáo trình Deitel (Hình 3.25 & 3.26): Bài 1 là in các hình khối hộp chữ nhật, hình oval, mũi tên và hình thoi bằng các dấu sao *. Bài 2 là in Bảng tính bình phương và lập phương của các số từ 0 đến 10 sử dụng các ký tự tab \\t để căn thẳng cột.",
     "Dạ thưa thầy, bài tập in bảng này giúp chúng em rèn luyện nhuần nhuyễn cả việc tính toán số học lẫn việc định dạng cột bằng \\t và String Interpolation ạ!"),

    (44, "Hands-on Lab 2: Viết ứng dụng Máy tính cơ bản",
     "Slide 44 giao nhiệm vụ cho bài thực hành Lab 2: Sinh viên viết chương trình MiniCalculator, cho phép nhập vào hai số nguyên a và b. Ứng dụng tính và hiển thị tổng, hiệu, tích, thương số nguyên và phần dư. Đặc biệt, sinh viên phải sử dụng câu lệnh if để kiểm tra điều kiện nếu b == 0 thì in cảnh báo 'Không thể chia cho số 0!' thay vì thực hiện phép chia!",
     "Dạ thưa thầy, bài Lab 2 này tổng hòa đầy đủ mọi kỹ năng của buổi học hôm nay: nhập liệu bàn phím, ép kiểu int.Parse, tính toán số học và kiểm tra điều kiện if. Cả lớp chúng em sẽ hoàn thành ngay trên máy tính ạ!"),

    (45, "Tổng kết Chương 3, Đối chiếu Chuẩn đầu ra (CLOs) & Hướng dẫn tự học",
     "Chúng ta về đích tại Slide 45! Hôm nay cả lớp IT26M đã hoàn thành xuất sắc 5 chuẩn đầu ra CLOs của Chương 3: làm chủ ứng dụng Console, thành thạo xuất chuỗi và nội suy $, hiểu bản chất ô nhớ RAM, thuần thục toán tử số học và cấu trúc rẽ nhánh if. Về nhà, các em hoàn thành 40 câu trắc nghiệm trên website học phần, làm lại hai bài Lab 1 và Lab 2, và đọc trước Chương 4: Giới thiệu về Lớp, Đối tượng, Phương thức và Chuỗi. Hẹn gặp lại các em ở buổi học tiếp theo!",
     "Dạ chúng em cảm ơn thầy rất nhiều vì buổi học vô cùng bổ ích và trực quan hôm nay ạ! Lớp IT26M chúng em sẽ hoàn thành đầy đủ bài tập và chuẩn bị kỹ lưỡng cho Chương 4 ạ!")
]

BASE_DIR = r"i:\Course_UDA\Kỹ thuật lập trình\ebooks\new ebooks\WebProgramingTechnique2026"
VIDEO_CH03_DIR = os.path.join(BASE_DIR, "VideoCShape", "Chapter_03")
JS_DIR = os.path.join(BASE_DIR, "js")

os.makedirs(VIDEO_CH03_DIR, exist_ok=True)
os.makedirs(JS_DIR, exist_ok=True)

# 1. Generate script.txt and scriptDemo.txt
script_path = os.path.join(VIDEO_CH03_DIR, "script.txt")
script_demo_path = os.path.join(VIDEO_CH03_DIR, "scriptDemo.txt")

lines_out = []
transcripts = {}

for num, title, spk1, spk2 in SCRIPTS_DATA:
    block = f"Slide {num}: {title}\nNgười 1: {spk1}\nNgười 2: {spk2}"
    lines_out.append(block)
    
    transcripts[str(num)] = {
        "title": title,
        "speaker1": spk1,
        "speaker2": spk2
    }

full_script_text = "\n\n".join(lines_out) + "\n"

with open(script_path, "w", encoding="utf-8") as f:
    f.write(full_script_text)

with open(script_demo_path, "w", encoding="utf-8") as f:
    f.write(full_script_text)

print(f"Generated {script_path} and {script_demo_path} ({len(SCRIPTS_DATA)} slides)")

# 2. Generate js/transcripts_ch03.js
js_path = os.path.join(JS_DIR, "transcripts_ch03.js")
js_code = "const SLIDE_TRANSCRIPTS_CHAPTER_03 = " + json.dumps(transcripts, ensure_ascii=False, indent=2) + ";\n"

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js_code)

print(f"Generated {js_path} successfully!")
