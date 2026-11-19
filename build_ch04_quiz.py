# -*- coding: utf-8 -*-
"""
Build 40 perfectly balanced questions for Chapter 4: Introduction to Classes, Objects, Methods and strings.
Requirements:
- Exactly 10 questions with correct answer at Pos 0 (A), 10 at Pos 1 (B), 10 at Pos 2 (C), 10 at Pos 3 (D)
- Exactly 10 questions at Rank 1 (Shortest), 10 at Rank 2 (2nd shortest), 10 at Rank 3 (2nd longest), 10 at Rank 4 (Longest)
- High-quality pedagogical questions based on Deitel & Deitel Chapter 4 (p. 146-181)
"""

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

questions_def = [
    # Q1: (0, 1) -> Pos A (0), Rank 1 (Shortest)
    {
        "id": 1,
        "category": "Lớp và Đối tượng",
        "bloom": "Understand",
        "clo": "CLO 4.1",
        "question": "Trong lập trình hướng đối tượng C#, mối quan hệ giữa Lớp (Class) và Đối tượng (Object) được định nghĩa chuẩn xác như thế nào?",
        "explanation": "Mục 4.2 Deitel: Lớp đóng vai trò là bản thiết kế (blueprint/template), còn đối tượng là một thực thể sống (instance) cụ thể được sinh ra từ bản thiết kế đó trong bộ nhớ.",
        "correct": "Lớp là bản thiết kế, đối tượng là thực thể được tạo ra.",
        "shorter": [],
        "longer": [
            "Đối tượng là mã nguồn khai báo, còn lớp là dữ liệu thực thi khi chạy.",
            "Lớp chỉ chứa các biến dữ liệu, còn đối tượng chỉ chứa các phương thức xử lý.",
            "Lớp và đối tượng là hai khái niệm hoàn toàn tương đồng và có thể thay thế lẫn nhau."
        ]
    },
    # Q2: (1, 2) -> Pos B (1), Rank 2
    {
        "id": 2,
        "category": "Khởi tạo Đối tượng",
        "bloom": "Apply",
        "clo": "CLO 4.1",
        "question": "Toán tử nào trong C# được sử dụng để yêu cầu máy ảo CLR cấp phát bộ nhớ trên Heap và khởi tạo một đối tượng mới?",
        "explanation": "Mục 4.3.1 Deitel: Toán tử new cấp phát bộ nhớ cho một đối tượng trên Managed Heap và gọi hàm tạo constructor để khởi tạo đối tượng.",
        "correct": "Toán tử new để cấp phát bộ nhớ trên Managed Heap.",
        "shorter": [
            "Từ khóa this."
        ],
        "longer": [
            "Toán tử định kiểu typeof kết hợp với reflection của nền tảng .NET.",
            "Phương thức tĩnh Object.CreateInstance() định nghĩa trong không gian tên System."
        ]
    },
    # Q3: (2, 3) -> Pos C (2), Rank 3
    {
        "id": 3,
        "category": "Kiểu Dữ liệu",
        "bloom": "Understand",
        "clo": "CLO 4.1",
        "question": "Giá trị mặc định của một biến thể hiện thuộc Kiểu Tham chiếu (Reference Type) khi chưa được gán đối tượng là gì?",
        "explanation": "Mục 4.3.2 Deitel: Các biến kiểu tham chiếu chưa trỏ tới đối tượng nào sẽ tự động được khởi tạo giá trị đặc biệt là null.",
        "correct": "Giá trị null biểu thị biến chưa tham chiếu tới bất kỳ đối tượng nào.",
        "shorter": [
            "Số 0 nguyên.",
            "Chuỗi rỗng \"\"."
        ],
        "longer": [
            "Giá trị không xác định chứa dữ liệu rác ngẫu nhiên còn sót lại trong ngăn xếp Stack."
        ]
    },
    # Q4: (3, 4) -> Pos D (3), Rank 4 (Longest)
    {
        "id": 4,
        "category": "Quản lý Bộ nhớ",
        "bloom": "Analyze",
        "clo": "CLO 4.1",
        "question": "Điều gì sẽ xảy ra nếu một chương trình cố gắng gọi phương thức thông qua một biến tham chiếu đang mang giá trị null?",
        "explanation": "Mục 4.3.2 Deitel: Cố gắng sử dụng biến null để truy cập thành viên của đối tượng sẽ gây ra lỗi nghiêm trọng lúc chạy NullReferenceException.",
        "correct": "Chương trình sẽ ngay lập tức ném ra ngoại lệ nghiêm trọng lúc thực thi mang tên NullReferenceException.",
        "shorter": [
            "Trình biên dịch báo lỗi CS0103.",
            "Phương thức sẽ tự động bỏ qua.",
            "Hệ điều hành cấp phát đối tượng rỗng."
        ],
        "longer": []
    },
    # Q5: (1, 1) -> Pos B (1), Rank 1 (Shortest)
    {
        "id": 5,
        "category": "Nguyên lý Đóng gói",
        "bloom": "Understand",
        "clo": "CLO 4.2",
        "question": "Từ khóa nào được sử dụng để khai báo biến thể hiện nhằm thực hiện nguyên lý Ẩn giấu Dữ liệu (Data Hiding)?",
        "explanation": "Mục 4.4 Deitel: Từ khóa private hạn chế quyền truy cập, chỉ cho phép các phương thức bên trong chính lớp đó thao tác trực tiếp với biến thể hiện.",
        "correct": "Từ khóa private.",
        "shorter": [],
        "longer": [
            "Từ khóa public cho phép toàn cục truy cập.",
            "Từ khóa static chia sẻ vùng nhớ chung cho mọi thể hiện.",
            "Từ khóa protected cho phép truy cập từ các lớp cùng gói thư viện."
        ]
    },
    # Q6: (2, 2) -> Pos C (2), Rank 2
    {
        "id": 6,
        "category": "Phương thức",
        "bloom": "Remember",
        "clo": "CLO 4.2",
        "question": "Từ khóa void xuất hiện trong phần đầu của một khai báo phương thức biểu thị điều gì?",
        "explanation": "Mục 4.4.1 Deitel: Kiểu trả về void chỉ ra rằng phương thức chỉ thực hiện một nhiệm vụ cụ thể và không trả về bất kỳ dữ liệu nào khi hoàn tất.",
        "correct": "Phương thức không trả về dữ liệu cho nơi gọi.",
        "shorter": [
            "Phương thức là hàm ảo."
        ],
        "longer": [
            "Phương thức bắt buộc phải chứa ít nhất một câu lệnh return giá trị nguyên 0.",
            "Phương thức không thể tiếp nhận bất kỳ tham số nào trong danh sách ngoặc đơn."
        ]
    },
    # Q7: (3, 3) -> Pos D (3), Rank 3
    {
        "id": 7,
        "category": "Biến & Vùng nhớ",
        "bloom": "Understand",
        "clo": "CLO 4.2",
        "question": "Điểm khác biệt căn bản giữa Biến thể hiện (Instance Variable) và Biến cục bộ (Local Variable) là gì?",
        "explanation": "Mục 4.4.3 Deitel: Biến thể hiện tồn tại cùng vòng đời của đối tượng trên Heap và có giá trị mặc định; biến cục bộ nằm trên Stack và mất đi khi hàm kết thúc.",
        "correct": "Biến thể hiện tồn tại theo đối tượng trên Heap, còn biến cục bộ mất khi hàm kết thúc.",
        "shorter": [
            "Biến thể hiện luôn là public.",
            "Biến cục bộ dùng cho mọi lớp."
        ],
        "longer": [
            "Biến cục bộ luôn được C# tự động khởi tạo giá trị mặc định là 0 hoặc null ngay khi khai báo."
        ]
    },
    # Q8: (0, 4) -> Pos A (0), Rank 4 (Longest)
    {
        "id": 8,
        "category": "Mô hình Hóa UML",
        "bloom": "Understand",
        "clo": "CLO 4.2",
        "question": "Trong Sơ đồ Lớp UML (UML Class Diagram), ký hiệu dấu trừ (-) và dấu cộng (+) trước tên thành viên có ý nghĩa gì?",
        "explanation": "Mục 4.4.4 Deitel: Ký hiệu dấu trừ (-) biểu thị phạm vi truy cập private, dấu cộng (+) biểu thị phạm vi truy cập công khai public.",
        "correct": "Dấu trừ (-) biểu thị phạm vi truy cập private, còn dấu cộng (+) biểu thị phạm vi truy cập công khai public.",
        "shorter": [
            "Dấu trừ là biến, dấu cộng là hàm.",
            "Dấu trừ là xóa, dấu cộng là thêm mới.",
            "Dấu trừ là số âm, dấu cộng là số dương."
        ],
        "longer": []
    },
    # Q9: (2, 1) -> Pos C (2), Rank 1 (Shortest)
    {
        "id": 9,
        "category": "Thuộc tính C#",
        "bloom": "Remember",
        "clo": "CLO 4.3",
        "question": "Hai khối mã lệnh thành phần (accessors) cấu thành nên một Thuộc tính (Property) trong C# là gì?",
        "explanation": "Mục 4.6 Deitel: Một thuộc tính trong C# bao gồm hai bộ truy cập get (để đọc dữ liệu) và set (để sửa đổi dữ liệu).",
        "correct": "Bộ truy cập get và set.",
        "shorter": [],
        "longer": [
            "Phương thức read và phương thức write.",
            "Cặp từ khóa input nhận dữ liệu và output xuất giá trị.",
            "Hai khối lệnh try xử lý ngoại lệ và catch bắt giữ lỗi lúc chạy."
        ]
    },
    # Q10: (3, 2) -> Pos D (3), Rank 2
    {
        "id": 10,
        "category": "Thuộc tính C#",
        "bloom": "Understand",
        "clo": "CLO 4.3",
        "question": "Từ khóa ngữ cảnh nào trong bộ truy cập set đại diện ngầm định cho giá trị được gán từ vế phải của biểu thức?",
        "explanation": "Mục 4.6.2 Deitel: Từ khóa ngữ cảnh value trong bộ truy cập set đại diện cho giá trị mới được cung cấp bởi câu lệnh gán phía client.",
        "correct": "Từ khóa ngữ cảnh mang tên value.",
        "shorter": [
            "Từ khóa this."
        ],
        "longer": [
            "Từ khóa tham số mặc định args truyền từ hàm Main.",
            "Biến cục bộ inputData do người lập trình bắt buộc phải tự khai báo."
        ]
    },

    # Q11: (0, 3) -> Pos A (0), Rank 3
    {
        "id": 11,
        "category": "UML Stereotype",
        "bloom": "Remember",
        "clo": "CLO 4.3",
        "question": "Trong Sơ đồ Lớp UML, thuộc tính của C# được phân biệt với các phương thức thông thường bằng ký hiệu đặc biệt nào?",
        "explanation": "Mục 4.6.3 Deitel: Thuộc tính trong UML được biểu diễn kèm theo một stereotype đặt trong cặp ngoặc kép Pháp: «property».",
        "correct": "Stereotype «property» đặt bên cạnh tên thuộc tính trong ngăn thứ hai hoặc ba.",
        "shorter": [
            "Ký tự hoa thị *.",
            "Biểu tượng mũi tên ->."
        ],
        "longer": [
            "Đường viền nét đứt màu đỏ bao quanh toàn bộ hình chữ nhật của lớp đối tượng trong sơ đồ."
        ]
    },
    # Q12: (1, 4) -> Pos B (1), Rank 4 (Longest)
    {
        "id": 12,
        "category": "Thuộc tính Tự động",
        "bloom": "Apply",
        "clo": "CLO 4.3",
        "question": "Ưu điểm nổi bật nhất của cú pháp Thuộc tính Tự động (Auto-Implemented Properties) như public string Name { get; set; } là gì?",
        "explanation": "Mục 4.7 Deitel: Trình biên dịch C# tự động tạo biến backing field ẩn và sinh code get/set, giúp mã nguồn cực kỳ ngắn gọn và sạch sẽ.",
        "correct": "Trình biên dịch tự động sinh ra biến backing field ẩn và mã lệnh get/set, giúp mã nguồn ngắn gọn và tăng tốc độ phát triển.",
        "shorter": [
            "Chạy nhanh hơn biến bình thường.",
            "Tự động đồng bộ hóa đa luồng an toàn.",
            "Không bao giờ bị lỗi NullReferenceException."
        ],
        "longer": []
    },
    # Q13: (3, 1) -> Pos D (3), Rank 1 (Shortest)
    {
        "id": 13,
        "category": "Hàm tạo Constructor",
        "bloom": "Remember",
        "clo": "CLO 4.4",
        "question": "Tên của một Hàm tạo (Constructor) trong C# bắt buộc phải tuân theo quy tắc nào sau đây?",
        "explanation": "Mục 4.8.1 Deitel: Hàm tạo constructor bắt buộc phải có tên hoàn toàn trùng khớp với tên của lớp chứa nó.",
        "correct": "Trùng hoàn toàn với tên của Lớp.",
        "shorter": [],
        "longer": [
            "Bắt đầu bằng từ khóa Create kèm theo tên của lớp.",
            "Bắt buộc phải mang tên là Init hoặc InitializeComponent.",
            "Có thể đặt bất kỳ tên hợp lệ nào miễn là có chứa từ khóa static."
        ]
    },
    # Q14: (0, 2) -> Pos A (0), Rank 2
    {
        "id": 14,
        "category": "Cú pháp Constructor",
        "bloom": "Understand",
        "clo": "CLO 4.4",
        "question": "Điểm khác biệt quan trọng nhất về cú pháp giữa một Hàm tạo (Constructor) và một Phương thức thông thường là gì?",
        "explanation": "Mục 4.8.1 Deitel: Khác với phương thức, constructor tuyệt đối không thể chỉ định kiểu dữ liệu trả về, kể cả từ khóa void cũng không được phép có.",
        "correct": "Hàm tạo tuyệt đối không có kiểu dữ liệu trả về.",
        "shorter": [
            "Hàm tạo không có tham số."
        ],
        "longer": [
            "Hàm tạo bắt buộc phải có từ khóa static đi kèm ở phần đầu khai báo.",
            "Hàm tạo luôn phải trả về một đối tượng kiểu Object cho máy ảo CLR."
        ]
    },
    # Q15: (1, 3) -> Pos B (1), Rank 3
    {
        "id": 15,
        "category": "Default Constructor",
        "bloom": "Understand",
        "clo": "CLO 4.4",
        "question": "Khi nào thì trình biên dịch C# sẽ KHÔNG tự động cung cấp Hàm tạo mặc định không tham số (Default Constructor) cho một lớp?",
        "explanation": "Mục 4.8.2 Deitel: Một khi bạn đã tự tay định nghĩa bất kỳ một constructor nào (kể cả constructor có tham số), trình biên dịch sẽ không tạo default constructor nữa.",
        "correct": "Khi lớp đã được người lập trình khai báo ít nhất một hàm tạo tùy biến.",
        "shorter": [
            "Khi lớp chứa biến private.",
            "Khi lớp kế thừa từ System."
        ],
        "longer": [
            "Khi lớp được lưu trữ trong một tệp mã nguồn độc lập có phần mở rộng là .cs trong Visual Studio."
        ]
    },
    # Q16: (2, 4) -> Pos C (2), Rank 4 (Longest)
    {
        "id": 16,
        "category": "Khởi tạo Đa đối tượng",
        "bloom": "Apply",
        "clo": "CLO 4.4",
        "question": "Khi đoạn mã Account acc1 = new Account(\"Jane\"); Account acc2 = new Account(\"John\"); thực thi, vùng nhớ được tổ chức như thế nào?",
        "explanation": "Mục 4.8.2 Deitel: Hai đối tượng Account độc lập được tạo trên Heap, mỗi đối tượng có vùng nhớ riêng cho thuộc tính Name của mình.",
        "correct": "Hai đối tượng độc lập được tạo ra trên Managed Heap, mỗi đối tượng sở hữu vùng nhớ riêng biệt cho thuộc tính Name.",
        "shorter": [
            "Chỉ có một vùng nhớ duy nhất.",
            "Đối tượng acc2 sẽ ghi đè acc1.",
            "Hai biến dùng chung một thuộc tính Name."
        ],
        "longer": []
    },
    # Q17: (0, 1) -> Pos A (0), Rank 1 (Shortest)
    {
        "id": 17,
        "category": "Số học Tài chính",
        "bloom": "Understand",
        "clo": "CLO 4.5",
        "question": "Tại sao trong các ứng dụng tài chính ngân hàng, lập trình viên không nên sử dụng kiểu double hoặc float để lưu trữ tiền tệ?",
        "explanation": "Mục 4.9 Deitel: float và double biểu diễn số thực dưới dạng nhị phân, dẫn đến sai số làm tròn thập phân không thể chấp nhận được trong kế toán tài chính.",
        "correct": "Vì xảy ra sai số làm tròn nhị phân.",
        "shorter": [],
        "longer": [
            "Vì kiểu double chiếm quá nhiều dung lượng bộ nhớ RAM.",
            "Vì Visual Studio không hỗ trợ toán tử cộng trừ cho kiểu double.",
            "Vì kiểu float không thể chuyển đổi hiển thị thành chuỗi ký tự trên Console."
        ]
    },
    # Q18: (1, 2) -> Pos B (1), Rank 2
    {
        "id": 18,
        "category": "Kiểu Dữ liệu decimal",
        "bloom": "Remember",
        "clo": "CLO 4.5",
        "question": "Kiểu dữ liệu decimal trong C# có kích thước bộ nhớ bao nhiêu bits và mang lại độ chính xác bao nhiêu chữ số có nghĩa?",
        "explanation": "Mục 4.9 Deitel: Kiểu decimal sử dụng 128 bits (16 bytes) và cho độ chính xác cực cao từ 28 đến 29 chữ số có nghĩa thập phân.",
        "correct": "Kích thước 128 bits, độ chính xác 28-29 chữ số có nghĩa.",
        "shorter": [
            "64 bits, chính xác 15 chữ số."
        ],
        "longer": [
            "Kích thước 32 bits, độ chính xác tối đa 7 chữ số phần thập phân.",
            "Kích thước 256 bits, độ chính xác vô hạn không giới hạn phần nguyên."
        ]
    },
    # Q19: (2, 3) -> Pos C (2), Rank 3
    {
        "id": 19,
        "category": "Cú pháp decimal",
        "bloom": "Apply",
        "clo": "CLO 4.5",
        "question": "Khi gán một hằng số số thực cho biến kiểu decimal trong mã nguồn C#, ký tự hậu tố nào bắt buộc phải gắn liền sau con số?",
        "explanation": "Mục 4.9.1 Deitel: Hằng số kiểu decimal bắt buộc phải có hậu tố m hoặc M (viết tắt của Monetary), nếu không C# sẽ coi là kiểu double.",
        "correct": "Hậu tố m hoặc M biểu thị giá trị thuộc kiểu số thực decimal tiền tệ.",
        "shorter": [
            "Hậu tố d hoặc D.",
            "Hậu tố f hoặc F."
        ],
        "longer": [
            "Hậu tố c hoặc C tương ứng với ký tự định dạng Currency trong chuỗi xuất."
        ]
    },
    # Q20: (3, 4) -> Pos D (3), Rank 4 (Longest)
    {
        "id": 20,
        "category": "Data Validation",
        "bloom": "Analyze",
        "clo": "CLO 4.5",
        "question": "Trong phương thức Deposit(decimal depositAmount) của lớp Account, tại sao cần câu lệnh kiểm tra if (depositAmount > 0.0m)?",
        "explanation": "Mục 4.9.1 Deitel: Cơ chế Data Validation đảm bảo rằng chỉ có số tiền gửi dương mới được cộng vào số dư, ngăn chặn việc làm sai lệch tài khoản.",
        "correct": "Để đảm bảo tính toàn vẹn dữ liệu, ngăn chặn việc nạp số tiền âm hoặc bằng 0 làm thay đổi số dư bất hợp lệ.",
        "shorter": [
            "Để tránh lỗi tràn bộ nhớ.",
            "Để kích hoạt máy ảo CLR.",
            "Để in thông báo nạp thành công."
        ],
        "longer": []
    },

    # Q21: (1, 1) -> Pos B (1), Rank 1 (Shortest)
    {
        "id": 21,
        "category": "Bảo vệ Thuộc tính",
        "bloom": "Understand",
        "clo": "CLO 4.3",
        "question": "Kỹ thuật nào giúp thuộc tính Balance cho phép bên ngoài đọc tự do nhưng chỉ nội bộ lớp Account mới được quyền sửa đổi?",
        "explanation": "Mục 4.9.1 Deitel: Khai báo public decimal Balance { get; private set; } hạn chế quyền ghi chỉ dành riêng cho các thành viên bên trong lớp.",
        "correct": "Khai báo private set.",
        "shorter": [],
        "longer": [
            "Xóa bỏ hoàn toàn bộ truy cập get khỏi thuộc tính.",
            "Thêm từ khóa readonly vào trước khai báo thuộc tính public.",
            "Chuyển toàn bộ lớp Account thành lớp niêm phong với từ khóa sealed."
        ]
    },
    # Q22: (2, 2) -> Pos C (2), Rank 2
    {
        "id": 22,
        "category": "Định dạng Chuỗi",
        "bloom": "Apply",
        "clo": "CLO 4.5",
        "question": "Trong biểu thức nội suy chuỗi $\"{account.Balance:C}\", ký hiệu định dạng :C có ý nghĩa gì?",
        "explanation": "Mục 4.9.2 Deitel: Ký tự định dạng C (Currency) hiển thị số theo định dạng tiền tệ của hệ thống, bao gồm ký hiệu tiền tệ và 2 chữ số thập phân.",
        "correct": "Định dạng giá trị số theo tiền tệ chuẩn quốc tế.",
        "shorter": [
            "Chuyển số thành ký tự char."
        ],
        "longer": [
            "Chuyển đổi số thực sang hệ thống cơ số 16 hexa không dấu.",
            "Căn lề chuỗi văn bản vào chính giữa màn hình cửa sổ console."
        ]
    },
    # Q23: (3, 3) -> Pos D (3), Rank 3
    {
        "id": 23,
        "category": "Ký tự Định dạng",
        "bloom": "Remember",
        "clo": "CLO 4.5",
        "question": "Ký tự định dạng nào trong .NET được dùng để hiển thị số nguyên thập phân và có thể chèn thêm các số 0 ở đầu (ví dụ: {x:D5})?",
        "explanation": "Mục 4.9.2 (Hình 4.13) Deitel: Ký tự D (Decimal) định dạng số nguyên thập phân và có thể đi kèm số lượng chữ số tối thiểu.",
        "correct": "Ký tự định dạng D dùng cho số nguyên và tự chèn thêm số 0 ở đầu.",
        "shorter": [
            "Ký tự định dạng F.",
            "Ký tự định dạng N."
        ],
        "longer": [
            "Ký tự định dạng P tự động nhân giá trị với 100 và thêm ký hiệu phần trăm ở cuối."
        ]
    },
    # Q24: (0, 4) -> Pos A (0), Rank 4 (Longest)
    {
        "id": 24,
        "category": "Ký tự Định dạng",
        "bloom": "Remember",
        "clo": "CLO 4.5",
        "question": "Ký tự định dạng nào trong .NET tự động nhân giá trị số với 100 và hiển thị kèm theo ký hiệu phần trăm (%) ở phía sau?",
        "explanation": "Mục 4.9.2 (Hình 4.13) Deitel: Ký tự P (Percentage) định dạng phần trăm, tự động nhân số với 100 và thêm ký hiệu %.",
        "correct": "Ký tự định dạng P (Percentage) tự động nhân số với 100 và thêm ký hiệu phần trăm ở cuối.",
        "shorter": [
            "Ký tự định dạng C.",
            "Ký tự định dạng E.",
            "Ký tự định dạng G."
        ],
        "longer": []
    },
    # Q25: (2, 1) -> Pos C (2), Rank 1 (Shortest)
    {
        "id": 25,
        "category": "Nhập xuất Dữ liệu",
        "bloom": "Apply",
        "clo": "CLO 4.5",
        "question": "Phương thức nào của kiểu decimal được dùng để chuyển đổi một chuỗi văn bản nhập từ bàn phím thành giá trị số decimal?",
        "explanation": "Mục 4.9.2 Deitel: Phương thức tĩnh decimal.Parse() tiếp nhận chuỗi ký tự và chuyển đổi thành giá trị kiểu decimal.",
        "correct": "Phương thức decimal.Parse().",
        "shorter": [],
        "longer": [
            "Phương thức ToString() của lớp Object.",
            "Toán tử ép kiểu ngầm định (decimal)Console.ReadLine().",
            "Hàm toàn cục ConvertToMoney() trong không gian tên System."
        ]
    },
    # Q26: (3, 2) -> Pos D (3), Rank 2
    {
        "id": 26,
        "category": "Cạm bẫy OOP",
        "bloom": "Analyze",
        "clo": "CLO 4.3",
        "question": "Điều gì sẽ xảy ra nếu lập trình viên viết: public string Name { get { return Name; } }?",
        "explanation": "Mục 4.6.2 Deitel: Thuộc tính tự gọi chính nó trong bộ get sẽ tạo ra vòng đệ quy vô hạn dẫn tới lỗi tràn ngăn xếp StackOverflowException.",
        "correct": "Gây đệ quy vô hạn và làm sập ứng dụng với lỗi StackOverflowException.",
        "shorter": [
            "Chương trình chạy bình thường."
        ],
        "longer": [
            "Trình biên dịch C# tự động phát hiện và chuyển thành mã thuộc tính tự động.",
            "Hệ thống sẽ tự động gán giá trị chuỗi rỗng cho thuộc tính Name ngay lập tức."
        ]
    },
    # Q27: (0, 3) -> Pos A (0), Rank 3
    {
        "id": 27,
        "category": "Cạm bẫy OOP",
        "bloom": "Analyze",
        "clo": "CLO 4.4",
        "question": "Trong hàm tạo: public Account(string name) { string Name = name; }, lỗi lập trình nghiêm trọng nào đã xảy ra?",
        "explanation": "Lập trình viên khai báo thêm từ khóa string trước Name, tạo thành biến cục bộ che khuất thuộc tính của lớp; giá trị không được lưu vào đối tượng.",
        "correct": "Khai báo lại kiểu dữ liệu tạo biến cục bộ che khuất thuộc tính của lớp.",
        "shorter": [
            "Lỗi thiếu từ khóa static.",
            "Lỗi sai kiểu dữ liệu số."
        ],
        "longer": [
            "Trình biên dịch C# bắt buộc hàm tạo phải luôn luôn có câu lệnh return một giá trị boolean."
        ]
    },
    # Q28: (1, 4) -> Pos B (1), Rank 4 (Longest)
    {
        "id": 28,
        "category": "Tái cấu trúc Mã nguồn",
        "bloom": "Apply",
        "clo": "CLO 4.5",
        "question": "Mục đích chính của việc thiết kế phương thức dùng chung static void DisplayAccount(Account accountToDisplay) là gì?",
        "explanation": "Exercise 4.13 Deitel: Áp dụng nguyên lý DRY (Don't Repeat Yourself) để loại bỏ mã in thông tin tài khoản lặp đi lặp lại nhiều lần trong Main.",
        "correct": "Áp dụng nguyên lý DRY để loại bỏ sự lặp lại mã nguồn, giúp code gọn gàng, dễ bảo trì và tập trung nơi thay đổi định dạng xuất.",
        "shorter": [
            "Để tăng tốc độ CPU thực thi.",
            "Để mã hóa bảo mật số dư.",
            "Để đối tượng tự động giải phóng."
        ],
        "longer": []
    },
    # Q29: (3, 1) -> Pos D (3), Rank 1 (Shortest)
    {
        "id": 29,
        "category": "Nghiệp vụ Ngân hàng",
        "bloom": "Apply",
        "clo": "CLO 4.5",
        "question": "Trong Bài tập 4.11, điều kiện kiểm tra nào bắt buộc phải có trước khi thực hiện trừ tiền trong phương thức Withdraw(decimal amount)?",
        "explanation": "Exercise 4.11 Deitel: Số tiền rút phải không vượt quá số dư (amount <= Balance) để tránh tình trạng thấu chi tài khoản.",
        "correct": "Số tiền rút phải nhỏ hơn hoặc bằng số dư.",
        "shorter": [],
        "longer": [
            "Tài khoản phải có số tiền gửi ban đầu là 100 đô la.",
            "Người dùng phải nhập mật khẩu mã PIN từ bàn phím console.",
            "Tên chủ tài khoản ngân hàng không được phép trùng với từ khóa C#."
        ]
    },
    # Q30: (0, 2) -> Pos A (0), Rank 2
    {
        "id": 30,
        "category": "Nghiệp vụ Ngân hàng",
        "bloom": "Understand",
        "clo": "CLO 4.5",
        "question": "Theo yêu cầu Bài tập 4.11, nếu số tiền rút vượt quá số dư hiện có, phương thức Withdraw cần thực hiện hành vi gì?",
        "explanation": "Exercise 4.11 Deitel: Nếu số tiền rút vượt quá số dư, số dư không thay đổi và phương thức in thông báo 'Withdrawal amount exceeded account balance.'",
        "correct": "Giữ nguyên số dư và in thông báo số tiền rút vượt quá số dư.",
        "shorter": [
            "Cho phép rút âm số dư."
        ],
        "longer": [
            "Tự động đóng băng tài khoản và thoát khỏi ứng dụng console ngay tức thì.",
            "Chuyển toàn bộ số tiền còn lại sang tài khoản phụ của người dùng khác."
        ]
    },

    # Q31: (1, 3) -> Pos B (1), Rank 3
    {
        "id": 31,
        "category": "Định dạng Cố định",
        "bloom": "Remember",
        "clo": "CLO 4.5",
        "question": "Ký tự định dạng F trong chuỗi $\"{x:F3}\" sẽ định dạng số thực theo cách nào?",
        "explanation": "Hình 4.13 Deitel: Ký tự định dạng F (Fixed-point) hiển thị số thực với số chữ số phần thập phân cố định theo sau (ở đây là đúng 3 chữ số).",
        "correct": "Hiển thị số thực với đúng 3 chữ số cố định ở phần thập phân sau dấu phẩy.",
        "shorter": [
            "Làm tròn thành số nguyên.",
            "Chuyển số sang dạng phân số."
        ],
        "longer": [
            "Tự động chuyển đổi số thực thành định dạng biểu diễn số mũ khoa học có ký tự E."
        ]
    },
    # Q32: (2, 4) -> Pos C (2), Rank 4 (Longest)
    {
        "id": 32,
        "category": "Giá trị Mặc định",
        "bloom": "Understand",
        "clo": "CLO 4.1",
        "question": "Giá trị mặc định ban đầu của các biến thể hiện kiểu bool, int và decimal trong một đối tượng C# khi mới khởi tạo là gì?",
        "explanation": "Mục 4.3.2 & 4.9.1 Deitel: Biến kiểu bool có mặc định là false, biến kiểu số nguyên int là 0, và biến decimal là 0.0m.",
        "correct": "Kiểu bool có giá trị mặc định là false, kiểu int là 0, và kiểu decimal là 0.0m.",
        "shorter": [
            "Tất cả đều mang giá trị null.",
            "Tất cả đều có giá trị bằng 1.",
            "Giá trị rác ngẫu nhiên trong bộ nhớ."
        ],
        "longer": []
    },
    # Q33: (0, 1) -> Pos A (0), Rank 1 (Shortest)
    {
        "id": 33,
        "category": "Khai báo Lớp",
        "bloom": "Remember",
        "clo": "CLO 4.2",
        "question": "Từ khóa nào trong C# xác định rằng một lớp có thể được truy cập và khởi tạo bởi bất kỳ lớp nào khác trong dự án?",
        "explanation": "Mục 4.3 Deitel: Công cụ sửa đổi quyền truy cập public cho phép lớp hoặc thành viên được truy cập từ mọi mã nguồn khác.",
        "correct": "Từ khóa public.",
        "shorter": [],
        "longer": [
            "Từ khóa internal giới hạn trong thư viện dll.",
            "Từ khóa private chỉ cho phép truy cập cục bộ.",
            "Từ khóa abstract yêu cầu phải kế thừa trước khi tạo."
        ]
    },
    # Q34: (1, 2) -> Pos B (1), Rank 2
    {
        "id": 34,
        "category": "Cấu trúc Dự án",
        "bloom": "Understand",
        "clo": "CLO 4.2",
        "question": "Quy chuẩn tổ chức tệp tin chuyên nghiệp của Microsoft đối với các lớp trong dự án C# là gì?",
        "explanation": "Mục 4.3.3 Deitel: Mỗi lớp nên được lưu trữ trong một tệp mã nguồn .cs riêng biệt có tên trùng khớp với tên của lớp.",
        "correct": "Mỗi lớp được lưu trong một tệp .cs riêng trùng tên với lớp.",
        "shorter": [
            "Gom mọi lớp vào Program.cs."
        ],
        "longer": [
            "Tất cả các lớp phải được biên dịch sẵn thành các tệp văn bản .txt phụ trợ.",
            "Mỗi phương thức của lớp phải được đặt ở một tệp tin mã nguồn hoàn toàn tách biệt."
        ]
    },
    # Q35: (2, 3) -> Pos C (2), Rank 3
    {
        "id": 35,
        "category": "Kiểu Tham chiếu",
        "bloom": "Understand",
        "clo": "CLO 4.1",
        "question": "Trong C#, mảng (arrays) và chuỗi ký tự (strings) thuộc nhóm kiểu dữ liệu nào sau đây?",
        "explanation": "Mục 4.3.2 Deitel: Cả string và array đều là Kiểu Tham chiếu (Reference Types), dữ liệu thực sự nằm trên Managed Heap.",
        "correct": "Kiểu Tham chiếu (Reference Types) có dữ liệu lưu trên Managed Heap.",
        "shorter": [
            "Kiểu Giá trị (Value Types).",
            "Kiểu Con trỏ không an toàn."
        ],
        "longer": [
            "Kiểu Cấu trúc nguyên thủy struct được cấp phát trực tiếp và cố định trên ngăn xếp Stack."
        ]
    },
    # Q36: (3, 4) -> Pos D (3), Rank 4 (Longest)
    {
        "id": 36,
        "category": "Hàm tạo Constructor",
        "bloom": "Understand",
        "clo": "CLO 4.4",
        "question": "Tại sao trong sơ đồ lớp UML, Hàm tạo (Constructor) không bao giờ có kiểu dữ liệu trả về sau dấu hai chấm?",
        "explanation": "Mục 4.8.2 Deitel: Vì trong cả UML và C#, constructor không trả về bất kỳ giá trị nào, mục đích duy nhất của nó là khởi tạo đối tượng.",
        "correct": "Vì theo chuẩn UML và cú pháp ngôn ngữ C#, hàm tạo không phải là phương thức thông thường và không bao giờ có kiểu trả về.",
        "shorter": [
            "Vì hàm tạo luôn trả về void.",
            "Do sơ đồ UML thiếu không gian vẽ.",
            "Vì hàm tạo tự động trả về kiểu int."
        ],
        "longer": []
    },
    # Q37: (1, 1) -> Pos B (1), Rank 1 (Shortest)
    {
        "id": 37,
        "category": "Biến Thể hiện",
        "bloom": "Remember",
        "clo": "CLO 4.2",
        "question": "Một tên gọi kỹ thuật chuẩn khác thường được dùng để chỉ Biến thể hiện (Instance Variable) trong C# là gì?",
        "explanation": "Mục 4.4 Deitel: Biến thể hiện thường được gọi là Trường (Field) của lớp.",
        "correct": "Trường dữ liệu (Field).",
        "shorter": [],
        "longer": [
            "Hằng số toàn cục (Global Constant).",
            "Biến môi trường hệ điều hành (Environment Variable).",
            "Phương thức thực thi nghiệp vụ (Business Logic Operation)."
        ]
    },
    # Q38: (2, 2) -> Pos C (2), Rank 2
    {
        "id": 38,
        "category": "Đóng gói & Hướng đối tượng",
        "bloom": "Understand",
        "clo": "CLO 4.2",
        "question": "Lợi ích then chốt của việc che giấu cấu trúc dữ liệu nội bộ (Information Hiding) thông qua Properties là gì?",
        "explanation": "Mục 4.4 & 4.6 Deitel: Cho phép thay đổi cấu trúc dữ liệu bên trong lớp mà không làm ảnh hưởng hay phá vỡ mã nguồn của các lớp bên ngoài (Loose Coupling).",
        "correct": "Có thể sửa đổi cấu trúc bên trong lớp mà không làm hỏng mã nguồn bên ngoài.",
        "shorter": [
            "Giảm một nửa dung lượng RAM."
        ],
        "longer": [
            "Làm cho ứng dụng tự động chạy song song trên tất cả các nhân của bộ vi xử lý CPU.",
            "Ngăn chặn hoàn toàn việc người dùng biên dịch ngược tệp tin thực thi .exe của dự án."
        ]
    },
    # Q39: (3, 3) -> Pos D (3), Rank 3
    {
        "id": 39,
        "category": "Bài tập HeartRates",
        "bloom": "Apply",
        "clo": "CLO 4.5",
        "question": "Trong Bài tập Y tế Số 4.14 (HeartRates), công thức của Hiệp hội Tim mạch Hoa Kỳ (AHA) tính nhịp tim tối đa theo số tuổi là gì?",
        "explanation": "Exercise 4.14 Deitel: Nhịp tim tối đa (Maximum Heart Rate) tính bằng 220 trừ đi số tuổi của người đó (220 - age).",
        "correct": "Nhịp tim tối đa được tính bằng 220 trừ đi số tuổi của một người (220 - age).",
        "shorter": [
            "Lấy 100 cộng với số tuổi.",
            "Nhân số tuổi với 2.5 lần."
        ],
        "longer": [
            "Lấy chỉ số khối cơ thể BMI nhân với hệ số vận động thể chất chuẩn y tế là 1.85."
        ]
    },
    # Q40: (0, 4) -> Pos A (0), Rank 4 (Longest)
    {
        "id": 40,
        "category": "Tổng kết Chương 4",
        "bloom": "Understand",
        "clo": "CLO 4.1 - 4.5",
        "question": "Phát biểu nào sau đây tổng kết chính xác nhất các nguyên lý lập trình hướng đối tượng nền tảng đã học trong Chương 4?",
        "explanation": "Chương 4 Deitel: Tổng hợp đầy đủ đóng gói dữ liệu bằng private, giao tiếp qua Property get/set, khởi tạo bằng constructor và độ chính xác decimal.",
        "correct": "Đóng gói dữ liệu với biến private, kiểm soát truy cập bằng thuộc tính get/set, khởi tạo trạng thái hợp lệ bằng constructor và tính toán tiền tệ chính xác với decimal.",
        "shorter": [
            "Tất cả các biến phải là public.",
            "Lập trình hướng đối tượng không cần lớp.",
            "Toán tử new chỉ dùng cho các biến int."
        ],
        "longer": []
    }
]

