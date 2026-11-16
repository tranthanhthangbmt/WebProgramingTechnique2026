# -*- coding: utf-8 -*-
"""
Build 40 perfectly balanced questions for Chapter 3: Introduction to C# App Programming.
Target requirements:
- Exactly 10 questions at Pos 0 (A), 10 at Pos 1 (B), 10 at Pos 2 (C), 10 at Pos 3 (D)
- Exactly 10 questions at Rank 1 (Shortest), 10 at Rank 2 (2nd shortest), 10 at Rank 3 (2nd longest), 10 at Rank 4 (Longest)
- High-quality pedagogy, accurate to Deitel & Deitel Chapter 3.
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
        "category": "Cấu trúc Ứng dụng Console",
        "bloom": "Remember",
        "question": "Điểm khởi nhập (Entry Point) duy nhất mà máy ảo .NET CLR kích hoạt khi chạy ứng dụng C# là gì?",
        "explanation": "Theo mục 3.2 giáo trình Deitel: Mọi ứng dụng C# đều bắt đầu thực thi từ phương thức Main. Phương thức này phải được khai báo với từ khóa static.",
        "correct": "Phương thức Main.",
        "shorter": [],
        "longer": [
            "Lớp cơ sở System.Object được nạp đầu tiên trong bộ nhớ.",
            "Phương thức khởi tạo constructor của lớp chứa giao diện đồ họa Form.",
            "Chỉ thị tiền xử lý using directive khai báo ở dòng đầu tiên của tệp mã nguồn."
        ]
    },
    # Q2: (1, 2) -> Pos B (1), Rank 2
    {
        "id": 2,
        "category": "Cú pháp & Chú thích",
        "bloom": "Understand",
        "question": "Ký hiệu nào sau đây được dùng để bắt đầu một dòng chú thích đơn (Single-line comment) trong C#?",
        "explanation": "Mục 3.2.1 Deitel: Hai dấu gạch chéo // bắt đầu một chú thích một dòng, trình biên dịch C# sẽ bỏ qua mọi ký tự từ // đến cuối dòng đó.",
        "correct": "Cặp dấu gạch chéo // ở đầu chú thích.",
        "shorter": [
            "Dấu thăng # đơn độc."
        ],
        "longer": [
            "Cặp dấu gạch chéo và dấu hoa thị /* bao bọc khối văn bản chú thích.",
            "Ký hiệu dấu chấm phẩy ; đặt ở cuối mỗi câu lệnh thực thi trong mã nguồn."
        ]
    },
    # Q3: (2, 3) -> Pos C (2), Rank 3
    {
        "id": 3,
        "category": "Khai báo Lớp",
        "bloom": "Remember",
        "question": "Theo quy ước đặt tên chuẩn của Microsoft và giáo trình Deitel, tên Lớp (Class) trong C# nên tuân theo quy tắc nào?",
        "explanation": "Mục 3.2.4 Deitel: Tên lớp trong C# sử dụng quy ước PascalCase, viết hoa chữ cái đầu tiên của mỗi từ cấu thành (ví dụ: Welcome1, BankAccount).",
        "correct": "Quy ước PascalCase viết hoa chữ cái đầu của mỗi từ cấu thành tên lớp.",
        "shorter": [
            "Quy ước camelCase.",
            "Viết hoa toàn bộ từ đầu đến cuối."
        ],
        "longer": [
            "Viết thường toàn bộ tên lớp và ngăn cách các từ bằng các dấu gạch dưới snake_case."
        ]
    },
    # Q4: (3, 4) -> Pos D (3), Rank 4 (Longest)
    {
        "id": 4,
        "category": "Khai báo Lớp",
        "bloom": "Understand",
        "question": "Cặp ký tự nào được ngôn ngữ C# quy định để xác định ranh giới bắt đầu và kết thúc của một khối mã lệnh (Block)?",
        "explanation": "Mục 3.2.7 Deitel: Cặp dấu ngoặc nhọn mở { và đóng } tạo thành một khối mã (Block), xác định phạm vi của lớp, phương thức hay cấu trúc điều khiển.",
        "correct": "Cặp dấu ngoặc nhọn mở { để bắt đầu và dấu ngoặc nhọn đóng } để kết thúc phạm vi khối mã.",
        "shorter": [
            "Cặp ngoặc tròn ( ).",
            "Cặp ngoặc vuông [ ].",
            "Cặp từ khóa BEGIN và END."
        ],
        "longer": []
    },
    # Q5: (1, 1) -> Pos B (1), Rank 1 (Shortest)
    {
        "id": 5,
        "category": "Xuất dữ liệu Console",
        "bloom": "Remember",
        "question": "Phương thức nào của lớp Console có chức năng in chuỗi ký tự ra màn hình và đưa con trỏ xuống đầu dòng tiếp theo?",
        "explanation": "Mục 3.2.6 Deitel: Console.WriteLine xuất dòng văn bản ra màn hình console và tự động định vị con trỏ ở đầu dòng mới kế tiếp.",
        "correct": "Console.WriteLine.",
        "shorter": [],
        "longer": [
            "Phương thức Console.Write giữ nguyên vị trí con trỏ trên dòng.",
            "Phương thức Console.ReadLine chờ người dùng nhấn phím Enter.",
            "Phương thức Console.Clear làm sạch toàn bộ cửa sổ giao diện dòng lệnh."
        ]
    },
    # Q6: (2, 2) -> Pos C (2), Rank 2
    {
        "id": 6,
        "category": "Xuất dữ liệu Console",
        "bloom": "Understand",
        "question": "Điểm khác biệt cốt lõi giữa hai phương thức Console.Write và Console.WriteLine trong C# là gì?",
        "explanation": "Mục 3.4.1 Deitel: Console.Write in chuỗi nhưng không đưa con trỏ xuống dòng mới, trong khi Console.WriteLine tự động gửi thêm ký tự xuống dòng.",
        "correct": "Console.Write không đưa con trỏ xuống dòng mới sau khi xuất xong.",
        "shorter": [
            "Write in chậm hơn WriteLine."
        ],
        "longer": [
            "Console.WriteLine chỉ cho phép xuất các số nguyên mà không thể xuất chuỗi ký tự văn bản.",
            "Console.Write yêu cầu quyền quản trị viên Administrator hệ thống mới có thể thực thi thành công."
        ]
    },
    # Q7: (3, 3) -> Pos D (3), Rank 3
    {
        "id": 7,
        "category": "Ký tự thoát Escape Sequences",
        "bloom": "Remember",
        "question": "Ký tự thoát (Escape Sequence) nào trong chuỗi ký tự C# đại diện cho hành động đưa con trỏ xuống một dòng mới (Newline)?",
        "explanation": "Mục 3.4.2 Deitel: Ký tự thoát \\n (Newline) đẩy con trỏ xuống đầu dòng tiếp theo; \\ đại diện cho ký tự thoát (Escape character).",
        "correct": "Ký tự thoát \\n quy định xuống một dòng mới trong chuỗi văn bản.",
        "shorter": [
            "Ký hiệu \\t.",
            "Ký hiệu \\r lùi đầu dòng."
        ],
        "longer": [
            "Ký hiệu hai dấu gạch chéo ngược \\\\ in ra dấu gạch chéo đơn độc lập trên màn hình."
        ]
    },
    # Q8: (0, 4) -> Pos A (0), Rank 4 (Longest)
    {
        "id": 8,
        "category": "Ký tự thoát Escape Sequences",
        "bloom": "Apply",
        "question": "Để in ra màn hình chuỗi ký tự chứa dấu ngoặc kép: \"Hello\", câu lệnh C# nào sau đây là hoàn toàn hợp lệ?",
        "explanation": "Mục 3.4.2 Deitel: Để nhúng dấu ngoặc kép bên trong một chuỗi ký tự mà không làm đóng chuỗi, ta phải dùng ký tự thoát \\\".",
        "correct": "Console.WriteLine(\"\\\"Hello\\\"\"); sử dụng ký tự thoát \\\" để vô hiệu hóa ý nghĩa kết thúc chuỗi của dấu ngoặc kép.",
        "shorter": [
            "Console.WriteLine(\"\"Hello\"\");",
            "Console.WriteLine('/Hello/');",
            "Console.WriteLine(@'Hello');"
        ],
        "longer": []
    },
    # Q9: (2, 1) -> Pos C (2), Rank 1 (Shortest)
    {
        "id": 9,
        "category": "Ký tự thoát Escape Sequences",
        "bloom": "Remember",
        "question": "Ký tự thoát nào sau đây được sử dụng để căn lề ngang theo từng bước Tab (Tab stop) trên màn hình Console?",
        "explanation": "Mục 3.4.2 Deitel: Ký tự \\t dịch chuyển con trỏ màn hình đến vị trí tab kế tiếp (Horizontal Tab), rất hữu ích khi in các bảng số liệu.",
        "correct": "Ký tự thoát \\t.",
        "shorter": [],
        "longer": [
            "Ký hiệu \\b lùi một khoảng trắng.",
            "Ký hiệu \\r đưa con trỏ về đầu dòng hiện hành.",
            "Ký hiệu \\a phát ra âm thanh cảnh báo hệ thống qua loa máy tính."
        ]
    },
    # Q10: (3, 2) -> Pos D (3), Rank 2
    {
        "id": 10,
        "category": "String Interpolation",
        "bloom": "Remember",
        "question": "Tính năng Định dạng chuỗi nội suy (String Interpolation) trong C# được kích hoạt bằng ký tự tiền tố nào đặt trước chuỗi?",
        "explanation": "Mục 3.5 Deitel: Ký tự dollar $ đặt ngay trước dấu mở ngoặc kép biến chuỗi thành một chuỗi nội suy (Interpolated string).",
        "correct": "Ký tự dollar $ đặt ngay trước dấu mở ngoặc kép của chuỗi.",
        "shorter": [
            "Dấu thăng # ở đầu chuỗi."
        ],
        "longer": [
            "Ký tự dấu chấm hỏi ? đặt trước tên biến bên trong khối ngoặc nhọn.",
            "Ký tự chữ a còng @ dùng để định dạng chuỗi nguyên văn bỏ qua ký tự thoát."
        ]
    },
    # Q11: (0, 3) -> Pos A (0), Rank 3
    {
        "id": 11,
        "category": "String Interpolation",
        "bloom": "Apply",
        "question": "Giả sử biến int age = 20; câu lệnh Console.WriteLine($\"Tuoi cua ban la {age}\"); sẽ xuất ra kết quả gì?",
        "explanation": "Mục 3.5 Deitel: Trình biên dịch C# thay thế biểu thức nội suy {age} bằng giá trị thực tế của biến age tại thời điểm chạy.",
        "correct": "Dòng văn bản: Tuoi cua ban la 20 hiển thị trọn vẹn trên màn hình.",
        "shorter": [
            "Tuoi cua ban la {age}.",
            "Lỗi biên dịch cú pháp."
        ],
        "longer": [
            "Dòng văn bản: Tuoi cua ban la {20} bao gồm cả hai dấu ngoặc nhọn bao quanh giá trị số."
        ]
    },
    # Q12: (1, 4) -> Pos B (1), Rank 4 (Longest)
    {
        "id": 12,
        "category": "String Interpolation",
        "bloom": "Understand",
        "question": "Ưu điểm vượt trội nhất của String Interpolation ($) so với phép nối chuỗi bằng toán tử cộng (+) truyền thống là gì?",
        "explanation": "Mục 3.5 Deitel: String Interpolation giúp mã nguồn trong sáng, dễ đọc, hạn chế lỗi nhầm lẫn dấu cách và được tối ưu hóa hiệu năng biên dịch.",
        "correct": "Cú pháp trực quan, dễ bảo trì, nhúng trực tiếp biến vào biểu thức và tối ưu hóa cấp phát bộ nhớ hơn phép nối chuỗi cộng.",
        "shorter": [
            "Cho phép bỏ qua hoàn toàn kiểu dữ liệu.",
            "Tự động dịch mã sang tệp nhị phân Assembly.",
            "Không cần sử dụng lớp Console."
        ],
        "longer": []
    },
    # Q13: (3, 1) -> Pos D (3), Rank 1 (Shortest)
    {
        "id": 13,
        "category": "Kiểu Dữ liệu & Biến",
        "bloom": "Remember",
        "question": "Kiểu dữ liệu nào trong C# được sử dụng để lưu trữ các giá trị số nguyên trong phạm vi từ khoảng -2.14 tỷ đến +2.14 tỷ?",
        "explanation": "Mục 3.6.1 Deitel: Kiểu int trong C# đại diện cho số nguyên có dấu 32-bit (System.Int32), có dải giá trị từ -2,147,483,648 đến +2,147,483,647.",
        "correct": "Kiểu dữ liệu int.",
        "shorter": [],
        "longer": [
            "Kiểu dữ liệu bool chỉ lưu giá trị đúng sai.",
            "Kiểu dữ liệu string chuyên dùng lưu chuỗi văn bản.",
            "Kiểu dữ liệu double lưu trữ số thực dấu phẩy động 64-bit."
        ]
    },
    # Q14: (0, 2) -> Pos A (0), Rank 2
    {
        "id": 14,
        "category": "Kiểu Dữ liệu & Biến",
        "bloom": "Understand",
        "question": "Quy tắc đặt tên định danh cho biến (Variable Identifier) nào sau đây là KHÔNG hợp lệ trong C#?",
        "explanation": "Mục 3.6.1 Deitel: Tên định danh trong C# không được bắt đầu bằng chữ số (ví dụ: 1number là bất hợp lệ); chỉ được bắt đầu bằng chữ cái hoặc dấu gạch dưới _.",
        "correct": "Tên biến bắt đầu bằng một chữ số như 1stValue hay 2Total.",
        "shorter": [
            "Tên biến có chứa dấu gạch dưới."
        ],
        "longer": [
            "Tên biến sử dụng chữ in hoa và chữ in thường kết hợp theo quy ước camelCase.",
            "Tên biến có độ dài vượt quá 20 ký tự nhưng chỉ bao gồm các chữ cái hợp lệ."
        ]
    },
    # Q15: (1, 3) -> Pos B (1), Rank 3
    {
        "id": 15,
        "category": "Nhập liệu Bàn phím",
        "bloom": "Remember",
        "question": "Phương thức Console.ReadLine() trong C# trả về kết quả thuộc kiểu dữ liệu nào sau khi người dùng nhấn Enter?",
        "explanation": "Mục 3.6.4 Deitel: Console.ReadLine() luôn đọc toàn bộ dòng ký tự từ bàn phím và trả về một đối tượng kiểu chuỗi (string).",
        "correct": "Kiểu chuỗi ký tự string chứa toàn bộ nội dung dòng văn bản vừa nhập.",
        "shorter": [
            "Kiểu số nguyên int.",
            "Kiểu logic bool."
        ],
        "longer": [
            "Kiểu mảng nhị phân các byte đại diện cho mã quét phần cứng của từng phím bấm vừa gõ."
        ]
    },
    # Q16: (2, 4) -> Pos C (2), Rank 4 (Longest)
    {
        "id": 16,
        "category": "Ép kiểu & Phân tích",
        "bloom": "Apply",
        "question": "Để chuyển đổi một chuỗi văn bản do Console.ReadLine() trả về sang số nguyên int, phương thức nào sau đây được sử dụng?",
        "explanation": "Mục 3.6.4 Deitel: int.Parse(string) nhận vào một chuỗi ký tự biểu diễn số và chuyển đổi thành giá trị kiểu int tương ứng.",
        "correct": "Phương thức int.Parse() nhận tham số là chuỗi và trả về giá trị số nguyên kiểu int tương ứng nếu cú pháp hợp lệ.",
        "shorter": [
            "Phương thức int.Convert().",
            "Hàm ép kiểu tĩnh (int).",
            "Phương thức String.ToInt()."
        ],
        "longer": []
    },
    # Q17: (0, 1) -> Pos A (0), Rank 1 (Shortest)
    {
        "id": 17,
        "category": "Xử lý Lỗi Ngoại lệ",
        "bloom": "Understand",
        "question": "Hiện tượng gì sẽ xảy ra nếu người dùng nhập chuỗi \"hello\" vào câu lệnh int.Parse(Console.ReadLine())?",
        "explanation": "Mục 3.6.4 Deitel: Nếu chuỗi không thể phân tích cú pháp thành một số nguyên hợp lệ, phương thức int.Parse sẽ ném ra lỗi ngoại lệ FormatException.",
        "correct": "Ném ngoại lệ FormatException.",
        "shorter": [],
        "longer": [
            "Chương trình tự động gán giá trị 0 cho biến mà không thông báo lỗi.",
            "Trình biên dịch tự động khởi động lại máy tính để khôi phục trạng thái ban đầu.",
            "Hệ điều hành chuyển đổi chuỗi hello thành độ dài 5 ký tự và lưu vào biến số nguyên."
        ]
    },
    # Q18: (1, 2) -> Pos B (1), Rank 2
    {
        "id": 18,
        "category": "Bản chất Bộ nhớ RAM",
        "bloom": "Understand",
        "question": "Bản chất kỹ thuật thực sự của một Biến (Variable) trong bộ nhớ máy tính là gì?",
        "explanation": "Mục 3.7 Deitel: Mọi biến đều có tên, kiểu, kích thước và giá trị; biến thực chất là tên định danh đại diện cho một vị trí ô nhớ trong RAM.",
        "correct": "Tên định danh đại diện cho một vị trí địa chỉ ô nhớ trong bộ nhớ RAM.",
        "shorter": [
            "Một tệp tin lưu trên ổ cứng SSD."
        ],
        "longer": [
            "Một chỉ thị lệnh được vi xử lý CPU thực thi trực tiếp trên bo mạch chủ hệ thống.",
            "Một bản ghi cơ sở dữ liệu được lưu trữ vĩnh viễn trên dịch vụ điện toán đám mây."
        ]
    },
    # Q19: (2, 3) -> Pos C (2), Rank 3
    {
        "id": 19,
        "category": "Bản chất Bộ nhớ RAM",
        "bloom": "Understand",
        "question": "Thao tác gán giá trị mới cho một biến đã tồn tại trong C# (ví dụ: number1 = 99;) tuân theo nguyên lý nào?",
        "explanation": "Mục 3.7 Deitel: Ghi giá trị vào ô nhớ là thao tác phá hủy (destructive) - giá trị cũ bị xóa hoàn toàn và thay thế bởi giá trị mới.",
        "correct": "Nguyên lý Ghi đè phá hủy (Destructive): giá trị cũ trong ô nhớ bị xóa vĩnh viễn để nhường chỗ cho giá trị mới.",
        "shorter": [
            "Nguyên lý Đọc không phá hủy.",
            "Nguyên lý phân mảnh ô nhớ RAM."
        ],
        "longer": [
            "Nguyên lý đồng bộ hóa dữ liệu song song và nhân bản phân tán qua hai tiến trình xử lý ngầm độc lập có giám sát chặt chẽ của hệ thống."
        ]
    },
    # Q20: (3, 4) -> Pos D (3), Rank 4 (Longest)
    {
        "id": 20,
        "category": "Bản chất Bộ nhớ RAM",
        "bloom": "Understand",
        "question": "Khi CPU đọc giá trị từ biến number1 để thực hiện phép tính cộng sum = number1 + number2, giá trị của number1 trong RAM sẽ ra sao?",
        "explanation": "Mục 3.7 Deitel: Đọc giá trị từ một vị trí bộ nhớ là thao tác không phá hủy (non-destructive) - giá trị gốc trong ô nhớ vẫn được bảo tồn.",
        "correct": "Giá trị trong ô nhớ number1 vẫn được giữ nguyên vẹn không hề suy suyển vì thao tác đọc bộ nhớ là không phá hủy (non-destructive).",
        "shorter": [
            "Bị xóa sạch về giá trị 0.",
            "Tự động tăng thêm 1 đơn vị.",
            "Bị hủy giải phóng khỏi RAM."
        ],
        "longer": []
    },
    # Q21: (1, 1) -> Pos B (1), Rank 1 (Shortest)
    {
        "id": 21,
        "category": "Toán tử Số học",
        "bloom": "Remember",
        "question": "Ký hiệu nào sau đây được sử dụng để biểu diễn phép toán nhân trong ngôn ngữ C#?",
        "explanation": "Mục 3.8 Deitel: Trong C#, phép nhân sử dụng dấu sao *, phép chia dùng dấu gạch chéo /, không dùng dấu nhân x hay dấu chia hai chấm :.",
        "correct": "Dấu hoa thị *.",
        "shorter": [],
        "longer": [
            "Ký tự chữ x viết thường.",
            "Ký hiệu dấu chấm ở giữa biểu thức.",
            "Từ khóa multiply tích hợp sẵn trong thư viện."
        ]
    },
    # Q22: (2, 2) -> Pos C (2), Rank 2
    {
        "id": 22,
        "category": "Phép chia Số nguyên",
        "bloom": "Apply",
        "question": "Trong C#, kết quả của biểu thức số học 7 / 4 khi cả hai toán hạng đều là số nguyên (int) là bao nhiêu?",
        "explanation": "Mục 3.8 Deitel: Phép chia giữa hai số nguyên là phép chia nguyên (Integer division) - phần thập phân bị cắt bỏ hoàn toàn, 7 / 4 bằng 1.",
        "correct": "Giá trị 1 vì phần thập phân bị cắt bỏ hoàn toàn.",
        "shorter": [
            "Giá trị là 1.75."
        ],
        "longer": [
            "Giá trị là 2 do cơ chế tự động làm tròn số lên của hệ điều hành.",
            "Chương trình báo lỗi biên dịch do không chia hết cho nhau."
        ]
    },
    # Q23: (3, 3) -> Pos D (3), Rank 3
    {
        "id": 23,
        "category": "Toán tử Chia lấy dư",
        "bloom": "Apply",
        "question": "Toán tử chia lấy phần dư (%) trong C# khi áp dụng cho biểu thức 17 % 5 sẽ cho kết quả là bao nhiêu?",
        "explanation": "Mục 3.8 Deitel: Toán tử % (remainder / modulus) trả về phần dư sau phép chia nguyên: 17 chia cho 5 được 3 dư 2.",
        "correct": "Giá trị 2 là phần dư còn lại sau phép chia số nguyên.",
        "shorter": [
            "Giá trị là 3.",
            "Giá trị là 3.4."
        ],
        "longer": [
            "Giá trị là 0 do toán tử phần trăm tự động quy đổi biểu thức về dạng tỷ lệ phần trăm."
        ]
    },
    # Q24: (0, 4) -> Pos A (0), Rank 4 (Longest)
    {
        "id": 24,
        "category": "Thứ tự Ưu tiên Toán tử",
        "bloom": "Remember",
        "question": "Thứ tự ưu tiên tính toán của các toán tử số học trong C# tuân theo quy tắc chuẩn mực nào sau đây?",
        "explanation": "Mục 3.8.3 Deitel: Biểu thức trong ngoặc () ưu tiên cao nhất, kế đến là *, /, %, thấp hơn là +, -, cùng độ ưu tiên thì tính từ trái sang phải.",
        "correct": "Ngoặc đơn () được thực hiện trước tiên, kế đến là các phép nhân (*), chia (/), chia lấy dư (%), sau cùng là cộng (+) và trừ (-).",
        "shorter": [
            "Cộng trừ trước, nhân chia sau.",
            "Tính tuần tự từ phải sang trái.",
            "Mọi toán tử có độ ưu tiên như nhau."
        ],
        "longer": []
    },
    # Q25: (2, 1) -> Pos C (2), Rank 1 (Shortest)
    {
        "id": 25,
        "category": "Thứ tự Ưu tiên Toán tử",
        "bloom": "Apply",
        "question": "Giá trị của biểu thức C# sau đây: 2 + 3 * 4 - 6 / 2 là bao nhiêu?",
        "explanation": "Mục 3.8.3 Deitel: 3 * 4 = 12; 6 / 2 = 3; biểu thức trở thành 2 + 12 - 3 = 11.",
        "correct": "Giá trị 11.",
        "shorter": [],
        "longer": [
            "Giá trị 10 sau khi tính tuần tự.",
            "Giá trị 7 do nhầm lẫn thứ tự các phép toán cộng trừ.",
            "Giá trị 14 khi các phép tính nhân chia được thực hiện sau cùng."
        ]
    },
    # Q26: (3, 2) -> Pos D (3), Rank 2
    {
        "id": 26,
        "category": "Biểu thức Đại số",
        "bloom": "Apply",
        "question": "Để tính đa thức đại số bậc 2: y = a*x^2 + b*x + c trong C#, cách viết mã lệnh nào sau đây là chuẩn xác nhất?",
        "explanation": "Mục 3.8.4 Deitel: Trong C# không có toán tử mũ ^ cho số học (^ là bitwise XOR), do đó x^2 phải viết thành x * x.",
        "correct": "y = a * x * x + b * x + c;",
        "shorter": [
            "y = ax^2 + bx + c;"
        ],
        "longer": [
            "y = (a * x)^2 + (b * x) + c;",
            "y = a * (x ^ 2) + b * x + c do ký tự mũ được hiểu là lũy thừa trong toán học."
        ]
    },
    # Q27: (0, 3) -> Pos A (0), Rank 3
    {
        "id": 27,
        "category": "Cấu trúc Rẽ nhánh if",
        "bloom": "Understand",
        "question": "Biểu thức điều kiện nằm bên trong cặp dấu ngoặc đơn của câu lệnh if trong C# bắt buộc phải thuộc kiểu dữ liệu nào?",
        "explanation": "Mục 3.9 Deitel: C# yêu cầu điều kiện của câu lệnh if phải là kiểu boolean (chỉ có giá trị true hoặc false), không cho phép số nguyên như C/C++.",
        "correct": "Kiểu boolean chỉ nhận một trong hai giá trị logic là true hoặc false.",
        "shorter": [
            "Kiểu số nguyên int.",
            "Kiểu chuỗi văn bản string."
        ],
        "longer": [
            "Kiểu con trỏ địa chỉ ô nhớ trỏ trực tiếp đến thanh ghi điều khiển của bộ vi xử lý CPU."
        ]
    },
    # Q28: (1, 4) -> Pos B (1), Rank 4 (Longest)
    {
        "id": 28,
        "category": "Toán tử So sánh Quan hệ",
        "bloom": "Remember",
        "question": "Toán tử nào sau đây trong C# được sử dụng để kiểm tra điều kiện 'Hai toán hạng có giá trị bằng nhau hay không'?",
        "explanation": "Mục 3.9 Deitel: Toán tử kiểm tra bằng nhau trong C# là hai dấu bằng liền nhau ==, còn một dấu bằng đơn = là toán tử gán giá trị.",
        "correct": "Cặp hai dấu bằng liền nhau == biểu thị phép so sánh bằng, phân biệt hoàn toàn với toán tử gán giá trị một dấu bằng =.",
        "shorter": [
            "Một dấu bằng đơn = duy nhất.",
            "Ký hiệu hai dấu gạch chéo //.",
            "Ký hiệu dấu hai chấm bằng :=."
        ],
        "longer": []
    },
    # Q29: (3, 1) -> Pos D (3), Rank 1 (Shortest)
    {
        "id": 29,
        "category": "Toán tử So sánh Quan hệ",
        "bloom": "Remember",
        "question": "Ký hiệu nào sau đây trong C# đại diện cho toán tử so sánh 'Khác nhau' (Not equal to)?",
        "explanation": "Mục 3.9 Deitel: Toán tử khác nhau trong C# là != (dấu chấm than kết hợp dấu bằng).",
        "correct": "Toán tử !=.",
        "shorter": [],
        "longer": [
            "Ký hiệu cặp ngoặc nhọn <>.",
            "Ký hiệu dấu ngã bằng ~=.",
            "Từ khóa notequal tích hợp sẵn trong lớp Console."
        ]
    },
    # Q30: (0, 2) -> Pos A (0), Rank 2
    {
        "id": 30,
        "category": "Toán tử So sánh Quan hệ",
        "bloom": "Remember",
        "question": "Toán tử nào sau đây trong C# đại diện cho phép so sánh 'Lớn hơn hoặc bằng'?",
        "explanation": "Mục 3.9 Deitel: Toán tử lớn hơn hoặc bằng là >=. Viết => là sai cú pháp (=> là lambda operator trong các phiên bản sau).",
        "correct": "Toán tử >= với dấu lớn hơn đứng trước dấu bằng.",
        "shorter": [
            "Toán tử => ngược lại."
        ],
        "longer": [
            "Ký hiệu hai dấu lớn hơn liền nhau >> biểu thị phép dịch bit.",
            "Từ khóa greater_or_equal định nghĩa trong thư viện chuẩn .NET FCL."
        ]
    },
    # Q31: (1, 3) -> Pos B (1), Rank 3
    {
        "id": 31,
        "category": "Lỗi Lập trình Kinh điển",
        "bloom": "Analyze",
        "question": "Hậu quả logic nào sẽ xảy ra nếu lập trình viên vô tình đặt dấu chấm phẩy ngay sau mệnh đề điều kiện của if: if (x == y); Console.WriteLine(\"Bang nhau\");?",
        "explanation": "Mục 3.9 Deitel: Dấu chấm phẩy sau if tạo thành một câu lệnh rỗng (empty statement). Khối lệnh phía sau sẽ luôn luôn được thực thi dù điều kiện đúng hay sai!",
        "correct": "Dấu chấm phẩy tạo thành câu lệnh rỗng khiến lệnh in luôn luôn được thực thi bất kể x có bằng y hay không.",
        "shorter": [
            "Trình biên dịch báo lỗi CS1002.",
            "Chương trình bị crash ngay lập tức."
        ],
        "longer": [
            "Hệ điều hành Windows sẽ tự động kích hoạt tính năng phục hồi lỗi cú pháp và xóa bỏ dấu chấm phẩy thừa đó của lập trình viên."
        ]
    },
    # Q32: (2, 4) -> Pos C (2), Rank 4 (Longest)
    {
        "id": 32,
        "category": "Lỗi Lập trình Kinh điển",
        "bloom": "Understand",
        "question": "Tại sao trong C#, lỗi gõ nhầm if (x = 7) thay vì if (x == 7) lại được trình biên dịch phát hiện và cảnh báo ngay lập tức?",
        "explanation": "Mục 3.9 Deitel: Phép gán x = 7 trả về giá trị số nguyên 7, trong khi if bắt buộc điều kiện phải là kiểu bool. Do đó C# báo lỗi type mismatch, tránh được bug nghiêm trọng của C/C++.",
        "correct": "Vì phép gán x = 7 trả về giá trị số nguyên 7, trong khi câu lệnh if trong C# bắt buộc biểu thức điều kiện phải thuộc kiểu dữ liệu boolean.",
        "shorter": [
            "Vì C# cấm sử dụng số 7.",
            "Vì dấu bằng đơn không có trong C#.",
            "Vì biến x chưa được khai báo kiểu."
        ],
        "longer": []
    },
    # Q33: (0, 1) -> Pos A (0), Rank 1 (Shortest)
    {
        "id": 33,
        "category": "Từ khóa C#",
        "bloom": "Remember",
        "question": "Từ khóa nào trong C# biểu thị rằng phương thức không trả về bất kỳ giá trị nào cho lời gọi?",
        "explanation": "Mục 3.2.5 Deitel: Từ khóa void quy định kiểu trả về rỗng, phương thức sẽ thực hiện tác vụ mà không trả dữ liệu về nơi gọi.",
        "correct": "Từ khóa void.",
        "shorter": [],
        "longer": [
            "Từ khóa null chỉ giá trị rỗng.",
            "Từ khóa empty khai báo chuỗi rỗng.",
            "Từ khóa return dừng thực thi khối lệnh."
        ]
    },
    # Q34: (1, 2) -> Pos B (1), Rank 2
    {
        "id": 34,
        "category": "Môi trường Visual Studio",
        "bloom": "Understand",
        "question": "Tổ hợp phím tắt nào được sử dụng trong Visual Studio để biên dịch và chạy ứng dụng Console mà giữ cửa sổ không bị đóng ngay?",
        "explanation": "Mục 3.3.4 Deitel: Tổ hợp phím Ctrl + F5 (Start Without Debugging) chạy ứng dụng và tự động hiển thị dòng 'Press any key to continue...' giữ màn hình console.",
        "correct": "Tổ hợp phím tắt Ctrl + F5 để chạy không gỡ lỗi.",
        "shorter": [
            "Phím F5 chạy có gỡ lỗi."
        ],
        "longer": [
            "Tổ hợp phím tắt Alt + F4 dùng để đóng ngay cửa sổ ứng dụng đang mở.",
            "Tổ hợp phím Ctrl + Shift + B dùng để biên dịch toàn bộ solution mà không chạy."
        ]
    },
    # Q35: (2, 3) -> Pos C (2), Rank 3
    {
        "id": 35,
        "category": "Môi trường Visual Studio",
        "bloom": "Remember",
        "question": "Tính năng nào của Visual Studio tự động liệt kê danh sách các thành viên, phương thức và từ khóa gợi ý khi người dùng đang gõ mã nguồn?",
        "explanation": "Mục 3.3.3 Deitel: IntelliSense là trợ lý mã nguồn thông minh giúp tự động hoàn thành từ khóa, hiển thị danh sách thành viên và tham số hàm.",
        "correct": "Tính năng trợ giúp thông minh IntelliSense hỗ trợ tự động hoàn thiện mã nguồn.",
        "shorter": [
            "Cửa sổ Solution Explorer.",
            "Cửa sổ Output Log."
        ],
        "longer": [
            "Trình biên dịch tức thời Just-In-Time Compiler chạy ngầm bên dưới hệ thống máy ảo CLR."
        ]
    },
    # Q36: (3, 4) -> Pos D (3), Rank 4 (Longest)
    {
        "id": 36,
        "category": "Môi trường Visual Studio",
        "bloom": "Understand",
        "question": "Cửa sổ nào trong Visual Studio hiển thị danh sách các lỗi cú pháp, số dòng và mô tả chi tiết khi chương trình biên dịch thất bại?",
        "explanation": "Mục 3.3.5 Deitel: Cửa sổ Error List liệt kê toàn bộ các lỗi cú pháp (Syntax errors) và cảnh báo (Warnings), cho phép nhấp đúp để nhảy ngay đến dòng lỗi.",
        "correct": "Cửa sổ Error List hiển thị mã lỗi, mô tả chi tiết, số dòng và cho phép nhấp đúp chuột để nhảy đến đúng vị trí mã lỗi.",
        "shorter": [
            "Cửa sổ Toolbox kéo thả.",
            "Cửa sổ Properties thiết lập.",
            "Cửa sổ Solution Explorer."
        ],
        "longer": []
    },
    # Q37: (1, 1) -> Pos B (1), Rank 1 (Shortest)
    {
        "id": 37,
        "category": "Thứ tự Ưu tiên Toàn diện",
        "bloom": "Remember",
        "question": "Trong tất cả các toán tử sau đây: (+, ==, *, =), toán tử nào có mức độ ưu tiên tính toán THẤP NHẤT?",
        "explanation": "Mục 3.9 & Hình 3.23 Deitel: Toán tử gán = có độ ưu tiên thấp nhất để đảm bảo toàn bộ phép tính toán và so sánh hoàn tất xong mới gán kết quả vào biến.",
        "correct": "Toán tử gán =.",
        "shorter": [],
        "longer": [
            "Toán tử nhân *.",
            "Toán tử cộng số học +.",
            "Toán tử so sánh bằng nhau ==."
        ]
    },
    # Q38: (2, 2) -> Pos C (2), Rank 2
    {
        "id": 38,
        "category": "Khoảng trắng & Định dạng",
        "bloom": "Understand",
        "question": "Khái niệm khoảng trắng (Whitespace) trong C# bao gồm những thành phần nào sau đây?",
        "explanation": "Mục 3.2.3 Deitel: Whitespace bao gồm ký tự dấu cách (space), ký tự tab, ký tự xuống dòng (newline) và dòng trống; trình biên dịch bỏ qua các khoảng trắng thừa.",
        "correct": "Các ký tự dấu cách, dấu tab, ký tự xuống dòng và dòng trống trong mã nguồn.",
        "shorter": [
            "Chỉ bao gồm dấu cách đơn lẻ."
        ],
        "longer": [
            "Chỉ các khối chú thích XML bắt đầu bằng ba dấu gạch chéo /// trong phần đầu tệp tin.",
            "Toàn bộ các dòng mã lệnh chứa phương thức Main được đánh dấu đặc biệt bởi lập trình viên."
        ]
    },
    # Q39: (3, 3) -> Pos D (3), Rank 3
    {
        "id": 39,
        "category": "Toán tử Số học",
        "bloom": "Apply",
        "question": "Để kết quả phép chia 7 / 4 trong C# nhận được giá trị số thực chính xác là 1.75, lập trình viên cần viết biểu thức như thế nào?",
        "explanation": "Mục 3.8 Deitel: Muốn kết quả phép chia là số thực, ít nhất một trong hai toán hạng phải là số thực (ví dụ: 7.0 / 4 hoặc 7 / 4.0 hoặc ép kiểu (double)7 / 4).",
        "correct": "Viết ít nhất một toán hạng dưới dạng số thực như 7.0 / 4 hoặc (double)7 / 4.",
        "shorter": [
            "Viết phép tính là 7 : 4.",
            "Thêm dấu chấm phẩy vào sau số 4."
        ],
        "longer": [
            "Bắt buộc phải khai báo lại toàn bộ các biến số nguyên trong chương trình thành kiểu chuỗi ký tự string."
        ]
    },
    # Q40: (0, 4) -> Pos A (0), Rank 4 (Longest)
    {
        "id": 40,
        "category": "Tổng kết Chương 3",
        "bloom": "Understand",
        "question": "Quy trình chuẩn mực 3 bước của một ứng dụng Console nhập dữ liệu, tính toán và hiển thị kết quả trong C# là gì?",
        "explanation": "Mục 3.6 Deitel: Quy trình kinh điển của chương trình Addition.cs gồm: 1) Nhập chuỗi từ bàn phím qua Console.ReadLine và ép kiểu bằng int.Parse; 2) Tính toán số học trong bộ nhớ RAM; 3) Xuất kết quả qua Console.WriteLine bằng String Interpolation $.",
        "correct": "Bước 1: Nhắc và đọc chuỗi từ bàn phím bằng Console.ReadLine rồi ép kiểu với int.Parse; Bước 2: Thực hiện tính toán số học trong bộ nhớ RAM; Bước 3: Xuất kết quả ra màn hình với Console.WriteLine sử dụng String Interpolation $.",
        "shorter": [
            "Bước 1: Tạo Form; Bước 2: Kéo thả Button; Bước 3: Đổi màu BackColor.",
            "Bước 1: Khởi động máy ảo CLR; Bước 2: Dịch mã sang MSIL; Bước 3: Tắt máy.",
            "Bước 1: Đọc bàn phím; Bước 2: Ghi dữ liệu ra tệp tin; Bước 3: Gửi email."
        ],
        "longer": []
    }
]

print(f"Total questions defined: {len(questions_def)}")
assert len(questions_def) == 40, f"Expected 40 questions, got {len(questions_def)}"

final_quiz = []
pos_counts = Counter()
rank_counts = Counter()

for idx, (target_pos, target_rank) in enumerate(TARGET_SPECS):
    q_data = questions_def[idx]
    correct_text = q_data["correct"]
    correct_len = len(correct_text)
    
    shorter_list = list(q_data.get("shorter", []))
    longer_list = list(q_data.get("longer", []))
    
    # Verify rank requirement
    req_shorter = target_rank - 1
    req_longer = 4 - target_rank
    
    assert len(shorter_list) == req_shorter, f"Q{idx+1}: shorter list length {len(shorter_list)} != {req_shorter}"
    assert len(longer_list) == req_longer, f"Q{idx+1}: longer list length {len(longer_list)} != {req_longer}"
    
    # Check length sanity
    for s in shorter_list:
        assert len(s) < correct_len, f"Q{idx+1}: shorter option '{s}' ({len(s)}) not < correct ({correct_len})"
    for l in longer_list:
        assert len(l) > correct_len, f"Q{idx+1}: longer option '{l}' ({len(l)}) not > correct ({correct_len})"
        
    distractors = shorter_list + longer_list
    
    options = [None, None, None, None]
    options[target_pos] = correct_text
    
    dist_idx = 0
    for p in range(4):
        if p != target_pos:
            options[p] = distractors[dist_idx]
            dist_idx += 1
            
    # Measure actual rank of correct in options
    lens = [(len(opt), opt_idx) for opt_idx, opt in enumerate(options)]
    lens_sorted = sorted(lens, key=lambda x: x[0])
    actual_rank = [r + 1 for r, (l, opt_idx) in enumerate(lens_sorted) if opt_idx == target_pos][0]
    
    assert actual_rank == target_rank, f"Q{idx+1}: actual rank {actual_rank} != target {target_rank}"
    
    pos_counts[target_pos] += 1
    rank_counts[actual_rank] += 1
    
    final_quiz.append({
        "id": q_data["id"],
        "category": q_data["category"],
        "bloom": q_data["bloom"],
        "question": q_data["question"],
        "options": options,
        "correct": target_pos,
        "explanation": q_data["explanation"]
    })

print("Position distribution (0=A, 1=B, 2=C, 3=D):", sorted(pos_counts.items()))
print("Rank distribution (1=shortest, 4=longest):", sorted(rank_counts.items()))

# Export to JSON / JS snippet
with open("js/quiz_ch03_snippet.json", "w", encoding="utf-8") as f:
    json.dump(final_quiz, f, ensure_ascii=False, indent=2)

print("Saved js/quiz_ch03_snippet.json successfully!")
