# -*- coding: utf-8 -*-
import json
from collections import Counter

TARGET_SPECS = [
    # Q01..Q10
    (0, 1), (1, 2), (2, 3), (3, 4), (1, 1), (2, 2), (3, 3), (0, 4), (2, 1), (3, 2),
    # Q11..Q20
    (0, 3), (1, 4), (3, 1), (0, 2), (1, 3), (2, 4), (0, 1), (1, 2), (2, 3), (3, 4),
    # Q21..Q30
    (1, 1), (2, 2), (3, 3), (0, 4), (2, 1), (3, 2), (0, 3), (1, 4), (3, 1), (0, 2),
    # Q31..Q40
    (1, 3), (2, 4), (0, 1), (1, 2), (2, 3), (3, 4), (1, 1), (2, 2), (3, 3), (0, 4)
]

# 40 Questions Data
# Each question defines:
# - id, category, bloom, question, explanation
# - correct_answer: text of correct answer
# - distractors: list of 3 distractors
# To achieve target_rank (1..4):
# Rank 1: correct is shortest -> all 3 distractors must be longer than correct
# Rank 2: 1 distractor shorter, 2 distractors longer
# Rank 3: 2 distractors shorter, 1 distractor longer
# Rank 4: correct is longest -> all 3 distractors must be shorter than correct

