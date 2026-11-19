# -*- coding: utf-8 -*-
"""
Generate script.txt and scriptDemo.txt for Chapter 4:
Introduction to Classes, Objects, Methods and strings (Deitel & Deitel)
Audience: Class IT26M (Faculty of IT - Dong A University)
Format:
Slide X: [Title]
Người 1: [Giảng viên]
Người 2: [Sinh viên IT26M]
"""

import os

BASE_DIR = r"i:\Course_UDA\Kỹ thuật lập trình\ebooks\new ebooks\WebProgramingTechnique2026"
VIDEO_CH04_DIR = os.path.join(BASE_DIR, "VideoCShape", "Chapter_04")
os.makedirs(VIDEO_CH04_DIR, exist_ok=True)

SCRIPT_PATH = os.path.join(VIDEO_CH04_DIR, "script.txt")
SCRIPTDEMO_PATH = os.path.join(VIDEO_CH04_DIR, "scriptDemo.txt")

slides_content = [
    # Slide 1
    (
        "KỸ THUẬT LẬP TRÌNH C# - CHƯƠNG 4: GIỚI THIỆU VỀ LỚP, ĐỐI TƯỢNG, PHƯƠNG THỨC VÀ CHUỖI",
        "Chào mừng tất cả các em sinh viên lớp IT26M Khóa 2026 đến với buổi học hôm nay! Chúng ta chính thức bước sang Chương 4: Giới thiệu về Lớp, Đối tượng, Phương thức và Chuỗi - Introduction to Classes, Objects, Methods and strings. Đây là một trong những chương bản lề và mang tính quyết định nhất trong toàn bộ học phần Kỹ thuật Lập trình. Bài giảng của chúng ta được biên soạn chuẩn mực theo giáo trình quốc tế danh tiếng Visual C# How to Program của hai tác giả Harvey Deitel và Paul Deitel. Nếu như ở 3 chương trước, các em đã nắm vững các câu lệnh tuần tự, biến số và cấu trúc điều khiển, thì bắt đầu từ chương này, các em sẽ chính thức bước chân vào thế giới của Lập trình Hướng đối tượng (Object-Oriented Programming - OOP) - nền tảng của mọi hệ thống phần mềm doanh nghiệp hiện đại.",
        "Dạ chào thầy! Cả lớp IT26M chúng em rất mong chờ chương học này ạ. Từ khi bắt đầu học công nghệ thông tin, chúng em đã nghe rất nhiều về Lập trình hướng đối tượng, về Lớp và Đối tượng nhưng vẫn chưa thực sự hiểu rõ bản chất bên dưới bộ nhớ máy tính hoạt động ra sao. Chúng em rất hào hứng muốn biết làm thế nào để tự thiết kế ra các lớp đối tượng của riêng mình bằng C# ạ!"
    ),
    # Slide 2
    (
        "Mục tiêu Bài học & Chuẩn đầu ra (CLOs)",
        "Để đảm bảo chất lượng đào tạo đại học chính quy chuẩn kiểm định quốc tế, bài học Chương 4 hướng tới 5 chuẩn đầu ra (CLOs) cốt lõi được đo lường theo thang đo Bloom. Thứ nhất (CLO 4.1 - Understand), các em phân biệt rõ ràng bản chất giữa Lớp (Class) và Đối tượng (Object), cơ chế cấp phát bộ nhớ Heap của toán tử new, và sự khác biệt giữa Kiểu Tham chiếu (Reference Types) so với Kiểu Giá trị (Value Types). Thứ hai (CLO 4.2 - Apply), tự tay định nghĩa lớp, khai báo biến thể hiện (instance variables) với phạm vi private, xây dựng các phương thức Set và Get để bảo toàn nguyên lý Đóng gói (Encapsulation). Thứ ba (CLO 4.3 - Apply), sử dụng thành thạo Thuộc tính C# (Properties) với các bộ truy cập get/set, từ khóa ngữ cảnh value, và ứng dụng cú pháp Thuộc tính Tự động (Auto-Implemented Properties). Thứ tư (CLO 4.4 - Apply), định nghĩa và nạp chồng Hàm tạo (Constructors) để khởi tạo trạng thái hợp lệ cho đối tượng ngay khi khai sinh. Và thứ năm (CLO 4.5 - Create), sử dụng kiểu số thực chính xác cao decimal cho bài toán tài chính, hiện thực hóa cơ chế kiểm tra tính hợp lệ dữ liệu (Data Validation), định dạng tiền tệ chuyên nghiệp :C và xây dựng hoàn chỉnh hệ thống ứng dụng ngân hàng Mini ATM.",
        "Dạ thưa thầy, 5 mục tiêu chuẩn đầu ra này bao quát toàn bộ những kỹ năng cốt lõi của một lập trình viên C# chuyên nghiệp! Từ việc quản lý bộ nhớ đến thiết kế hướng đối tượng chuẩn mực và ứng dụng vào bài toán nghiệp vụ tài chính thực tế. Lớp IT26M chúng em quyết tâm sẽ đạt xuất sắc tất cả các chuẩn đầu ra này ạ!"
    ),
    # Slide 3
    (
        "Tiến trình Bài học 3 Tiết (150 Phút Tích hợp)",
        "Buổi học hôm nay được thiết kế theo phương pháp sư phạm tích hợp trong 150 phút, kết hợp hài hòa giữa lý thuyết chuyên sâu, phân tích mã nguồn chuẩn giáo trình Deitel và thực hành tương tác tại chỗ. Tiết 1 dành 50 phút tập trung vào Cơ sở Hướng đối tượng: phân biệt Class và Object, driver class AccountTest, toán tử new, phân tích ô nhớ Heap vs Stack, biến thể hiện private, phương thức SetName/GetName, sơ đồ lớp UML 3 ngăn và bài thực hành Lab 1. Tiết 2 dành 50 phút đi sâu vào Thuộc tính C# & Hàm khởi tạo: cú pháp Property get/set, từ khóa value, Auto-Implemented Properties, Constructor tùy biến loại bỏ default constructor và bài thực hành Lab 2. Tiết 3 dành 50 phút bùng nổ với Nghiệp vụ Ngân hàng: kiểu số thực decimal, cơ chế data validation, phương thức Deposit, định dạng tiền tệ :C, bảng format specifiers, tái cấu trúc DisplayAccount và bài thực hành Lab 3 xây dựng Mini ATM System.",
        "Dạ, lộ trình 3 tiết này rất mạch lạc và thực tế thầy ạ! Cứ sau mỗi phần lý thuyết là chúng em được làm bài Checkpoint củng cố ngay và có một bài Hands-on Lab để tự tay gõ lệnh kiểm chứng trên Visual Studio. Cách học này giúp chúng em ghi nhớ kiến thức rất sâu ạ."
    ),
    # Slide 4
    (
        "Cuộc chuyển dịch Tư duy: Lập trình Thủ tục sang Hướng đối tượng",
        "Trước khi viết code, chúng ta cần hiểu cuộc chuyển dịch tư duy lịch sử trên Slide 4: từ Lập trình Thủ tục (Procedural Programming) sang Lập trình Hướng đối tượng (OOP). Trong mô hình thủ tục, chương trình được xem như một chuỗi các hành động thực thi; dữ liệu và các hàm xử lý dữ liệu bị tách rời nhau, dữ liệu thường được truyền qua lại giữa các hàm, rất dễ bị sửa đổi ngoài ý muốn và khó bảo trì khi dự án phình to. Ngược lại, trong OOP, phần mềm được mô hình hóa thành một tập hợp các Đối tượng (Objects) tương tác với nhau, y hệt như các thực thể trong thế giới thực! Mỗi đối tượng là một thể đóng gói trọn vẹn cả Thuộc tính (Attributes/Data) - tức trạng thái mà nó sở hữu, và Hành vi (Behaviors/Methods) - tức những việc mà nó có thể làm.",
        "Thầy cho một ví dụ sinh động dễ hình dung được không ạ?",
        "Rất tuyệt! Hãy tưởng tượng chiếc ô tô của các em. Trạng thái của ô tô là màu sơn, số lượng xăng trong bình, tốc độ hiện tại. Hành vi của ô tô là tăng ga, đạp phanh, rẽ trái. Khi các em đạp chân ga, các em không cần phải thò tay vào buồng đốt để bơm thêm nhiên liệu; chân ga chính là một phương thức giao tiếp công khai (public method) an toàn để thay đổi trạng thái bên trong chiếc xe mà không làm hỏng động cơ! Đó chính là triết lý hướng đối tượng."
    ),
    # Slide 5
    (
        "Phân chia Tiết 1: Lớp, Đối tượng & Phương thức",
        "Chúng ta chính thức bắt đầu Tiết 1: Cơ bản về Lớp, Đối tượng và Phương thức! Trong tiết học này, chúng ta sẽ khảo sát ứng dụng lái thử AccountTest.cs, bóc tách cơ chế cấp phát ô nhớ Heap bằng toán tử new, phân biệt biến tham chiếu và biến giá trị, tìm hiểu cấu trúc lớp Account.cs với biến thể hiện private name, hai phương thức SetName và GetName, quy chuẩn vẽ sơ đồ lớp UML 3 ngăn của giáo trình Deitel và nguyên lý đóng gói dữ liệu an toàn. Thầy đề nghị cả lớp mở sẵn Visual Studio để chúng ta cùng phân tích từng dòng lệnh!",
        "Dạ vâng ạ, chúng em đã sẵn sàng màn hình Visual Studio bên cạnh để bắt đầu Tiết 1 cùng thầy ạ!"
    ),
    # Slide 6
    (
        "Lái thử lớp Account: Chương trình AccountTest.cs (Hình 4.1)",
        "Các em quan sát Hình 4.1 trên Slide 6. Đây là tệp AccountTest.cs - chương trình lái thử (Test-Drive App). Tại dòng 8, chúng ta có câu lệnh kinh điển: Account myAccount = new Account();. Câu lệnh này làm nhiệm vụ khởi tạo một đối tượng mới thuộc lớp Account và gán tham chiếu vào biến myAccount. Tại dòng 11, chúng ta gọi phương thức myAccount.GetName() để lấy ra tên tài khoản ban đầu và in ra màn hình. Khi mới tạo, vì chuỗi name chưa được thiết lập, GetName() trả về null, nên màn hình hiển thị một chuỗi rỗng. Tiếp tục ở dòng 14, chương trình yêu cầu người dùng nhập tên mới từ bàn phím bằng Console.ReadLine(), lưu vào biến theName. Tại dòng 17, ta gọi myAccount.SetName(theName); để truyền tên mới vào cho đối tượng lưu giữ. Và cuối cùng tại dòng 21, ta gọi lại myAccount.GetName() để kiểm chứng xem tên tài khoản đã được cập nhật chính xác thành Jane Green hay chưa!",
        "Dạ thưa thầy, em thấy ở dòng 8 có từ khóa new. Có phải từ khóa new này chính là lệnh yêu cầu hệ điều hành cấp phát bộ nhớ để sinh ra đối tượng Account mới không ạ?"
    ),
    # Slide 7
    (
        "Khái niệm Driver Class & Toán tử new",
        "Hoàn toàn chính xác! Slide 7 phân tích sâu hai khái niệm cốt lõi này. Thứ nhất, Lớp Lái thử (Driver Class): Lớp AccountTest được gọi là Driver Class vì nó chứa phương thức Main - điểm khởi nhập thực thi của chương trình. Nhiệm vụ duy nhất của Driver Class là tạo ra các thể hiện của những lớp khác và điều khiển chúng thực thi để kiểm thử các tính năng. Thứ hai, Toán tử new: Trong C#, khi toán tử new được gọi, nó sẽ gửi yêu cầu tới máy ảo .NET CLR để cấp phát một vùng nhớ trên bộ nhớ Managed Heap để chứa toàn bộ dữ liệu của đối tượng mới. Đồng thời, toán tử new sẽ gọi hàm khởi tạo (Constructor) của lớp đó để thiết lập trạng thái ban đầu, và cuối cùng nó trả về một Tham chiếu (Reference) - tức địa chỉ của đối tượng trên Heap để biến myAccount nắm giữ!",
        "Dạ, vậy biến myAccount nằm trên ngăn xếp Stack, còn bản thân đối tượng Account thì nằm trên vùng nhớ Heap đúng không thầy?"
    ),
    # Slide 8
    (
        "Kiểu Tham chiếu (Reference Types) vs Kiểu Giá trị (Value Types)",
        "Xuất sắc! Slide 8 chỉ rõ sự khác biệt bản chất giữa Kiểu Tham chiếu (Reference Types) và Kiểu Giá trị (Value Types). Trong C#, các kiểu dữ liệu nguyên thủy như int, double, float, bool, char, struct là Kiểu Giá trị. Biến kiểu giá trị chứa trực tiếp dữ liệu thô ngay trong ô nhớ của chính nó trên vùng nhớ Stack. Khi ta gán biến giá trị này cho biến giá trị khác, hệ thống sẽ sao chép toàn bộ bản sao dữ liệu. Ngược lại, tất cả các Lớp (Classes), đối tượng do ta tạo ra, mảng và chuỗi string đều là Kiểu Tham chiếu. Biến kiểu tham chiếu không chứa đối tượng bên trong nó, mà nó chỉ chứa một 'con trỏ an toàn' lưu địa chỉ tham chiếu trỏ tới đối tượng thực sự đang nằm trên Managed Heap! Nếu một biến tham chiếu chưa được khởi tạo với new hoặc không trỏ tới đối tượng nào, nó sẽ mang giá trị đặc biệt là null. Nếu các em cố tình gọi phương thức trên một biến null, chương trình sẽ sụp đổ ngay lập tức với ngoại lệ kinh điển NullReferenceException!",
        "Dạ thưa thầy, hiểu được cơ chế Heap và Stack này giúp em giải thích được vì sao khi hai biến cùng trỏ vào một đối tượng, nếu một bên thay đổi dữ liệu thì bên kia cũng thấy thay đổi theo, vì thực chất chúng đang nhìn vào cùng một vùng nhớ trên Heap ạ!"
    ),
    # Slide 9
    (
        "Khai báo lớp Account.cs & Biến thể hiện private (Hình 4.2)",
        "Bây giờ chúng ta chuyển sang Hình 4.2 trên Slide 9 để khảo sát cấu trúc nội tại của lớp Account.cs. Lớp Account bắt đầu bằng dòng public class Account. Từ khóa public biểu thị đây là lớp công khai, có thể được truy cập và sử dụng bởi bất kỳ lớp nào khác trong dự án. Bên trong thân lớp, tại dòng 6, chúng ta khai báo: private string name;. Đây được gọi là Biến thể hiện (Instance Variable) hay Field. Thầy nhấn mạnh từ khóa private: private là công cụ quyền lực nhất để hiện thực hóa nguyên lý Ẩn giấu Dữ liệu (Data Hiding). Khi biến name được khai báo là private, chỉ duy nhất các phương thức nằm bên trong lớp Account mới có quyền đọc và sửa đổi nó. Các lớp bên ngoài như AccountTest tuyệt đối không thể truy cập trực tiếp bằng cú pháp myAccount.name được!",
        "Dạ thưa thầy, nếu lớp bên ngoài không thể truy cập trực tiếp vào biến private name, thì làm thế nào để người dùng có thể xem hoặc thay đổi tên tài khoản được ạ?"
    ),
    # Slide 10
    (
        "Phương thức SetName: Khái niệm Tham số (Parameter)",
        "Đó chính là lý do chúng ta cần đến hai phương thức SetName và GetName! Slide 10 phân tích chi tiết phương thức SetName tại dòng 9 của Hình 4.2: public void SetName(string accountName) { name = accountName; }. Phương thức này được khai báo với phạm vi public, đóng vai trò như một 'cổng giao tiếp công khai' để thế giới bên ngoài gửi yêu cầu vào. Kiểu trả về là void vì nhiệm vụ của nó chỉ là lưu trữ dữ liệu chứ không cần trả lại kết quả gì. Trong cặp ngoặc đơn là Tham số (Parameter) accountName kiểu chuỗi string. Khi AccountTest gọi myAccount.SetName(theName), giá trị của biến theName được truyền vào làm đối số (Argument). Bên trong thân hàm, câu lệnh name = accountName; sẽ sao chép giá trị từ tham số cục bộ vào lưu giữ trong biến thể hiện name của đối tượng!",
        "Dạ, như vậy phương thức SetName giống như một người bảo vệ cổng: nhận dữ liệu từ bên ngoài và cất giữ vào biến an toàn bên trong lớp ạ!"
    ),
    # Slide 11
    (
        "Phương thức GetName: Kiểu trả về & Lệnh return",
        "Chính xác! Và ở chiều ngược lại, Slide 11 giải phẫu phương thức GetName tại dòng 15 của Hình 4.2: public string GetName() { return name; }. Phương thức này cũng là public. Nhưng các em lưu ý kiểu trả về của nó không phải là void nữa, mà là string! Điều này thông báo cho trình biên dịch C# biết rằng: khi phương thức này kết thúc thực thi, nó bắt buộc phải chuyển giao một giá trị kiểu chuỗi string trở lại cho nơi đã gọi nó. Bên trong thân hàm, câu lệnh return name; thực hiện nhiệm vụ đọc giá trị đang lưu trong biến thể hiện name và gửi trả về. Nhờ cặp phương thức SetName và GetName, ta vừa cho phép bên ngoài tương tác với dữ liệu, vừa kiểm soát tuyệt đối quyền truy cập!",
        "Dạ thưa thầy, trong C# có từ khóa return, vậy khi gặp lệnh return thì phương thức sẽ dừng lại ngay lập tức đúng không ạ?",
        "Đúng vậy! Lệnh return lập tức kết thúc thực thi của phương thức và trả luồng điều khiển cùng giá trị về nơi gọi hàm."
    ),
    # Slide 12
    (
        "Phân biệt Biến thể hiện (Instance Variables) vs Biến cục bộ (Local Variables)",
        "Slide 12 là một bảng so sánh cực kỳ quan trọng mà các em phải phân biệt thật rạch ròi: Biến thể hiện (Instance Variables) so với Biến cục bộ (Local Variables). Về vị trí khai báo: Biến thể hiện được khai báo trong thân lớp, bên ngoài mọi phương thức (ví dụ: private string name;); trong khi Biến cục bộ được khai báo bên trong thân của một phương thức hoặc trong danh sách tham số (ví dụ: string theName trong Main, hay accountName trong SetName). Về phạm vi hoạt động: Biến thể hiện có thể được truy cập bởi toàn bộ các phương thức bên trong lớp; còn biến cục bộ chỉ tồn tại và được nhìn thấy duy nhất trong khối lệnh bao bọc nó. Về vòng đời sinh mệnh: Biến thể hiện sinh ra khi đối tượng được tạo bằng new và tồn tại suốt chừng nào đối tượng đó còn tồn tại trên Heap; còn biến cục bộ chỉ sinh ra khi phương thức được gọi và lập tức bị xóa sổ khỏi Stack ngay khi phương thức kết thúc. Đặc biệt về giá trị mặc định: Biến thể hiện được C# tự động khởi tạo giá trị mặc định (kiểu số là 0, bool là false, kiểu tham chiếu là null); còn biến cục bộ không có giá trị mặc định, nếu các em cố đọc một biến cục bộ chưa gán giá trị thì C# sẽ báo lỗi biên dịch ngay lập tức!",
        "Dạ thưa thầy, bảng phân tích này giải đáp trọn vẹn thắc mắc của em lúc nãy: vì sao khi mới tạo đối tượng Account thì GetName() trả về null, là do biến thể hiện string name tự động được C# khởi tạo giá trị mặc định là null ạ!"
    ),
    # Slide 13
    (
        "Sơ đồ lớp UML (UML Class Diagram) Chuẩn mực 3 Ngăn (Hình 4.3)",
        "Trong kỹ nghệ phần mềm chuyên nghiệp, trước khi bắt tay vào viết code, các kỹ sư luôn mô hình hóa hệ thống bằng Ngôn ngữ Mô hình Hóa Thống nhất (Unified Modeling Language - UML). Slide 13 giới thiệu Sơ đồ Lớp UML chuẩn mực theo Hình 4.3 trong giáo trình Deitel. Một lớp trong UML luôn được vẽ thành một hình chữ nhật chia làm 3 ngăn (compartments) rõ ràng: Ngăn trên cùng chứa Tên lớp (Class Name), ví dụ: Account. Ngăn giữa chứa danh sách Thuộc tính và Biến thể hiện (Attributes), ví dụ: - name : string. Dấu trừ (-) ở phía trước thể hiện phạm vi private, theo sau là tên biến và kiểu dữ liệu. Ngăn dưới cùng chứa danh sách các Hoạt động và Phương thức (Operations/Methods), ví dụ: + SetName(accountName : string) và + GetName() : string. Dấu cộng (+) ở phía trước thể hiện phạm vi public. Tên tham số và kiểu dữ liệu được đặt trong ngoặc đơn, kiểu trả về được viết sau dấu hai chấm. Nhìn vào sơ đồ UML này, bất kỳ lập trình viên nào dù dùng C#, Java hay C++ đều có thể cài đặt chính xác cấu trúc của lớp!",
        "Dạ thưa thầy, quy ước dấu cộng là public, dấu trừ là private trong UML rất trực quan và dễ nhớ ạ. Sau này làm đồ án môn học chúng em sẽ dùng chuẩn này để vẽ thiết kế kiến trúc ạ!"
    ),
    # Slide 14
    (
        "Tổ chức Dự án Đa tệp lớp (Multiple Class Files) trong Visual Studio",
        "Slide 14 hướng dẫn các em kỹ năng tổ chức dự án đa tệp lớp (Multiple Class Files) chuyên nghiệp trong Visual Studio. Trong các bài tập đơn giản, các em thường gom tất cả các lớp vào chung một tệp Program.cs; tuy nhiên trong công nghiệp phần mềm, chuẩn mực bắt buộc là: Mỗi lớp phải được lưu trong một tệp mã nguồn .cs riêng biệt trùng tên với tên lớp! Trong dự án của chúng ta, lớp Account được lưu trong Account.cs, còn lớp kiểm thử AccountTest được lưu trong AccountTest.cs. Để thêm một lớp mới trong Visual Studio, các em chỉ cần nhấp chuột phải vào tên Project trong cửa sổ Solution Explorer, chọn Add, chọn Class, đặt tên tệp là Account.cs và nhấn Add. Visual Studio sẽ tự động tạo khung mã nguồn với cùng một không gian tên (namespace), giúp các lớp tự động nhìn thấy nhau và phối hợp trơn tru mà không cần bất kỳ câu lệnh include phức tạp nào!",
        "Dạ, tách riêng mỗi lớp ra một tệp .cs giúp dự án gọn gàng, dễ tìm kiếm và khi làm việc nhóm trên Git các thành viên sẽ không bị xung đột mã nguồn lẫn nhau thầy ạ!"
    ),
    # Slide 15
    (
        "Nguyên lý Đóng gói (Encapsulation) & Ẩn giấu Dữ liệu (Hình 4.4)",
        "Slide 15 đúc kết Trụ cột số 1 của Lập trình Hướng đối tượng: Nguyên lý Đóng gói (Encapsulation) và Ẩn giấu Dữ liệu (Information Hiding), minh họa trực quan từ Hình 4.4 của giáo trình. Các em hãy quan sát hình ảnh quả cầu đối tượng Account: Biến thể hiện private string name nằm sâu trong vùng lõi được bảo vệ nghiêm ngặt. Lớp bên ngoài không thể thò tay trực tiếp vào để sửa đổi hay làm hỏng dữ liệu. Cách duy nhất để tương tác là thông qua lớp vỏ bọc bảo vệ gồm các phương thức public SetName và GetName. Lợi ích sống còn của đóng gói là gì? Thứ nhất: Bảo toàn tính toàn vẹn của dữ liệu (Data Integrity) - ta có thể kiểm tra tính hợp lệ trước khi cho phép ghi vào biến. Thứ hai: Giảm thiểu sự phụ thuộc (Loose Coupling) - ta có thể thoải mái thay đổi cấu trúc lưu trữ nội bộ bên trong lớp mà không làm gãy đổ bất kỳ dòng mã nào của các lớp sử dụng bên ngoài!",
        "Dạ, em rất tâm đắc với nguyên lý đóng gói này thầy ạ! Nó giống như việc chúng ta sử dụng máy tính bảng: chúng ta chỉ tương tác qua màn hình cảm ứng chứ không cần và không được phép thò tay vào mạch điện bên trong, nhờ đó thiết bị luôn vận hành an toàn và bền bỉ ạ!"
    ),
    # Slide 16
    (
        "Checkpoint 1: Kiểm tra Nhanh & Thực hành Tiết 1",
        "Để kết thúc Tiết 1, chúng ta cùng thực hiện bài Checkpoint 1 trên Slide 16 để củng cố toàn bộ kiến thức. Câu hỏi 1: Điều gì sẽ xảy ra nếu trong phương thức Main của lớp AccountTest, các em viết câu lệnh myAccount.name = \"John\";? Bốn phương án: A. Chương trình chạy bình thường; B. Báo lỗi biên dịch CS0122 vì biến name có phạm vi private; C. Báo lỗi lúc chạy NullReferenceException; D. Biến name được tự động chuyển thành public. Em chọn đáp án nào?",
        "Dạ thưa thầy, Câu 1 em chọn đáp án B ạ! Vì biến name được khai báo là private trong lớp Account nên lớp AccountTest ở bên ngoài hoàn toàn không có quyền truy cập trực tiếp, trình biên dịch C# sẽ chặn lại và báo lỗi CS0122 ngay lập tức ạ!",
        "Hoàn toàn chính xác! Và trong 15 phút thực hành Lab 1 tại chỗ, cả lớp mở Visual Studio, tạo Console App tên AccountApp, thêm tệp Account.cs và AccountTest.cs, gõ đúng mã nguồn Hình 4.1 và 4.2, chạy thử và kiểm tra sự thay đổi của biến name trong cửa sổ Debug Watch. Cả lớp bắt đầu thực hành!"
    ),
    # Slide 17
    (
        "Phân chia Tiết 2: Thuộc tính & Hàm tạo (Properties & Constructors)",
        "Chào mừng các em bước vào Tiết 2: Thuộc tính và Hàm khởi tạo (Properties & Constructors)! Ở Tiết 1, chúng ta đã dùng cặp phương thức SetName và GetName theo phong cách truyền thống của C++ và Java. Tuy nhiên, ngôn ngữ C# sở hữu một tính năng vô cùng độc đáo, thanh lịch và mạnh mẽ gọi là Thuộc tính (Properties). Trong tiết học này, chúng ta sẽ khám phá bộ truy cập get và set, từ khóa ngữ cảnh value, Thuộc tính Tự động (Auto-Implemented Properties), cơ chế Hàm khởi tạo tùy biến và sự biến mất của hàm tạo mặc định. Chúng ta cùng bắt đầu!",
        "Dạ thưa thầy, em nghe nói tính năng Property trong C# giúp việc đọc ghi dữ liệu trông tự nhiên như một biến thông thường nhưng vẫn giữ nguyên được sự an toàn của đóng gói. Chúng em rất nóng lòng muốn tìm hiểu cú pháp của nó ạ!"
    ),
    # Slide 18
    (
        "Giới thiệu Thuộc tính (Properties) trong C# (Hình 4.5)",
        "Đúng như em vừa nói! Các em hãy quan sát Hình 4.5 trên Slide 18. Ở phiên bản nâng cấp này, lớp AccountTest không còn gọi myAccount.SetName(theName) hay myAccount.GetName() nữa! Thay vào đó, tại dòng 11 và dòng 21, chương trình viết cực kỳ ngắn gọn và tự nhiên: Console.WriteLine(myAccount.Name); để đọc tên tài khoản. Và tại dòng 17, để gán tên mới, chương trình viết: myAccount.Name = theName;! Cú pháp gán dấu bằng myAccount.Name = theName trông hệt như ta đang truy cập một biến thông thường, nhưng thực chất bên dưới, trình biên dịch C# đang tự động kích hoạt bộ truy cập set của Thuộc tính Name để xử lý an toàn! Đây chính là vẻ đẹp cú pháp đặc trưng của ngôn ngữ C#.",
        "Dạ thưa thầy, cách viết myAccount.Name = theName vừa trực quan, dễ đọc, lại vừa ngắn gọn hơn rất nhiều so với việc phải gọi tên hàm SetName dài dòng ạ!"
    ),
    # Slide 19
    (
        "Cấu trúc Thuộc tính Name: Bộ truy cập get và set (Hình 4.6)",
        "Vậy bên trong lớp Account.cs, Thuộc tính Name được định nghĩa như thế nào? Slide 19 giải phẫu chi tiết mã nguồn Hình 4.6. Một Property được khai báo với kiểu dữ liệu, tên thuộc tính viết hoa theo chuẩn PascalCase, theo sau là một khối ngoặc nhọn chứa hai bộ truy cập (accessors): get và set. Bộ truy cập get tương đương với phương thức GetName: bên trong chứa câu lệnh return name; để trả về giá trị của biến thể hiện. Bộ truy cập set tương đương với phương thức SetName: bên trong chứa câu lệnh name = value; để gán giá trị mới vào biến. Ở đây, biến private string name được gọi là Biến hỗ trợ (Backing Field) cho thuộc tính Name!",
        "Dạ thưa thầy, em thấy trong bộ truy cập set có xuất hiện một từ lạ là value. Biến value này ở đâu ra mà chúng ta không cần khai báo kiểu dữ liệu ạ?"
    ),
    # Slide 20
    (
        "Từ khóa Ngữ cảnh value trong Bộ truy cập set",
        "Một câu hỏi cực kỳ xuất sắc! Slide 20 giải thích cặn kẽ về từ khóa ngữ cảnh value. Trong C#, value là một Từ khóa Ngữ cảnh (Contextual Keyword). Nó chỉ đóng vai trò là một từ khóa đặc biệt khi nằm bên trong bộ truy cập set của một Property. Khi bên ngoài thực hiện câu lệnh gán: myAccount.Name = \"Jane Green\";, biểu thức nằm bên phải dấu bằng (ở đây là chuỗi \"Jane Green\") sẽ tự động được trình biên dịch C# đóng gói và chuyển giao vào biến ngầm định có tên là value. Kiểu dữ liệu của value luôn tự động trùng khớp 100% với kiểu dữ liệu của chính Property đó (ở đây là string). Các em không cần và không được phép khai báo lại biến value!",
        "Dạ, em hiểu rồi ạ! Như vậy vế phải của phép gán truyền giá trị gì thì biến value trong set sẽ nhận đúng giá trị đó, rồi câu lệnh name = value; sẽ cất vào backing field ạ!"
    ),
    # Slide 21
    (
        "Sơ đồ lớp UML Biểu diễn Thuộc tính với Stereotype (Hình 4.7)",
        "Các em nhìn lên Slide 21 để xem cách chuẩn quốc tế UML biểu diễn Thuộc tính C# theo Hình 4.7 của giáo trình. Khi một thuộc tính có cả hai bộ truy cập get và set, trong UML nó được biểu diễn bằng một Stereotype đặc thù đặt trong cặp dấu ngoặc kép: «property». Dòng thuộc tính được viết: + Name : string «get/set». Dấu cộng (+) biểu thị thuộc tính Name là public. Nếu một thuộc tính chỉ cho phép đọc mà không cho sửa, ta gọi là Thuộc tính Chỉ đọc (Read-Only Property), trong UML sẽ ghi là «get». Stereotype này giúp người đọc sơ đồ phân biệt rạch ròi giữa một biến dữ liệu thô thông thường với một Thuộc tính thông minh có khối xử lý logic!",
        "Dạ, nhìn vào ký hiệu «property» «get/set» trong UML là chúng em biết ngay trong code C# sẽ phải viết một Property với đầy đủ hai khối get và set tương ứng ạ!"
    ),
    # Slide 22
    (
        "Thuộc tính Tự động (Auto-Implemented Properties)",
        "Bây giờ, thầy giới thiệu với các em một 'vũ khí' tối thượng giúp tăng tốc độ viết code trong C#: Thuộc tính Tự động (Auto-Implemented Properties) trên Slide 22! Hãy quan sát: nếu một Property chỉ làm nhiệm vụ đơn giản là lưu trữ và trả về giá trị mà không cần thêm bất kỳ logic kiểm tra phức tạp nào, các em không cần phải mất công tự tay khai báo biến private backing field nữa! Thay vào đó, các em chỉ cần viết đúng một dòng duy nhất: public string Name { get; set; }. Trình biên dịch C# sẽ tự động âm thầm tạo ra một biến private backing field ẩn bên dưới mã máy, và tự động tạo mã lệnh cho get trả về biến đó, set gán value vào biến đó. Mã nguồn của các em trở nên thanh thoát, gọn gàng và hiện đại tới mức tối đa!",
        "Thật kỳ diệu thầy ạ! Thay vì phải viết hơn mười dòng code khai báo biến private rồi viết get, return, set, name = value, giờ đây chỉ với đúng một dòng public string Name { get; set; } là chúng em đã có trọn vẹn một thuộc tính an toàn chuẩn hướng đối tượng rồi ạ!"
    ),
    # Slide 23
    (
        "So sánh: Thuộc tính Tự động vs Thuộc tính Tường minh",
        "Slide 23 là một bảng đúc kết quy tắc chọn lựa giữa Thuộc tính Tự động (Auto-Implemented Properties) và Thuộc tính Tường minh (Explicit Properties). Khi nào nên dùng Thuộc tính Tự động? Khi thuộc tính không cần bất kỳ logic nghiệp vụ nào, chỉ đơn thuần đọc và ghi dữ liệu thô. Khi nào bắt buộc phải dùng Thuộc tính Tường minh? Đó là khi các em cần thực hiện Kiểm tra Tính hợp lệ dữ liệu (Data Validation) - ví dụ kiểm tra số tiền nạp phải lớn hơn 0; hoặc khi cần tính toán dữ liệu động - ví dụ thuộc tính FullName ghép từ FirstName và LastName; hoặc khi cần ghi vết kiểm toán (Logging). Một kỹ sư C# giỏi là người biết sử dụng linh hoạt cả hai loại cú pháp này tùy theo yêu cầu bài toán!",
        "Dạ, khi cần validate dữ liệu thì ta dùng thuộc tính tường minh với backing field, còn dữ liệu thông thường thì ta dùng auto-property cho ngắn gọn và sạch sẽ ạ!"
    ),
    # Slide 24
    (
        "Vấn đề Khởi tạo Đối tượng: Tại sao cần Hàm tạo (Constructors)?",
        "Chúng ta sang nửa sau của Tiết 2 với vấn đề: Tại sao cần Hàm khởi tạo (Constructors)? Nhìn lên Slide 24: trong các ví dụ trước, khi chúng ta gọi Account myAccount = new Account();, đối tượng Account sinh ra với tên mặc định là null. Sau đó, ta lại phải mất thêm một câu lệnh thứ hai là myAccount.Name = \"Jane Green\"; để gán tên cho nó. Trong thực tế, điều này rất nguy hiểm! Một đối tượng tài khoản ngân hàng sinh ra mà không có tên chủ tài khoản hoặc không có số dư ban đầu thì ở trong trạng thái không hợp lệ (Invalid State). Sẽ ra sao nếu lập trình viên quên không gọi lệnh gán tên? Đối tượng sẽ mang giá trị rác hoặc null gây lỗi hệ thống! Để giải quyết triệt để vấn đề này, ngôn ngữ C# cung cấp Hàm tạo (Constructor) - cho phép truyền dữ liệu và thiết lập trạng thái hoàn chỉnh cho đối tượng ngay trong khoảnh khắc khai sinh bằng toán tử new!",
        "Dạ, hàm tạo giống như giấy khai sinh cho đối tượng vậy thầy ạ! Ngay khi sinh ra là phải có đầy đủ họ tên và thông tin hợp lệ, không bao giờ được phép để đối tượng bơ vơ ở trạng thái rỗng ạ!"
    ),
    # Slide 25
    (
        "Khai báo Hàm tạo trong lớp Account.cs (Hình 4.8)",
        "Hình ảnh so sánh giấy khai sinh của em rất hay! Slide 25 khảo sát cú pháp khai báo Hàm tạo trong Hình 4.8. Các em hãy chú ý kỹ hai quy tắc cú pháp bất di bất dịch của Hàm tạo trong C#: Thứ nhất, Hàm tạo bắt buộc phải có tên trùng khớp 100% với tên của Lớp (ở đây là Account). Thứ hai, Hàm tạo tuyệt đối không có kiểu dữ liệu trả về, kể cả từ khóa void cũng không được phép có! Tại dòng 8 của Hình 4.8, ta viết: public Account(string accountName) { Name = accountName; }. Hàm tạo này tiếp nhận một tham số là chuỗi accountName. Bên trong thân hàm, nó gọi thuộc tính Name để gán giá trị khởi tạo. Thầy nhấn mạnh: việc gọi qua Property Name thay vì gán trực tiếp vào biến private giúp chúng ta tận dụng ngay cơ chế kiểm tra tính hợp lệ dữ liệu nếu có!",
        "Dạ thưa thầy, nếu em lỡ tay viết thêm từ khóa void vào trước tên hàm tạo: public void Account(string accountName), thì điều gì sẽ xảy ra ạ?",
        "Một câu hỏi bẫy kinh điển! Nếu viết thêm void, trình biên dịch C# sẽ coi đây là một phương thức thông thường có tên là Account chứ không còn là một Hàm tạo nữa! Khi đó, các em sẽ không thể dùng nó để khởi tạo đối tượng với toán tử new được. Nhớ kỹ: Constructor không bao giờ có kiểu trả về!"
    ),
    # Slide 26
    (
        "Khởi tạo nhiều Đối tượng với Đối số trong AccountTest.cs (Hình 4.9)",
        "Các em quan sát Hình 4.9 trên Slide 26 để thấy sức mạnh của Hàm tạo khi khởi tạo nhiều đối tượng. Tại dòng 8 và dòng 9, chúng ta tạo ra hai tài khoản độc lập với đúng một câu lệnh thanh lịch: Account account1 = new Account(\"Jane Green\"); và Account account2 = new Account(\"John Blue\");. Đối số \"Jane Green\" được truyền thẳng vào hàm tạo của account1, và đối số \"John Blue\" được truyền vào hàm tạo của account2. Hai đối tượng này nằm ở hai vùng nhớ hoàn toàn độc lập trên Managed Heap, mỗi đối tượng tự quản lý một bản sao thuộc tính Name riêng biệt của chính nó! Khi gọi in ra màn hình, account1.Name cho ra \"Jane Green\", còn account2.Name cho ra \"John Blue\".",
        "Dạ thưa thầy, chỉ với một lớp Account đóng vai trò là bản thiết kế chung (Blueprint), chúng ta có thể tạo ra vô số các đối tượng tài khoản khác nhau trong bộ nhớ, mỗi đối tượng mang một dữ liệu riêng biệt của khách hàng đó ạ!"
    ),
    # Slide 27
    (
        "Hàm tạo Mặc định (Default Constructor) vs Hàm tạo Tùy biến",
        "Đúng vậy! Slide 27 phân tích một nguyên lý cực kỳ then chốt trong C#: Sự biến mất của Hàm tạo Mặc định (Default Constructor). Nếu trong một lớp, các em không viết bất kỳ một hàm tạo nào, trình biên dịch C# sẽ tự động ban tặng cho lớp đó một Hàm tạo Mặc định không tham số (Default Parameterless Constructor) với thân hàm rỗng, cho phép ta viết new Account(). TUY NHIÊN, một khi các em đã tự tay định nghĩa bất kỳ một Hàm tạo tùy biến nào có tham số (ví dụ: public Account(string accountName)), thì trình biên dịch C# sẽ lập tức thu hồi và xóa bỏ vĩnh viễn hàm tạo mặc định đó! Kể từ thời điểm đó, nếu các em cố tình viết new Account() mà không truyền đối số, chương trình sẽ báo lỗi biên dịch CS7036 ngay lập tức! Muốn vừa khởi tạo không đối số, vừa khởi tạo có đối số, các em bắt buộc phải tự tay viết thêm cả hai hàm tạo, kỹ thuật này gọi là Nạp chồng Hàm tạo (Constructor Overloading).",
        "Dạ thưa thầy, kiến thức này cực kỳ quan trọng ạ! Trước đây khi làm bài tập, đôi khi em viết hàm tạo có tham số xong rồi quay lại gọi new không tham số bị báo lỗi đỏ lòm mà không hiểu tại sao. Giờ em đã hiểu rõ bản chất của trình biên dịch C# rồi ạ!"
    ),
    # Slide 28
    (
        "Sơ đồ lớp UML Biểu diễn Hàm tạo (Hình 4.10)",
        "Slide 28 minh họa cách vẽ Hàm tạo trên Sơ đồ lớp UML theo Hình 4.10 giáo trình. Các em nhìn vào ngăn dưới cùng của hình chữ nhật Account: Hàm tạo được đặt ở vị trí đầu tiên của danh sách phương thức: + Account(accountName : string). Tương tự như trong mã nguồn C#, trên sơ đồ UML, hàm tạo mang tên trùng hoàn toàn với tên lớp ở ngăn trên cùng, có dấu cộng (+) thể hiện phạm vi public, danh sách tham số nằm trong ngoặc đơn, và đặc biệt là phía sau hoàn toàn không có dấu hai chấm kèm kiểu trả về! Nhìn vào sơ đồ UML này, người lập trình biết ngay lớp này yêu cầu bắt buộc phải truyền một tham số chuỗi khi khởi tạo đối tượng.",
        "Dạ, ký hiệu UML cho hàm tạo rất nhất quán với cú pháp C#: cùng tên lớp và không có kiểu trả về ạ!"
    ),
    # Slide 29
    (
        "Checkpoint 2: Kiểm tra Nhanh & Thực hành Tiết 2",
        "Để đúc kết Tiết 2, thầy mời cả lớp cùng giải quyết Checkpoint 2 trên Slide 29. Câu hỏi: Một lớp có hàm tạo public Student(string name) { ... }. Câu lệnh nào sau đây sẽ gây ra lỗi biên dịch? A. Student s = new Student(\"Alice\"); B. Student s = new Student(); C. string n = s.Name; D. Cả A và C đều đúng. Em chọn đáp án nào?",
        "Dạ thưa thầy, Câu hỏi Checkpoint 2 em chọn đáp án B: Student s = new Student(); sẽ gây lỗi biên dịch ạ! Vì lớp đã có hàm tạo tùy biến có tham số nên C# đã hủy bỏ hàm tạo mặc định không tham số, do đó việc gọi new không truyền đối số sẽ bị trình biên dịch từ chối ngay lập tức ạ!",
        "Chính xác tuyệt đối! Cả lớp dành 15 phút thực hành Lab 2: Nâng cấp lớp Account với thuộc tính Auto-Implemented và Hàm tạo có tham số, khởi tạo hai tài khoản khác nhau trong AccountTest và chạy thử kết quả!"
    ),
    # Slide 30
    (
        "Phân chia Tiết 3: Decimal, Validation & Dự án Ngân hàng ATM",
        "Chào mừng các em đến với Tiết 3 - phần thực chiến đỉnh cao của bài học hôm nay: Kiểu số thực decimal, Cơ chế Data Validation và Dự án Ngân hàng Mini ATM! Trong tiết này, chúng ta sẽ trả lời câu hỏi hóc búa: Tại sao trong các ứng dụng tài chính ngân hàng, lập trình viên bị cấm tuyệt đối không được dùng double hay float? Chúng ta sẽ tìm hiểu kiểu 128-bit decimal, bổ sung thuộc tính Balance với cơ chế kiểm tra giá trị hợp lệ, xây dựng phương thức nạp tiền Deposit, định dạng tiền tệ chuyên nghiệp với ký tự :C, nhận diện các lỗi lập trình kinh điển, tái cấu trúc mã nguồn và hoàn thành bài thực hành Lab 3 xây dựng Mini ATM System. Chúng ta cùng bắt đầu!",
        "Dạ, phần này nghe rất cuốn hút và đậm chất thực tế doanh nghiệp thầy ạ! Chúng em rất tò mò muốn biết vì sao các ngân hàng lại cấm dùng double và float ạ!"
    ),
    # Slide 31
    (
        "Bài toán Tài chính: Tại sao cấm dùng double/float cho Tiền tệ?",
        "Các em hãy nhìn lên Slide 31: Đây là một bài học đắt giá của ngành công nghệ phần mềm! Tại sao cấm dùng float và double cho bài toán tiền tệ? Bởi vì float (32-bit) và double (64-bit) biểu diễn số thực theo chuẩn IEEE 754 dưới dạng Nhị phân (Binary Floating-Point). Trong hệ nhị phân, các phân số thập phân quen thuộc như 0.1 hay 0.01 không thể được biểu diễn chính xác tuyệt đối mà bị làm tròn vô hạn tuần hoàn! Thầy lấy ví dụ: nếu các em lấy 0.1 cộng 0.2 trong kiểu double, kết quả máy tính in ra sẽ là 0.30000000000000004! Khi một ngân hàng xử lý hàng triệu giao dịch chuyển tiền mỗi ngày, sự sai lệch ở hàng phần triệu này sẽ tích tụ lại thành những khoản tiền chênh lệch khổng lồ, gây ra thảm họa kế toán và vi phạm pháp luật tài chính nghiêm trọng!",
        "Trời ơi nguy hiểm thật thầy ạ! Chỉ một sai số nhỏ ở phần thập phân nhị phân mà nhân lên hàng triệu giao dịch thì hệ thống kế toán sẽ bị lệch tiền ngay lập tức! Vậy giải pháp cứu cánh của Microsoft trong C# là gì ạ?"
    ),
    # Slide 32
    (
        "Đặc tính Kỹ thuật Kiểu decimal (128-bit) & Hậu tố m / M",
        "Giải pháp chính là kiểu dữ liệu decimal được thiết kế riêng cho bài toán tài chính trên Slide 32! Khác hoàn toàn với float và double, kiểu decimal sử dụng tới 128 bits (16 bytes) và biểu diễn số thực dưới dạng Thập phân (Base-10 Floating-Point). Nó mang lại độ chính xác siêu việt lên tới 28 đến 29 chữ số có nghĩa! Mọi phép tính tiền tệ với 0.1 hay 0.01 đều chính xác tuyệt đối 100%, hoàn toàn không có sai số làm tròn nhị phân. Khi viết hằng số kiểu decimal trong mã nguồn C#, các em BẮT BUỘC phải thêm hậu tố chữ m hoặc M ở phía sau con số (ví dụ: decimal balance = 150.50m;). Chữ m là viết tắt của Monetary (Tiền tệ). Nếu các em viết 150.50 mà không có m, trình biên dịch C# sẽ mặc định đó là kiểu double và báo lỗi không cho phép gán ngầm định vào biến decimal!",
        "Dạ thưa thầy, hậu tố m rất dễ nhớ vì nó đại diện cho Money hay Monetary. Từ nay về sau khi làm các bài toán tiền tệ, kế toán hay bán hàng thương mại điện tử, chúng em sẽ luôn luôn sử dụng kiểu decimal ạ!"
    ),
    # Slide 33
    (
        "Nâng cấp lớp Account.cs: Bổ sung Biến balance & Thuộc tính Balance (Hình 4.11 - Phần 1)",
        "Rất chuẩn mực! Bây giờ chúng ta cùng phân tích Hình 4.11 trên Slide 33 để nâng cấp lớp Account toàn diện. Lớp Account lúc này có hai biến thể hiện private: private string name; và private decimal balance;. Trong hàm tạo tại dòng 11: public Account(string accountName, decimal initialBalance), chúng ta nhận vào hai tham số: tên tài khoản và số dư khởi tạo. Bên trong hàm tạo, ta gán Name = accountName; và Balance = initialBalance;. Tiếp theo tại dòng 24, chúng ta khai báo Thuộc tính: public decimal Balance. Điểm đặc biệt nhất của thuộc tính Balance là nó có bộ truy cập get công khai để bên ngoài đọc số dư, nhưng bộ truy cập set lại được khai báo là private set;! Điều này có nghĩa là chỉ nội bộ lớp Account mới được phép thay đổi số dư, các lớp bên ngoài không thể tự tiện gán myAccount.Balance = 999999999 được!",
        "Dạ thưa thầy, việc đặt private set cho thuộc tính Balance là một thiết kế bảo mật quá tuyệt vời ạ! Số dư tài khoản ngân hàng chỉ được phép thay đổi thông qua các giao dịch nạp tiền hoặc rút tiền hợp lệ, chứ bên ngoài không thể tùy tiện sửa đổi số dư được ạ!"
    ),
    # Slide 34
    (
        "Cơ chế Kiểm tra Tính hợp lệ của Dữ liệu (Data Validation)",
        "Chính xác! Và Slide 34 đi sâu vào Cơ chế Kiểm tra Tính hợp lệ của Dữ liệu (Data Validation) trong bộ truy cập set của Balance và trong hàm tạo. Các em quan sát câu lệnh rẽ nhánh: if (initialBalance > 0.0m) { Balance = initialBalance; }. Tại sao cần điều kiện này? Bởi vì một tài khoản ngân hàng khi mới mở không bao giờ được phép có số dư âm! Nếu người dùng cố tình truyền vào một số tiền âm như -50.0m, điều kiện if sẽ sai, và biến Balance sẽ không bị gán giá trị âm đó mà giữ nguyên giá trị mặc định là 0.0m. Nhờ kiểm tra tính hợp lệ dữ liệu ngay tại 'cửa ngõ' hàm tạo và thuộc tính, đối tượng của chúng ta luôn luôn được đảm bảo nằm trong một trạng thái nhất quán và hợp lệ (Consistent State) suốt vòng đời của nó!",
        "Dạ, đây chính là sức mạnh của Data Validation mà thầy đã nhấn mạnh: ngăn chặn dữ liệu rác và dữ liệu sai quy tắc nghiệp vụ ngay từ khi nó manh nha xâm nhập vào hệ thống ạ!"
    ),
    # Slide 35
    (
        "Phương thức Nghiệp vụ Ngân hàng: Deposit(decimal depositAmount) (Hình 4.11 - Phần 2)",
        "Tiếp theo tại Hình 4.11 phần 2 trên Slide 35, chúng ta xây dựng phương thức nghiệp vụ cốt lõi của ngân hàng: Phương thức Nạp tiền Deposit! Phương thức được khai báo: public void Deposit(decimal depositAmount). Nó tiếp nhận một tham số là số tiền muốn nạp depositAmount kiểu decimal. Bên trong thân hàm, một lập trình viên non tay sẽ chỉ viết đơn giản: Balance = Balance + depositAmount;. Nhưng một kỹ sư chuyên nghiệp bắt buộc phải có câu lệnh kiểm tra validation: if (depositAmount > 0.0m) { Balance = Balance + depositAmount; }! Tại sao? Bởi vì nếu khách hàng nạp một số tiền âm hoặc bằng 0, giao dịch đó là phi lý! Chỉ khi số tiền nạp thực sự dương, ta mới cộng dồn vào số dư hiện tại.",
        "Dạ thưa thầy, nếu không có câu lệnh kiểm tra if (depositAmount > 0.0m), kẻ xấu có thể lợi dụng phương thức nạp tiền Deposit nhưng lại truyền vào số tiền âm để biến việc nạp tiền thành hành vi rút trộm tiền đúng không ạ?",
        "Tư duy bảo mật của em quá sắc bén! Đúng là như vậy! Thiếu validation trong phương thức nghiệp vụ chính là lỗ hổng bảo mật chết người mà các tin tặc thường khai thác để tấn công hệ thống tài chính!"
    ),
    # Slide 36
    (
        "Khảo sát AccountTest.cs: Khởi tạo & In Tiền tệ (Hình 4.12 - Phần 1)",
        "Bây giờ chúng ta cùng khảo sát tệp AccountTest.cs nâng cấp trong Hình 4.12 trên Slide 36. Tại dòng 9 và dòng 11, chúng ta khởi tạo hai tài khoản: account1 của Jane Green với số dư ban đầu hợp lệ là 50.00m; và account2 của John Blue với số dư ban đầu không hợp lệ là -7.53m. Sau đó, chương trình in thông tin tài khoản ra màn hình. Kết quả in ra: Jane Green có số dư là 50.00 đô la, còn John Blue có số dư là 0.00 đô la! Số tiền âm -7.53m đã bị cơ chế validation trong hàm tạo chặn lại hoàn toàn, bảo vệ tài khoản của John Blue không bị âm tiền ngay từ đầu!",
        "Dạ, nhìn thấy kết quả chạy thực tế hiển thị John Blue balance: $0.00 làm em càng khâm phục cơ chế kiểm soát dữ liệu của hướng đối tượng thầy ạ!"
    ),
    # Slide 37
    (
        "Khảo sát AccountTest.cs: Nạp tiền & Cập nhật Số dư (Hình 4.12 - Phần 2)",
        "Chúng ta sang tiếp Hình 4.12 phần 2 trên Slide 37: Thực hiện giao dịch nạp tiền. Tại dòng 19, chương trình nhắc người dùng nhập số tiền nạp cho account1. Người dùng nhập 25.45. Chương trình đọc vào biến depositAmount bằng decimal.Parse(Console.ReadLine()) rồi gọi: account1.Deposit(depositAmount);. Ngay lập tức, số dư của Jane Green được cập nhật chính xác từ 50.00 đô la lên thành 75.45 đô la! Tiếp theo, người dùng nhập số tiền nạp cho account2 là 124.59. Chương trình gọi account2.Deposit(depositAmount); và số dư của John Blue tăng chuẩn xác từ 0.00 lên 124.59 đô la. Mọi phép cộng tiền tệ đều chính xác tuyệt đối từng xu một!",
        "Dạ thưa thầy, ở các dòng lệnh in số dư, em thấy có ký hiệu rất lạ nằm trong dấu ngoặc nhọn: {account1.Balance:C}. Ký hiệu hai chấm C đó có ý nghĩa gì ạ?"
    ),
    # Slide 38
    (
        "Kỹ thuật Định dạng Tiền tệ với Ký tự :C (Currency Format)",
        "Đó chính là nội dung của Slide 38: Kỹ thuật Định dạng Tiền tệ với Ký tự Định dạng :C (Currency Format Specifier)! Khi sử dụng tính năng nội suy chuỗi String Interpolation bắt đầu bằng dấu đô la $, chúng ta có thể đặt một Ký tự Định dạng (Format Specifier) ở phía sau tên biến, ngăn cách bởi dấu hai chấm :. Ký hiệu :C thông báo cho môi trường .NET biết rằng: hãy hiển thị con số này dưới dạng Tiền tệ chuẩn quốc tế! Hệ thống sẽ tự động thêm ký hiệu tiền tệ (ví dụ dấu $ ở Mỹ hoặc chữ đ ở Việt Nam), tự động thêm dấu phân cách hàng nghìn (dấu phẩy hoặc dấu chấm), và tự động làm tròn chuẩn xác đến 2 chữ số phần thập phân. Các em không cần phải viết hàng chục dòng code chia tách chuỗi phức tạp!",
        "Dạ thưa thầy, nếu ứng dụng này chạy trên hệ điều hành Windows cài đặt vùng ngôn ngữ là Tiếng Việt thì :C sẽ tự động hiển thị đơn vị tiền tệ là đồng Việt Nam đúng không ạ?",
        "Chính xác 100%! .NET sẽ dựa vào CultureInfo của hệ điều hành để hiển thị đúng định dạng tiền tệ của quốc gia đó, cực kỳ chuyên nghiệp!"
    ),
    # Slide 39
    (
        "Bảng Tra cứu Ký tự Định dạng Chuỗi Thông dụng trong .NET (Hình 4.13)",
        "Slide 39 cung cấp Bảng Tra cứu các Ký tự Định dạng Chuỗi Thông dụng trong .NET theo Hình 4.13 giáo trình mà mọi lập trình viên đều phải thuộc lòng: Ký tự C định dạng Tiền tệ (Currency) với 2 chữ số thập phân và ký hiệu tiền tệ. Ký tự D định dạng Số nguyên thập phân (Decimal integer), thường dùng để chèn thêm các số 0 ở đầu mã số sinh viên hay mã hóa đơn (ví dụ: {12:D5} sẽ in ra 00012). Ký tự E định dạng Số mũ khoa học (Scientific notation). Ký tự F định dạng Số thực dấu phẩy tĩnh (Fixed-point), cho phép chỉ định số chữ số thập phân mong muốn (ví dụ: {x:F3} lấy 3 chữ số thập phân). Ký tự G định dạng Tổng quát (General). Ký tự N định dạng Số có dấu phẩy phân cách hàng nghìn (Number). Và ký tự P định dạng Phần trăm (Percentage), tự động nhân số với 100 và thêm ký hiệu % ở cuối! Bảng này là cẩm nang gối đầu giường khi thiết kế giao diện xuất báo cáo dữ liệu.",
        "Dạ, bảng tra cứu này quá tiện lợi thầy ạ! Sau này khi in bảng điểm sinh viên hay xuất báo cáo thống kê doanh số, chúng em chỉ cần áp dụng các ký tự định dạng này là bảng biểu sẽ ngay ngắn và chuẩn mực ạ!"
    ),
    # Slide 40
    (
        "Sơ đồ lớp UML Toàn diện của Lớp Account Hoàn chỉnh (Hình 4.14)",
        "Slide 40 là bức tranh toàn cảnh: Sơ đồ lớp UML Toàn diện của Lớp Account Hoàn chỉnh theo Hình 4.14 giáo trình. Các em hãy nhìn lại cấu trúc 3 ngăn hoàn chỉnh: Ngăn 1 là tên lớp Account. Ngăn 2 gồm hai biến thể hiện private: - name : string và - balance : decimal. Ngăn 3 gồm hàm tạo có hai tham số: + Account(accountName : string, initialBalance : decimal), hai thuộc tính: + Name : string «get/set» và + Balance : decimal «get», cùng phương thức nghiệp vụ: + Deposit(depositAmount : decimal). Đây là một thiết kế mẫu mực của ngành công nghệ phần mềm: các thuộc tính dữ liệu được bảo vệ an toàn tối đa, các hành vi bên ngoài được kiểm soát chặt chẽ qua giao diện public rõ ràng!",
        "Dạ thưa thầy, nhìn vào sơ đồ UML hoàn chỉnh này, chúng em thấy rõ sự trưởng thành của lớp Account: từ một lớp đơn giản chỉ có tên ở Tiết 1, giờ đây đã trở thành một lớp thực thể ngân hàng hoàn chỉnh, có số dư an toàn và phương thức giao dịch nghiệp vụ chuẩn mực ạ!"
    ),
    # Slide 41
    (
        "Các Lỗi Lập trình Kinh điển Cần Tránh trong OOP C#",
        "Trước khi bước vào phần thực hành tổng hợp, Slide 41 cảnh báo 4 Cạm bẫy Lập trình Kinh điển mà sinh viên mới học OOP rất hay mắc phải: Lỗi 1: Khai báo lại kiểu dữ liệu trong hàm tạo (ví dụ viết string Name = accountName; trong Constructor). Khi đó các em vừa tạo ra một biến cục bộ trùng tên và che khuất thuộc tính của lớp, dữ liệu truyền vào sẽ biến mất ngay khi hàm tạo kết thúc! Lỗi 2: Nhầm lẫn dấu bằng trong bộ truy cập set của Property (viết value = name; thay vì name = value;). Lỗi này khiến biến thể hiện không nhận được dữ liệu mới mà giá trị của value bị mất! Lỗi 3: Đệ quy vô hạn trong Property (viết public string Name { get { return Name; } }). Ở đây thay vì trả về backing field name chữ thường, các em lại gọi chính Name chữ hoa, dẫn đến vòng lặp vô tận và làm sụp đổ chương trình với lỗi tràn ngăn xếp StackOverflowException! Và Lỗi 4: Gọi phương thức trên biến mang giá trị null gây ra ngoại lệ NullReferenceException khét tiếng!",
        "Dạ thưa thầy, 4 lỗi này em thấy rất nhiều bạn trong lớp từng gặp phải khi gõ code nhầm chữ hoa chữ thường ạ. Slide cảnh báo này thực sự rất giá trị giúp chúng em tránh được hàng giờ ngồi sửa lỗi mò mẫm ạ!"
    ),
    # Slide 42
    (
        "Tái cấu trúc Mã nguồn: Phương thức Dùng chung DisplayAccount (Exercise 4.13)",
        "Slide 42 hướng dẫn các em một kỹ năng tối quan trọng trong công nghiệp phần mềm: Tái cấu trúc Mã nguồn (Code Refactoring) theo Bài tập 4.13 của giáo trình Deitel. Trong tệp AccountTest.cs ban đầu, các em thấy các câu lệnh in tên và số dư tài khoản bị lặp đi lặp lại tới 4 lần! Quy tắc vàng của lập trình sạch Clean Code là: Đừng lặp lại chính mình (DRY - Don't Repeat Yourself)! Thay vì lặp code, chúng ta thiết kế một phương thức dùng chung trong AccountTest: public static void DisplayAccount(Account accountToDisplay) { Console.WriteLine($\"{accountToDisplay.Name}'s balance: {accountToDisplay.Balance:C}\"); }. Phương thức này tiếp nhận một tham số là đối tượng Account. Mỗi khi cần in, ta chỉ cần gọi một dòng duy nhất: DisplayAccount(account1); hoặc DisplayAccount(account2);. Mã nguồn ngắn gọn hơn một nửa, dễ đọc và khi cần thay đổi định dạng in, ta chỉ cần sửa đúng một nơi duy nhất!",
        "Dạ thưa thầy, nguyên lý DRY - Đừng lặp lại chính mình quả là chân lý ạ! Tách thành phương thức DisplayAccount giúp mã nguồn sáng sủa, thanh lịch và mang phong cách của một lập trình viên chuyên nghiệp thực thụ ạ!"
    ),
    # Slide 43
    (
        "Mở rộng Nghiệp vụ: Thiết kế Phương thức Rút tiền Withdraw (Exercise 4.11)",
        "Để chuẩn bị cho bài Lab lớn, Slide 43 hướng dẫn các em mở rộng nghiệp vụ ngân hàng: Thiết kế Phương thức Rút tiền Withdraw theo Bài tập 4.11 của giáo trình. Một tài khoản có nạp tiền thì bắt buộc phải có rút tiền! Cú pháp phương thức: public void Withdraw(decimal withdrawalAmount). Thuật toán xử lý gồm 2 bước kiểm tra validation chặt chẽ: Bước 1: Kiểm tra số tiền yêu cầu rút phải là số dương (withdrawalAmount > 0.0m). Bước 2: Kiểm tra số dư khả dụng xem có đủ tiền để rút hay không: if (withdrawalAmount <= Balance) { Balance = Balance - withdrawalAmount; }. Nếu khách hàng yêu cầu rút số tiền lớn hơn số dư hiện có trong tài khoản (thấu chi / overdraft), chương trình tuyệt đối không trừ tiền, mà in ra dòng cảnh báo chuẩn mực: \"Withdrawal amount exceeded account balance.\" (Số tiền rút vượt quá số dư tài khoản)!",
        "Dạ, phương thức Withdraw này mô phỏng chính xác hành vi của cây ATM ngoài đời thực thầy ạ: nếu tài khoản chỉ có 1 triệu mà bấm rút 2 triệu thì máy ATM sẽ báo số dư không đủ và nhả thẻ ra chứ không thể cho rút âm tiền được ạ!"
    ),
    # Slide 44
    (
        "[HANDS-ON LAB 3] Xây dựng Hệ thống ATM Quản lý Tài khoản (25 Phút)",
        "Và bây giờ là 25 phút thực hành đỉnh cao của buổi học: [HANDS-ON LAB 3] Xây dựng Hệ thống ATM Quản lý Tài khoản Mini ATM System! Yêu cầu thực hành dành cho tất cả các bạn sinh viên lớp IT26M: Nhiệm vụ 1: Hoàn thiện lớp Account.cs với đầy đủ hai thuộc tính Name, Balance (private set), hàm tạo 2 tham số, phương thức Deposit(amount) và phương thức Withdraw(amount) có cơ chế chặn thấu chi overdraft. Nhiệm vụ 2: Xây dựng lớp Program.cs cung cấp một Vòng lặp Menu giao diện Console tương tác: 1. Xem số dư tài khoản; 2. Nạp tiền (Deposit); 3. Rút tiền (Withdraw); 4. Thoát hệ thống. Nhiệm vụ 3: Sử dụng phương thức dùng chung DisplayAccount và định dạng tiền tệ chuẩn :C cho mọi thông báo số dư. Các em có 25 phút để hoàn thành và nộp bài trên hệ thống LMS!",
        "Dạ thưa thầy, bài tập Lab 3 này tổng hợp toàn bộ tinh hoa kiến thức của cả 3 tiết học hôm nay: từ Lớp, Đối tượng, Thuộc tính, Hàm tạo, kiểu decimal, Validation đến menu điều khiển vòng lặp. Chúng em sẽ bắt tay vào code ngay bây giờ để hoàn thành xuất sắc hệ thống Mini ATM này ạ!"
    ),
    # Slide 45
    (
        "Tổng kết 5 Chuẩn đầu ra (CLOs) & Chuẩn bị Chương 5",
        "Tuyệt vời! Như vậy chúng ta đã hoàn thành trọn vẹn buổi học Chương 4 vô cùng hiệu quả và bổ ích. Nhìn lên Slide 45, thầy trò chúng ta cùng điểm lại 5 Chuẩn đầu ra (CLOs) mà cả lớp IT26M đã xuất sắc chinh phục hôm nay: CLO 4.1: Phân biệt bản chất Lớp và Đối tượng, hiểu rõ cơ chế vùng nhớ Heap/Stack của toán tử new và sự khác nhau giữa Kiểu Tham chiếu vs Kiểu Giá trị. CLO 4.2: Thành thạo nguyên lý Đóng gói và Ẩn giấu dữ liệu với biến private và phương thức Get/Set. CLO 4.3: Sử dụng nhuần nhuyễn Thuộc tính C# (Properties) và cú pháp Thuộc tính Tự động siêu tốc. CLO 4.4: Định nghĩa và nạp chồng Hàm tạo (Constructors) để bảo đảm đối tượng luôn được khai sinh ở trạng thái hợp lệ. Và CLO 4.5: Làm chủ kiểu số thực chính xác cao decimal, kỹ thuật Data Validation, định dạng tiền tệ :C và xây dựng thành công ứng dụng ngân hàng Mini ATM. Về nhà, các em hoàn thiện các bài tập cuối chương trong giáo trình Deitel và đọc trước Chương 5: Cấu trúc Điều khiển Phần 1 để chuẩn bị cho buổi học tiếp theo. Chúc các em học tập thật tốt và hẹn gặp lại các em vào tuần tới!",
        "Dạ, chúng em xin chân thành cảm ơn thầy vì một buổi học cực kỳ lôi cuốn, chi tiết và tràn đầy cảm hứng lập trình ạ! Chúng em đã nắm rất chắc tư duy hướng đối tượng và sẽ hoàn thành đầy đủ bài tập về nhà để sẵn sàng cho Chương 5 ạ. Kính chúc thầy nhiều sức khỏe ạ!"
    )
]

# Write to both script.txt and scriptDemo.txt
def write_dialogue(filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        for idx, item in enumerate(slides_content, 1):
            title = item[0]
            f.write(f"Slide {idx}: {title}\n")
            for turn_idx, text in enumerate(item[1:]):
                speaker = "Người 1" if turn_idx % 2 == 0 else "Người 2"
                f.write(f"{speaker}: {text}\n")
            f.write("\n")

write_dialogue(SCRIPT_PATH)
write_dialogue(SCRIPTDEMO_PATH)
print(f"Successfully generated {SCRIPT_PATH} and {SCRIPTDEMO_PATH} ({len(slides_content)} slides)")
