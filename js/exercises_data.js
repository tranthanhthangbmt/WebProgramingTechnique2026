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
