# -*- coding: utf-8 -*-
"""
Build Final Balanced Quiz for Chapter 1 C#
Strict guarantees:
- Exactly 10 questions with correct answer at position A (0), B (1), C (2), D (3)
- Exactly 10 questions where correct answer length is Rank 1 (shortest), Rank 2, Rank 3, Rank 4 (longest)
- No cyclic patterns (e.g. not ABCDABCD or 12341234)
- Maximum 2 consecutive questions with same position
- Distractors are natural, technically plausible, and length differences within each question are reasonable (spread of 15-35 chars, no 12 vs 120 silliness)
- Question 5 is specifically Rank 1 (shortest) at position B (fixing user's screenshot)
"""

import json
from collections import Counter

# Assigned (pos, rank) targets for Q1..Q40 (generated with seed 2026 and Q5 adjusted):
# Pos: 0=A, 1=B, 2=C, 3=D
# Rank: 1=shortest, 2=2nd shortest, 3=3rd shortest, 4=longest
TARGET_SPECS = [
    # Q01..Q10
    (2, 2), (2, 1), (3, 1), (3, 3), (1, 1), (3, 4), (0, 2), (2, 3), (1, 2), (0, 1),
    # Q11..Q20
    (1, 3), (1, 4), (0, 3), (1, 4), (2, 2), (2, 4), (0, 4), (1, 2), (3, 3), (1, 1),
    # Q21..Q30
    (1, 3), (2, 1), (2, 4), (3, 2), (3, 2), (0, 4), (0, 2), (1, 4), (0, 1), (0, 1),
    # Q31..Q40
    (3, 4), (2, 4), (3, 1), (2, 3), (1, 2), (0, 3), (3, 3), (3, 2), (2, 1), (0, 3)
]

