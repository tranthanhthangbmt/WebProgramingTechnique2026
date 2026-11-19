// ============================================================================
// HỌC PHẦN: KỸ THUẬT LẬP TRÌNH (4 TÍN CHỈ) - IT26M
// EXERCISES DATABASE: CHAPTERS 1, 2, 3, 4
// ============================================================================

const EXERCISES_CHAPTER_01 = [
  {
    "id": "sre-1.1",
    "type": "self-review",
    "category": "1.3 Hardware & Data Hierarchy",
    "number": "Self-Review 1.1",
    "page": 67,
    "title": "Điền vào chỗ trống: Khái niệm Máy tính, Phần cứng & Phân cấp dữ liệu",
    "description": "Điền từ hoặc cụm từ thích hợp vào chỗ trống trong các phát biểu sau:\na) Máy tính xử lý dữ liệu dưới sự điều khiển của các chuỗi chỉ thị được gọi là ________.\nb) Một chiếc máy tính bao gồm nhiều thiết bị vật lý khác nhau được gọi là ________, ví dụ: bàn phím, màn hình, chuột, ổ cứng, bộ nhớ, ổ DVD và các khối xử lý.\nc) Các phần tử dữ liệu được xử lý bởi máy tính tạo thành một ________, có cấu trúc ngày càng lớn hơn và phức tạp hơn khi đi từ các phần tử đơn giản nhất ('bit') đến các phần tử phong phú hơn như ký tự, trường dữ liệu, v.v.\nd) Máy tính chỉ có thể trực tiếp hiểu được ngôn ngữ ________ của chính nó, chỉ bao gồm các số 1 và 0.\ne) Ba loại ngôn ngữ lập trình máy tính được thảo luận trong chương này là ngôn ngữ máy, ________ và ________.\nf) Các chương trình dùng để dịch chương trình ngôn ngữ bậc cao sang ngôn ngữ máy được gọi là ________.\ng) Một bộ vi xử lý ________ tích hợp nhiều vi xử lý trên cùng một vi mạch bán dẫn (microchip)—bộ vi xử lý lõi kép (dual-core) có 2 CPU và bộ vi xử lý lõi tứ (quad-core) có 4 CPU.\nh) Windows 10 đã giới thiệu nền tảng ________ để xây dựng các ứng dụng chạy trên máy tính để bàn, máy tính xách tay, máy tính bảng, điện thoại, Xbox và kính thực tế tăng cường HoloLens bằng mã nguồn gần như giống hệt nhau.",
    "image": "extracted_images/fig1_2_logical_units_p1.png",
    "hint": "Xem lại mục 1.3 (Phần cứng), 1.4 (Phân cấp dữ liệu) và 1.5 (Các thế hệ ngôn ngữ lập trình).",
    "answer": "Đáp án chuẩn theo trang 69 giáo trình Deitel:\na) computer programs (chương trình máy tính / phần mềm).\nb) hardware (phần cứng).\nc) data hierarchy (cấu trúc phân cấp dữ liệu).\nd) machine (ngôn ngữ máy - machine language).\ne) assembly languages (hợp ngữ), high-level languages (ngôn ngữ bậc cao).\nf) compilers (các trình biên dịch).\ng) multicore (đa nhân / đa lõi).\nh) Universal Windows Platform - UWP (Nền tảng Windows Phổ quát)."
  },
  {
    "id": "sre-1.2",
    "type": "self-review",
    "category": "1.6 Object Technology & Visual C#",
    "number": "Self-Review 1.2",
    "page": 68,
    "title": "Điền vào chỗ trống: Công nghệ đối tượng & Ngôn ngữ Visual C#",
    "description": "Điền từ hoặc cụm từ thích hợp vào chỗ trống trong các phát biểu sau:\na) Các đối tượng, hay chính xác hơn là các ________ mà từ đó các đối tượng được sinh ra, về bản chất là các thành phần phần mềm có thể tái sử dụng.\nb) Bạn gửi thông điệp tới một đối tượng. Mỗi thông điệp được hiện thực hóa dưới dạng một ________ phương thức để yêu cầu một phương thức của đối tượng thực hiện nhiệm vụ của nó.\nc) Một lớp đối tượng mới có thể được tạo ra một cách nhanh chóng và thuận tiện nhờ cơ chế ________; lớp mới sẽ tiếp thu toàn bộ đặc tính của lớp có sẵn, tùy biến chúng và bổ sung thêm các đặc tính độc đáo của riêng mình.\nd) Để tạo ra các giải pháp tốt nhất, bạn nên tuân thủ quy trình phân tích chi tiết nhằm xác định các ________ của dự án (tức là định nghĩa hệ thống cần phải làm gì) và phát triển một bản thiết kế thỏa mãn chúng (tức là quyết định hệ thống sẽ làm điều đó như thế nào).\ne) Visual C# là ngôn ngữ hướng ________. Bạn sẽ viết các chương trình phản hồi lại các cú nhấp chuột, gõ phím, hết thời gian của bộ đếm thời gian (timer) cũng như các thao tác chạm và vuốt ngón tay.\nf) Mục tiêu then chốt của Java là có thể viết các chương trình chạy được trên nhiều hệ thống máy tính và thiết bị điều khiển khác nhau. Điều này đôi khi được gọi là ________.",
    "image": "extracted_images/fig1_10_painter_app_gui.png",
    "hint": "Xem lại mục 1.6 (Công nghệ đối tượng: Class, Message call, Inheritance, Requirements) và 1.8 (C# hướng sự kiện).",
    "answer": "Đáp án chuẩn theo trang 69 giáo trình Deitel:\na) classes (các lớp).\nb) call (lời gọi phương thức - method call).\nc) inheritance (kế thừa).\nd) requirements (các yêu cầu hệ thống).\ne) event (hướng sự kiện - event-driven).\nf) write once, run anywhere (viết một lần, chạy mọi nơi)."
  },
  {
    "id": "sre-1.3",
    "type": "self-review",
    "category": "1.9 Microsoft .NET & Visual Studio",
    "number": "Self-Review 1.3",
    "page": 68,
    "title": "Điền vào chỗ trống: Nền tảng .NET & Môi trường Visual Studio",
    "description": "Điền từ hoặc cụm từ thích hợp vào chỗ trống trong các phát biểu sau:\na) Thành phần ________ thực thi các chương trình .NET.\nb) Máy ảo CLR cung cấp nhiều dịch vụ khác nhau cho mã ________, chẳng hạn như tích hợp các thành phần phần mềm viết bằng các ngôn ngữ .NET khác nhau, xử lý lỗi giữa các thành phần đó, tăng cường bảo mật và nhiều hơn nữa.\nc) Khả năng một chương trình có thể chạy mà không cần sửa đổi trên nhiều nền tảng phần cứng và hệ điều hành khác nhau được gọi là tính ________ nền tảng.\nd) Visual Studio là một ________ trong đó các chương trình C# được phát triển.\ne) Bạn có thể bán các ứng dụng Windows Phone và Windows của riêng mình trên ________.",
    "image": "extracted_images/fig1_8_painter_solution.png",
    "hint": "Xem lại mục 1.9 (Microsoft .NET, CLR, Managed code, Platform independence) và 1.11 (Visual Studio IDE).",
    "answer": "Đáp án chuẩn theo trang 69 giáo trình Deitel:\na) Common Language Runtime (CLR) của .NET Framework / .NET.\nb) managed (mã được quản lý - managed code).\nc) independence (độc lập nền tảng - platform independence).\nd) IDE (Integrated Development Environment - Môi trường phát triển tích hợp).\ne) Windows Store (Cửa hàng ứng dụng Windows)."
  },
  {
    "id": "sre-1.4",
    "type": "self-review",
    "category": "Tổng hợp Chương 1",
    "number": "Self-Review 1.4",
    "page": 68,
    "title": "Đúng hay Sai: Khảo sát nhận định toàn diện Chương 1",
    "description": "Xác định mỗi phát biểu sau đây là Đúng (True) hay Sai (False). Nếu sai, hãy giải thích rõ lý do:\na) Các đối tượng phần mềm mô hình hóa cả những khái niệm trừu tượng lẫn những sự vật trong thế giới thực.\nb) Mô hình cơ sở dữ liệu phổ biến nhất là cơ sở dữ liệu quan hệ, trong đó dữ liệu được lưu trữ trong các bảng đơn giản. Một bảng bao gồm các bản ghi (records) và các trường (fields).\nc) Cơ sở dữ liệu là một tập hợp dữ liệu được tổ chức để dễ dàng truy cập và thao tác.\nd) Dữ liệu trên bộ nhớ thứ cấp mất nhiều thời gian truy xuất hơn so với dữ liệu trong bộ nhớ chính, nhưng chi phí trên mỗi đơn vị lưu trữ của bộ nhớ thứ cấp cao hơn nhiều so với bộ nhớ chính.\ne) Các ngôn ngữ bậc cao cho phép bạn viết các chỉ thị trông gần giống như tiếng Anh hàng ngày và chứa các biểu thức toán học thông dụng.\nf) Một đối tượng sở hữu các thuộc tính đi liền với nó trong suốt quá trình đối tượng được sử dụng trong chương trình.\ng) Giao thức điều khiển truyền vận (TCP) đảm bảo rằng các thông điệp, bao gồm các phần được đánh số tuần tự gọi là bytes, được định tuyến chính xác từ người gửi tới người nhận, đến nơi nguyên vẹn và được lắp ráp lại theo đúng thứ tự.\nh) Dung lượng truyền tải thông tin của các đường truyền thông trên Internet đã tăng lên khủng khiếp, trong khi chi phí phần cứng cũng tăng theo.\ni) Bạn có thể xây dựng các ứng dụng trên nền web bằng C#.\nj) Ngôn ngữ Objective-C và Java là hai ngôn ngữ lập trình chủ chốt được sử dụng để phát triển các ứng dụng iOS cho iPhone, iPad và iPod Touch.\nk) Công nghệ JavaServer Pages (JSP) cho phép bạn tạo các ứng dụng web với C#.\nl) CLR là máy ảo thực thi các chương trình .NET.",
    "hint": "Chú ý đơn vị của gói tin mạng TCP (packets chứ không phải bytes), chi phí phần cứng (giảm mạnh), ngôn ngữ của Apple (Swift/Objective-C), và công nghệ web của Microsoft (ASP.NET).",
    "answer": "Đáp án chuẩn theo trang 69 giáo trình Deitel:\na) Đúng (True).\nb) Đúng (True).\nc) Đúng (True).\nd) Sai (False). Chi phí trên mỗi đơn vị dung lượng của bộ nhớ thứ cấp THẤP HƠN NHIỀU so với bộ nhớ chính RAM.\ne) Đúng (True).\nf) Đúng (True).\ng) Sai (False). Các mảnh dữ liệu được đánh số tuần tự trong TCP được gọi là các GÓI TIN (PACKETS), không phải bytes.\nh) Sai (False). Chi phí phần cứng đã GIẢM MẠNH (decreased) theo thời gian nhờ định luật Moore.\ni) Đúng (True) - thông qua công nghệ ASP.NET / ASP.NET Core.\nj) Sai (False). Ngôn ngữ lập trình chính cho iOS của Apple là Swift và Objective-C, không phải Java.\nk) Sai (False). Công nghệ web của C# là ASP.NET, còn JSP (JavaServer Pages) là công nghệ của nền tảng Java.\nl) Đúng (True)."
  },
  {
    "id": "sre-1.5",
    "type": "self-review",
    "category": "1.4 Data Hierarchy & Measurements",
    "number": "Self-Review 1.5",
    "page": 69,
    "title": "Sắp xếp các đơn vị đo lường dung lượng byte theo thứ tự tăng dần",
    "description": "Hãy sắp xếp các đơn vị đo lường sau theo thứ tự dung lượng tăng dần: gigabyte, megabyte, petabyte, kilobyte, terabyte.",
    "image": "extracted_images/fig1_4_byte_measurements.png",
    "hint": "Xem Bảng 1.4: KB (nghìn), MB (triệu), GB (tỷ), TB (nghìn tỷ), PB (triệu tỷ).",
    "answer": "Thứ tự tăng dần chuẩn xác theo trang 69 giáo trình:\nkilobyte (KB) < megabyte (MB) < gigabyte (GB) < terabyte (TB) < petabyte (PB)."
  },
  {
    "id": "sre-1.6",
    "type": "self-review",
    "category": "1.9 .NET Execution Pipeline",
    "number": "Self-Review 1.6",
    "page": 69,
    "title": "Mô tả chu trình biên dịch và thực thi hai giai đoạn của chương trình C#",
    "description": "Giải thích ngắn gọn cách một chương trình C# được biên dịch và thực thi trên máy tính thông qua MSIL và CLR.",
    "hint": "Mã nguồn .cs -> Trình biên dịch C# -> MSIL (.dll/.exe) -> Trình biên dịch JIT trong CLR -> Mã máy CPU.",
    "answer": "Giải thích chuẩn theo trang 69 giáo trình:\nMã nguồn C# trước tiên được biên dịch bởi trình biên dịch C# thành Ngôn ngữ Trung gian Microsoft (MSIL) và đặt trong một tệp thực thi (.exe hoặc .dll assembly). Khi ứng dụng bắt đầu thực thi, một trình biên dịch khác gọi là trình biên dịch tức thời JIT (Just-In-Time) nằm bên trong máy ảo CLR sẽ dịch mã MSIL trong tệp thực thi đó thành mã máy nhị phân bản địa (cho nền tảng phần cứng và hệ điều hành cụ thể) để CPU xử lý."
  },
  {
    "id": "ex-1.7",
    "type": "exercises",
    "category": "1.3 & 1.6 Fundamentals",
    "number": "Exercise 1.7",
    "page": 69,
    "title": "Điền vào chỗ trống: Kiến trúc máy tính & Tư duy lập trình đối tượng",
    "description": "Điền từ hoặc cụm từ thích hợp vào chỗ trống trong các phát biểu sau:\na) Bất kể sự khác biệt về hình thức bên ngoài, các máy tính đều có thể được hình dung như được chia thành nhiều ________ khác nhau.\nb) Các hệ thống như điện thoại thông minh, thiết bị gia dụng, tay cầm chơi game, đầu thu truyền hình cáp và ô tô có chứa máy tính nhỏ bên trong được gọi là ________.\nc) Giống như các ký tự được cấu thành từ các bits, các ________ được cấu thành từ các ký tự hoặc bytes.\nd) Thông tin trên các thiết bị lưu trữ thứ cấp là ________; nó được bảo toàn ngay cả khi nguồn điện máy tính bị tắt.\ne) ________ cung cấp các dịch vụ cho phép mỗi ứng dụng thực thi một cách an toàn, hiệu quả và đồng thời cùng với các ứng dụng khác.\nf) Trong các ngôn ngữ lập trình hướng đối tượng, chúng ta tạo ra một đơn vị chương trình gọi là ________ để chứa tập hợp các phương thức thực hiện các nhiệm vụ của nó.\ng) Hãy sử dụng cách tiếp cận khối ghép (building-block) để xây dựng chương trình của bạn. Tránh 'phát minh lại bánh xe'—hãy tận dụng các thành phần có sẵn bất cứ khi nào có thể. Việc ________ phần mềm như vậy là một lợi ích then chốt của lập trình hướng đối tượng.",
    "image": "extracted_images/fig1_3_data_hierarchy.png",
    "hint": "Xem các khái niệm: Logical units, Embedded systems, Fields, Persistent, Operating systems, Class, Reuse.",
    "answer": "Đáp án giải thích chi tiết:\na) logical units (các khối chức năng logic).\nb) embedded systems (các hệ thống nhúng).\nc) fields (các trường dữ liệu).\nd) persistent / non-volatile (bền vững / bất biến / lưu trữ lâu dài).\ne) Operating Systems - OS (Các hệ điều hành).\nf) class (lớp đối tượng).\ng) reuse (tái sử dụng - software reuse)."
  },
  {
    "id": "ex-1.8",
    "type": "exercises",
    "category": "1.6, 1.7 & 1.9 Advanced Concepts",
    "number": "Exercise 1.8",
    "page": 69,
    "title": "Điền vào chỗ trống: UML, Web, CLR & Điện toán đám mây",
    "description": "Điền từ hoặc cụm từ thích hợp vào chỗ trống trong các phát biểu sau:\na) Mặc dù có nhiều quy trình phân tích và thiết kế hướng đối tượng (OOAD) khác nhau tồn tại, một ngôn ngữ đồ họa duy nhất dùng để biểu đạt kết quả của bất kỳ quy trình OOAD nào đã được sử dụng rộng rãi. Ngôn ngữ này được gọi là ________, hiện là lược đồ đồ họa phổ biến nhất để mô hình hóa các hệ thống hướng đối tượng.\nb) Tim Berners-Lee đã phát triển ________ để chia sẻ thông tin thông qua các tài liệu văn bản 'siêu liên kết' (hyperlinked) trên nền web.\nc) Máy ảo CLR là một cỗ máy ________. Nó là phần mềm quản lý việc thực thi các chương trình và ẩn đi hệ điều hành cũng như phần cứng bên dưới khỏi tầm nhìn của ứng dụng.\nd) Việc chuyển đổi một chương trình để chạy trên một nền tảng khác với nền tảng ban đầu dự định được gọi là ________ mã nguồn.\ne) Nền tảng Microsoft ________ là một nền tảng điện toán đám mây cho phép bạn phát triển, quản lý và phân phối các ứng dụng của mình trên đám mây.\nf) Bằng cách sử dụng các điều khiển (controls) có sẵn—vốn là các đối tượng—bạn có thể tạo ra các ứng dụng mạnh mẽ nhanh hơn nhiều so với việc phải tự viết tất cả mã từ đầu. Đây là lợi ích then chốt của việc ________ phần mềm.",
    "image": "extracted_images/fig1_13_drawing_complete.png",
    "hint": "UML, World Wide Web / HTTP, Virtual machine, Porting, Azure, Reuse.",
    "answer": "Đáp án giải thích chi tiết:\na) UML (Unified Modeling Language - Ngôn ngữ Mô hình hóa Hợp nhất).\nb) World Wide Web (WWW) / HTML & HTTP.\nc) virtual (máy ảo - virtual machine).\nd) porting (chuyển đổi nền tảng / chuyển mã).\ne) Azure (Microsoft Azure / Windows Azure).\nf) reuse (tái sử dụng phần mềm - software reuse)."
  },
  {
    "id": "ex-1.9",
    "type": "exercises",
    "category": "Khảo sát Lý thuyết & Đánh giá Phán đoán",
    "number": "Exercise 1.9",
    "page": 70,
    "title": "Đúng hay Sai: Kiểm tra kiến thức mở rộng Chương 1",
    "description": "Xác định mỗi phát biểu sau là Đúng hay Sai. Nếu sai, hãy giải thích rõ tại sao:\na) Phần tử dữ liệu nhỏ nhất trong máy tính có thể nhận giá trị 1 hoặc giá trị 2. Phần tử dữ liệu như vậy được gọi là bit.\nb) Bộ ký tự Unicode là một tập con phổ biến của ASCII, biểu diễn các chữ cái viết hoa và viết thường, chữ số và một số ký tự đặc biệt thông dụng.\nc) Bộ vi xử lý trung tâm (CPU) đóng vai trò như một bộ phận 'hành chính' điều phối và giám sát hoạt động của các bộ phận khác như khối nhập, khối xuất, ALU, v.v.\nd) Tái sử dụng (Reuse) giúp bạn xây dựng các hệ thống đáng tin cậy và hiệu quả hơn, bởi vì các lớp và thành phần có sẵn thường đã trải qua quá trình kiểm thử, gỡ lỗi và tinh chỉnh hiệu năng sâu rộng.\ne) Một trong những mục tiêu chính của tổ chức W3C là làm cho nền tảng web có thể tiếp cận được với mọi người trên toàn cầu, bất kể khuyết tật, ngôn ngữ hay văn hóa.\nf) C# chỉ có thể sử dụng được trên hệ điều hành Microsoft Windows.\ng) Các ứng dụng C# chỉ có thể được phát triển cho các môi trường máy tính để bàn (desktop).\nh) Các chương trình .NET có thể chạy trên bất kỳ nền tảng nào có cài đặt môi trường thực thi .NET tương thích.\ni) Nền tảng Universal Windows Platform (UWP) được thiết kế để cung cấp một nền tảng chung và trải nghiệm người dùng nhất quán trên tất cả các thiết bị bao gồm PC, smartphone, máy tính bảng và máy chơi game Xbox.",
    "hint": "Chú ý giá trị của Bit (0 hoặc 1), Unicode là SIÊU TẬP (superset) chứa ASCII, tính đa nền tảng hiện đại của C# (.NET Core/.NET 8+ chạy trên Linux, macOS).",
    "answer": "Đáp án giải thích chi tiết:\na) Sai (False). Bit chỉ có thể nhận giá trị 0 hoặc 1, không thể nhận giá trị 2.\nb) Sai (False). ASCII mới là tập con (subset) của Unicode; Unicode là bảng mã siêu tập (superset) khổng lồ hỗ trợ hầu hết mọi ngôn ngữ trên thế giới.\nc) Đúng (True). CPU điều phối nhịp nhàng toàn bộ hệ thống.\nd) Đúng (True). Lợi ích cốt lõi của Software Reuse.\ne) Đúng (True). Sứ mệnh toàn cầu hóa và khả năng tiếp cận (Accessibility) của W3C.\nf) Sai (False). C# hiện đại (.NET Core / .NET 8 / Mono) là mã nguồn mở và chạy đa nền tảng trên Windows, macOS, Linux, Android, iOS.\ng) Sai (False). C# phát triển đa dạng: Web (ASP.NET), Mobile (MAUI/Xamarin), Cloud, IoT và Game 3D (Unity).\nh) Đúng (True). Nhờ máy ảo CLR và chuẩn mã trung gian MSIL.\ni) Đúng (True)."
  },
  {
    "id": "ex-1.10",
    "type": "exercises",
    "category": "1.5 Compilers & Interpreters",
    "number": "Exercise 1.10",
    "page": 70,
    "title": "Ưu điểm và nhược điểm then chốt của Trình thông dịch so với Trình biên dịch",
    "description": "Ưu điểm then chốt của trình thông dịch (interpreter) so với trình biên dịch (compiler) là gì? Nhược điểm then chốt của nó là gì?",
    "hint": "So sánh về tính linh hoạt khi gỡ lỗi / sửa code nhanh so với tốc độ thực thi của mã máy biên dịch sẵn.",
    "answer": "- Ưu điểm then chốt của Interpreter: Tính linh hoạt cao, lập trình viên có thể chạy thử và kiểm tra mã lệnh ngay lập tức mà không cần mất thời gian chờ đợi biên dịch toàn bộ dự án; dễ dàng gỡ lỗi và chỉnh sửa tương tác.\n- Nhược điểm then chốt của Interpreter: Tốc độ thực thi chậm hơn đáng kể so với chương trình đã biên dịch sẵn, vì mọi dòng lệnh đều phải trải qua quá trình thông dịch sang mã máy mỗi khi chạy."
  },
  {
    "id": "ex-1.11",
    "type": "exercises",
    "category": "1.8 C# Features",
    "number": "Exercise 1.11",
    "page": 70,
    "title": "Ưu thế của tính năng 'async' trong C# so với mô hình đa luồng kiểu cũ",
    "description": "Ưu điểm then chốt của việc sử dụng tính năng 'async/await' hiện đại trong C# so với việc sử dụng kỹ thuật đa luồng (multithreading) kiểu cũ là gì?",
    "hint": "Độ phức tạp khi viết code, khả năng quản lý tài nguyên luồng và tránh tình trạng khóa chết (deadlock).",
    "answer": "Ưu điểm then chốt của async/await:\n1. Đơn giản hóa mã nguồn: Cho phép viết mã bất đồng bộ có cấu trúc tuần tự và trực quan giống hệt mã đồng bộ thông thường, dễ đọc và dễ bảo trì hơn nhiều so với việc tự quản lý Thread, Callback hay Lock thủ công.\n2. Hiệu quả sử dụng tài nguyên: Mô hình async dựa trên luồng tác vụ (Task-based asynchronous pattern) sử dụng ThreadPool tối ưu, không lãng phí tài nguyên hệ thống để giữ một luồng bị khóa đứng chờ (blocking) tác vụ I/O, giảm thiểu nguy cơ lỗi cạnh tranh (race condition) và khóa chết (deadlock)."
  },
  {
    "id": "ex-1.12",
    "type": "exercises",
    "category": "1.3 Hardware & Moore's Law",
    "number": "Exercise 1.12",
    "page": 70,
    "title": "Định luật Moore đã nâng cao năng lực của máy tính như thế nào?",
    "description": "Định luật Moore đã làm cho máy tính ngày càng có nhiều năng lực mạnh mẽ hơn theo cơ chế như thế nào?",
    "hint": "Số lượng transistor tăng gấp đôi sau mỗi 18-24 tháng -> diện tích chip thu nhỏ, tốc độ tăng, giá giảm.",
    "answer": "Bằng cách tăng gấp đôi số lượng bóng bán dẫn trên các vi mạch tích hợp sau mỗi 18-24 tháng trong khi chi phí sản xuất giữ nguyên:\n- Phần cứng máy tính trở nên nhỏ gọn hơn, tiết kiệm điện năng hơn và giá thành ngày càng rẻ.\n- Năng lực tính toán, dung lượng bộ nhớ và khả năng xử lý đồ họa tăng theo hàm mũ, cho phép máy tính cá nhân và thiết bị di động ngày nay có thể xử lý các tác vụ xử lý video 4K, huấn luyện trí tuệ nhân tạo (AI/Machine Learning) và thực thi các mô phỏng khoa học phức tạp mà trước đây chỉ có các siêu máy tính đắt tiền mới làm được."
  },
  {
    "id": "ex-1.13",
    "type": "exercises",
    "category": "1.7 Cloud Computing",
    "number": "Exercise 1.13",
    "page": 70,
    "title": "Tại sao việc thuê tài nguyên Cloud đôi khi tốt hơn mua phần cứng vật lý?",
    "description": "Tại sao việc sử dụng các tài nguyên điện toán đám mây (Cloud Computing) đôi khi lại được ưa chuộng hơn là mua sắm toàn bộ phần cứng mà bạn cần cho máy tính của mình?",
    "hint": "Chi phí đầu tư ban đầu (CapEx vs OpEx), khả năng co giãn đàn hồi (elastic scalability) và chi phí bảo trì.",
    "answer": "Điện toán đám mây (như Microsoft Azure, AWS) được ưa chuộng vì:\n1. Tiết kiệm chi phí đầu tư ban đầu: Doanh nghiệp không phải bỏ ra số tiền lớn để mua sắm máy chủ đắt đỏ và xây dựng phòng máy lạnh bảo quản (chuyển từ CapEx sang OpEx theo mô hình dùng bao nhiêu trả bấy nhiêu - Pay-as-you-go).\n2. Khả năng co giãn linh hoạt (Scalability): Dễ dàng nâng cấp hoặc giảm bớt tài nguyên CPU, RAM, ổ lưu trữ chỉ trong vài giây khi lưu lượng truy cập biến động.\n3. Giảm gánh nặng bảo trì: Nhà cung cấp dịch vụ đám mây tự động sao lưu dữ liệu, bảo mật, cập nhật bản vá và bảo trì hạ tầng 24/7."
  },
  {
    "id": "ex-1.14",
    "type": "exercises",
    "category": "1.3 Hardware vs Software",
    "number": "Exercise 1.14",
    "page": 70,
    "title": "Phân loại thành phần: Phần cứng, Phần mềm hay Kết hợp cả hai",
    "description": "Mỗi mục sau đây thuộc về lớp phần cứng (hardware), phần mềm (software) hay sự kết hợp của cả hai?\na) Memory Unit (Bộ nhớ chính RAM)\nb) World Wide Web (Mạng lưới toàn cầu)\nc) .NET Framework Class Library (Thư viện lớp .NET)\nd) ALU (Đơn vị số học và logic)\ne) OS (Hệ điều hành)",
    "hint": "Thực thể vật lý = Hardware; Chỉ thị/chương trình = Software; Hệ thống mạng toàn cầu = Kết hợp cả hai.",
    "answer": "Phân loại chuẩn xác:\na) Memory Unit: Phần cứng (Hardware) - gồm các chip bán dẫn lưu trữ điện tích.\nb) World Wide Web: Kết hợp cả hai (Combination of both) - hạ tầng cáp quang, máy chủ vật lý, bộ định tuyến (phần cứng) kết hợp các giao thức HTTP, trình duyệt web, máy chủ web (phần mềm).\nc) .NET Framework Class Library: Phần mềm (Software) - tập hợp các lớp mã nguồn được biên dịch sẵn.\nd) ALU: Phần cứng (Hardware) - mạch logic số trên đế chip vi xử lý.\ne) OS (Operating System): Phần mềm (Software) - tập hợp các chương trình quản trị tài nguyên hệ thống."
  },
  {
    "id": "ex-1.15",
    "type": "exercises",
    "category": "1.9 .NET Framework Class Library",
    "number": "Exercise 1.15",
    "page": 70,
    "title": "Đúng hay Sai về ứng dụng .NET và Thư viện lớp FCL",
    "description": "Các ứng dụng .NET có thể được tạo ra bằng bất kỳ ngôn ngữ tương thích .NET nào như C#, Visual Basic, Visual C++, v.v. Hãy xác định mỗi phát biểu sau là Đúng (True) hay Sai (False) trong ngữ cảnh này:\na) Thư viện Lớp .NET Framework (FCL) có nhiều năng lực giúp xây dựng nhiều ứng dụng C# một cách nhanh chóng và dễ dàng.\nb) Thư viện lớp FCL chứa rất ít các lớp dựng sẵn có giá trị đã được kiểm thử và tinh chỉnh tối đa hiệu năng.\nc) .NET có Trình biên dịch JIT thực thi các chương trình .NET và cung cấp chức năng giúp việc phát triển và gỡ lỗi chúng trở nên dễ dàng hơn.\nd) Các lớp của .NET Framework được tái sử dụng để tăng tốc quy trình phát triển phần mềm.",
    "hint": "FCL chứa hàng chục nghìn lớp phong phú; JIT biên dịch sang native code; FCL tối ưu hóa thời gian lập trình.",
    "answer": "Đáp án giải thích chi tiết:\na) Đúng (True). FCL cung cấp giải pháp dựng sẵn phong phú cho giao diện, mạng, tệp tin, CSDL.\nb) Sai (False). FCL chứa HÀNG CHỤC NGHÌN lớp được thiết kế công phu, kiểm thử nghiêm ngặt để tối ưu hóa hiệu năng.\nc) Đúng (True). JIT Compiler dịch MSIL sang mã máy và tích hợp chặt chẽ với cơ chế debug của CLR.\nd) Đúng (True). Tái sử dụng lớp FCL là nguyên lý cốt lõi để nâng cao năng suất."
  },
  {
    "id": "ex-1.16",
    "type": "exercises",
    "category": "Thuật ngữ & Viết tắt Chuyên ngành",
    "number": "Exercise 1.16",
    "page": 70,
    "title": "Viết dạng đầy đủ của các từ viết tắt chuyên ngành CNTT",
    "description": "Hãy viết dạng đầy đủ (tiếng Anh) và giải nghĩa tiếng Việt ngắn gọn cho các từ viết tắt sau:\na) ASCII\nb) JITC\nc) TCP/IP\nd) OOAD\ne) UWP\nf) GPS",
    "hint": "Bảng mã ký tự, Trình biên dịch tức thời, Giao thức Internet, Phân tích hướng đối tượng, Nền tảng Windows, Định vị vệ tinh.",
    "answer": "Dạng đầy đủ của các từ viết tắt:\na) ASCII: American Standard Code for Information Interchange (Mã chuẩn của Mỹ dùng cho trao đổi thông tin).\nb) JITC: Just-In-Time Compiler (Trình biên dịch tức thời / đúng lúc).\nc) TCP/IP: Transmission Control Protocol / Internet Protocol (Giao thức điều khiển truyền vận / Giao thức mạng Internet).\nd) OOAD: Object-Oriented Analysis and Design (Phân tích và Thiết kế Hướng đối tượng).\ne) UWP: Universal Windows Platform (Nền tảng Windows Phổ quát).\nf) GPS: Global Positioning System (Hệ thống Định vị Toàn cầu)."
  },
  {
    "id": "ex-1.17",
    "type": "exercises",
    "category": "1.9 .NET Framework & CLR",
    "number": "Exercise 1.17",
    "page": 70,
    "title": "Lợi ích then chốt và hạn chế của .NET Framework và CLR",
    "description": "Lợi ích then chốt của .NET Framework và máy ảo CLR là gì? Hạn chế hoặc điểm đánh đổi của chúng là gì?",
    "hint": "Lợi ích: Độc lập nền tảng, thu gom rác an toàn, tương tác đa ngôn ngữ. Hạn chế: Overhead bộ nhớ và thời gian biên dịch JIT ban đầu.",
    "answer": "- Lợi ích then chốt:\n  + Độc lập nền tảng thông qua mã trung gian MSIL.\n  + Quản lý bộ nhớ tự động với Garbage Collection, loại bỏ rò rỉ bộ nhớ.\n  + Tương tác đa ngôn ngữ liền mạch (C#, VB.NET, F#).\n  + Kho thư viện lớp đồ sộ (FCL) giúp tăng tốc độ phát triển phần mềm.\n- Hạn chế / Điểm đánh đổi:\n  + Khởi động ứng dụng có thể tốn một khoảng thời gian nhỏ ban đầu do JIT Compiler cần dịch mã MSIL sang mã máy.\n  + Tốn thêm dung lượng bộ nhớ RAM để duy trì môi trường máy ảo CLR so với các ứng dụng viết bằng C/C++ thuần túy."
  },
  {
    "id": "ex-1.18",
    "type": "exercises",
    "category": "1.6 Object Technology & OOAD",
    "number": "Exercise 1.18",
    "page": 71,
    "title": "Quy trình OOAD giúp thiết kế hệ thống phần mềm lớn và phức tạp như thế nào?",
    "description": "Quy trình Phân tích và Thiết kế Hướng đối tượng (OOAD) giúp ích như thế nào trong việc xây dựng các hệ thống phần mềm quy mô lớn và phức tạp?",
    "hint": "Phân chia module, trừu tượng hóa thế giới thực thành các lớp, giảm phụ thuộc (loose coupling).",
    "answer": "OOAD giúp ích bằng cách:\n1. Phân rã độ phức tạp: Chia nhỏ hệ thống phần mềm khổng lồ thành các lớp đối tượng độc lập, dễ quản lý, tương ứng tự nhiên với các thực thể trong thế giới thực.\n2. Chuẩn hóa giao tiếp: Sử dụng ngôn ngữ mô hình hóa UML để các kỹ sư, nhà phân tích và khách hàng có chung một tiếng nói thiết kế rõ ràng trước khi viết code.\n3. Giảm thiểu rủi ro: Xác định chính xác các yêu cầu (requirements) và thiết kế kiến trúc chuẩn mực giúp tránh việc sửa đổi cấu trúc tốn kém ở giai đoạn sau của dự án."
  },
  {
    "id": "ex-1.19",
    "type": "exercises",
    "category": "1.6 Car Analogy in OOP",
    "number": "Exercise 1.19",
    "page": 71,
    "title": "Ẩn dụ chiếc xe ô tô trong lập trình hướng đối tượng (OOP Analogy)",
    "description": "Khi quan sát một chiếc xe ô tô ngoài đời thực, bạn quyết định liên hệ nó với các khái niệm của mô hình lập trình hướng đối tượng. Hãy thảo luận về khái niệm xe ô tô bằng phép ẩn dụ này: Lớp (class) mà nó thuộc về, các đối tượng (objects) cùng loại, các thuộc tính (attributes) và hành vi (behaviors) gắn liền với đối tượng.",
    "image": "extracted_images/fig1_2_logical_units_p2.png",
    "hint": "Class = Bản vẽ thiết kế kỹ thuật ô tô; Object = Chiếc xe cụ thể lăn bánh; Attributes = Màu sơn, số chỗ ngồi, lượng xăng; Behaviors = Tăng tốc, phanh, bật đèn.",
    "answer": "Thảo luận chi tiết ẩn dụ xe ô tô trong OOP:\n- Lớp (Class): Là bản vẽ thiết kế kỹ thuật của mẫu xe ô tô trên giấy (ví dụ: lớp `Automobile`). Bản vẽ quy định xe phải có động cơ, 4 bánh, vô lăng, chân ga và phanh.\n- Đối tượng (Objects): Là những chiếc xe ô tô cụ thể được sản xuất xuất xưởng từ bản vẽ đó và đang lăn bánh trên đường (ví dụ: chiếc xe VinFast VF8 màu đỏ biển số 43A-12345, chiếc xe Toyota Camry màu bạc biển số 29A-67890).\n- Thuộc tính (Attributes / Properties): Các đặc điểm mô tả trạng thái của chiếc xe như: màu sơn (`Color`), số chỗ ngồi (`Capacity`), lượng xăng hoặc dung lượng pin còn lại (`FuelLevel`), tốc độ hiện tại (`Speed`).\n- Hành vi (Behaviors / Methods): Các hành động mà xe có thể thực hiện được như: nổ máy (`Start()`), tăng tốc (`Accelerate()`), đạp phanh (`Brake()`), rẽ hướng (`Turn()`)."
  },
  {
    "id": "ex-1.20",
    "type": "exercises",
    "category": "1.6 UML Accomplishment",
    "number": "Exercise 1.20",
    "page": 71,
    "title": "Thành tựu then chốt của Ngôn ngữ Mô hình hóa Hợp nhất (UML)",
    "description": "Thành tựu then chốt mang tính lịch sử của ngôn ngữ UML (Unified Modeling Language) đối với ngành công nghiệp phần mềm là gì?",
    "hint": "Thống nhất các phương pháp luận đồ họa thành một chuẩn duy nhất toàn cầu.",
    "answer": "Thành tựu then chốt của UML:\nUML đã hợp nhất nhiều phương pháp luận mô hình hóa đồ họa rời rạc trước đó thành một ngôn ngữ chuẩn đồ họa duy nhất, được chấp nhận trên toàn thế giới. Nhờ UML, các kỹ sư phần mềm trên khắp hành tinh có thể truyền đạt, mô hình hóa và ghi lại các thiết kế kiến trúc hệ thống hướng đối tượng một cách nhất quán và chuẩn xác."
  },
  {
    "id": "ex-1.21",
    "type": "exercises",
    "category": "1.7 Internet History",
    "number": "Exercise 1.21",
    "page": 71,
    "title": "Lợi ích hàng đầu của mạng Internet trong giai đoạn sơ khai",
    "description": "Lợi ích hàng đầu và chứng minh được giá trị to lớn nhất của mạng Internet trong những ngày đầu ra đời là gì?",
    "hint": "Khả năng liên lạc quân sự và học thuật bền vững khi một phần mạng bị phá hủy (chuyển mạch gói).",
    "answer": "Lợi ích hàng đầu của mạng Internet thời kỳ đầu (ARPANET):\nKhả năng duy trì liên lạc truyền thông linh hoạt, bền bỉ ngay cả khi một phần của mạng lưới bị phá hủy hoặc gián đoạn (nhờ kỹ thuật chuyển mạch gói packet-switching và định tuyến phi tập trung), cho phép các nhà khoa học và viện nghiên cứu chia sẻ dữ liệu và tài nguyên tính toán từ xa."
  },
  {
    "id": "ex-1.22",
    "type": "exercises",
    "category": "1.7 Web Capability",
    "number": "Exercise 1.22",
    "page": 71,
    "title": "Năng lực then chốt của World Wide Web",
    "description": "Năng lực then chốt nào đã biến World Wide Web trở thành phương tiện chia sẻ thông tin bùng nổ nhất nhân loại?",
    "hint": "Siêu văn bản (Hyperlinks), ngôn ngữ HTML và giao thức HTTP.",
    "answer": "Năng lực then chốt của Web:\nKhả năng liên kết và chia sẻ thông tin đa phương tiện không giới hạn thông qua 'siêu văn bản' (hypertext) và các 'siêu liên kết' (hyperlinks), cho phép người dùng nhấp chuột chuyển đổi tức thì giữa các tài liệu nằm trên các máy chủ phân tán khắp toàn cầu qua giao thức HTTP."
  },
  {
    "id": "ex-1.23",
    "type": "exercises",
    "category": "1.9 Microsoft .NET Vision",
    "number": "Exercise 1.23",
    "page": 71,
    "title": "Tầm nhìn kiến trúc cốt lõi của sáng kiến Microsoft .NET",
    "description": "Tầm nhìn cốt lõi của sáng kiến Microsoft .NET khi được công bố là gì?",
    "hint": "Kết nối thông tin, con người, hệ thống và thiết bị qua phần mềm và Internet.",
    "answer": "Tầm nhìn cốt lõi của Microsoft .NET:\nXây dựng một nền tảng toàn diện và thống nhất kết nối thông tin, con người, hệ thống và các thiết bị thông qua các dịch vụ web và phần mềm chạy trên mạng Internet; mang lại sự tự do lựa chọn ngôn ngữ lập trình cho nhà phát triển mà vẫn đảm bảo tính tương tác cao và an toàn tuyệt đối."
  },
  {
    "id": "ex-1.24",
    "type": "exercises",
    "category": "1.9 .NET FCL",
    "number": "Exercise 1.24",
    "page": 71,
    "title": "Thư viện lớp FCL tạo thuận lợi cho việc phát triển ứng dụng .NET ra sao?",
    "description": "Thư viện Lớp .NET Framework (FCL) tạo điều kiện thuận lợi và thúc đẩy tốc độ phát triển các ứng dụng .NET như thế nào?",
    "hint": "Cung cấp sẵn hàng nghìn thành phần chuẩn cho GUI, File, Network, Database, Security.",
    "answer": "FCL tạo thuận lợi bằng cách:\nCung cấp sẵn hàng chục nghìn lớp đối tượng chuẩn mực đã được tối ưu hiệu năng cao cho hầu hết mọi nhu cầu lập trình: từ nhập xuất tệp tin, giao diện đồ họa (Windows Forms, WPF), kết nối cơ sở dữ liệu (ADO.NET), lập trình mạng đến mã hóa bảo mật. Lập trình viên chỉ cần kế thừa và gọi sử dụng thay vì phải tự viết lại các thuật toán cơ bản từ đầu."
  },
  {
    "id": "ex-1.25",
    "type": "exercises",
    "category": "1.6 Benefits of OOP",
    "number": "Exercise 1.25",
    "page": 71,
    "title": "Lợi ích lớn khác của OOP bên cạnh việc tái sử dụng phần mềm",
    "description": "Bên cạnh lợi ích rõ ràng về khả năng tái sử dụng (reuse) do OOP mang lại, nhiều tổ chức và doanh nghiệp công nghệ báo cáo một lợi ích then chốt khác của OOP là gì?",
    "hint": "Tính dễ bảo trì (maintainability), khả năng mở rộng (extensibility) và quản lý dự án nhóm hiệu quả.",
    "answer": "Lợi ích then chốt khác của OOP:\nKhả năng bảo trì phần mềm (Maintainability) và dễ dàng nâng cấp, mở rộng hệ thống (Extensibility). Do mã nguồn được tổ chức thành các lớp độc lập, đóng gói chặt chẽ, việc sửa đổi hoặc nâng cấp bên trong một lớp sẽ không gây hiệu ứng dây chuyền làm hỏng các phần khác của chương trình, giúp giảm thiểu đáng kể chi phí bảo trì dài hạn."
  },
  {
    "id": "mad-1.26",
    "type": "making-a-difference",
    "category": "Making a Difference / Green Computing",
    "number": "Exercise 1.26",
    "page": 71,
    "title": "Dự án Chạy thử: Máy tính Dấu chân Carbon (Carbon Footprint Calculator)",
    "description": "Biến đổi khí hậu toàn cầu đang là thách thức lớn nhất của nhân loại. Dấu chân carbon (carbon footprint) đo lường lượng khí thải nhà kính (chủ yếu là CO₂) do hoạt động của một cá nhân hoặc tổ chức tạo ra.\nHãy truy cập các trang web tính toán dấu chân carbon trực tuyến (như Carbon Footprint Calculator) và thực hiện các yêu cầu sau:\n1. Chạy thử máy tính để ước tính lượng phát thải carbon hàng năm của bạn (dựa trên việc sử dụng điện, nhiên liệu xe máy/ô tô, ăn uống, đi lại).\n2. Nghiên cứu các công thức toán học cơ bản được dùng để tính toán dấu chân carbon nhằm chuẩn bị cho bài tập lập trình xây dựng ứng dụng tính dấu chân carbon bằng C# trong các chương sau.",
    "hint": "Khám phá các trang như carbonfootprint.com/calculator.aspx hoặc terrapass.com.",
    "answer": "Hướng dẫn thực hiện và Công thức tham khảo:\n- Công thức cơ bản: Tổng lượng CO₂ (kg) = (Số kWh điện tiêu thụ × Hệ số phát thải lưới điện) + (Lượng xăng dầu tiêu thụ × Hệ số phát thải nhiên liệu) + (Số km bay/đi xe × Suất tiêu hao).\n- Ý nghĩa sư phạm: Giúp sinh viên IT26M ý thức được trách nhiệm của kỹ sư công nghệ với phát triển bền vững và chuẩn bị tư duy thuật toán cho bài tập lập trình ở các chương sau."
  },
  {
    "id": "mad-1.27",
    "type": "making-a-difference",
    "category": "Making a Difference / Healthcare",
    "number": "Exercise 1.27",
    "page": 71,
    "title": "Dự án Chạy thử: Máy tính Chỉ số khối cơ thể (BMI Calculator)",
    "description": "Chỉ số khối cơ thể (Body Mass Index - BMI) là chỉ số tiêu chuẩn quốc tế được Tổ chức Y tế Thế giới (WHO) sử dụng để đánh giá tình trạng thể trọng của một người (gầy, bình thường, thừa cân hoặc béo phì).\n1. Tìm hiểu công thức tính BMI theo hệ mét tiêu chuẩn quốc tế.\n2. Tự tính toán chỉ số BMI của chính mình và xác định phân loại thể trọng tương ứng.\n3. Liệt kê các điều kiện rẽ nhánh logic cần thiết để phân loại kết quả (suy dinh dưỡng, bình thường, tiền béo phì, béo phì cấp độ I, II) làm nền tảng cho bài tập lập trình cấu trúc if-else trong Chương 3.",
    "hint": "Công thức hệ mét: BMI = Cân nặng (kg) / (Chiều cao (m))².",
    "answer": "Công thức và logic phân loại BMI:\n1. Công thức chuẩn: BMI = weight_kg / (height_m * height_m)\n2. Bảng phân loại của WHO:\n   - BMI < 18.5: Thiếu cân (Underweight).\n   - 18.5 <= BMI < 25.0: Thể trọng bình thường (Normal).\n   - 25.0 <= BMI < 30.0: Thừa cân (Overweight).\n   - BMI >= 30.0: Béo phì (Obese).\n3. Bài tập này chuẩn bị thuật toán rẽ nhánh điều kiện cho sinh viên thực hành trong Chương 3 của giáo trình."
  },
  {
    "id": "mad-1.28",
    "type": "making-a-difference",
    "category": "Making a Difference / Clean Tech",
    "number": "Exercise 1.28",
    "page": 71,
    "title": "Phân tích Hướng đối tượng: Các thuộc tính của Lớp Xe lai điện (Hybrid Vehicle)",
    "description": "Xe lai xăng-điện (Hybrid Vehicle) ngày càng trở nên phổ biến vì hiệu quả tiết kiệm nhiên liệu và giảm phát thải bảo vệ môi trường. Hãy vận dụng tư duy hướng đối tượng đã học trong chương 1 để thiết kế một Lớp (Class) có tên là `HybridVehicle`:\n1. Nghiên cứu tính năng của 4-5 dòng xe hybrid nổi tiếng hiện nay (Toyota Prius, Honda CR-V Hybrid, Hyundai Ioniq, v.v.).\n2. Liệt kê càng nhiều thuộc tính (attributes) liên quan đến hệ thống hybrid càng tốt (ví dụ: mức tiêu thụ nhiên liệu trong đô thị, mức tiêu thụ đường trường, chế độ sạc tái sinh năng lượng, v.v.).\n3. Liệt kê các thuộc tính chi tiết của khối pin (battery attributes: loại pin lithium-ion hay NiMH, dung lượng kWh, khối lượng pin, điện áp, thời gian bảo hành).",
    "hint": "Tách thuộc tính thành nhóm Động cơ xăng, Động cơ điện và Bộ pin lưu trữ.",
    "answer": "Bản thiết kế thuộc tính Lớp `HybridVehicle`:\n- Thuộc tính động cơ và tiêu thụ nhiên liệu:\n  + `CityMilesPerGallon` / `LitresPer100kmCity`: Mức tiêu thụ nhiên liệu trong đô thị.\n  + `HighwayMilesPerGallon` / `LitresPer100kmHighway`: Mức tiêu thụ đường trường.\n  + `FuelTankCapacity`: Dung tích bình nhiên liệu (lít).\n  + `DriveMode`: Chế độ lái (EV Mode thuần điện, ECO, Sport).\n- Thuộc tính khối pin (Battery Properties):\n  + `BatteryType`: Loại pin (Lithium-ion, Nickel-Metal Hydride).\n  + `BatteryCapacityKWh`: Dung lượng pin tính bằng kWh.\n  + `BatteryWeightKg`: Khối lượng khối pin.\n  + `RegenerativeBrakingEfficiency`: Hiệu suất phanh tái sinh năng lượng.\n  + `BatteryWarrantyYears`: Số năm bảo hành bộ pin."
  },
  {
    "id": "mad-1.29",
    "type": "making-a-difference",
    "category": "Making a Difference / Ethics & NLP",
    "number": "Exercise 1.29",
    "page": 71,
    "title": "Thuật toán Xử lý ngôn ngữ trung tính giới tính (Gender Neutrality Algorithm)",
    "description": "Để thúc đẩy bình đẳng giới trong giao tiếp công vụ và tài liệu chuyên nghiệp, người ta muốn loại bỏ các từ ngữ mang định kiến giới tính bằng các từ ngữ trung tính.\nGiả sử bạn được giao một danh sách các từ chỉ giới tính và từ thay thế trung tính tương ứng (ví dụ: thay 'wife' thành 'spouse', 'man' thành 'person', 'daughter' thành 'child', 'chairman' thành 'chairperson', v.v.).\n1. Hãy trình bày quy trình (thủ tục / thuật toán) mà bạn sẽ sử dụng để đọc qua một đoạn văn bản và thực hiện các phép thay thế này.\n2. Giải thích tại sao một thuật toán thay thế chuỗi con ngây thơ (naive substring replacement) có thể vô tình tạo ra những từ kỳ quặc, chẳng hạn như biến từ 'woman' thành 'woperchild' (được ghi nhận trong Urban Dictionary)?\n3. Bạn sẽ cải tiến thuật toán như thế nào để ngăn chặn lỗi ngữ nghĩa nghiêm trọng này?",
    "hint": "Chú ý việc thay thế chuỗi con nằm bên trong từ khác: 'woman' chứa 'man'; nếu thay 'man' bằng 'person' thì 'woman' -> 'woperson'. Nếu 'person' lại chứa 'son' và thay 'son' bằng 'child' thì 'woperson' biến thành 'woperchild'!",
    "answer": "Phân tích thuật toán và Giải pháp cải tiến:\n1. Thủ tục cơ bản: Đọc từng đoạn văn bản, tách thành các từ riêng biệt (tokenization) dựa trên khoảng trắng và dấu câu, tra cứu từng từ trong từ điển ánh xạ (lookup dictionary), nếu khớp thì thay thế bằng từ trung tính.\n2. Nguồn gốc của lỗi 'woperchild': Do thuật toán thay thế chuỗi con ngây thơ thực hiện nhiều lượt liên tiếp:\n   - Từ gốc: 'woman'\n   - Lượt 1: Thấy chứa 'man', thay 'man' thành 'person' -> tạo ra từ 'woperson'!\n   - Lượt 2: Trong 'woperson' lại chứa từ 'son', thuật toán thay 'son' bằng 'child' -> biến thành 'woperchild' vô nghĩa!\n3. Giải pháp cải tiến kỹ thuật:\n   - Sử dụng ranh giới từ (Word Boundaries - ví dụ biểu thức chính quy Regex `\\bman\\b`) để chỉ thay thế khi nó là một từ độc lập, không thay thế chuỗi con nằm bên trong từ khác.\n   - Thực hiện thay thế đồng thời một lượt (Single-pass replacement) bằng Bảng băm (Hash Map) hoặc cây tiền tố Trie thay vì chạy nhiều vòng lặp thay thế lồng nhau."
  }
];