# Generate 40 questions with exact TARGET_SPECS
quiz_data = []

pos_counter = Counter()
rank_counter = Counter()

for idx, q_def in enumerate(questions_def):
    target_pos, target_rank = TARGET_SPECS[idx]
    
    correct_text = q_def["correct"]
    shorter_list = list(q_def["shorter"])
    longer_list = list(q_def["longer"])
    
    # We need 3 distractors:
    # target_rank = 1 -> correct is shortest -> shorter: 0, longer: 3
    # target_rank = 2 -> correct is 2nd shortest -> shorter: 1, longer: 2
    # target_rank = 3 -> correct is 2nd longest -> shorter: 2, longer: 1
    # target_rank = 4 -> correct is longest -> shorter: 3, longer: 0
    assert len(shorter_list) == target_rank - 1, f"Q{idx+1} shorter count mismatch: expected {target_rank - 1}, got {len(shorter_list)}"
    assert len(longer_list) == 4 - target_rank, f"Q{idx+1} longer count mismatch: expected {4 - target_rank}, got {len(longer_list)}"
    
    # Ordered by length:
    all_by_length = shorter_list + [correct_text] + longer_list
    assert all_by_length[target_rank - 1] == correct_text
    
    # Distractors:
    distractors = shorter_list + longer_list
    
    # Assemble 4 options with correct_text at target_pos
    options = [None] * 4
    options[target_pos] = correct_text
    
    d_idx = 0
    for pos in range(4):
        if pos != target_pos:
            options[pos] = distractors[d_idx]
            d_idx += 1
            
    # Verify rank by string length
    sorted_opts = sorted(options, key=lambda s: len(s))
    actual_rank = sorted_opts.index(correct_text) + 1
    actual_pos = options.index(correct_text)
    
    assert actual_pos == target_pos, f"Q{idx+1} pos mismatch: expected {target_pos}, got {actual_pos}"
    assert actual_rank == target_rank, f"Q{idx+1} rank mismatch: expected {target_rank}, got {actual_rank}"
    
    pos_counter[actual_pos] += 1
    rank_counter[actual_rank] += 1
    
    quiz_data.append({
        "id": q_def["id"],
        "category": q_def["category"],
        "bloom": q_def["bloom"],
        "clo": q_def.get("clo", "CLO 4.1"),
        "question": q_def["question"],
        "options": options,
        "correct": actual_pos,
        "answer": actual_pos,
        "explanation": q_def["explanation"]
    })

print("Position distribution (0=A, 1=B, 2=C, 3=D):", dict(pos_counter))
print("Rank distribution (1=shortest, 4=longest):", dict(rank_counter))
assert pos_counter == {0: 10, 1: 10, 2: 10, 3: 10}
assert rank_counter == {1: 10, 2: 10, 3: 10, 4: 10}

out_file = r"js\quiz_ch04_snippet.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(quiz_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {out_file} with {len(quiz_data)} questions perfectly balanced!")