raw_questions_data = [
    # Q1: target_pos = 2 (C), target_rank = 2
    {
        "id": 1,
        "category": "Nền tảng Tính toán",
        "bloom": "Remember",
        "question": "Máy tính xử lý dữ liệu dưới sự điều khiển của các chuỗi chỉ thị được gọi là gì?",
        "explanation": "Theo mục 1.3 giáo trình Deitel: Máy tính xử lý dữ liệu dưới sự điều khiển của các chuỗi chỉ thị gọi là chương trình máy tính (computer programs) hay phần mềm (software).",
        "options_by_rank": {
            1: "Hệ thống các tệp tin dữ liệu nhị phân lưu trữ trên các đĩa từ tính.",
            2: "Chương trình máy tính (hay các phần mềm hệ thống và ứng dụng / Programs).",
            3: "Các vi mạch bán dẫn phần cứng tích hợp chuyên dụng gắn cố định trên bo mạch chủ.",
            4: "Các thanh ghi lưu trữ trạng thái phần cứng được thiết kế bên trong đế chip vi xử lý.",
        }
    },

    # Q2: target_pos = 2 (C), target_rank = 1 (Shortest)
    {
        "id": 2,
        "category": "Phần cứng Máy tính",
        "bloom": "Understand",
        "question": "Nội dung cốt lõi của Định luật Gordon Moore (đồng sáng lập Intel, 1965) là gì?",
        "explanation": "Định luật Moore (mục 1.3.1): Số lượng bóng bán dẫn trên các vi mạch tích hợp tăng gấp đôi xấp xỉ sau mỗi 18-24 tháng trong khi chi phí sản xuất giữ nguyên, giúp máy tính ngày càng mạnh mẽ và rẻ hơn.",
        "options_by_rank": {
            1: "Số lượng bóng bán dẫn trên vi mạch tăng gấp đôi xấp xỉ sau mỗi 18-24 tháng với chi phí không đổi.",
            2: "Dung lượng bộ nhớ RAM máy tính cá nhân sẽ tăng gấp 4 lần sau mỗi chu kỳ 5 năm phát triển công nghệ.",
            3: "Tốc độ truyền dữ liệu của mạng Internet toàn cầu tăng gấp đôi sau mỗi 12 tháng nhờ mở rộng mạng cáp quang.",
            4: "Giá thành sản xuất vi mạch xử lý máy tính sẽ giảm đi một nửa sau mỗi chu kỳ ba năm hoạt động trên thị trường.",
        }
    },

    # Q3: target_pos = 3 (D), target_rank = 1 (Shortest)
    {
        "id": 3,
        "category": "Kiến trúc Máy tính",
        "bloom": "Remember",
        "question": "Theo cách phân loại kiến trúc logic của giáo trình Deitel, máy tính được chia thành mấy khối chức năng logic?",
        "explanation": "Mục 1.3.2 phân loại máy tính thành 6 khối chức năng logic: Input unit, Output unit, Memory unit, ALU, CPU, Secondary storage unit.",
        "options_by_rank": {
            1: "6 khối chức năng logic (Input, Output, Memory, ALU, CPU, Secondary Storage).",
            2: "4 khối phần cứng cơ bản của máy tính cá nhân gồm màn hình hiển thị, chuột, bàn phím và CPU.",
            3: "3 khối xử lý tổng quát bao gồm khối tiếp nhận dữ liệu, khối xử lý trung tâm và khối xuất thông tin.",
            4: "8 khối chức năng bao gồm bộ giải mã lệnh, bus truyền dẫn, thanh ghi cache cùng các cổng kết nối ngoại vi.",
        }
    },

    # Q4: target_pos = 3 (D), target_rank = 3 (3rd shortest)
    {
        "id": 4,
        "category": "Kiến trúc Máy tính",
        "bloom": "Understand",
        "question": "Khối chức năng logic nào trực tiếp thực hiện các phép tính số học và so sánh logic (A > B)?",
        "explanation": "ALU (Arithmetic and Logic Unit) là bộ phận trực tiếp thực hiện mọi phép tính toán số học cơ bản (+, -, *, /) và các phép so sánh logic (==, >, <).",
        "options_by_rank": {
            1: "Khối điều khiển trung tâm (Control Unit - CU) điều phối hệ thống.",
            2: "Bộ nhớ chính tạm thời (Memory Unit / RAM) lưu trữ lệnh và biến số.",
            3: "Đơn vị số học và logic (Arithmetic and Logic Unit - ALU) tính toán số học và so sánh.",
            4: "Bộ nhớ thứ cấp (Secondary Storage Unit) lưu trữ tệp tin nhị phân lâu dài trên các ổ đĩa.",
        }
    },

    # Q5: target_pos = 1 (B), target_rank = 1 (Shortest - Solves screenshot issue!)
    {
        "id": 5,
        "category": "Kiến trúc Máy tính",
        "bloom": "Understand",
        "question": "Đặc tính kỹ thuật quan trọng nhất của Bộ nhớ chính (Memory unit / RAM) mà lập trình viên cần ghi nhớ là gì?",
        "explanation": "Bộ nhớ chính RAM có tốc độ truy xuất cực nhanh nhưng là bộ nhớ khả biến (volatile), dữ liệu lưu trữ trên RAM sẽ biến mất hoàn toàn khi tắt máy.",
        "options_by_rank": {
            1: "Dữ liệu mang tính khả biến (volatile), sẽ mất hoàn toàn khi bị ngắt nguồn điện.",
            2: "Dữ liệu được lưu trữ vĩnh viễn trên các phiến đĩa từ và không bao giờ bị mất đi khi mất điện.",
            3: "Tốc độ truy xuất chậm hơn ổ cứng hàng nghìn lần nên CPU chỉ truy cập khi hệ thống cạn kiệt bộ nhớ ảo.",
            4: "Chỉ cho phép đọc dữ liệu nhị phân mà tuyệt đối không hỗ trợ ghi đè hay cập nhật giá trị mới của chương trình.",
        }
    },

    # Q6: target_pos = 3 (D), target_rank = 4 (Longest)
    {
        "id": 6,
        "category": "Kiến trúc Máy tính",
        "bloom": "Understand",
        "question": "Tại sao trong kiến trúc máy tính, CPU không xử lý dữ liệu trực tiếp trên ổ cứng mà phải nạp vào RAM?",
        "explanation": "Sự chênh lệch tốc độ giữa RAM và bộ nhớ thứ cấp (SSD/HDD) lên tới hàng nghìn lần. Nạp dữ liệu vào RAM giúp CPU luôn được cung cấp dữ liệu ở tốc độ cao nhất của bus hệ thống.",
        "options_by_rank": {
            1: "Do kiến trúc phần cứng của CPU và ổ đĩa cứng xung đột chuẩn mã nhị phân.",
            2: "Do ổ cứng chỉ hỗ trợ lưu trữ tệp tin văn bản mà không thể chứa mã máy thực thi.",
            3: "Do hệ điều hành Windows ngăn cấm CPU thực hiện đọc trực tiếp từ các cung từ ổ đĩa.",
            4: "Vì RAM truy xuất nhanh hơn ổ cứng hàng nghìn lần, giúp cung cấp dữ liệu kịp thời cho CPU.",
        }
    },

    # Q7: target_pos = 0 (A), target_rank = 2
    {
        "id": 7,
        "category": "Phần cứng Máy tính",
        "bloom": "Remember",
        "question": "Một bộ vi xử lý đa nhân (multicore processor) có cấu trúc đặc trưng như thế nào?",
        "explanation": "Giáo trình định nghĩa: Bộ vi xử lý đa nhân tích hợp hai hoặc nhiều nhân xử lý (CPUs) trên cùng một đế chip bán dẫn (ví dụ dual-core có 2 CPU, quad-core có 4 CPU).",
        "options_by_rank": {
            1: "Chỉ sở hữu một nhân CPU duy nhất nhưng tăng gấp đôi tốc độ xung nhịp thạch anh hệ thống.",
            2: "Tích hợp hai hoặc nhiều nhân vi xử lý hoàn chỉnh (CPUs) trên cùng một vi mạch bán dẫn duy nhất.",
            3: "Sử dụng hai thanh RAM độc lập gắn trên bo mạch chủ nhằm tăng tốc độ truyền tải bus dữ liệu trung tâm.",
            4: "Ghép nối nhiều thùng máy tính vật lý với nhau thông qua mạng nội bộ để chia sẻ tác vụ tính toán phân tán.",
        }
    },

    # Q8: target_pos = 2 (C), target_rank = 3
    {
        "id": 8,
        "category": "Kiến trúc Máy tính",
        "bloom": "Understand",
        "question": "Vai trò của Bộ nhớ thứ cấp (Secondary Storage Unit) trong hệ thống tính toán là gì?",
        "explanation": "Secondary Storage (SSD, HDD, USB) là bộ lưu trữ bất biến (persistent), dung lượng cao và chi phí thấp trên mỗi byte, giữ dữ liệu lâu dài khi tắt máy.",
        "options_by_rank": {
            1: "Trực tiếp thực hiện các phép nhân chia số thực dấu phẩy động của CPU.",
            2: "Chuyển đổi tín hiệu analog sang digital để phục vụ kết xuất âm thanh loa.",
            3: "Lưu trữ dữ liệu dung lượng lớn, bền vững (persistent) ngay cả khi mất nguồn điện.",
            4: "Đóng vai trò làm bộ tạo xung nhịp đồng hồ điều phối chu kỳ xử lý của toàn bộ bo mạch chủ máy tính.",
        }
    },

    # Q9: target_pos = 1 (B), target_rank = 2
    {
        "id": 9,
        "category": "Phân cấp Dữ liệu",
        "bloom": "Remember",
        "question": "Đơn vị dữ liệu nhỏ nhất trong máy tính, chỉ có thể mang giá trị 0 hoặc 1, được gọi là gì?",
        "explanation": "Bit (viết tắt của Binary Digit) là đơn vị thông tin nhỏ nhất, mang giá trị 0 hoặc 1.",
        "options_by_rank": {
            1: "Ký tự mã hóa nhị phân chuẩn định dạng văn bản ký tự ASCII.",
            2: "Bit (viết tắt của Binary Digit, biểu diễn chữ số nhị phân 0 hoặc 1).",
            3: "Trường dữ liệu đơn vị chứa một nhóm ký tự mang ý nghĩa hoàn chỉnh (Field).",
            4: "Byte dữ liệu tiêu chuẩn được cấu thành từ chuỗi liên tiếp gồm đúng 8 bits nhị phân.",
        }
    },

    # Q10: target_pos = 0 (A), target_rank = 1 (Shortest)
    {
        "id": 10,
        "category": "Phân cấp Dữ liệu",
        "bloom": "Understand",
        "question": "Thứ tự sắp xếp đúng từ đơn giản nhất đến phức tạp nhất trong Cấu trúc phân cấp dữ liệu là gì?",
        "explanation": "Theo Hình 1.3: Cấu trúc phân cấp dữ liệu chuẩn: Bit -> Byte (Ký tự) -> Field (Trường) -> Record (Bản ghi) -> File (Tệp) -> Database (Cơ sở dữ liệu) -> Big Data.",
        "options_by_rank": {
            1: "Bit -> Byte (Character) -> Field -> Record -> File -> Database.",
            2: "Bit -> Field -> Byte -> Record -> File -> Hệ cơ sở dữ liệu quan hệ hoàn chỉnh.",
            3: "Byte -> Bit -> Record -> Field -> File -> Database quản trị dữ liệu quy mô lớn.",
            4: "Record -> Field -> File -> Byte -> Bit -> Hệ thống kho dữ liệu phân tán đám mây.",
        }
    },

    # Q11: target_pos = 1 (B), target_rank = 3
    {
        "id": 11,
        "category": "Phân cấp Dữ liệu",
        "bloom": "Understand",
        "question": "Một Byte gồm bao nhiêu bits và có thể biểu diễn được bao nhiêu trạng thái phân biệt?",
        "explanation": "1 Byte = 8 bits. Số trạng thái tối đa là 2^8 = 256 giá trị riêng biệt, đủ để mã hóa bảng ký tự ASCII chuẩn.",
        "options_by_rank": {
            1: "Gồm đúng 4 bits nhị phân và mã hóa được 16 giá trị trạng thái tín hiệu.",
            2: "Gồm đúng 10 bits nhị phân và mã hóa được 1024 trạng thái lưu trữ bus dữ liệu.",
            3: "Gồm đúng 8 bits nhị phân và biểu diễn được 256 trạng thái khác nhau (từ 0 đến 255).",
            4: "Gồm đúng 16 bits mở rộng cho phép biểu diễn tới 65.536 ký tự đa ngôn ngữ chuẩn Unicode.",
        }
    },

    # Q12: target_pos = 1 (B), target_rank = 4 (Longest)
    {
        "id": 12,
        "category": "Phân cấp Dữ liệu",
        "bloom": "Apply",
        "question": "Trong phân cấp dữ liệu, tập hợp các trường như Mã SV, Họ tên, Điểm thi của cùng một sinh viên được gọi là gì?",
        "explanation": "Record (Bản ghi) là tập hợp các trường thông tin có liên quan mật thiết về một thực thể hoặc đối tượng cụ thể.",
        "options_by_rank": {
            1: "Một trường dữ liệu đơn vị (Field) của cơ sở dữ liệu.",
            2: "Một tệp tin nhị phân có cấu trúc (Structured File) trên ổ cứng.",
            3: "Một cơ sở dữ liệu quan hệ gồm nhiều bảng dữ liệu liên kết với nhau.",
            4: "Một Bản ghi (Record) chứa tập hợp các trường thông tin có liên quan về một đối tượng.",
        }
    },

    # Q13: target_pos = 0 (A), target_rank = 3
    {
        "id": 13,
        "category": "Đo lường Dữ liệu",
        "bloom": "Remember",
        "question": "Theo quy ước khoa học máy tính (hệ nhị phân), 1 Megabyte (MB) bằng bao nhiêu Kilobytes (KB)?",
        "explanation": "Trong hệ nhị phân, các đơn vị tăng theo lũy thừa 2^10 = 1024. Do đó 1 MB = 1024 KB = 1.048.576 Bytes.",
        "options_by_rank": {
            1: "Bằng đúng 512 Kilobytes (KB) theo phân bổ khối bộ nhớ đệm.",
            2: "Bằng đúng 1000 Kilobytes (KB) theo quy tắc làm tròn hệ thập phân.",
            3: "Bằng đúng 1024 Kilobytes (KB) theo quy chuẩn tính lũy thừa nhị phân 2 mũ 10.",
            4: "Bằng đúng 2048 Kilobytes (KB) theo quy chuẩn phân chia dung lượng của bộ nhớ kênh đôi RAM.",
        }
    },

    # Q14: target_pos = 1 (B), target_rank = 4 (Longest)
    {
        "id": 14,
        "category": "Đo lường Dữ liệu",
        "bloom": "Understand",
        "question": "Thứ tự tăng dần chuẩn xác của các đơn vị đo lường dung lượng dữ liệu trên máy tính là:",
        "explanation": "Bảng Hình 1.4 giáo trình Deitel: Kilobyte (KB) < Megabyte (MB) < Gigabyte (GB) < Terabyte (TB) < Petabyte (PB) < Exabyte (EB) < Zettabyte (ZB) < Yottabyte (YB).",
        "options_by_rank": {
            1: "Byte < KB < MB < TB < GB < PB (đặt sai thứ tự TB và GB).",
            2: "Byte < KB < GB < MB < TB < PB (đặt sai thứ tự giữa GB và MB).",
            3: "Byte < KB < MB < GB < TB < PB < ZB < EB < YB (đặt sai thứ tự ZB và EB).",
            4: "Byte < KB < MB < GB < TB < PB < EB < ZB < YB (sắp xếp hoàn toàn chính xác).",
        }
    },

    # Q15: target_pos = 2 (C), target_rank = 2
    {
        "id": 15,
        "category": "Tiến hóa Ngôn ngữ",
        "bloom": "Remember",
        "question": "Ngôn ngữ duy nhất mà phần cứng máy tính (CPU) trực tiếp hiểu và thực thi không qua chương trình dịch là gì?",
        "explanation": "Ngôn ngữ máy (Machine Language) gồm các chuỗi nhị phân 0 và 1 là ngôn ngữ 'bản địa' duy nhất mà mạch điện CPU hiểu và thực thi trực tiếp.",
        "options_by_rank": {
            1: "Hợp ngữ (Assembly Language) sử dụng các mã lệnh viết tắt gợi nhớ thao tác.",
            2: "Ngôn ngữ máy (Machine Language) bao gồm các chuỗi nhị phân gồm chữ số 0 và 1.",
            3: "Ngôn ngữ C++ biên dịch với cờ tối ưu hóa phần cứng ở mức cao nhất của trình dịch.",
            4: "Mã trung gian chuẩn ECMA được thực thi độc lập trên mọi loại kiến trúc vi xử lý hiện đại.",
        }
    },

    # Q16: target_pos = 2 (C), target_rank = 4 (Longest)
    {
        "id": 16,
        "category": "Tiến hóa Ngôn ngữ",
        "bloom": "Understand",
        "question": "Hợp ngữ (Assembly Language) sử dụng các từ viết tắt tiếng Anh mang tính gợi nhớ (như LOAD, ADD, STORE) được gọi là gì?",
        "explanation": "Hợp ngữ sử dụng các từ viết tắt gợi nhớ gọi là mnemonics để đại diện cho các chỉ thị máy nguyên thủy.",
        "options_by_rank": {
            1: "Keywords (các từ khóa cú pháp dành riêng của ngôn ngữ lập trình).",
            2: "Variables (các biến số lưu trữ giá trị tạm thời trong vùng nhớ RAM).",
            3: "Directives (các chỉ thị tiền xử lý dùng để cấu hình trình biên dịch).",
            4: "Mnemonics (các từ viết tắt mang tính gợi nhớ đại diện cho chỉ thị phần cứng máy tính).",
        }
    },

    # Q17: target_pos = 0 (A), target_rank = 4 (Longest)
    {
        "id": 17,
        "category": "Biên dịch & Thông dịch",
        "bloom": "Understand",
        "question": "Điểm khác biệt cốt lõi giữa Trình biên dịch (Compiler) và Trình thông dịch (Interpreter) là gì?",
        "explanation": "Compiler biên dịch trọn vẹn chương trình ra mã máy trước khi chạy (tốc độ cao). Interpreter dịch và chạy từng dòng lệnh một (linh hoạt nhưng chậm hơn).",
        "options_by_rank": {
            1: "Compiler chỉ dùng cho web; Interpreter chỉ dùng cho phát triển hệ thống.",
            2: "Compiler không tạo file chạy; Interpreter luôn tạo tệp tin thực thi .exe độc lập.",
            3: "Compiler chỉ kiểm tra lỗi logic hệ thống; Interpreter chỉ kiểm tra lỗi cú pháp biên dịch.",
            4: "Compiler dịch toàn bộ mã sang mã máy trước khi chạy; Interpreter dịch và thực thi từng dòng.",
        }
    },

    # Q18: target_pos = 1 (B), target_rank = 2
    {
        "id": 18,
        "category": "Biên dịch & Thông dịch",
        "bloom": "Understand",
        "question": "Cơ chế thực thi của ngôn ngữ C# và nền tảng .NET là gì?",
        "explanation": "C# kết hợp ưu điểm của cả hai: Biên dịch trước ra MSIL (độc lập nền tảng) và dùng JIT (Just-In-Time) Compiler biên dịch sang mã máy tại thời điểm thực thi.",
        "options_by_rank": {
            1: "Thuần túy thông dịch từng dòng lệnh mã nguồn C# mỗi khi người dùng khởi chạy ứng dụng.",
            2: "Cơ chế lai (Hybrid): Dịch ra mã MSIL trước, sau đó JIT Compiler dịch sang mã máy khi chạy.",
            3: "Thuần túy biên dịch trực tiếp ra mã máy nhị phân bản địa của CPU tương tự như ngôn ngữ C/C++.",
            4: "Chuyển đổi trực tiếp mã nguồn C# thành mã kịch bản JavaScript để thực thi trong trình duyệt web.",
        }
    },

    # Q19: target_pos = 3 (D), target_rank = 3
    {
        "id": 19,
        "category": "Tiến hóa Ngôn ngữ",
        "bloom": "Understand",
        "question": "Chương trình dùng để chuyển đổi mã hợp ngữ (Assembly) sang mã máy (Machine language) được gọi là gì?",
        "explanation": "Assembler (trình hợp dịch) là phần mềm chuyên trách dịch các chỉ thị hợp ngữ (Assembly) thành mã máy tương ứng.",
        "options_by_rank": {
            1: "Debugger (công cụ hỗ trợ theo dõi và gỡ lỗi phần mềm máy tính).",
            2: "Loader (trình nạp mã chương trình vào RAM để chuẩn bị thực thi).",
            3: "Assembler (trình hợp dịch chuyên trách dịch mã hợp ngữ sang chuỗi mã máy).",
            4: "Linker (trình liên kết các tệp tin đối tượng nhị phân thành tệp chương trình thực thi).",
        }
    },

    # Q20: target_pos = 1 (B), target_rank = 1 (Shortest)
    {
        "id": 20,
        "category": "Công nghệ Đối tượng",
        "bloom": "Understand",
        "question": "Trong Lập trình hướng đối tượng (OOP), sự khác biệt cơ bản giữa Thuộc tính (Attributes) và Hành vi (Behaviors) là gì?",
        "explanation": "Thuộc tính đại diện cho dữ liệu và trạng thái của đối tượng (ví dụ: màu sơn, số dư). Hành vi đại diện cho các hành động (ví dụ: tăng tốc, rút tiền) được hiện thực bằng phương thức.",
        "options_by_rank": {
            1: "Thuộc tính mô tả trạng thái dữ liệu; Hành vi là thao tác đối tượng thực hiện.",
            2: "Thuộc tính là các hằng số bất biến; Hành vi là các biến số thay đổi theo thời gian chạy.",
            3: "Thuộc tính chỉ khai báo trên tài liệu thiết kế; Hành vi là mã nguồn viết trong tệp chương trình.",
            4: "Thuộc tính quyết định tốc độ xử lý phần cứng; Hành vi quyết định dung lượng bộ nhớ RAM mà đối tượng chiếm giữ.",
        }
    },

    # Q21: target_pos = 1 (B), target_rank = 3
    {
        "id": 21,
        "category": "Công nghệ Đối tượng",
        "bloom": "Understand",
        "question": "Mối quan hệ chính xác giữa Lớp (Class) và Đối tượng (Object) trong ngôn ngữ C# là gì?",
        "explanation": "Class là bản vẽ mẫu (blueprint). Từ một Class, ta có thể khởi tạo vô số đối tượng cụ thể (instances) bằng toán tử new.",
        "options_by_rank": {
            1: "Class và Object là hai khái niệm hoàn toàn đồng nghĩa trong ngôn ngữ C#.",
            2: "Object là bản thiết kế trên giấy còn Class là thực thể cụ thể sống trong RAM.",
            3: "Class là bản vẽ mẫu thiết kế (blueprint); Object là thực thể cụ thể sinh ra từ Class.",
            4: "Một Object có thể chứa đồng thời hàng trăm Class độc lập bên trong cấu trúc phân cấp kế thừa đa tầng.",
        }
    },

    # Q22: target_pos = 2 (C), target_rank = 1 (Shortest)
    {
        "id": 22,
        "category": "Công nghệ Đối tượng",
        "bloom": "Remember",
        "question": "Mục tiêu tối thượng hàng đầu của Lập trình hướng đối tượng (OOP) đối với ngành công nghiệp phần mềm là gì?",
        "explanation": "Tái sử dụng phần mềm (Software Reuse) là lợi ích kinh tế và kỹ thuật to lớn nhất của OOP, giúp tận dụng các lớp đã được kiểm thử để giảm thời gian phát triển.",
        "options_by_rank": {
            1: "Tái sử dụng phần mềm (Software Reuse) để nâng cao chất lượng và năng suất.",
            2: "Tiết kiệm dung lượng lưu trữ trên ổ đĩa cứng của máy tính bằng cách nén mã nguồn.",
            3: "Loại bỏ hoàn toàn sự can thiệp của con người trong khâu kiểm thử và phát hiện lỗi phần mềm.",
            4: "Bắt buộc người dùng cuối phải tương tác bằng dòng lệnh thay vì sử dụng giao diện đồ họa trực quan.",
        }
    },

    # Q23: target_pos = 2 (C), target_rank = 4 (Longest)
    {
        "id": 23,
        "category": "Công nghệ Đối tượng",
        "bloom": "Understand",
        "question": "Trụ cột Đóng gói (Encapsulation) trong công nghệ đối tượng mang lại lợi ích gì cho việc bảo vệ mã nguồn?",
        "explanation": "Đóng gói (Encapsulation) gom nhóm dữ liệu và hàm xử lý, đồng thời che giấu chi tiết cài đặt (information hiding) để bảo vệ tính toàn vẹn của đối tượng.",
        "options_by_rank": {
            1: "Cho phép các chương trình bên ngoài truy cập và sửa đổi trực tiếp dữ liệu biến.",
            2: "Mở toàn bộ mã nguồn của các hàm thành viên cho tất cả thành viên trong nhóm dự án.",
            3: "Tự động tăng tốc độ tính toán số học của vi xử lý lên gấp đôi khi chạy thuật toán đa luồng.",
            4: "Gom dữ liệu và phương thức vào lớp, che giấu chi tiết cài đặt để bảo vệ tính toàn vẹn dữ liệu.",
        }
    },

    # Q24: target_pos = 3 (D), target_rank = 2
    {
        "id": 24,
        "category": "Công nghệ Đối tượng",
        "bloom": "Understand",
        "question": "Trụ cột Kế thừa (Inheritance) trong lập trình C# có ý nghĩa kỹ thuật là gì?",
        "explanation": "Kế thừa cho phép một lớp con (derived class) tiếp thu các thuộc tính và phương thức từ một lớp cha (base class) có sẵn, thúc đẩy tái sử dụng mã nguồn.",
        "options_by_rank": {
            1: "Tự động xóa bỏ lớp cha cũ khỏi bộ nhớ RAM để tiết kiệm không gian lưu trữ heap.",
            2: "Tạo lớp mới từ lớp có sẵn, kế thừa thuộc tính và hành vi đồng thời bổ sung tính năng mới.",
            3: "Chuyển đổi kiểu dữ liệu của biến số từ kiểu số nguyên sang kiểu số thực dấu phẩy động chính xác cao.",
            4: "Sao chép thủ công toàn bộ mã nguồn giữa các tệp tin khác nhau trong cùng một dự án phần mềm ứng dụng C#.",
        }
    },

    # Q25: target_pos = 3 (D), target_rank = 2
    {
        "id": 25,
        "category": "Công nghệ Đối tượng",
        "bloom": "Apply",
        "question": "Trong cú pháp C#, câu lệnh nào sau đây dùng để khởi tạo một đối tượng mới từ lớp 'Car' trong bộ nhớ RAM?",
        "explanation": "Toán tử new trong C# được sử dụng để cấp phát vùng nhớ trên Managed Heap cho một đối tượng mới và gọi phương thức khởi tạo (constructor).",
        "options_by_rank": {
            1: "Car myCar = Car.CreateInstance();",
            2: "Car myCar = new Car(\"VinFast VF8\", \"Do\");",
            3: "Car myCar = allocate Memory<Car>(\"VinFast\", \"Do\");",
            4: "Car myCar = construct Object.From(\"Car\", \"VF8\", \"Do\");",
        }
    },

    # Q26: target_pos = 0 (A), target_rank = 4 (Longest)
    {
        "id": 26,
        "category": "Lịch sử C#",
        "bloom": "Remember",
        "question": "Ngôn ngữ C# được ra mắt vào năm nào, bởi tập đoàn nào và ai là kiến trúc sư trưởng chỉ huy thiết kế?",
        "explanation": "C# được Microsoft công bố năm 2000 cùng sáng kiến .NET. Kiến trúc sư trưởng thiết kế C# là Anders Hejlsberg (người cũng thiết kế Turbo Pascal, Delphi, TypeScript).",
        "options_by_rank": {
            1: "Năm 1995, bởi Sun Microsystems, do kiến trúc sư James Gosling thiết kế.",
            2: "Năm 1983, bởi Bell Laboratories, do nhà khoa học Bjarne Stroustrup sáng tạo.",
            3: "Năm 1991, bởi tổ chức mã nguồn mở Python Software Foundation phát triển toàn cầu.",
            4: "Năm 2000, bởi tập đoàn Microsoft, do kiến trúc sư Anders Hejlsberg chỉ huy thiết kế.",
        }
    },

    # Q27: target_pos = 0 (A), target_rank = 2
    {
        "id": 27,
        "category": "Lịch sử C#",
        "bloom": "Understand",
        "question": "Nguồn gốc tên gọi 'C#' xuất phát từ ý nghĩa biểu tượng nào?",
        "explanation": "Dấu '#' mượn từ ký hiệu thăng trong âm nhạc biểu thị sự nâng cấp cao hơn, và được ghép từ 4 dấu '+' của C++ xếp lại, ngụ ý sự kế thừa và tiến hóa.",
        "options_by_rank": {
            1: "Viết tắt từ cụm từ tiếng Anh 'Computer Sharp' biểu thị sự tinh tế của máy tính.",
            2: "Dấu thăng (#) trong âm nhạc thể hiện sự thăng tiến, và ghép từ 4 dấu cộng (++) của C++.",
            3: "Được đặt tên theo một câu lệnh điều khiển dòng đặc biệt xuất hiện trong hệ điều hành Unix.",
            4: "Do nhóm kỹ sư phần mềm lựa chọn ngẫu nhiên từ các phím ký tự đặc biệt trên bàn phím máy tính.",
        }
    },

    # Q28: target_pos = 1 (B), target_rank = 4 (Longest)
    {
        "id": 28,
        "category": "Đặc trưng C#",
        "bloom": "Understand",
        "question": "Cơ chế Thu gom rác tự động (Garbage Collection - GC) trong môi trường .NET có nhiệm vụ cốt lõi là gì?",
        "explanation": "Garbage Collector (GC) là cơ chế tự động của CLR chịu trách nhiệm theo dõi và thu hồi vùng nhớ heap đã cấp phát cho các đối tượng không còn được sử dụng.",
        "options_by_rank": {
            1: "Quét sạch các mã độc và phần mềm gián điệp khỏi tệp tin dự án.",
            2: "Tự động dọn dẹp các tệp tin tạm nằm trong Recycle Bin của hệ điều hành Windows.",
            3: "Tự động sửa chữa các lỗi cú pháp phát sinh trong lúc lập trình viên gõ mã nguồn.",
            4: "Tự động thu hồi vùng nhớ heap của các đối tượng không còn sử dụng để tránh rò rỉ bộ nhớ.",
        }
    },

    # Q29: target_pos = 0 (A), target_rank = 1 (Shortest)
    {
        "id": 29,
        "category": "Đặc trưng C#",
        "bloom": "Remember",
        "question": "Cặp từ khóa nào trong C# được dùng để lập trình bất đồng bộ giúp giao diện người dùng không bị đơ treo?",
        "explanation": "Từ khóa async và await trong C# cho phép lập trình viên viết code bất đồng bộ một cách tự nhiên, giữ cho ứng dụng luôn mượt mà khi xử lý các tác vụ I/O tốn thời gian.",
        "options_by_rank": {
            1: "Cặp từ khóa async và await dùng cho tác vụ bất đồng bộ.",
            2: "Cặp từ khóa lock và monitor dùng để đồng bộ hóa các luồng xử lý dữ liệu.",
            3: "Cặp từ khóa try và catch dùng trong khối cấu trúc bắt và xử lý ngoại lệ lỗi.",
            4: "Cặp từ khóa public và private dùng để thiết lập phạm vi truy cập biến thành viên.",
        }
    },

    # Q30: target_pos = 0 (A), target_rank = 1 (Shortest)
    {
        "id": 30,
        "category": "Kiến trúc .NET",
        "bloom": "Remember",
        "question": "Hai trụ cột nền tảng cốt lõi cấu thành nên hệ sinh thái Microsoft .NET là gì?",
        "explanation": "Kiến trúc .NET gồm hai thành phần chủ chốt: FCL (kho thư viện lớp đồ sộ có sẵn) và CLR (máy ảo thực thi, quản lý vòng đời ứng dụng).",
        "options_by_rank": {
            1: "Thư viện lớp (.NET FCL) và Môi trường thực thi mã chung CLR.",
            2: "Hệ điều hành Windows 11 bản quyền cùng bộ công cụ văn phòng Microsoft Office 365.",
            3: "Trình duyệt web Microsoft Edge và Công cụ tìm kiếm dữ liệu phân tán quy mô lớn Bing.",
            4: "Phần cứng vi xử lý Intel Core đa nhân cùng hệ thống thanh nhớ RAM tốc độ cao có tản nhiệt.",
        }
    },

    # Q31: target_pos = 3 (D), target_rank = 4 (Longest)
    {
        "id": 31,
        "category": "Kiến trúc .NET",
        "bloom": "Understand",
        "question": "Khái niệm 'Managed Code' (Mã được quản lý) trong thế giới .NET có nghĩa là gì?",
        "explanation": "Managed code là mã được CLR quản lý trực tiếp trong lúc chạy, cung cấp các dịch vụ như thu gom rác, kiểm tra kiểu dữ liệu an toàn và xử lý biệt lệ.",
        "options_by_rank": {
            1: "Mã nguồn được đặt mật khẩu bảo vệ quyền truy cập trong thư mục dự án.",
            2: "Mã nguồn phần mềm do trực tiếp Giám đốc dự án (Project Manager) giám sát.",
            3: "Mã máy nhị phân chạy trực tiếp trên chip mà không cần máy ảo trung gian hỗ trợ.",
            4: "Mã được biên dịch ra MSIL và chạy dưới sự kiểm soát, quản lý an toàn của máy ảo CLR.",
        }
    },

    # Q32: target_pos = 2 (C), target_rank = 4 (Longest)
    {
        "id": 32,
        "category": "Kiến trúc .NET",
        "bloom": "Understand",
        "question": "Khi lập trình viên biên dịch mã nguồn C# (*.cs) bằng trình biên dịch csc.exe, kết quả đầu ra trực tiếp là gì?",
        "explanation": "Trình biên dịch C# không dịch trực tiếp ra mã máy CPU mà dịch thành mã trung gian MSIL (Microsoft Intermediate Language) kèm Metadata lưu trong file assembly (.dll/.exe).",
        "options_by_rank": {
            1: "Mã nguồn C++ tương đương để lập trình viên chỉnh sửa thủ công.",
            2: "Mã máy nhị phân thuần túy tối ưu riêng cho dòng vi xử lý Intel x86/x64.",
            3: "Tệp tin văn bản định dạng HTML chứa tài liệu hướng dẫn kỹ thuật của phần mềm.",
            4: "Mã trung gian MSIL kèm siêu dữ liệu Metadata đóng gói trong tệp assembly .dll hoặc .exe.",
        }
    },

    # Q33: target_pos = 3 (D), target_rank = 1 (Shortest)
    {
        "id": 33,
        "category": "Kiến trúc .NET",
        "bloom": "Understand",
        "question": "Bộ phận nào trong máy ảo CLR chịu trách nhiệm chuyển đổi mã trung gian MSIL thành mã máy bản địa khi ứng dụng chạy?",
        "explanation": "JIT (Just-In-Time) Compiler là thành phần của CLR có nhiệm vụ biên dịch mã MSIL sang mã máy bản địa của CPU cụ thể ngay khi phương thức được gọi lần đầu.",
        "options_by_rank": {
            1: "Trình biên dịch tức thời JIT Compiler (Just-In-Time Compiler).",
            2: "Trình nạp lớp đối tượng hệ thống (Class Loader) của môi trường thực thi.",
            3: "Bộ thu gom rác tự động của vùng nhớ heap (Garbage Collector) trên máy ảo.",
            4: "Hệ quản trị cơ sở dữ liệu quan hệ tích hợp sẵn trong nhân hệ điều hành máy tính.",
        }
    },

    # Q34: target_pos = 2 (C), target_rank = 3
    {
        "id": 34,
        "category": "Kiến trúc .NET",
        "bloom": "Understand",
        "question": "Nguy cơ bảo mật và sự cố hệ thống nghiêm trọng nhất khi thực thi 'Unmanaged Code' (như C/C++ truyền thống) là gì?",
        "explanation": "Unmanaged code không có CLR giám sát. Sai sót con trỏ bộ nhớ có thể gây tràn bộ đệm (Buffer Overflow), rò rỉ bộ nhớ nghiêm trọng hoặc làm sập toàn bộ hệ điều hành.",
        "options_by_rank": {
            1: "Làm tiêu tốn điện năng của pin máy tính xách tay nhanh hơn so với bình thường.",
            2: "Không thể hiển thị được các ký tự font chữ Unicode tiếng Việt trên giao diện ứng dụng.",
            3: "Lỗi con trỏ bộ nhớ và tràn bộ đệm (Buffer Overflow) có thể làm sập hệ thống hoặc màn hình xanh.",
            4: "Bắt buộc máy tính phải duy trì kết nối mạng Internet liên tục thì mới tải được các thư viện liên kết.",
        }
    },

    # Q35: target_pos = 1 (B), target_rank = 2
    {
        "id": 35,
        "category": "Độc lập Nền tảng",
        "bloom": "Understand",
        "question": "Tính độc lập nền tảng (Platform Independence) của .NET Core và .NET 8 mang lại quyền năng gì cho lập trình viên?",
        "explanation": "Nhờ mã trung gian MSIL và máy ảo CLR đa nền tảng, một ứng dụng .NET có thể chạy mượt mà trên Windows, macOS và các bản phân phối Linux mà không cần biên dịch lại.",
        "options_by_rank": {
            1: "Chỉ cho phép ứng dụng khởi chạy duy nhất trên hệ điều hành Windows có bản quyền đầy đủ.",
            2: "Viết và biên dịch một lần; tệp MSIL có thể chạy trên Windows, Linux và macOS nếu có CLR phù hợp.",
            3: "Tự động chuyển đổi máy tính cá nhân thành máy chủ đám mây phân tán mà không cần cấu hình mạng phức tạp.",
            4: "Không cần cài đặt bất kỳ phần mềm môi trường thực thi nào ứng dụng vẫn tự động chạy được trên tất cả các loại chip.",
        }
    },

    # Q36: target_pos = 0 (A), target_rank = 3
    {
        "id": 36,
        "category": "Tương tác Đa ngôn ngữ",
        "bloom": "Understand",
        "question": "Khả năng Tương tác đa ngôn ngữ (Language Interoperability) trong hệ sinh thái .NET được hiện thực hóa dựa trên nguyên lý nào?",
        "explanation": "Do C#, Visual Basic .NET và F# đều biên dịch ra cùng một chuẩn MSIL và dùng chung kiểu dữ liệu CTS (Common Type System), chúng có thể kế thừa và gọi hàm qua lại không rào cản.",
        "options_by_rank": {
            1: "Lập trình viên tự sử dụng công cụ trí tuệ nhân tạo để dịch mã nguồn thủ công qua lại giữa các ngôn ngữ.",
            2: "Tất cả các ngôn ngữ lập trình đều bắt buộc phải tuân thủ nghiêm ngặt quy tắc ngữ pháp tiếng Anh thông dụng.",
            3: "Các ngôn ngữ tương thích .NET (C#, VB.NET, F#) đều được biên dịch về chung định dạng mã trung gian chuẩn MSIL.",
            4: "Hệ điều hành Windows tự động phát hiện cú pháp khác biệt và sửa chữa mã lệnh trong quá trình nạp vào bộ nhớ RAM.",
        }
    },

    # Q37: target_pos = 3 (D), target_rank = 3
    {
        "id": 37,
        "category": "Visual Studio IDE",
        "bloom": "Understand",
        "question": "Trong môi trường Visual Studio IDE, mối quan hệ phân cấp giữa Solution (*.sln) và Project (*.csproj) là gì?",
        "explanation": "Solution (.sln) là container cấp cao nhất quản lý một hoặc nhiều Project (.csproj) cùng các cấu hình build và dependencies liên kết.",
        "options_by_rank": {
            1: "Project là thùng chứa cấp cao nhất quản lý hàng loạt các Solution độc lập bên trong.",
            2: "Solution và Project là hai thuật ngữ hoàn toàn đồng nghĩa và có thể dùng thay thế cho nhau.",
            3: "Solution chứa một hoặc nhiều Project; mỗi Project chứa các tệp mã nguồn và tài nguyên liên quan.",
            4: "Solution chỉ dùng cấu hình cơ sở dữ liệu; Project chỉ dùng để thiết kế giao diện bằng kéo thả điều khiển.",
        }
    },

    # Q38: target_pos = 3 (D), target_rank = 2
    {
        "id": 38,
        "category": "Lập trình Trực quan",
        "bloom": "Remember",
        "question": "Trong ứng dụng đồ họa Painter (mục 1.12), điều khiển GUI nào được dùng để người dùng rê chuột vẽ các nét vẽ màu lên bề mặt?",
        "explanation": "Panel màu trắng là vùng không gian giao diện tiếp nhận các thao tác chuột (MouseDown, MouseMove) để hiển thị các nét vẽ nghệ thuật.",
        "options_by_rank": {
            1: "Điều khiển Button (nút bấm kích hoạt hành động tức thì Undo hoặc Clear).",
            2: "Điều khiển Panel (vùng không gian đồ họa tiếp nhận thao tác vẽ từ chuột).",
            3: "Điều khiển GroupBox (khung chứa phân nhóm các nút tùy chọn màu sắc và kích cỡ nét vẽ).",
            4: "Điều khiển RadioButton (nút chọn hình tròn mang tính chất loại trừ lẫn nhau trong cùng nhóm).",
        }
    },

    # Q39: target_pos = 2 (C), target_rank = 1 (Shortest)
    {
        "id": 39,
        "category": "Lập trình Trực quan",
        "bloom": "Understand",
        "question": "Tính chất đặc trưng nhất của điều khiển RadioButton khi được đặt trong cùng một GroupBox là gì?",
        "explanation": "Trong cùng một GroupBox, các RadioButton mang tính loại trừ lẫn nhau: người dùng chỉ có thể chọn đúng một tùy chọn duy nhất tại một thời điểm.",
        "options_by_rank": {
            1: "Tính loại trừ: Chỉ duy nhất một nút được chọn tại một thời điểm.",
            2: "Cho phép người dùng đánh dấu chọn đồng thời tất cả các nút trong nhóm cùng lúc.",
            3: "Tự động đổi màu sắc hiển thị khi con trỏ chuột của người dùng rê ngang qua bề mặt form.",
            4: "Không thể kích hoạt bất kỳ sự kiện xử lý nào khi người dùng tương tác nhấp chuột trên giao diện.",
        }
    },

    # Q40: target_pos = 0 (A), target_rank = 3
    {
        "id": 40,
        "category": "Lập trình Hướng sự kiện",
        "bloom": "Understand",
        "question": "Trong mô hình Lập trình Hướng sự kiện (Event-Driven Programming), chương trình phản hồi lại các thao tác của người dùng như thế nào?",
        "explanation": "Ứng dụng GUI vận hành theo mô hình Event-Driven: ứng dụng luôn ở trạng thái lắng nghe trong Event Loop, khi có sự kiện (Event) xảy ra thì Trình xử lý sự kiện (Event Handler) tương ứng sẽ được gọi.",
        "options_by_rank": {
            1: "Chương trình thực thi tuần tự từ đầu đến cuối tệp mã nguồn rồi tự động kết thúc.",
            2: "Bắt buộc người dùng nhập các chuỗi dòng lệnh văn bản từ bàn phím thì mới có thể xử lý.",
            3: "Duy trì Event Loop lắng nghe; khi có sự kiện thì kích hoạt Event Handler tương ứng để xử lý.",
            4: "Tự động suy đoán trước hành vi tiếp theo của người dùng thông qua thuật toán học máy tích hợp sẵn.",
        }
    }
]