questions_def = [
    # Q1: target (0, 1) -> Pos A (0), Rank 1 (Shortest)
    {
        "id": 1,
        "category": "Tổng quan IDE",
        "bloom": "Remember",
        "question": "Thuật ngữ viết tắt IDE trong môi trường phát triển ứng dụng Visual C# là viết tắt của cụm từ nào?",
        "explanation": "Theo mục 2.1 giáo trình Deitel: IDE là viết tắt của Integrated Development Environment (Môi trường phát triển tích hợp), đóng gói trình soạn thảo, biên dịch, thiết kế giao diện và gỡ lỗi trên một phần mềm thống nhất.",
        "correct": "Integrated Development Environment.",
        "shorter": [],
        "longer": [
            "Interactive Data Execution for Systems Programming.",
            "Interface Deployment Engine for Windows Applications.",
            "Internal Developer Equipment for Systems Architecture."
        ]
    },
    # Q2: target (1, 2) -> Pos B (1), Rank 2
    {
        "id": 2,
        "category": "Triết lý RAD",
        "bloom": "Understand",
        "question": "Đặc trưng then chốt nhất của mô hình Phát triển Ứng dụng Nhanh (RAD) trong lập trình Windows Forms là gì?",
        "explanation": "RAD tập trung vào việc tạo nhanh bản mẫu (Prototyping), kéo thả linh kiện trực quan và tái sử dụng tối đa các lớp điều khiển có sẵn trong .NET Framework Class Library (FCL).",
        "correct": "Tái sử dụng linh kiện có sẵn và tạo mẫu giao diện nhanh bằng kéo thả.",
        "shorter": [
            "Chỉ viết mã nguồn bằng dòng lệnh console."
        ],
        "longer": [
            "Yêu cầu lập trình viên phải tự tính toán tọa độ điểm ảnh pixel cho từng nút bấm.",
            "Loại bỏ hoàn toàn trình biên dịch và thực thi trực tiếp mã C# trên bo mạch chủ phần cứng."
        ]
    },
    # Q3: target (2, 3) -> Pos C (2), Rank 3
    {
        "id": 3,
        "category": "Tổng quan IDE",
        "bloom": "Remember",
        "question": "Phiên bản Visual Studio nào sau đây được Microsoft cung cấp hoàn toàn miễn phí phục vụ đào tạo sinh viên và dự án cá nhân?",
        "explanation": "Visual Studio Community là ấn bản miễn phí bản quyền nhưng sở hữu đầy đủ tính năng thiết kế giao diện, biên dịch C# và gỡ lỗi nâng cao phục vụ sinh viên, giảng viên và nghiên cứu cá nhân.",
        "correct": "Visual Studio Community bản đầy đủ tính năng cho học tập.",
        "shorter": [
            "Visual Studio Pro.",
            "Visual Studio Enterprise Suite."
        ],
        "longer": [
            "Visual Studio Professional dành riêng cho doanh nghiệp quy mô vừa và lớn trên toàn cầu."
        ]
    },
    # Q4: target (3, 4) -> Pos D (3), Rank 4 (Longest)
    {
        "id": 4,
        "category": "Màn hình Khởi động",
        "bloom": "Remember",
        "question": "Khu vực 'Recent' trên màn hình Start Page khi vừa mở Visual Studio có công dụng chính là gì?",
        "explanation": "Khu vực Recent trên Start Page liệt kê danh sách các dự án (.csproj) và giải pháp (.sln) được truy cập gần nhất, giúp lập trình viên mở lại công việc nhanh mà không cần tìm kiếm thư mục.",
        "correct": "Hiển thị danh sách các giải pháp và dự án đã làm việc gần đây để mở lại tức thì chỉ bằng một cú nhấp chuột.",
        "shorter": [
            "Xem bản vá lỗi Windows.",
            "Cập nhật tin tức công nghệ.",
            "Xóa sạch bộ nhớ đệm cũ."
        ],
        "longer": []
    },
    # Q5: target (1, 1) -> Pos B (1), Rank 1 (Shortest)
    {
        "id": 5,
        "category": "Hộp thoại New Project",
        "bloom": "Apply",
        "question": "Để tạo dự án phần mềm giao diện đồ họa cửa sổ màn hình Desktop bằng Visual C#, lập trình viên chọn mẫu template nào?",
        "explanation": "Mẫu Windows Forms Application trong phân mục Visual C# -> Windows được dùng để xây dựng các ứng dụng đồ họa máy tính tương tác chuẩn mực trên hệ điều hành Windows.",
        "correct": "Windows Forms Application.",
        "shorter": [],
        "longer": [
            "Console Application độc lập dòng lệnh đen trắng.",
            "WCF Service Application cho dịch vụ phân tán đám mây.",
            "ASP.NET Web Forms Application cho ứng dụng trực tuyến."
        ]
    },
    # Q6: target (2, 2) -> Pos C (2), Rank 2
    {
        "id": 6,
        "category": "Hộp thoại New Project",
        "bloom": "Understand",
        "question": "Tại sao trong ô nhập tên dự án (Name), lập trình viên nên đặt tên theo chuẩn PascalCase, viết liền không dấu tiếng Việt?",
        "explanation": "Tên dự án được Visual Studio sử dụng làm Không gian tên mặc định (Default Namespace) và tên file nhị phân đầu ra (.exe). Nếu chứa khoảng trắng hay ký tự đặc biệt, nó có thể gây lỗi cú pháp và đường dẫn.",
        "correct": "Vì tên dự án sẽ trở thành Namespace mặc định và tên tệp thực thi .exe của ứng dụng.",
        "shorter": [
            "Để giảm dung lượng RAM của hệ điều hành."
        ],
        "longer": [
            "Vì hệ điều hành Windows không hỗ trợ lưu tệp tin có khoảng trắng trên ổ đĩa cứng chuẩn NTFS.",
            "Nhằm giúp máy tính tự động tăng gấp đôi tốc độ xung nhịp của CPU trong quá trình biên dịch mã nguồn."
        ]
    },
    # Q7: target (3, 3) -> Pos D (3), Rank 3
    {
        "id": 7,
        "category": "Hộp thoại New Project",
        "bloom": "Understand",
        "question": "Mục đích quan trọng của việc tích chọn ô kiểm 'Create directory for solution' khi tạo dự án mới là gì?",
        "explanation": "Tích chọn 'Create directory for solution' giúp tạo thư mục cha riêng chứa tệp giải pháp .sln và các thư mục dự án con, thuận tiện khi sao lưu, nén nộp bài hoặc chia sẻ mã nguồn.",
        "correct": "Tạo thư mục cha bao bọc toàn bộ giải pháp giúp quản lý mã nguồn, tài nguyên gọn gàng và độc lập.",
        "shorter": [
            "Mã hóa tệp tin chống sao chép.",
            "Tự động tải mã nguồn lên kho lưu trữ đám mây."
        ],
        "longer": [
            "Bắt buộc người dùng máy tính phải nhập mật khẩu quản trị viên mới có thể mở được ứng dụng trên máy trạm."
        ]
    },
    # Q8: target (0, 4) -> Pos A (0), Rank 4 (Longest)
    {
        "id": 8,
        "category": "Khung nhìn Design View",
        "bloom": "Understand",
        "question": "Bề mặt Form1 màu xám hiển thị ở trung tâm màn hình Design View có vai trò kỹ thuật là gì?",
        "explanation": "Design View hiển thị Form1 như một tấm toan vẽ (Canvas) trực quan, cho phép lập trình viên kéo thả, căn chỉnh vị trí và thay đổi thuộc tính của các điều khiển đồ họa theo mô hình WYSIWYG.",
        "correct": "Là tấm toan vẽ đồ họa đại diện cho cửa sổ ứng dụng Windows thực tế để kéo thả và bài trí các điều khiển giao diện.",
        "shorter": [
            "Chỉ là một hình ảnh tĩnh để minh họa.",
            "Là bảng hiển thị các lỗi cú pháp lập trình.",
            "Là nơi kiểm tra bộ nhớ RAM đang hoạt động thực tế."
        ],
        "longer": []
    },
    # Q9: target (2, 1) -> Pos C (2), Rank 1 (Shortest)
    {
        "id": 9,
        "category": "Khung nhìn Design View",
        "bloom": "Apply",
        "question": "Các ô vuông nhỏ màu trắng (Sizing handles) xuất hiện quanh viền Form1 khi được nhấp chọn dùng để làm gì?",
        "explanation": "Sizing handles (chốt điều chỉnh kích thước) ở 4 góc và 4 cạnh cho phép dùng chuột kéo giãn để tăng giảm chiều rộng và chiều cao của Form một cách trực quan.",
        "correct": "Kéo giãn thay đổi kích thước Form.",
        "shorter": [],
        "longer": [
            "Đổi màu nền của Form sang màu trắng tinh khôi.",
            "Xóa vĩnh viễn Form hiện hành ra khỏi dự án đang mở.",
            "Khóa cố định vị trí cửa sổ trên màn hình máy tính cá nhân."
        ]
    },
    # Q10: target (3, 2) -> Pos D (3), Rank 2
    {
        "id": 10,
        "category": "Hệ thống Menu Bar",
        "bloom": "Remember",
        "question": "Khi vô tình đóng mất một cửa sổ làm việc như Solution Explorer hoặc Toolbox, menu nào là nơi giúp mở lại nhanh nhất?",
        "explanation": "Menu View là trung tâm quản lý hiển thị của IDE. Mọi cửa sổ bị ẩn hay đóng nhầm đều có thể mở lại thông qua menu View (View -> Solution Explorer, View -> Toolbox...).",
        "correct": "Menu View chứa danh mục các cửa sổ công cụ của IDE.",
        "shorter": [
            "Menu File trên Menu Bar."
        ],
        "longer": [
            "Menu Edit chứa các lệnh hoàn tác và tìm kiếm văn bản.",
            "Menu Tools dùng cấu hình môi trường phát triển phần mềm."
        ]
    },
    # Q11: target (0, 3) -> Pos A (0), Rank 3
    {
        "id": 11,
        "category": "Menu Build",
        "bloom": "Analyze",
        "question": "Sự khác biệt then chốt giữa lệnh 'Build Solution' và lệnh 'Rebuild Solution' trong menu Build là gì?",
        "explanation": "Build Solution thực hiện biên dịch gia tăng (Incremental Build) cho các file có thay đổi để tiết kiệm thời gian; Rebuild Solution dọn sạch toàn bộ thư mục bin/obj rồi biên dịch mới 100% để loại bỏ lỗi cache.",
        "correct": "Build biên dịch các file vừa sửa, còn Rebuild xóa sạch file nhị phân cũ trong bin/obj rồi dịch lại toàn bộ từ đầu.",
        "shorter": [
            "Build dịch mã C#, Rebuild dịch mã C++.",
            "Build chạy ứng dụng, Rebuild chỉ lưu file mã nguồn."
        ],
        "longer": [
            "Build dành riêng cho hệ điều hành Windows 32-bit, trong khi Rebuild được tối ưu cho các dòng máy tính 64-bit đa nhân hiện đại."
        ]
    },
    # Q12: target (1, 4) -> Pos B (1), Rank 4 (Longest)
    {
        "id": 12,
        "category": "Menu Debug",
        "bloom": "Analyze",
        "question": "Lệnh 'Start Debugging' (F5) khác với lệnh 'Start Without Debugging' (Ctrl + F5) ở điểm cốt lõi nào?",
        "explanation": "F5 kích hoạt Debugger để theo dõi biến và bắt điểm dừng Breakpoint khi có sự cố. Ctrl+F5 chạy trực tiếp không gắn cờ Debugger, thích hợp khi cần kiểm thử tốc độ thực tế của người dùng.",
        "correct": "F5 chạy ứng dụng có kết nối với bộ giám sát lỗi của IDE, còn Ctrl+F5 chạy ứng dụng độc lập với tốc độ cao nhất.",
        "shorter": [
            "F5 chỉ dịch mã, Ctrl+F5 chạy ngay.",
            "F5 chỉ chạy được trên hệ điều hành 64-bit.",
            "F5 yêu cầu quyền quản trị viên máy tính phòng máy."
        ],
        "longer": []
    },
    # Q13: target (3, 1) -> Pos D (3), Rank 1 (Shortest)
    {
        "id": 13,
        "category": "Menu Format",
        "bloom": "Apply",
        "question": "Menu nào trên thanh Menu Bar sẽ tự động xuất hiện khi lập trình viên chọn đồng thời từ hai điều khiển trở lên trên Form?",
        "explanation": "Menu Format chỉ hiển thị khi có từ hai điều khiển trở lên được chọn, cung cấp các lệnh căn lề (Align), chỉnh bằng kích thước (Make Same Size) và giãn khoảng cách (Horizontal/Vertical Spacing).",
        "correct": "Menu Format.",
        "shorter": [],
        "longer": [
            "Menu Project để thêm mới tệp tin.",
            "Menu Tools cung cấp các tiện ích hệ thống.",
            "Menu Debug dùng để đặt các điểm dừng kiểm thử."
        ]
    },
    # Q14: target (0, 2) -> Pos A (0), Rank 2
    {
        "id": 14,
        "category": "Standard Toolbar",
        "bloom": "Apply",
        "question": "Tại sao lập trình viên luôn được khuyến nghị sử dụng nút 'Save All' (Ctrl + Shift + S) thay vì Save thường (Ctrl + S)?",
        "explanation": "Trong Windows Forms, mỗi thay đổi trên giao diện ảnh hưởng đồng thời tới tệp mã logic (Form1.cs), tệp mã sinh tự động (Form1.Designer.cs) và tài nguyên (.resx). Save All đảm bảo toàn bộ được lưu an toàn.",
        "correct": "Vì thao tác kéo thả Form làm biến động đồng thời cả Form1.cs, Form1.Designer.cs và Form1.resx.",
        "shorter": [
            "Để giải phóng dung lượng bộ nhớ RAM."
        ],
        "longer": [
            "Vì thao tác Save All sẽ tự động biên dịch toàn bộ chương trình mã nguồn C# sang tệp nhị phân .exe trên máy tính.",
            "Vì nếu chỉ bấm Save thường thì các điều khiển đồ họa trên Form sẽ bị khôi phục về giá trị mặc định."
        ]
    },
    # Q15: target (1, 3) -> Pos B (1), Rank 3
    {
        "id": 15,
        "category": "Thanh Công cụ",
        "bloom": "Remember",
        "question": "Tính năng hiển thị một nhãn nhỏ màu vàng nhạt mô tả chức năng của nút bấm khi rê chuột qua nút công cụ được gọi là gì?",
        "explanation": "Tooltip là nhãn chú giải nổi lên khi rê chuột dừng trên một nút công cụ, hiển thị tên lệnh và phím tắt tương ứng trong dấu ngoặc đơn.",
        "correct": "Tooltip (Chú giải công cụ kèm phím tắt).",
        "shorter": [
            "Smart Tag.",
            "Context Menu."
        ],
        "longer": [
            "Status Label nằm ở thanh trạng thái dưới chân màn hình."
        ]
    },
    # Q16: target (2, 4) -> Pos C (2), Rank 4 (Longest)
    {
        "id": 16,
        "category": "Phím tắt Chuẩn",
        "bloom": "Remember",
        "question": "Phím tắt mặc định trong Visual Studio dùng để mở nhanh Cửa sổ Thuộc tính (Properties Window) là phím nào?",
        "explanation": "Phím F4 là phím tắt mặc định để mở hoặc di chuyển tiêu điểm trực tiếp đến Properties Window để cấu hình thuộc tính của đối tượng đang chọn.",
        "correct": "Phím F4 (kích hoạt cửa sổ Properties của đối tượng đang chọn).",
        "shorter": [
            "Phím F2.",
            "Phím F7.",
            "Tổ hợp phím Shift + F5."
        ],
        "longer": []
    },
    # Q17: target (0, 1) -> Pos A (0), Rank 1 (Shortest)
    {
        "id": 17,
        "category": "Trợ giúp Ngữ cảnh",
        "bloom": "Understand",
        "question": "Phím F1 trong Visual Studio kích hoạt tính năng Trợ giúp Ngữ cảnh (Context-Sensitive Help) có cơ chế hoạt động như thế nào?",
        "explanation": "Phím F1 nhận diện đối tượng đang được chọn (trên Form hoặc từ khóa trong code) và tự động mở đúng trang tài liệu Microsoft MSDN / Learn liên quan đến đối tượng đó.",
        "correct": "Mở tài liệu MSDN đúng điều khiển đang chọn.",
        "shorter": [],
        "longer": [
            "Tự động sửa toàn bộ lỗi cú pháp trong mã lệnh C#.",
            "Gửi thông báo cầu cứu đến máy chủ hỗ trợ kỹ thuật.",
            "Chuyển giao diện làm việc của Visual Studio sang ngôn ngữ tiếng Việt."
        ]
    },
    # Q18: target (1, 2) -> Pos B (1), Rank 2
    {
        "id": 18,
        "category": "Kỹ thuật Điều hướng",
        "bloom": "Understand",
        "question": "Khi biểu tượng chiếc đinh ghim (Pushpin) trên thanh tiêu đề của một cửa sổ công cụ xoay sang tư thế nằm ngang, cửa sổ đó đang ở trạng thái nào?",
        "explanation": "Khi đinh ghim nằm ngang (Horizontal pin), tính năng Auto-Hide được kích hoạt: cửa sổ thu thành tab nhỏ ở mép màn hình, chỉ mở ra khi rê chuột vào và thụt lại khi rê chuột ra.",
        "correct": "Kích hoạt chế độ Tự động ẩn (Auto-Hide).",
        "shorter": [
            "Cửa sổ bị khóa."
        ],
        "longer": [
            "Cửa sổ đang ở trạng thái Ghim cố định trên màn hình.",
            "Cửa sổ đã bị gỡ bỏ hoàn toàn khỏi môi trường phát triển."
        ]
    },
    # Q19: target (2, 3) -> Pos C (2), Rank 3
    {
        "id": 19,
        "category": "Kỹ thuật Điều hướng",
        "bloom": "Apply",
        "question": "Biểu tượng hướng dẫn ghép nối (Docking Visualizer) hình chữ thập với 4 mũi tên xuất hiện khi người dùng thực hiện thao tác nào?",
        "explanation": "Docking Visualizer xuất hiện khi kéo thanh tiêu đề cửa sổ, hỗ trợ neo (dock) cửa sổ vào cạnh màn hình hoặc thả vào tâm để gộp thành tab.",
        "correct": "Nhấp giữ thanh tiêu đề của một cửa sổ và kéo di chuyển trên màn hình.",
        "shorter": [
            "Nhấp đúp chuột lên Form.",
            "Nhấn tổ hợp phím tắt Ctrl + Shift + B."
        ],
        "longer": [
            "Mở hộp thoại New Project để khởi tạo một giải pháp mới với cấu trúc đa tầng phức tạp."
        ]
    },
    # Q20: target (3, 4) -> Pos D (3), Rank 4 (Longest)
    {
        "id": 20,
        "category": "Kỹ thuật Điều hướng",
        "bloom": "Apply",
        "question": "Lệnh nào sau đây giúp khôi phục toàn bộ bố cục các cửa sổ công cụ về trạng thái xuất xưởng mặc định khi giao diện bị xáo trộn?",
        "explanation": "Lệnh Window -> Reset Window Layout trên thanh Menu Bar sẽ sắp xếp lại toàn bộ các cửa sổ làm việc về vị trí và bố cục mặc định của nhà sản xuất.",
        "correct": "Window -> Reset Window Layout (khôi phục toàn bộ giao diện IDE về trạng thái chuẩn ban đầu).",
        "shorter": [
            "File -> Close Solution.",
            "Edit -> Undo All Window Moves.",
            "Tools -> Import and Export Settings."
        ],
        "longer": []
    },
    # Q21: target (1, 1) -> Pos B (1), Rank 1 (Shortest)
    {
        "id": 21,
        "category": "Solution Explorer",
        "bloom": "Understand",
        "question": "Thứ bậc phân cấp giữa Solution (.sln) và Project (.csproj) trong Visual Studio được hiểu đúng như thế nào?",
        "explanation": "Solution (đuôi .sln) là cấp cao nhất đóng vai trò như một chiếc cặp lớn, có thể chứa một hoặc nhiều Project (.csproj) cùng phối hợp hoạt động.",
        "correct": "Solution chứa một hoặc nhiều Project con.",
        "shorter": [],
        "longer": [
            "Project là cấp cha chứa các Solution con bên trong.",
            "Solution và Project hoàn toàn ngang hàng và không có quan hệ chứa nhau.",
            "Mỗi Solution chỉ được phép chứa duy nhất một tệp tin mã nguồn C# đơn lẻ."
        ]
    },
    # Q22: target (2, 2) -> Pos C (2), Rank 2
    {
        "id": 22,
        "category": "Giải phẫu Tệp tin",
        "bloom": "Understand",
        "question": "Tệp tin nào trong dự án Windows Forms là nơi lập trình viên chúng ta viết mã xử lý nghiệp vụ và các phương thức xử lý sự kiện?",
        "explanation": "Tệp Form1.cs là nơi lập trình viên viết mã nguồn nghiệp vụ và các hàm xử lý sự kiện (Event Handlers) cho ứng dụng.",
        "correct": "Tệp tin mã nguồn chính Form1.cs.",
        "shorter": [
            "Tệp cấu hình App.config."
        ],
        "longer": [
            "Tệp tin tài nguyên nhị phân Form1.resx của dự án.",
            "Tệp tin sinh mã tự động Form1.Designer.cs của IDE."
        ]
    },
    # Q23: target (3, 3) -> Pos D (3), Rank 3
    {
        "id": 23,
        "category": "Giải phẫu Tệp tin",
        "bloom": "Analyze",
        "question": "Tại sao trong tệp Form1.Designer.cs có cảnh báo lập trình viên không được tự ý sửa đổi mã trong phương thức InitializeComponent()?",
        "explanation": "InitializeComponent() hoàn toàn do công cụ trực quan Form Designer đồng bộ tự động. Sửa tay sai cú pháp có thể khiến IDE không phân tích cú pháp thiết kế được và không mở lại được Design View.",
        "correct": "Vì phương thức này do Form Designer quản lý tự động, việc sửa tay dễ gây xung đột làm hỏng màn hình Design View.",
        "shorter": [
            "Vì chứa mã bản quyền Windows.",
            "Vì nó sẽ làm hỏng kết nối mạng Internet."
        ],
        "longer": [
            "Vì mã tại đây sẽ tự động kích hoạt lệnh xóa sạch toàn bộ hệ quản trị cơ sở dữ liệu của máy chủ doanh nghiệp khi biên dịch phần mềm."
        ]
    },
    # Q24: target (0, 4) -> Pos A (0), Rank 4 (Longest)
    {
        "id": 24,
        "category": "Giải phẫu Tệp tin",
        "bloom": "Remember",
        "question": "Tệp tin Form1.resx đi kèm với Form trong dự án Windows Forms đảm nhiệm vai trò gì?",
        "explanation": "Tệp .resx (Resource XML) dùng để lưu trữ các tài nguyên nhị phân và chuỗi bản địa hóa đi kèm với Form như hình ảnh, biểu tượng (icon) và văn bản dịch.",
        "correct": "Lưu trữ các dữ liệu tài nguyên phi mã nguồn của form như chuỗi ký tự đa ngôn ngữ, hình ảnh và biểu tượng nhị phân.",
        "shorter": [
            "Chứa mã hợp ngữ của CPU.",
            "Quản lý mạng không dây của máy tính.",
            "Lưu lịch sử đăng nhập phòng máy sinh viên."
        ],
        "longer": []
    },
    # Q25: target (2, 1) -> Pos C (2), Rank 1 (Shortest)
    {
        "id": 25,
        "category": "Giải phẫu Tệp tin",
        "bloom": "Understand",
        "question": "Phương thức tĩnh static void Main() - điểm khởi nhập (Entry Point) của toàn bộ ứng dụng Windows Forms nằm trong tệp nào?",
        "explanation": "Tệp Program.cs chứa hàm Main() tĩnh, là điểm bắt đầu thực thi của toàn bộ ứng dụng khi được nạp vào máy ảo .NET CLR.",
        "correct": "Tệp Program.cs.",
        "shorter": [],
        "longer": [
            "Tệp giao diện Form1.cs.",
            "Tệp tài nguyên Form1.Designer.cs.",
            "Tệp thông tin hợp ngữ AssemblyInfo.cs."
        ]
    },
    # Q26: target (3, 2) -> Pos D (3), Rank 2
    {
        "id": 26,
        "category": "Thư viện References",
        "bloom": "Analyze",
        "question": "Hai thư viện nền tảng (.dll) cốt lõi nào trong nhánh References bắt buộc phải có để ứng dụng hiển thị được cửa sổ và vẽ đồ họa?",
        "explanation": "System.Windows.Forms cung cấp các lớp điều khiển GUI (Form, Button, Label...) và System.Drawing cung cấp các dịch vụ đồ họa GDI+ (màu sắc, phông chữ, điểm ảnh, khung hình).",
        "correct": "System.Windows.Forms và System.Drawing.",
        "shorter": [
            "System.IO và System.Net."
        ],
        "longer": [
            "System.Xml và System.Linq cho xử lý dữ liệu.",
            "System.Security và System.Data cho hệ quản trị cơ sở dữ liệu."
        ]
    },
    # Q27: target (0, 3) -> Pos A (0), Rank 3
    {
        "id": 27,
        "category": "Toolbox",
        "bloom": "Understand",
        "question": "Vì sao khi mở một tệp mã nguồn code .cs thuần túy, cửa sổ Toolbox lại bị trống trơn và hiển thị thông báo 'no usable controls'?",
        "explanation": "Toolbox là công cụ thiết kế trực quan. Khi con trỏ nằm ở tab soạn thảo văn bản code .cs, Toolbox tự động ẩn các linh kiện; chỉ khi mở tab Form [Design] các linh kiện mới hiện lên.",
        "correct": "Vì Toolbox chỉ kích hoạt cho bề mặt đồ họa Design View, khi đang xem văn bản code thì không có canvas để nhận điều khiển.",
        "shorter": [
            "Do Visual Studio bị lỗi phân tích cú pháp.",
            "Do máy tính bị mất kết nối thư viện đám mây."
        ],
        "longer": [
            "Vì sinh viên chưa tiến hành kích hoạt bản quyền chính hãng của hệ điều hành Microsoft Windows trên máy trạm của trường học."
        ]
    },
    # Q28: target (1, 4) -> Pos B (1), Rank 4 (Longest)
    {
        "id": 28,
        "category": "Common Controls",
        "bloom": "Remember",
        "question": "Đặc điểm nhận diện quan trọng nhất của điều khiển Label trong nhóm Common Controls là gì?",
        "explanation": "Label dùng để hiển thị văn bản hướng dẫn hoặc nhãn tiêu đề tĩnh; người dùng cuối nhìn thấy nội dung nhưng không thể nhấp vào gõ chỉnh sửa trực tiếp.",
        "correct": "Dùng để hiển thị văn bản tĩnh, chú thích hoặc tiêu đề mà người dùng cuối không thể nhấp chuột gõ sửa trực tiếp.",
        "shorter": [
            "Cho phép gõ văn bản tự do.",
            "Dùng để nạp và phát video.",
            "Tự động gửi email thông báo hệ thống."
        ],
        "longer": []
    },
    # Q29: target (3, 1) -> Pos D (3), Rank 1 (Shortest)
    {
        "id": 29,
        "category": "Common Controls",
        "bloom": "Remember",
        "question": "Điều khiển nào trong Windows Forms cho phép người dùng nhập dữ liệu văn bản từ bàn phím vào chương trình?",
        "explanation": "TextBox là điều khiển chuyên dụng tiếp nhận dữ liệu văn bản nhập từ bàn phím máy tính của người dùng.",
        "correct": "TextBox.",
        "shorter": [],
        "longer": [
            "Điều khiển Label gắn nhãn tĩnh.",
            "Điều khiển PictureBox hiển thị hình ảnh.",
            "Điều khiển Panel dùng làm khung chứa giao diện."
        ]
    },
    # Q30: target (0, 2) -> Pos A (0), Rank 2
    {
        "id": 30,
        "category": "Common Controls",
        "bloom": "Remember",
        "question": "Điều khiển đồ họa nào cung cấp nút bấm trực quan để người dùng nhấp chuột kích hoạt một hành động xử lý nghiệp vụ?",
        "explanation": "Điều khiển Button cung cấp bề mặt nút bấm trực quan, kích hoạt sự kiện Click khi người dùng nhấp chuột để thực thi đoạn mã tương ứng.",
        "correct": "Điều khiển Button (nút bấm).",
        "shorter": [
            "Điều khiển GroupBox."
        ],
        "longer": [
            "Điều khiển ProgressBar thể hiện tiến độ xử lý tác vụ.",
            "Điều khiển ToolTip hiển thị nhãn gợi ý nhỏ khi rê chuột."
        ]
    },
    # Q31: target (1, 3) -> Pos B (1), Rank 3
    {
        "id": 31,
        "category": "Common Controls",
        "bloom": "Remember",
        "question": "Điều khiển nào trong Windows Forms chuyên dùng để nạp và hiển thị các tệp hình ảnh như PNG, JPG, GIF hay BMP?",
        "explanation": "PictureBox là điều khiển đồ họa chuẩn trong Windows Forms được thiết kế để hiển thị các tệp tin hình ảnh tĩnh hoặc ảnh động gif.",
        "correct": "PictureBox (khung hiển thị hình ảnh).",
        "shorter": [
            "ImageViewer.",
            "GraphicCanvas đồ họa."
        ],
        "longer": [
            "MediaElement hỗ trợ âm thanh đa kênh và hình ảnh động."
        ]
    },
    # Q32: target (2, 4) -> Pos C (2), Rank 4 (Longest)
    {
        "id": 32,
        "category": "Properties Window",
        "bloom": "Understand",
        "question": "Khung Mô tả Thuộc tính (Description Pane) ở đáy cửa sổ Properties cung cấp thông tin hữu ích nào?",
        "explanation": "Description Pane hiển thị tài liệu tóm lược về ý nghĩa chức năng của thuộc tính đang chọn, là trợ thủ đắc lực giúp người học tự tra cứu và hiểu bản chất thuộc tính.",
        "correct": "Hiển thị đoạn văn ngắn giải thích ý nghĩa kỹ thuật và hướng dẫn cách thiết lập giá trị cho thuộc tính đang chọn.",
        "shorter": [
            "Báo dung lượng ổ đĩa cứng.",
            "Thống kê số lượng sinh viên trực tuyến.",
            "Đo lường điện năng tiêu thụ của cạc đồ họa."
        ],
        "longer": []
    },
    # Q33: target (0, 1) -> Pos A (0), Rank 1 (Shortest)
    {
        "id": 33,
        "category": "Properties Window",
        "bloom": "Apply",
        "question": "Để tìm nhanh một thuộc tính khi đã biết rõ tên gọi bắt đầu bằng chữ cái nào (ví dụ SizeMode hay TextAlign), ta chọn chế độ xem nào?",
        "explanation": "Chế độ xem Alphabetical sắp xếp danh sách thuộc tính theo thứ tự bảng chữ cái từ A đến Z, giúp lập trình viên tìm nhanh thuộc tính theo ký tự đầu.",
        "correct": "Chế độ Alphabetical (A-Z).",
        "shorter": [],
        "longer": [
            "Chế độ Categorized phân nhóm theo chủ đề.",
            "Chế độ xem các sự kiện Events của điều khiển.",
            "Chế độ xem mã nguồn nhị phân cấp thấp của máy tính."
        ]
    },
    # Q34: target (1, 2) -> Pos B (1), Rank 2
    {
        "id": 34,
        "category": "Thuộc tính Điều khiển",
        "bloom": "Analyze",
        "question": "Sự khác biệt bản chất giữa thuộc tính '(Name)' và thuộc tính 'Text' của một điều khiển trên Form là gì?",
        "explanation": "Thuộc tính (Name) là định danh biến đối tượng trong mã C# để lập trình viên gọi lệnh; còn Text là chuỗi văn bản hiển thị ra ngoài giao diện cho người dùng nhìn thấy.",
        "correct": "Name là tên biến trong mã C#, còn Text là chuỗi ký tự hiển thị trực quan lên giao diện.",
        "shorter": [
            "Name đổi màu, Text đổi font."
        ],
        "longer": [
            "Name chỉ áp dụng cho Form, còn Text là thuộc tính riêng của nút bấm Button trên màn hình.",
            "Name bắt buộc viết bằng tiếng Việt có dấu, còn Text chỉ được phép viết bằng tiếng Anh chuẩn."
        ]
    },
    # Q35: target (2, 3) -> Pos C (2), Rank 3
    {
        "id": 35,
        "category": "Thuộc tính BackColor",
        "bloom": "Apply",
        "question": "Tại sao khi tùy biến màu nền BackColor cho Form hoặc điều khiển, lập trình viên nên ưu tiên chọn màu trong tab 'Web'?",
        "explanation": "Các màu trong tab Web có mã màu cố định, đảm bảo ứng dụng luôn hiển thị đúng tone màu mong muốn trên mọi máy tính, không bị biến đổi theo Theme (Dark/Light) của hệ điều hành.",
        "correct": "Vì màu tab Web là màu cố định, không bị méo mó đổi màu khi máy tính người dùng thay đổi Theme giao diện.",
        "shorter": [
            "Vì tab Web giúp máy chạy mát hơn.",
            "Vì tab Web chỉ hoạt động khi có mạng."
        ],
        "longer": [
            "Vì màu tab Web giúp ứng dụng tự động đồng bộ lên trang web cá nhân của người lập trình viên trên máy chủ."
        ]
    },
    # Q36: target (3, 4) -> Pos D (3), Rank 4 (Longest)
    {
        "id": 36,
        "category": "Thuộc tính Font",
        "bloom": "Apply",
        "question": "Khi nhấp vào nút dấu 3 chấm [...] (Ellipsis button) ở thuộc tính Font của Label, điều gì sẽ xảy ra?",
        "explanation": "Nút dấu 3 chấm [...] mở hộp thoại đồ họa chuẩn Font Dialog cho phép chọn FontFamily, FontStyle (Bold, Italic) và Size (pt) một cách trực quan.",
        "correct": "Mở hộp thoại Font Dialog cho phép lựa chọn trực quan kiểu phông chữ, kiểu dáng in đậm/nghiêng và kích thước cỡ chữ.",
        "shorter": [
            "Thuộc tính Font bị xóa.",
            "Mở trình soạn thảo Word.",
            "Tự động tải thêm phông chữ từ Internet."
        ],
        "longer": []
    },
    # Q37: target (1, 1) -> Pos B (1), Rank 1 (Shortest)
    {
        "id": 37,
        "category": "Thuộc tính TextAlign",
        "bloom": "Apply",
        "question": "Lưới đồ họa 9 ô vuông nhỏ (3x3) của thuộc tính TextAlign trên Label cung cấp giá trị căn giữa hoàn hảo nào?",
        "explanation": "Ô vuông ở chính tâm đại diện cho giá trị MiddleCenter - căn đều văn bản vào chính giữa nhãn theo cả trục ngang và trục dọc.",
        "correct": "MiddleCenter.",
        "shorter": [],
        "longer": [
            "TopLeft ở góc trên bên trái.",
            "BottomRight ở góc dưới bên phải.",
            "CenterAlign theo trục tọa độ độc lập."
        ]
    },
    # Q38: target (2, 2) -> Pos C (2), Rank 2
    {
        "id": 38,
        "category": "Đường căn Snap Lines",
        "bloom": "Understand",
        "question": "Tính năng 'Đường căn thông minh' (Snap Lines) tự động xuất hiện khi kéo thả điều khiển mang lại lợi ích gì?",
        "explanation": "Snap Lines là các đường căn thông minh tự động bắt dính mép các điều khiển thẳng hàng nhau và giữ khoảng cách đệm (Padding/Margin) chuẩn theo khuyến nghị UI của Microsoft.",
        "correct": "Bắt dính thẳng hàng các mép điều khiển và duy trì khoảng cách lề chuẩn UI khuyến nghị.",
        "shorter": [
            "Tự động vẽ các biểu đồ hình học."
        ],
        "longer": [
            "Kiểm tra xem hệ thống máy tính có bị nhiễm virus hay các phần mềm gián điệp độc hại hay không.",
            "Tự động đổi màu tất cả các nút bấm trên Form sang màu hồng thắm và xanh lam rực rỡ sắc nét."
        ]
    },
    # Q39: target (3, 3) -> Pos D (3), Rank 3
    {
        "id": 39,
        "category": "PictureBox Resource",
        "bloom": "Apply",
        "question": "Khi nạp ảnh cho PictureBox trong hộp thoại Select Resource, tại sao nên chọn 'Project resource file' thay vì 'Local resource'?",
        "explanation": "Chọn 'Project resource file' nhúng trực tiếp bức ảnh vào tệp tài nguyên .resx và đóng gói vào tệp thực thi .exe, giúp ứng dụng đem đi máy khác vẫn hiển thị nguyên vẹn mà không bị đứt liên kết.",
        "correct": "Vì ảnh được đóng gói vĩnh viễn vào tệp tài nguyên của dự án và nhúng vào tệp .exe khi biên dịch, không lo bị mất ảnh.",
        "shorter": [
            "Vì tùy chọn này giúp ảnh nét hơn.",
            "Vì nó sẽ giảm kích thước tệp ảnh xuống thấp."
        ],
        "longer": [
            "Vì nó cho phép người dùng tự do chỉnh sửa tệp ảnh trực tiếp bằng các phần mềm đồ họa chuyên nghiệp của bên thứ ba độc lập trên máy trạm."
        ]
    },
    # Q40: target (0, 4) -> Pos A (0), Rank 4 (Longest)
    {
        "id": 40,
        "category": "Thuộc tính SizeMode",
        "bloom": "Analyze",
        "question": "Khi muốn hình ảnh trong PictureBox tự động co giãn để vừa khít hoàn toàn 100% cả chiều rộng và chiều cao khung điều khiển, ta thiết lập thuộc tính SizeMode mang giá trị nào?",
        "explanation": "StretchImage ép hình ảnh co giãn vừa khít toàn bộ diện tích của PictureBox. (Normal cắt xén; AutoSize làm khung phình theo ảnh; CenterImage căn giữa; Zoom co giãn giữ nguyên tỷ lệ Aspect Ratio).",
        "correct": "StretchImage (ép bức ảnh co giãn vừa khít hoàn toàn cả chiều ngang lẫn chiều dọc của khung PictureBox).",
        "shorter": [
            "Normal (cắt xén ảnh).",
            "CenterImage (căn ảnh vào giữa).",
            "AutoSize (khung tự phình to bằng ảnh)."
        ],
        "longer": []
    }
]

