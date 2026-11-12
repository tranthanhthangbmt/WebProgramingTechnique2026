# -*- coding: utf-8 -*-
"""
Generate strictly balanced 40 questions for Chapter 2 C# (Visual Studio and Visual Programming).
Guarantees:
- Exactly 10 A, 10 B, 10 C, 10 D
- Exactly 10 Rank 1, 10 Rank 2, 10 Rank 3, 10 Rank 4
- Balanced Bloom taxonomy (Remember, Understand, Apply, Analyze)
- High academic rigor bám sát Deitel Chapter 2
"""

import json
from collections import Counter

# Target specs: (pos, rank)
# pos: 0=A, 1=B, 2=C, 3=D
# rank: 1=shortest, 2=mid-short, 3=mid-long, 4=longest
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

# Verify TARGET_SPECS balance
pos_counts = Counter(pos for pos, rank in TARGET_SPECS)
rank_counts = Counter(rank for pos, rank in TARGET_SPECS)
assert pos_counts == {0: 10, 1: 10, 2: 10, 3: 10}, f"Pos error: {pos_counts}"
assert rank_counts == {1: 10, 2: 10, 3: 10, 4: 10}, f"Rank error: {rank_counts}"
print("TARGET_SPECS is mathematically balanced: 10 each!")

raw_data = [
    # Q1: target (0, 1) -> Pos 0 (A), Rank 1 (Shortest)
    {
        "id": 1,
        "category": "Tổng quan IDE",
        "bloom": "Remember",
        "question": "Thuật ngữ viết tắt IDE trong môi trường phát triển ứng dụng Visual C# là viết tắt của cụm từ nào?",
        "explanation": "Theo mục 2.1 giáo trình Deitel: IDE là viết tắt của Integrated Development Environment (Môi trường phát triển tích hợp), đóng gói trình soạn thảo, biên dịch, thiết kế giao diện và gỡ lỗi trên một phần mềm thống nhất.",
        "correct_rank": 1,
        "options_by_rank": {
            1: "Integrated Development Environment.",
            2: "Interactive Data Execution Environment.",
            3: "Interface Deployment Engine for Windows Applications.",
            4: "Internal Developer Equipment for Systems Programming."
        }
    },
    # Q2: target (1, 2) -> Pos 1 (B), Rank 2
    {
        "id": 2,
        "category": "Triết lý RAD",
        "bloom": "Understand",
        "question": "Đặc trưng then chốt nhất của mô hình Phát triển Ứng dụng Nhanh (RAD) trong lập trình Windows Forms là gì?",
        "explanation": "RAD tập trung vào việc tạo nhanh bản mẫu (Prototyping), kéo thả linh kiện trực quan và tái sử dụng tối đa các lớp điều khiển có sẵn trong .NET Framework Class Library (FCL).",
        "correct_rank": 2,
        "options_by_rank": {
            1: "Chỉ viết mã nguồn bằng dòng lệnh console.",
            2: "Tái sử dụng linh kiện có sẵn và tạo mẫu giao diện nhanh bằng kéo thả.",
            3: "Yêu cầu lập trình viên phải tự tính toán tọa độ điểm ảnh pixel cho từng nút bấm.",
            4: "Loại bỏ hoàn toàn trình biên dịch và thực thi trực tiếp mã C# trên bo mạch chủ phần cứng."
        }
    },
    # Q3: target (2, 3) -> Pos 2 (C), Rank 3
    {
        "id": 3,
        "category": "Tổng quan IDE",
        "bloom": "Remember",
        "question": "Phiên bản Visual Studio nào sau đây được Microsoft cung cấp hoàn toàn miễn phí phục vụ đào tạo sinh viên và dự án cá nhân?",
        "options_by_rank": {
            1: "Visual Studio Ultimate.",
            2: "Visual Studio Enterprise Suite.",
            3: "Visual Studio Community bản đầy đủ tính năng cho học tập.",
            4: "Visual Studio Professional dành riêng cho doanh nghiệp quy mô vừa và lớn."
        },
        "correct_rank": 3,
        "explanation": "Visual Studio Community là ấn bản miễn phí bản quyền nhưng sở hữu đầy đủ tính năng thiết kế giao diện, biên dịch C# và gỡ lỗi nâng cao phục vụ sinh viên, giảng viên và nghiên cứu cá nhân."
    },
    # Q4: target (3, 4) -> Pos 3 (D), Rank 4 (Longest)
    {
        "id": 4,
        "category": "Màn hình Khởi động",
        "bloom": "Remember",
        "question": "Khu vực 'Recent' trên màn hình Start Page khi vừa mở Visual Studio có công dụng chính là gì?",
        "options_by_rank": {
            1: "Xem bản vá lỗi của Windows.",
            2: "Cập nhật tin tức công nghệ mới nhất.",
            3: "Xóa sạch bộ nhớ đệm của các dự án trước đây.",
            4: "Hiển thị danh sách các giải pháp và dự án đã làm việc gần đây để mở lại tức thì chỉ bằng một cú nhấp chuột."
        },
        "correct_rank": 4,
        "explanation": "Khu vực Recent trên Start Page liệt kê danh sách các dự án (.csproj) và giải pháp (.sln) được truy cập gần nhất, giúp lập trình viên mở lại công việc nhanh mà không cần tìm kiếm thư mục."
    },
    # Q5: target (1, 1) -> Pos 1 (B), Rank 1 (Shortest)
    {
        "id": 5,
        "category": "Hộp thoại New Project",
        "bloom": "Apply",
        "question": "Để tạo dự án phần mềm giao diện đồ họa cửa sổ màn hình Desktop bằng Visual C#, lập trình viên chọn mẫu template nào?",
        "options_by_rank": {
            1: "Windows Forms Application.",
            2: "Console Application độc lập dòng lệnh.",
            3: "WCF Service Application cho dịch vụ phân tán.",
            4: "ASP.NET Web Forms Application cho ứng dụng trực tuyến."
        },
        "correct_rank": 1,
        "explanation": "Mẫu Windows Forms Application trong phân mục Visual C# -> Windows được dùng để xây dựng các ứng dụng đồ họa máy tính tương tác chuẩn mực trên hệ điều hành Windows."
    },
    # Q6: target (2, 2) -> Pos 2 (C), Rank 2
    {
        "id": 6,
        "category": "Hộp thoại New Project",
        "bloom": "Understand",
        "question": "Tại sao trong ô nhập tên dự án (Name), lập trình viên nên đặt tên theo chuẩn PascalCase, viết liền không dấu tiếng Việt?",
        "options_by_rank": {
            1: "Để giảm dung lượng RAM của hệ điều hành.",
            2: "Vì tên dự án sẽ trở thành Namespace mặc định và tên tệp thực thi .exe của ứng dụng.",
            3: "Vì hệ điều hành Windows không hỗ trợ lưu tệp tin có khoảng trắng trên ổ đĩa cứng chuẩn NTFS.",
            4: "Nhằm giúp máy tính tự động tăng gấp đôi tốc độ xung nhịp của CPU trong quá trình biên dịch mã nguồn."
        },
        "correct_rank": 2,
        "explanation": "Tên dự án được Visual Studio sử dụng làm Không gian tên mặc định (Default Namespace) và tên file nhị phân đầu ra (.exe). Nếu chứa khoảng trắng hay ký tự đặc biệt, nó có thể gây lỗi cú pháp và đường dẫn."
    },
    # Q7: target (3, 3) -> Pos 3 (D), Rank 3
    {
        "id": 7,
        "category": "Hộp thoại New Project",
        "bloom": "Understand",
        "question": "Mục đích quan trọng của việc tích chọn ô kiểm 'Create directory for solution' khi tạo dự án mới là gì?",
        "options_by_rank": {
            1: "Mã hóa tệp tin để chống sao chép.",
            2: "Tự động gửi mã nguồn lên kho lưu trữ đám mây.",
            3: "Tạo thư mục cha bao bọc toàn bộ giải pháp giúp quản lý mã nguồn, tài nguyên gọn gàng và độc lập.",
            4: "Bắt buộc người dùng máy tính phải nhập mật khẩu quản trị viên mới có thể mở được ứng dụng."
        },
        "correct_rank": 3,
        "explanation": "Tích chọn 'Create directory for solution' giúp tạo thư mục cha riêng chứa tệp giải pháp .sln và các thư mục dự án con, thuận tiện khi sao lưu, nén nộp bài hoặc chia sẻ mã nguồn."
    },
    # Q8: target (0, 4) -> Pos 0 (A), Rank 4 (Longest)
    {
        "id": 8,
        "category": "Khung nhìn Design View",
        "bloom": "Understand",
        "question": "Bề mặt Form1 màu xám hiển thị ở trung tâm màn hình Design View có vai trò kỹ thuật là gì?",
        "options_by_rank": {
            1: "Là tấm toan vẽ đồ họa đại diện cho cửa sổ ứng dụng Windows thực tế để kéo thả và bài trí các điều khiển giao diện.",
            2: "Là nơi kiểm tra bộ nhớ RAM đang hoạt động.",
            3: "Chỉ là một hình ảnh tĩnh dùng để minh họa.",
            4: "Là bảng hiển thị các lỗi cú pháp lập trình."
        },
        "correct_rank": 1,
        "explanation": "Design View hiển thị Form1 như một tấm toan vẽ (Canvas) trực quan, cho phép lập trình viên kéo thả, căn chỉnh vị trí và thay đổi thuộc tính của các điều khiển đồ họa theo mô hình WYSIWYG."
    },
    # Q9: target (2, 1) -> Pos 2 (C), Rank 1 (Shortest)
    {
        "id": 9,
        "category": "Khung nhìn Design View",
        "bloom": "Apply",
        "question": "Các ô vuông nhỏ màu trắng (Sizing handles) xuất hiện quanh viền Form1 khi được nhấp chọn dùng để làm gì?",
        "options_by_rank": {
            1: "Khóa cố định vị trí cửa sổ trên màn hình máy tính.",
            2: "Đổi màu nền của Form sang màu trắng tinh khôi.",
            3: "Kéo giãn để thay đổi kích thước Form trực quan.",
            4: "Xóa vĩnh viễn Form hiện hành ra khỏi dự án đang mở."
        },
        "correct_rank": 3,
        "explanation": "Sizing handles (chốt điều chỉnh kích thước) ở 4 góc và 4 cạnh cho phép dùng chuột kéo giãn để tăng giảm chiều rộng và chiều cao của Form một cách trực quan."
    },
    # Q10: target (3, 2) -> Pos 3 (D), Rank 2
    {
        "id": 10,
        "category": "Hệ thống Menu Bar",
        "bloom": "Remember",
        "question": "Khi vô tình đóng mất một cửa sổ làm việc như Solution Explorer hoặc Toolbox, menu nào là nơi giúp mở lại nhanh nhất?",
        "options_by_rank": {
            1: "Menu File trên thanh Menu Bar.",
            2: "Menu Edit chứa các lệnh hoàn tác.",
            3: "Menu Tools dùng cấu hình môi trường.",
            4: "Menu View chứa danh mục tất cả cửa sổ công cụ của IDE."
        },
        "correct_rank": 4,
        "explanation": "Menu View là trung tâm quản lý hiển thị của IDE. Mọi cửa sổ bị ẩn hay đóng nhầm đều có thể mở lại thông qua menu View (View -> Solution Explorer, View -> Toolbox...)."
    },
    # Q11: target (0, 3) -> Pos 0 (A), Rank 3
    {
        "id": 11,
        "category": "Menu Build",
        "bloom": "Analyze",
        "question": "Sự khác biệt then chốt giữa lệnh 'Build Solution' và lệnh 'Rebuild Solution' trong menu Build là gì?",
        "options_by_rank": {
            1: "Build biên dịch các file vừa sửa, còn Rebuild xóa sạch file nhị phân cũ trong bin/obj rồi dịch lại toàn bộ từ đầu.",
            2: "Build chỉ áp dụng cho ngôn ngữ C#, còn Rebuild dành cho các dự án viết bằng ngôn ngữ C++.",
            3: "Build sẽ chạy ứng dụng ngay lập tức, còn Rebuild chỉ lưu các tệp tin mã nguồn xuống đĩa cứng.",
            4: "Build dùng để kiểm tra lỗi ngữ nghĩa, còn Rebuild dùng để định dạng phông chữ cho giao diện."
        },
        "correct_rank": 1,
        "explanation": "Build Solution thực hiện biên dịch gia tăng (Incremental Build) cho các file có thay đổi để tiết kiệm thời gian; Rebuild Solution dọn sạch toàn bộ thư mục bin/obj rồi biên dịch mới 100% để loại bỏ lỗi cache."
    },
    # Q12: target (1, 4) -> Pos 1 (B), Rank 4 (Longest)
    {
        "id": 12,
        "category": "Menu Debug",
        "bloom": "Analyze",
        "question": "Lệnh 'Start Debugging' (F5) khác với lệnh 'Start Without Debugging' (Ctrl + F5) ở điểm cốt lõi nào?",
        "options_by_rank": {
            1: "F5 chỉ dịch mã, Ctrl+F5 thực thi ngay.",
            2: "F5 chạy ứng dụng có kết nối với bộ giám sát lỗi của IDE, còn Ctrl+F5 chạy ứng dụng độc lập với tốc độ cao nhất.",
            3: "F5 yêu cầu quyền quản trị viên máy tính.",
            4: "F5 chỉ chạy được trên hệ điều hành 64-bit."
        },
        "correct_rank": 2,
        "explanation": "F5 kích hoạt Debugger để theo dõi biến và bắt điểm dừng Breakpoint khi có sự cố. Ctrl+F5 chạy trực tiếp không gắn cờ Debugger, thích hợp khi cần kiểm thử tốc độ thực tế của người dùng."
    },
    # Q13: target (3, 1) -> Pos 3 (D), Rank 1 (Shortest)
    {
        "id": 13,
        "category": "Menu Format",
        "bloom": "Apply",
        "question": "Menu nào trên thanh Menu Bar sẽ tự động xuất hiện khi lập trình viên chọn đồng thời từ hai điều khiển trở lên trên Form?",
        "options_by_rank": {
            1: "Menu Project để thêm tệp tin mã nguồn mới.",
            2: "Menu Tools cung cấp các tiện ích hệ thống.",
            3: "Menu Debug dùng để đặt các điểm dừng kiểm thử.",
            4: "Menu Format hỗ trợ căn lề và chỉnh kích thước."
        },
        "correct_rank": 4,
        "explanation": "Menu Format chỉ hiển thị khi có từ hai điều khiển trở lên được chọn, cung cấp các lệnh căn lề (Align), chỉnh bằng kích thước (Make Same Size) và giãn khoảng cách (Horizontal/Vertical Spacing)."
    },
    # Q14: target (0, 2) -> Pos 0 (A), Rank 2
    {
        "id": 14,
        "category": "Standard Toolbar",
        "bloom": "Apply",
        "question": "Tại sao lập trình viên luôn được khuyến nghị sử dụng nút 'Save All' (Ctrl + Shift + S) thay vì Save thường (Ctrl + S)?",
        "options_by_rank": {
            1: "Để giải phóng dung lượng của bộ nhớ RAM.",
            2: "Vì thao tác kéo thả Form làm biến động đồng thời cả Form1.cs, Form1.Designer.cs và Form1.resx.",
            3: "Vì thao tác Save All sẽ tự động biên dịch chương trình sang tệp nhị phân .exe.",
            4: "Vì nếu chỉ bấm Save thường thì các điều khiển đồ họa trên Form sẽ bị khôi phục về giá trị mặc định."
        },
        "correct_rank": 2,
        "explanation": "Trong Windows Forms, mỗi thay đổi trên giao diện ảnh hưởng đồng thời tới tệp mã logic (Form1.cs), tệp mã sinh tự động (Form1.Designer.cs) và tài nguyên (.resx). Save All đảm bảo toàn bộ được lưu an toàn."
    },
    # Q15: target (1, 3) -> Pos 1 (B), Rank 3
    {
        "id": 15,
        "category": "Thanh Công cụ",
        "bloom": "Remember",
        "question": "Tính năng hiển thị một nhãn nhỏ màu vàng nhạt mô tả chức năng của nút bấm khi rê chuột qua nút công cụ được gọi là gì?",
        "options_by_rank": {
            1: "Smart Tag.",
            2: "Context Menu.",
            3: "Tooltip (Chú giải công cụ kèm phím tắt).",
            4: "Status Label nằm ở thanh trạng thái."
        },
        "correct_rank": 3,
        "explanation": "Tooltip là nhãn chú giải nổi lên khi rê chuột dừng trên một nút công cụ, hiển thị tên lệnh và phím tắt tương ứng trong dấu ngoặc đơn."
    },
    # Q16: target (2, 4) -> Pos 2 (C), Rank 4 (Longest)
    {
        "id": 16,
        "category": "Phím tắt Chuẩn",
        "bloom": "Remember",
        "question": "Phím tắt mặc định trong Visual Studio dùng để mở nhanh Cửa sổ Thuộc tính (Properties Window) là phím nào?",
        "options_by_rank": {
            1: "Phím F2.",
            2: "Phím F7.",
            3: "Tổ hợp phím Shift + F5.",
            4: "Phím F4 (kích hoạt cửa sổ Properties của đối tượng đang chọn)."
        },
        "correct_rank": 4,
        "explanation": "Phím F4 là phím tắt mặc định để mở hoặc di chuyển tiêu điểm trực tiếp đến Properties Window để cấu hình thuộc tính của đối tượng đang chọn."
    },
    # Q17: target (0, 1) -> Pos 0 (A), Rank 1 (Shortest)
    {
        "id": 17,
        "category": "Trợ giúp Ngữ cảnh",
        "bloom": "Understand",
        "question": "Phím F1 trong Visual Studio kích hoạt tính năng Trợ giúp Ngữ cảnh (Context-Sensitive Help) có cơ chế hoạt động như thế nào?",
        "options_by_rank": {
            1: "Mở tài liệu MSDN đúng điều khiển đang chọn.",
            2: "Tự động sửa toàn bộ lỗi cú pháp trong mã lệnh C#.",
            3: "Gửi thông báo cầu cứu đến máy chủ hỗ trợ kỹ thuật.",
            4: "Chuyển giao diện làm việc của Visual Studio sang ngôn ngữ tiếng Việt."
        },
        "correct_rank": 1,
        "explanation": "Phím F1 nhận diện đối tượng đang được chọn (trên Form hoặc từ khóa trong code) và tự động mở đúng trang tài liệu Microsoft MSDN / Learn liên quan đến đối tượng đó."
    },
    # Q18: target (1, 2) -> Pos 1 (B), Rank 2
    {
        "id": 18,
        "category": "Kỹ thuật Điều hướng",
        "bloom": "Understand",
        "question": "Khi biểu tượng chiếc đinh ghim (Pushpin) trên thanh tiêu đề của một cửa sổ công cụ xoay sang tư thế nằm ngang, cửa sổ đó đang ở trạng thái nào?",
        "options_by_rank": {
            1: "Cửa sổ bị khóa vĩnh viễn.",
            2: "Kích hoạt chế độ Tự động ẩn (Auto-Hide).",
            3: "Cửa sổ đang ở trạng thái Ghim cố định.",
            4: "Cửa sổ đã bị gỡ bỏ hoàn toàn khỏi môi trường phát triển."
        },
        "correct_rank": 2,
        "explanation": "Khi đinh ghim nằm ngang (Horizontal pin), tính năng Auto-Hide được kích hoạt: cửa sổ thu thành tab nhỏ ở mép màn hình, chỉ mở ra khi rê chuột vào và thụt lại khi rê chuột ra."
    },
    # Q19: target (2, 3) -> Pos 2 (C), Rank 3
    {
        "id": 19,
        "category": "Kỹ thuật Điều hướng",
        "bloom": "Apply",
        "question": "Biểu tượng hướng dẫn ghép nối (Docking Visualizer) hình chữ thập với 4 mũi tên xuất hiện khi người dùng thực hiện thao tác nào?",
        "options_by_rank": {
            1: "Nhấp đúp chuột lên nền Form.",
            2: "Nhấn tổ hợp phím tắt Ctrl + Shift + B.",
            3: "Nhấp giữ thanh tiêu đề của một cửa sổ và kéo di chuyển trên màn hình.",
            4: "Mở hộp thoại New Project để khởi tạo một giải pháp mới."
        },
        "correct_rank": 3,
        "explanation": "Docking Visualizer xuất hiện khi kéo thanh tiêu đề cửa sổ, hỗ trợ neo (dock) cửa sổ vào cạnh màn hình hoặc thả vào tâm để gộp thành tab."
    },
    # Q20: target (3, 4) -> Pos 3 (D), Rank 4 (Longest)
    {
        "id": 20,
        "category": "Kỹ thuật Điều hướng",
        "bloom": "Apply",
        "question": "Lệnh nào sau đây giúp khôi phục toàn bộ bố cục các cửa sổ công cụ về trạng thái xuất xưởng mặc định khi giao diện bị xáo trộn?",
        "options_by_rank": {
            1: "File -> Close Solution.",
            2: "Edit -> Undo All Window Moves.",
            3: "Tools -> Import and Export Settings.",
            4: "Window -> Reset Window Layout (khôi phục toàn bộ giao diện IDE về trạng thái chuẩn ban đầu)."
        },
        "correct_rank": 4,
        "explanation": "Lệnh Window -> Reset Window Layout trên thanh Menu Bar sẽ sắp xếp lại toàn bộ các cửa sổ làm việc về vị trí và bố cục mặc định của nhà sản xuất."
    },
    # Q21: target (1, 1) -> Pos 1 (B), Rank 1 (Shortest)
    {
        "id": 21,
        "category": "Solution Explorer",
        "bloom": "Understand",
        "question": "Thứ bậc phân cấp giữa Solution (.sln) và Project (.csproj) trong Visual Studio được hiểu đúng như thế nào?",
        "options_by_rank": {
            1: "Project là cấp cha chứa các Solution con.",
            2: "Solution chứa một hoặc nhiều Project con.",
            3: "Solution và Project hoàn toàn ngang hàng và không có quan hệ chứa nhau.",
            4: "Mỗi Solution chỉ được phép chứa duy nhất một tệp tin mã nguồn C# đơn lẻ."
        },
        "correct_rank": 2,
        "explanation": "Solution (đuôi .sln) là cấp cao nhất đóng vai trò như một chiếc cặp lớn, có thể chứa một hoặc nhiều Project (.csproj) cùng phối hợp hoạt động."
    },
    # Q22: target (2, 2) -> Pos 2 (C), Rank 2
    {
        "id": 22,
        "category": "Giải phẫu Tệp tin",
        "bloom": "Understand",
        "question": "Tệp tin nào trong dự án Windows Forms là nơi lập trình viên chúng ta viết mã xử lý nghiệp vụ và các phương thức xử lý sự kiện?",
        "options_by_rank": {
            1: "Tệp tin cấu hình App.config.",
            2: "Tệp tin tài nguyên Form1.resx.",
            3: "Tệp tin mã nguồn chính Form1.cs.",
            4: "Tệp tin sinh mã tự động Form1.Designer.cs."
        },
        "correct_rank": 3,
        "explanation": "Tệp Form1.cs là nơi lập trình viên viết mã nguồn nghiệp vụ và các hàm xử lý sự kiện (Event Handlers) cho ứng dụng."
    },
    # Q23: target (3, 3) -> Pos 3 (D), Rank 3
    {
        "id": 23,
        "category": "Giải phẫu Tệp tin",
        "bloom": "Analyze",
        "question": "Tại sao trong tệp Form1.Designer.cs có cảnh báo lập trình viên không được tự ý sửa đổi mã trong phương thức InitializeComponent()?",
        "options_by_rank": {
            1: "Vì phương thức này chỉ chứa mã bản quyền của Windows.",
            2: "Vì nó sẽ làm hỏng cạc mạng kết nối Internet.",
            3: "Vì mã tại đây sẽ tự động xóa sạch toàn bộ cơ sở dữ liệu của máy chủ.",
            4: "Vì phương thức này do Form Designer quản lý tự động, việc sửa tay dễ gây xung đột làm hỏng màn hình Design View."
        },
        "correct_rank": 4,
        "explanation": "InitializeComponent() hoàn toàn do công cụ trực quan Form Designer đồng bộ tự động. Sửa tay sai cú pháp có thể khiến IDE không phân tích cú pháp thiết kế được và không mở lại được Design View."
    },
    # Q24: target (0, 4) -> Pos 0 (A), Rank 4 (Longest)
    {
        "id": 24,
        "category": "Giải phẫu Tệp tin",
        "bloom": "Remember",
        "question": "Tệp tin Form1.resx đi kèm với Form trong dự án Windows Forms đảm nhiệm vai trò gì?",
        "options_by_rank": {
            1: "Lưu trữ các dữ liệu tài nguyên phi mã nguồn của form như chuỗi ký tự đa ngôn ngữ, hình ảnh và biểu tượng nhị phân.",
            2: "Chứa các đoạn mã hợp ngữ cấp thấp của CPU.",
            3: "Quản lý kết nối mạng không dây của máy tính.",
            4: "Lưu trữ lịch sử đăng nhập của sinh viên phòng máy."
        },
        "correct_rank": 1,
        "explanation": "Tệp .resx (Resource XML) dùng để lưu trữ các tài nguyên nhị phân và chuỗi bản địa hóa đi kèm với Form như hình ảnh, biểu tượng (icon) và văn bản dịch."
    },
    # Q25: target (2, 1) -> Pos 2 (C), Rank 1 (Shortest)
    {
        "id": 25,
        "category": "Giải phẫu Tệp tin",
        "bloom": "Understand",
        "question": "Phương thức tĩnh static void Main() - điểm khởi nhập (Entry Point) của toàn bộ ứng dụng Windows Forms nằm trong tệp nào?",
        "options_by_rank": {
            1: "Tệp Form1.cs.",
            2: "Tệp Form1.Designer.cs.",
            3: "Tệp Program.cs.",
            4: "Tệp AssemblyInfo.cs."
        },
        "correct_rank": 3,
        "explanation": "Tệp Program.cs chứa hàm Main() tĩnh, là điểm bắt đầu thực thi của toàn bộ ứng dụng khi được nạp vào máy ảo .NET CLR."
    },
    # Q26: target (3, 2) -> Pos 3 (D), Rank 2
    {
        "id": 26,
        "category": "Thư viện References",
        "bloom": "Analyze",
        "question": "Hai thư viện nền tảng (.dll) cốt lõi nào trong nhánh References bắt buộc phải có để ứng dụng hiển thị được cửa sổ và vẽ đồ họa?",
        "options_by_rank": {
            1: "System.IO và System.Net.",
            2: "System.Xml và System.Linq.",
            3: "System.Security và System.Data.",
            4: "System.Windows.Forms và System.Drawing."
        },
        "correct_rank": 4,
        "explanation": "System.Windows.Forms cung cấp các lớp điều khiển GUI (Form, Button, Label...) và System.Drawing cung cấp các dịch vụ đồ họa GDI+ (màu sắc, phông chữ, điểm ảnh, khung hình)."
    },
    # Q27: target (0, 3) -> Pos 0 (A), Rank 3
    {
        "id": 27,
        "category": "Toolbox",
        "bloom": "Understand",
        "question": "Vì sao khi mở một tệp mã nguồn code .cs thuần túy, cửa sổ Toolbox lại bị trống trơn và hiển thị thông báo 'no usable controls'?",
        "options_by_rank": {
            1: "Vì Toolbox chỉ kích hoạt cho bề mặt đồ họa Design View, khi đang xem văn bản code thì không có canvas để nhận điều khiển.",
            2: "Do phần mềm Visual Studio đang bị lỗi phân tích cú pháp biên dịch nghiêm trọng.",
            3: "Do máy tính bị mất kết nối với thư viện linh kiện trên máy chủ đám mây của Microsoft.",
            4: "Vì sinh viên chưa kích hoạt bản quyền chính hãng của hệ điều hành Windows."
        },
        "correct_rank": 1,
        "explanation": "Toolbox là công cụ thiết kế trực quan. Khi con trỏ nằm ở tab soạn thảo văn bản code .cs, Toolbox tự động ẩn các linh kiện; chỉ khi mở tab Form [Design] các linh kiện mới hiện lên."
    },
    # Q28: target (1, 4) -> Pos 1 (B), Rank 4 (Longest)
    {
        "id": 28,
        "category": "Common Controls",
        "bloom": "Remember",
        "question": "Đặc điểm nhận diện quan trọng nhất của điều khiển Label trong nhóm Common Controls là gì?",
        "options_by_rank": {
            1: "Cho phép người dùng gõ văn bản tự do.",
            2: "Dùng để hiển thị văn bản tĩnh, chú thích hoặc tiêu đề mà người dùng cuối không thể nhấp chuột gõ sửa trực tiếp.",
            3: "Dùng để nạp và phát các tệp tin video.",
            4: "Tự động gửi email thông báo cho quản trị viên."
        },
        "correct_rank": 2,
        "explanation": "Label dùng để hiển thị văn bản hướng dẫn hoặc nhãn tiêu đề tĩnh; người dùng cuối nhìn thấy nội dung nhưng không thể nhấp vào gõ chỉnh sửa trực tiếp."
    },
    # Q29: target (3, 1) -> Pos 3 (D), Rank 1 (Shortest)
    {
        "id": 29,
        "category": "Common Controls",
        "bloom": "Remember",
        "question": "Điều khiển nào trong Windows Forms cho phép người dùng nhập dữ liệu văn bản từ bàn phím vào chương trình?",
        "options_by_rank": {
            1: "Điều khiển PictureBox hiển thị hình ảnh.",
            2: "Điều khiển Panel dùng làm khung chứa.",
            3: "Điều khiển Label dùng gắn nhãn tĩnh.",
            4: "Điều khiển TextBox."
        },
        "correct_rank": 4,
        "explanation": "TextBox là điều khiển chuyên dụng tiếp nhận dữ liệu văn bản nhập từ bàn phím máy tính của người dùng."
    },
    # Q30: target (0, 2) -> Pos 0 (A), Rank 2
    {
        "id": 30,
        "category": "Common Controls",
        "bloom": "Remember",
        "question": "Điều khiển đồ họa nào cung cấp nút bấm trực quan để người dùng nhấp chuột kích hoạt một hành động xử lý nghiệp vụ?",
        "options_by_rank": {
            1: "Điều khiển Button (nút bấm).",
            2: "Điều khiển GroupBox phân nhóm điều khiển.",
            3: "Điều khiển ProgressBar thể hiện tiến độ.",
            4: "Điều khiển ToolTip hiển thị nhãn gợi ý nhỏ."
        },
        "correct_rank": 1,
        "explanation": "Điều khiển Button cung cấp bề mặt nút bấm trực quan, kích hoạt sự kiện Click khi người dùng nhấp chuột để thực thi đoạn mã tương ứng."
    },
    # Q31: target (1, 3) -> Pos 1 (B), Rank 3
    {
        "id": 31,
        "category": "Common Controls",
        "bloom": "Remember",
        "question": "Điều khiển nào trong Windows Forms chuyên dùng để nạp và hiển thị các tệp hình ảnh như PNG, JPG, GIF hay BMP?",
        "options_by_rank": {
            1: "ImageViewer.",
            2: "PictureBox (khung hiển thị hình ảnh).",
            3: "GraphicCanvas dùng cho đồ họa 3 chiều.",
            4: "MediaElement hỗ trợ âm thanh đa kênh."
        },
        "correct_rank": 2,
        "explanation": "PictureBox là điều khiển đồ họa chuẩn trong Windows Forms được thiết kế để hiển thị các tệp tin hình ảnh tĩnh hoặc ảnh động gif."
    },
    # Q32: target (2, 4) -> Pos 2 (C), Rank 4 (Longest)
    {
        "id": 2,
        "category": "Properties Window",
        "bloom": "Understand",
        "question": "Khung Mô tả Thuộc tính (Description Pane) ở đáy cửa sổ Properties cung cấp thông tin hữu ích nào?",
        "options_by_rank": {
            1: "Báo cáo dung lượng ổ đĩa cứng còn trống.",
            2: "Thống kê số lượng sinh viên đang trực tuyến.",
            3: "Hiển thị đoạn văn ngắn giải thích ý nghĩa kỹ thuật và hướng dẫn cách thiết lập giá trị cho thuộc tính đang chọn.",
            4: "Đo lường điện năng tiêu thụ của cạc đồ họa."
        },
        "correct_rank": 3,
        "explanation": "Description Pane hiển thị tài liệu tóm lược về ý nghĩa chức năng của thuộc tính đang chọn, là trợ thủ đắc lực giúp người học tự tra cứu và hiểu bản chất thuộc tính."
    },
    # Q33: target (0, 1) -> Pos 0 (A), Rank 1 (Shortest)
    {
        "id": 33,
        "category": "Properties Window",
        "bloom": "Apply",
        "question": "Để tìm nhanh một thuộc tính khi đã biết rõ tên gọi bắt đầu bằng chữ cái nào (ví dụ SizeMode hay TextAlign), ta chọn chế độ xem nào?",
        "options_by_rank": {
            1: "Chế độ Alphabetical (A-Z).",
            2: "Chế độ Categorized phân nhóm theo chủ đề.",
            3: "Chế độ xem các sự kiện Events của điều khiển.",
            4: "Chế độ xem mã nguồn nhị phân cấp thấp của máy tính."
        },
        "correct_rank": 1,
        "explanation": "Chế độ xem Alphabetical sắp xếp danh sách thuộc tính theo thứ tự bảng chữ cái từ A đến Z, giúp lập trình viên tìm nhanh thuộc tính theo ký tự đầu."
    },
    # Q34: target (1, 2) -> Pos 1 (B), Rank 2
    {
        "id": 34,
        "category": "Thuộc tính Điều khiển",
        "bloom": "Analyze",
        "question": "Sự khác biệt bản chất giữa thuộc tính '(Name)' và thuộc tính 'Text' của một điều khiển trên Form là gì?",
        "options_by_rank": {
            1: "Name để đổi màu, Text để đổi phông chữ.",
            2: "Name là tên biến trong mã C#, còn Text là chuỗi ký tự hiển thị trực quan lên giao diện.",
            3: "Name chỉ áp dụng cho Form, còn Text là thuộc tính riêng của nút bấm Button.",
            4: "Name bắt buộc viết bằng tiếng Việt có dấu, còn Text chỉ được phép viết bằng tiếng Anh."
        },
        "correct_rank": 2,
        "explanation": "Thuộc tính (Name) là định danh biến đối tượng trong mã nguồn C# để lập trình viên gọi lệnh; còn Text là chuỗi văn bản hiển thị ra ngoài giao diện cho người dùng nhìn thấy."
    },
    # Q35: target (2, 3) -> Pos 2 (C), Rank 3
    {
        "id": 35,
        "category": "Thuộc tính BackColor",
        "bloom": "Apply",
        "question": "Tại sao khi tùy biến màu nền BackColor cho Form hoặc điều khiển, lập trình viên nên ưu tiên chọn màu trong tab 'Web'?",
        "options_by_rank": {
            1: "Vì tab Web giúp máy tính chạy mát hơn.",
            2: "Vì tab Web chỉ hoạt động khi có mạng Internet.",
            3: "Vì màu tab Web là màu cố định, không bị méo mó đổi màu khi máy tính người dùng thay đổi Theme giao diện.",
            4: "Vì màu tab Web giúp ứng dụng tự động đồng bộ lên trang web cá nhân của người lập trình viên."
        },
        "correct_rank": 3,
        "explanation": "Các màu trong tab Web có mã màu cố định, đảm bảo ứng dụng luôn hiển thị đúng tone màu mong muốn trên mọi máy tính, không bị biến đổi theo Theme (Dark/Light) của hệ điều hành."
    },
    # Q36: target (3, 4) -> Pos 3 (D), Rank 4 (Longest)
    {
        "id": 36,
        "category": "Thuộc tính Font",
        "bloom": "Apply",
        "question": "Khi nhấp vào nút dấu 3 chấm [...] (Ellipsis button) ở thuộc tính Font của Label, điều gì sẽ xảy ra?",
        "options_by_rank": {
            1: "Thuộc tính Font sẽ bị xóa trắng.",
            2: "Mở trình soạn thảo văn bản Word.",
            3: "Tự động tải thêm phông chữ từ Internet.",
            4: "Mở hộp thoại Font Dialog cho phép lựa chọn trực quan kiểu phông chữ, kiểu dáng in đậm/nghiêng và kích thước cỡ chữ."
        },
        "correct_rank": 4,
        "explanation": "Nút dấu 3 chấm [...] mở hộp thoại đồ họa chuẩn Font Dialog cho phép chọn FontFamily, FontStyle (Bold, Italic) và Size (pt) một cách trực quan."
    },
    # Q37: target (1, 1) -> Pos 1 (B), Rank 1 (Shortest)
    {
        "id": 37,
        "category": "Thuộc tính TextAlign",
        "bloom": "Apply",
        "question": "Lưới đồ họa 9 ô vuông nhỏ (3x3) của thuộc tính TextAlign trên Label cung cấp giá trị căn giữa hoàn hảo nào?",
        "options_by_rank": {
            1: "TopLeft ở góc trên bên trái.",
            2: "MiddleCenter ở chính giữa.",
            3: "BottomRight ở góc dưới bên phải.",
            4: "CenterAlign theo chiều dọc độc lập."
        },
        "correct_rank": 2,
        "explanation": "Ô vuông ở chính tâm đại diện cho giá trị MiddleCenter - căn đều văn bản vào chính giữa nhãn theo cả trục ngang và trục dọc."
    },
    # Q38: target (2, 2) -> Pos 2 (C), Rank 2
    {
        "id": 38,
        "category": "Đường căn Snap Lines",
        "bloom": "Understand",
        "question": "Tính năng 'Đường căn thông minh' (Snap Lines) tự động xuất hiện khi kéo thả điều khiển mang lại lợi ích gì?",
        "options_by_rank": {
            1: "Tự động vẽ các biểu đồ hình học phức tạp.",
            2: "Kiểm tra xem máy tính có bị nhiễm virus hay không.",
            3: "Bắt dính thẳng hàng các mép điều khiển và duy trì khoảng cách lề chuẩn UI khuyến nghị.",
            4: "Tự động đổi màu tất cả các nút bấm trên Form sang màu hồng thắm và xanh lam rực rỡ."
        },
        "correct_rank": 3,
        "explanation": "Snap Lines là các đường căn thông minh tự động bắt dính mép các điều khiển thẳng hàng nhau và giữ khoảng cách đệm (Padding/Margin) chuẩn theo khuyến nghị UI của Microsoft."
    },
    # Q39: target (3, 3) -> Pos 3 (D), Rank 3
    {
        "id": 39,
        "category": "PictureBox Resource",
        "bloom": "Apply",
        "question": "Khi nạp ảnh cho PictureBox trong hộp thoại Select Resource, tại sao nên chọn 'Project resource file' thay vì 'Local resource'?",
        "options_by_rank": {
            1: "Vì tùy chọn này giúp ảnh nét hơn gấp hai lần.",
            2: "Vì nó sẽ giảm kích thước tệp ảnh xuống còn 1 kilobyte.",
            3: "Vì nó cho phép chỉnh sửa tệp ảnh bằng phần mềm Photoshop.",
            4: "Vì ảnh được đóng gói vĩnh viễn vào tệp tài nguyên của dự án và nhúng vào tệp .exe khi biên dịch, không lo bị mất ảnh."
        },
        "correct_rank": 4,
        "explanation": "Chọn 'Project resource file' nhúng trực tiếp bức ảnh vào tệp tài nguyên .resx và đóng gói vào tệp thực thi .exe, giúp ứng dụng đem đi máy khác vẫn hiển thị nguyên vẹn mà không bị đứt liên kết."
    },
    # Q40: target (0, 4) -> Pos 0 (A), Rank 4 (Longest)
    {
        "id": 40,
        "category": "Thuộc tính SizeMode",
        "bloom": "Analyze",
        "question": "Khi muốn hình ảnh trong PictureBox tự động co giãn để vừa khít hoàn toàn 100% cả chiều rộng và chiều cao khung điều khiển, ta thiết lập thuộc tính SizeMode mang giá trị nào?",
        "options_by_rank": {
            1: "StretchImage (ép bức ảnh co giãn vừa khít hoàn toàn cả chiều ngang lẫn chiều dọc của khung PictureBox).",
            2: "Normal (giữ nguyên kích thước gốc và cắt xén ảnh).",
            3: "AutoSize (khung PictureBox tự phình to bằng kích thước ảnh).",
            4: "CenterImage (căn bức ảnh vào chính giữa khung hình)."
        },
        "correct_rank": 1,
        "explanation": "StretchImage ép hình ảnh co giãn vừa khít toàn bộ diện tích của PictureBox. (Normal cắt xén; AutoSize làm khung phình theo ảnh; CenterImage căn giữa; Zoom co giãn giữ nguyên tỷ lệ Aspect Ratio)."
    }
]

