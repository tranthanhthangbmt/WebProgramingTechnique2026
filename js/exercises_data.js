// ============================================================================
// HỌC PHẦN: KỸ THUẬT LẬP TRÌNH (4 TÍN CHỈ) - IT26M
// BỘ DỮ LIỆU BÀI TẬP CUỐI CHƯƠNG 1 (VISUAL C# HOW TO PROGRAM - DEITEL & DEITEL - CH.1, TRANG 67-72)
// GỒM 3 MỤC: SELF-REVIEW EXERCISES, EXERCISES, VÀ MAKING-A-DIFFERENCE EXERCISES
// TOÀN BỘ ĐÃ ĐƯỢC CHUYỂN NGỮ SANG TIẾNG VIỆT, TÍCH HỢP HÌNH ẢNH MINH HỌA VÀ ĐÁP ÁN ĐẦY ĐỦ
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

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { EXERCISES_CHAPTER_01 };
}

// ============================================================================
// HỌC PHẦN: KỸ THUẬT LẬP TRÌNH (4 TÍN CHỈ) - IT26M
// BỘ DỮ LIỆU BÀI TẬP CUỐI CHƯƠNG 2: INTRODUCTION TO VISUAL STUDIO AND VISUAL PROGRAMMING
// (VISUAL C# HOW TO PROGRAM - DEITEL & DEITEL - CH.2, TRANG 99-104)
// GỒM: SELF-REVIEW EXERCISES (2.1 - 2.6) VÀ GUI DESIGN PROJECTS (2.7 - 2.11)
// ============================================================================

// ============================================================================
// BÀI TẬP CUỐI CHƯƠNG & ĐỒ ÁN GUI C# - CHƯƠNG 2
// GIÁO TRÌNH: VISUAL C# HOW TO PROGRAM (DEITEL & DEITEL - 6TH EDITION)
// BẢN DỊCH TIẾNG VIỆT CHUẨN MỰC, HÌNH ẢNH GỐC & LỜI GIẢI WINDOWS FORMS
// ============================================================================
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

if (typeof window !== 'undefined') {
  window.EXERCISES_CHAPTER_01 = EXERCISES_CHAPTER_01;
  window.EXERCISES_CHAPTER_02 = EXERCISES_CHAPTER_02;
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { EXERCISES_CHAPTER_01, EXERCISES_CHAPTER_02 };
}