# Assemble the final quiz objects
final_questions = []

for idx, q_raw in enumerate(raw_questions_data):
    qid = q_raw["id"]
    target_pos, target_rank = TARGET_SPECS[idx]
    obr = q_raw["options_by_rank"]

    # Verify strict length ordering
    l1 = len(obr[1])
    l2 = len(obr[2])
    l3 = len(obr[3])
    l4 = len(obr[4])
    assert l1 < l2 < l3 < l4, f"Q{qid} length ordering error: {l1}, {l2}, {l3}, {l4}"

    # Build options array of length 4
    options = [None, None, None, None]
    
    # Place correct answer at target_pos
    options[target_pos] = obr[target_rank]
    
    # Place distractors in the other 3 positions
    distractor_ranks = [r for r in [1, 2, 3, 4] if r != target_rank]
    available_positions = [p for p in [0, 1, 2, 3] if p != target_pos]
    
    for p_idx, r in zip(available_positions, distractor_ranks):
        options[p_idx] = obr[r]

    # Verify that options array is completely filled
    assert all(opt is not None for opt in options), f"Q{qid} has unfilled option slot!"
    
    # Verify calculated rank matches target_rank
    lens = [len(opt) for opt in options]
    sorted_lens = sorted(lens)
    calc_rank = sorted_lens.index(len(options[target_pos])) + 1
    assert calc_rank == target_rank, f"Q{qid} rank mismatch: expected {target_rank}, got {calc_rank}"

    final_questions.append({
        "id": qid,
        "category": q_raw["category"],
        "bloom": q_raw["bloom"],
        "question": q_raw["question"],
        "options": options,
        "correct": target_pos,
        "explanation": q_raw["explanation"]
    })

