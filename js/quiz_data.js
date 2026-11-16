// ============================================================================
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

const QUIZ_CHAPTER_01 = [
  {
    "id": 1,
    "category": "Nền tảng Tính toán",
    "bloom": "Remember",
    "question": "Máy tính xử lý dữ liệu dưới sự điều khiển của các chuỗi chỉ thị được gọi là gì?",
    "options": [
      "Hệ thống các tệp tin dữ liệu nhị phân lưu trữ trên các đĩa từ tính.",
      "Các vi mạch bán dẫn phần cứng tích hợp chuyên dụng gắn cố định trên bo mạch chủ.",
      "Chương trình máy tính (hay các phần mềm hệ thống và ứng dụng / Programs).",
      "Các thanh ghi lưu trữ trạng thái phần cứng được thiết kế bên trong đế chip vi xử lý."
    ],
    "correct": 2,
    "explanation": "Theo mục 1.3 giáo trình Deitel: Máy tính xử lý dữ liệu dưới sự điều khiển của các chuỗi chỉ thị gọi là chương trình máy tính (computer programs) hay phần mềm (software)."
  },
  {
    "id": 2,
    "category": "Phần cứng Máy tính",
    "bloom": "Understand",
    "question": "Nội dung cốt lõi của Định luật Gordon Moore (đồng sáng lập Intel, 1965) là gì?",
    "options": [
      "Dung lượng bộ nhớ RAM máy tính cá nhân sẽ tăng gấp 4 lần sau mỗi chu kỳ 5 năm phát triển công nghệ.",
      "Tốc độ truyền dữ liệu của mạng Internet toàn cầu tăng gấp đôi sau mỗi 12 tháng nhờ mở rộng mạng cáp quang.",
      "Số lượng bóng bán dẫn trên vi mạch tăng gấp đôi xấp xỉ sau mỗi 18-24 tháng với chi phí không đổi.",
      "Giá thành sản xuất vi mạch xử lý máy tính sẽ giảm đi một nửa sau mỗi chu kỳ ba năm hoạt động trên thị trường."
    ],
    "correct": 2,
    "explanation": "Định luật Moore (mục 1.3.1): Số lượng bóng bán dẫn trên các vi mạch tích hợp tăng gấp đôi xấp xỉ sau mỗi 18-24 tháng trong khi chi phí sản xuất giữ nguyên, giúp máy tính ngày càng mạnh mẽ và rẻ hơn."
  },
  {
    "id": 3,
    "category": "Kiến trúc Máy tính",
    "bloom": "Remember",
    "question": "Theo cách phân loại kiến trúc logic của giáo trình Deitel, máy tính được chia thành mấy khối chức năng logic?",
    "options": [
      "4 khối phần cứng cơ bản của máy tính cá nhân gồm màn hình hiển thị, chuột, bàn phím và CPU.",
      "3 khối xử lý tổng quát bao gồm khối tiếp nhận dữ liệu, khối xử lý trung tâm và khối xuất thông tin.",
      "8 khối chức năng bao gồm bộ giải mã lệnh, bus truyền dẫn, thanh ghi cache cùng các cổng kết nối ngoại vi.",
      "6 khối chức năng logic (Input, Output, Memory, ALU, CPU, Secondary Storage)."
    ],
    "correct": 3,
    "explanation": "Mục 1.3.2 phân loại máy tính thành 6 khối chức năng logic: Input unit, Output unit, Memory unit, ALU, CPU, Secondary storage unit."
  },
  {
    "id": 4,
    "category": "Kiến trúc Máy tính",
    "bloom": "Understand",
    "question": "Khối chức năng logic nào trực tiếp thực hiện các phép tính số học và so sánh logic (A > B)?",
    "options": [
      "Khối điều khiển trung tâm (Control Unit - CU) điều phối hệ thống.",
      "Bộ nhớ chính tạm thời (Memory Unit / RAM) lưu trữ lệnh và biến số.",
      "Bộ nhớ thứ cấp (Secondary Storage Unit) lưu trữ tệp tin nhị phân lâu dài trên các ổ đĩa.",
      "Đơn vị số học và logic (Arithmetic and Logic Unit - ALU) tính toán số học và so sánh."
    ],
    "correct": 3,
    "explanation": "ALU (Arithmetic and Logic Unit) là bộ phận trực tiếp thực hiện mọi phép tính toán số học cơ bản (+, -, *, /) và các phép so sánh logic (==, >, <)."
  },
  {
    "id": 5,
    "category": "Kiến trúc Máy tính",
    "bloom": "Understand",
    "question": "Đặc tính kỹ thuật quan trọng nhất của Bộ nhớ chính (Memory unit / RAM) mà lập trình viên cần ghi nhớ là gì?",
    "options": [
      "Dữ liệu được lưu trữ vĩnh viễn trên các phiến đĩa từ và không bao giờ bị mất đi khi mất điện.",
      "Dữ liệu mang tính khả biến (volatile), sẽ mất hoàn toàn khi bị ngắt nguồn điện.",
      "Tốc độ truy xuất chậm hơn ổ cứng hàng nghìn lần nên CPU chỉ truy cập khi hệ thống cạn kiệt bộ nhớ ảo.",
      "Chỉ cho phép đọc dữ liệu nhị phân mà tuyệt đối không hỗ trợ ghi đè hay cập nhật giá trị mới của chương trình."
    ],
    "correct": 1,
    "explanation": "Bộ nhớ chính RAM có tốc độ truy xuất cực nhanh nhưng là bộ nhớ khả biến (volatile), dữ liệu lưu trữ trên RAM sẽ biến mất hoàn toàn khi tắt máy."
  },
  {
    "id": 6,
    "category": "Kiến trúc Máy tính",
    "bloom": "Understand",
    "question": "Tại sao trong kiến trúc máy tính, CPU không xử lý dữ liệu trực tiếp trên ổ cứng mà phải nạp vào RAM?",
    "options": [
      "Do kiến trúc phần cứng của CPU và ổ đĩa cứng xung đột chuẩn mã nhị phân.",
      "Do ổ cứng chỉ hỗ trợ lưu trữ tệp tin văn bản mà không thể chứa mã máy thực thi.",
      "Do hệ điều hành Windows ngăn cấm CPU thực hiện đọc trực tiếp từ các cung từ ổ đĩa.",
      "Vì RAM truy xuất nhanh hơn ổ cứng hàng nghìn lần, giúp cung cấp dữ liệu kịp thời cho CPU."
    ],
    "correct": 3,
    "explanation": "Sự chênh lệch tốc độ giữa RAM và bộ nhớ thứ cấp (SSD/HDD) lên tới hàng nghìn lần. Nạp dữ liệu vào RAM giúp CPU luôn được cung cấp dữ liệu ở tốc độ cao nhất của bus hệ thống."
  },
  {
    "id": 7,
    "category": "Phần cứng Máy tính",
    "bloom": "Remember",
    "question": "Một bộ vi xử lý đa nhân (multicore processor) có cấu trúc đặc trưng như thế nào?",
    "options": [
      "Tích hợp hai hoặc nhiều nhân vi xử lý hoàn chỉnh (CPUs) trên cùng một vi mạch bán dẫn duy nhất.",
      "Chỉ sở hữu một nhân CPU duy nhất nhưng tăng gấp đôi tốc độ xung nhịp thạch anh hệ thống.",
      "Sử dụng hai thanh RAM độc lập gắn trên bo mạch chủ nhằm tăng tốc độ truyền tải bus dữ liệu trung tâm.",
      "Ghép nối nhiều thùng máy tính vật lý với nhau thông qua mạng nội bộ để chia sẻ tác vụ tính toán phân tán."
    ],
    "correct": 0,
    "explanation": "Giáo trình định nghĩa: Bộ vi xử lý đa nhân tích hợp hai hoặc nhiều nhân xử lý (CPUs) trên cùng một đế chip bán dẫn (ví dụ dual-core có 2 CPU, quad-core có 4 CPU)."
  },
  {
    "id": 8,
    "category": "Kiến trúc Máy tính",
    "bloom": "Understand",
    "question": "Vai trò của Bộ nhớ thứ cấp (Secondary Storage Unit) trong hệ thống tính toán là gì?",
    "options": [
      "Trực tiếp thực hiện các phép nhân chia số thực dấu phẩy động của CPU.",
      "Chuyển đổi tín hiệu analog sang digital để phục vụ kết xuất âm thanh loa.",
      "Lưu trữ dữ liệu dung lượng lớn, bền vững (persistent) ngay cả khi mất nguồn điện.",
      "Đóng vai trò làm bộ tạo xung nhịp đồng hồ điều phối chu kỳ xử lý của toàn bộ bo mạch chủ máy tính."
    ],
    "correct": 2,
    "explanation": "Secondary Storage (SSD, HDD, USB) là bộ lưu trữ bất biến (persistent), dung lượng cao và chi phí thấp trên mỗi byte, giữ dữ liệu lâu dài khi tắt máy."
  },
  {
    "id": 9,
    "category": "Phân cấp Dữ liệu",
    "bloom": "Remember",
    "question": "Đơn vị dữ liệu nhỏ nhất trong máy tính, chỉ có thể mang giá trị 0 hoặc 1, được gọi là gì?",
    "options": [
      "Ký tự mã hóa nhị phân chuẩn định dạng văn bản ký tự ASCII.",
      "Bit (viết tắt của Binary Digit, biểu diễn chữ số nhị phân 0 hoặc 1).",
      "Trường dữ liệu đơn vị chứa một nhóm ký tự mang ý nghĩa hoàn chỉnh (Field).",
      "Byte dữ liệu tiêu chuẩn được cấu thành từ chuỗi liên tiếp gồm đúng 8 bits nhị phân."
    ],
    "correct": 1,
    "explanation": "Bit (viết tắt của Binary Digit) là đơn vị thông tin nhỏ nhất, mang giá trị 0 hoặc 1."
  },
  {
    "id": 10,
    "category": "Phân cấp Dữ liệu",
    "bloom": "Understand",
    "question": "Thứ tự sắp xếp đúng từ đơn giản nhất đến phức tạp nhất trong Cấu trúc phân cấp dữ liệu là gì?",
    "options": [
      "Bit -> Byte (Character) -> Field -> Record -> File -> Database.",
      "Bit -> Field -> Byte -> Record -> File -> Hệ cơ sở dữ liệu quan hệ hoàn chỉnh.",
      "Byte -> Bit -> Record -> Field -> File -> Database quản trị dữ liệu quy mô lớn.",
      "Record -> Field -> File -> Byte -> Bit -> Hệ thống kho dữ liệu phân tán đám mây."
    ],
    "correct": 0,
    "explanation": "Theo Hình 1.3: Cấu trúc phân cấp dữ liệu chuẩn: Bit -> Byte (Ký tự) -> Field (Trường) -> Record (Bản ghi) -> File (Tệp) -> Database (Cơ sở dữ liệu) -> Big Data."
  },
  {
    "id": 11,
    "category": "Phân cấp Dữ liệu",
    "bloom": "Understand",
    "question": "Một Byte gồm bao nhiêu bits và có thể biểu diễn được bao nhiêu trạng thái phân biệt?",
    "options": [
      "Gồm đúng 4 bits nhị phân và mã hóa được 16 giá trị trạng thái tín hiệu.",
      "Gồm đúng 8 bits nhị phân và biểu diễn được 256 trạng thái khác nhau (từ 0 đến 255).",
      "Gồm đúng 10 bits nhị phân và mã hóa được 1024 trạng thái lưu trữ bus dữ liệu.",
      "Gồm đúng 16 bits mở rộng cho phép biểu diễn tới 65.536 ký tự đa ngôn ngữ chuẩn Unicode."
    ],
    "correct": 1,
    "explanation": "1 Byte = 8 bits. Số trạng thái tối đa là 2^8 = 256 giá trị riêng biệt, đủ để mã hóa bảng ký tự ASCII chuẩn."
  },
  {
    "id": 12,
    "category": "Phân cấp Dữ liệu",
    "bloom": "Apply",
    "question": "Trong phân cấp dữ liệu, tập hợp các trường như Mã SV, Họ tên, Điểm thi của cùng một sinh viên được gọi là gì?",
    "options": [
      "Một trường dữ liệu đơn vị (Field) của cơ sở dữ liệu.",
      "Một Bản ghi (Record) chứa tập hợp các trường thông tin có liên quan về một đối tượng.",
      "Một tệp tin nhị phân có cấu trúc (Structured File) trên ổ cứng.",
      "Một cơ sở dữ liệu quan hệ gồm nhiều bảng dữ liệu liên kết với nhau."
    ],
    "correct": 1,
    "explanation": "Record (Bản ghi) là tập hợp các trường thông tin có liên quan mật thiết về một thực thể hoặc đối tượng cụ thể."
  },
  {
    "id": 13,
    "category": "Đo lường Dữ liệu",
    "bloom": "Remember",
    "question": "Theo quy ước khoa học máy tính (hệ nhị phân), 1 Megabyte (MB) bằng bao nhiêu Kilobytes (KB)?",
    "options": [
      "Bằng đúng 1024 Kilobytes (KB) theo quy chuẩn tính lũy thừa nhị phân 2 mũ 10.",
      "Bằng đúng 512 Kilobytes (KB) theo phân bổ khối bộ nhớ đệm.",
      "Bằng đúng 1000 Kilobytes (KB) theo quy tắc làm tròn hệ thập phân.",
      "Bằng đúng 2048 Kilobytes (KB) theo quy chuẩn phân chia dung lượng của bộ nhớ kênh đôi RAM."
    ],
    "correct": 0,
    "explanation": "Trong hệ nhị phân, các đơn vị tăng theo lũy thừa 2^10 = 1024. Do đó 1 MB = 1024 KB = 1.048.576 Bytes."
  },
  {
    "id": 14,
    "category": "Đo lường Dữ liệu",
    "bloom": "Understand",
    "question": "Thứ tự tăng dần chuẩn xác của các đơn vị đo lường dung lượng dữ liệu trên máy tính là:",
    "options": [
      "Byte < KB < MB < TB < GB < PB (đặt sai thứ tự TB và GB).",
      "Byte < KB < MB < GB < TB < PB < EB < ZB < YB (sắp xếp hoàn toàn chính xác).",
      "Byte < KB < GB < MB < TB < PB (đặt sai thứ tự giữa GB và MB).",
      "Byte < KB < MB < GB < TB < PB < ZB < EB < YB (đặt sai thứ tự ZB và EB)."
    ],
    "correct": 1,
    "explanation": "Bảng Hình 1.4 giáo trình Deitel: Kilobyte (KB) < Megabyte (MB) < Gigabyte (GB) < Terabyte (TB) < Petabyte (PB) < Exabyte (EB) < Zettabyte (ZB) < Yottabyte (YB)."
  },
  {
    "id": 15,
    "category": "Tiến hóa Ngôn ngữ",
    "bloom": "Remember",
    "question": "Ngôn ngữ duy nhất mà phần cứng máy tính (CPU) trực tiếp hiểu và thực thi không qua chương trình dịch là gì?",
    "options": [
      "Hợp ngữ (Assembly Language) sử dụng các mã lệnh viết tắt gợi nhớ thao tác.",
      "Ngôn ngữ C++ biên dịch với cờ tối ưu hóa phần cứng ở mức cao nhất của trình dịch.",
      "Ngôn ngữ máy (Machine Language) bao gồm các chuỗi nhị phân gồm chữ số 0 và 1.",
      "Mã trung gian chuẩn ECMA được thực thi độc lập trên mọi loại kiến trúc vi xử lý hiện đại."
    ],
    "correct": 2,
    "explanation": "Ngôn ngữ máy (Machine Language) gồm các chuỗi nhị phân 0 và 1 là ngôn ngữ 'bản địa' duy nhất mà mạch điện CPU hiểu và thực thi trực tiếp."
  },
  {
    "id": 16,
    "category": "Tiến hóa Ngôn ngữ",
    "bloom": "Understand",
    "question": "Hợp ngữ (Assembly Language) sử dụng các từ viết tắt tiếng Anh mang tính gợi nhớ (như LOAD, ADD, STORE) được gọi là gì?",
    "options": [
      "Keywords (các từ khóa cú pháp dành riêng của ngôn ngữ lập trình).",
      "Variables (các biến số lưu trữ giá trị tạm thời trong vùng nhớ RAM).",
      "Mnemonics (các từ viết tắt mang tính gợi nhớ đại diện cho chỉ thị phần cứng máy tính).",
      "Directives (các chỉ thị tiền xử lý dùng để cấu hình trình biên dịch)."
    ],
    "correct": 2,
    "explanation": "Hợp ngữ sử dụng các từ viết tắt gợi nhớ gọi là mnemonics để đại diện cho các chỉ thị máy nguyên thủy."
  },
  {
    "id": 17,
    "category": "Biên dịch & Thông dịch",
    "bloom": "Understand",
    "question": "Điểm khác biệt cốt lõi giữa Trình biên dịch (Compiler) và Trình thông dịch (Interpreter) là gì?",
    "options": [
      "Compiler dịch toàn bộ mã sang mã máy trước khi chạy; Interpreter dịch và thực thi từng dòng.",
      "Compiler chỉ dùng cho web; Interpreter chỉ dùng cho phát triển hệ thống.",
      "Compiler không tạo file chạy; Interpreter luôn tạo tệp tin thực thi .exe độc lập.",
      "Compiler chỉ kiểm tra lỗi logic hệ thống; Interpreter chỉ kiểm tra lỗi cú pháp biên dịch."
    ],
    "correct": 0,
    "explanation": "Compiler biên dịch trọn vẹn chương trình ra mã máy trước khi chạy (tốc độ cao). Interpreter dịch và chạy từng dòng lệnh một (linh hoạt nhưng chậm hơn)."
  },
  {
    "id": 18,
    "category": "Biên dịch & Thông dịch",
    "bloom": "Understand",
    "question": "Cơ chế thực thi của ngôn ngữ C# và nền tảng .NET là gì?",
    "options": [
      "Thuần túy thông dịch từng dòng lệnh mã nguồn C# mỗi khi người dùng khởi chạy ứng dụng.",
      "Cơ chế lai (Hybrid): Dịch ra mã MSIL trước, sau đó JIT Compiler dịch sang mã máy khi chạy.",
      "Thuần túy biên dịch trực tiếp ra mã máy nhị phân bản địa của CPU tương tự như ngôn ngữ C/C++.",
      "Chuyển đổi trực tiếp mã nguồn C# thành mã kịch bản JavaScript để thực thi trong trình duyệt web."
    ],
    "correct": 1,
    "explanation": "C# kết hợp ưu điểm của cả hai: Biên dịch trước ra MSIL (độc lập nền tảng) và dùng JIT (Just-In-Time) Compiler biên dịch sang mã máy tại thời điểm thực thi."
  },
  {
    "id": 19,
    "category": "Tiến hóa Ngôn ngữ",
    "bloom": "Understand",
    "question": "Chương trình dùng để chuyển đổi mã hợp ngữ (Assembly) sang mã máy (Machine language) được gọi là gì?",
    "options": [
      "Debugger (công cụ hỗ trợ theo dõi và gỡ lỗi phần mềm máy tính).",
      "Loader (trình nạp mã chương trình vào RAM để chuẩn bị thực thi).",
      "Linker (trình liên kết các tệp tin đối tượng nhị phân thành tệp chương trình thực thi).",
      "Assembler (trình hợp dịch chuyên trách dịch mã hợp ngữ sang chuỗi mã máy)."
    ],
    "correct": 3,
    "explanation": "Assembler (trình hợp dịch) là phần mềm chuyên trách dịch các chỉ thị hợp ngữ (Assembly) thành mã máy tương ứng."
  },
  {
    "id": 20,
    "category": "Công nghệ Đối tượng",
    "bloom": "Understand",
    "question": "Trong Lập trình hướng đối tượng (OOP), sự khác biệt cơ bản giữa Thuộc tính (Attributes) và Hành vi (Behaviors) là gì?",
    "options": [
      "Thuộc tính là các hằng số bất biến; Hành vi là các biến số thay đổi theo thời gian chạy.",
      "Thuộc tính mô tả trạng thái dữ liệu; Hành vi là thao tác đối tượng thực hiện.",
      "Thuộc tính chỉ khai báo trên tài liệu thiết kế; Hành vi là mã nguồn viết trong tệp chương trình.",
      "Thuộc tính quyết định tốc độ xử lý phần cứng; Hành vi quyết định dung lượng bộ nhớ RAM mà đối tượng chiếm giữ."
    ],
    "correct": 1,
    "explanation": "Thuộc tính đại diện cho dữ liệu và trạng thái của đối tượng (ví dụ: màu sơn, số dư). Hành vi đại diện cho các hành động (ví dụ: tăng tốc, rút tiền) được hiện thực bằng phương thức."
  },
  {
    "id": 21,
    "category": "Công nghệ Đối tượng",
    "bloom": "Understand",
    "question": "Mối quan hệ chính xác giữa Lớp (Class) và Đối tượng (Object) trong ngôn ngữ C# là gì?",
    "options": [
      "Class và Object là hai khái niệm hoàn toàn đồng nghĩa trong ngôn ngữ C#.",
      "Class là bản vẽ mẫu thiết kế (blueprint); Object là thực thể cụ thể sinh ra từ Class.",
      "Object là bản thiết kế trên giấy còn Class là thực thể cụ thể sống trong RAM.",
      "Một Object có thể chứa đồng thời hàng trăm Class độc lập bên trong cấu trúc phân cấp kế thừa đa tầng."
    ],
    "correct": 1,
    "explanation": "Class là bản vẽ mẫu (blueprint). Từ một Class, ta có thể khởi tạo vô số đối tượng cụ thể (instances) bằng toán tử new."
  },
  {
    "id": 22,
    "category": "Công nghệ Đối tượng",
    "bloom": "Remember",
    "question": "Mục tiêu tối thượng hàng đầu của Lập trình hướng đối tượng (OOP) đối với ngành công nghiệp phần mềm là gì?",
    "options": [
      "Tiết kiệm dung lượng lưu trữ trên ổ đĩa cứng của máy tính bằng cách nén mã nguồn.",
      "Loại bỏ hoàn toàn sự can thiệp của con người trong khâu kiểm thử và phát hiện lỗi phần mềm.",
      "Tái sử dụng phần mềm (Software Reuse) để nâng cao chất lượng và năng suất.",
      "Bắt buộc người dùng cuối phải tương tác bằng dòng lệnh thay vì sử dụng giao diện đồ họa trực quan."
    ],
    "correct": 2,
    "explanation": "Tái sử dụng phần mềm (Software Reuse) là lợi ích kinh tế và kỹ thuật to lớn nhất của OOP, giúp tận dụng các lớp đã được kiểm thử để giảm thời gian phát triển."
  },
  {
    "id": 23,
    "category": "Công nghệ Đối tượng",
    "bloom": "Understand",
    "question": "Trụ cột Đóng gói (Encapsulation) trong công nghệ đối tượng mang lại lợi ích gì cho việc bảo vệ mã nguồn?",
    "options": [
      "Cho phép các chương trình bên ngoài truy cập và sửa đổi trực tiếp dữ liệu biến.",
      "Mở toàn bộ mã nguồn của các hàm thành viên cho tất cả thành viên trong nhóm dự án.",
      "Gom dữ liệu và phương thức vào lớp, che giấu chi tiết cài đặt để bảo vệ tính toàn vẹn dữ liệu.",
      "Tự động tăng tốc độ tính toán số học của vi xử lý lên gấp đôi khi chạy thuật toán đa luồng."
    ],
    "correct": 2,
    "explanation": "Đóng gói (Encapsulation) gom nhóm dữ liệu và hàm xử lý, đồng thời che giấu chi tiết cài đặt (information hiding) để bảo vệ tính toàn vẹn của đối tượng."
  },
  {
    "id": 24,
    "category": "Công nghệ Đối tượng",
    "bloom": "Understand",
    "question": "Trụ cột Kế thừa (Inheritance) trong lập trình C# có ý nghĩa kỹ thuật là gì?",
    "options": [
      "Tự động xóa bỏ lớp cha cũ khỏi bộ nhớ RAM để tiết kiệm không gian lưu trữ heap.",
      "Chuyển đổi kiểu dữ liệu của biến số từ kiểu số nguyên sang kiểu số thực dấu phẩy động chính xác cao.",
      "Sao chép thủ công toàn bộ mã nguồn giữa các tệp tin khác nhau trong cùng một dự án phần mềm ứng dụng C#.",
      "Tạo lớp mới từ lớp có sẵn, kế thừa thuộc tính và hành vi đồng thời bổ sung tính năng mới."
    ],
    "correct": 3,
    "explanation": "Kế thừa cho phép một lớp con (derived class) tiếp thu các thuộc tính và phương thức từ một lớp cha (base class) có sẵn, thúc đẩy tái sử dụng mã nguồn."
  },
  {
    "id": 25,
    "category": "Công nghệ Đối tượng",
    "bloom": "Apply",
    "question": "Trong cú pháp C#, câu lệnh nào sau đây dùng để khởi tạo một đối tượng mới từ lớp 'Car' trong bộ nhớ RAM?",
    "options": [
      "Car myCar = Car.CreateInstance();",
      "Car myCar = allocate Memory<Car>(\"VinFast\", \"Do\");",
      "Car myCar = construct Object.From(\"Car\", \"VF8\", \"Do\");",
      "Car myCar = new Car(\"VinFast VF8\", \"Do\");"
    ],
    "correct": 3,
    "explanation": "Toán tử new trong C# được sử dụng để cấp phát vùng nhớ trên Managed Heap cho một đối tượng mới và gọi phương thức khởi tạo (constructor)."
  },
  {
    "id": 26,
    "category": "Lịch sử C#",
    "bloom": "Remember",
    "question": "Ngôn ngữ C# được ra mắt vào năm nào, bởi tập đoàn nào và ai là kiến trúc sư trưởng chỉ huy thiết kế?",
    "options": [
      "Năm 2000, bởi tập đoàn Microsoft, do kiến trúc sư Anders Hejlsberg chỉ huy thiết kế.",
      "Năm 1995, bởi Sun Microsystems, do kiến trúc sư James Gosling thiết kế.",
      "Năm 1983, bởi Bell Laboratories, do nhà khoa học Bjarne Stroustrup sáng tạo.",
      "Năm 1991, bởi tổ chức mã nguồn mở Python Software Foundation phát triển toàn cầu."
    ],
    "correct": 0,
    "explanation": "C# được Microsoft công bố năm 2000 cùng sáng kiến .NET. Kiến trúc sư trưởng thiết kế C# là Anders Hejlsberg (người cũng thiết kế Turbo Pascal, Delphi, TypeScript)."
  },
  {
    "id": 27,
    "category": "Lịch sử C#",
    "bloom": "Understand",
    "question": "Nguồn gốc tên gọi 'C#' xuất phát từ ý nghĩa biểu tượng nào?",
    "options": [
      "Dấu thăng (#) trong âm nhạc thể hiện sự thăng tiến, và ghép từ 4 dấu cộng (++) của C++.",
      "Viết tắt từ cụm từ tiếng Anh 'Computer Sharp' biểu thị sự tinh tế của máy tính.",
      "Được đặt tên theo một câu lệnh điều khiển dòng đặc biệt xuất hiện trong hệ điều hành Unix.",
      "Do nhóm kỹ sư phần mềm lựa chọn ngẫu nhiên từ các phím ký tự đặc biệt trên bàn phím máy tính."
    ],
    "correct": 0,
    "explanation": "Dấu '#' mượn từ ký hiệu thăng trong âm nhạc biểu thị sự nâng cấp cao hơn, và được ghép từ 4 dấu '+' của C++ xếp lại, ngụ ý sự kế thừa và tiến hóa."
  },
  {
    "id": 28,
    "category": "Đặc trưng C#",
    "bloom": "Understand",
    "question": "Cơ chế Thu gom rác tự động (Garbage Collection - GC) trong môi trường .NET có nhiệm vụ cốt lõi là gì?",
    "options": [
      "Quét sạch các mã độc và phần mềm gián điệp khỏi tệp tin dự án.",
      "Tự động thu hồi vùng nhớ heap của các đối tượng không còn sử dụng để tránh rò rỉ bộ nhớ.",
      "Tự động dọn dẹp các tệp tin tạm nằm trong Recycle Bin của hệ điều hành Windows.",
      "Tự động sửa chữa các lỗi cú pháp phát sinh trong lúc lập trình viên gõ mã nguồn."
    ],
    "correct": 1,
    "explanation": "Garbage Collector (GC) là cơ chế tự động của CLR chịu trách nhiệm theo dõi và thu hồi vùng nhớ heap đã cấp phát cho các đối tượng không còn được sử dụng."
  },
  {
    "id": 29,
    "category": "Đặc trưng C#",
    "bloom": "Remember",
    "question": "Cặp từ khóa nào trong C# được dùng để lập trình bất đồng bộ giúp giao diện người dùng không bị đơ treo?",
    "options": [
      "Cặp từ khóa async và await dùng cho tác vụ bất đồng bộ.",
      "Cặp từ khóa lock và monitor dùng để đồng bộ hóa các luồng xử lý dữ liệu.",
      "Cặp từ khóa try và catch dùng trong khối cấu trúc bắt và xử lý ngoại lệ lỗi.",
      "Cặp từ khóa public và private dùng để thiết lập phạm vi truy cập biến thành viên."
    ],
    "correct": 0,
    "explanation": "Từ khóa async và await trong C# cho phép lập trình viên viết code bất đồng bộ một cách tự nhiên, giữ cho ứng dụng luôn mượt mà khi xử lý các tác vụ I/O tốn thời gian."
  },
  {
    "id": 30,
    "category": "Kiến trúc .NET",
    "bloom": "Remember",
    "question": "Hai trụ cột nền tảng cốt lõi cấu thành nên hệ sinh thái Microsoft .NET là gì?",
    "options": [
      "Thư viện lớp (.NET FCL) và Môi trường thực thi mã chung CLR.",
      "Hệ điều hành Windows 11 bản quyền cùng bộ công cụ văn phòng Microsoft Office 365.",
      "Trình duyệt web Microsoft Edge và Công cụ tìm kiếm dữ liệu phân tán quy mô lớn Bing.",
      "Phần cứng vi xử lý Intel Core đa nhân cùng hệ thống thanh nhớ RAM tốc độ cao có tản nhiệt."
    ],
    "correct": 0,
    "explanation": "Kiến trúc .NET gồm hai thành phần chủ chốt: FCL (kho thư viện lớp đồ sộ có sẵn) và CLR (máy ảo thực thi, quản lý vòng đời ứng dụng)."
  },
  {
    "id": 31,
    "category": "Kiến trúc .NET",
    "bloom": "Understand",
    "question": "Khái niệm 'Managed Code' (Mã được quản lý) trong thế giới .NET có nghĩa là gì?",
    "options": [
      "Mã nguồn được đặt mật khẩu bảo vệ quyền truy cập trong thư mục dự án.",
      "Mã nguồn phần mềm do trực tiếp Giám đốc dự án (Project Manager) giám sát.",
      "Mã máy nhị phân chạy trực tiếp trên chip mà không cần máy ảo trung gian hỗ trợ.",
      "Mã được biên dịch ra MSIL và chạy dưới sự kiểm soát, quản lý an toàn của máy ảo CLR."
    ],
    "correct": 3,
    "explanation": "Managed code là mã được CLR quản lý trực tiếp trong lúc chạy, cung cấp các dịch vụ như thu gom rác, kiểm tra kiểu dữ liệu an toàn và xử lý biệt lệ."
  },
  {
    "id": 32,
    "category": "Kiến trúc .NET",
    "bloom": "Understand",
    "question": "Khi lập trình viên biên dịch mã nguồn C# (*.cs) bằng trình biên dịch csc.exe, kết quả đầu ra trực tiếp là gì?",
    "options": [
      "Mã nguồn C++ tương đương để lập trình viên chỉnh sửa thủ công.",
      "Mã máy nhị phân thuần túy tối ưu riêng cho dòng vi xử lý Intel x86/x64.",
      "Mã trung gian MSIL kèm siêu dữ liệu Metadata đóng gói trong tệp assembly .dll hoặc .exe.",
      "Tệp tin văn bản định dạng HTML chứa tài liệu hướng dẫn kỹ thuật của phần mềm."
    ],
    "correct": 2,
    "explanation": "Trình biên dịch C# không dịch trực tiếp ra mã máy CPU mà dịch thành mã trung gian MSIL (Microsoft Intermediate Language) kèm Metadata lưu trong file assembly (.dll/.exe)."
  },
  {
    "id": 33,
    "category": "Kiến trúc .NET",
    "bloom": "Understand",
    "question": "Bộ phận nào trong máy ảo CLR chịu trách nhiệm chuyển đổi mã trung gian MSIL thành mã máy bản địa khi ứng dụng chạy?",
    "options": [
      "Trình nạp lớp đối tượng hệ thống (Class Loader) của môi trường thực thi.",
      "Bộ thu gom rác tự động của vùng nhớ heap (Garbage Collector) trên máy ảo.",
      "Hệ quản trị cơ sở dữ liệu quan hệ tích hợp sẵn trong nhân hệ điều hành máy tính.",
      "Trình biên dịch tức thời JIT Compiler (Just-In-Time Compiler)."
    ],
    "correct": 3,
    "explanation": "JIT (Just-In-Time) Compiler là thành phần của CLR có nhiệm vụ biên dịch mã MSIL sang mã máy bản địa của CPU cụ thể ngay khi phương thức được gọi lần đầu."
  },
  {
    "id": 34,
    "category": "Kiến trúc .NET",
    "bloom": "Understand",
    "question": "Nguy cơ bảo mật và sự cố hệ thống nghiêm trọng nhất khi thực thi 'Unmanaged Code' (như C/C++ truyền thống) là gì?",
    "options": [
      "Làm tiêu tốn điện năng của pin máy tính xách tay nhanh hơn so với bình thường.",
      "Không thể hiển thị được các ký tự font chữ Unicode tiếng Việt trên giao diện ứng dụng.",
      "Lỗi con trỏ bộ nhớ và tràn bộ đệm (Buffer Overflow) có thể làm sập hệ thống hoặc màn hình xanh.",
      "Bắt buộc máy tính phải duy trì kết nối mạng Internet liên tục thì mới tải được các thư viện liên kết."
    ],
    "correct": 2,
    "explanation": "Unmanaged code không có CLR giám sát. Sai sót con trỏ bộ nhớ có thể gây tràn bộ đệm (Buffer Overflow), rò rỉ bộ nhớ nghiêm trọng hoặc làm sập toàn bộ hệ điều hành."
  },
  {
    "id": 35,
    "category": "Độc lập Nền tảng",
    "bloom": "Understand",
    "question": "Tính độc lập nền tảng (Platform Independence) của .NET Core và .NET 8 mang lại quyền năng gì cho lập trình viên?",
    "options": [
      "Chỉ cho phép ứng dụng khởi chạy duy nhất trên hệ điều hành Windows có bản quyền đầy đủ.",
      "Viết và biên dịch một lần; tệp MSIL có thể chạy trên Windows, Linux và macOS nếu có CLR phù hợp.",
      "Tự động chuyển đổi máy tính cá nhân thành máy chủ đám mây phân tán mà không cần cấu hình mạng phức tạp.",
      "Không cần cài đặt bất kỳ phần mềm môi trường thực thi nào ứng dụng vẫn tự động chạy được trên tất cả các loại chip."
    ],
    "correct": 1,
    "explanation": "Nhờ mã trung gian MSIL và máy ảo CLR đa nền tảng, một ứng dụng .NET có thể chạy mượt mà trên Windows, macOS và các bản phân phối Linux mà không cần biên dịch lại."
  },
  {
    "id": 36,
    "category": "Tương tác Đa ngôn ngữ",
    "bloom": "Understand",
    "question": "Khả năng Tương tác đa ngôn ngữ (Language Interoperability) trong hệ sinh thái .NET được hiện thực hóa dựa trên nguyên lý nào?",
    "options": [
      "Các ngôn ngữ tương thích .NET (C#, VB.NET, F#) đều được biên dịch về chung định dạng mã trung gian chuẩn MSIL.",
      "Lập trình viên tự sử dụng công cụ trí tuệ nhân tạo để dịch mã nguồn thủ công qua lại giữa các ngôn ngữ.",
      "Tất cả các ngôn ngữ lập trình đều bắt buộc phải tuân thủ nghiêm ngặt quy tắc ngữ pháp tiếng Anh thông dụng.",
      "Hệ điều hành Windows tự động phát hiện cú pháp khác biệt và sửa chữa mã lệnh trong quá trình nạp vào bộ nhớ RAM."
    ],
    "correct": 0,
    "explanation": "Do C#, Visual Basic .NET và F# đều biên dịch ra cùng một chuẩn MSIL và dùng chung kiểu dữ liệu CTS (Common Type System), chúng có thể kế thừa và gọi hàm qua lại không rào cản."
  },
  {
    "id": 37,
    "category": "Visual Studio IDE",
    "bloom": "Understand",
    "question": "Trong môi trường Visual Studio IDE, mối quan hệ phân cấp giữa Solution (*.sln) và Project (*.csproj) là gì?",
    "options": [
      "Project là thùng chứa cấp cao nhất quản lý hàng loạt các Solution độc lập bên trong.",
      "Solution và Project là hai thuật ngữ hoàn toàn đồng nghĩa và có thể dùng thay thế cho nhau.",
      "Solution chỉ dùng cấu hình cơ sở dữ liệu; Project chỉ dùng để thiết kế giao diện bằng kéo thả điều khiển.",
      "Solution chứa một hoặc nhiều Project; mỗi Project chứa các tệp mã nguồn và tài nguyên liên quan."
    ],
    "correct": 3,
    "explanation": "Solution (.sln) là container cấp cao nhất quản lý một hoặc nhiều Project (.csproj) cùng các cấu hình build và dependencies liên kết."
  },
  {
    "id": 38,
    "category": "Lập trình Trực quan",
    "bloom": "Remember",
    "question": "Trong ứng dụng đồ họa Painter (mục 1.12), điều khiển GUI nào được dùng để người dùng rê chuột vẽ các nét vẽ màu lên bề mặt?",
    "options": [
      "Điều khiển Button (nút bấm kích hoạt hành động tức thì Undo hoặc Clear).",
      "Điều khiển GroupBox (khung chứa phân nhóm các nút tùy chọn màu sắc và kích cỡ nét vẽ).",
      "Điều khiển RadioButton (nút chọn hình tròn mang tính chất loại trừ lẫn nhau trong cùng nhóm).",
      "Điều khiển Panel (vùng không gian đồ họa tiếp nhận thao tác vẽ từ chuột)."
    ],
    "correct": 3,
    "explanation": "Panel màu trắng là vùng không gian giao diện tiếp nhận các thao tác chuột (MouseDown, MouseMove) để hiển thị các nét vẽ nghệ thuật."
  },
  {
    "id": 39,
    "category": "Lập trình Trực quan",
    "bloom": "Understand",
    "question": "Tính chất đặc trưng nhất của điều khiển RadioButton khi được đặt trong cùng một GroupBox là gì?",
    "options": [
      "Cho phép người dùng đánh dấu chọn đồng thời tất cả các nút trong nhóm cùng lúc.",
      "Tự động đổi màu sắc hiển thị khi con trỏ chuột của người dùng rê ngang qua bề mặt form.",
      "Tính loại trừ: Chỉ duy nhất một nút được chọn tại một thời điểm.",
      "Không thể kích hoạt bất kỳ sự kiện xử lý nào khi người dùng tương tác nhấp chuột trên giao diện."
    ],
    "correct": 2,
    "explanation": "Trong cùng một GroupBox, các RadioButton mang tính loại trừ lẫn nhau: người dùng chỉ có thể chọn đúng một tùy chọn duy nhất tại một thời điểm."
  },
  {
    "id": 40,
    "category": "Lập trình Hướng sự kiện",
    "bloom": "Understand",
    "question": "Trong mô hình Lập trình Hướng sự kiện (Event-Driven Programming), chương trình phản hồi lại các thao tác của người dùng như thế nào?",
    "options": [
      "Duy trì Event Loop lắng nghe; khi có sự kiện thì kích hoạt Event Handler tương ứng để xử lý.",
      "Chương trình thực thi tuần tự từ đầu đến cuối tệp mã nguồn rồi tự động kết thúc.",
      "Bắt buộc người dùng nhập các chuỗi dòng lệnh văn bản từ bàn phím thì mới có thể xử lý.",
      "Tự động suy đoán trước hành vi tiếp theo của người dùng thông qua thuật toán học máy tích hợp sẵn."
    ],
    "correct": 0,
    "explanation": "Ứng dụng GUI vận hành theo mô hình Event-Driven: ứng dụng luôn ở trạng thái lắng nghe trong Event Loop, khi có sự kiện (Event) xảy ra thì Trình xử lý sự kiện (Event Handler) tương ứng sẽ được gọi."
  }
];