const EXERCISES_CHAPTER_02 = [
  {
    "id": "sre-2.1",
    "type": "self-review",
    "category": "2.2 Visual Studio IDE & 2.4 Menus",
    "number": "Self-Review 2.1",
    "page": 100,
    "title": "Self-Review 2.1: Điền vào chỗ trống các khái niệm nền tảng",
    "description": "Củng cố các khái niệm cơ bản về môi trường phát triển ứng dụng trực quan Visual C#.\n\nĐiền từ hoặc cụm từ thích hợp vào chỗ trống trong các phát biểu sau:\na) Kỹ thuật _______ cho phép bạn tạo giao diện người dùng (GUI) mà không cần phải viết bất kỳ dòng mã lệnh nào.\nb) Một _______ là nhóm gồm một hoặc nhiều dự án (projects) cùng hợp thành một ứng dụng Visual C# hoàn chỉnh.\nc) Tính năng _______ cho phép tự động ẩn một cửa sổ làm việc trong IDE thành một tab ở mép màn hình.\nd) Một _______ sẽ nổi lên khi con trỏ chuột dừng (hover) trên một biểu tượng nút bấm công cụ.\ne) Cửa sổ _______ cho phép lập trình viên duyệt cây thư mục và quản lý toàn bộ các tệp tin trong giải pháp.\nf) Danh sách các thuộc tính trong Properties window có thể được sắp xếp theo _______ hoặc theo _______.\ng) Thuộc tính _______ của Form quy định dòng chữ hiển thị trên thanh tiêu đề của cửa sổ ứng dụng.\nh) Hộp công cụ _______ chứa sẵn các linh kiện điều khiển đồ họa mà bạn có thể kéo thả vào Form.\ni) Tính năng _______ hiển thị bài viết hướng dẫn phù hợp từ MSDN dựa trên đối tượng đang được chọn khi bấm phím F1.\nj) Thuộc tính _______ quy định cách căn lề chuỗi văn bản (trái, phải, giữa) bên trong ranh giới của điều khiển Label.",
    "hint": "Xem lại Mục 2.2 đến 2.4 trong giáo trình Deitel: các cửa sổ nòng cốt, phím tắt F1, tính năng ghim pin và thuộc tính Form/Label.",
    "image": null,
    "answer": "Đáp án chuẩn mực theo Giáo trình Deitel (trang 100):\n\na) **visual app development** (phát triển ứng dụng trực quan / lập trình kéo thả).\nb) **solution** (giải pháp phần mềm - tệp đuôi .sln).\nc) **auto-hide** (tự động ẩn - biểu tượng đinh ghim xoay ngang).\nd) **tool tip** (chú giải công cụ kèm phím tắt trong ngoặc đơn).\ne) **Solution Explorer** (cửa sổ quản trị cấu trúc dự án - phím tắt Ctrl+Alt+L).\nf) **alphabetically** (theo bảng chữ cái từ A-Z), **categorically** (phân loại theo nhóm chủ đề: Appearance, Behavior, Layout...).\ng) **Text** (thuộc tính quy định chuỗi tiêu đề hiển thị trên thanh tiêu đề Form).\nh) **Toolbox** (hộp công cụ linh kiện đồ họa - phím tắt Ctrl+Alt+X).\ni) **context-sensitive help** (trợ giúp theo ngữ cảnh kích hoạt bằng phím F1).\nj) **TextAlign** (căn lề văn bản trong nhãn, cung cấp lưới 9 ô vuông 3x3 với giá trị tâm MiddleCenter)."
  },
  {
    "id": "sre-2.2",
    "type": "self-review",
    "category": "2.3 Navigating the IDE & Controls",
    "number": "Self-Review 2.2",
    "page": 100,
    "title": "Self-Review 2.2: Nhận định Đúng / Sai và giải thích kỹ thuật",
    "description": "Kiểm tra sự thấu hiểu về hành vi của các thành phần giao diện Visual Studio IDE.\n\nXác định các phát biểu sau là Đúng (True) hay Sai (False). Nếu Sai, hãy giải thích rõ lý do kỹ thuật:\na) Biểu tượng chiếc đinh ghim dùng để bật/tắt chế độ tự động ẩn (auto-hide), còn dấu X dùng để đóng cửa sổ.\nb) Các biểu tượng trên thanh công cụ chuẩn (toolbar) đại diện cho các lệnh thường dùng trên thanh menu bar.\nc) Thanh công cụ toolbar chứa các biểu tượng đại diện cho các điều khiển đồ họa mà bạn có thể kéo thả vào Form.\nd) Cả Form và điều khiển Label đều sở hữu một thanh tiêu đề (title bar) hoàn chỉnh.\ne) Thuộc tính của các điều khiển chỉ có thể được chỉnh sửa bằng cách viết mã lệnh C# trong lúc chạy.\nf) Điều khiển PictureBox là điều khiển chuyên dụng để hiển thị các tệp hình ảnh đồ họa.\ng) Các tệp tin mã nguồn Visual C# sử dụng phần mở rộng là .csharp.\nh) Màu nền của Form được thiết lập thông qua thuộc tính BackColor.",
    "hint": "Phân biệt rạch ròi giữa Toolbar (lệnh IDE) và Toolbox (linh kiện kéo thả); đuôi tệp C# là .cs.",
    "image": null,
    "answer": "Phân tích và lời giải chuẩn mực theo Giáo trình Deitel (trang 100):\n\na) **True (Đúng)**. Biểu tượng đinh ghim (pushpin) bật/tắt chế độ auto-hide, còn nút dấu X màu đỏ/xám dùng để đóng hoàn toàn cửa sổ.\nb) **True (Đúng)**. Toolbar đóng vai trò phím tắt trực quan đại diện cho các lệnh phổ biến nhất trên Menu Bar (Save All, Open, Start...).\nc) **False (Sai)**. Cửa sổ **Toolbox** mới là nơi chứa các biểu tượng điều khiển để kéo thả vào Form; toolbar chỉ chứa các lệnh thao tác IDE.\nd) **False (Sai)**. Chỉ có **Form** mới sở hữu thanh tiêu đề (title bar) có icon, tiêu đề và các nút thu phóng/đóng; Label chỉ là nhãn văn bản phẳng không có title bar.\ne) **False (Sai)**. Thuộc tính điều khiển hoàn toàn có thể được tùy biến trực quan lúc thiết kế (Design-Time) thông qua cửa sổ **Properties Window** mà không cần viết một dòng mã nào.\nf) **True (Đúng)**. PictureBox là điều khiển chuyên dụng để nạp và hiển thị các định dạng ảnh như PNG, JPG, GIF, BMP, ICO.\ng) **False (Sai)**. Tệp mã nguồn Visual C# sử dụng phần mở rộng chuẩn mực là **.cs** (viết tắt của C Sharp), ví dụ: `Form1.cs`, `Program.cs`.\nh) **True (Đúng)**. Thuộc tính `BackColor` (Background Color) quy định màu nền của Form cũng như của các điều khiển đồ họa."
  },
  {
    "id": "ex-2.3",
    "type": "exercises",
    "category": "2.4 Properties Window & Dialogs",
    "number": "Exercise 2.3",
    "page": 100,
    "title": "Exercise 2.3: Điền vào chỗ trống các thao tác nâng cao trong IDE",
    "description": "Các thao tác với hộp thoại Dialog, trợ giúp F1 và menu Window.\n\nĐiền từ thích hợp vào chỗ trống trong các nhận định sau:\na) Khi một nút hình dấu 3 chấm [...] (ellipsis button) được nhấp chọn, một _______ sẽ được hiển thị.\nb) Sử dụng trợ giúp _______ giúp lập trình viên mở ngay lập tức bài viết hướng dẫn tương ứng với ngữ cảnh hiện tại.\nc) Khi bạn chọn một thuộc tính, phần mô tả ngắn gọn về thuộc tính đó sẽ hiển thị ở đáy của cửa sổ _______.\nd) Thuộc tính _______ quy định tệp tin hình ảnh nào sẽ được hiển thị bên trong khung PictureBox.\ne) Menu _______ trên Menu Bar chứa các lệnh quản lý, sắp xếp bố cục và khôi phục các cửa sổ làm việc.",
    "hint": "Mục 2.4 - 2.6 Deitel: Nút dấu 3 chấm [...] luôn mở hộp thoại đồ họa; menu Window quản trị layout.",
    "image": null,
    "answer": "Đáp án chi tiết:\n\na) **dialog / dialog box** (hộp thoại - ví dụ: Font Dialog, Select Resource Dialog, Color Picker).\nb) **context-sensitive** (trợ giúp theo ngữ cảnh kích hoạt qua phím F1).\nc) **Properties** (cụ thể là khung mô tả Description Pane nằm ở chân cửa sổ Properties Window).\nd) **Image** (thuộc tính lưu tham chiếu hình ảnh trong PictureBox).\ne) **Window** (menu chứa lệnh Reset Window Layout, chia tab, quản lý màn hình làm việc)."
  },
  {
    "id": "ex-2.4",
    "type": "exercises",
    "category": "2.5 Visual Programming & Event-Driven",
    "number": "Exercise 2.4",
    "page": 100,
    "title": "Exercise 2.4: Nhận định Đúng / Sai về hành vi thao tác và lập trình",
    "description": "Khảo sát các thao tác thực tế khi thiết kế Form và viết mã phần mềm.\n\nCho biết mỗi phát biểu sau là Đúng hay Sai. Giải thích ngắn gọn:\na) Bạn có thể thêm nhanh một điều khiển vào Form bằng cách nhấp đúp chuột lên biểu tượng của nó trong Toolbox.\nb) Các điều khiển Form, Label và PictureBox sở hữu tập hợp các thuộc tính hoàn toàn giống hệt nhau.\nc) Nếu máy tính có kết nối Internet, lập trình viên có thể duyệt web và đọc tài liệu ngay trong Visual Studio IDE.\nd) Các nhà phát triển ứng dụng Visual C# thường tạo nên các phần mềm phức tạp quy mô lớn mà không cần viết bất kỳ dòng mã nào.\ne) Nhấp vào biểu tượng mũi tên (hoặc dấu cộng/trừ) bên trái của một nút phân cấp (node) sẽ giúp mở rộng hoặc thu gọn nút đó.",
    "hint": "Xem lại tính năng nhấp đúp trong Toolbox; các ứng dụng thương mại luôn cần mã nguồn logic sự kiện.",
    "image": null,
    "answer": "Phân tích và lời giải:\n\na) **True (Đúng)**. Ngoài việc kéo thả, nhấp đúp vào một điều khiển trong Toolbox sẽ tự động thêm ngay một đối tượng điều khiển đó vào góc trên bên trái của Form.\nb) **False (Sai)**. Mặc dù cùng kế thừa từ lớp cha `Control` và có một số thuộc tính chung (như Size, Location, BackColor), mỗi điều khiển có các thuộc tính đặc thù riêng biệt: PictureBox có `Image`, `SizeMode`; Label có `TextAlign`; Form có `StartPosition`, `WindowState`, `FormBorderStyle`.\nc) **True (Đúng)**. Visual Studio tích hợp sẵn trình duyệt web nội bộ (Web Browser pane) và tab Start Page/MSDN cho phép duyệt web trực tiếp.\nd) **False (Sai)**. Lập trình trực quan WYSIWYG chỉ giúp thiết kế nhanh bộ khung giao diện (GUI). Mọi ứng dụng thực tế phức tạp đều bắt buộc phải viết mã C# xử lý logic thuật toán, cơ sở dữ liệu và xử lý ngoại lệ.\ne) **True (Đúng)**. Biểu tượng mũi tên/dấu cộng trong cây thư mục Solution Explorer hoặc danh sách thuộc tính Categorized cho phép mở rộng (expand) hoặc thu gọn (collapse) các nhánh phân cấp."
  },
  {
    "id": "ex-2.5",
    "type": "exercises",
    "category": "2.2 GUI Design Consistency",
    "number": "Exercise 2.5",
    "page": 100,
    "title": "Exercise 2.5: Phân tích tính nhất quán trong trải nghiệm giao diện Visual Studio",
    "description": "Giải thích vai trò của các mẫu thiết kế UI nhất quán: nút ba chấm [...], mũi tên xổ xuống, và tooltips.\n\nMột số thành phần giao diện xuất hiện xuyên suốt trong Visual Studio thực hiện các hành vi tương tự nhau trong các ngữ cảnh khác nhau. Hãy giải thích và nêu ví dụ minh họa về cách hoạt động của:\n1. Nút bấm hình dấu ba chấm [...] (ellipsis buttons).\n2. Nút mũi tên trỏ xuống (down-arrow buttons).\n3. Nhãn chú giải công cụ (tool tips).\nTheo em, tại sao môi trường Visual Studio IDE lại được thiết kế theo phong cách nhất quán như vậy?",
    "hint": "Mục 2.4 giáo trình Deitel: Nguyên lý nhất quán giúp tăng tốc độ phát triển và giảm thiểu sai sót.",
    "image": null,
    "answer": "Phân tích công thái học và nguyên lý thiết kế UI/UX nhất quán trong Visual Studio:\n\n1. **Nút dấu ba chấm [...] (Ellipsis buttons):**\n   - *Cơ chế:* Báo hiệu cho lập trình viên biết rằng khi bấm vào đây, một hộp thoại (Dialog) đầy đủ tính năng sẽ xuất hiện để cung cấp nhiều tùy chọn cấu hình phức tạp mà một ô nhập liệu đơn dòng không thể chứa hết.\n   - *Ví dụ:* Nút `[...]` ở thuộc tính `Font` mở hộp thoại Font Dialog để chọn phông/kích cỡ; nút `[...]` ở thuộc tính `Image` mở hộp thoại Select Resource để duyệt và nạp tệp ảnh; nút `[...]` ở ô Location khi tạo dự án mới mở hộp thoại Browse Folder.\n\n2. **Nút mũi tên xổ xuống (Down-arrow buttons):**\n   - *Cơ chế:* Cung cấp một danh sách hữu hạn các giá trị hoặc tùy chọn cho trước (Dropdown list/Palette picker), ngăn ngừa người dùng gõ sai chính tả và tiết kiệm thời gian.\n   - *Ví dụ:* Mũi tên ở thuộc tính `BackColor` mở bảng màu 3 tab (Custom, Web, System); mũi tên ở thuộc tính `SizeMode` liệt kê 5 giá trị enum (Normal, StretchImage, AutoSize, CenterImage, Zoom); mũi tên ở thuộc tính `TextAlign` hiển thị lưới 9 ô vuông trực quan.\n\n3. **Chú giải công cụ (Tool tips):**\n   - *Cơ chế:* Hỗ trợ người dùng nhận diện nhanh tên gọi và chức năng của một biểu tượng đồ họa trừu tượng kèm phím tắt thao tác nhanh.\n   - *Ví dụ:* Rê chuột qua nút Start hiển thị `Start (F5)`, rê qua đĩa mềm hiển thị `Save All (Ctrl+Shift+S)`.\n\n**Ý nghĩa thiết kế:** Triết lý thiết kế này tuân thủ nguyên lý **Tính nhất quán (Consistency)** trong công thái học phần mềm: Giúp giảm tải nhận thức (Cognitive load), giúp lập trình viên nhanh chóng hình thành phản xạ tự nhiên, học cách sử dụng một tính năng một lần và áp dụng được ở mọi ngóc ngách của công cụ."
  },
  {
    "id": "ex-2.6",
    "type": "exercises",
    "category": "2.7 Terminology & Architecture",
    "number": "Exercise 2.6",
    "page": 100,
    "title": "Exercise 2.6: Định nghĩa các thuật ngữ trọng tâm của Chương 2",
    "description": "Giải thích ngắn gọn và chuẩn mực các khái niệm cốt lõi của môn học.\n\nHãy trình bày định nghĩa kỹ thuật ngắn gọn, súc tích cho 6 thuật ngữ sau:\na) Project\nb) IDE\nc) Debug\nd) Properties window\ne) Dialogs\nf) Visual Studio",
    "hint": "Mục 2.1 - 2.5 Deitel: Nắm vững vai trò của từng công cụ trong vòng đời phát triển phần mềm.",
    "image": null,
    "answer": "Định nghĩa chuẩn hóa theo Giáo trình Deitel & Deitel:\n\na) **Project (Dự án):** Là một tập hợp các tệp mã nguồn C#, tệp cấu hình, tham chiếu thư viện và tài nguyên đồ họa được tổ chức lại để cùng biên dịch thành một sản phẩm phần mềm duy nhất (như một tệp thực thi `.exe` hoặc thư viện `.dll`), được quản lý bởi tệp định dạng `.csproj`.\n\nb) **IDE (Integrated Development Environment - Môi trường Phát triển Tích hợp):** Gói phần mềm đa năng cung cấp toàn diện tất cả các công cụ cần thiết cho toàn bộ vòng đời phát triển phần mềm (soạn thảo code, thiết kế giao diện đồ họa, biên dịch mã, quản lý tài nguyên và dò tìm sửa lỗi) trên một giao diện thống nhất.\n\nc) **Debug (Gỡ lỗi / Dò lỗi):** Quy trình chạy ứng dụng dưới sự kiểm soát và giám sát của công cụ Debugger nhằm phát hiện, theo dõi giá trị biến, phân tích luồng thực thi và loại bỏ các lỗi logic (bugs) hoặc các ngoại lệ bất thường (Exceptions).\n\nd) **Properties window (Cửa sổ Thuộc tính):** Cửa sổ công cụ trong IDE (phím tắt F4) cho phép lập trình viên kiểm tra và cấu hình các thuộc tính ngoại quan (Appearance), hành vi (Behavior) và bố cục (Layout) của Form và các điều khiển đồ họa ngay tại thời điểm thiết kế (Design-Time).\n\ne) **Dialogs (Hộp thoại):** Các cửa sổ phụ chuyên dụng bật lên tạm thời trên màn hình để giao tiếp với người dùng: hiển thị thông báo, nhận xác nhận, hoặc hỗ trợ thực hiện một tác vụ cấu hình chi tiết (ví dụ: Font Dialog, OpenFileDialog, Color Dialog).\n\nf) **Visual Studio:** Bộ công cụ phát triển phần mềm hàng đầu thế giới do Microsoft phát triển, hỗ trợ lập trình đa ngôn ngữ (C#, F#, C++, VB.NET, TypeScript) và đa nền tảng (Desktop, Web, Cloud, Mobile, Game, AI)."
  },
  {
    "id": "ex-2.7",
    "type": "making-a-difference",
    "category": "GUI Project / Windows Forms",
    "number": "Exercise 2.7",
    "page": 101,
    "title": "Exercise 2.7: Đồ án Thiết kế Giao diện Đồng hồ Bấm giờ (Stop Watch GUI)",
    "description": "Tạo giao diện người dùng hoàn chỉnh cho ứng dụng đồng hồ bấm giờ thể thao theo Hình 2.36 giáo trình Deitel.\n\nHãy tạo giao diện đồ họa cho ứng dụng Stop Watch như minh họa tại Hình 2.36 trong giáo trình:\n1. Form: Đổi thuộc tính `Text` thành 'Stop Watch', chỉnh kích thước phù hợp.\n2. Màn hình thời gian: Thêm điều khiển `RichTextBox` hiển thị số to `00:00:00`, căn lề và định vị ở nửa trên của Form.\n3. Bảng điều khiển: Thêm một `GroupBox` hoặc bố trí hàng ngang 3 điều khiển `Button` mang nhãn lần lượt là 'Start', 'Stop', và 'Reset'.\n4. Căn chỉnh lề: Sử dụng đường Snap Lines để căn thẳng hàng các nút bấm và tạo khoảng cách đối xứng hai bên.",
    "hint": "Mục 2.7 Deitel: RichTextBox cho phép hiển thị phông chữ lớn, đặt ReadOnly để người dùng không sửa số giờ.",
    "image": "extracted_images/fig2_36_stopwatch_gui.png",
    "solutionCode": "Hướng dẫn từng bước thiết kế giao diện Stop Watch GUI:\n\n**Bước 1: Thiết lập Form chính:**\n- Mở Visual Studio, tạo dự án Windows Forms Application đặt tên `StopWatchGUI`.\n- Chọn Form1, mở Properties Window (F4), đặt thuộc tính `Text` = `Stop Watch`.\n- Đặt thuộc tính `Size` = `350, 220`, `StartPosition` = `CenterScreen`.\n\n**Bước 2: Thêm màn hình hiển thị số RichTextBox:**\n- Kéo thả điều khiển `RichTextBox` từ Toolbox vào nửa trên của Form.\n- Đặt thuộc tính `Text` = `00:00:00`.\n- Nhấp nút `[...]` ở thuộc tính `Font`: chọn phông `Segoe UI` (hoặc `Consolas`), kiểu `Bold`, cỡ chữ `28 pt`.\n- Đặt thuộc tính `ReadOnly` = `True` (ngăn người dùng gõ sửa số).\n- Đặt thuộc tính `Size` = `280, 60`, căn giữa theo chiều ngang của Form.\n\n**Bước 3: Thêm các nút bấm điều khiển (Buttons):**\n- Kéo 3 điều khiển `Button` vào nửa dưới của Form:\n  + Button 1: `(Name)` = `btnStart`, `Text` = `Start`, `Size` = `80, 35`.\n  + Button 2: `(Name)` = `btnStop`, `Text` = `Stop`, `Size` = `80, 35`.\n  + Button 3: `(Name)` = `btnReset`, `Text` = `Reset`, `Size` = `80, 35`.\n- Chọn cả 3 nút, vào menu `Format -> Align -> Middles` và `Format -> Horizontal Spacing -> Make Equal` để các nút thẳng hàng và cách đều nhau tăm tắp.\n\n**Bước 4: Kiểm thử giao diện:**\n- Nhấn phím `F5` để chạy ứng dụng ở Run Mode và kiểm tra độ sắc nét của giao diện.",
    "starterCode": "// Mã C# khởi tạo giao diện Form Stop Watch\nthis.Text = \"Stop Watch\";\nthis.ClientSize = new System.Drawing.Size(340, 180);\n\n// RichTextBox hiển thị đồng hồ\nRichTextBox rtbTimer = new RichTextBox();\nrtbTimer.Text = \"00:00:00\";\nrtbTimer.Font = new Font(\"Segoe UI\", 28, FontStyle.Bold);\nrtbTimer.Size = new Size(280, 65);\nrtbTimer.Location = new Point(30, 25);\nrtbTimer.ReadOnly = true;\nthis.Controls.Add(rtbTimer);\n\n// Các nút bấm điều khiển\nButton btnStart = new Button() { Text = \"Start\", Location = new Point(30, 110), Size = new Size(80, 35) };\nButton btnStop = new Button() { Text = \"Stop\", Location = new Point(130, 110), Size = new Size(80, 35) };\nButton btnReset = new Button() { Text = \"Reset\", Location = new Point(230, 110), Size = new Size(80, 35) };\nthis.Controls.AddRange(new Control[] { btnStart, btnStop, btnReset });"
  },
  {
    "id": "ex-2.8",
    "type": "making-a-difference",
    "category": "GUI Project / Security & Authentication",
    "number": "Exercise 2.8",
    "page": 101,
    "title": "Exercise 2.8: Đồ án Thiết kế Màn hình Đăng nhập (Login Form GUI)",
    "description": "Xây dựng giao diện đăng nhập chuẩn doanh nghiệp có Username, Password và nút kiểm ghi nhớ theo Hình 2.37 giáo trình Deitel.\n\nHãy thiết kế giao diện Màn hình Đăng nhập (Login Form) theo Hình 2.37 trong giáo trình Deitel:\n1. Form: Đặt `Text` = 'Login Form', `BackColor` = tông màu ấm hài hòa.\n2. Tiêu đề: Thêm Label tiêu đề lớn 'Please Sign In', phông `Bookman Old Style` (hoặc `Georgia`), `14.25 pt Bold`.\n3. Nhãn & Hộp nhập liệu: Thêm Label 'User Name:' đi kèm `TextBox`, Label 'Password:' đi kèm `TextBox` (đặt thuộc tính `PasswordChar` = '*').\n4. Tùy chọn: Thêm `CheckBox` với nhãn 'Remember me on this computer'.\n5. Nút bấm: Thêm hai nút 'OK' và 'Cancel' ở phía dưới.",
    "hint": "Mục 2.8 Deitel: Thuộc tính PasswordChar che mật khẩu; dùng Snap Lines để căn thẳng hàng hai TextBox.",
    "image": "extracted_images/fig2_37_login_form_gui.png",
    "solutionCode": "Hướng dẫn chi tiết xây dựng Login Form GUI:\n\n**Bước 1: Tùy biến thuộc tính Form:**\n- Tạo dự án `LoginFormGUI`.\n- Chọn Form, đặt `Text` = `Login Form`, `Size` = `380, 280`, `FormBorderStyle` = `FixedDialog`.\n- Đặt `BackColor` = `Bisque` (hoặc `NavajoWhite` trong tab Web).\n\n**Bước 2: Thêm nhãn tiêu đề chào mừng:**\n- Kéo điều khiển `Label` đặt ở đỉnh Form, `Text` = `Please Sign In`.\n- Font: `Bookman Old Style`, `14.25pt`, `Bold`.\n\n**Bước 3: Thêm các điều khiển nhập thông tin:**\n- Label 1: `Text` = `User Name:`, `Location` = `(30, 70)`.\n- TextBox 1: `(Name)` = `txtUserName`, `Location` = `(130, 68)`, `Size` = `190, 25`.\n- Label 2: `Text` = `Password:`, `Location` = `(30, 110)`.\n- TextBox 2: `(Name)` = `txtPassword`, `Location` = `(130, 108)`, `Size` = `190, 25`, thiết lập thuộc tính `PasswordChar` = `*` để che dấu mật khẩu.\n\n**Bước 4: Thêm CheckBox và Buttons:**\n- CheckBox: `Text` = `Remember me on this computer`, `Location` = `(130, 145)`.\n- Button OK: `Text` = `OK`, `Location` = `(130, 185)`, `Size` = `85, 30`.\n- Button Cancel: `Text` = `Cancel`, `Location` = `(235, 185)`, `Size` = `85, 30`.\n\n**Bước 5: Hoàn thiện:**\n- Bấm `F5` chạy thử. Thử gõ vào ô Password để chiêm ngưỡng ký tự ngôi sao `*` xuất hiện an toàn!",
    "starterCode": "// Mã C# thiết kế giao diện Login Form\nthis.Text = \"Login Form\";\nthis.BackColor = Color.Bisque;\nthis.ClientSize = new Size(360, 240);\n\nLabel lblTitle = new Label() {\n    Text = \"Please Sign In\",\n    Font = new Font(\"Bookman Old Style\", 14.25f, FontStyle.Bold),\n    AutoSize = true,\n    Location = new Point(30, 20)\n};\n\nTextBox txtUser = new TextBox() { Location = new Point(130, 65), Width = 190 };\nTextBox txtPass = new TextBox() { Location = new Point(130, 105), Width = 190, PasswordChar = '*' };\nCheckBox chkRemember = new CheckBox() { Text = \"Remember me on this computer\", Location = new Point(130, 140), AutoSize = true };\nButton btnOK = new Button() { Text = \"OK\", Location = new Point(130, 180), Size = new Size(85, 30) };\nButton btnCancel = new Button() { Text = \"Cancel\", Location = new Point(235, 180), Size = new Size(85, 30) };\n\nthis.Controls.AddRange(new Control[] { lblTitle, txtUser, txtPass, chkRemember, btnOK, btnCancel });"
  },
  {
    "id": "ex-2.9",
    "type": "making-a-difference",
    "category": "GUI Project / Layout & Panels",
    "number": "Exercise 2.9",
    "page": 102,
    "title": "Exercise 2.9: Đồ án Thiết kế Bàn phím Máy tính Bỏ túi (Calculator GUI)",
    "description": "Sử dụng các khung chứa Panel có viền Fixed3D để bài trí 20 nút bấm máy tính khoa học theo Hình 2.38 giáo trình Deitel.\n\nHãy tạo giao diện Bàn phím Máy tính Bỏ túi (Calculator GUI) theo Hình 2.38 trong giáo trình:\n1. Form: Đặt `Text` = 'Calculator', kích thước khoảng `260, 240`.\n2. Màn hình kết quả: Thêm `TextBox` ở đỉnh, đặt `Text` = '0', `TextAlign` = `Right` (căn lề phải), kích thước kéo dài theo chiều ngang.\n3. Panel 1 (Số 0-9): Thêm Panel kích thước `90, 120`, đặt `BorderStyle` = `Fixed3D` (hiệu ứng lõm xuống), chứa các nút số 0-9 và dấu chấm.\n4. Panel 2 (Toán tử): Thêm Panel kích thước `62, 120`, `BorderStyle` = `Fixed3D`, chứa các nút phép tính `*`, `/`, `-`, `+`, `=`.\n5. Panel 3 (Xóa & Nguồn): Thêm Panel kích thước `54, 62`, `BorderStyle` = `Fixed3D`, chứa các nút `C`, `C/A`, `OFF`.\n6. Kích thước nút: Nút số `23, 23`; nút '00' `52, 23`; nút 'OFF' `54, 23`; nút '+' kéo dài `23, 81`; nút 'C' và 'C/A' `44, 23`.",
    "hint": "Mục 2.9 Deitel: Panel giúp gom nhóm điều khiển logic; thuộc tính BorderStyle = Fixed3D tạo hiệu ứng khắc lõm chuyên nghiệp.",
    "image": "extracted_images/fig2_38_calculator_gui.png",
    "solutionCode": "Hướng dẫn chi tiết xây dựng Calculator GUI chuẩn mực:\n\n**Bước 1: Khởi tạo Form và Màn hình TextBox:**\n- Tạo dự án `CalculatorGUI`, đặt `Text` = `Calculator`, `ClientSize` = `240, 200`.\n- Thêm `TextBox` ở tọa độ `(15, 15)`, `Width` = `210`.\n- Trong Properties Window, chỉnh `Text` = `0`, `TextAlign` = `Right` (chữ số căn sát lề phải chuẩn máy tính).\n\n**Bước 2: Tạo và phân bố 3 khung Panel chứa linh kiện:**\n- *Panel Số (panelNumbers):* `Location` = `(15, 55)`, `Size` = `90, 120`, `BorderStyle` = `Fixed3D`.\n- *Panel Toán tử (panelOperators):* `Location` = `(115, 55)`, `Size` = `62, 120`, `BorderStyle` = `Fixed3D`.\n- *Panel Lệnh (panelCommands):* `Location` = `(185, 55)`, `Size` = `54, 120`, `BorderStyle` = `Fixed3D`.\n\n**Bước 3: Đặt các nút bấm (Buttons) vào bên trong từng Panel:**\n- Kéo các nút bấm thả trực tiếp vào bề mặt của từng Panel tương ứng.\n- Đặt thuộc tính `Size` chuẩn theo giáo trình:\n  + Các phím `0` đến `9`, dấu `.`, `*`, `/`, `-`, `=` có kích thước vuông vắn `23, 23`.\n  + Phím `00` có kích thước ngang gấp đôi `52, 23`.\n  + Phím `+` có kích thước dọc trải dài `23, 81`.\n  + Phím `C` (Clear) và `C/A` (Clear All) có kích thước `44, 23`.\n  + Phím `OFF` có kích thước `54, 23`.\n\n**Bước 4: Kiểm thử giao diện:**\n- Nhấn `F5` chạy thử. Các Panel lõm `Fixed3D` tạo hiệu ứng chiều sâu nổi khối cực kỳ đẹp mắt!",
    "starterCode": "// Mã C# xây dựng Calculator GUI bằng Panel\nthis.Text = \"Calculator\";\nthis.ClientSize = new Size(250, 190);\n\nTextBox txtDisplay = new TextBox() {\n    Text = \"0\",\n    TextAlign = HorizontalAlignment.Right,\n    Location = new Point(15, 12),\n    Width = 220\n};\nthis.Controls.Add(txtDisplay);\n\n// 3 Khung Panel lõm Fixed3D\nPanel pnlNum = new Panel() { Location = new Point(15, 45), Size = new Size(90, 130), BorderStyle = BorderStyle.Fixed3D };\nPanel pnlOp = new Panel() { Location = new Point(115, 45), Size = new Size(65, 130), BorderStyle = BorderStyle.Fixed3D };\nPanel pnlCmd = new Panel() { Location = new Point(190, 45), Size = new Size(55, 130), BorderStyle = BorderStyle.Fixed3D };\nthis.Controls.AddRange(new Control[] { pnlNum, pnlOp, pnlCmd });"
  },
  {
    "id": "ex-2.10",
    "type": "making-a-difference",
    "category": "GUI Project / Containers & Controls",
    "number": "Exercise 2.10",
    "page": 103,
    "title": "Exercise 2.10: Đồ án Thiết kế Đồng hồ Báo thức Điện tử (Alarm Clock GUI)",
    "description": "Kết hợp GroupBox tiêu đề, RadioButton loại trừ và màn hình Label số điện tử nền đen chữ bạc theo Hình 2.39 giáo trình Deitel.\n\nHãy thiết kế giao diện Đồng hồ Báo thức (Alarm Clock GUI) theo Hình 2.39 trong giáo trình:\n1. Form: Đặt `Text` = 'Alarm Clock', `Font` = `Segoe UI 9pt`, `Size` = `438, 170`.\n2. Bảng nút điều khiển: Bố trí 7 `Button` điều khiển chức năng ('Hour', 'Minute', 'Second', 'Alarm', 'Snooze'...) căn lề đối xứng.\n3. Khung phân nhóm buổi: Thêm `GroupBox` có `Text` = 'AM/PM', kích thước `100, 50`, đặt ở chính giữa theo trục ngang.\n4. Nút chọn buổi: Đặt hai `RadioButton` có nhãn 'AM' và 'PM' bên trong GroupBox.\n5. Màn hình đồng hồ số điện tử: Thêm `Label` có `Text` = '00:00:00', `BorderStyle` = `Fixed3D`, `BackColor` = `Black`, `ForeColor` = `Silver` (trong tab Web), `Font` = `12pt Bold`.",
    "hint": "Mục 2.10 Deitel: GroupBox hiển thị đường viền và tiêu đề; RadioButton cho phép chọn duy nhất 1 tùy chọn; màu Silver trên nền Black tạo phong cách đồng hồ số LED.",
    "image": "extracted_images/fig2_39_alarm_clock_gui.png",
    "solutionCode": "Hướng dẫn chi tiết xây dựng Alarm Clock GUI:\n\n**Bước 1: Thiết lập Form chính:**\n- Tạo dự án `AlarmClockGUI`, đặt `Text` = `Alarm Clock`, `Size` = `438, 170`.\n- Đặt phông chữ mặc định của Form là `Segoe UI 9pt`.\n\n**Bước 2: Thiết kế màn hình hiển thị đồng hồ LED số điện tử:**\n- Kéo thả điều khiển `Label` vào Form, đặt `Text` = `00:00:00`.\n- Đặt `BorderStyle` = `Fixed3D` (tạo khung màn hình LED lõm).\n- Chuyển `BackColor` sang màu `Black` (đen tuyền).\n- Chuyển `ForeColor` sang màu `Silver` (trong tab Web) để chữ số phát sáng nổi bật trên nền đen.\n- Chỉnh `Font` = `12pt Bold`, căn lề `TextAlign` = `MiddleCenter`.\n\n**Bước 3: Thêm GroupBox và RadioButton:**\n- Kéo `GroupBox` từ Toolbox vào Form, đổi `Text` = `AM/PM`, đặt `Size` = `100, 50`.\n- Kéo hai điều khiển `RadioButton` thả vào bên trong GroupBox: một nút `Text` = `AM`, một nút `Text` = `PM`.\n- Lưu ý: RadioButton đặt trong cùng một GroupBox sẽ tự động có tính chất loại trừ lẫn nhau (chỉ được chọn 1 trong 2).\n\n**Bước 4: Bố trí 7 nút bấm chức năng (Buttons):**\n- Thêm các nút bấm chỉnh giờ, phút, giây, báo thức và nút Snooze hoãn báo thức xung quanh màn hình LED.\n- Dùng tính năng Snap Lines để căn thẳng hàng các nút đối xứng hai bên.\n\n**Bước 5: Chạy thử nghiệm:**\n- Bấm `F5` chạy thử. Màn hình đồng hồ LED nền đen chữ bạc trông y hệt một chiếc đồng hồ điện tử thực thụ!",
    "starterCode": "// Mã C# thiết kế Alarm Clock GUI\nthis.Text = \"Alarm Clock\";\nthis.ClientSize = new Size(420, 135);\nthis.Font = new Font(\"Segoe UI\", 9);\n\n// Màn hình số LED điện tử\nLabel lblDisplay = new Label() {\n    Text = \"00:00:00\",\n    BackColor = Color.Black,\n    ForeColor = Color.Silver,\n    Font = new Font(\"Segoe UI\", 12, FontStyle.Bold),\n    TextAlign = ContentAlignment.MiddleCenter,\n    BorderStyle = BorderStyle.Fixed3D,\n    Size = new Size(95, 35),\n    Location = new Point(160, 20)\n};\n\n// GroupBox AM/PM\nGroupBox grpAMPM = new GroupBox() {\n    Text = \"AM/PM\",\n    Size = new Size(100, 50),\n    Location = new Point(160, 65)\n};\nRadioButton rdoAM = new RadioButton() { Text = \"AM\", Location = new Point(10, 20), Width = 40, Checked = true };\nRadioButton rdoPM = new RadioButton() { Text = \"PM\", Location = new Point(55, 20), Width = 40 };\ngrpAMPM.Controls.AddRange(new Control[] { rdoAM, rdoPM });\n\nthis.Controls.AddRange(new Control[] { lblDisplay, grpAMPM });"
  },
  {
    "id": "ex-2.11",
    "type": "making-a-difference",
    "category": "GUI Project / Complex Multimedia Layout",
    "number": "Exercise 2.11",
    "page": 103,
    "title": "Exercise 2.11: Đồ án Thiết kế Máy Nghe Đài Bán Dẫn (Radio GUI)",
    "description": "Tích hợp đầy đủ các điều khiển phức hợp: 4 GroupBoxes, 6 Buttons cài kênh, 2 CheckBoxes loa, TrackBar âm lượng, RadioButton AM/FM và PictureBox nốt nhạc theo Hình 2.40 giáo trình Deitel.\n\nHãy tạo giao diện Máy Nghe Đài Radio (Radio GUI) theo Hình 2.40 trong giáo trình Deitel:\n1. Form: Đặt `Text` = 'Radio', `Font` = `Segoe UI 9pt`, `Size` = `427, 194`.\n2. Khung Pre-set Stations: GroupBox `180, 55` chứa 6 Button số `1` đến `6` (kích thước `23, 23`).\n3. Khung Speakers: GroupBox `120, 55` chứa 2 CheckBox 'Rear' và 'Front'.\n4. Nút nguồn: Button 'Power On/Off' kích thước `75, 55`.\n5. Khung Volume Control: GroupBox `180, 70` chứa CheckBox 'Mute' và thanh trượt `TrackBar` chỉnh âm lượng.\n6. Khung Tuning: GroupBox `120, 70` chứa Label tần số số '92.9' (nền Black, chữ Silver, 12pt bold) và 2 RadioButton 'AM', 'FM'.\n7. Hình ảnh: Thêm PictureBox hiển thị linh vật nốt nhạc `MusicNote.gif` (`SizeMode` = `StretchImage`, kích thước `55, 70`).",
    "hint": "Mục 2.11 Deitel: TrackBar tạo thanh kéo âm lượng; AutoSize = False của Label cho phép chỉnh kích thước tự do; SizeMode = StretchImage giúp ảnh nốt nhạc vừa vặn khung hình.",
    "image": "extracted_images/fig2_40_radio_gui.png",
    "solutionCode": "Hướng dẫn chi tiết xây dựng kiệt tác giao diện Radio GUI:\n\n**Bước 1: Thiết lập Form chính:**\n- Tạo dự án `RadioGUI`, đặt `Text` = `Radio`, `Size` = `427, 194`.\n- Đặt phông chữ chung của Form là `Segoe UI 9pt`.\n\n**Bước 2: Hàng điều khiển trên (Top row):**\n- *GroupBox 'Pre-set Stations':* `Size` = `180, 55`, `Location` = `(15, 12)`. Bên trong đặt 6 nút bấm vuông kích thước `23, 23` mang nhãn `1, 2, 3, 4, 5, 6`.\n- *GroupBox 'Speakers':* `Size` = `120, 55`, `Location` = `(205, 12)`. Bên trong đặt 2 `CheckBox` mang nhãn `Rear` và `Front`.\n- *Nút 'Power On/Off':* `Size` = `75, 55`, `Location` = `(335, 12)`, `Text` = `Power On/Off`.\n\n**Bước 3: Hàng điều khiển dưới (Bottom row):**\n- *GroupBox 'Volume Control':* `Size` = `180, 75`, `Location` = `(15, 75)`. Đặt một `CheckBox` mang nhãn `Mute` và một thanh kéo `TrackBar` chỉnh âm lượng.\n- *GroupBox 'Tuning':* `Size` = `120, 75`, `Location` = `(205, 75)`:\n  + Thêm `Label` hiển thị đài `92.9`: `Size` = `50, 44`, `BackColor` = `Black`, `ForeColor` = `Silver`, `Font` = `12pt Bold`, `TextAlign` = `MiddleCenter`, `AutoSize` = `False`.\n  + Thêm 2 `RadioButton` nhãn `AM` và `FM` đặt dọc bên cạnh nhãn số.\n- *Khung ảnh PictureBox:* `Size` = `55, 75`, `Location` = `(345, 75)`. Đặt thuộc tính `SizeMode` = `StretchImage`, nạp hình ảnh nốt nhạc `MusicNote.gif` qua hộp thoại Select Resource.\n\n**Bước 4: Kiểm thử và thưởng thức:**\n- Nhấn phím `F5` để chạy ứng dụng. Kéo thanh trượt TrackBar, bấm các nút chọn đài và tận hưởng giao diện đầy sống động!",
    "starterCode": "// Mã C# xây dựng Radio GUI hoàn chỉnh\nthis.Text = \"Radio\";\nthis.ClientSize = new Size(415, 160);\nthis.Font = new Font(\"Segoe UI\", 9);\n\n// 1. GroupBox Pre-set Stations\nGroupBox grpStations = new GroupBox() { Text = \"Pre-set Stations\", Location = new Point(12, 10), Size = new Size(180, 60) };\nfor (int i = 1; i <= 6; i++) {\n    grpStations.Controls.Add(new Button() { Text = i.ToString(), Size = new Size(24, 25), Location = new Point(10 + (i-1)*27, 22) });\n}\n\n// 2. GroupBox Speakers\nGroupBox grpSpeakers = new GroupBox() { Text = \"Speakers\", Location = new Point(200, 10), Size = new Size(120, 60) };\ngrpSpeakers.Controls.Add(new CheckBox() { Text = \"Rear\", Location = new Point(10, 25), Width = 50 });\ngrpSpeakers.Controls.Add(new CheckBox() { Text = \"Front\", Location = new Point(65, 25), Width = 50 });\n\n// 3. Power Button\nButton btnPower = new Button() { Text = \"Power On/Off\", Location = new Point(330, 15), Size = new Size(75, 55) };\n\n// 4. Volume Control & TrackBar\nGroupBox grpVol = new GroupBox() { Text = \"Volume Control\", Location = new Point(12, 75), Size = new Size(180, 75) };\ngrpVol.Controls.Add(new CheckBox() { Text = \"Mute\", Location = new Point(10, 18), Width = 55 });\ngrpVol.Controls.Add(new TrackBar() { Location = new Point(10, 40), Width = 160, Height = 25 });\n\n// 5. Tuning & Frequency Display\nGroupBox grpTune = new GroupBox() { Text = \"Tuning\", Location = new Point(200, 75), Size = new Size(120, 75) };\nLabel lblFreq = new Label() {\n    Text = \"92.9\", AutoSize = false, Size = new Size(50, 42), Location = new Point(10, 22),\n    BackColor = Color.Black, ForeColor = Color.Silver, Font = new Font(\"Segoe UI\", 12, FontStyle.Bold),\n    TextAlign = ContentAlignment.MiddleCenter\n};\ngrpTune.Controls.Add(lblFreq);\ngrpTune.Controls.Add(new RadioButton() { Text = \"AM\", Location = new Point(65, 20), Width = 45 });\ngrpTune.Controls.Add(new RadioButton() { Text = \"FM\", Location = new Point(65, 45), Width = 45, Checked = true });\n\n// 6. PictureBox MusicNote\nPictureBox picNote = new PictureBox() {\n    Location = new Point(340, 75), Size = new Size(60, 75),\n    SizeMode = PictureBoxSizeMode.StretchImage,\n    BorderStyle = BorderStyle.FixedSingle\n};\n\nthis.Controls.AddRange(new Control[] { grpStations, grpSpeakers, btnPower, grpVol, grpTune, picNote });"
  }
];