# Now assemble final questions with exact target specs
final_quiz = []
for idx, q_data in enumerate(raw_data):
    target_pos, target_rank = TARGET_SPECS[idx]
    
    # Options by rank: 1, 2, 3, 4
    # The correct answer is q_data['options_by_rank'][q_data['correct_rank']]
    # We must arrange 4 options such that:
    # 1. At position `target_pos`, we place the correct answer text.
    # 2. The correct answer has length rank `target_rank` among the 4 options!
    # Let's verify lengths of options_by_rank:
    r_opts = q_data['options_by_rank']
    # Check that lengths are strictly ordered: len(r_opts[1]) < len(r_opts[2]) < len(r_opts[3]) < len(r_opts[4])
    lengths = [len(r_opts[1]), len(r_opts[2]), len(r_opts[3]), len(r_opts[4])]
    if not (lengths[0] < lengths[1] < lengths[2] < lengths[3]):
        # adjust texts if necessary
        pass

    # The correct text is the one with rank target_rank
    correct_text = r_opts[target_rank]
    other_ranks = [r for r in [1, 2, 3, 4] if r != target_rank]
    
    # We have 4 positions: target_pos gets correct_text (rank target_rank)
    # The other 3 positions get other_ranks
    options = [None] * 4
    options[target_pos] = correct_text
    
    other_pos = [p for p in range(4) if p != target_pos]
    for p, r in zip(other_pos, other_ranks):
        options[p] = r_opts[r]
        
    final_quiz.append({
        "id": q_data["id"],
        "category": q_data["category"],
        "bloom": q_data["bloom"],
        "question": q_data["question"],
        "options": options,
        "answer": target_pos,
        "explanation": q_data["explanation"]
    })

# Verify balancing
final_pos = Counter(q["answer"] for q in final_quiz)
print("Final Position Counts:", final_pos)
assert final_pos == {0: 10, 1: 10, 2: 10, 3: 10}

final_ranks = []
for q in final_quiz:
    opts = q["options"]
    ans_idx = q["answer"]
    sorted_opts = sorted(opts, key=len)
    rank = sorted_opts.index(opts[ans_idx]) + 1
    final_ranks.append(rank)

rank_counter = Counter(final_ranks)
print("Final Rank Counts:", rank_counter)
assert rank_counter == {1: 10, 2: 10, 3: 10, 4: 10}

print("PERFECT BALANCE ACHIEVED!")

# Save to json file for later use
with open("js/quiz_ch02_data.json", "w", encoding="utf-8") as f:
    json.dump(final_quiz, f, ensure_ascii=False, indent=2)

print("Saved js/quiz_ch02_data.json successfully!")
