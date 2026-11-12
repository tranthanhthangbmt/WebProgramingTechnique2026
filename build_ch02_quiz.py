# -*- coding: utf-8 -*-
import json
import random

# 40 Questions for Chapter 2
# Format: id, category, bloom, question, options (list of 4), answer (index 0..3), explanation

raw_questions = [
    # 1
    {
        "id": 1,
        "category": "Tổng quan IDE",
        "bloom": "Remember",
        "question": "Thuật ngữ IDE trong phát triển phần mềm Visual C# là viết tắt của cụm từ nào sau đây?",
        "options": [
            "Integrated Development Environment - Môi trường phát triển tích hợp.",
            "Internal Design Engine - Động cơ thiết kế đồ họa nội bộ hệ thống.",
            "Interactive Data Execution - Môi trường thực thi dữ liệu tương tác.",
            "Interface Deployment Editor - Trình biên tập triển khai giao diện."
        ],
        "answer": 0,
        "explanation": "IDE là viết tắt của Integrated Development Environment (Môi trường phát triển tích hợp), gói phần mềm gom toàn bộ trình soạn thảo mã, trình biên dịch, trình thiết kế trực quan và bộ dò lỗi trên một giao diện thống nhất."
    },
    # 2
    {
        "id": 2,
        "category": "Triết lý RAD",
        "bloom": "Understand",
        "question": "Mục tiêu cốt lõi của triết lý Phát triển Ứng dụng Nhanh (Rapid Application Development - RAD) trong Windows Forms là gì?",
        "options": [
            "Giảm thiểu việc viết mã thủ công bằng cách tái sử dụng linh kiện và kéo thả tạo mẫu nhanh.",
            "Loại bỏ hoàn toàn mã nguồn C# và chỉ sử dụng các tệp tin cấu hình nhị phân để chạy phần mềm.",
            "Bắt buộc lập trình viên phải tự viết mã giao diện bằng tay ở cấp độ đồ họa điểm ảnh pixel.",
            "Tự động tối ưu hóa tốc độ xung nhịp phần cứng của vi xử lý CPU khi phần mềm đang hoạt động."
        ],
        "answer": 0,
        "explanation": "Triết lý RAD tập trung vào việc tạo mẫu nhanh (Prototyping), tái sử dụng tối đa các linh kiện có sẵn trong thư viện .NET Framework Class Library (FCL) và kéo thả trực quan để rút ngắn thời gian phát triển ứng dụng."
    },
    # 3
    {
        "id": 3,
        "category": "Tổng quan IDE",
        "bloom": "Remember",
        "question": "Phiên bản Visual Studio nào sau đây được Microsoft cung cấp miễn phí đầy đủ tính năng phục vụ sinh viên, giảng viên và nghiên cứu cá nhân?",
        "options": [
            "Visual Studio Enterprise.",
            "Visual Studio Professional.",
            "Visual Studio Community.",
            "Visual Studio Ultimate."
        ],
        "answer": 2,
        "explanation": "Visual Studio Community là ấn bản miễn phí bản quyền đầy đủ tính năng dành cho sinh viên, giảng viên, nhà nghiên cứu cá nhân và các dự án mã nguồn mở theo quy định của Microsoft."
    },
    # 4
    {
        "id": 4,
        "category": "Giao diện Visual Studio",
        "bloom": "Remember",
        "question": "Khu vực 'Recent' trên màn hình Start Page của Visual Studio có công dụng chính là gì?",
        "options": [
            "Hiển thị danh sách các dự án và giải pháp vừa mở gần đây giúp lập trình viên truy cập nhanh chóng.",
            "Liệt kê danh sách các bản cập nhật phần cứng và bản vá bảo mật mới nhất của hệ điều hành Windows.",
            "Tự động sao lưu toàn bộ mã nguồn của giải pháp lên các máy chủ điện toán đám mây công cộng.",
            "Hiển thị toàn bộ các lỗi cú pháp lập trình còn đọng lại từ phiên làm việc trước của máy tính."
        ],
        "answer": 0,
        "explanation": "Khu vực Recent trên Start Page liệt kê các giải pháp (Solutions) và dự án (Projects) đã làm việc gần nhất, cho phép nhấp chuột mở lại tức thì mà không cần duyệt thư mục ổ đĩa."
    },
    # 5
    {
        "id": 5,
        "category": "Khởi tạo Dự án",
        "bloom": "Apply",
        "question": "Để tạo một ứng dụng giao diện đồ họa cửa sổ trên máy tính để bàn bằng C#, lập trình viên chọn mẫu dự án nào trong hộp thoại New Project?",
        "options": [
            "Console Application.",
            "Windows Forms Application.",
            "Class Library.",
            "WCF Service Application."
        ],
        "answer": 1,
        "explanation": "Mẫu 'Windows Forms Application' trong nhánh Visual C# -> Windows được sử dụng để xây dựng ứng dụng máy tính đồ họa trực quan chuẩn mực trên nền tảng .NET."
    },
    # 6
    {
        "id": 6,
        "category": "Khởi tạo Dự án",
        "bloom": "Understand",
        "question": "Tại sao khi đặt tên cho dự án trong ô 'Name' của hộp thoại New Project, ta nên tuân thủ quy tắc viết liền không dấu cách và không có ký tự đặc biệt?",
        "options": [
            "Vì tên dự án sẽ tự động trở thành Namespace mặc định và tên tệp thực thi .exe của ứng dụng.",
            "Vì hệ điều hành Windows sẽ ngay lập tức từ chối lưu trữ các tệp tin có khoảng trắng trên ổ đĩa.",
            "Vì trình biên dịch C# không hỗ trợ lưu trữ tệp tin trên các phân vùng định dạng chuẩn NTFS.",
            "Vì việc đặt dấu cách sẽ làm tăng gấp đôi dung lượng bộ nhớ RAM mà ứng dụng chiếm dụng khi chạy."
        ],
        "answer": 0,
        "explanation": "Tên dự án được Visual Studio sử dụng làm Không gian tên mặc định (Default Namespace) và tên file nhị phân đầu ra (.exe). Nếu chứa dấu cách hoặc ký tự đặc biệt, nó có thể gây xung đột đường dẫn và định danh cú pháp."
    },
    # 7
    {
        "id": 7,
        "category": "Khởi tạo Dự án",
        "bloom": "Understand",
        "question": "Tùy chọn 'Create directory for solution' trong hộp thoại New Project mang lại lợi ích kỹ thuật quan trọng nào?",
        "options": [
            "Tự động đóng gói giải pháp và các dự án con vào một thư mục riêng biệt giúp quản lý khoa học.",
            "Khóa quyền chỉnh sửa tệp tin để ngăn chặn người khác xem mã nguồn của giải pháp trên máy tính.",
            "Tự động tải toàn bộ mã nguồn lên kho lưu trữ trực tuyến GitHub ngay khi vừa khởi tạo dự án.",
            "Bắt buộc tất cả các tệp tin mã nguồn C# phải được mã hóa nhị phân 128-bit trước khi lưu đĩa."
        ],
        "answer": 0,
        "explanation": "Tích chọn 'Create directory for solution' giúp tạo một thư mục cha bao bọc toàn bộ solution (.sln) và các thư mục project con (.csproj), giúp cấu trúc tệp gọn gàng, độc lập và thuận tiện nén gửi bài hoặc quản lý git."
    },
    # 8
    {
        "id": 8,
        "category": "Design View",
        "bloom": "Understand",
        "question": "Khung nhìn Thiết kế Trực quan (Design View) của Windows Forms đóng vai trò gì trong quá trình phát triển phần mềm?",
        "options": [
            "Là tấm toan vẽ trực quan mô phỏng giao diện cửa sổ ứng dụng thực tế để kéo thả linh kiện.",
            "Là trình soạn thảo văn bản thuần túy chỉ cho phép gõ mã nguồn C# mà không có bất kỳ đồ họa nào.",
            "Là môi trường chạy thử nghiệm dòng lệnh console để kiểm tra tốc độ thực thi của thuật toán.",
            "Là cửa sổ dành riêng cho quản trị viên hệ thống cấu hình các cổng kết nối mạng Internet."
        ],
        "answer": 0,
        "explanation": "Design View là không gian thiết kế WYSIWYG, hiển thị trực quan bề mặt của Form như một tấm toan vẽ (Canvas) cho phép lập trình viên kéo thả, định vị và căn chỉnh các điều khiển đồ họa."
    },
    # 9
    {
        "id": 9,
        "category": "Design View",
        "bloom": "Apply",
        "question": "Các ô vuông nhỏ màu trắng (Sizing handles) xuất hiện ở 4 góc và 4 cạnh của Form khi được chọn dùng để làm gì?",
        "options": [
            "Nhấp giữ chuột và kéo để thay đổi kích thước chiều rộng và chiều cao của Form một cách trực quan.",
            "Nhấp chuột để khóa cố định Form không cho phép bất kỳ thay đổi nào về mặt giao diện.",
            "Xóa vĩnh viễn Form hiện hành ra khỏi dự án phần mềm đang mở trong Visual Studio.",
            "Tự động đổi màu nền của Form sang màu trắng mặc định của hệ điều hành Windows."
        ],
        "answer": 0,
        "explanation": "Sizing handles (chốt điều chỉnh kích thước) xuất hiện xung quanh điều khiển đang được chọn; rê chuột vào sẽ hiển thị mũi tên hai chiều cho phép kéo giãn để tăng giảm kích thước linh hoạt."
    },
    # 10
    {
        "id": 10,
        "category": "Hệ thống Menu",
        "bloom": "Remember",
        "question": "Khi vô tình đóng mất một cửa sổ công cụ như Solution Explorer hay Toolbox, lập trình viên truy cập vào menu nào trên Menu Bar để mở lại?",
        "options": [
            "Menu File.",
            "Menu Edit.",
            "Menu View.",
            "Menu Tools."
        ],
        "answer": 2,
        "explanation": "Menu View là trung tâm quản lý hiển thị của IDE, chứa các lệnh mở lại tất cả các cửa sổ công cụ như Solution Explorer (Ctrl+Alt+L), Toolbox (Ctrl+Alt+X), Properties Window (F4), Error List, v.v."
    },
    # 11
    {
        "id": 11,
        "category": "Hệ thống Menu",
        "bloom": "Analyze",
        "question": "Sự khác biệt cốt lõi giữa lệnh 'Build Solution' và lệnh 'Rebuild Solution' trong menu Build là gì?",
        "options": [
            "Build chỉ biên dịch các tệp vừa sửa, còn Rebuild xóa sạch file nhị phân cũ trong bin/obj rồi dịch lại toàn bộ.",
            "Build sẽ biên dịch mã nguồn sang ngôn ngữ máy, còn Rebuild chỉ kiểm tra lỗi chính tả tiếng Anh.",
            "Build sẽ thực thi chạy ứng dụng ngay lập tức, còn Rebuild chỉ lưu các tệp tin xuống đĩa cứng.",
            "Build dành riêng cho phiên bản C# cũ, còn Rebuild bắt buộc phải kết nối với máy chủ đám mây."
        ],
        "answer": 0,
        "explanation": "Build Solution thực hiện biên dịch gia tăng (Incremental Build) chỉ với các tệp có sửa đổi để tiết kiệm thời gian; trong khi Rebuild Solution dọn sạch toàn bộ tệp nhị phân đầu ra cũ rồi biên dịch lại từ đầu 100% để loại bỏ lỗi đọng bộ nhớ cache."
    },
    # 12
    {
        "id": 12,
        "category": "Thực thi Ứng dụng",
        "bloom": "Analyze",
        "question": "Phím tắt F5 (Start Debugging) khác với tổ hợp phím Ctrl + F5 (Start Without Debugging) ở điểm then chốt nào?",
        "options": [
            "F5 chạy ứng dụng kèm trình giám sát lỗi Debugger, còn Ctrl+F5 chạy ứng dụng độc lập với hiệu năng tối đa.",
            "F5 chỉ biên dịch mã nguồn chứ không chạy, còn Ctrl+F5 vừa biên dịch vừa chạy ứng dụng.",
            "F5 dành riêng cho ứng dụng Console, còn Ctrl+F5 chỉ áp dụng cho ứng dụng đồ họa Windows Forms.",
            "F5 yêu cầu quyền quản trị viên Administrator, còn Ctrl+F5 cho phép người dùng khách sử dụng."
        ],
        "answer": 0,
        "explanation": "F5 kích hoạt Start Debugging, gắn tiến trình phần mềm vào bộ dò lỗi của Visual Studio để bắt Exception và điểm dừng Breakpoints. Ctrl+F5 chạy độc lập không qua Debugger, cho tốc độ thực thi cao nhất."
    },
    # 13
    {
        "id": 13,
        "category": "Hệ thống Menu",
        "bloom": "Apply",
        "question": "Menu nào trên thanh Menu Bar cung cấp các lệnh căn lề (Align), chỉnh kích thước đều nhau (Make Same Size) và giãn khoảng cách (Spacing) khi chọn nhiều điều khiển?",
        "options": [
            "Menu Project.",
            "Menu Format.",
            "Menu Debug.",
            "Menu Tools."
        ],
        "answer": 1,
        "explanation": "Menu Format xuất hiện khi chọn từ hai điều khiển trở lên trên Form, cung cấp các công cụ dàn trang chuyên nghiệp: căn thẳng hàng (Align), chỉnh bằng kích thước (Make Same Size) và giãn cách đều nhau (Spacing)."
    },
    # 14
    {
        "id": 14,
        "category": "Standard Toolbar",
        "bloom": "Apply",
        "question": "Tại sao trong quá trình thiết kế giao diện Windows Forms, thao tác bấm 'Save All' (Ctrl + Shift + S) được xem là nguyên tắc làm việc bắt buộc?",
        "options": [
            "Vì một thay đổi giao diện làm biến động đồng thời cả Form1.cs, Form1.Designer.cs và Form1.resx ngầm bên dưới.",
            "Vì nếu chỉ bấm Save thường thì toàn bộ tệp tin hình ảnh đã nạp vào dự án sẽ bị xóa khỏi bộ nhớ.",
            "Vì thao tác Save All sẽ tự động kích hoạt trình biên dịch chuyển đổi mã nguồn sang tệp cài đặt .msi.",
            "Vì Visual Studio sẽ khóa không cho phép lập trình viên chạy thử chương trình nếu chưa bấm Save All."
        ],
        "answer": 0,
        "explanation": "Một thao tác kéo thả trên Form Designer tác động đồng thời lên nhiều tệp: Form1.cs, Form1.Designer.cs và tệp tài nguyên Form1.resx. Bấm Save All (Ctrl+Shift+S) đảm bảo toàn bộ các tệp liên quan được ghi xuống đĩa đồng bộ."
    },
    # 15
    {
        "id": 15,
        "category": "Standard Toolbar",
        "bloom": "Remember",
        "question": "Tính năng hiển thị một nhãn văn bản nhỏ màu vàng giải thích chức năng của nút bấm khi rê chuột qua nút công cụ được gọi là gì?",
        "options": [
            "Context Menu.",
            "Tooltip.",
            "Status Bar.",
            "Smart Tag."
        ],
        "answer": 1,
        "explanation": "Tooltip (chú giải công cụ) là hộp nhãn nhỏ xuất hiện khi người dùng rê chuột qua một nút bấm hoặc biểu tượng, hiển thị tên thao tác và tổ hợp phím tắt tương ứng trong dấu ngoặc đơn."
    },
    # 16
    {
        "id": 16,
        "category": "Phím tắt Chuẩn",
        "bloom": "Remember",
        "question": "Phím tắt mặc định trong Visual Studio dùng để kích hoạt hiển thị Cửa sổ Thuộc tính (Properties Window) là phím nào?",
        "options": [
            "F2.",
            "F4.",
            "F7.",
            "F12."
        ],
        "answer": 1,
        "explanation": "Phím F4 là phím tắt kinh điển trong Visual Studio dùng để mở hoặc di chuyển tiêu điểm trực tiếp đến cửa sổ Properties Window của điều khiển đang được chọn."
    },
    # 17
    {
        "id": 17,
        "category": "Trợ giúp Ngữ cảnh",
        "bloom": "Understand",
        "question": "Tính năng Trợ giúp Ngữ cảnh (Context-Sensitive Help) kích hoạt bằng phím F1 mang lại ưu điểm vượt trội nào cho lập trình viên?",
        "options": [
            "Tự động mở đúng trang tài liệu MSDN / Microsoft Learn mô tả cặn kẽ về điều khiển hoặc từ khóa đang chọn.",
            "Tự động sửa toàn bộ các lỗi cú pháp trong mã nguồn mà không cần lập trình viên phải can thiệp.",
            "Gửi yêu cầu trợ giúp trực tiếp đến bộ phận kỹ thuật của Microsoft qua đường truyền video call.",
            "Tự động hoàn thành toàn bộ bài tập lớn và đồ án học phần cho sinh viên lớp IT26M."
        ],
        "answer": 0,
        "explanation": "Context-Sensitive Help nhận diện chính xác ngữ cảnh đang thao tác (điều khiển trên Form hoặc từ khóa trong code) và nhấn phím F1 sẽ mở ngay tài liệu chính thức từ Microsoft Learn tương ứng với phần tử đó."
    },
    # 18
    {
        "id": 18,
        "category": "Điều hướng Cửa sổ",
        "bloom": "Understand",
        "question": "Khi biểu tượng chiếc đinh ghim (Pushpin) trên thanh tiêu đề của một cửa sổ công cụ nằm ở vị trí nằm ngang, cửa sổ đang ở chế độ nào?",
        "options": [
            "Chế độ Ghim cố định (Pinned).",
            "Chế độ Tự động ẩn (Auto-Hide).",
            "Chế độ Cửa sổ nổi (Floating).",
            "Chế độ Đóng vĩnh viễn (Closed)."
        ],
        "answer": 1,
        "explanation": "Khi đinh ghim xoay ngang (Horizontal pin), tính năng Auto-Hide được kích hoạt: cửa sổ thu gọn thành tab dọc ở mép màn hình và chỉ trượt ra khi rê chuột vào, tự động thụt lại khi rê chuột ra ngoài."
    },
    # 19
    {
        "id": 19,
        "category": "Điều hướng Cửa sổ",
        "bloom": "Apply",
        "question": "Biểu tượng điều hướng ghép nối (Docking Visualizer) hình chữ thập với 4 mũi tên xuất hiện khi nào trong Visual Studio?",
        "options": [
            "Khi lập trình viên nhấp giữ thanh tiêu đề của một cửa sổ công cụ và kéo di chuyển trên màn hình.",
            "Khi chương trình C# gặp phải một lỗi ngoại lệ nghiêm trọng trong quá trình biên dịch mã.",
            "Khi máy tính bị mất kết nối Internet trong lúc đang tải các gói thư viện NuGet từ bên ngoài.",
            "Khi lập trình viên nhấn tổ hợp phím Ctrl + Alt + Delete trên bàn phím máy tính phòng máy."
        ],
        "answer": 0,
        "explanation": "Docking Visualizer xuất hiện khi kéo thanh tiêu đề cửa sổ, cho phép thả chuột vào các mũi tên định hướng (trên, dưới, trái, phải) hoặc tâm ở giữa để neo (dock) cửa sổ vào cạnh màn hình hoặc gộp thành tab."
    },
    # 20
    {
        "id": 20,
        "category": "Điều hướng Cửa sổ",
        "bloom": "Apply",
        "question": "Lệnh nào sau đây giúp khôi phục toàn bộ cách bố trí cửa sổ trong Visual Studio về trạng thái xuất xưởng mặc định khi giao diện bị xáo trộn?",
        "options": [
            "Window -> Reset Window Layout.",
            "Tools -> Options -> Environment -> Clear.",
            "File -> Revert Workspace.",
            "View -> Restore All Toolbars."
        ],
        "answer": 0,
        "explanation": "Lệnh Window -> Reset Window Layout trên thanh Menu Bar sẽ ngay lập tức khôi phục toàn bộ vị trí, kích thước và trạng thái ghim của tất cả các cửa sổ trong IDE về bố cục chuẩn mặc định."
    },
    # 21
    {
        "id": 21,
        "category": "Solution Explorer",
        "bloom": "Understand",
        "question": "Trong kiến trúc quản trị dự án của Visual Studio, mối quan hệ giữa Solution (.sln) và Project (.csproj) được định nghĩa như thế nào?",
        "options": [
            "Một Solution là tập hợp bao bọc chứa một hoặc nhiều Project thành viên cùng phục vụ giải pháp phần mềm.",
            "Một Project là cấp cao nhất chứa nhiều Solution con độc lập bên trong cấu trúc thư mục.",
            "Solution và Project là hai định dạng tệp tin hoàn toàn giống nhau và có thể đổi tên đuôi mở rộng tùy ý.",
            "Một Solution chỉ được phép chứa duy nhất một Project và không thể thêm bất kỳ dự án nào khác."
        ],
        "answer": 0,
        "explanation": "Solution (đuôi .sln) là thùng chứa cấp cao nhất quản lý một hoặc nhiều Project (.csproj) liên kết với nhau (ví dụ: project WinForms GUI, project Class Library, project Unit Test)."
    },
    # 22
    {
        "id": 22,
        "category": "Giải phẫu Dự án",
        "bloom": "Understand",
        "question": "Tệp tin nào trong dự án Windows Forms là nơi lập trình viên trực tiếp viết mã xử lý nghiệp vụ và các hàm phản hồi sự kiện (Event Handlers)?",
        "options": [
            "Form1.cs.",
            "Form1.Designer.cs.",
            "Form1.resx.",
            "App.config."
        ],
        "answer": 0,
        "explanation": "Tệp Form1.cs là nơi lập trình viên viết code xử lý logic, tính toán nghiệp vụ và các phương thức xử lý sự kiện (như click nút bấm, nhập văn bản)."
    },
    # 23
    {
        "id": 23,
        "category": "Giải phẫu Dự án",
        "bloom": "Analyze",
        "question": "Tại sao trong tệp Form1.Designer.cs, Microsoft lại đặt lời cảnh báo: 'Do not modify the contents of this method with the code editor' tại phương thức InitializeComponent()?",
        "options": [
            "Vì phương thức này do Form Designer tự động sinh ra và đồng bộ lại mỗi khi lập trình viên kéo thả trên giao diện.",
            "Vì phương thức này chứa mã nguồn bản quyền được mã hóa cứng của tập đoàn công nghệ Microsoft.",
            "Vì việc sửa mã tại đây sẽ làm hỏng trình điều khiển cạc đồ họa GPU của máy tính vĩnh viễn.",
            "Vì phương thức này chỉ được phép chỉnh sửa trên máy chủ của trường Đại học Đông Á."
        ],
        "answer": 0,
        "explanation": "InitializeComponent() hoàn toàn do công cụ trực quan Form Designer kiểm soát. Khi lập trình viên kéo thả hay đổi thuộc tính, IDE tự động ghi đè mã nguồn vào phương thức này. Việc sửa tay có thể làm bộ phân tích thiết kế (Design Parser) bị lỗi cú pháp."
    },
    # 24
    {
        "id": 24,
        "category": "Giải phẫu Dự án",
        "bloom": "Remember",
        "question": "Tệp tin nào có phần mở rộng .resx đi kèm với Form trong dự án Windows Forms chịu trách nhiệm lưu trữ các tài nguyên nhị phân cục bộ như hình ảnh và âm thanh?",
        "options": [
            "Form1.resx.",
            "Form1.xml.",
            "Form1.bin.",
            "Form1.resources."
        ],
        "answer": 0,
        "explanation": "Tệp Form1.resx là tệp tài nguyên dựa trên định dạng XML lưu trữ các dữ liệu phi mã nguồn của form như chuỗi ký tự bản địa hóa, hình ảnh và icon."
    },
    # 25
    {
        "id": 25,
        "category": "Giải phẫu Dự án",
        "bloom": "Understand",
        "question": "Điểm khởi nhập (Entry Point) của toàn bộ ứng dụng C# Windows Forms chứa phương thức tĩnh static void Main() nằm trong tệp tin nào?",
        "options": [
            "Program.cs.",
            "Form1.cs.",
            "AssemblyInfo.cs.",
            "App.config."
        ],
        "answer": 0,
        "explanation": "Tệp Program.cs chứa hàm tĩnh Main() - điểm khởi nhập đầu tiên khi ứng dụng được khởi chạy bởi máy ảo CLR, gọi Application.Run(new Form1()) để nạp form chính lên màn hình."
    },
    # 26
    {
        "id": 26,
        "category": "Thư viện Liên kết",
        "bloom": "Analyze",
        "question": "Nhánh References trong Solution Explorer chứa tham chiếu đến các thư viện liên kết (.dll) nào đóng vai trò cốt lõi để xây dựng giao diện Windows Forms?",
        "options": [
            "System.Windows.Forms và System.Drawing.",
            "System.Console và System.Terminal.",
            "System.Web và System.Cloud.",
            "System.Kernel và System.Hardware."
        ],
        "answer": 0,
        "explanation": "System.Windows.Forms cung cấp các lớp điều khiển đồ họa (Form, Button, Label, PictureBox...), còn System.Drawing cung cấp các dịch vụ đồ họa GDI+ (màu sắc Color, phông chữ Font, điểm ảnh Point, khung hình Size, vẽ hình)."
    },
    # 27
    {
        "id": 27,
        "category": "Toolbox",
        "bloom": "Understand",
        "question": "Hiện tượng nào sau đây giải thích việc cửa sổ Toolbox hiển thị thông báo 'There are no usable controls in this category' khi mở một tệp mã nguồn C# (.cs)?",
        "options": [
            "Do tab hiện hành là trình soạn thảo văn bản mã nguồn code, không có bề mặt đồ họa để tiếp nhận điều khiển.",
            "Do phiên bản Visual Studio đã hết hạn bản quyền dùng thử và bị khóa tính năng thiết kế giao diện.",
            "Do tệp tin mã nguồn C# bị nhiễm virus máy tính làm tê liệt toàn bộ kho linh kiện của IDE.",
            "Do lập trình viên chưa cài đặt gói phần mềm .NET Framework Class Library trên máy tính cá nhân."
        ],
        "answer": 0,
        "explanation": "Toolbox chỉ kích hoạt và hiển thị linh kiện khi khung nhìn hiện hành là Form Designer đồ họa [Design]. Khi đang xem mã nguồn văn bản .cs thuần túy, Toolbox tự động ẩn các linh kiện kéo thả."
    },
    # 28
    {
        "id": 28,
        "category": "Common Controls",
        "bloom": "Remember",
        "question": "Điều khiển đồ họa cơ bản nào trong nhóm Common Controls được dùng để hiển thị các nhãn văn bản cố định mà người dùng không thể gõ sửa trực tiếp?",
        "options": [
            "Label.",
            "TextBox.",
            "RichTextBox.",
            "Button."
        ],
        "answer": 0,
        "explanation": "Điều khiển Label dùng để gắn nhãn, hiển thị hướng dẫn hoặc tiêu đề tĩnh trên giao diện người dùng; người dùng cuối không thể nhấp chuột gõ thay đổi trực tiếp nội dung của Label."
    },
    # 29
    {
        "id": 29,
        "category": "Common Controls",
        "bloom": "Remember",
        "question": "Điều khiển nào trong Windows Forms cho phép người dùng nhập văn bản một dòng hoặc nhiều dòng trực tiếp từ bàn phím máy tính?",
        "options": [
            "TextBox.",
            "Label.",
            "PictureBox.",
            "Panel."
        ],
        "answer": 0,
        "explanation": "TextBox (hộp nhập liệu văn bản) tiếp nhận thông tin người dùng nhập từ bàn phím, hỗ trợ các thuộc tính đa dòng (Multiline), mật khẩu (PasswordChar) và căn lề."
    },
    # 30
    {
        "id": 30,
        "category": "Common Controls",
        "bloom": "Remember",
        "question": "Điều khiển nào cung cấp một bề mặt trực quan để người dùng nhấp chuột nhằm kích hoạt một hành động hoặc xử lý nghiệp vụ trong ứng dụng?",
        "options": [
            "Button.",
            "GroupBox.",
            "PictureBox.",
            "ProgressBar."
        ],
        "answer": 0,
        "explanation": "Điều khiển Button (nút nhấn) là điều khiển tương tác kinh điển kích hoạt sự kiện Click để thực thi chuỗi lệnh được lập trình viên gán cho nó."
    },
    # 31
    {
        "id": 31,
        "category": "Common Controls",
        "bloom": "Remember",
        "question": "Điều khiển nào trong Windows Forms chuyên dùng để hiển thị các tệp hình ảnh đồ họa (định dạng PNG, JPEG, GIF, BMP, ICO)?",
        "options": [
            "PictureBox.",
            "ImageFrame.",
            "GraphicView.",
            "CanvasBox."
        ],
        "answer": 0,
        "explanation": "PictureBox là điều khiển chuyên dụng trong .NET Windows Forms để chứa và hiển thị hình ảnh đồ họa từ tệp tin hoặc tài nguyên của dự án."
    },
    # 32
    {
        "id": 32,
        "category": "Properties Window",
        "bloom": "Understand",
        "question": "Khung chữ nhật nhỏ màu xám nằm ở đáy của Cửa sổ Properties (Description Pane) có tác dụng gì đối với người lập trình?",
        "options": [
            "Hiển thị đoạn văn ngắn mô tả ý nghĩa kỹ thuật và hướng dẫn sử dụng của thuộc tính đang được chọn.",
            "Hiển thị dung lượng bộ nhớ RAM mà thuộc tính đó đang tiêu tốn trên máy chủ cơ sở dữ liệu.",
            "Cảnh báo lập trình viên nếu thuộc tính đó chuẩn bị bị gỡ bỏ trong phiên bản C# tương lai.",
            "Tự động dịch mã nguồn của thuộc tính sang ngôn ngữ lập trình Python và Java."
        ],
        "answer": 0,
        "explanation": "Description Pane ở chân cửa sổ Properties cung cấp tài liệu chú giải tóm tắt về vai trò và kiểu dữ liệu của thuộc tính đang được chọn, hỗ trợ việc tự học và tra cứu nhanh."
    },
    # 33
    {
        "id": 33,
        "category": "Properties Window",
        "bloom": "Apply",
        "question": "Khi muốn tìm nhanh một thuộc tính theo tên gọi cụ thể mà ta đã biết rõ chữ cái đầu (ví dụ thuộc tính SizeMode hay TextAlign), ta nên chọn chế độ hiển thị nào trên Properties Window?",
        "options": [
            "Chế độ Bảng chữ cái (Alphabetical).",
            "Chế độ Phân loại (Categorized).",
            "Chế độ Nhóm sự kiện (Event View).",
            "Chế độ Thu gọn (Minimized View)."
        ],
        "answer": 0,
        "explanation": "Chế độ Alphabetical (nút A-Z) sắp xếp toàn bộ danh sách thuộc tính theo thứ tự từ điển A đến Z, giúp người có kinh nghiệm duyệt thẳng đến ký tự chữ cái đầu cần tìm nhanh chóng."
    },
    # 34
    {
        "id": 34,
        "category": "Thuộc tính Điều khiển",
        "bloom": "Analyze",
        "question": "Sự khác biệt bản chất giữa thuộc tính '(Name)' và thuộc tính 'Text' của một điều khiển trên Form là gì?",
        "options": [
            "(Name) là tên định danh biến số trong mã nguồn C#, còn Text là văn bản hiển thị ra ngoài giao diện cho người dùng thấy.",
            "(Name) dùng để hiển thị trên thanh tiêu đề, còn Text là mã bí mật dùng để bảo vệ bản quyền phần mềm.",
            "(Name) chỉ áp dụng cho Form, còn Text là thuộc tính độc quyền của điều khiển PictureBox.",
            "(Name) có thể chứa dấu cách và tiếng Việt, còn Text bắt buộc phải tuân theo quy tắc cú pháp PascalCase."
        ],
        "answer": 0,
        "explanation": "Thuộc tính (Name) là định danh biến đối tượng trong mã C# (để gọi `label1.Text = ...`), còn thuộc tính Text là nội dung chuỗi ký tự hiển thị trực quan lên màn hình cho người dùng đọc."
    },
    # 35
    {
        "id": 35,
        "category": "Thuộc tính Điều khiển",
        "bloom": "Apply",
        "question": "Trong hộp thoại chọn màu của thuộc tính BackColor, tại sao lập trình viên thường ưu tiên chọn màu từ tab 'Web' thay vì tab 'System'?",
        "options": [
            "Vì các màu trong tab Web là màu cố định chuẩn mực, không bị biến đổi khi máy tính người dùng đổi chủ đề giao diện (Theme).",
            "Vì các màu trong tab System sẽ làm tăng đáng kể kích thước tệp tin thực thi .exe khi biên dịch phần mềm.",
            "Vì tab Web chỉ hoạt động khi máy tính được kết nối trực tiếp với mạng cáp quang Internet tốc độ cao.",
            "Vì các màu trong tab System không tương thích với màn hình độ phân giải Retina và màn hình 4K."
        ],
        "answer": 0,
        "explanation": "Tab System sử dụng màu phụ thuộc vào Theme/chủ đề Windows của máy người dùng (có thể đổi thành tối hoặc sáng tùy ý). Chọn màu tab Web đảm bảo tính đồng nhất thẩm mỹ trên mọi môi trường chạy."
    },
    # 36
    {
        "id": 36,
        "category": "Thuộc tính Điều khiển",
        "bloom": "Apply",
        "question": "Khi cấu hình thuộc tính Font của Label, nút bấm hình dấu 3 chấm [...] (Ellipsis button) ở bên phải ô giá trị có chức năng gì?",
        "options": [
            "Mở hộp thoại đồ họa chuẩn Font Dialog cho phép chọn trực quan kiểu phông, kiểu chữ (Bold/Italic) và kích thước cỡ chữ.",
            "Mở trình duyệt web để tải thêm các phông chữ đẹp từ kho phông chữ trực tuyến của Google Fonts.",
            "Tự động xóa toàn bộ các định dạng phông chữ hiện tại và đưa về phông chữ mặc định của MS-DOS.",
            "Kiểm tra xem máy tính có cài đặt bộ gõ tiếng Việt Unikey hoặc Vietkey hay không."
        ],
        "answer": 0,
        "explanation": "Nút dấu 3 chấm [...] (Ellipsis button) mở hộp thoại Font Dialog trực quan của hệ thống để chọn FontFamily (Segoe UI, Arial...), FontStyle (Regular, Bold, Italic) và Size (pt)."
    },
    # 37
    {
        "id": 37,
        "category": "Thuộc tính Điều khiển",
        "bloom": "Apply",
        "question": "Lưới đồ họa trực quan 9 ô vuông nhỏ (3x3) xuất hiện khi cấu hình thuộc tính TextAlign của Label cho phép thiết lập giá trị căn giữa hoàn hảo nào?",
        "options": [
            "MiddleCenter.",
            "TopLeft.",
            "BottomRight.",
            "AbsoluteCenter."
        ],
        "answer": 0,
        "explanation": "Lưới 3x3 đại diện cho 9 vị trí căn chỉnh văn bản. Ô vuông ở chính giữa đại diện cho giá trị MiddleCenter - căn đều chính giữa theo cả trục ngang và trục dọc."
    },
    # 38
    {
        "id": 38,
        "category": "Design View",
        "bloom": "Understand",
        "question": "Tính năng 'Đường căn thông minh' (Snap Lines) tự động hiển thị các đường kẻ đứt nét màu xanh và hồng khi kéo thả điều khiển mang lại lợi ích gì?",
        "options": [
            "Giúp tự động bắt dính và căn thẳng hàng các mép điều khiển, đảm bảo khoảng cách lề chuẩn UI mà không cần đo pixel thủ công.",
            "Báo hiệu rằng máy tính đang bị quá tải bộ nhớ và cần phải khởi động lại môi trường Visual Studio.",
            "Đo lường độ dài của các đường dây cáp mạng kết nối từ máy trạm đến máy chủ phòng thực hành.",
            "Vẽ các đường đồ thị hàm số toán học bậc hai lên giao diện Form của bài toán."
        ],
        "answer": 0,
        "explanation": "Snap Lines là các đường căn thông minh xuất hiện khi di chuyển điều khiển, giúp bắt dính lề trên, dưới, trái, phải và khoảng cách đệm (Padding/Margin) chuẩn theo khuyến nghị UX của Microsoft."
    },
    # 39
    {
        "id": 39,
        "category": "PictureBox",
        "bloom": "Apply",
        "question": "Trong hộp thoại Select Resource khi nạp ảnh cho PictureBox, việc chọn tùy chọn 'Project resource file' mang lại ưu thế vượt trội nào?",
        "options": [
            "Đóng gói vĩnh viễn tệp hình ảnh vào tài nguyên của dự án (.resx) và nhúng vào tệp thực thi .exe khi biên dịch.",
            "Chỉ tạo một đường dẫn tạm thời đến tệp ảnh trên ổ cứng máy tính và sẽ mất ảnh nếu đem file sang máy khác.",
            "Tự động nén chất lượng hình ảnh xuống mức thấp nhất để tiết kiệm tối đa dung lượng bộ nhớ lưu trữ.",
            "Bắt buộc tất cả các hình ảnh phải được chuyển đổi sang định dạng đen trắng trước khi hiển thị."
        ],
        "answer": 0,
        "explanation": "Chọn 'Project resource file' nhúng trực tiếp tệp ảnh vào tệp tài nguyên của dự án (.resx) và đóng gói vào tệp .exe khi biên dịch, giúp ứng dụng chạy được ở bất kỳ máy tính nào mà không bị đứt liên kết ảnh."
    },
    # 40
    {
        "id": 40,
        "category": "PictureBox",
        "bloom": "Analyze",
        "question": "Khi muốn hình ảnh trong PictureBox tự động co hoặc giãn để vừa khít 100% cả chiều rộng và chiều cao của khung hình, ta gán thuộc tính SizeMode giá trị nào?",
        "options": [
            "StretchImage.",
            "Normal.",
            "AutoSize.",
            "CenterImage."
        ],
        "answer": 0,
        "explanation": "Giá trị StretchImage ép hình ảnh co hoặc giãn vừa khít hoàn toàn theo kích thước chiều rộng và chiều cao của PictureBox. (AutoSize làm khung phình theo ảnh; Zoom co giãn giữ nguyên tỷ lệ aspect ratio; Normal cắt xén ảnh)."
    }
]

print(f"Total raw questions: {len(raw_questions)}")

# Now we want strict balancing:
# 1. Answer distribution: exactly 10 A, 10 B, 10 C, 10 D (keys 0, 1, 2, 3)
# 2. Length rank distribution: exactly 10 Rank 1, 10 Rank 2, 10 Rank 3, 10 Rank 4
# Let's write an optimizer / balancer script that assigns correct answer positions and lengths.
EOF
python build_ch02_quiz.py