const EXERCISES_CHAPTER_03 = [
  {
    "id": "3.1",
    "category": "self-review",
    "title": "Self-Review 3.1: Điền vào chỗ trống các khái niệm nền tảng",
    "description": "Củng cố các khái niệm cú pháp cơ bản của ứng dụng Console trong C#.",
    "question": "Điền từ hoặc cụm từ thích hợp vào chỗ trống trong các phát biểu sau:\na) Một _______ bắt đầu thân của mọi phương thức, và một _______ kết thúc thân của mọi phương thức.\nb) Hầu hết các câu lệnh trong C# kết thúc bằng một dấu _______.\nc) Câu lệnh _______ được sử dụng để đưa ra quyết định (rẽ nhánh).\nd) Ký hiệu _______ bắt đầu một dòng chú thích đơn (single-line comment).\ne) Dòng trống, ký tự dấu cách và ký tự _______ được gọi là khoảng trắng (whitespace).\nf) Các _______ là những từ ngữ được dành riêng cho ngôn ngữ C# sử dụng.\ng) Mọi ứng dụng C# đều bắt đầu thực thi tại phương thức _______.\nh) Các phương thức _______ và _______ của lớp Console dùng để hiển thị thông tin ra màn hình.\ni) Tính năng _______ cho phép bạn nhúng trực tiếp giá trị biến vào bên trong một chuỗi ký tự bằng dấu $.",
    "solution": "Đáp án chuẩn mực theo Giáo trình Deitel (trang 139):\n\na) **left brace ({)** (ngoặc nhọn mở), **right brace (})** (ngoặc nhọn đóng).\nb) **semicolon (;)** (dấu chấm phẩy).\nc) **if** (câu lệnh điều kiện if).\nd) **//** (hai dấu gạch chéo liền nhau).\ne) **tab characters** (ký tự tab, cùng với newline - ký tự xuống dòng).\nf) **Keywords** (từ khóa / reserved words).\ng) **Main** (phương thức Main viết hoa chữ M).\nh) **Console.WriteLine** và **Console.Write**.\ni) **string interpolation** (định dạng chuỗi nội suy với ký tự tiền tố $).",
    "hints": "Xem lại Mục 3.2 đến 3.5 trong giáo trình Deitel: cấu trúc Welcome1, escape sequences, và string interpolation.",
    "image": "images/fig3_01_welcome1_app.png",
    "type": "self-review"
  },
  {
    "id": "3.2",
    "category": "self-review",
    "title": "Self-Review 3.2: Nhận định Đúng / Sai và giải thích kỹ thuật",
    "description": "Kiểm tra sự thấu hiểu về hành vi của trình biên dịch, toán tử và tính năng chuỗi trong C#.",
    "question": "Xác định các phát biểu sau là Đúng (True) hay Sai (False). Nếu Sai, hãy giải thích rõ lý do kỹ thuật:\na) Chú thích (Comments) khiến máy tính hiển thị văn bản đứng sau dấu // lên màn hình khi ứng dụng chạy.\nb) C# xem hai biến number và NuMbEr là hoàn toàn giống nhau (identical).\nc) Toán tử chia lấy dư (%) chỉ có thể được sử dụng với các toán hạng kiểu số nguyên.\nd) Các toán tử số học *, /, %, + và - đều có cùng một mức độ ưu tiên tính toán.\ne) Một chuỗi nội suy (interpolated string) bắt buộc phải bắt đầu bằng ký tự $ đặt ngay trước chuỗi.",
    "solution": "Phân tích và lời giải chuẩn mực theo Giáo trình Deitel (trang 140):\n\na) **False (Sai)**. Chú thích không làm máy tính thực hiện bất kỳ hành động nào và bị trình biên dịch bỏ qua hoàn toàn. Chúng chỉ dùng để giải thích mã nguồn cho con người đọc.\nb) **False (Sai)**. C# là ngôn ngữ phân biệt hoa thường (case-sensitive), do đó `number` và `NuMbEr` là hai biến hoàn toàn khác nhau trong bộ nhớ.\nc) **False (Sai)**. Trong C#, toán tử chia lấy dư `%` có thể áp dụng cho cả số thực dấu phẩy động (float, double), ví dụ: `7.5 % 2.0 = 1.5`.\nd) **False (Sai)**. Các toán tử `*`, `/`, `%` có cùng mức độ ưu tiên cao hơn, còn `+` và `-` có mức độ ưu tiên thấp hơn.\ne) **True (Đúng)**. Chuỗi nội suy bắt buộc phải có ký tự tiền tố `$` đứng ngay trước dấu mở ngoặc kép `$\"...\"`.",
    "hints": "Phân biệt tính nhạy chữ hoa/thường, cơ chế toán tử % trên số thực trong C#, và thứ tự ưu tiên nhân chia trước cộng trừ sau.",
    "image": "images/fig3_19_operator_precedence.png",
    "type": "self-review"
  },
  {
    "id": "3.3",
    "category": "self-review",
    "title": "Self-Review 3.3: Viết câu lệnh thực thi các tác vụ cơ bản",
    "description": "Thực hành viết các câu lệnh khai báo biến, nhập xuất dữ liệu và so sánh điều kiện.",
    "question": "Viết câu lệnh C# chuẩn xác để hoàn thành mỗi tác vụ sau:\na) Khai báo các biến c, thisIsAVariable, q76354 và number thuộc kiểu dữ liệu int.\nb) In câu nhắc yêu cầu người dùng nhập một số nguyên: \"Enter an integer: \".\nc) Đọc một số nguyên từ bàn phím và gán kết quả cho biến value kiểu int.\nd) Nếu biến number khác 7, hiển thị thông báo \"The variable number is not equal to 7\".\ne) In chuỗi \"This is a C# app\" trên cùng một dòng trong cửa sổ console.\nf) In chuỗi \"This is a C# app\" trên hai dòng, dòng thứ nhất kết thúc bằng C# sử dụng Console.WriteLine.\ng) Sử dụng String Interpolation để hiển thị tổng của hai biến x và y.",
    "solution": "Mã nguồn câu lệnh chuẩn mực theo Giáo trình Deitel (trang 140):\n\n```csharp\n// a) Khai bao 4 bien kieu int\nint c;\nint thisIsAVariable;\nint q76354;\nint number;\n\n// b) Cau nhac nhap so nguyen khong xuong dong\nConsole.Write(\"Enter an integer: \");\n\n// c) Nhap chuoi va ep kieu sang int\nint value = int.Parse(Console.ReadLine());\n\n// d) Kiem tra dieu kien khac 7\nif (number != 7)\n{\n   Console.WriteLine(\"The variable number is not equal to 7\");\n}\n\n// e) In tren mot dong\nConsole.WriteLine(\"This is a C# app\");\n\n// f) In tren hai dong bang ky tu thoat \\n\nConsole.WriteLine(\"This is a C#\\napp\");\n\n// g) String Interpolation tinh tong\nConsole.WriteLine($\"The sum of {x} and {y} is {x + y}\");\n```",
    "hints": "Sử dụng int.Parse(Console.ReadLine()), toán tử khác !=, ký tự thoát \\n và cú pháp nội suy $.",
    "image": "images/fig3_14_addition_part1.png",
    "type": "self-review"
  },
  {
    "id": "3.4",
    "category": "self-review",
    "title": "Self-Review 3.4: Phát hiện và sửa lỗi cú pháp trong câu lệnh",
    "description": "Rèn luyện kỹ năng phân tích lỗi cú pháp (Syntax Errors) và lỗi logic thường gặp.",
    "question": "Chỉ ra lỗi và sửa lại cho đúng trong mỗi đoạn mã lệnh C# sau:\n\na)\n```csharp\nif (c < 7);\n{\n   Console.WriteLine(\"c is less than 7\");\n}\n```\n\nb)\n```csharp\nif (c => 7)\n{\n   Console.WriteLine(\"c is equal to or greater than 7\");\n}\n```",
    "solution": "Phân tích lỗi và phương án sửa chuẩn theo Giáo trình Deitel (trang 140):\n\na) **Lỗi:** Dấu chấm phẩy `;` đặt ngay sau dấu đóng ngoặc đơn của mệnh đề điều kiện `(c < 7)`. Dấu chấm phẩy này tạo thành một câu lệnh rỗng, khiến khối lệnh in phía sau luôn luôn được thực thi dù `c` có nhỏ hơn 7 hay không!\n   **Khắc phục:** Xóa bỏ dấu chấm phẩy sau `(c < 7)`:\n   ```csharp\n   if (c < 7)\n   {\n      Console.WriteLine(\"c is less than 7\");\n   }\n   ```\n\nb) **Lỗi:** Toán tử quan hệ viết sai thứ tự `=>`. Trong C#, toán tử lớn hơn hoặc bằng bắt buộc phải là `>=` (dấu `=>` dành riêng cho biểu thức lambda).\n   **Khắc phục:** Đổi `=>` thành `>=`:\n   ```csharp\n   if (c >= 7)\n   {\n      Console.WriteLine(\"c is equal to or greater than 7\");\n   }\n   ```",
    "hints": "Không bao giờ đặt dấu chấm phẩy ngay sau biểu thức if; toán tử lớn hơn hoặc bằng là >= chứ không phải =>.",
    "image": "images/fig3_09_syntax_error_ide.png",
    "type": "self-review"
  },
  {
    "id": "3.5",
    "category": "self-review",
    "title": "Self-Review 3.5: Các bước giải thuật tính tích của ba số nguyên",
    "description": "Thiết kế giải thuật và viết các dòng lệnh đơn lẻ tính tích 3 số nhập từ bàn phím.",
    "question": "Viết các khai báo biến, câu lệnh và chú thích thực hiện từng bước sau:\na) Viết chú thích nói rằng ứng dụng sẽ tính tích của ba số nguyên.\nb) Khai báo các biến x, y, z và result thuộc kiểu int.\nc) In câu nhắc yêu cầu người dùng nhập số nguyên thứ nhất.\nd) Đọc số nguyên thứ nhất từ bàn phím và lưu vào biến x.\ne) In câu nhắc và đọc số nguyên thứ hai lưu vào biến y.\nf) In câu nhắc và đọc số nguyên thứ ba lưu vào biến z.\ng) Tính tích của ba số x, y, z và gán kết quả cho biến result.\nh) Hiển thị thông báo \"Product is \" kèm giá trị biến result sử dụng String Interpolation.",
    "solution": "Mã lệnh từng bước chuẩn mực theo Giáo trình Deitel (trang 140):\n\n```csharp\n// a) Chú thích mô tả mục đích chương trình\n// Calculating the product of three integers\n\n// b) Khai báo 4 biến số nguyên\nint x; int y; int z; int result;\n\n// c & d) Nhập số thứ nhất\nConsole.Write(\"Enter first integer: \");\nx = int.Parse(Console.ReadLine());\n\n// e) Nhập số thứ hai\nConsole.Write(\"Enter second integer: \");\ny = int.Parse(Console.ReadLine());\n\n// f) Nhập số thứ ba\nConsole.Write(\"Enter third integer: \");\nz = int.Parse(Console.ReadLine());\n\n// g) Tính tích ba số nguyên\nresult = x * y * z;\n\n// h) Xuất kết quả bằng String Interpolation\nConsole.WriteLine($\"Product is {result}\");\n```",
    "hints": "Áp dụng kỹ thuật nhập liệu với int.Parse(Console.ReadLine()) và toán tử nhân * lặp lại cho 3 toán hạng.",
    "image": "images/fig3_14_addition_part2.png",
    "type": "self-review"
  },
  {
    "id": "3.6",
    "category": "self-review",
    "title": "Self-Review 3.6: Ứng dụng hoàn chỉnh Product.cs",
    "description": "Ghép nối các câu lệnh ở Bài 3.5 thành một ứng dụng C# hoàn chỉnh có thể biên dịch và chạy được.",
    "question": "Từ các câu lệnh đã viết ở Exercise 3.5, hãy đóng gói thành một chương trình C# hoàn chỉnh có tên lớp là Product, chứa phương thức Main và sử dụng không gian tên System. Chạy thử chương trình với ba số nguyên: 10, 20 và 30.",
    "solution": "Mã nguồn hoàn chỉnh `Product.cs` theo Giáo trình Deitel (Hình 3.24, trang 141):\n\n```csharp\n// Exercise 3.6: Product.cs\n// Calculating the product of three integers.\nusing System;\n\nclass Product\n{\n   static void Main()\n   {\n      int x;      // Lưu số nguyên thứ nhất do người dùng nhập\n      int y;      // Lưu số nguyên thứ hai do người dùng nhập\n      int z;      // Lưu số nguyên thứ ba do người dùng nhập\n      int result; // Lưu tích của ba số\n\n      Console.Write(\"Enter first integer: \");\n      x = int.Parse(Console.ReadLine());\n\n      Console.Write(\"Enter second integer: \");\n      y = int.Parse(Console.ReadLine());\n\n      Console.Write(\"Enter third integer: \");\n      z = int.Parse(Console.ReadLine());\n\n      result = x * y * z; // Thực hiện phép nhân trong bộ nhớ\n\n      Console.WriteLine($\"Product is {result}\");\n   } // kết thúc Main\n} // kết thúc class Product\n```\n\n**Kết quả chạy thử mẫu:**\n```text\nEnter first integer: 10\nEnter second integer: 20\nEnter third integer: 30\nProduct is 6000\n```",
    "hints": "Tạo dự án Console App trong Visual Studio, dán đoạn mã trên vào Program.cs và bấm Ctrl+F5 để chạy.",
    "image": "images/fig3_20_polynomial_evaluation.png",
    "type": "self-review"
  },
  {
    "id": "3.7",
    "category": "exercises",
    "title": "Exercise 3.7: Điền từ còn thiếu vào các nhận định nâng cao",
    "description": "Các khái niệm nâng cao về chỉ thị using, loại chú thích và thứ tự ngoặc lồng nhau.",
    "question": "Điền từ hoặc cụm từ thích hợp vào chỗ trống:\na) Mỗi chỉ thị using xác định một _______ chứa các lớp mà ứng dụng C# có thể sử dụng.\nb) Các ký hiệu _______ và _______ được dùng cho chú thích nhiều dòng (delimited comments).\nc) Các phép tính toán trong C# thường được thực hiện bởi các câu lệnh _______.\nd) Các toán tử số học có cùng mức độ ưu tiên với phép nhân (*) là phép chia (/) và phép _______.\ne) Khi các cặp ngoặc đơn trong biểu thức số học lồng nhau, cặp ngoặc _______ sẽ được tính toán trước tiên.\nf) Một vị trí trong bộ nhớ máy tính có thể chứa các giá trị khác nhau tại các thời điểm trong khi ứng dụng chạy được gọi là một _______.",
    "solution": "Đáp án chuẩn theo Giáo trình Deitel (trang 141):\n\na) **namespace** (không gian tên, ví dụ: System).\nb) **/* ** và ** */** (cặp ký hiệu mở và đóng chú thích khối nhiều dòng).\nc) **assignment** (câu lệnh gán / tính toán số học).\nd) **remainder (%)** (phép chia lấy dư).\ne) **innermost** (cặp ngoặc đơn nằm trong cùng nhất).\nf) **variable** (biến số).",
    "hints": "Nhớ lại: namespace gom nhóm các lớp; ngoặc trong cùng tính trước; biến lưu trữ giá trị khả biến trong RAM.",
    "image": "images/fig3_18_arithmetic_operators.png",
    "type": "exercises"
  },
  {
    "id": "3.8",
    "category": "exercises",
    "title": "Exercise 3.8: Viết câu lệnh in bảng tab và nhúng dấu ngoặc kép",
    "description": "Ứng dụng ký tự thoát \\t và \\\" trong thực tế định dạng văn bản.",
    "question": "Viết các câu lệnh C# thực hiện mỗi yêu cầu sau:\na) In dòng chữ \"Roll Number    Student Name    Grade\" trên một dòng đơn, phân cách các cột bằng tab stop.\nb) In ra màn hình ký tự dấu ngoặc kép đôi (\") bên trong một chuỗi văn bản.\nc) Khai báo một biến kiểu chuỗi có tên là courseName và khởi tạo giá trị ban đầu là \"C# Programming\".",
    "solution": "Mã nguồn câu lệnh C# chuẩn xác:\n\n```csharp\n// a) In tieu de bang bang ky tu thoat \\t\nConsole.WriteLine(\"Roll Number\\tStudent Name\\tGrade\");\n\n// b) In ky tu ngoac kep doi bang \\\"\nConsole.WriteLine(\"He said: \\\"C# is awesome!\\\"\");\n\n// c) Khai bao va khoi tao bien kieu string\nstring courseName = \"C# Programming\";\n```",
    "hints": "Sử dụng \\t cho tab ngang và \\\" cho dấu ngoặc kép đôi.",
    "image": "images/fig3_12_escape_sequences_table.png",
    "type": "exercises"
  },
  {
    "id": "3.9",
    "category": "exercises",
    "title": "Exercise 3.9: Nhận định Đúng / Sai về tên biến, IntelliSense và void",
    "description": "Đánh giá tính hợp lệ của quy tắc đặt tên định danh và cơ chế IntelliSense.",
    "question": "Xác định Đúng (True) hay Sai (False). Nếu Sai, hãy giải thích rõ lý do:\na) IntelliSense liệt kê các mục bắt đầu bằng hoặc chứa các chữ cái mà người dùng đã gõ.\nb) Các tên sau đây đều là tên biến hợp lệ trong C#: _under_bar_, m928134, t5, j7, her_sales, his_account_total, a, b, c, z và z2.\nc) Một biểu thức số học C# hợp lệ không chứa dấu ngoặc đơn luôn luôn được tính toán tuần tự từ trái sang phải.\nd) Từ khóa void chỉ ra rằng phương thức Main sẽ không trả về bất kỳ giá trị nào sau khi hoàn thành nhiệm vụ.",
    "solution": "Phân tích chuẩn xác theo Giáo trình Deitel (trang 141):\n\na) **True (Đúng)**. IntelliSense hỗ trợ tìm kiếm mờ (fuzzy search), hiển thị cả thành viên bắt đầu hoặc chứa chuỗi ký tự vừa gõ.\nb) **True (Đúng)**. Tất cả các tên này đều hợp lệ vì bắt đầu bằng chữ cái hoặc dấu gạch dưới `_`, và chỉ chứa chữ cái, chữ số, dấu gạch dưới.\nc) **False (Sai)**. Biểu thức không có ngoặc vẫn phải tuân thủ thứ tự ưu tiên của toán tử: các toán tử `*`, `/`, `%` được tính trước các toán tử `+`, `-` dù chúng đứng sau trong biểu thức!\nd) **True (Đúng)**. Từ khóa `void` biểu thị kiểu trả về rỗng, phương thức kết thúc mà không truyền giá trị về cho hệ điều hành.",
    "hints": "Nhớ rằng nhân chia luôn được ưu tiên tính trước cộng trừ dù không có ngoặc đơn; tên biến bắt đầu bằng dấu gạch dưới là hoàn toàn hợp lệ.",
    "image": "images/fig3_02_keywords_table.png",
    "type": "exercises"
  },
  {
    "id": "3.10",
    "category": "exercises",
    "title": "Exercise 3.10: Dự đoán kết quả hiển thị của String Interpolation",
    "description": "Rèn luyện khả năng đọc hiểu mã nguồn và cơ chế tính toán trong chuỗi nội suy $.",
    "question": "Giả sử biến x = 2 và y = 3, hãy cho biết mỗi câu lệnh sau đây sẽ in ra màn hình nội dung gì:\na) Console.WriteLine($\"x = {x}\");\nb) Console.WriteLine($\"Value of {x} + {x} is {x + x}\");\nc) Console.Write(\"x =\");\nd) Console.WriteLine($\"{x + y} = {y + x}\");",
    "solution": "Kết quả hiển thị chính xác trên màn hình Console:\n\na) `x = 2`\nb) `Value of 2 + 2 is 4`\nc) `x =` (không xuống dòng)\nd) `5 = 5`\n\n**Giải thích:** Các biểu thức `{x + x}` và `{x + y}` bên trong cặp ngoặc nhọn của chuỗi nội suy được tính toán tự động thành các số nguyên (4 và 5) trước khi chuyển đổi sang chuỗi và ghép vào dòng văn bản.",
    "hints": "Thay thế x bằng 2, y bằng 3 và tính toán các phép toán số học bên trong { }.",
    "image": "images/fig3_13_welcome4_interpolation.png",
    "type": "exercises"
  },
  {
    "id": "3.11",
    "category": "exercises",
    "title": "Exercise 3.11: Xác định câu lệnh làm thay đổi giá trị biến (Ghi đè phá hủy)",
    "description": "Phân biệt giữa thao tác đọc không phá hủy và thao tác ghi đè phá hủy ô nhớ.",
    "question": "Trong các câu lệnh C# sau đây, câu lệnh nào làm thay đổi giá trị của một biến (thao tác Destructive Write)?\na) p = i + j + k + 7;\nb) Console.WriteLine(\"variables whose values are modified\");\nc) Console.WriteLine(\"a = 5\");\nd) value = int.Parse(Console.ReadLine());",
    "solution": "Phân tích và đáp án chuẩn mực theo Giáo trình Deitel (trang 142):\n\n- **Câu a)**: **CÓ thay đổi**. Biến `p` nằm ở vế trái của toán tử gán `=` sẽ nhận giá trị mới từ tổng `i + j + k + 7`, giá trị cũ của `p` bị xóa vĩnh viễn (Destructive Write). Các biến `i`, `j`, `k` chỉ bị đọc nên không đổi.\n- **Câu b)**: **KHÔNG thay đổi**. Chỉ là câu lệnh in một chuỗi văn bản cố định ra màn hình console.\n- **Câu c)**: **KHÔNG thay đổi**. Mặc dù có chữ `a = 5` nhưng đây chỉ là ký tự bên trong chuỗi, không phải câu lệnh gán biến.\n- **Câu d)**: **CÓ thay đổi**. Biến `value` nhận giá trị số nguyên mới do người dùng nhập từ bàn phím thông qua toán tử gán `=`, giá trị cũ trong ô nhớ bị ghi đè hoàn toàn.",
    "hints": "Chỉ các câu lệnh có toán tử gán = với biến ở vế trái mới làm thay đổi ô nhớ của biến đó.",
    "image": "images/fig3_15_memory_number1.png",
    "type": "exercises"
  },
  {
    "id": "3.12",
    "category": "exercises",
    "title": "Exercise 3.12: Chuyển đổi biểu thức toán học sang mã lệnh C#",
    "description": "Viết biểu thức C# tương đương cho các công thức đại số toán học.",
    "question": "Chuyển các biểu thức toán học sau sang mã lệnh C# chuẩn xác:\na) Tích của m và n chia cho 2: (m * n) / 2\nb) Biểu thức tính diện tích hình thang: area = (a + b) * h / 2\nc) Biểu thức tính giá trị đa thức bậc 3: y = a * x^3 + 7",
    "solution": "Mã lệnh C# tương đương chuẩn mực:\n\n```csharp\n// a) Tich m va n chia 2 (neu can so thuc thi dung 2.0)\nint result1 = (m * n) / 2;\n\n// b) Dien tich hinh thang (can ngoac don de cong a + b truoc)\ndouble area = (a + b) * h / 2.0;\n\n// c) Da thuc bac 3 (khong dung dau mu ^ vi ^ la phep toan XOR)\nint y = a * x * x * x + 7;\n```",
    "hints": "Luôn dùng ngoặc đơn để chỉ rõ thứ tự ưu tiên; lũy thừa x^3 viết thành x * x * x.",
    "image": "images/fig3_20_polynomial_evaluation.png",
    "type": "exercises"
  },
  {
    "id": "3.14",
    "category": "exercises",
    "title": "Exercise 3.14: Ứng dụng tính toán Hình tròn (Circle)",
    "description": "Viết ứng dụng Console cho phép nhập bán kính r (kiểu int) và tính đường kính, chu vi, diện tích.",
    "question": "Viết một ứng dụng C# cho phép người dùng nhập vào bán kính của một hình tròn (số nguyên r kiểu int) và in ra màn hình:\n- Đường kính (Diameter = 2 * r)\n- Chu vi (Circumference = 2 * Math.PI * r)\n- Diện tích (Area = Math.PI * r * r)\nSử dụng hằng số Math.PI và định dạng chuỗi nội suy $.",
    "solution": "Mã nguồn hoàn chỉnh `Circle.cs`:\n\n```csharp\nusing System;\n\nclass Circle\n{\n   static void Main()\n   {\n      Console.Write(\"Nhap ban kinh hinh tron (so nguyen): \");\n      int r = int.Parse(Console.ReadLine());\n\n      int diameter = 2 * r;\n      double circumference = 2 * Math.PI * r;\n      double area = Math.PI * r * r;\n\n      Console.WriteLine($\"Duong kinh (Diameter): {diameter}\");\n      Console.WriteLine($\"Chu vi (Circumference): {circumference:F2}\");\n      Console.WriteLine($\"Dien tich (Area): {area:F2}\");\n   }\n}\n```",
    "hints": "Sử dụng Math.PI có sẵn trong không gian tên System; r * r để tính r bình phương.",
    "image": "images/fig3_26_multiplication_table.png",
    "type": "exercises"
  },
  {
    "id": "3.25",
    "category": "exercises",
    "title": "Exercise 3.25: Vẽ các hình khối bằng ký tự hoa thị (*)",
    "description": "Viết ứng dụng vẽ hình hộp chữ nhật, oval, mũi tên và hình thoi bằng các dấu sao.",
    "question": "Viết một ứng dụng Console C# sử dụng các câu lệnh Console.WriteLine để in ra 4 hình đồ họa đặt cạnh nhau: Hình hộp chữ nhật, Hình Oval, Mũi tên hướng lên, và Hình thoi (Diamond) như minh họa tại Hình 3.25 trong giáo trình Deitel.",
    "solution": "Mã nguồn hoàn chỉnh `Shapes.cs` theo Giáo trình Deitel:\n\n```csharp\nusing System;\n\nclass Shapes\n{\n   static void Main()\n   {\n      Console.WriteLine(\"*********     ***       *        *    \");\n      Console.WriteLine(\"*       *   *     *    ***      * *   \");\n      Console.WriteLine(\"*       *  *       *  *****    *   *  \");\n      Console.WriteLine(\"*       *  *       *    *     *     * \");\n      Console.WriteLine(\"*       *  *       *    *    *       *\");\n      Console.WriteLine(\"*       *  *       *    *     *     * \");\n      Console.WriteLine(\"*       *  *       *    *      *   *  \");\n      Console.WriteLine(\"*       *   *     *     *       * *   \");\n      Console.WriteLine(\"*********     ***       *        *    \");\n   }\n}\n```",
    "hints": "Mỗi dòng lệnh Console.WriteLine in ra một lát cắt ngang của cả 4 hình cùng một lúc.",
    "image": "images/fig3_25_shapes_output.png",
    "type": "exercises"
  },
  {
    "id": "3.26",
    "category": "exercises",
    "title": "Exercise 3.26: Bảng tính bình phương và lập phương từ 0 đến 10",
    "description": "In bảng số nguyên gồm 3 cột: number, square, cube từ 0 đến 10 sử dụng tab \\t.",
    "question": "Viết một ứng dụng C# tính và hiển thị bình phương (x^2) và lập phương (x^3) của các số từ 0 đến 10. Bảng in ra phải có tiêu đề ba cột: number, square, cube được căn chỉnh thẳng hàng bằng ký tự thoát \\t.",
    "solution": "Mã nguồn hoàn chỉnh `SquaresAndCubes.cs` theo Giáo trình Deitel:\n\n```csharp\nusing System;\n\nclass SquaresAndCubes\n{\n   static void Main()\n   {\n      Console.WriteLine(\"number\\tsquare\\tcube\");\n      Console.WriteLine($\"0\\t{0*0}\\t{0*0*0}\");\n      Console.WriteLine($\"1\\t{1*1}\\t{1*1*1}\");\n      Console.WriteLine($\"2\\t{2*2}\\t{2*2*2}\");\n      Console.WriteLine($\"3\\t{3*3}\\t{3*3*3}\");\n      Console.WriteLine($\"4\\t{4*4}\\t{4*4*4}\");\n      Console.WriteLine($\"5\\t{5*5}\\t{5*5*5}\");\n      Console.WriteLine($\"6\\t{6*6}\\t{6*6*6}\");\n      Console.WriteLine($\"7\\t{7*7}\\t{7*7*7}\");\n      Console.WriteLine($\"8\\t{8*8}\\t{8*8*8}\");\n      Console.WriteLine($\"9\\t{9*9}\\t{9*9*9}\");\n      Console.WriteLine($\"10\\t{10*10}\\t{10*10*10}\");\n   }\n}\n```",
    "hints": "Sử dụng String Interpolation $ kết hợp ký tự thoát \\t để căn thẳng các cột số.",
    "image": "images/fig3_26_multiplication_table.png",
    "type": "exercises"
  }
];

