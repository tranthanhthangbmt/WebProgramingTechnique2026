// ============================================================================
// HỌC PHẦN: KỸ THUẬT LẬP TRÌNH (4 TÍN CHỈ) - IT26M
// NGÂN HÀNG CÂU HỎI TRẮC NGHIỆM CHƯƠNG 1: INTRODUCTION TO JAVA PROGRAMMING
// ĐẶC TẢ: 40 CÂU HỎI CHUẨN HÓA, ĐỘ DÀI CÁC PHƯƠNG ÁN LỰA CHỌN LÀ NGẪU NHIÊN
// ============================================================================

const QUIZ_CHAPTER_01 = [
  // --- NHÓM 1: HỆ THỐNG TÍNH TOÁN, PHẦN CỨNG & HỆ NHỊ PHÂN (CÂU 1 - 8) ---
  {
    id: 1,
    category: "Nền tảng Tính toán",
    bloom: "Understand",
    question: "Theo Giáo sư Donald Knuth (nhà khoa học máy tính đoạt giải Turing), một người chỉ thực sự hiểu thấu đáo một vấn đề khi nào?",
    options: [
      "Khi dạy lại vấn đề đó cho một chiếc máy tính dưới dạng một thuật toán rõ ràng.",
      "Khi đạt điểm tối đa trong kỳ thi chuyên ngành.",
      "Lúc giảng giải được cho người khác hiểu.",
      "Khi tự tay viết xong 1.000 dòng code không có lỗi."
    ],
    correct: 0,
    explanation: "Trích dẫn nguyên văn giáo trình trang 6: 'Actually a person does not really understand something until after teaching it to a computer, i.e., expressing it as an algorithm.' (Một người không thực sự hiểu điều gì cho đến khi dạy nó cho máy tính dưới dạng thuật toán)."
  },
  {
    id: 2,
    category: "Phần cứng Máy tính",
    bloom: "Remember",
    question: "Thành phần phần cứng nào đóng vai trò là 'bộ não' của máy tính, trực tiếp thực thi các chỉ thị và phép toán?",
    options: [
      "Bộ nhớ RAM",
      "Ổ đĩa cứng SSD lưu trữ vĩnh viễn",
      "CPU (Central Processing Unit)",
      "Bộ nguồn máy tính cung cấp điện áp ổn định cho bo mạch chủ"
    ],
    correct: 2,
    explanation: "CPU (Central Processing Unit) là bộ xử lý trung tâm, đóng vai trò như bộ não điều phối và thực thi các lệnh chương trình."
  },
  {
    id: 3,
    category: "Phần cứng Máy tính",
    bloom: "Understand",
    question: "Điểm khác biệt cốt lõi giữa Bộ nhớ chính (RAM) và Bộ nhớ thứ cấp (Ổ cứng SSD/HDD) là gì?",
    options: [
      "RAM có dung lượng lớn hơn ổ cứng nhiều lần.",
      "RAM lưu tạm thời và mất dữ liệu khi mất nguồn điện, còn ổ cứng lưu trữ vĩnh viễn.",
      "Ổ cứng truy xuất nhanh hơn RAM.",
      "RAM chỉ chứa hình ảnh và video giải trí của người dùng."
    ],
    correct: 1,
    explanation: "RAM là bộ nhớ khả biến (volatile), tốc độ cao nhưng mất dữ liệu khi tắt máy. Ổ cứng là bộ nhớ bất biến (non-volatile) dùng để lưu file lâu dài."
  },
  {
    id: 4,
    category: "Hệ nhị phân",
    bloom: "Understand",
    question: "Tại sao phần cứng máy tính hiện đại lại biểu diễn dữ liệu bằng Hệ nhị phân (chỉ gồm các chữ số 0 và 1)?",
    options: [
      "Vì các nhà toán học thế kỷ 19 quy định như vậy để bảo mật.",
      "Để tiết kiệm dung lượng giấy in kết quả.",
      "Vì CPU chỉ có thể đọc được bảng chữ cái tiếng Anh.",
      "Do phần cứng cấu tạo từ bóng bán dẫn (transistor), việc duy trì và phân biệt 2 trạng thái bật/tắt (điện áp cao/thấp) là đơn giản, bền vững và chính xác nhất."
    ],
    correct: 3,
    explanation: "Phần cứng vật lý dựa trên các mạch điện tử bán dẫn. Hai trạng thái đóng/ngắt mạch hoặc điện thế cao/thấp là phương án kỹ thuật ổn định và chống nhiễu tin cậy nhất."
  },
  {
    id: 5,
    category: "Hệ nhị phân",
    bloom: "Apply",
    question: "Số nhị phân (1011)₂ tương ứng với giá trị nào trong hệ thập phân (Base-10)?",
    options: [
      "11",
      "13",
      "9 (được tính bằng cách lấy tám cộng một)",
      "15"
    ],
    correct: 0,
    explanation: "(1011)₂ = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 8 + 0 + 2 + 1 = 11 trong hệ thập phân."
  },
  {
    id: 6,
    category: "Hệ nhị phân",
    bloom: "Apply",
    question: "Số thập phân 44 khi chuyển đổi sang hệ nhị phân (Base-2) sẽ có giá trị là gì?",
    options: [
      "101100₂",
      "110010₂ (tương đương ba mươi hai cộng mười sáu cộng hai)",
      "100110₂",
      "111000₂"
    ],
    correct: 0,
    explanation: "44 = 32 + 8 + 4 = 1×2⁵ + 0×2⁴ + 1×2³ + 1×2² + 0×2¹ + 0×2⁰ = 101100₂."
  },
  {
    id: 7,
    category: "Hệ nhị phân",
    bloom: "Remember",
    question: "Một Byte (gồm 8 bits) có thể biểu diễn được bao nhiêu trạng thái/giá trị khác nhau?",
    options: [
      "128 trạng thái",
      "256 trạng thái (từ 0 đến 255)",
      "64 giá trị số",
      "1024 trạng thái khác nhau tương ứng với một kilobyte dung lượng bộ nhớ"
    ],
    correct: 1,
    explanation: "Với 8 bit, số lượng trạng thái có thể biểu diễn là 2⁸ = 256 giá trị (từ 0 đến 255)."
  },
  {
    id: 8,
    category: "Nền tảng Tính toán",
    bloom: "Understand",
    question: "Một chuỗi các chỉ thị từng bước rõ ràng, hữu hạn, không nhập nhằng nhằm giải quyết một bài toán cụ thể được gọi là gì?",
    options: [
      "Mã máy (Machine code)",
      "Trình biên dịch (Compiler)",
      "Thuật toán (Algorithm)",
      "Hệ điều hành Windows"
    ],
    correct: 2,
    explanation: "Thuật toán (Algorithm) là tập hợp hữu hạn các chỉ thị được định nghĩa rõ ràng để hoàn thành một nhiệm vụ hoặc tính toán."
  },

  // --- NHÓM 2: TRÌNH BIÊN DỊCH, MÁY ẢO JVM & TRIẾT LÝ WORA (CÂU 9 - 16) ---
  {
    id: 9,
    category: "Biên dịch & Thông dịch",
    bloom: "Understand",
    question: "Nhược điểm lớn nhất của các ngôn ngữ biên dịch trực tiếp ra mã máy truyền thống (như C hoặc C++) là gì?",
    options: [
      "Mã thực thi bị phụ thuộc hoàn toàn vào nền tảng kiến trúc phần cứng và hệ điều hành cụ thể, không thể chạy chéo trên các hệ máy khác nhau mà không biên dịch lại.",
      "Tốc độ chạy quá chậm.",
      "Không hỗ trợ lập trình hướng đối tượng.",
      "Mã nguồn bị mất sau khi chạy."
    ],
    correct: 0,
    explanation: "Mã máy tạo bởi C/C++ là Native Code (cho Intel x86, ARM, v.v.), do đó file chạy trên Windows x86 sẽ không thể chạy trên Mac ARM hay Linux."
  },
  {
    id: 10,
    category: "Kiến trúc Java",
    bloom: "Remember",
    question: "Triết lý nổi tiếng mà Sun Microsystems đặt ra cho ngôn ngữ Java khi ra mắt năm 1995 là gì?",
    options: [
      "Code Once, Debug Everywhere",
      "Compile Fast, Run Native",
      "Write Once, Run Anywhere (WORA)",
      "Pure Speed Above All Else"
    ],
    correct: 2,
    explanation: "'Write Once, Run Anywhere' (WORA) là khẩu hiệu cốt lõi thể hiện tính độc lập nền tảng của Java."
  },
  {
    id: 11,
    category: "Kiến trúc Java",
    bloom: "Understand",
    question: "Java Bytecode thực chất là gì?",
    options: [
      "Tập lệnh nhị phân chuẩn dành riêng cho máy ảo Java Virtual Machine (JVM).",
      "Mã nguồn viết bằng tiếng Anh.",
      "Mã máy chạy trực tiếp trên chip Intel.",
      "File cấu hình giao diện người dùng của phần mềm lập trình Eclipse."
    ],
    correct: 0,
    explanation: "Bytecode là tập lệnh máy trung gian của máy ảo JVM, được lưu trữ trong các file có phần mở rộng .class."
  },
  {
    id: 12,
    category: "Kiến trúc Java",
    bloom: "Understand",
    question: "Vai trò then chốt của máy ảo Java Virtual Machine (JVM) trong quá trình thực thi ứng dụng là gì?",
    options: [
      "Quét và tiêu diệt virus xâm nhập máy tính.",
      "Nạp Bytecode (.class) và thông dịch hoặc JIT-compile sang mã máy thực của hệ điều hành sở tại để CPU chạy.",
      "Tự động viết code thay cho lập trình viên.",
      "Vẽ giao diện đồ họa cửa sổ cho hệ điều hành Windows."
    ],
    correct: 1,
    explanation: "JVM đóng vai trò cầu nối: nó nạp file bytecode (.class) và chuyển đổi thành mã máy thực của máy tính đang chạy."
  },
  {
    id: 13,
    category: "Kiến trúc Java",
    bloom: "Analyze",
    question: "Mối quan hệ chính xác giữa ba khái niệm JDK, JRE và JVM là gì?",
    options: [
      "JDK chứa JRE; JRE chứa JVM và thư viện chuẩn.",
      "JVM chứa JDK; JDK chứa JRE.",
      "Cả ba là tên gọi khác nhau của cùng một phần mềm.",
      "JRE là công cụ chỉ dùng riêng cho lập trình viên chuyên nghiệp để dịch code C++ sang Java."
    ],
    correct: 0,
    explanation: "JDK (Java Development Kit) = JRE + Tools (javac, debugger). JRE (Java Runtime Environment) = JVM + Class Libraries."
  },
  {
    id: 14,
    category: "Quy trình phát triển",
    bloom: "Remember",
    question: "Trong quy trình phát triển Java (Hình 1.1 giáo trình), câu lệnh nào được dùng để biên dịch file mã nguồn `Hello.java`?",
    options: [
      "run Hello.java",
      "java Hello.java",
      "javac Hello.java",
      "compile Hello"
    ],
    correct: 2,
    explanation: "Lệnh 'javac' (Java Compiler) dùng để biên dịch mã nguồn .java thành file bytecode .class."
  },
  {
    id: 15,
    category: "Quy trình phát triển",
    bloom: "Remember",
    question: "Sau khi biên dịch thành công file `Hello.java`, lệnh nào trong terminal được sử dụng để khởi động JVM chạy chương trình?",
    options: [
      "java Hello",
      "javac Hello.class",
      "run Hello.exe",
      "execute Hello"
    ],
    correct: 0,
    explanation: "Để chạy chương trình, ta dùng lệnh 'java <TênClass>', không kèm đuôi file: ví dụ 'java Hello'."
  },
  {
    id: 16,
    category: "Quy trình phát triển",
    bloom: "Understand",
    question: "File nào sau đây chứa Java Bytecode không dành cho con người đọc trực tiếp?",
    options: [
      "Hello.txt",
      "Hello.class",
      "Hello.java",
      "Hello.c"
    ],
    correct: 1,
    explanation: "File .class là file nhị phân chứa bytecode sau khi được javac biên dịch từ file mã nguồn .java."
  },

  // --- NHÓM 3: CẤU TRÚC CHƯƠNG TRÌNH JAVA & LỆNH XUẤT DỮ LIỆU (CÂU 17 - 24) ---
  {
    id: 17,
    category: "Cú pháp cơ bản",
    bloom: "Remember",
    question: "Quy tắc bắt buộc đối với mọi mã lệnh trong ngôn ngữ lập trình Java là gì?",
    options: [
      "Mọi mã lệnh đều phải nằm bên trong một lớp (class).",
      "Phải khai báo ít nhất 5 biến số.",
      "Phải có lệnh đồ họa vẽ hình tròn.",
      "Mã lệnh phải viết trên cùng một dòng duy nhất để tăng tốc độ."
    ],
    correct: 0,
    explanation: "Trong Java, tính đóng gói rất cao: không có hàm hay câu lệnh nào được tồn tại tự do bên ngoài class."
  },
  {
    id: 18,
    category: "Cú pháp cơ bản",
    bloom: "Apply",
    question: "Nếu một chương trình Java có khai báo `public class WelcomeIT26M`, thì file mã nguồn bắt buộc phải lưu với tên nào?",
    options: [
      "welcomeit26m.java",
      "WelcomeIT26M.class",
      "WelcomeIT26M.java",
      "Welcome_IT26M.java"
    ],
    correct: 2,
    explanation: "Tên file mã nguồn .java bắt buộc phải trùng khớp 100% từng chữ hoa chữ thường với tên của public class."
  },
  {
    id: 19,
    category: "Cú pháp cơ bản",
    bloom: "Remember",
    question: "Ký hiệu nào được dùng để xác định phần mở đầu và kết thúc của một khối lệnh (scope) trong Java?",
    options: [
      "Cặp dấu ngoặc đơn ( )",
      "Cặp dấu ngoặc nhọn { }",
      "Cặp dấu ngoặc vuông [ ]",
      "Cặp từ khóa BEGIN và END"
    ],
    correct: 1,
    explanation: "Cặp dấu ngoặc nhọn { } dùng để đóng gói phạm vi khối lệnh của class, phương thức hoặc cấu trúc điều khiển."
  },
  {
    id: 20,
    category: "Cú pháp cơ bản",
    bloom: "Understand",
    question: "Dòng tiêu đề phương thức nào là điểm bắt đầu thực thi hợp lệ của mọi chương trình Java độc lập?",
    options: [
      "public static void Main(String args)",
      "public void main(String[] args)",
      "public static void main(String[] args)",
      "static void main()"
    ],
    correct: 2,
    explanation: "Tiêu đề chuẩn bắt buộc là 'public static void main(String[] args)'. Chú ý 'main' viết thường."
  },
  {
    id: 21,
    category: "Cú pháp cơ bản",
    bloom: "Understand",
    question: "Từ khóa `void` trong khai báo hàm `main` biểu thị điều gì?",
    options: [
      "Phương thức này chạy vô hạn lần.",
      "Phương thức thực hiện nhiệm vụ và không trả lại bất kỳ giá trị nào.",
      "Phương thức này bị lỗi không thể gọi được.",
      "Phương thức chỉ nhận số nguyên làm dữ liệu đầu vào."
    ],
    correct: 1,
    explanation: "'void' là kiểu trả về rỗng, báo cho trình biên dịch biết phương thức này không trả về giá trị (no return value)."
  },
  {
    id: 22,
    category: "Lệnh xuất dữ liệu",
    bloom: "Understand",
    question: "Sự khác biệt chính giữa lệnh `System.out.println()` và `System.out.print()` là gì?",
    options: [
      "`println` in xong tự động nhảy xuống dòng mới (newline), còn `print` giữ nguyên con trỏ ở cuối nội dung vừa in.",
      "`print` in nhanh hơn `println` 100 lần.",
      "`println` chỉ in được số thực.",
      "`print` tự động thêm dấu chấm phẩy vào cuối chuỗi văn bản."
    ],
    correct: 0,
    explanation: "println (print line) in xong sẽ tạo ký tự xuống dòng mới, trong khi print giữ nguyên vị trí con trỏ in tiếp theo."
  },
  {
    id: 23,
    category: "Lệnh xuất dữ liệu",
    bloom: "Apply",
    question: "Đoạn mã sau sẽ in ra màn hình nội dung gì?\n`System.out.print(\"A\");`\n`System.out.println(\"B\");`\n`System.out.print(\"C\");`",
    options: [
      "AB trên dòng thứ nhất, C trên dòng thứ hai.",
      "Ba chữ A, B, C mỗi chữ nằm trên một dòng riêng biệt.",
      "A trên dòng 1, BC trên dòng 2.",
      "ABC trên cùng một dòng duy nhất."
    ],
    correct: 0,
    explanation: "'A' được in (giữ nguyên dòng), 'B' được in tiếp ngay sau 'A' rồi nhảy xuống dòng, sau đó 'C' được in ở dòng mới -> 'AB' ở dòng 1 và 'C' ở dòng 2."
  },
  {
    id: 24,
    category: "Cú pháp cơ bản",
    bloom: "Remember",
    question: "Lệnh nào sau đây dùng để tạo ra một dòng trống trên màn hình console?",
    options: [
      "System.out.println(\"\");",
      "System.out.print(\"\");",
      "System.out.println();",
      "Cả phương án A và C đều đúng."
    ],
    correct: 3,
    explanation: "Cả System.out.println(); (không đối số) và System.out.println(\"\"); đều đẩy con trỏ xuống dòng mới, tạo ra 1 dòng trống."
  },

  // --- NHÓM 4: CHUỖI, KÝ TỰ THOÁT & PHONG CÁCH LẬP TRÌNH (CÂU 25 - 32) ---
  {
    id: 25,
    category: "Ký tự thoát",
    bloom: "Understand",
    question: "Ký tự nào được dùng làm tiền tố mở đầu cho một ký tự thoát (Escape Sequence) trong Java?",
    options: [
      "Dấu gạch chéo xuôi ( / )",
      "Dấu thăng ( # )",
      "Dấu gạch chéo ngược ( \\ )",
      "Dấu và ( & )"
    ],
    correct: 2,
    explanation: "Dấu gạch chéo ngược backslash ( \\ ) là ký tự thoát, dùng kết hợp với ký tự kế tiếp (ví dụ \\n, \\t, \\\", \\\\)."
  },
  {
    id: 26,
    category: "Ký tự thoát",
    bloom: "Apply",
    question: "Để in ra màn hình chính xác câu: `Cô ấy nói: \"Xin chào!\"`, câu lệnh Java nào sau đây là hợp lệ?",
    options: [
      "System.out.println(\"Cô ấy nói: \"Xin chào!\"\");",
      "System.out.println(\"Cô ấy nói: \\\"Xin chào!\\\"\");",
      "System.out.println('Cô ấy nói: \"Xin chào!\"');",
      "System.out.print(\"Cô ấy nói: /\"Xin chào!/\"\");"
    ],
    correct: 1,
    explanation: "Để in dấu ngoặc kép bên trong một chuỗi, ta bắt buộc phải sử dụng ký tự thoát \\\" để compiler không nhầm lẫn là dấu đóng chuỗi."
  },
  {
    id: 27,
    category: "Ký tự thoát",
    bloom: "Apply",
    question: "Để in ra màn hình đường dẫn tệp `C:\\Java\\IT26M`, lập trình viên phải viết chuỗi trong lệnh println như thế nào?",
    options: [
      "\"C:\\Java\\IT26M\"",
      "\"C:\\\\Java\\\\IT26M\"",
      "\"C:/Java/IT26M\"",
      "\"C:\\new Java\\tab IT26M\""
    ],
    correct: 1,
    explanation: "Dấu gạch chéo ngược đơn lẻ \\ mang ý nghĩa thoát, do đó để in 1 dấu \\ thật sự, ta phải viết hai dấu gạch chéo liên tiếp: \\\\."
  },
  {
    id: 28,
    category: "Ký tự thoát",
    bloom: "Remember",
    question: "Ký tự thoát `\\t` có tác dụng gì khi in ra màn hình console?",
    options: [
      "Tắt chương trình ngay lập tức.",
      "Tạo một khoảng thụt lề tab (căn chỉnh cột).",
      "Tạo một tiếp đầu ngữ màu đỏ.",
      "Thêm ngày giờ hiện tại của hệ điều hành."
    ],
    correct: 1,
    explanation: "'\\t' chèn một ký tự Tab, dịch con trỏ đến vị trí tab stop kế tiếp để căn chỉnh bảng cột thẳng hàng."
  },
  {
    id: 29,
    category: "Định danh & Từ khóa",
    bloom: "Apply",
    question: "Tên định danh (Identifier) nào sau đây là KHÔNG hợp lệ trong Java?",
    options: [
      "total_score",
      "2ndAttempt",
      "_count",
      "$money"
    ],
    correct: 1,
    explanation: "Định danh trong Java tuyệt đối KHÔNG được bắt đầu bằng chữ số (2ndAttempt vi phạm quy tắc này)."
  },
  {
    id: 30,
    category: "Định danh & Từ khóa",
    bloom: "Remember",
    question: "Từ nào sau đây KHÔNG PHẢI là từ khóa dành riêng (reserved keyword) của Java?",
    options: [
      "class",
      "program",
      "public",
      "static"
    ],
    correct: 1,
    explanation: "'program' không phải là từ khóa trong Java (nó là từ khóa trong Pascal). Java dùng 'class', 'public', 'static', 'void'..."
  },
  {
    id: 31,
    category: "Phong cách lập trình",
    bloom: "Understand",
    question: "Theo quy ước đặt tên CamelCase chuẩn trong Java, tên Phương thức (Method) nên được viết theo dạng nào?",
    options: [
      "UpperCamelCase (viết hoa mọi chữ cái đầu: DrawRocket)",
      "ALL_CAPS (viết hoa toàn bộ: DRAW_ROCKET)",
      "lowerCamelCase (chữ đầu viết thường, viết hoa các từ sau: drawRocket)",
      "kebab-case (nối dấu gạch ngang: draw-rocket)"
    ],
    correct: 2,
    explanation: "Quy ước chuẩn Java: Tên Lớp viết UpperCamelCase (StudentManager); Tên Phương thức và Biến viết lowerCamelCase (drawDiamond, totalScore)."
  },
  {
    id: 32,
    category: "Phong cách lập trình",
    bloom: "Remember",
    question: "Loại chú thích nào trong Java bắt đầu bằng `/**` và kết thúc bằng `*/`, thường dùng để sinh tài liệu API?",
    options: [
      "Chú thích một dòng (Single-line comment)",
      "Chú thích tài liệu Javadoc",
      "Chú thích trình biên dịch compiler",
      "Khối lệnh ẩn"
    ],
    correct: 1,
    explanation: "Cặp /** ... */ là Javadoc comment, được công cụ javadoc đọc để tự động sinh tài liệu chuẩn HTML cho thư viện."
  },

  // --- NHÓM 5: CHẨN ĐOÁN LỖI & PHÂN RÃ THỦ TỤC (CÂU 33 - 40) ---
  {
    id: 33,
    category: "Chẩn đoán Lỗi",
    bloom: "Understand",
    question: "Lỗi cú pháp (Syntax Error / Compile-time Error) được phát hiện vào thời điểm nào?",
    options: [
      "Khi người dùng đang sử dụng ứng dụng.",
      "Trong giai đoạn biên dịch bằng lệnh javac, trước khi file .class được tạo ra.",
      "Khi máy tính bị hết pin đột ngột.",
      "Sau khi chương trình đã chạy xong và in ra kết quả."
    ],
    correct: 1,
    explanation: "Lỗi cú pháp là lỗi ngữ pháp (quên dấu chấm phẩy, sai chính tả từ khóa), được trình biên dịch phát hiện ngay khi dịch mã."
  },
  {
    id: 34,
    category: "Chẩn đoán Lỗi",
    bloom: "Understand",
    question: "Chương trình biên dịch tốt, chạy không bị sập nhưng kết quả in ra màn hình bị sai so với yêu cầu thuộc loại lỗi nào?",
    options: [
      "Lỗi cú pháp (Syntax error)",
      "Lỗi thực thi (Runtime exception)",
      "Lỗi phần cứng (Hardware failure)",
      "Lỗi ngữ nghĩa / logic (Logic error / Intent error)"
    ],
    correct: 3,
    explanation: "Lỗi logic xảy ra khi thuật toán hoặc phép tính bị sai lệch mục đích thiết kế, chương trình vẫn chạy nhưng cho đáp số sai."
  },
  {
    id: 35,
    category: "Chẩn đoán Lỗi",
    bloom: "Apply",
    question: "Kinh nghiệm vàng quan trọng nhất khi đọc danh sách dài các lỗi do trình biên dịch `javac` thông báo là gì?",
    options: [
      "Luôn tập trung sửa lỗi đầu tiên trong danh sách, vì một lỗi ở dòng trên có thể gây ra hiệu ứng domino sinh ra nhiều lỗi giả phía dưới.",
      "Chỉ sửa lỗi cuối cùng dưới đáy màn hình.",
      "Bỏ qua thông báo lỗi và bấm chạy lại nhiều lần.",
      "Xóa toàn bộ chương trình và viết lại từ đầu."
    ],
    correct: 0,
    explanation: "Trình biên dịch phân tích tuần tự từ trên xuống. Một dấu ngoặc mở hoặc dấu chấm phẩy thiếu ở dòng 3 có thể làm compiler hiểu sai hàng chục dòng tiếp theo."
  },
  {
    id: 36,
    category: "Phân rã thủ tục",
    bloom: "Understand",
    question: "Tư duy Phân rã Top-down (Procedural Decomposition) trong lập trình có nghĩa là gì?",
    options: [
      "Viết toàn bộ code vào một hàm duy nhất để tiết kiệm bộ nhớ.",
      "Chia bài toán phức tạp ban đầu thành các bài toán con nhỏ hơn, rồi tiếp tục chia nhỏ cho đến khi thành các thao tác đơn giản dễ quản lý.",
      "Xóa bỏ các hàm con để máy tính chạy nhanh hơn.",
      "Tự động dịch mã Java sang mã C++."
    ],
    correct: 1,
    explanation: "Top-down decomposition (Chia để trị) chia nhiệm vụ lớn thành các nhiệm vụ con, giúp giải quyết bài toán phức tạp một cách có cấu trúc."
  },
  {
    id: 37,
    category: "Phân rã thủ tục",
    bloom: "Understand",
    question: "Nguyên lý cốt lõi 'DRY' trong kỹ nghệ phần mềm là viết tắt của cụm từ nào?",
    options: [
      "Do Right Yourself",
      "Don't Repeat Yourself",
      "Dynamic Routing Yield",
      "Debug Rapidly Yearly"
    ],
    correct: 1,
    explanation: "DRY nghĩa là 'Don't Repeat Yourself' - Đừng lặp lại chính mình, nhằm triệt tiêu sự trùng lặp mã nguồn trong chương trình."
  },
  {
    id: 38,
    category: "Phương thức tĩnh",
    bloom: "Apply",
    question: "Khi một phương thức được gọi thực thi (ví dụ `drawBox();`), CPU sẽ xử lý luồng điều khiển (Flow of Control) như thế nào?",
    options: [
      "CPU chạy song song hai hàm cùng một lúc.",
      "CPU tạm dừng hàm gọi (main), nhảy sang thực thi các câu lệnh trong thân hàm con, khi gặp dấu ngoặc đóng } thì quay trở lại tiếp tục dòng kế tiếp của hàm gọi.",
      "CPU khởi động lại toàn bộ máy tính.",
      "CPU xóa hàm con khỏi bộ nhớ vĩnh viễn."
    ],
    correct: 1,
    explanation: "Cơ chế Transfer of Control: Lưu vị trí hiện tại, chuyển quyền sang hàm con thực thi, sau đó Return quay về đúng điểm hẹn để chạy tiếp."
  },
  {
    id: 39,
    category: "Phương thức tĩnh",
    bloom: "Analyze",
    question: "Cấu trúc dữ liệu nào trong bộ nhớ RAM được máy tính sử dụng để ghi nhớ thứ tự các điểm quay về khi các hàm gọi lồng nhau?",
    options: [
      "Ngăn xếp gọi hàm (Call Stack - LIFO: Vào sau ra trước)",
      "Hàng đợi (Queue - FIFO: Vào trước ra trước)",
      "Bảng băm (Hash Table)",
      "Cây nhị phân tìm kiếm (Binary Search Tree)"
    ],
    correct: 0,
    explanation: "Call Stack hoạt động theo cơ chế LIFO (Last-In, First-Out): hàm nào được gọi sau cùng sẽ thực thi xong trước và được lấy ra khỏi stack."
  },
  {
    id: 40,
    category: "Case Study DrawFigures",
    bloom: "Analyze",
    question: "Trong Case Study `DrawFigures`, điểm vượt trội của Phiên bản 3 (DrawFigures3) so với Phiên bản 2 (DrawFigures2) là gì?",
    options: [
      "Phiên bản 3 dùng nhiều dòng lệnh hơn.",
      "Phiên bản 3 có thêm giao diện cửa sổ 3D.",
      "Phiên bản 3 phân rã hoàn chỉnh 2 cấp, tách các khối nguyên thủy tái sử dụng (drawCone, drawV, drawBox), triệt tiêu 100% việc lặp lại mã in hình.",
      "Phiên bản 3 chỉ chạy được trên điện thoại di động."
    ],
    correct: 2,
    explanation: "DrawFigures3 thiết kế theo kiến trúc 3 tầng: main điều phối -> các hình lớn -> các khối nguyên thủy tái sử dụng tối đa, loại bỏ hoàn toàn trùng lặp."
  }
];

if (typeof module !== 'undefined' && module.exports) {
  module.exports = QUIZ_CHAPTER_01;
}