// ============================================================================
// HỌC PHẦN: KỸ THUẬT LẬP TRÌNH (4 TÍN CHỈ) - IT26M
// NGÂN HÀNG CÂU HỎI TRẮC NGHIỆM CHƯƠNG 2: INTRODUCTION TO VISUAL STUDIO AND VISUAL PROGRAMMING
// ĐẶC TẢ CHUẨN HÓA:
// - Tổng số: 40 câu trắc nghiệm chuẩn hóa 4 lựa chọn (A, B, C, D)
// - Phân bố đáp án đúng: Chính xác 10 A, 10 B, 10 C, 10 D
// - Phân bố độ dài đáp án đúng: 10 Ngắn nhất (Rank 1), 10 Rank 2, 10 Rank 3, 10 Dài nhất (Rank 4)
// - Thang đo Bloom: Remember (12), Understand (14), Apply (9), Analyze (5)
// ============================================================================
const QUIZ_CHAPTER_02 = [
  {
    "id": 1,
    "category": "Tổng quan IDE",
    "bloom": "Remember",
    "question": "Thuật ngữ viết tắt IDE trong môi trường phát triển ứng dụng Visual C# là viết tắt của cụm từ nào?",
    "options": [
      "Integrated Development Environment.",
      "Interactive Data Execution for Systems Programming.",
      "Interface Deployment Engine for Windows Applications.",
      "Internal Developer Equipment for Systems Architecture."
    ],
    "answer": 0,
    "explanation": "Theo mục 2.1 giáo trình Deitel: IDE là viết tắt của Integrated Development Environment (Môi trường phát triển tích hợp), đóng gói trình soạn thảo, biên dịch, thiết kế giao diện và gỡ lỗi trên một phần mềm thống nhất."
  },
  {
    "id": 2,
    "category": "Triết lý RAD",
    "bloom": "Understand",
    "question": "Đặc trưng then chốt nhất của mô hình Phát triển Ứng dụng Nhanh (RAD) trong lập trình Windows Forms là gì?",
    "options": [
      "Chỉ viết mã nguồn bằng dòng lệnh console.",
      "Tái sử dụng linh kiện có sẵn và tạo mẫu giao diện nhanh bằng kéo thả.",
      "Yêu cầu lập trình viên phải tự tính toán tọa độ điểm ảnh pixel cho từng nút bấm.",
      "Loại bỏ hoàn toàn trình biên dịch và thực thi trực tiếp mã C# trên bo mạch chủ phần cứng."
    ],
    "answer": 1,
    "explanation": "RAD tập trung vào việc tạo nhanh bản mẫu (Prototyping), kéo thả linh kiện trực quan và tái sử dụng tối đa các lớp điều khiển có sẵn trong .NET Framework Class Library (FCL)."
  },
  {
    "id": 3,
    "category": "Tổng quan IDE",
    "bloom": "Remember",
    "question": "Phiên bản Visual Studio nào sau đây được Microsoft cung cấp hoàn toàn miễn phí phục vụ đào tạo sinh viên và dự án cá nhân?",
    "options": [
      "Visual Studio Pro.",
      "Visual Studio Enterprise Suite.",
      "Visual Studio Community bản đầy đủ tính năng cho học tập.",
      "Visual Studio Professional dành riêng cho doanh nghiệp quy mô vừa và lớn trên toàn cầu."
    ],
    "answer": 2,
    "explanation": "Visual Studio Community là ấn bản miễn phí bản quyền nhưng sở hữu đầy đủ tính năng thiết kế giao diện, biên dịch C# và gỡ lỗi nâng cao phục vụ sinh viên, giảng viên và nghiên cứu cá nhân."
  },
  {
    "id": 4,
    "category": "Màn hình Khởi động",
    "bloom": "Remember",
    "question": "Khu vực 'Recent' trên màn hình Start Page khi vừa mở Visual Studio có công dụng chính là gì?",
    "options": [
      "Xem bản vá lỗi Windows.",
      "Cập nhật tin tức công nghệ.",
      "Xóa sạch bộ nhớ đệm cũ.",
      "Hiển thị danh sách các giải pháp và dự án đã làm việc gần đây để mở lại tức thì chỉ bằng một cú nhấp chuột."
    ],
    "answer": 3,
    "explanation": "Khu vực Recent trên Start Page liệt kê danh sách các dự án (.csproj) và giải pháp (.sln) được truy cập gần nhất, giúp lập trình viên mở lại công việc nhanh mà không cần tìm kiếm thư mục."
  },
  {
    "id": 5,
    "category": "Hộp thoại New Project",
    "bloom": "Apply",
    "question": "Để tạo dự án phần mềm giao diện đồ họa cửa sổ màn hình Desktop bằng Visual C#, lập trình viên chọn mẫu template nào?",
    "options": [
      "Console Application độc lập dòng lệnh đen trắng.",
      "Windows Forms Application.",
      "WCF Service Application cho dịch vụ phân tán đám mây.",
      "ASP.NET Web Forms Application cho ứng dụng trực tuyến."
    ],
    "answer": 1,
    "explanation": "Mẫu Windows Forms Application trong phân mục Visual C# -> Windows được dùng để xây dựng các ứng dụng đồ họa máy tính tương tác chuẩn mực trên hệ điều hành Windows."
  },
  {
    "id": 6,
    "category": "Hộp thoại New Project",
    "bloom": "Understand",
    "question": "Tại sao trong ô nhập tên dự án (Name), lập trình viên nên đặt tên theo chuẩn PascalCase, viết liền không dấu tiếng Việt?",
    "options": [
      "Để giảm dung lượng RAM của hệ điều hành.",
      "Vì hệ điều hành Windows không hỗ trợ lưu tệp tin có khoảng trắng trên ổ đĩa cứng chuẩn NTFS.",
      "Vì tên dự án sẽ trở thành Namespace mặc định và tên tệp thực thi .exe của ứng dụng.",
      "Nhằm giúp máy tính tự động tăng gấp đôi tốc độ xung nhịp của CPU trong quá trình biên dịch mã nguồn."
    ],
    "answer": 2,
    "explanation": "Tên dự án được Visual Studio sử dụng làm Không gian tên mặc định (Default Namespace) và tên file nhị phân đầu ra (.exe). Nếu chứa khoảng trắng hay ký tự đặc biệt, nó có thể gây lỗi cú pháp và đường dẫn."
  },
  {
    "id": 7,
    "category": "Hộp thoại New Project",
    "bloom": "Understand",
    "question": "Mục đích quan trọng của việc tích chọn ô kiểm 'Create directory for solution' khi tạo dự án mới là gì?",
    "options": [
      "Mã hóa tệp tin chống sao chép.",
      "Tự động tải mã nguồn lên kho lưu trữ đám mây.",
      "Bắt buộc người dùng máy tính phải nhập mật khẩu quản trị viên mới có thể mở được ứng dụng trên máy trạm.",
      "Tạo thư mục cha bao bọc toàn bộ giải pháp giúp quản lý mã nguồn, tài nguyên gọn gàng và độc lập."
    ],
    "answer": 3,
    "explanation": "Tích chọn 'Create directory for solution' giúp tạo thư mục cha riêng chứa tệp giải pháp .sln và các thư mục dự án con, thuận tiện khi sao lưu, nén nộp bài hoặc chia sẻ mã nguồn."
  },
  {
    "id": 8,
    "category": "Khung nhìn Design View",
    "bloom": "Understand",
    "question": "Bề mặt Form1 màu xám hiển thị ở trung tâm màn hình Design View có vai trò kỹ thuật là gì?",
    "options": [
      "Là tấm toan vẽ đồ họa đại diện cho cửa sổ ứng dụng Windows thực tế để kéo thả và bài trí các điều khiển giao diện.",
      "Chỉ là một hình ảnh tĩnh để minh họa.",
      "Là bảng hiển thị các lỗi cú pháp lập trình.",
      "Là nơi kiểm tra bộ nhớ RAM đang hoạt động thực tế."
    ],
    "answer": 0,
    "explanation": "Design View hiển thị Form1 như một tấm toan vẽ (Canvas) trực quan, cho phép lập trình viên kéo thả, căn chỉnh vị trí và thay đổi thuộc tính của các điều khiển đồ họa theo mô hình WYSIWYG."
  },
  {
    "id": 9,
    "category": "Khung nhìn Design View",
    "bloom": "Apply",
    "question": "Các ô vuông nhỏ màu trắng (Sizing handles) xuất hiện quanh viền Form1 khi được nhấp chọn dùng để làm gì?",
    "options": [
      "Đổi màu nền của Form sang màu trắng tinh khôi.",
      "Xóa vĩnh viễn Form hiện hành ra khỏi dự án đang mở.",
      "Kéo giãn thay đổi kích thước Form.",
      "Khóa cố định vị trí cửa sổ trên màn hình máy tính cá nhân."
    ],
    "answer": 2,
    "explanation": "Sizing handles (chốt điều chỉnh kích thước) ở 4 góc và 4 cạnh cho phép dùng chuột kéo giãn để tăng giảm chiều rộng và chiều cao của Form một cách trực quan."
  },
  {
    "id": 10,
    "category": "Hệ thống Menu Bar",
    "bloom": "Remember",
    "question": "Khi vô tình đóng mất một cửa sổ làm việc như Solution Explorer hoặc Toolbox, menu nào là nơi giúp mở lại nhanh nhất?",
    "options": [
      "Menu File trên Menu Bar.",
      "Menu Edit chứa các lệnh hoàn tác và tìm kiếm văn bản.",
      "Menu Tools dùng cấu hình môi trường phát triển phần mềm.",
      "Menu View chứa danh mục các cửa sổ công cụ của IDE."
    ],
    "answer": 3,
    "explanation": "Menu View là trung tâm quản lý hiển thị của IDE. Mọi cửa sổ bị ẩn hay đóng nhầm đều có thể mở lại thông qua menu View (View -> Solution Explorer, View -> Toolbox...)."
  },
  {
    "id": 11,
    "category": "Menu Build",
    "bloom": "Analyze",
    "question": "Sự khác biệt then chốt giữa lệnh 'Build Solution' và lệnh 'Rebuild Solution' trong menu Build là gì?",
    "options": [
      "Build biên dịch các file vừa sửa, còn Rebuild xóa sạch file nhị phân cũ trong bin/obj rồi dịch lại toàn bộ từ đầu.",
      "Build dịch mã C#, Rebuild dịch mã C++.",
      "Build chạy ứng dụng, Rebuild chỉ lưu file mã nguồn.",
      "Build dành riêng cho hệ điều hành Windows 32-bit, trong khi Rebuild được tối ưu cho các dòng máy tính 64-bit đa nhân hiện đại."
    ],
    "answer": 0,
    "explanation": "Build Solution thực hiện biên dịch gia tăng (Incremental Build) cho các file có thay đổi để tiết kiệm thời gian; Rebuild Solution dọn sạch toàn bộ thư mục bin/obj rồi biên dịch mới 100% để loại bỏ lỗi cache."
  },
  {
    "id": 12,
    "category": "Menu Debug",
    "bloom": "Analyze",
    "question": "Lệnh 'Start Debugging' (F5) khác với lệnh 'Start Without Debugging' (Ctrl + F5) ở điểm cốt lõi nào?",
    "options": [
      "F5 chỉ dịch mã, Ctrl+F5 chạy ngay.",
      "F5 chạy ứng dụng có kết nối với bộ giám sát lỗi của IDE, còn Ctrl+F5 chạy ứng dụng độc lập với tốc độ cao nhất.",
      "F5 chỉ chạy được trên hệ điều hành 64-bit.",
      "F5 yêu cầu quyền quản trị viên máy tính phòng máy."
    ],
    "answer": 1,
    "explanation": "F5 kích hoạt Debugger để theo dõi biến và bắt điểm dừng Breakpoint khi có sự cố. Ctrl+F5 chạy trực tiếp không gắn cờ Debugger, thích hợp khi cần kiểm thử tốc độ thực tế của người dùng."
  },
  {
    "id": 13,
    "category": "Menu Format",
    "bloom": "Apply",
    "question": "Menu nào trên thanh Menu Bar sẽ tự động xuất hiện khi lập trình viên chọn đồng thời từ hai điều khiển trở lên trên Form?",
    "options": [
      "Menu Project để thêm mới tệp tin.",
      "Menu Tools cung cấp các tiện ích hệ thống.",
      "Menu Debug dùng để đặt các điểm dừng kiểm thử.",
      "Menu Format."
    ],
    "answer": 3,
    "explanation": "Menu Format chỉ hiển thị khi có từ hai điều khiển trở lên được chọn, cung cấp các lệnh căn lề (Align), chỉnh bằng kích thước (Make Same Size) và giãn khoảng cách (Horizontal/Vertical Spacing)."
  },
  {
    "id": 14,
    "category": "Standard Toolbar",
    "bloom": "Apply",
    "question": "Tại sao lập trình viên luôn được khuyến nghị sử dụng nút 'Save All' (Ctrl + Shift + S) thay vì Save thường (Ctrl + S)?",
    "options": [
      "Vì thao tác kéo thả Form làm biến động đồng thời cả Form1.cs, Form1.Designer.cs và Form1.resx.",
      "Để giải phóng dung lượng bộ nhớ RAM.",
      "Vì thao tác Save All sẽ tự động biên dịch toàn bộ chương trình mã nguồn C# sang tệp nhị phân .exe trên máy tính.",
      "Vì nếu chỉ bấm Save thường thì các điều khiển đồ họa trên Form sẽ bị khôi phục về giá trị mặc định."
    ],
    "answer": 0,
    "explanation": "Trong Windows Forms, mỗi thay đổi trên giao diện ảnh hưởng đồng thời tới tệp mã logic (Form1.cs), tệp mã sinh tự động (Form1.Designer.cs) và tài nguyên (.resx). Save All đảm bảo toàn bộ được lưu an toàn."
  },
  {
    "id": 15,
    "category": "Thanh Công cụ",
    "bloom": "Remember",
    "question": "Tính năng hiển thị một nhãn nhỏ màu vàng nhạt mô tả chức năng của nút bấm khi rê chuột qua nút công cụ được gọi là gì?",
    "options": [
      "Smart Tag.",
      "Tooltip (Chú giải công cụ kèm phím tắt).",
      "Context Menu.",
      "Status Label nằm ở thanh trạng thái dưới chân màn hình."
    ],
    "answer": 1,
    "explanation": "Tooltip là nhãn chú giải nổi lên khi rê chuột dừng trên một nút công cụ, hiển thị tên lệnh và phím tắt tương ứng trong dấu ngoặc đơn."
  },
  {
    "id": 16,
    "category": "Phím tắt Chuẩn",
    "bloom": "Remember",
    "question": "Phím tắt mặc định trong Visual Studio dùng để mở nhanh Cửa sổ Thuộc tính (Properties Window) là phím nào?",
    "options": [
      "Phím F2.",
      "Phím F7.",
      "Phím F4 (kích hoạt cửa sổ Properties của đối tượng đang chọn).",
      "Tổ hợp phím Shift + F5."
    ],
    "answer": 2,
    "explanation": "Phím F4 là phím tắt mặc định để mở hoặc di chuyển tiêu điểm trực tiếp đến Properties Window để cấu hình thuộc tính của đối tượng đang chọn."
  },
  {
    "id": 17,
    "category": "Trợ giúp Ngữ cảnh",
    "bloom": "Understand",
    "question": "Phím F1 trong Visual Studio kích hoạt tính năng Trợ giúp Ngữ cảnh (Context-Sensitive Help) có cơ chế hoạt động như thế nào?",
    "options": [
      "Mở tài liệu MSDN đúng điều khiển đang chọn.",
      "Tự động sửa toàn bộ lỗi cú pháp trong mã lệnh C#.",
      "Gửi thông báo cầu cứu đến máy chủ hỗ trợ kỹ thuật.",
      "Chuyển giao diện làm việc của Visual Studio sang ngôn ngữ tiếng Việt."
    ],
    "answer": 0,
    "explanation": "Phím F1 nhận diện đối tượng đang được chọn (trên Form hoặc từ khóa trong code) và tự động mở đúng trang tài liệu Microsoft MSDN / Learn liên quan đến đối tượng đó."
  },
  {
    "id": 18,
    "category": "Kỹ thuật Điều hướng",
    "bloom": "Understand",
    "question": "Khi biểu tượng chiếc đinh ghim (Pushpin) trên thanh tiêu đề của một cửa sổ công cụ xoay sang tư thế nằm ngang, cửa sổ đó đang ở trạng thái nào?",
    "options": [
      "Cửa sổ bị khóa.",
      "Kích hoạt chế độ Tự động ẩn (Auto-Hide).",
      "Cửa sổ đang ở trạng thái Ghim cố định trên màn hình.",
      "Cửa sổ đã bị gỡ bỏ hoàn toàn khỏi môi trường phát triển."
    ],
    "answer": 1,
    "explanation": "Khi đinh ghim nằm ngang (Horizontal pin), tính năng Auto-Hide được kích hoạt: cửa sổ thu thành tab nhỏ ở mép màn hình, chỉ mở ra khi rê chuột vào và thụt lại khi rê chuột ra."
  },
  {
    "id": 19,
    "category": "Kỹ thuật Điều hướng",
    "bloom": "Apply",
    "question": "Biểu tượng hướng dẫn ghép nối (Docking Visualizer) hình chữ thập với 4 mũi tên xuất hiện khi người dùng thực hiện thao tác nào?",
    "options": [
      "Nhấp đúp chuột lên Form.",
      "Nhấn tổ hợp phím tắt Ctrl + Shift + B.",
      "Nhấp giữ thanh tiêu đề của một cửa sổ và kéo di chuyển trên màn hình.",
      "Mở hộp thoại New Project để khởi tạo một giải pháp mới với cấu trúc đa tầng phức tạp."
    ],
    "answer": 2,
    "explanation": "Docking Visualizer xuất hiện khi kéo thanh tiêu đề cửa sổ, hỗ trợ neo (dock) cửa sổ vào cạnh màn hình hoặc thả vào tâm để gộp thành tab."
  },
  {
    "id": 20,
    "category": "Kỹ thuật Điều hướng",
    "bloom": "Apply",
    "question": "Lệnh nào sau đây giúp khôi phục toàn bộ bố cục các cửa sổ công cụ về trạng thái xuất xưởng mặc định khi giao diện bị xáo trộn?",
    "options": [
      "File -> Close Solution.",
      "Edit -> Undo All Window Moves.",
      "Tools -> Import and Export Settings.",
      "Window -> Reset Window Layout (khôi phục toàn bộ giao diện IDE về trạng thái chuẩn ban đầu)."
    ],
    "answer": 3,
    "explanation": "Lệnh Window -> Reset Window Layout trên thanh Menu Bar sẽ sắp xếp lại toàn bộ các cửa sổ làm việc về vị trí và bố cục mặc định của nhà sản xuất."
  },
  {
    "id": 21,
    "category": "Solution Explorer",
    "bloom": "Understand",
    "question": "Thứ bậc phân cấp giữa Solution (.sln) và Project (.csproj) trong Visual Studio được hiểu đúng như thế nào?",
    "options": [
      "Project là cấp cha chứa các Solution con bên trong.",
      "Solution chứa một hoặc nhiều Project con.",
      "Solution và Project hoàn toàn ngang hàng và không có quan hệ chứa nhau.",
      "Mỗi Solution chỉ được phép chứa duy nhất một tệp tin mã nguồn C# đơn lẻ."
    ],
    "answer": 1,
    "explanation": "Solution (đuôi .sln) là cấp cao nhất đóng vai trò như một chiếc cặp lớn, có thể chứa một hoặc nhiều Project (.csproj) cùng phối hợp hoạt động."
  },
  {
    "id": 22,
    "category": "Giải phẫu Tệp tin",
    "bloom": "Understand",
    "question": "Tệp tin nào trong dự án Windows Forms là nơi lập trình viên chúng ta viết mã xử lý nghiệp vụ và các phương thức xử lý sự kiện?",
    "options": [
      "Tệp cấu hình App.config.",
      "Tệp tin tài nguyên nhị phân Form1.resx của dự án.",
      "Tệp tin mã nguồn chính Form1.cs.",
      "Tệp tin sinh mã tự động Form1.Designer.cs của IDE."
    ],
    "answer": 2,
    "explanation": "Tệp Form1.cs là nơi lập trình viên viết mã nguồn nghiệp vụ và các hàm xử lý sự kiện (Event Handlers) cho ứng dụng."
  },
  {
    "id": 23,
    "category": "Giải phẫu Tệp tin",
    "bloom": "Analyze",
    "question": "Tại sao trong tệp Form1.Designer.cs có cảnh báo lập trình viên không được tự ý sửa đổi mã trong phương thức InitializeComponent()?",
    "options": [
      "Vì chứa mã bản quyền Windows.",
      "Vì nó sẽ làm hỏng kết nối mạng Internet.",
      "Vì mã tại đây sẽ tự động kích hoạt lệnh xóa sạch toàn bộ hệ quản trị cơ sở dữ liệu của máy chủ doanh nghiệp khi biên dịch phần mềm.",
      "Vì phương thức này do Form Designer quản lý tự động, việc sửa tay dễ gây xung đột làm hỏng màn hình Design View."
    ],
    "answer": 3,
    "explanation": "InitializeComponent() hoàn toàn do công cụ trực quan Form Designer đồng bộ tự động. Sửa tay sai cú pháp có thể khiến IDE không phân tích cú pháp thiết kế được và không mở lại được Design View."
  },
  {
    "id": 24,
    "category": "Giải phẫu Tệp tin",
    "bloom": "Remember",
    "question": "Tệp tin Form1.resx đi kèm với Form trong dự án Windows Forms đảm nhiệm vai trò gì?",
    "options": [
      "Lưu trữ các dữ liệu tài nguyên phi mã nguồn của form như chuỗi ký tự đa ngôn ngữ, hình ảnh và biểu tượng nhị phân.",
      "Chứa mã hợp ngữ của CPU.",
      "Quản lý mạng không dây của máy tính.",
      "Lưu lịch sử đăng nhập phòng máy sinh viên."
    ],
    "answer": 0,
    "explanation": "Tệp .resx (Resource XML) dùng để lưu trữ các tài nguyên nhị phân và chuỗi bản địa hóa đi kèm với Form như hình ảnh, biểu tượng (icon) và văn bản dịch."
  },
  {
    "id": 25,
    "category": "Giải phẫu Tệp tin",
    "bloom": "Understand",
    "question": "Phương thức tĩnh static void Main() - điểm khởi nhập (Entry Point) của toàn bộ ứng dụng Windows Forms nằm trong tệp nào?",
    "options": [
      "Tệp giao diện Form1.cs.",
      "Tệp tài nguyên Form1.Designer.cs.",
      "Tệp Program.cs.",
      "Tệp thông tin hợp ngữ AssemblyInfo.cs."
    ],
    "answer": 2,
    "explanation": "Tệp Program.cs chứa hàm Main() tĩnh, là điểm bắt đầu thực thi của toàn bộ ứng dụng khi được nạp vào máy ảo .NET CLR."
  },
  {
    "id": 26,
    "category": "Thư viện References",
    "bloom": "Analyze",
    "question": "Hai thư viện nền tảng (.dll) cốt lõi nào trong nhánh References bắt buộc phải có để ứng dụng hiển thị được cửa sổ và vẽ đồ họa?",
    "options": [
      "System.IO và System.Net.",
      "System.Xml và System.Linq cho xử lý dữ liệu.",
      "System.Security và System.Data cho hệ quản trị cơ sở dữ liệu.",
      "System.Windows.Forms và System.Drawing."
    ],
    "answer": 3,
    "explanation": "System.Windows.Forms cung cấp các lớp điều khiển GUI (Form, Button, Label...) và System.Drawing cung cấp các dịch vụ đồ họa GDI+ (màu sắc, phông chữ, điểm ảnh, khung hình)."
  },
  {
    "id": 27,
    "category": "Toolbox",
    "bloom": "Understand",
    "question": "Vì sao khi mở một tệp mã nguồn code .cs thuần túy, cửa sổ Toolbox lại bị trống trơn và hiển thị thông báo 'no usable controls'?",
    "options": [
      "Vì Toolbox chỉ kích hoạt cho bề mặt đồ họa Design View, khi đang xem văn bản code thì không có canvas để nhận điều khiển.",
      "Do Visual Studio bị lỗi phân tích cú pháp.",
      "Do máy tính bị mất kết nối thư viện đám mây.",
      "Vì sinh viên chưa tiến hành kích hoạt bản quyền chính hãng của hệ điều hành Microsoft Windows trên máy trạm của trường học."
    ],
    "answer": 0,
    "explanation": "Toolbox là công cụ thiết kế trực quan. Khi con trỏ nằm ở tab soạn thảo văn bản code .cs, Toolbox tự động ẩn các linh kiện; chỉ khi mở tab Form [Design] các linh kiện mới hiện lên."
  },
  {
    "id": 28,
    "category": "Common Controls",
    "bloom": "Remember",
    "question": "Đặc điểm nhận diện quan trọng nhất của điều khiển Label trong nhóm Common Controls là gì?",
    "options": [
      "Cho phép gõ văn bản tự do.",
      "Dùng để hiển thị văn bản tĩnh, chú thích hoặc tiêu đề mà người dùng cuối không thể nhấp chuột gõ sửa trực tiếp.",
      "Dùng để nạp và phát video.",
      "Tự động gửi email thông báo hệ thống."
    ],
    "answer": 1,
    "explanation": "Label dùng để hiển thị văn bản hướng dẫn hoặc nhãn tiêu đề tĩnh; người dùng cuối nhìn thấy nội dung nhưng không thể nhấp vào gõ chỉnh sửa trực tiếp."
  },
  {
    "id": 29,
    "category": "Common Controls",
    "bloom": "Remember",
    "question": "Điều khiển nào trong Windows Forms cho phép người dùng nhập dữ liệu văn bản từ bàn phím vào chương trình?",
    "options": [
      "Điều khiển Label gắn nhãn tĩnh.",
      "Điều khiển PictureBox hiển thị hình ảnh.",
      "Điều khiển Panel dùng làm khung chứa giao diện.",
      "TextBox."
    ],
    "answer": 3,
    "explanation": "TextBox là điều khiển chuyên dụng tiếp nhận dữ liệu văn bản nhập từ bàn phím máy tính của người dùng."
  },
  {
    "id": 30,
    "category": "Common Controls",
    "bloom": "Remember",
    "question": "Điều khiển đồ họa nào cung cấp nút bấm trực quan để người dùng nhấp chuột kích hoạt một hành động xử lý nghiệp vụ?",
    "options": [
      "Điều khiển Button (nút bấm).",
      "Điều khiển GroupBox.",
      "Điều khiển ProgressBar thể hiện tiến độ xử lý tác vụ.",
      "Điều khiển ToolTip hiển thị nhãn gợi ý nhỏ khi rê chuột."
    ],
    "answer": 0,
    "explanation": "Điều khiển Button cung cấp bề mặt nút bấm trực quan, kích hoạt sự kiện Click khi người dùng nhấp chuột để thực thi đoạn mã tương ứng."
  },
  {
    "id": 31,
    "category": "Common Controls",
    "bloom": "Remember",
    "question": "Điều khiển nào trong Windows Forms chuyên dùng để nạp và hiển thị các tệp hình ảnh như PNG, JPG, GIF hay BMP?",
    "options": [
      "ImageViewer.",
      "PictureBox (khung hiển thị hình ảnh).",
      "GraphicCanvas đồ họa.",
      "MediaElement hỗ trợ âm thanh đa kênh và hình ảnh động."
    ],
    "answer": 1,
    "explanation": "PictureBox là điều khiển đồ họa chuẩn trong Windows Forms được thiết kế để hiển thị các tệp tin hình ảnh tĩnh hoặc ảnh động gif."
  },
  {
    "id": 32,
    "category": "Properties Window",
    "bloom": "Understand",
    "question": "Khung Mô tả Thuộc tính (Description Pane) ở đáy cửa sổ Properties cung cấp thông tin hữu ích nào?",
    "options": [
      "Báo dung lượng ổ đĩa cứng.",
      "Thống kê số lượng sinh viên trực tuyến.",
      "Hiển thị đoạn văn ngắn giải thích ý nghĩa kỹ thuật và hướng dẫn cách thiết lập giá trị cho thuộc tính đang chọn.",
      "Đo lường điện năng tiêu thụ của cạc đồ họa."
    ],
    "answer": 2,
    "explanation": "Description Pane hiển thị tài liệu tóm lược về ý nghĩa chức năng của thuộc tính đang chọn, là trợ thủ đắc lực giúp người học tự tra cứu và hiểu bản chất thuộc tính."
  },
  {
    "id": 33,
    "category": "Properties Window",
    "bloom": "Apply",
    "question": "Để tìm nhanh một thuộc tính khi đã biết rõ tên gọi bắt đầu bằng chữ cái nào (ví dụ SizeMode hay TextAlign), ta chọn chế độ xem nào?",
    "options": [
      "Chế độ Alphabetical (A-Z).",
      "Chế độ Categorized phân nhóm theo chủ đề.",
      "Chế độ xem các sự kiện Events của điều khiển.",
      "Chế độ xem mã nguồn nhị phân cấp thấp của máy tính."
    ],
    "answer": 0,
    "explanation": "Chế độ xem Alphabetical sắp xếp danh sách thuộc tính theo thứ tự bảng chữ cái từ A đến Z, giúp lập trình viên tìm nhanh thuộc tính theo ký tự đầu."
  },
  {
    "id": 34,
    "category": "Thuộc tính Điều khiển",
    "bloom": "Analyze",
    "question": "Sự khác biệt bản chất giữa thuộc tính '(Name)' và thuộc tính 'Text' của một điều khiển trên Form là gì?",
    "options": [
      "Name đổi màu, Text đổi font.",
      "Name là tên biến trong mã C#, còn Text là chuỗi ký tự hiển thị trực quan lên giao diện.",
      "Name chỉ áp dụng cho Form, còn Text là thuộc tính riêng của nút bấm Button trên màn hình.",
      "Name bắt buộc viết bằng tiếng Việt có dấu, còn Text chỉ được phép viết bằng tiếng Anh chuẩn."
    ],
    "answer": 1,
    "explanation": "Thuộc tính (Name) là định danh biến đối tượng trong mã C# để lập trình viên gọi lệnh; còn Text là chuỗi văn bản hiển thị ra ngoài giao diện cho người dùng nhìn thấy."
  },
  {
    "id": 35,
    "category": "Thuộc tính BackColor",
    "bloom": "Apply",
    "question": "Tại sao khi tùy biến màu nền BackColor cho Form hoặc điều khiển, lập trình viên nên ưu tiên chọn màu trong tab 'Web'?",
    "options": [
      "Vì tab Web giúp máy chạy mát hơn.",
      "Vì tab Web chỉ hoạt động khi có mạng.",
      "Vì màu tab Web là màu cố định, không bị méo mó đổi màu khi máy tính người dùng thay đổi Theme giao diện.",
      "Vì màu tab Web giúp ứng dụng tự động đồng bộ lên trang web cá nhân của người lập trình viên trên máy chủ."
    ],
    "answer": 2,
    "explanation": "Các màu trong tab Web có mã màu cố định, đảm bảo ứng dụng luôn hiển thị đúng tone màu mong muốn trên mọi máy tính, không bị biến đổi theo Theme (Dark/Light) của hệ điều hành."
  },
  {
    "id": 36,
    "category": "Thuộc tính Font",
    "bloom": "Apply",
    "question": "Khi nhấp vào nút dấu 3 chấm [...] (Ellipsis button) ở thuộc tính Font của Label, điều gì sẽ xảy ra?",
    "options": [
      "Thuộc tính Font bị xóa.",
      "Mở trình soạn thảo Word.",
      "Tự động tải thêm phông chữ từ Internet.",
      "Mở hộp thoại Font Dialog cho phép lựa chọn trực quan kiểu phông chữ, kiểu dáng in đậm/nghiêng và kích thước cỡ chữ."
    ],
    "answer": 3,
    "explanation": "Nút dấu 3 chấm [...] mở hộp thoại đồ họa chuẩn Font Dialog cho phép chọn FontFamily, FontStyle (Bold, Italic) và Size (pt) một cách trực quan."
  },
  {
    "id": 37,
    "category": "Thuộc tính TextAlign",
    "bloom": "Apply",
    "question": "Lưới đồ họa 9 ô vuông nhỏ (3x3) của thuộc tính TextAlign trên Label cung cấp giá trị căn giữa hoàn hảo nào?",
    "options": [
      "TopLeft ở góc trên bên trái.",
      "MiddleCenter.",
      "BottomRight ở góc dưới bên phải.",
      "CenterAlign theo trục tọa độ độc lập."
    ],
    "answer": 1,
    "explanation": "Ô vuông ở chính tâm đại diện cho giá trị MiddleCenter - căn đều văn bản vào chính giữa nhãn theo cả trục ngang và trục dọc."
  },
  {
    "id": 38,
    "category": "Đường căn Snap Lines",
    "bloom": "Understand",
    "question": "Tính năng 'Đường căn thông minh' (Snap Lines) tự động xuất hiện khi kéo thả điều khiển mang lại lợi ích gì?",
    "options": [
      "Tự động vẽ các biểu đồ hình học.",
      "Kiểm tra xem hệ thống máy tính có bị nhiễm virus hay các phần mềm gián điệp độc hại hay không.",
      "Bắt dính thẳng hàng các mép điều khiển và duy trì khoảng cách lề chuẩn UI khuyến nghị.",
      "Tự động đổi màu tất cả các nút bấm trên Form sang màu hồng thắm và xanh lam rực rỡ sắc nét."
    ],
    "answer": 2,
    "explanation": "Snap Lines là các đường căn thông minh tự động bắt dính mép các điều khiển thẳng hàng nhau và giữ khoảng cách đệm (Padding/Margin) chuẩn theo khuyến nghị UI của Microsoft."
  },
  {
    "id": 39,
    "category": "PictureBox Resource",
    "bloom": "Apply",
    "question": "Khi nạp ảnh cho PictureBox trong hộp thoại Select Resource, tại sao nên chọn 'Project resource file' thay vì 'Local resource'?",
    "options": [
      "Vì tùy chọn này giúp ảnh nét hơn.",
      "Vì nó sẽ giảm kích thước tệp ảnh xuống thấp.",
      "Vì nó cho phép người dùng tự do chỉnh sửa tệp ảnh trực tiếp bằng các phần mềm đồ họa chuyên nghiệp của bên thứ ba độc lập trên máy trạm.",
      "Vì ảnh được đóng gói vĩnh viễn vào tệp tài nguyên của dự án và nhúng vào tệp .exe khi biên dịch, không lo bị mất ảnh."
    ],
    "answer": 3,
    "explanation": "Chọn 'Project resource file' nhúng trực tiếp bức ảnh vào tệp tài nguyên .resx và đóng gói vào tệp thực thi .exe, giúp ứng dụng đem đi máy khác vẫn hiển thị nguyên vẹn mà không bị đứt liên kết."
  },
  {
    "id": 40,
    "category": "Thuộc tính SizeMode",
    "bloom": "Analyze",
    "question": "Khi muốn hình ảnh trong PictureBox tự động co giãn để vừa khít hoàn toàn 100% cả chiều rộng và chiều cao khung điều khiển, ta thiết lập thuộc tính SizeMode mang giá trị nào?",
    "options": [
      "StretchImage (ép bức ảnh co giãn vừa khít hoàn toàn cả chiều ngang lẫn chiều dọc của khung PictureBox).",
      "Normal (cắt xén ảnh).",
      "CenterImage (căn ảnh vào giữa).",
      "AutoSize (khung tự phình to bằng ảnh)."
    ],
    "answer": 0,
    "explanation": "StretchImage ép hình ảnh co giãn vừa khít toàn bộ diện tích của PictureBox. (Normal cắt xén; AutoSize làm khung phình theo ảnh; CenterImage căn giữa; Zoom co giãn giữ nguyên tỷ lệ Aspect Ratio)."
  }
];