const EXERCISES_CHAPTER_04 = [
  {
    "id": "4.1",
    "category": "self-review",
    "title": "Self-Review 4.1: Điền vào chỗ trống các khái niệm nền tảng OOP C#",
    "description": "Củng cố các khái niệm cốt lõi: lớp, đối tượng, từ khóa, bổ từ truy cập và kiểu tiền tệ decimal.",
    "question": "Điền từ hoặc cụm từ thích hợp vào chỗ trống trong các phát biểu sau:\na) Ký tự định dạng _______ được sử dụng để hiển thị các giá trị số dưới định dạng tiền tệ (monetary format).\nb) Mọi khai báo lớp đều bắt đầu bằng từ khóa _______ theo sau ngay là tên của lớp.\nc) Toán tử _______ tạo ra một đối tượng của lớp được chỉ định ở bên phải từ khóa.\nd) Mỗi tham số trong danh sách tham số của phương thức phải chỉ định cả _______ và _______.\ne) Kiểu trả về _______ biểu thị rằng phương thức sẽ không trả về bất kỳ dữ liệu nào khi hoàn tất nhiệm vụ.\nf) Khi mỗi đối tượng của một lớp duy trì bản sao dữ liệu riêng của một thuộc tính, thuộc tính đó được gọi là một _______.\ng) Đối với một _______, trình biên dịch C# tự động sinh ra một biến thể hiện private ẩn cùng các bộ truy cập set và get.\nh) Các biến thuộc kiểu dữ liệu _______ thường được sử dụng chuyên dụng để biểu diễn các số tiền trong tài chính.\ni) Phương thức _______ của kiểu decimal chuyển đổi một chuỗi văn bản thành một giá trị kiểu decimal.\nj) Từ khóa public là một _______ (quy định phạm vi truy cập).",
    "solution": "Đáp án chuẩn mực theo Giáo trình Deitel (trang 179):\n\na) **C** (Ký tự định dạng tiền tệ Currency).\nb) **class** (từ khóa khai báo lớp).\nc) **new** (toán tử cấp phát bộ nhớ trên Heap và khởi tạo đối tượng).\nd) **type** (kiểu dữ liệu) và **name** (tên tham số).\ne) **void** (kiểu không trả về giá trị).\nf) **instance variable** (biến thể hiện / trường dữ liệu field).\ng) **auto-implemented property** (thuộc tính tự động `{ get; set`).\nh) **decimal** (kiểu số thực 128-bit độ chính xác cao 28-29 chữ số).\ni) **Parse** (phương thức `decimal.Parse`).\nj) **access modifier** (bổ từ truy cập / công cụ sửa đổi phạm vi).",
    "hints": "Xem lại Mục 4.2 đến 4.9 trong giáo trình Deitel: cấu trúc lớp Account, toán tử new, auto-properties và kiểu decimal.",
    "image": "images/fig4_03_uml_account.png",
    "type": "self-review"
  },
  {
    "id": "4.2",
    "category": "self-review",
    "title": "Self-Review 4.2: Nhận định Đúng / Sai và phân tích kỹ thuật",
    "description": "Kiểm tra sự thấu hiểu về quy ước đặt tên, cơ chế thuộc tính, khởi tạo biến và phạm vi truy cập trong C#.",
    "question": "Xác định các phát biểu sau là Đúng (True) hay Sai (False). Nếu Sai, hãy giải thích rõ lý do kỹ thuật:\na) Theo quy ước, tên phương thức bắt đầu bằng chữ cái thường và các từ tiếp theo viết hoa chữ cái đầu.\nb) Bộ truy cập get của một thuộc tính cho phép phía client sửa đổi giá trị của biến thể hiện tương ứng.\nc) Tất cả các biến thể hiện đều được khởi tạo mặc định là null.\nd) Cặp ngoặc đơn rỗng () theo sau tên phương thức biểu thị phương thức đó không yêu cầu bất kỳ tham số nào.\ne) Số lượng đối số trong lời gọi phương thức bắt buộc phải khớp với số lượng tham số trong khai báo phương thức.\nf) Các biến hoặc phương thức được khai báo với bổ từ private chỉ có thể truy cập bởi các thành viên trong cùng lớp.\ng) Các biến được khai báo trong thân của một phương thức cụ thể được gọi là biến thể hiện và dùng được ở mọi nơi trong lớp.\nh) Một khai báo thuộc tính bắt buộc phải chứa cả hai bộ truy cập get và set.\ni) Thân của mọi phương thức hoặc thuộc tính đều được bao bọc bởi cặp ngoặc nhọn mở và đóng { }.\nj) Các biến cục bộ được tự động khởi tạo giá trị mặc định khi khai báo.",
    "solution": "Phân tích và lời giải chuẩn mực theo Giáo trình Deitel (trang 179):\n\na) **False (Sai)**. Theo quy ước chuẩn C#, tên phương thức sử dụng PascalCase: viết hoa chữ cái đầu tiên của mọi từ cấu thành (ví dụ: `SetName`, `DisplayAccount`).\nb) **False (Sai)**. Bộ truy cập `get` dùng để ĐỌC (retrieve) giá trị; bộ truy cập `set` mới cho phép SỬA ĐỔI (modify) giá trị.\nc) **False (Sai)**. Biến thể hiện kiểu số được khởi tạo là `0`, kiểu `bool` là `false`, chỉ có các kiểu tham chiếu (reference types) mới khởi tạo là `null`.\nd) **True (Đúng)**. Cặp ngoặc đơn rỗng `()` chỉ ra phương thức không nhận tham số đầu vào.\ne) **True (Đúng)**. Số lượng và kiểu của đối số phải tương thích hoàn toàn với danh sách tham số.\nf) **True (Đúng)**. Bổ từ `private` bảo toàn nguyên lý đóng gói (Encapsulation), ngăn chặn truy cập trực tiếp từ bên ngoài.\ng) **False (Sai)**. Các biến khai báo trong thân phương thức là Biến cục bộ (Local Variables) và chỉ tồn tại trong nội bộ phương thức đó.\nh) **False (Sai)**. Thuộc tính có thể chỉ có `get` (chỉ đọc - read-only), chỉ có `set` (chỉ ghi), hoặc kết hợp `private set`.\ni) **True (Đúng)**. Cặp ngoặc nhọn `{ }` phân định khối mã lệnh (block).\nj) **False (Sai)**. Biến thể hiện mới được khởi tạo mặc định; biến cục bộ KHÔNG có giá trị mặc định và C# báo lỗi biên dịch nếu đọc biến cục bộ chưa gán giá trị.",
    "hints": "Phân biệt PascalCase vs camelCase, chức năng get/set, giá trị mặc định của biến thể hiện vs biến cục bộ.",
    "image": "images/fig4_04_conceptual_object.png",
    "type": "self-review"
  },
  {
    "id": "4.3",
    "category": "self-review",
    "title": "Self-Review 4.3: Phân biệt Biến cục bộ (Local Variables) vs Biến thể hiện (Instance Variables)",
    "description": "Phân tích chuyên sâu về vòng đời, vị trí khai báo, phạm vi hoạt động và cơ chế khởi tạo ô nhớ trong RAM.",
    "question": "Trình bày sự khác biệt căn bản giữa một Biến cục bộ (Local Variable) và một Biến thể hiện (Instance Variable) trên 4 phương diện kỹ thuật:\n1) Vị trí khai báo trong tệp mã nguồn C#.\n2) Phạm vi hoạt động (Scope) và khả năng nhìn thấy (Visibility).\n3) Vòng đời sinh mệnh (Lifetime) và phân vùng bộ nhớ (Stack vs Heap).\n4) Cơ chế gán giá trị mặc định (Default Initialization).",
    "solution": "Phân tích chuẩn mực theo Giáo trình Deitel (trang 179 - Mục 4.4.3):\n\n1) **Vị trí khai báo:**\n   - *Biến thể hiện:* Được khai báo trong thân lớp, bên ngoài mọi phương thức (thường có bổ từ `private`).\n   - *Biến cục bộ:* Được khai báo bên trong thân của một phương thức cụ thể hoặc trong danh sách tham số của hàm.\n\n2) **Phạm vi hoạt động:**\n   - *Biến thể hiện:* Có thể được truy cập bởi toàn bộ các phương thức bên trong lớp đó.\n   - *Biến cục bộ:* Chỉ tồn tại và được nhìn thấy duy nhất trong khối lệnh `{ }` bao bọc nó.\n\n3) **Vòng đời & Bộ nhớ:**\n   - *Biến thể hiện:* Được cấp phát trên Managed Heap cùng với đối tượng khi gọi toán tử `new`, tồn tại chừng nào đối tượng còn được tham chiếu.\n   - *Biến cục bộ:* Được cấp phát trên Stack khi phương thức được gọi, và lập tức bị xóa sổ khỏi bộ nhớ khi phương thức kết thúc.\n\n4) **Giá trị mặc định:**\n   - *Biến thể hiện:* Được C# tự động khởi tạo mặc định (`0` cho số, `false` cho boolean, `null` cho tham chiếu).\n   - *Biến cục bộ:* Không có giá trị mặc định; nếu cố tình đọc biến cục bộ chưa gán, trình biên dịch C# sẽ báo lỗi CS0165 ngay lập tức.",
    "hints": "Vẽ bảng so sánh 4 tiêu chí: Vị trí, Phạm vi (Scope), Vùng nhớ (Heap vs Stack), Giá trị mặc định.",
    "image": "images/fig4_02_account_class.png",
    "type": "self-review"
  },
  {
    "id": "4.4",
    "category": "self-review",
    "title": "Self-Review 4.4: Bản chất của Tham số Phương thức: Parameter vs Argument",
    "description": "Làm rõ vai trò truyền dữ liệu vào phương thức và phân biệt rạch ròi giữa Tham số hình thức và Đối số thực tế.",
    "question": "Giải thích mục đích của Tham số phương thức (Method Parameter). Điểm khác biệt bản chất giữa Tham số (Parameter) và Đối số (Argument) là gì?",
    "solution": "Phân tích chuẩn mực theo Giáo trình Deitel (trang 179 - Mục 4.4.1):\n\n1) **Mục đích của Tham số:**\n   - Cho phép phương thức tiếp nhận dữ liệu đầu vào từ nơi gọi để thực hiện nhiệm vụ được giao.\n   - Giúp phương thức trở nên tổng quát, linh hoạt và tái sử dụng được với các tập dữ liệu khác nhau.\n\n2) **Phân biệt Parameter vs Argument:**\n   - **Tham số (Parameter / Formal Parameter):** Là biến được khai báo trong phần đầu (header) của phương thức (ví dụ: `accountName` trong `public void SetName(string accountName)`).\n   - **Đối số (Argument / Actual Argument):** Là giá trị thực tế hoặc biểu thức được truyền vào phương thức khi thực hiện lời gọi hàm (ví dụ: `theName` trong `myAccount.SetName(theName)`). Khi hàm chạy, giá trị của đối số được sao chép vào cho tham số sử dụng.",
    "hints": "Tham số là biến khai báo ở định nghĩa hàm; đối số là giá trị thực tế truyền vào khi gọi hàm.",
    "image": "images/fig4_01_accounttest_app.png",
    "type": "self-review"
  },
  {
    "id": "4.5",
    "category": "exercise",
    "title": "Exercise 4.5: Mục đích của Hàm tạo (Constructor) trong Lập trình Hướng đối tượng",
    "description": "Phân tích vai trò của Constructor trong việc bảo toàn trạng thái hợp lệ của đối tượng ngay khi khai sinh.",
    "question": "Mục đích của Hàm tạo (Constructor) là gì? Tại sao Hàm tạo trong C# không bao giờ có kiểu dữ liệu trả về?",
    "solution": "Lời giải kỹ thuật theo Giáo trình Deitel (trang 180 - Mục 4.8):\n\n1) **Mục đích của Constructor:**\n   - Khởi tạo trạng thái ban đầu hợp lệ cho các biến thể hiện của đối tượng ngay khi đối tượng được sinh ra bằng toán tử `new`.\n   - Ngăn chặn việc đối tượng rơi vào trạng thái rỗng hoặc dữ liệu rác không nhất quán (inconsistent state).\n   - Thực hiện các thiết lập cần thiết (như mở kết nối, cấp phát tài nguyên) trước khi đối tượng phục vụ các yêu cầu tác vụ.\n\n2) **Tại sao Constructor không có kiểu trả về:**\n   - Constructor không phải là một phương thức thông thường. Nhiệm vụ của nó là cấu hình vùng nhớ đối tượng vừa được toán tử `new` cấp phát trên Heap.\n   - Toán tử `new` luôn tự động trả về một tham chiếu (reference) trỏ tới đối tượng mới được tạo; do đó constructor không cần và không được phép chỉ định bất kỳ kiểu trả về nào (kể cả `void`).",
    "hints": "Constructor đảm bảo đối tượng sinh ra ở trạng thái hợp lệ; toán tử new đã đảm nhận việc trả về tham chiếu đối tượng.",
    "image": "images/fig4_08_account_constructor.png",
    "type": "exercises"
  },
  {
    "id": "4.6",
    "category": "exercise",
    "title": "Exercise 4.6: Cơ chế Cấp phát Đối tượng: Toán tử new và Kiểu Giá trị",
    "description": "Khảo sát cơ chế cấp phát bộ nhớ của C# đối với Kiểu Tham chiếu và Kiểu Giá trị.",
    "question": "Giải thích cách một chương trình C# cấp phát bộ nhớ cho các biến thuộc Kiểu Giá trị (Value Types) so với Kiểu Tham chiếu (Reference Types) tạo bằng new.",
    "solution": "Phân tích bộ nhớ theo Giáo trình Deitel (Mục 4.3.2):\n\n1) **Kiểu Giá trị (Value Types - int, double, bool, struct):**\n   - Được cấp phát trực tiếp trên ngăn xếp **Stack** khi khai báo (ví dụ: `int x = 10;`).\n   - Ô nhớ của biến chứa trực tiếp dữ liệu thô, không cần gọi toán tử `new` (trừ một số trường hợp khởi tạo struct).\n   - Khi gán biến này cho biến khác, hệ thống sao chép toàn bộ giá trị nhị phân độc lập.\n\n2) **Kiểu Tham chiếu (Reference Types - class, string, array):**\n   - Bắt buộc phải dùng toán tử `new` để máy ảo CLR cấp phát vùng nhớ trên **Managed Heap** chứa dữ liệu đối tượng.\n   - Biến tham chiếu trên Stack chỉ lưu địa chỉ trỏ tới đối tượng trên Heap. Nếu chưa gọi `new`, biến mang giá trị `null`.",
    "hints": "So sánh Stack (lưu giá trị trực tiếp) và Heap (cấp phát bởi new, biến chỉ giữ tham chiếu địa chỉ).",
    "image": "images/fig4_04_conceptual_object.png",
    "type": "exercises"
  },
  {
    "id": "4.7",
    "category": "exercise",
    "title": "Exercise 4.7: Hàm tạo Mặc định (Default Constructor) và Quy tắc Thu hồi của C#",
    "description": "Hiểu rõ cơ chế tự động cung cấp và tự động loại bỏ Default Constructor của trình biên dịch C#.",
    "question": "Hàm tạo mặc định (Default Constructor) là gì? Điều gì sẽ xảy ra với hàm tạo mặc định khi bạn tự định nghĩa một hàm tạo có tham số trong lớp?",
    "solution": "Lời giải chuẩn xác theo Giáo trình Deitel (Mục 4.8.2):\n\n1) **Định nghĩa:**\n   - Hàm tạo mặc định là constructor công khai không có tham số (`public ClassName()`), có thân hàm rỗng, do trình biên dịch C# tự động tạo ra cho một lớp nếu lớp đó không có bất kỳ constructor nào.\n   - Nó khởi tạo các biến thể hiện về giá trị mặc định của hệ thống (`0`, `false`, `null`).\n\n2) **Quy tắc thu hồi:**\n   - Một khi lập trình viên đã tự tay khai báo BẤT KỲ một constructor nào (dù có 1 hay nhiều tham số), trình biên dịch C# sẽ **LẬP TỨC THU HỒI VÀ KHÔNG SINH RA** hàm tạo mặc định nữa!\n   - Khi đó, nếu phía client cố tình gọi `new ClassName()` mà không truyền tham số, chương trình sẽ báo lỗi biên dịch **CS7036: There is no argument given that corresponds to the required parameter**.\n   - Muốn vừa gọi được constructor có tham số, vừa gọi được không tham số, lập trình viên bắt buộc phải tự tay viết cả hai constructor (Constructor Overloading).",
    "hints": "Nhớ nguyên tắc: Có constructor tự viết -> C# xóa default constructor; muốn dùng cả hai phải tự overload.",
    "image": "images/fig4_10_uml_constructor.png",
    "type": "exercises"
  },
  {
    "id": "4.8",
    "category": "exercise",
    "title": "Exercise 4.8: Ưu điểm của Thuộc tính (Properties) trong C# so với C++ và Java",
    "description": "So sánh thiết kế ngôn ngữ C# Properties với các phương thức getter/setter truyền thống.",
    "question": "Mục đích của các bộ truy cập get và set trong Thuộc tính C# là gì? Thuộc tính C# mang lại ưu điểm vượt trội nào về cú pháp so với các phương thức get/set của Java hoặc C++?",
    "solution": "Phân tích theo Giáo trình Deitel (Mục 4.6):\n\n1) **Mục đích của get và set:**\n   - Bộ truy cập `get`: Thực thi khi client đọc thuộc tính, trả về giá trị biến thể hiện hoặc kết quả tính toán.\n   - Bộ truy cập `set`: Thực thi khi client gán dữ liệu cho thuộc tính, sử dụng từ khóa ngữ cảnh `value` để nhận giá trị mới và có thể thực hiện kiểm tra tính hợp lệ (Data Validation).\n\n2) **Ưu điểm vượt trội của C# Properties:**\n   - **Cú pháp tự nhiên, thanh lịch:** Trong Java/C++, lập trình viên phải gọi hàm dài dòng: `account.setName(\"Jane\");` và `account.getName();`. Trong C#, ta viết hệt như thao tác với biến thông thường: `account.Name = \"Jane\";` và `Console.WriteLine(account.Name);`.\n   - **Bảo toàn 100% nguyên lý đóng gói:** Mặc dù cú pháp nhìn như truy cập biến trực tiếp, nhưng bên dưới máy ảo vẫn thực thi mã lệnh của `get`/`set`, cho phép bảo vệ dữ liệu, kiểm tra hợp lệ hoặc chỉ cho phép đọc (`private set`).\n   - **Hỗ trợ Auto-Properties:** Cú pháp `{ get; set` siêu ngắn gọn không cần khai báo backing field.",
    "hints": "Cú pháp tự nhiên như biến thô nhưng bên dưới vẫn chạy logic get/set an toàn; từ khóa ngữ cảnh value.",
    "image": "images/fig4_06_account_properties.png",
    "type": "exercises"
  },
  {
    "id": "4.9",
    "category": "project",
    "title": "Exercise 4.9: Nâng cấp lớp Account với Phương thức Rút tiền Withdraw",
    "description": "Cài đặt phương thức Withdraw có cơ chế kiểm tra thấu chi tài khoản (overdraft protection) theo bài tập 4.9 giáo trình.",
    "question": "Nâng cấp lớp Account (Hình 4.11) để bổ sung phương thức Withdraw rút tiền từ tài khoản. Đảm bảo rằng số tiền rút không được vượt quá số dư hiện có. Nếu vượt quá, số dư không thay đổi và in ra thông báo: \"Withdrawal amount exceeded account balance.\". Nâng cấp tệp AccountTest (Hình 4.12) để kiểm thử phương thức Withdraw.",
    "solution": "Mã nguồn cài đặt phương thức Withdraw chuẩn mực:\n\n```csharp\n// Bo sung vao lop Account.cs\npublic void Withdraw(decimal withdrawalAmount)\n{\n   if (withdrawalAmount > 0.0m)\n   {\n      if (withdrawalAmount <= Balance)\n      {\n         Balance = Balance - withdrawalAmount; // Tru tien hop le\n      }\n      else\n      {\n         Console.WriteLine(\"Withdrawal amount exceeded account balance.\");\n      }\n   }\n}\n```",
    "hints": "Kiểm tra 2 điều kiện: số tiền rút phải dương, và withdrawalAmount <= Balance. Nếu lớn hơn thì in cảnh báo và không trừ tiền.",
    "image": "images/fig4_11_account_balance_p2.png",
    "type": "making-a-difference"
  },
  {
    "id": "4.10",
    "category": "project",
    "title": "Exercise 4.10: Thiết kế Lớp Quản lý Hồ sơ Sinh viên (Student Record Class)",
    "description": "Tạo lớp Student quản lý mã sinh viên, họ tên và điểm 3 môn học, kiểm tra điểm không âm, tính tổng và phần trăm.",
    "question": "Tạo lớp Student bao gồm: Id (string), Name (string), và điểm 3 môn thi: Score1, Score2, Score3 (decimal). Cung cấp Constructor khởi tạo 5 giá trị. Thuộc tính cho điểm số phải kiểm tra: nếu giá trị gán là số âm thì giữ nguyên điểm cũ. Xây dựng hai phương thức GetAggregate() tính tổng điểm 3 môn, và GetPercentage() tính tỷ lệ phần trăm (tổng / 50 * 100). Viết chương trình StudentRecordTest kiểm thử toàn bộ tính năng.",
    "solution": "Mã nguồn lớp Student.cs chuẩn mực:\n\n```csharp\npublic class Student\n{\n   public string Id { get; set\n   public string Name { get; set\n   private decimal score1;\n   private decimal score2;\n   private decimal score3;\n\n   public Student(string id, string name, decimal s1, decimal s2, decimal s3)\n   {\n      Id = id;\n      Name = name;\n      Score1 = s1;\n      Score2 = s2;\n      Score3 = s3;\n   }\n\n   public decimal Score1\n   {\n      get { return score1\n      set { if (value >= 0.0m) score1 = value\n   }\n\n   public decimal Score2\n   {\n      get { return score2\n      set { if (value >= 0.0m) score2 = value\n   }\n\n   public decimal Score3\n   {\n      get { return score3\n      set { if (value >= 0.0m) score3 = value\n   }\n\n   public decimal GetAggregate() => Score1 + Score2 + Score3;\n   public decimal GetPercentage() => (GetAggregate() / 50.0m) * 100.0m;\n}\n```",
    "hints": "Sử dụng backing field cho 3 điểm thi để validate value >= 0.0m trong bộ truy cập set; phương thức tính toán trả về decimal.",
    "image": "images/fig4_14_uml_balance.png",
    "type": "making-a-difference"
  },
  {
    "id": "4.11",
    "category": "project",
    "title": "Exercise 4.11: Thiết kế Lớp Quản lý Tài sản Doanh nghiệp (Asset Class)",
    "description": "Tạo lớp Asset gồm tên tài sản, giá trị và tỷ lệ khấu hao, kiểm tra dữ liệu không âm, tính giá trị sau khấu hao.",
    "question": "Tạo lớp Asset gồm: AssetName (string), AssetValue (decimal), DepreciationRate (decimal - tỷ lệ khấu hao từ 0.0 đến 1.0). Constructor khởi tạo 3 giá trị. Validation: nếu giá trị hoặc tỷ lệ khấu hao âm thì giữ nguyên giá trị cũ. Viết ứng dụng AssetTest tạo 2 tài sản, hiển thị số tiền khấu hao và giá trị còn lại, sau đó tăng giá trị tài sản thêm 5% và hiển thị lại.",
    "solution": "Mã nguồn lớp Asset.cs chuẩn mực:\n\n```csharp\npublic class Asset\n{\n   public string AssetName { get; set\n   private decimal assetValue;\n   private decimal depreciationRate;\n\n   public Asset(string name, decimal val, decimal rate)\n   {\n      AssetName = name;\n      AssetValue = val;\n      DepreciationRate = rate;\n   }\n\n   public decimal AssetValue\n   {\n      get => assetValue;\n      set { if (value >= 0.0m) assetValue = value\n   }\n\n   public decimal DepreciationRate\n   {\n      get => depreciationRate;\n      set { if (value >= 0.0m && value <= 1.0m) depreciationRate = value\n   }\n\n   public decimal GetDepreciationAmount() => AssetValue * DepreciationRate;\n   public decimal GetDepreciatedValue() => AssetValue - GetDepreciationAmount();\n}\n```",
    "hints": "Data validation trong set accessor; phương thức tính khấu hao = AssetValue * DepreciationRate.",
    "image": "images/fig4_13_format_specifiers.png",
    "type": "making-a-difference"
  },
  {
    "id": "4.12",
    "category": "project",
    "title": "Exercise 4.12: Thiết kế Lớp Coaching với Auto-Implemented Properties",
    "description": "Áp dụng thuộc tính tự động để thiết kế lớp đào tạo học phần ngắn gọn và thanh lịch.",
    "question": "Tạo lớp Coaching bao gồm 4 thuộc tính tự động: CourseName (string), InstructorName (string), TuitionFee (decimal), DurationWeeks (int). Viết Constructor và chương trình kiểm thử CoachingTest hiển thị thông tin học phần với định dạng học phí tiền tệ chuẩn :C.",
    "solution": "Mã nguồn lớp Coaching.cs sử dụng Auto-Properties:\n\n```csharp\npublic class Coaching\n{\n   public string CourseName { get; set\n   public string InstructorName { get; set\n   public decimal TuitionFee { get; set\n   public int DurationWeeks { get; set\n\n   public Coaching(string course, string instructor, decimal fee, int weeks)\n   {\n      CourseName = course;\n      InstructorName = instructor;\n      TuitionFee = fee;\n      DurationWeeks = weeks;\n   }\n}\n```",
    "hints": "Sử dụng cú pháp { get; set cho cả 4 thuộc tính để mã nguồn ngắn gọn tối đa.",
    "image": "images/fig4_07_uml_properties.png",
    "type": "making-a-difference"
  },
  {
    "id": "4.13",
    "category": "project",
    "title": "Exercise 4.13: Tái cấu trúc Mã nguồn: Phương thức Dùng chung DisplayAccount (DRY)",
    "description": "Áp dụng nguyên lý Don't Repeat Yourself để loại bỏ mã in tài khoản lặp lại 4 lần trong AccountTest.",
    "question": "Trong tệp AccountTest.cs (Hình 4.12), câu lệnh hiển thị tên và số dư tài khoản bị lặp lại nhiều lần. Khai báo phương thức tĩnh DisplayAccount nhận vào tham số là một đối tượng Account và in thông tin định dạng :C. Thay thế tất cả các câu lệnh in lặp trong Main bằng lời gọi đến DisplayAccount.",
    "solution": "Phương thức tĩnh DisplayAccount chuẩn mực theo Exercise 4.13 Deitel:\n\n```csharp\npublic static void DisplayAccount(Account accountToDisplay)\n{\n   Console.WriteLine($\"{accountToDisplay.Name}'s balance: {accountToDisplay.Balance:C}\");\n}\n\n// Trong Main, thay vi lap lai Console.WriteLine, ta goi:\nDisplayAccount(account1);\nDisplayAccount(account2);\n```",
    "hints": "Phương thức static nhận đối số kiểu Account; sử dụng string interpolation với định dạng :C.",
    "image": "images/fig4_12_accounttest_balance_p1.png",
    "type": "making-a-difference"
  },
  {
    "id": "4.14",
    "category": "making-a-difference",
    "title": "Exercise 4.14: Ứng dụng Y tế Số: Bộ Tính Nhịp Tim Mục Tiêu (HeartRates Calculator)",
    "description": "Xây dựng ứng dụng y tế số tính tuổi, nhịp tim tối đa và dải nhịp tim mục tiêu theo khuyến cáo của Hiệp hội Tim mạch Hoa Kỳ (AHA).",
    "question": "Theo AHA, nhịp tim tối đa = 220 - tuổi. Dải nhịp tim mục tiêu an toàn khi tập thể thao là từ 50% đến 85% nhịp tim tối đa. Tạo lớp HeartRates gồm: FirstName, LastName, BirthYear, CurrentYear. Constructor nhận dữ liệu này. Cung cấp các thuộc tính tính: Tuổi (Age), Nhịp tim tối đa (MaxHeartRate), Nhịp tim mục tiêu tối thiểu (MinTargetRate = 50%) và tối đa (MaxTargetRate = 85%). Viết app kiểm thử nhập thông tin và in kết quả sức khỏe.",
    "solution": "Mã nguồn lớp HeartRates.cs y tế số:\n\n```csharp\npublic class HeartRates\n{\n   public string FirstName { get; set\n   public string LastName { get; set\n   public int BirthYear { get; set\n   public int CurrentYear { get; set\n\n   public HeartRates(string firstName, string lastName, int birthYear, int currentYear)\n   {\n      FirstName = firstName;\n      LastName = lastName;\n      BirthYear = birthYear;\n      CurrentYear = currentYear;\n   }\n\n   public int Age => CurrentYear - BirthYear;\n   public int MaxHeartRate => 220 - Age;\n   public double MinTargetRate => MaxHeartRate * 0.50;\n   public double MaxTargetRate => MaxHeartRate * 0.85;\n}\n```",
    "hints": "Sử dụng expression-bodied properties (=>) để tính tuổi và dải nhịp tim mục tiêu 50%-85%.",
    "image": "images/fig4_13_format_specifiers.png",
    "type": "making-a-difference"
  },
  {
    "id": "4.15",
    "category": "making-a-difference",
    "title": "Exercise 4.15: Số hóa Hồ sơ Sức khỏe Cá nhân (Computerization of Health Records - HealthProfile)",
    "description": "Thiết kế hồ sơ sức khỏe điện tử EHR hoàn chỉnh tính BMI, tuổi, nhịp tim mục tiêu và phân loại thể trạng y tế.",
    "question": "Tạo lớp HealthProfile bao gồm: Họ tên, Giới tính, Ngày tháng năm sinh, Chiều cao (cm) và Cân nặng (kg). Xây dựng các phương thức/thuộc tính tính: Tuổi, Nhịp tim tối đa, Dải nhịp tim mục tiêu, và Chỉ số khối cơ thể BMI = weight / (heightInMeters * heightInMeters). Hiển thị bảng phân loại chuẩn WHO: Gầy (< 18.5), Bình thường (18.5-24.9), Thừa cân (25-29.9), Béo phì (>= 30).",
    "solution": "Mã nguồn lớp HealthProfile.cs chuẩn y tế quốc tế:\n\n```csharp\npublic class HealthProfile\n{\n   public string Name { get; set\n   public string Gender { get; set\n   public int BirthYear { get; set\n   public int CurrentYear { get; set\n   public double HeightCm { get; set\n   public double WeightKg { get; set\n\n   public HealthProfile(string name, string gender, int birthYear, int currentYear, double height, double weight)\n   {\n      Name = name;\n      Gender = gender;\n      BirthYear = birthYear;\n      CurrentYear = currentYear;\n      HeightCm = height;\n      WeightKg = weight;\n   }\n\n   public int Age => CurrentYear - BirthYear;\n   public int MaxHeartRate => 220 - Age;\n   public double BMI\n   {\n      get\n      {\n         double heightM = HeightCm / 100.0;\n         return WeightKg / (heightM * heightM);\n      }\n   }\n}\n```",
    "hints": "Tính chiều cao ra mét (HeightCm / 100.0) trước khi tính BMI; kết hợp với công thức nhịp tim AHA.",
    "image": "images/fig4_13_format_specifiers.png",
    "type": "making-a-difference"
  }
];


if (typeof window !== 'undefined') {
  window.EXERCISES_CHAPTER_01 = (typeof EXERCISES_CHAPTER_01 !== 'undefined') ? EXERCISES_CHAPTER_01 : [];
  window.EXERCISES_CHAPTER_02 = (typeof EXERCISES_CHAPTER_02 !== 'undefined') ? EXERCISES_CHAPTER_02 : [];
  window.EXERCISES_CHAPTER_03 = (typeof EXERCISES_CHAPTER_03 !== 'undefined') ? EXERCISES_CHAPTER_03 : [];
  window.EXERCISES_CHAPTER_04 = (typeof EXERCISES_CHAPTER_04 !== 'undefined') ? EXERCISES_CHAPTER_04 : [];
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { EXERCISES_CHAPTER_01, EXERCISES_CHAPTER_02, EXERCISES_CHAPTER_03, EXERCISES_CHAPTER_04 };
}