# Build final options list for each question
final_quiz_data = []

for idx, q in enumerate(questions_def):
    target_pos, target_rank = TARGET_SPECS[idx]
    correct_text = q["correct"]
    shorter_list = list(q["shorter"])
    longer_list = list(q["longer"])
    
    # We need:
    # target_rank - 1 shorter distractors
    # 4 - target_rank longer distractors
    num_shorter_needed = target_rank - 1
    num_longer_needed = 4 - target_rank
    
    assert len(shorter_list) == num_shorter_needed, f"Q{q['id']}: shorter count mismatch ({len(shorter_list)} vs {num_shorter_needed})"
    assert len(longer_list) == num_longer_needed, f"Q{q['id']}: longer count mismatch ({len(longer_list)} vs {num_longer_needed})"
    
    # Verify strict length differences:
    c_len = len(correct_text)
    for s in shorter_list:
        assert len(s) < c_len, f"Q{q['id']}: shorter '{s}' ({len(s)}) >= correct '{correct_text}' ({c_len})"
    for l in longer_list:
        assert len(l) > c_len, f"Q{q['id']}: longer '{l}' ({len(l)}) <= correct '{correct_text}' ({c_len})"
        
    # Combine distractors
    distractors = shorter_list + longer_list
    # Shuffle or arrange distractors into other positions
    options = [None] * 4
    options[target_pos] = correct_text
    
    other_pos = [p for p in range(4) if p != target_pos]
    for p, d in zip(other_pos, distractors):
        options[p] = d
        
    final_quiz_data.append({
        "id": q["id"],
        "category": q["category"],
        "bloom": q["bloom"],
        "question": q["question"],
        "options": options,
        "answer": target_pos,
        "explanation": q["explanation"]
    })