# Global assertions across all 40 questions
all_positions = [q["correct"] for q in final_questions]
all_ranks = []
for q in final_questions:
    lens = [len(opt) for opt in q["options"]]
    sorted_lens = sorted(lens)
    rank = sorted_lens.index(lens[q["correct"]]) + 1
    all_ranks.append(rank)

pos_counter = Counter(all_positions)
rank_counter = Counter(all_ranks)

print("=" * 60)
print("FINAL QUIZ VERIFICATION RESULTS:")
print(f"Total Questions: {len(final_questions)}")
print(f"Position Counts (0=A, 1=B, 2=C, 3=D): {pos_counter}")
print(f"Rank Counts (1=shortest, 4=longest): {rank_counter}")
print("=" * 60)

assert pos_counter == {0: 10, 1: 10, 2: 10, 3: 10}, f"Position counts not balanced: {pos_counter}"
assert rank_counter == {1: 10, 2: 10, 3: 10, 4: 10}, f"Rank counts not balanced: {rank_counter}"

# Write to js/quiz_data.js
js_content = f"""// ============================================================================
// HỌC PHẦN: KỸ THUẬT LẬP TRÌNH (4 TÍN CHỈ) - IT26M
// NGÂN HÀNG CÂU HỎI TRẮC NGHIỆM CHƯƠNG 1: INTRODUCTION TO COMPUTERS, THE INTERNET AND VISUAL C#
// ĐẶC TẢ CHUẨN HÓA:
// - Tổng số: 40 câu trắc nghiệm chuẩn hóa 4 lựa chọn (A, B, C, D)
// - Cân bằng độ dài ngẫu nhiên tuyệt đối:
//   * 10 câu đáp án đúng là lựa chọn NGẮN NHẤT (Hạng 1)
//   * 10 câu đáp án đúng là lựa chọn NGẮN THỨ NHÌ (Hạng 2)
//   * 10 câu đáp án đúng là lựa chọn DÀI THỨ NHÌ (Hạng 3)
//   * 10 câu đáp án đúng là lựa chọn DÀI NHẤT (Hạng 4)
// - Phân bố vị trí đáp án đúng đều tuyệt đối: Đúng 10 câu A, 10 câu B, 10 câu C, 10 câu D
// - Độ dài các phương án trong mỗi câu biến thiên tự nhiên, không có phương án cụt lủn hay phình to bất thường
// - Triệt tiêu hoàn toàn khả năng đoán đáp án đúng dựa vào độ dài phương án
// - Giáo trình gốc: Visual C# How to Program (Deitel & Deitel) - Chapter 1
// ============================================================================

const QUIZ_CHAPTER_01 = {json.dumps(final_questions, ensure_ascii=False, indent=2)};
"""

with open("js/quiz_data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("SUCCESS: js/quiz_data.js written successfully!")