// ============================================================================
// NGÂN HÀNG CÂU HỎI TRẮC NGHIỆM CHƯƠNG 3: INTRODUCTION TO C# APP PROGRAMMING
// (40 CÂU CÂN BẰNG ĐỘ DÀI & ĐÁP ÁN: 10 A, 10 B, 10 C, 10 D; 10 R1, 10 R2, 10 R3, 10 R4)
// ============================================================================
const QUIZ_CHAPTER_03 = [
  {
    "id": 1,
    "category": "Cấu trúc Ứng dụng Console",
    "bloom": "Remember",
    "question": "Điểm khởi nhập (Entry Point) duy nhất mà máy ảo .NET CLR kích hoạt khi chạy ứng dụng C# là gì?",
    "options": [
      "Phương thức Main.",
      "Lớp cơ sở System.Object được nạp đầu tiên trong bộ nhớ.",
      "Phương thức khởi tạo constructor của lớp chứa giao diện đồ họa Form.",
      "Chỉ thị tiền xử lý using directive khai báo ở dòng đầu tiên của tệp mã nguồn."
    ],
    "correct": 0,
    "explanation": "Theo mục 3.2 giáo trình Deitel: Mọi ứng dụng C# đều bắt đầu thực thi từ phương thức Main. Phương thức này phải được khai báo với từ khóa static.",
    "answer": 0
  },
  {
    "id": 2,
    "category": "Cú pháp & Chú thích",
    "bloom": "Understand",
    "question": "Ký hiệu nào sau đây được dùng để bắt đầu một dòng chú thích đơn (Single-line comment) trong C#?",
    "options": [
      "Dấu thăng # đơn độc.",
      "Cặp dấu gạch chéo // ở đầu chú thích.",
      "Cặp dấu gạch chéo và dấu hoa thị /* bao bọc khối văn bản chú thích.",
      "Ký hiệu dấu chấm phẩy ; đặt ở cuối mỗi câu lệnh thực thi trong mã nguồn."
    ],
    "correct": 1,
    "explanation": "Mục 3.2.1 Deitel: Hai dấu gạch chéo // bắt đầu một chú thích một dòng, trình biên dịch C# sẽ bỏ qua mọi ký tự từ // đến cuối dòng đó.",
    "answer": 1
  },
  {
    "id": 3,
    "category": "Khai báo Lớp",
    "bloom": "Remember",
    "question": "Theo quy ước đặt tên chuẩn của Microsoft và giáo trình Deitel, tên Lớp (Class) trong C# nên tuân theo quy tắc nào?",
    "options": [
      "Quy ước camelCase.",
      "Viết hoa toàn bộ từ đầu đến cuối.",
      "Quy ước PascalCase viết hoa chữ cái đầu của mỗi từ cấu thành tên lớp.",
      "Viết thường toàn bộ tên lớp và ngăn cách các từ bằng các dấu gạch dưới snake_case."
    ],
    "correct": 2,
    "explanation": "Mục 3.2.4 Deitel: Tên lớp trong C# sử dụng quy ước PascalCase, viết hoa chữ cái đầu tiên của mỗi từ cấu thành (ví dụ: Welcome1, BankAccount).",
    "answer": 2
  },
  {
    "id": 4,
    "category": "Khai báo Lớp",
    "bloom": "Understand",
    "question": "Cặp ký tự nào được ngôn ngữ C# quy định để xác định ranh giới bắt đầu và kết thúc của một khối mã lệnh (Block)?",
    "options": [
      "Cặp ngoặc tròn ( ).",
      "Cặp ngoặc vuông [ ].",
      "Cặp từ khóa BEGIN và END.",
      "Cặp dấu ngoặc nhọn mở { để bắt đầu và dấu ngoặc nhọn đóng } để kết thúc phạm vi khối mã."
    ],
    "correct": 3,
    "explanation": "Mục 3.2.7 Deitel: Cặp dấu ngoặc nhọn mở { và đóng } tạo thành một khối mã (Block), xác định phạm vi của lớp, phương thức hay cấu trúc điều khiển.",
    "answer": 3
  },
  {
    "id": 5,
    "category": "Xuất dữ liệu Console",
    "bloom": "Remember",
    "question": "Phương thức nào của lớp Console có chức năng in chuỗi ký tự ra màn hình và đưa con trỏ xuống đầu dòng tiếp theo?",
    "options": [
      "Phương thức Console.Write giữ nguyên vị trí con trỏ trên dòng.",
      "Console.WriteLine.",
      "Phương thức Console.ReadLine chờ người dùng nhấn phím Enter.",
      "Phương thức Console.Clear làm sạch toàn bộ cửa sổ giao diện dòng lệnh."
    ],
    "correct": 1,
    "explanation": "Mục 3.2.6 Deitel: Console.WriteLine xuất dòng văn bản ra màn hình console và tự động định vị con trỏ ở đầu dòng mới kế tiếp.",
    "answer": 1
  },
  {
    "id": 6,
    "category": "Xuất dữ liệu Console",
    "bloom": "Understand",
    "question": "Điểm khác biệt cốt lõi giữa hai phương thức Console.Write và Console.WriteLine trong C# là gì?",
    "options": [
      "Write in chậm hơn WriteLine.",
      "Console.WriteLine chỉ cho phép xuất các số nguyên mà không thể xuất chuỗi ký tự văn bản.",
      "Console.Write không đưa con trỏ xuống dòng mới sau khi xuất xong.",
      "Console.Write yêu cầu quyền quản trị viên Administrator hệ thống mới có thể thực thi thành công."
    ],
    "correct": 2,
    "explanation": "Mục 3.4.1 Deitel: Console.Write in chuỗi nhưng không đưa con trỏ xuống dòng mới, trong khi Console.WriteLine tự động gửi thêm ký tự xuống dòng.",
    "answer": 2
  },
  {
    "id": 7,
    "category": "Ký tự thoát Escape Sequences",
    "bloom": "Remember",
    "question": "Ký tự thoát (Escape Sequence) nào trong chuỗi ký tự C# đại diện cho hành động đưa con trỏ xuống một dòng mới (Newline)?",
    "options": [
      "Ký hiệu \\t.",
      "Ký hiệu \\r lùi đầu dòng.",
      "Ký hiệu hai dấu gạch chéo ngược \\\\ in ra dấu gạch chéo đơn độc lập trên màn hình.",
      "Ký tự thoát \\n quy định xuống một dòng mới trong chuỗi văn bản."
    ],
    "correct": 3,
    "explanation": "Mục 3.4.2 Deitel: Ký tự thoát \\n (Newline) đẩy con trỏ xuống đầu dòng tiếp theo; \\ đại diện cho ký tự thoát (Escape character).",
    "answer": 3
  },
  {
    "id": 8,
    "category": "Ký tự thoát Escape Sequences",
    "bloom": "Apply",
    "question": "Để in ra màn hình chuỗi ký tự chứa dấu ngoặc kép: \"Hello\", câu lệnh C# nào sau đây là hoàn toàn hợp lệ?",
    "options": [
      "Console.WriteLine(\"\\\"Hello\\\"\"); sử dụng ký tự thoát \\\" để vô hiệu hóa ý nghĩa kết thúc chuỗi của dấu ngoặc kép.",
      "Console.WriteLine(\"\"Hello\"\");",
      "Console.WriteLine('/Hello/');",
      "Console.WriteLine(@'Hello');"
    ],
    "correct": 0,
    "explanation": "Mục 3.4.2 Deitel: Để nhúng dấu ngoặc kép bên trong một chuỗi ký tự mà không làm đóng chuỗi, ta phải dùng ký tự thoát \\\".",
    "answer": 0
  },
  {
    "id": 9,
    "category": "Ký tự thoát Escape Sequences",
    "bloom": "Remember",
    "question": "Ký tự thoát nào sau đây được sử dụng để căn lề ngang theo từng bước Tab (Tab stop) trên màn hình Console?",
    "options": [
      "Ký hiệu \\b lùi một khoảng trắng.",
      "Ký hiệu \\r đưa con trỏ về đầu dòng hiện hành.",
      "Ký tự thoát \\t.",
      "Ký hiệu \\a phát ra âm thanh cảnh báo hệ thống qua loa máy tính."
    ],
    "correct": 2,
    "explanation": "Mục 3.4.2 Deitel: Ký tự \\t dịch chuyển con trỏ màn hình đến vị trí tab kế tiếp (Horizontal Tab), rất hữu ích khi in các bảng số liệu.",
    "answer": 2
  },
  {
    "id": 10,
    "category": "String Interpolation",
    "bloom": "Remember",
    "question": "Tính năng Định dạng chuỗi nội suy (String Interpolation) trong C# được kích hoạt bằng ký tự tiền tố nào đặt trước chuỗi?",
    "options": [
      "Dấu thăng # ở đầu chuỗi.",
      "Ký tự dấu chấm hỏi ? đặt trước tên biến bên trong khối ngoặc nhọn.",
      "Ký tự chữ a còng @ dùng để định dạng chuỗi nguyên văn bỏ qua ký tự thoát.",
      "Ký tự dollar $ đặt ngay trước dấu mở ngoặc kép của chuỗi."
    ],
    "correct": 3,
    "explanation": "Mục 3.5 Deitel: Ký tự dollar $ đặt ngay trước dấu mở ngoặc kép biến chuỗi thành một chuỗi nội suy (Interpolated string).",
    "answer": 3
  },
  {
    "id": 11,
    "category": "String Interpolation",
    "bloom": "Apply",
    "question": "Giả sử biến int age = 20; câu lệnh Console.WriteLine($\"Tuoi cua ban la {age}\"); sẽ xuất ra kết quả gì?",
    "options": [
      "Dòng văn bản: Tuoi cua ban la 20 hiển thị trọn vẹn trên màn hình.",
      "Tuoi cua ban la {age}.",
      "Lỗi biên dịch cú pháp.",
      "Dòng văn bản: Tuoi cua ban la {20} bao gồm cả hai dấu ngoặc nhọn bao quanh giá trị số."
    ],
    "correct": 0,
    "explanation": "Mục 3.5 Deitel: Trình biên dịch C# thay thế biểu thức nội suy {age} bằng giá trị thực tế của biến age tại thời điểm chạy.",
    "answer": 0
  },
  {
    "id": 12,
    "category": "String Interpolation",
    "bloom": "Understand",
    "question": "Ưu điểm vượt trội nhất của String Interpolation ($) so với phép nối chuỗi bằng toán tử cộng (+) truyền thống là gì?",
    "options": [
      "Cho phép bỏ qua hoàn toàn kiểu dữ liệu.",
      "Cú pháp trực quan, dễ bảo trì, nhúng trực tiếp biến vào biểu thức và tối ưu hóa cấp phát bộ nhớ hơn phép nối chuỗi cộng.",
      "Tự động dịch mã sang tệp nhị phân Assembly.",
      "Không cần sử dụng lớp Console."
    ],
    "correct": 1,
    "explanation": "Mục 3.5 Deitel: String Interpolation giúp mã nguồn trong sáng, dễ đọc, hạn chế lỗi nhầm lẫn dấu cách và được tối ưu hóa hiệu năng biên dịch.",
    "answer": 1
  },
  {
    "id": 13,
    "category": "Kiểu Dữ liệu & Biến",
    "bloom": "Remember",
    "question": "Kiểu dữ liệu nào trong C# được sử dụng để lưu trữ các giá trị số nguyên trong phạm vi từ khoảng -2.14 tỷ đến +2.14 tỷ?",
    "options": [
      "Kiểu dữ liệu bool chỉ lưu giá trị đúng sai.",
      "Kiểu dữ liệu string chuyên dùng lưu chuỗi văn bản.",
      "Kiểu dữ liệu double lưu trữ số thực dấu phẩy động 64-bit.",
      "Kiểu dữ liệu int."
    ],
    "correct": 3,
    "explanation": "Mục 3.6.1 Deitel: Kiểu int trong C# đại diện cho số nguyên có dấu 32-bit (System.Int32), có dải giá trị từ -2,147,483,648 đến +2,147,483,647.",
    "answer": 3
  },
  {
    "id": 14,
    "category": "Kiểu Dữ liệu & Biến",
    "bloom": "Understand",
    "question": "Quy tắc đặt tên định danh cho biến (Variable Identifier) nào sau đây là KHÔNG hợp lệ trong C#?",
    "options": [
      "Tên biến bắt đầu bằng một chữ số như 1stValue hay 2Total.",
      "Tên biến có chứa dấu gạch dưới.",
      "Tên biến sử dụng chữ in hoa và chữ in thường kết hợp theo quy ước camelCase.",
      "Tên biến có độ dài vượt quá 20 ký tự nhưng chỉ bao gồm các chữ cái hợp lệ."
    ],
    "correct": 0,
    "explanation": "Mục 3.6.1 Deitel: Tên định danh trong C# không được bắt đầu bằng chữ số (ví dụ: 1number là bất hợp lệ); chỉ được bắt đầu bằng chữ cái hoặc dấu gạch dưới _.",
    "answer": 0
  },
  {
    "id": 15,
    "category": "Nhập liệu Bàn phím",
    "bloom": "Remember",
    "question": "Phương thức Console.ReadLine() trong C# trả về kết quả thuộc kiểu dữ liệu nào sau khi người dùng nhấn Enter?",
    "options": [
      "Kiểu số nguyên int.",
      "Kiểu chuỗi ký tự string chứa toàn bộ nội dung dòng văn bản vừa nhập.",
      "Kiểu logic bool.",
      "Kiểu mảng nhị phân các byte đại diện cho mã quét phần cứng của từng phím bấm vừa gõ."
    ],
    "correct": 1,
    "explanation": "Mục 3.6.4 Deitel: Console.ReadLine() luôn đọc toàn bộ dòng ký tự từ bàn phím và trả về một đối tượng kiểu chuỗi (string).",
    "answer": 1
  },
  {
    "id": 16,
    "category": "Ép kiểu & Phân tích",
    "bloom": "Apply",
    "question": "Để chuyển đổi một chuỗi văn bản do Console.ReadLine() trả về sang số nguyên int, phương thức nào sau đây được sử dụng?",
    "options": [
      "Phương thức int.Convert().",
      "Hàm ép kiểu tĩnh (int).",
      "Phương thức int.Parse() nhận tham số là chuỗi và trả về giá trị số nguyên kiểu int tương ứng nếu cú pháp hợp lệ.",
      "Phương thức String.ToInt()."
    ],
    "correct": 2,
    "explanation": "Mục 3.6.4 Deitel: int.Parse(string) nhận vào một chuỗi ký tự biểu diễn số và chuyển đổi thành giá trị kiểu int tương ứng.",
    "answer": 2
  },
  {
    "id": 17,
    "category": "Xử lý Lỗi Ngoại lệ",
    "bloom": "Understand",
    "question": "Hiện tượng gì sẽ xảy ra nếu người dùng nhập chuỗi \"hello\" vào câu lệnh int.Parse(Console.ReadLine())?",
    "options": [
      "Ném ngoại lệ FormatException.",
      "Chương trình tự động gán giá trị 0 cho biến mà không thông báo lỗi.",
      "Trình biên dịch tự động khởi động lại máy tính để khôi phục trạng thái ban đầu.",
      "Hệ điều hành chuyển đổi chuỗi hello thành độ dài 5 ký tự và lưu vào biến số nguyên."
    ],
    "correct": 0,
    "explanation": "Mục 3.6.4 Deitel: Nếu chuỗi không thể phân tích cú pháp thành một số nguyên hợp lệ, phương thức int.Parse sẽ ném ra lỗi ngoại lệ FormatException.",
    "answer": 0
  },
  {
    "id": 18,
    "category": "Bản chất Bộ nhớ RAM",
    "bloom": "Understand",
    "question": "Bản chất kỹ thuật thực sự của một Biến (Variable) trong bộ nhớ máy tính là gì?",
    "options": [
      "Một tệp tin lưu trên ổ cứng SSD.",
      "Tên định danh đại diện cho một vị trí địa chỉ ô nhớ trong bộ nhớ RAM.",
      "Một chỉ thị lệnh được vi xử lý CPU thực thi trực tiếp trên bo mạch chủ hệ thống.",
      "Một bản ghi cơ sở dữ liệu được lưu trữ vĩnh viễn trên dịch vụ điện toán đám mây."
    ],
    "correct": 1,
    "explanation": "Mục 3.7 Deitel: Mọi biến đều có tên, kiểu, kích thước và giá trị; biến thực chất là tên định danh đại diện cho một vị trí ô nhớ trong RAM.",
    "answer": 1
  },
  {
    "id": 19,
    "category": "Bản chất Bộ nhớ RAM",
    "bloom": "Understand",
    "question": "Thao tác gán giá trị mới cho một biến đã tồn tại trong C# (ví dụ: number1 = 99;) tuân theo nguyên lý nào?",
    "options": [
      "Nguyên lý Đọc không phá hủy.",
      "Nguyên lý phân mảnh ô nhớ RAM.",
      "Nguyên lý Ghi đè phá hủy (Destructive): giá trị cũ trong ô nhớ bị xóa vĩnh viễn để nhường chỗ cho giá trị mới.",
      "Nguyên lý đồng bộ hóa dữ liệu song song và nhân bản phân tán qua hai tiến trình xử lý ngầm độc lập có giám sát chặt chẽ của hệ thống."
    ],
    "correct": 2,
    "explanation": "Mục 3.7 Deitel: Ghi giá trị vào ô nhớ là thao tác phá hủy (destructive) - giá trị cũ bị xóa hoàn toàn và thay thế bởi giá trị mới.",
    "answer": 2
  },
  {
    "id": 20,
    "category": "Bản chất Bộ nhớ RAM",
    "bloom": "Understand",
    "question": "Khi CPU đọc giá trị từ biến number1 để thực hiện phép tính cộng sum = number1 + number2, giá trị của number1 trong RAM sẽ ra sao?",
    "options": [
      "Bị xóa sạch về giá trị 0.",
      "Tự động tăng thêm 1 đơn vị.",
      "Bị hủy giải phóng khỏi RAM.",
      "Giá trị trong ô nhớ number1 vẫn được giữ nguyên vẹn không hề suy suyển vì thao tác đọc bộ nhớ là không phá hủy (non-destructive)."
    ],
    "correct": 3,
    "explanation": "Mục 3.7 Deitel: Đọc giá trị từ một vị trí bộ nhớ là thao tác không phá hủy (non-destructive) - giá trị gốc trong ô nhớ vẫn được bảo tồn.",
    "answer": 3
  },
  {
    "id": 21,
    "category": "Toán tử Số học",
    "bloom": "Remember",
    "question": "Ký hiệu nào sau đây được sử dụng để biểu diễn phép toán nhân trong ngôn ngữ C#?",
    "options": [
      "Ký tự chữ x viết thường.",
      "Dấu hoa thị *.",
      "Ký hiệu dấu chấm ở giữa biểu thức.",
      "Từ khóa multiply tích hợp sẵn trong thư viện."
    ],
    "correct": 1,
    "explanation": "Mục 3.8 Deitel: Trong C#, phép nhân sử dụng dấu sao *, phép chia dùng dấu gạch chéo /, không dùng dấu nhân x hay dấu chia hai chấm :.",
    "answer": 1
  },
  {
    "id": 22,
    "category": "Phép chia Số nguyên",
    "bloom": "Apply",
    "question": "Trong C#, kết quả của biểu thức số học 7 / 4 khi cả hai toán hạng đều là số nguyên (int) là bao nhiêu?",
    "options": [
      "Giá trị là 1.75.",
      "Giá trị là 2 do cơ chế tự động làm tròn số lên của hệ điều hành.",
      "Giá trị 1 vì phần thập phân bị cắt bỏ hoàn toàn.",
      "Chương trình báo lỗi biên dịch do không chia hết cho nhau."
    ],
    "correct": 2,
    "explanation": "Mục 3.8 Deitel: Phép chia giữa hai số nguyên là phép chia nguyên (Integer division) - phần thập phân bị cắt bỏ hoàn toàn, 7 / 4 bằng 1.",
    "answer": 2
  },
  {
    "id": 23,
    "category": "Toán tử Chia lấy dư",
    "bloom": "Apply",
    "question": "Toán tử chia lấy phần dư (%) trong C# khi áp dụng cho biểu thức 17 % 5 sẽ cho kết quả là bao nhiêu?",
    "options": [
      "Giá trị là 3.",
      "Giá trị là 3.4.",
      "Giá trị là 0 do toán tử phần trăm tự động quy đổi biểu thức về dạng tỷ lệ phần trăm.",
      "Giá trị 2 là phần dư còn lại sau phép chia số nguyên."
    ],
    "correct": 3,
    "explanation": "Mục 3.8 Deitel: Toán tử % (remainder / modulus) trả về phần dư sau phép chia nguyên: 17 chia cho 5 được 3 dư 2.",
    "answer": 3
  },
  {
    "id": 24,
    "category": "Thứ tự Ưu tiên Toán tử",
    "bloom": "Remember",
    "question": "Thứ tự ưu tiên tính toán của các toán tử số học trong C# tuân theo quy tắc chuẩn mực nào sau đây?",
    "options": [
      "Ngoặc đơn () được thực hiện trước tiên, kế đến là các phép nhân (*), chia (/), chia lấy dư (%), sau cùng là cộng (+) và trừ (-).",
      "Cộng trừ trước, nhân chia sau.",
      "Tính tuần tự từ phải sang trái.",
      "Mọi toán tử có độ ưu tiên như nhau."
    ],
    "correct": 0,
    "explanation": "Mục 3.8.3 Deitel: Biểu thức trong ngoặc () ưu tiên cao nhất, kế đến là *, /, %, thấp hơn là +, -, cùng độ ưu tiên thì tính từ trái sang phải.",
    "answer": 0
  },
  {
    "id": 25,
    "category": "Thứ tự Ưu tiên Toán tử",
    "bloom": "Apply",
    "question": "Giá trị của biểu thức C# sau đây: 2 + 3 * 4 - 6 / 2 là bao nhiêu?",
    "options": [
      "Giá trị 10 sau khi tính tuần tự.",
      "Giá trị 7 do nhầm lẫn thứ tự các phép toán cộng trừ.",
      "Giá trị 11.",
      "Giá trị 14 khi các phép tính nhân chia được thực hiện sau cùng."
    ],
    "correct": 2,
    "explanation": "Mục 3.8.3 Deitel: 3 * 4 = 12; 6 / 2 = 3; biểu thức trở thành 2 + 12 - 3 = 11.",
    "answer": 2
  },
  {
    "id": 26,
    "category": "Biểu thức Đại số",
    "bloom": "Apply",
    "question": "Để tính đa thức đại số bậc 2: y = a*x^2 + b*x + c trong C#, cách viết mã lệnh nào sau đây là chuẩn xác nhất?",
    "options": [
      "y = ax^2 + bx + c;",
      "y = (a * x)^2 + (b * x) + c;",
      "y = a * (x ^ 2) + b * x + c do ký tự mũ được hiểu là lũy thừa trong toán học.",
      "y = a * x * x + b * x + c;"
    ],
    "correct": 3,
    "explanation": "Mục 3.8.4 Deitel: Trong C# không có toán tử mũ ^ cho số học (^ là bitwise XOR), do đó x^2 phải viết thành x * x.",
    "answer": 3
  },
  {
    "id": 27,
    "category": "Cấu trúc Rẽ nhánh if",
    "bloom": "Understand",
    "question": "Biểu thức điều kiện nằm bên trong cặp dấu ngoặc đơn của câu lệnh if trong C# bắt buộc phải thuộc kiểu dữ liệu nào?",
    "options": [
      "Kiểu boolean chỉ nhận một trong hai giá trị logic là true hoặc false.",
      "Kiểu số nguyên int.",
      "Kiểu chuỗi văn bản string.",
      "Kiểu con trỏ địa chỉ ô nhớ trỏ trực tiếp đến thanh ghi điều khiển của bộ vi xử lý CPU."
    ],
    "correct": 0,
    "explanation": "Mục 3.9 Deitel: C# yêu cầu điều kiện của câu lệnh if phải là kiểu boolean (chỉ có giá trị true hoặc false), không cho phép số nguyên như C/C++.",
    "answer": 0
  },
  {
    "id": 28,
    "category": "Toán tử So sánh Quan hệ",
    "bloom": "Remember",
    "question": "Toán tử nào sau đây trong C# được sử dụng để kiểm tra điều kiện 'Hai toán hạng có giá trị bằng nhau hay không'?",
    "options": [
      "Một dấu bằng đơn = duy nhất.",
      "Cặp hai dấu bằng liền nhau == biểu thị phép so sánh bằng, phân biệt hoàn toàn với toán tử gán giá trị một dấu bằng =.",
      "Ký hiệu hai dấu gạch chéo //.",
      "Ký hiệu dấu hai chấm bằng :=."
    ],
    "correct": 1,
    "explanation": "Mục 3.9 Deitel: Toán tử kiểm tra bằng nhau trong C# là hai dấu bằng liền nhau ==, còn một dấu bằng đơn = là toán tử gán giá trị.",
    "answer": 1
  },
  {
    "id": 29,
    "category": "Toán tử So sánh Quan hệ",
    "bloom": "Remember",
    "question": "Ký hiệu nào sau đây trong C# đại diện cho toán tử so sánh 'Khác nhau' (Not equal to)?",
    "options": [
      "Ký hiệu cặp ngoặc nhọn <>.",
      "Ký hiệu dấu ngã bằng ~=.",
      "Từ khóa notequal tích hợp sẵn trong lớp Console.",
      "Toán tử !=."
    ],
    "correct": 3,
    "explanation": "Mục 3.9 Deitel: Toán tử khác nhau trong C# là != (dấu chấm than kết hợp dấu bằng).",
    "answer": 3
  },
  {
    "id": 30,
    "category": "Toán tử So sánh Quan hệ",
    "bloom": "Remember",
    "question": "Toán tử nào sau đây trong C# đại diện cho phép so sánh 'Lớn hơn hoặc bằng'?",
    "options": [
      "Toán tử >= với dấu lớn hơn đứng trước dấu bằng.",
      "Toán tử => ngược lại.",
      "Ký hiệu hai dấu lớn hơn liền nhau >> biểu thị phép dịch bit.",
      "Từ khóa greater_or_equal định nghĩa trong thư viện chuẩn .NET FCL."
    ],
    "correct": 0,
    "explanation": "Mục 3.9 Deitel: Toán tử lớn hơn hoặc bằng là >=. Viết => là sai cú pháp (=> là lambda operator trong các phiên bản sau).",
    "answer": 0
  },
  {
    "id": 31,
    "category": "Lỗi Lập trình Kinh điển",
    "bloom": "Analyze",
    "question": "Hậu quả logic nào sẽ xảy ra nếu lập trình viên vô tình đặt dấu chấm phẩy ngay sau mệnh đề điều kiện của if: if (x == y); Console.WriteLine(\"Bang nhau\");?",
    "options": [
      "Trình biên dịch báo lỗi CS1002.",
      "Dấu chấm phẩy tạo thành câu lệnh rỗng khiến lệnh in luôn luôn được thực thi bất kể x có bằng y hay không.",
      "Chương trình bị crash ngay lập tức.",
      "Hệ điều hành Windows sẽ tự động kích hoạt tính năng phục hồi lỗi cú pháp và xóa bỏ dấu chấm phẩy thừa đó của lập trình viên."
    ],
    "correct": 1,
    "explanation": "Mục 3.9 Deitel: Dấu chấm phẩy sau if tạo thành một câu lệnh rỗng (empty statement). Khối lệnh phía sau sẽ luôn luôn được thực thi dù điều kiện đúng hay sai!",
    "answer": 1
  },
  {
    "id": 32,
    "category": "Lỗi Lập trình Kinh điển",
    "bloom": "Understand",
    "question": "Tại sao trong C#, lỗi gõ nhầm if (x = 7) thay vì if (x == 7) lại được trình biên dịch phát hiện và cảnh báo ngay lập tức?",
    "options": [
      "Vì C# cấm sử dụng số 7.",
      "Vì dấu bằng đơn không có trong C#.",
      "Vì phép gán x = 7 trả về giá trị số nguyên 7, trong khi câu lệnh if trong C# bắt buộc biểu thức điều kiện phải thuộc kiểu dữ liệu boolean.",
      "Vì biến x chưa được khai báo kiểu."
    ],
    "correct": 2,
    "explanation": "Mục 3.9 Deitel: Phép gán x = 7 trả về giá trị số nguyên 7, trong khi if bắt buộc điều kiện phải là kiểu bool. Do đó C# báo lỗi type mismatch, tránh được bug nghiêm trọng của C/C++.",
    "answer": 2
  },
  {
    "id": 33,
    "category": "Từ khóa C#",
    "bloom": "Remember",
    "question": "Từ khóa nào trong C# biểu thị rằng phương thức không trả về bất kỳ giá trị nào cho lời gọi?",
    "options": [
      "Từ khóa void.",
      "Từ khóa null chỉ giá trị rỗng.",
      "Từ khóa empty khai báo chuỗi rỗng.",
      "Từ khóa return dừng thực thi khối lệnh."
    ],
    "correct": 0,
    "explanation": "Mục 3.2.5 Deitel: Từ khóa void quy định kiểu trả về rỗng, phương thức sẽ thực hiện tác vụ mà không trả dữ liệu về nơi gọi.",
    "answer": 0
  },
  {
    "id": 34,
    "category": "Môi trường Visual Studio",
    "bloom": "Understand",
    "question": "Tổ hợp phím tắt nào được sử dụng trong Visual Studio để biên dịch và chạy ứng dụng Console mà giữ cửa sổ không bị đóng ngay?",
    "options": [
      "Phím F5 chạy có gỡ lỗi.",
      "Tổ hợp phím tắt Ctrl + F5 để chạy không gỡ lỗi.",
      "Tổ hợp phím tắt Alt + F4 dùng để đóng ngay cửa sổ ứng dụng đang mở.",
      "Tổ hợp phím Ctrl + Shift + B dùng để biên dịch toàn bộ solution mà không chạy."
    ],
    "correct": 1,
    "explanation": "Mục 3.3.4 Deitel: Tổ hợp phím Ctrl + F5 (Start Without Debugging) chạy ứng dụng và tự động hiển thị dòng 'Press any key to continue...' giữ màn hình console.",
    "answer": 1
  },
  {
    "id": 35,
    "category": "Môi trường Visual Studio",
    "bloom": "Remember",
    "question": "Tính năng nào của Visual Studio tự động liệt kê danh sách các thành viên, phương thức và từ khóa gợi ý khi người dùng đang gõ mã nguồn?",
    "options": [
      "Cửa sổ Solution Explorer.",
      "Cửa sổ Output Log.",
      "Tính năng trợ giúp thông minh IntelliSense hỗ trợ tự động hoàn thiện mã nguồn.",
      "Trình biên dịch tức thời Just-In-Time Compiler chạy ngầm bên dưới hệ thống máy ảo CLR."
    ],
    "correct": 2,
    "explanation": "Mục 3.3.3 Deitel: IntelliSense là trợ lý mã nguồn thông minh giúp tự động hoàn thành từ khóa, hiển thị danh sách thành viên và tham số hàm.",
    "answer": 2
  },
  {
    "id": 36,
    "category": "Môi trường Visual Studio",
    "bloom": "Understand",
    "question": "Cửa sổ nào trong Visual Studio hiển thị danh sách các lỗi cú pháp, số dòng và mô tả chi tiết khi chương trình biên dịch thất bại?",
    "options": [
      "Cửa sổ Toolbox kéo thả.",
      "Cửa sổ Properties thiết lập.",
      "Cửa sổ Solution Explorer.",
      "Cửa sổ Error List hiển thị mã lỗi, mô tả chi tiết, số dòng và cho phép nhấp đúp chuột để nhảy đến đúng vị trí mã lỗi."
    ],
    "correct": 3,
    "explanation": "Mục 3.3.5 Deitel: Cửa sổ Error List liệt kê toàn bộ các lỗi cú pháp (Syntax errors) và cảnh báo (Warnings), cho phép nhấp đúp để nhảy ngay đến dòng lỗi.",
    "answer": 3
  },
  {
    "id": 37,
    "category": "Thứ tự Ưu tiên Toàn diện",
    "bloom": "Remember",
    "question": "Trong tất cả các toán tử sau đây: (+, ==, *, =), toán tử nào có mức độ ưu tiên tính toán THẤP NHẤT?",
    "options": [
      "Toán tử nhân *.",
      "Toán tử gán =.",
      "Toán tử cộng số học +.",
      "Toán tử so sánh bằng nhau ==."
    ],
    "correct": 1,
    "explanation": "Mục 3.9 & Hình 3.23 Deitel: Toán tử gán = có độ ưu tiên thấp nhất để đảm bảo toàn bộ phép tính toán và so sánh hoàn tất xong mới gán kết quả vào biến.",
    "answer": 1
  },
  {
    "id": 38,
    "category": "Khoảng trắng & Định dạng",
    "bloom": "Understand",
    "question": "Khái niệm khoảng trắng (Whitespace) trong C# bao gồm những thành phần nào sau đây?",
    "options": [
      "Chỉ bao gồm dấu cách đơn lẻ.",
      "Chỉ các khối chú thích XML bắt đầu bằng ba dấu gạch chéo /// trong phần đầu tệp tin.",
      "Các ký tự dấu cách, dấu tab, ký tự xuống dòng và dòng trống trong mã nguồn.",
      "Toàn bộ các dòng mã lệnh chứa phương thức Main được đánh dấu đặc biệt bởi lập trình viên."
    ],
    "correct": 2,
    "explanation": "Mục 3.2.3 Deitel: Whitespace bao gồm ký tự dấu cách (space), ký tự tab, ký tự xuống dòng (newline) và dòng trống; trình biên dịch bỏ qua các khoảng trắng thừa.",
    "answer": 2
  },
  {
    "id": 39,
    "category": "Toán tử Số học",
    "bloom": "Apply",
    "question": "Để kết quả phép chia 7 / 4 trong C# nhận được giá trị số thực chính xác là 1.75, lập trình viên cần viết biểu thức như thế nào?",
    "options": [
      "Viết phép tính là 7 : 4.",
      "Thêm dấu chấm phẩy vào sau số 4.",
      "Bắt buộc phải khai báo lại toàn bộ các biến số nguyên trong chương trình thành kiểu chuỗi ký tự string.",
      "Viết ít nhất một toán hạng dưới dạng số thực như 7.0 / 4 hoặc (double)7 / 4."
    ],
    "correct": 3,
    "explanation": "Mục 3.8 Deitel: Muốn kết quả phép chia là số thực, ít nhất một trong hai toán hạng phải là số thực (ví dụ: 7.0 / 4 hoặc 7 / 4.0 hoặc ép kiểu (double)7 / 4).",
    "answer": 3
  },
  {
    "id": 40,
    "category": "Tổng kết Chương 3",
    "bloom": "Understand",
    "question": "Quy trình chuẩn mực 3 bước của một ứng dụng Console nhập dữ liệu, tính toán và hiển thị kết quả trong C# là gì?",
    "options": [
      "Bước 1: Nhắc và đọc chuỗi từ bàn phím bằng Console.ReadLine rồi ép kiểu với int.Parse; Bước 2: Thực hiện tính toán số học trong bộ nhớ RAM; Bước 3: Xuất kết quả ra màn hình với Console.WriteLine sử dụng String Interpolation $.",
      "Bước 1: Tạo Form; Bước 2: Kéo thả Button; Bước 3: Đổi màu BackColor.",
      "Bước 1: Khởi động máy ảo CLR; Bước 2: Dịch mã sang MSIL; Bước 3: Tắt máy.",
      "Bước 1: Đọc bàn phím; Bước 2: Ghi dữ liệu ra tệp tin; Bước 3: Gửi email."
    ],
    "correct": 0,
    "explanation": "Mục 3.6 Deitel: Quy trình kinh điển của chương trình Addition.cs gồm: 1) Nhập chuỗi từ bàn phím qua Console.ReadLine và ép kiểu bằng int.Parse; 2) Tính toán số học trong bộ nhớ RAM; 3) Xuất kết quả qua Console.WriteLine bằng String Interpolation $.",
    "answer": 0
  }
];

if (typeof window !== 'undefined') {
  window.QUIZ_CHAPTER_01 = (typeof QUIZ_CHAPTER_01 !== 'undefined') ? QUIZ_CHAPTER_01 : [];
  window.QUIZ_CHAPTER_02 = (typeof QUIZ_CHAPTER_02 !== 'undefined') ? QUIZ_CHAPTER_02 : [];
  window.QUIZ_CHAPTER_03 = QUIZ_CHAPTER_03;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { QUIZ_CHAPTER_01, QUIZ_CHAPTER_02, QUIZ_CHAPTER_03 };
}