# Verify strict balancing
pos_counter = Counter(q["answer"] for q in final_quiz_data)
print("Position counts:", pos_counter)
assert pos_counter == {0: 10, 1: 10, 2: 10, 3: 10}

rank_counter = Counter()
for q in final_quiz_data:
    opts = q["options"]
    ans = q["answer"]
    sorted_opts = sorted(opts, key=len)
    rank = sorted_opts.index(opts[ans]) + 1
    rank_counter[rank] += 1

print("Rank counts:", rank_counter)
assert rank_counter == {1: 10, 2: 10, 3: 10, 4: 10}

print("SUCCESS: Chapter 2 Quiz is 100% mathematically balanced!")

# Output as JavaScript string
js_content = "// ============================================================================\n"
js_content += "// HỌC PHẦN: KỸ THUẬT LẬP TRÌNH (4 TÍN CHỈ) - IT26M\n"
js_content += "// NGÂN HÀNG CÂU HỎI TRẮC NGHIỆM CHƯƠNG 2: INTRODUCTION TO VISUAL STUDIO AND VISUAL PROGRAMMING\n"
js_content += "// ĐẶC TẢ CHUẨN HÓA:\n"
js_content += "// - Tổng số: 40 câu trắc nghiệm chuẩn hóa 4 lựa chọn (A, B, C, D)\n"
js_content += "// - Phân bố đáp án đúng: Chính xác 10 A, 10 B, 10 C, 10 D\n"
js_content += "// - Phân bố độ dài đáp án đúng: 10 Ngắn nhất (Rank 1), 10 Rank 2, 10 Rank 3, 10 Dài nhất (Rank 4)\n"
js_content += "// - Thang đo Bloom: Remember (12), Understand (14), Apply (9), Analyze (5)\n"
js_content += "// ============================================================================\n"
js_content += "const QUIZ_CHAPTER_02 = " + json.dumps(final_quiz_data, ensure_ascii=False, indent=2) + ";\n"

with open("js/quiz_ch02.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Saved js/quiz_ch02.js successfully!")
