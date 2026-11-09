// ============================================================================
// HỌC PHẦN: KỸ THUẬT LẬP TRÌNH (4 TÍN CHỈ) - IT26M
// APPLICATION LOGIC (PORTAL CONTROLLER, QUIZ ENGINE, EXERCISE HUB, SLIDE PLAYER)
// ============================================================================

// State Management
const AppState = {
  currentTab: 'overview',
  currentSlide: 1,
  totalSlides: 42,
  currentQuestionIndex: 0,
  quizFilter: 'all',
  userAnswers: {}, // questionId -> selectedOptionIndex
  exerciseFilter: 'all',
  theme: localStorage.getItem('theme') || 'light',
  isPlayingAudio: false
};

// ============================================================================
// INITIALIZATION
// ============================================================================
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initTabs();
  initSlidePlayer();
  initTheaterTranscript();
  initQuizEngine();
  initExerciseHub();
  initCodeRepository();
});

// ============================================================================
// THEME CONTROLLER
// ============================================================================
function initTheme() {
  if (AppState.theme === 'dark') {
    document.body.classList.add('dark-theme');
    updateThemeIcon('☀️');
  } else {
    document.body.classList.remove('dark-theme');
    updateThemeIcon('🌙');
  }

  const themeBtn = document.getElementById('themeToggleBtn');
  if (themeBtn) {
    themeBtn.addEventListener('click', () => {
      document.body.classList.toggle('dark-theme');
      const isDark = document.body.classList.contains('dark-theme');
      AppState.theme = isDark ? 'dark' : 'light';
      localStorage.setItem('theme', AppState.theme);
      updateThemeIcon(isDark ? '☀️' : '🌙');
    });
  }
}

function updateThemeIcon(icon) {
  const btn = document.getElementById('themeToggleBtn');
  if (btn) btn.textContent = icon;
}

// ============================================================================
// TAB NAVIGATION
// ============================================================================
function initTabs() {
  const tabBtns = document.querySelectorAll('.nav-tab-btn');
  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetTab = btn.getAttribute('data-tab');
      switchTab(targetTab);
    });
  });
}

function switchTab(tabId) {
  AppState.currentTab = tabId;

  // Update Buttons
  document.querySelectorAll('.nav-tab-btn').forEach(btn => {
    if (btn.getAttribute('data-tab') === tabId) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });

  // Update Panes
  document.querySelectorAll('.tab-pane').forEach(pane => {
    if (pane.id === `tab-${tabId}`) {
      pane.classList.add('active');
    } else {
      pane.classList.remove('active');
    }
  });

  // Scroll to top of content smoothly
  window.scrollTo({ top: 120, behavior: 'smooth' });
}

// ============================================================================
// SLIDE & TRANSCRIPT PLAYER
// ============================================================================
const SLIDE_TRANSCRIPTS = {
  "1": {
    "title": "KỸ THUẬT LẬP TRÌNH / C# - CHƯƠNG 1: GIỚI THIỆU VỀ MÁY TÍNH, INTERNET VÀ VISUAL C#",
    "speaker1": "Chào mừng tất cả các em sinh viên lớp IT26M Khóa 2026 đến với học phần Kỹ thuật Lập trình! Hôm nay chúng ta chính thức khởi động chương trình học với Chương 1: Giới thiệu về Máy tính, Internet và Visual C# - Introduction to Computers, the Internet and Visual C#. Bài giảng của chúng ta được thiết kế chuẩn mực theo giáo trình quốc tế danh tiếng Visual C# How to Program của hai tác giả Harvey Deitel và Paul Deitel. Đây là bước ngoặt quan trọng giúp các em chuyển dịch tư duy từ một người dùng công nghệ đơn thuần trở thành những kỹ sư phần mềm thực thụ, làm chủ các giải pháp kiến trúc hệ thống hiện đại.",
    "speaker2": "Dạ chào thầy! Cả lớp IT26M chúng em rất hào hứng với môn học này ạ. Chúng em đều biết C# và nền tảng .NET đang là một trong những công nghệ trụ cột của các tập đoàn phần mềm lớn, các hệ thống tài chính ngân hàng cũng như trong ngành công nghiệp game và ứng dụng đám mây. Chúng em rất mong muốn được thầy dẫn dắt qua bức tranh toàn cảnh của hệ thống máy tính và hành trình lập trình Visual C# ạ!"
  },
  "2": {
    "title": "Mục tiêu Bài học & Chuẩn đầu ra (CLOs)",
    "speaker1": "Để đảm bảo chất lượng đào tạo đại học chính quy chuẩn kiểm định quốc tế, bài học hôm nay hướng tới 5 chuẩn đầu ra (CLOs) cốt lõi được đo lường theo thang đo Bloom. Thứ nhất (CLO 1.1), các em giải thích được cấu trúc phần cứng, định luật Moore, 6 khối chức năng logic của máy tính và thang bậc phân cấp dữ liệu từ Bit đến Big Data. Thứ hai (CLO 1.2), nắm vững sự tiến hóa của các thế hệ ngôn ngữ lập trình và 3 trụ cột công nghệ đối tượng: Đóng gói, Kế thừa, Đa hình. Thứ ba (CLO 1.3), trình bày thấu đáo kiến trúc Microsoft .NET: máy ảo CLR, mã được quản lý Managed Code, mã trung gian MSIL, trình biên dịch tức thời JIT và tính độc lập nền tảng trên .NET 8+. Thứ tư (CLO 1.4), sử dụng thành thạo môi trường Visual Studio IDE: Solution, Project, Form Designer, Toolbox và Debugger. Và thứ năm (CLO 1.5), vận dụng mô hình Lập trình trực quan và Hướng sự kiện để thực hành chạy thử (Test-Drive), phân tích ứng dụng đồ họa tương tác Painter.",
    "speaker2": "Dạ thưa thầy, 5 mục tiêu chuẩn đầu ra này rất toàn diện và cân đối từ lý thuyết nền tảng đến kỹ năng thực chiến. Chúng em nhìn thấy rõ lộ trình tiến bộ của mình: vừa hiểu bản chất cơ chế hoạt động của máy tính bên dưới, vừa tự tay điều khiển môi trường IDE chuyên nghiệp ngay tại lớp ạ."
  },
  "3": {
    "title": "Tiến trình Bài học 3 Tiết (150 Phút Tích hợp)",
    "speaker1": "Nhìn lên slide 3, buổi học của chúng ta được tổ chức theo phương pháp sư phạm tích hợp hiện đại trong 3 tiết liên tục, tổng cộng 150 phút. Tiết 1 dành 50 phút tập trung vào Nền tảng tính toán & Dữ liệu: phần cứng, định luật Moore, 6 khối chức năng logic, phân cấp dữ liệu và đo lường byte, kết thúc bằng bài thực hành Lab 1 khảo sát máy tính phòng máy. Tiết 2 dành 50 phút đi sâu vào Tư duy đối tượng OOP & Kiến trúc nền tảng Microsoft .NET: tiến hóa ngôn ngữ, Compiler vs Interpreter, các trụ cột OOP, CLR, MSIL, JIT, kết thúc bằng bài thực hành Lab 2 làm quen .NET CLI. Tiết 3 dành 50 phút bùng nổ với Visual Studio IDE & Test-Drive ứng dụng đồ họa Painter theo mô hình Lập trình trực quan và Hướng sự kiện, kết thúc bằng bài tổng kết chuẩn đầu ra.",
    "speaker2": "Cách phân bổ này rất hợp lý thầy ạ! Cứ sau mỗi phần lý thuyết chuyên sâu là chúng em lại được bắt tay ngay vào một bài thực hành Hands-on Lab trên máy tính. Việc học đi đôi với hành tại chỗ chắc chắn sẽ giúp sinh viên chúng em nhớ sâu bản chất và không hề cảm thấy khô khan."
  },
  "4": {
    "title": "Tổng quan Vị thế của Ngôn ngữ C# & Nền tảng .NET",
    "speaker1": "Tại sao Khoa Công nghệ Thông tin lại lựa chọn C# làm ngôn ngữ lập trình chiến lược cho các kỹ sư tương lai Khóa 2026? C# được thiết kế bởi Anders Hejlsberg - kiến trúc sư huyền thoại, cha đẻ của Turbo Pascal, Delphi và TypeScript. C# là ngôn ngữ thanh lịch, hiện đại, kết hợp sức mạnh xử lý phần cứng hiệu năng cao của C++ với tính an toàn kiểu, sự trong sáng và năng suất phát triển siêu tốc của Java. Đặc biệt, hệ sinh thái .NET hiện nay là vô cùng khổng lồ và hoàn toàn đa nền tảng: từ phát triển web phân tán với ASP.NET Core, ứng dụng di động MAUI, ứng dụng doanh nghiệp đám mây Azure, cho đến phát triển game 2D/3D đỉnh cao trên nền tảng Unity. Với các phiên bản hiện đại như .NET 8 và .NET 9, hiệu năng xử lý của C# luôn đứng trong nhóm đầu thế giới về tốc độ I/O và tối ưu bộ nhớ.",
    "speaker2": "Dạ thưa thầy, quả thực là một hệ sinh thái quá mạnh mẽ và đa năng! Một ngôn ngữ mà vừa làm được cả web, ứng dụng máy tính, di động lẫn game 3D thực tế ảo thì sinh viên chúng em học xong sẽ có rất nhiều cơ hội việc làm rộng mở trong các dự án công nghệ lớn ạ."
  },
  "5": {
    "title": "Khái niệm Cốt lõi: Phần cứng & Phần mềm",
    "speaker1": "Các em nhìn lên Slide 5. Một hệ thống máy tính hoàn chỉnh luôn được tạo nên bởi mối quan hệ cộng sinh giữa Phần cứng (Hardware) và Phần mềm (Software). Phần cứng là tất cả các thiết bị vật lý hữu hình: từ bộ vi xử lý trung tâm CPU, các thanh nhớ RAM, ổ lưu trữ thể rắn SSD, cho đến màn hình, bàn phím và bo mạch chủ. Ở cấp độ bán dẫn, phần cứng chỉ biết thực thi trực tiếp các tín hiệu điện thế và lệnh máy nhị phân. Trong khi đó, Phần mềm chính là tập hợp các chỉ thị và chương trình mang tư duy con người để ra lệnh cho phần cứng làm việc. Nếu ví phần cứng là cơ bắp cung cấp năng lực tính toán vật lý, thì phần mềm chính là bộ não dẫn dắt và điều phối mọi hành vi của cỗ máy đó. Phần mềm được chia làm hai nhánh lớn: Phần mềm hệ thống như Windows, Linux quản lý tài nguyên; và Phần mềm ứng dụng do các lập trình viên chúng ta trực tiếp thiết kế.",
    "speaker2": "Em rất thích hình ảnh so sánh cơ bắp và bộ não của thầy ạ. Phần cứng dù có đắt tiền và tối tân đến đâu mà không có phần mềm điều khiển thì cũng chỉ là một khối kim loại bất động. Và sứ mệnh của kỹ sư CNTT chúng em chính là thổi hồn vào phần cứng đó bằng những dòng mã nguồn tối ưu!"
  },
  "6": {
    "title": "Máy tính & Internet trong Đời sống và Nghiên cứu",
    "speaker1": "Trong mục 1.2 của giáo trình, tác giả Deitel chỉ ra rằng máy tính và mạng Internet ngày nay đã thâm nhập và tái định hình mọi lĩnh vực của đời sống nhân loại. Trên slide là những ví dụ điển hình: Hồ sơ y tế điện tử EHR số hóa toàn bộ bệnh án, đơn thuốc và phân tích bản đồ gen giúp cứu sống hàng triệu bệnh nhân; Thiết bị bay không người lái Drones ứng dụng trong cứu hộ cứu nạn, nông nghiệp chính xác và giao hàng tự động; Hệ thống định vị toàn cầu GPS tính toán khoảng cách và dẫn đường vệ tinh chính xác đến từng phần nghìn giây; Robot y tế thông minh hỗ trợ phẫu thuật xâm lấn tối thiểu chính xác từng micromet; và Xe tự hành xử lý hàng tỷ phép tính mỗi giây từ cảm biến Lidar, Radar và Camera để đưa ra quyết định lái xe an toàn trong tích tắc.",
    "speaker2": "Những thành tựu này thật kỳ diệu thầy ạ! Nhìn vào những ứng dụng sống động này, chúng em càng ý thức sâu sắc rằng việc học lập trình không chỉ là gõ vài câu lệnh đơn giản, mà là trang bị kỹ năng để tạo ra các giải pháp có tầm ảnh hưởng to lớn đến sức khỏe, an toàn và tương lai của xã hội."
  },
  "7": {
    "title": "Phần cứng: Tốc độ Tính toán & Định luật Moore",
    "speaker1": "Nói về sức mạnh phần cứng máy tính, tốc độ tính toán đã có bước nhảy vọt phi thường trong lịch sử. Một chiếc máy tính cá nhân hiện nay có thể thực hiện hàng tỷ phép tính mỗi giây, đo bằng Gigahertz (GHz). Các siêu máy tính thế giới đã đạt ngưỡng hàng triệu tỷ phép tính mỗi giây, tức là hàng trăm Petaflops! Động lực thúc đẩy sự tăng trưởng thần kỳ này chính là Định luật Moore nổi tiếng, do Gordon Moore - nhà đồng sáng lập tập đoàn Intel công bố năm 1965. Định luật phát biểu rằng: Số lượng bóng bán dẫn (transistor) tích hợp trên một vi mạch điện tử sẽ tăng gấp đôi xấp xỉ sau mỗi 18 đến 24 tháng, trong khi giá thành sản xuất lại gần như không đổi! Rất sắc bén! Lợi thế là phần cứng ngày càng rẻ và mạnh, giúp chúng ta chạy được các mô hình AI/Machine Learning và đồ họa phức tạp trên máy cá nhân. Nhưng thách thức là: tốc độ xung nhịp đơn nhân đã chạm giới hạn vật lý nhiệt năng, buộc các hãng chip phải phát triển vi xử lý đa nhân (Multi-core). Điều này đòi hỏi lập trình viên hiện đại phải biết viết code tối ưu đa luồng, xử lý bất đồng bộ và tận dụng kiến trúc song song!",
    "speaker2": "Dạ thưa thầy, định luật Moore đã biến những cỗ máy tính khổng lồ chiếm cả căn phòng ngày xưa thành những con chip siêu nhỏ nằm gọn trong lòng bàn tay và smartphone ngày nay. Vậy đối với lập trình viên, định luật Moore mang lại lợi thế và thách thức gì ạ?"
  },
  "8": {
    "title": "Tổ chức Máy tính: 6 Khối Chức năng Logic (Phần 1)",
    "speaker1": "Dù máy tính có hiện đại đến đâu, về mặt kiến trúc logic, mọi máy tính số từ trước đến nay đều được tổ chức thành 6 khối chức năng logic chuẩn mực, được mô tả tại Hình 1.2 trong giáo trình. Nhìn lên slide 8, chúng ta tìm hiểu 3 khối đầu tiên: Khối thứ nhất là Khối nhập dữ liệu (Input unit) - đóng vai trò tiếp nhận thông tin từ thế giới bên ngoài vào máy tính qua các thiết bị như bàn phím, chuột, màn hình cảm ứng, micro, máy quét. Khối thứ hai là Khối xuất dữ liệu (Output unit) - chuyển phát thông tin đã được xử lý ra cho người dùng hoặc hệ thống khác qua màn hình hiển thị, máy in, loa thanh. Khối thứ ba là Bộ nhớ chính (Memory unit / RAM) - nơi lưu trữ dữ liệu và mã lệnh tạm thời với tốc độ truy xuất cực nhanh để CPU xử lý. Điểm mấu chốt của RAM là tính chất khả biến (volatile): dữ liệu trên RAM sẽ biến mất hoàn toàn ngay khi mất điện hoặc tắt máy! Hoàn toàn chính xác! Đó là lý do hệ thống máy tính luôn cần thêm một khối lưu trữ bền vững khác mà chúng ta sẽ tìm hiểu ngay ở slide tiếp theo.",
    "speaker2": "Dạ, vậy nên khi chúng em đang gõ văn bản hay viết code mà chưa kịp bấm Save mà bị mất điện đột ngột thì toàn bộ nội dung trong RAM sẽ bị mất trắng đúng không ạ?"
  },
  "9": {
    "title": "Tổ chức Máy tính: 6 Khối Chức năng Logic (Phần 2)",
    "speaker1": "Chúng ta sang slide 9 với 3 khối chức năng logic còn lại. Khối thứ tư là Đơn vị số học và logic (Arithmetic and Logic Unit - ALU) - đây là 'phân xưởng sản xuất' trực tiếp thực hiện mọi phép tính số học như cộng, trừ, nhân, chia và các phép toán so sánh logic như bằng nhau, lớn hơn, nhỏ hơn. Khối thứ năm là Bộ vi xử lý trung tâm (Central Processing Unit - CPU) - đóng vai trò 'bộ não chỉ huy', giám sát và điều phối nhịp nhàng toàn bộ hoạt động của tất cả các khối trong hệ thống. Trong các vi xử lý hiện đại, ALU và Khối điều khiển Control Unit được tích hợp trực tiếp chung trên một con chip CPU. Và khối thứ sáu là Bộ nhớ thứ cấp (Secondary Storage Unit) - kho chứa dữ liệu dung lượng lớn, dài hạn và bền bỉ như ổ cứng SSD, HDD, thẻ nhớ USB. Dữ liệu trên bộ nhớ thứ cấp có tính chất bền vững (persistent), vẫn tồn tại nguyên vẹn ngay cả khi máy tính bị ngắt nguồn điện.",
    "speaker2": "Dạ thưa thầy, em đã nắm rất rõ sự phân công lao động của 6 khối: Input đưa vào, RAM chứa tạm, ALU tính toán, CPU điều hành, Output đưa ra và Secondary Storage lưu giữ dài lâu ạ!"
  },
  "10": {
    "title": "Sơ đồ Luồng Dữ liệu giữa 6 Khối Kiến trúc Máy tính",
    "speaker1": "Bây giờ, các em hãy quan sát kỹ sơ đồ luồng dữ liệu trên Slide 10. Đây là bức tranh tổng hòa mô tả cách mà 6 khối phối hợp nhịp nhàng với nhau. Dữ liệu từ Input Unit được nạp vào Memory Unit (RAM). CPU điều phối lấy lệnh và dữ liệu từ RAM đưa vào các thanh ghi nội bộ, chuyển cho ALU tính toán và so sánh logic, rồi ghi kết quả ngược trở lại RAM, trước khi chuyển ra Output Unit hiển thị cho người dùng. Thầy muốn cả lớp IT26M ghi nhớ 'Nguyên lý Vàng' trong khung màu cam trên slide: CPU tuyệt đối không bao giờ làm việc và xử lý trực tiếp với các tệp tin trên ổ cứng SSD/HDD, vì chênh lệch tốc độ truy xuất giữa RAM và ổ cứng lên tới hàng nghìn lần! Mọi chương trình và dữ liệu muốn CPU thực thi bắt buộc 100% phải được nạp từ bộ nhớ thứ cấp lên bộ nhớ chính RAM trước tiên!",
    "speaker2": "Thảo nào mỗi khi chúng em nhấp đúp chuột để mở một phần mềm hay một tựa game nặng, máy tính luôn mất một khoảng thời gian chờ để tải dữ liệu từ ổ cứng SSD lên các thanh RAM rồi mới xuất hiện giao diện để chơi thầy ạ. Sơ đồ này giúp em hiểu thấu suốt nguyên lý hoạt động bên dưới của hệ điều hành!"
  },
  "11": {
    "title": "Phân cấp Dữ liệu (Data Hierarchy): Từ Bit đến Big Data",
    "speaker1": "Tiếp theo, chúng ta nghiên cứu mục 1.4 của giáo trình: Cấu trúc phân cấp dữ liệu (Data Hierarchy), minh họa trực quan từ Hình 1.3 của sách trên slide 11. Dữ liệu trong thế giới số được cấu thành từ cấp độ vi mô thấp nhất đến cấp độ vĩ mô cao nhất theo một trật tự kim tự tháp cực kỳ chặt chẽ: Cấp 1 là Bit (Binary Digit) - đơn vị dữ liệu nhỏ nhất chỉ chứa giá trị 0 hoặc 1. Cấp 2 là Byte (Ký tự / Character) - tập hợp gồm đúng 8 bits, ví dụ chuỗi 01001010 trong mã ASCII đại diện cho chữ cái 'J'. Cấp 3 là Field (Trường dữ liệu) - một nhóm các ký tự mang một ý nghĩa logic cụ thể, ví dụ trường Tên là 'Judy'. Cấp 4 là Record (Bản ghi) - tập hợp các trường liên quan mật thiết về một đối tượng, ví dụ bản ghi nhân sự gồm: Mã định danh, Họ tên, Lương, Ngày sinh. Cấp 5 là File (Tệp tin) - tập hợp của nhiều bản ghi có cùng cấu trúc. Cấp 6 là Database (Cơ sở dữ liệu) - hệ thống lưu trữ có tổ chức gồm nhiều bảng và tệp liên kết chặt chẽ. Và đỉnh cao hiện nay là Big Data - các kho dữ liệu khổng lồ hàng nghìn Terabyte, Petabyte với vận tốc sinh dữ liệu cực nhanh.",
    "speaker2": "Nhìn sơ đồ phân cấp này rất sáng rõ và logic thầy ạ! Nó giống như trong ngôn ngữ tự nhiên: từng nét chữ ghép thành chữ cái, các chữ cái ghép thành từ, các từ ghép thành câu, các câu thành đoạn văn và các đoạn văn hợp thành một cuốn sách vậy."
  },
  "12": {
    "title": "Bảng Đo lường Dung lượng Dữ liệu: Từ KB đến YB",
    "speaker1": "Khi dữ liệu tích lũy ngày càng nhiều, chúng ta đo lường chúng như thế nào? Giáo trình cung cấp Bảng đo lường Hình 1.4 trên slide 12. Trong khoa học máy tính, do hệ thống vận hành trên hệ nhị phân, các bội số dung lượng được tính theo lũy thừa của 2, cụ thể là 2 mũ 10 bằng 1024. Cứ 1024 Bytes tạo thành 1 Kilobyte (KB). 1024 KB thành 1 Megabyte (MB - xấp xỉ 1 triệu byte). 1024 MB thành 1 Gigabyte (GB - xấp xỉ 1 tỷ byte). Tiếp theo là Terabyte (TB - nghìn tỷ), Petabyte (PB - triệu tỷ), Exabyte (EB - tỷ tỷ), Zettabyte (ZB) và lớn nhất hiện nay là Yottabyte (YB - 2 mũ 80 bytes). Thầy có một câu đố thực tế: Tại sao khi các em đi mua một chiếc ổ cứng di động ghi trên vỏ hộp là 500 GB, nhưng khi cắm vào máy tính Windows thì hệ điều hành chỉ báo dung lượng khả dụng khoảng 465 GB? Có phải nhà sản xuất đã 'lừa' chúng ta không? Xuất sắc tuyệt vời! 500 tỷ byte của nhà sản xuất chia cho 1024 mũ 3 sẽ ra đúng 465,66 GB trên Windows. Hiểu bản chất nhị phân giúp kỹ sư chúng ta không bao giờ bị nhầm lẫn khi thiết kế kiến trúc lưu trữ dữ liệu!",
    "speaker2": "Dạ em cũng từng rất thắc mắc điều này ạ! Có phải là vì nhà sản xuất phần cứng tính theo hệ thập phân, coi 1 GB là 10 mũ 9 tức là đúng 1 tỷ byte; trong khi hệ điều hành Windows lại chia theo hệ nhị phân chuẩn, lấy 1 GB bằng 1024 nhân 1024 nhân 1024 tức là khoảng 1 tỷ 73 triệu byte, dẫn đến con số hiển thị bị chênh lệch khoảng 7% đúng không thầy?"
  },
  "13": {
    "title": "[CHECKPOINT 1] Kiểm tra Nhanh Kiến thức Tiết 1",
    "speaker1": "Để chắc chắn rằng cả lớp IT26M đã thấu suốt toàn bộ kiến thức của Tiết 1 trước khi bước vào phòng thực hành, thầy mời cả lớp cùng giải quyết Checkpoint 1 trên slide 13. Câu hỏi 1: Khối chức năng logic nào trong máy tính trực tiếp thực hiện các phép so sánh logic như A > B? Bốn phương án: 1. Input unit, 2. Memory unit (RAM), 3. Arithmetic and Logic Unit (ALU), 4. Secondary storage unit. Em chọn đáp án nào? Hoàn toàn chính xác! Sang Câu hỏi số 2: Trong cấu trúc phân cấp dữ liệu, cấp độ nào bao gồm một nhóm các trường (fields) có liên quan chặt chẽ với nhau về cùng một đối tượng? Bốn phương án: 1. Byte, 2. Record (Bản ghi), 3. Bit, 4. Character. Chuẩn xác 100%! Cả lớp đã nắm lý thuyết rất vững vàng. Giờ chúng ta bước vào bài thực hành đầu tiên!",
    "speaker2": "Dạ thưa thầy, Câu hỏi 1 em chọn phương án số 3: ALU - Arithmetic and Logic Unit ạ! Vì ALU chính là bộ phận chuyên trách mọi phép tính toán số học và so sánh logic. Dạ thưa thầy, Câu hỏi 2 em chọn phương án số 2: Record - Bản ghi ạ! Vì một bản ghi gom nhóm các trường thông tin như Mã sinh viên, Họ tên, Điểm số của cùng một sinh viên. Còn Byte hay Character chỉ là cấp độ ký tự đơn lẻ phía dưới thôi ạ."
  },
  "14": {
    "title": "[HANDS-ON LAB 1] Khảo sát Phần cứng & Tính toán Nhị phân",
    "speaker1": "Bây giờ là 15 phút thực hành tại chỗ của Tiết 1. Tất cả các bạn sinh viên ngồi trước máy tính phòng thực hành thực hiện 2 nhiệm vụ: Nhiệm vụ 1: Nhấn tổ hợp phím Ctrl + Shift + Esc để mở Task Manager, chọn tab Performance. Quan sát và ghi lại các thông số phần cứng thực tế của máy: Tên vi xử lý CPU, Xung nhịp cơ bản (GHz), Số nhân vật lý (Cores) và Số luồng xử lý (Logical Processors), cùng dung lượng và xung nhịp của bộ nhớ RAM. Sau đó mở PowerShell hoặc Command Prompt, gõ lệnh wmic cpu get name, numberofcores, numberoflogicalprocessors, maxclockspeed để so sánh kết quả. Nhiệm vụ 2: Lấy giấy bút giải bài tập chuyển đổi số nguyên 45 từ hệ thập phân sang chuỗi nhị phân 6 bits. Bắt đầu nào! Quá chuẩn mực! Các em đã kết hợp hoàn hảo giữa công cụ khảo sát hệ điều hành hiện đại và tư duy tính toán nhị phân nền tảng.",
    "speaker2": "Thưa thầy, em vừa chạy lệnh trên máy phòng lab của em rồi ạ! Máy báo CPU Intel Core i7-13700H với 14 nhân và 20 luồng xử lý cực kỳ mạnh mẽ, RAM 16 GB tốc độ 3200 MHz. Còn về bài toán nhị phân, số 45 tách thành: 32 + 8 + 4 + 1, tương ứng với các vị trí lũy thừa của 2, cho ra kết quả nhị phân chính xác là 1 0 1 1 0 1 gồm 6 bits ạ!"
  },
  "15": {
    "title": "Tổng kết Trọng tâm Tiết 1 & Chuẩn bị Tiết 2",
    "speaker1": "Như vậy chúng ta đã hoàn thành trọn vẹn Tiết 1. Thầy đúc kết lại 3 trụ cột vàng mà các em cần ghi nhớ trong sổ tay: Thứ nhất, Định luật Moore là động lực phát triển phần cứng trong suốt nửa thế kỷ qua. Thứ hai, Kiến trúc 6 khối chức năng logic máy tính và nguyên lý bắt buộc mọi dữ liệu phải nạp lên RAM để CPU xử lý. Thứ ba, Cấu trúc phân cấp dữ liệu từ Bit, Byte, Field, Record, File, Database đến Big Data. Trước khi bước vào Tiết 2, thầy đặt ra các câu hỏi suy ngẫm: Làm thế nào con người có thể điều khiển được hàng tỷ bóng bán dẫn của phần cứng làm việc theo ý muốn? Ngôn ngữ lập trình đã tiến hóa như thế nào? Và tại sao Microsoft lại tạo ra ngôn ngữ C# và nền tảng .NET mang tính cách mạng? Thầy mời cả lớp giải lao 5 phút!",
    "speaker2": "Dạ, bài học Tiết 1 rất cuốn hút và rõ ràng thầy ạ. Chúng em sẽ nghỉ giải lao ít phút và sẵn sàng tâm thế để bước vào thế giới lập trình hướng đối tượng và kiến trúc .NET trong Tiết 2 ạ!"
  },
  "16": {
    "title": "Các Thế hệ Ngôn ngữ Lập trình (Language Evolution)",
    "speaker1": "Chào mừng các em quay trở lại với Tiết 2! Chúng ta cùng tìm hiểu mục 1.5 của giáo trình: Các thế hệ ngôn ngữ lập trình (Language Evolution) trên slide 16. Để con người có thể giao tiếp và điều khiển máy tính, lịch sử đã trải qua 3 bước tiến lớn: Thế hệ thứ nhất là Ngôn ngữ máy (Machine Language) - đây là thứ ngôn ngữ 'bản địa' duy nhất mà CPU hiểu và thực thi trực tiếp, bao gồm toàn bộ các chuỗi số nhị phân 0 và 1. Nhược điểm chí tử của nó là cực kỳ khó viết, dễ xảy ra sai sót, phụ thuộc hoàn toàn vào phần cứng của từng loại chip và con người gần như không thể bảo trì nổi. Thế hệ thứ hai là Hợp ngữ (Assembly Language) - các nhà khoa học đã dùng các từ tiếng Anh viết tắt mang tính gợi nhớ (mnemonics) như LOAD, ADD, STORE để thay cho chuỗi số 0-1, và cần một chương trình dịch gọi là Assembler để chuyển về mã máy. Tuy nhiên nó vẫn phụ thuộc chặt chẽ vào kiến trúc vi xử lý. Đúng vậy! Ra đời từ thập niên 1950 với Fortran, COBOL, rồi đến C, C++, Java, Python và C#. Ngôn ngữ bậc cao có cú pháp tiếng Anh trong sáng, logic toán học gần gũi với tư duy con người và hoàn toàn độc lập với phần cứng. Nhờ đó, một lập trình viên có thể viết nên những hệ thống phần mềm đồ sộ mà không cần bận tâm bên dưới CPU đang bật tắt transistor nào!",
    "speaker2": "Và bước nhảy vọt thực sự của nhân loại chính là Thế hệ thứ ba - Ngôn ngữ bậc cao (High-Level Languages) đúng không thầy?"
  },
  "17": {
    "title": "Biên dịch (Compiler) vs Thông dịch (Interpreter)",
    "speaker1": "Nhưng làm thế nào để máy tính thực thi được mã nguồn ngôn ngữ bậc cao do con người viết? Slide 17 so sánh hai cơ chế xử lý kinh điển: Trình biên dịch (Compiler) và Trình thông dịch (Interpreter). Trình biên dịch sẽ đọc và dịch toàn bộ mã nguồn chương trình thành một tệp mã máy hoàn chỉnh trước khi chạy. Ưu điểm là chương trình chạy với tốc độ cực nhanh và phát hiện toàn bộ lỗi cú pháp ngay từ đầu; đại diện là C, C++, Rust, Go. Ngược lại, Trình thông dịch không dịch trước mà đọc từng dòng lệnh, dịch tức thời dòng đó sang mã máy và thực thi ngay trước khi chuyển sang dòng tiếp theo; ưu điểm là linh hoạt, thử nghiệm nhanh nhưng tốc độ thực thi lại rất chậm; đại diện là Python, JavaScript, Ruby. Câu hỏi cực kỳ xuất sắc! C# và Java không đi theo hai lối mòn truyền thống đó, mà áp dụng một Cơ chế Lai (Hybrid Approach) mang tính cách mạng: Mã nguồn C# ban đầu được trình biên dịch dịch thành một dạng Mã trung gian siêu tối ưu gọi là MSIL. Sau đó, khi chương trình được khởi chạy, một Trình biên dịch tức thời JIT Compiler nằm bên trong máy ảo sẽ dịch từng đoạn mã trung gian này sang mã máy bản địa với tốc độ chớp nhoáng. Cơ chế lai này vừa giữ được hiệu năng thực thi cực nhanh của Compiler, vừa đạt được tính độc lập đa nền tảng linh hoạt của Interpreter!",
    "speaker2": "Dạ thưa thầy, vậy ngôn ngữ C# và Java thuộc loại nào trong hai nhóm trên ạ?"
  },
  "18": {
    "title": "Công nghệ Đối tượng (Object Technology)",
    "speaker1": "Giờ chúng ta bước vào một trong những tư duy quan trọng nhất của kỹ sư phần mềm hiện đại: Công nghệ đối tượng (Object Technology), được tác giả Deitel trình bày rất sâu sắc trong mục 1.6. Trong thế giới thực quanh ta, mọi thứ đều là Đối tượng (Objects): chiếc ô tô, điện thoại thông minh, con người, tài khoản ngân hàng. Mỗi đối tượng luôn sở hữu hai khía cạnh: Thứ nhất là Thuộc tính (Attributes / Properties) thể hiện trạng thái và đặc điểm như màu sơn xe, số dư tài khoản. Thứ hai là Hành vi (Behaviors / Methods) thể hiện các hành động đối tượng có thể làm như xe tăng tốc, nhấn còi, rút tiền, chuyển khoản. Mục tiêu tối thượng của Lập trình hướng đối tượng (OOP) chính là Tái sử dụng phần mềm (Software Reuse)! Thay vì mỗi lần làm dự án mới ta lại phải ngồi cặm cụi viết lại từng thuật toán sơ khai từ đầu, các kỹ sư sẽ tận dụng lại các lớp đối tượng chuẩn mực đã được kiểm thử chất lượng cao từ các thư viện có sẵn. Giống như các kỹ sư ô tô chế tạo xe mới từ các khối động cơ, hộp số và bánh xe tiêu chuẩn, việc tái sử dụng giúp năng suất phát triển phần mềm tăng lên gấp hàng chục lần và giảm thiểu tối đa rủi ro lỗi phần mềm!",
    "speaker2": "Dạ thưa thầy, việc mô hình hóa phần mềm mô phỏng theo các đối tượng ngoài đời thực mang lại lợi ích lớn nhất là gì cho ngành công nghiệp phần mềm ạ?"
  },
  "19": {
    "title": "Phân biệt Lớp (Class) và Đối tượng (Object)",
    "speaker1": "Để học tốt C#, các em phải phân biệt rạch ròi giữa hai khái niệm Lớp (Class) và Đối tượng (Object) trên slide 19. Lớp (Class) chính là Bản vẽ thiết kế (Blueprint) hay khuôn mẫu định nghĩa cấu trúc dữ liệu và hành vi chung. Hãy tưởng tượng bản vẽ thiết kế một chiếc ô tô trên giấy: nó quy định chiếc xe có 4 bánh, có vô lăng, có động cơ và có phương thức khởi động. Nhưng bản thân bản vẽ trên giấy thì không thể tự nổ máy hay chạy trên đường cao tốc được! Đối tượng (Object / Instance) chính là một thực thể sống cụ thể được chế tạo ra từ bản vẽ lớp đó. Ví dụ: chiếc xe VinFast VF8 màu đỏ mang biển kiểm soát 43A-12345 đang lăn bánh trên đường chính là một Object cụ thể. Hoàn toàn chính xác! Hiểu sâu bản chất bản vẽ Class và thực thể Object trong RAM là các em đã nắm giữ chìa khóa của lập trình hướng đối tượng.",
    "speaker2": "Em hiểu rồi ạ! Từ một bản vẽ Class duy nhất, nhà máy có thể dập ra hàng vạn chiếc xe Object khác nhau với màu sắc và số khung số máy riêng biệt. Trong code C#, khi chúng ta viết từ khóa new, ví dụ: Car myCar = new Car(\"VinFast VF8\", \"Do\"); thì toán tử new đó chính là lệnh ra lệnh cho máy tính xuất xưởng cấp phát vùng nhớ RAM cho một Object mới đúng không thầy?"
  },
  "20": {
    "title": "3 Trụ Cột Công Nghệ Đối Tượng Trong C#",
    "speaker1": "Trong C#, công nghệ đối tượng được xây dựng vững chắc trên 3 Trụ cột cốt lõi: Trụ cột 1 là Đóng gói (Encapsulation) - gom nhóm toàn bộ dữ liệu thuộc tính và phương thức xử lý vào chung một Class, đồng thời che giấu các chi tiết cài đặt nội bộ. Giống như người lái xe ô tô chỉ cần biết đạp chân ga để xe tăng tốc, mà không cần và không được phép thò tay can thiệp trực tiếp vào kim phun xăng điện tử bên trong động cơ! Điều này bảo vệ dữ liệu nội bộ không bị sửa đổi trái phép. Trụ cột 2 là Kế thừa (Inheritance) - cho phép tạo ra Class mới kế thừa toàn bộ thuộc tính và hành vi của Class có sẵn mà không cần viết lại mã nguồn, đồng thời bổ sung các tính năng riêng biệt. Ví dụ: Lớp XeDien kế thừa từ OTo nhưng bổ sung thêm thuộc tính DungLuongPin. Trụ cột 3 là Đa hình (Polymorphism) - cho phép các đối tượng thuộc các lớp khác nhau cùng phản hồi với một thông điệp theo những cách thức riêng biệt, giúp mã nguồn cực kỳ linh hoạt và dễ mở rộng.",
    "speaker2": "Ba trụ cột này bổ trợ cho nhau thật hoàn hảo thầy ạ! Đóng gói giúp an toàn dữ liệu, Kế thừa giúp tái sử dụng tối đa mã nguồn, và Đa hình giúp kiến trúc hệ thống thích ứng mềm dẻo với mọi thay đổi trong tương lai."
  },
  "21": {
    "title": "Internet và World Wide Web: Các Cột Mốc Tiến Hóa",
    "speaker1": "Tiếp theo, mục 1.7 đưa chúng ta nhìn lại các cột mốc tiến hóa vĩ đại của mạng máy tính toàn cầu trên Slide 21. Năm 1969, mạng ARPANET ra đời bởi Bộ Quốc phòng Mỹ, tiên phong áp dụng kỹ thuật chuyển mạch gói (packet switching) - nền móng của giao thức kết nối TCP/IP hiện nay. Năm 1989, nhà khoa học máy tính Tim Berners-Lee tại CERN đã phát minh ra World Wide Web cùng ngôn ngữ HTML và giao thức HTTP, mở ra kỷ nguyên kết nối tri thức nhân loại qua mạng Internet. Thập niên 2000 đánh dấu sự chuyển mình sang Web 2.0 với các trang web tương tác người dùng cao, mạng xã hội và dịch vụ điện toán đám mây Cloud Computing như Microsoft Azure hay AWS, cho phép thuê năng lực tính toán phân tán toàn cầu. Và ngày nay là Internet vạn vật (IoT), kết nối hàng tỷ thiết bị thông minh từ cảm biến đến ô tô vào không gian số.",
    "speaker2": "Nhìn lại lịch sử mới thấy tốc độ phát triển của ngành CNTT thật kinh ngạc thầy ạ. Chính hạ tầng Internet và Web toàn cầu này là mảnh đất màu mỡ để ngôn ngữ C# và nền tảng .NET vươn lên khẳng định vị thế dẫn đầu trong phát triển phần mềm phân tán."
  },
  "22": {
    "title": "Ngôn Ngữ C#: Lịch Sử Hình Thành & Chuẩn Hóa",
    "speaker1": "Chúng ta cùng đến với mục 1.8: Ngôn ngữ C# và lịch sử ra đời của nó. Vào năm 2000, tập đoàn Microsoft công bố sáng kiến nền tảng .NET mang tầm nhìn thế kỷ, và C# chính thức được trình làng như là ngôn ngữ cờ đầu của nền tảng này. Người chỉ huy đội ngũ thiết kế C# không ai khác chính là huyền thoại Anders Hejlsberg. C# nhanh chóng được chuẩn hóa quốc tế bởi hiệp hội ECMA với mã hiệu ECMA-334 và tổ chức tiêu chuẩn hóa thế giới ISO/IEC 23270. Các em có biết nguồn gốc rất thú vị của tên gọi C# không? Rất đúng! Dấu thăng mang thông điệp về sự nâng cấp, tiến bộ vượt bậc. Đặc biệt hơn, về mặt hình học, nếu các em nhìn kỹ dấu thăng #, nó chính là sự ghép lại của 4 dấu cộng '+' của C++! Điều đó ngụ ý rằng C# kế thừa toàn bộ tinh hoa sức mạnh của C++ nhưng ở một đẳng cấp cao hơn, hiện đại hơn, an toàn hơn và năng suất hơn gấp bội!",
    "speaker2": "Dạ em nghe nói dấu thăng (#) trong âm nhạc có nghĩa là thăng tiến, cao hơn nốt nhạc gốc nửa cung đúng không thầy?"
  },
  "23": {
    "title": "Đặc Trưng Cốt Lõi Của C#",
    "speaker1": "Slide 23 tổng hợp những đặc trưng cốt lõi làm nên sức hấp dẫn của C#: Thứ nhất, C# là ngôn ngữ Hướng đối tượng thuần 100% (Pure OOP) - mọi đoạn mã, mọi hàm đều bắt buộc phải nằm trong một Class, không có hàm tự do bên ngoài. Thứ hai, C# hỗ trợ Lập trình trực quan (Visual Programming) mạnh mẽ, cho phép kéo thả giao diện đồ họa. Thứ ba, Định kiểu tĩnh mạnh mẽ và An toàn kiểu (Type-safe) giúp phát hiện hầu hết lỗi dữ liệu ngay lúc biên dịch. Thứ tư, Cơ chế Thu gom rác tự động (Garbage Collection - GC) tự động giải phóng vùng nhớ RAM khi đối tượng không còn được sử dụng, xóa tan hoàn toàn nỗi ác mộng rò rỉ bộ nhớ (memory leaks) vốn làm đau đầu các lập trình viên C/C++. Cuối cùng là hỗ trợ lập trình bất đồng bộ hiện đại với cặp từ khóa async/await và khả năng chạy đa nền tảng tuyệt đối.",
    "speaker2": "Cơ chế Thu gom rác tự động (Garbage Collection) đúng là một cứu cánh tuyệt vời cho lập trình viên thầy ạ! Chúng em có thể yên tâm khởi tạo đối tượng bằng toán tử new để phục vụ bài toán mà không phải loay hoay ngồi viết lệnh malloc hay free để giải phóng từng byte nhớ thủ công nữa."
  },
  "24": {
    "title": "Các Phong Cách Lập Trình Đa Dạng Trong C#",
    "speaker1": "Điểm đặc biệt khiến C# trở thành ngôn ngữ 'vạn năng' chính là sự tích hợp hài hòa nhiều phong cách lập trình đa dạng trên Slide 24: Một là Lập trình Hướng sự kiện (Event-Driven) - ứng dụng phản hồi linh hoạt các hành động click chuột, gõ phím của người dùng; đây là cốt lõi của mọi ứng dụng GUI hiện đại. Hai là Lập trình Trực quan (Visual Programming) - thiết kế giao diện bằng kéo thả các điều khiển trên Form Designer thay vì phải ngồi viết tay hàng trăm dòng code tọa độ. Ba là Lập trình Tổng quát (Generics) - viết thuật toán và cấu trúc dữ liệu dùng chung cho mọi kiểu dữ liệu như List<T> mà vẫn bảo đảm tối đa tính an toàn kiểu. Bốn là Lập trình Bất đồng bộ (Asynchronous Programming) - dùng async và await để thực thi các tác vụ tốn thời gian như gọi API, đọc tệp tin hay truy vấn cơ sở dữ liệu ở chế độ nền mà không bao giờ làm đơ hay treo giao diện ứng dụng!",
    "speaker2": "C# giống như một bộ công cụ đa năng đỉnh cao thầy ạ! Bất kể bài toán yêu cầu xây dựng giao diện kéo thả, xử lý dữ liệu tổng quát hay tối ưu phản hồi mạng đa luồng, C# đều cung cấp sẵn các cú pháp thanh lịch để giải quyết một cách mượt mà."
  },
  "25": {
    "title": "Nền Tảng Microsoft .NET: Tầm Nhìn Kiến Trúc",
    "speaker1": "Giờ chúng ta bước vào mục 1.9 của giáo trình: Nền tảng Microsoft .NET và tầm nhìn kiến trúc của nó trên slide 25. Sáng kiến .NET được Microsoft công bố nhằm xây dựng một môi trường toàn diện để phát triển, triển khai và vận hành các ứng dụng mạng phân tán. Kiến trúc của .NET tựa trên hai trụ cột khổng lồ: Trụ cột 1 là Thư viện lớp cơ sở (.NET Framework Class Library - FCL) - một kho tàng gồm hàng chục nghìn lớp đối tượng chuẩn mực đã được tối ưu hiệu năng cao, cung cấp giải pháp trọn gói từ nhập xuất tệp tin, lập trình mạng, kết nối cơ sở dữ liệu ADO.NET, đến an ninh bảo mật và đồ họa. Nhờ FCL, lập trình viên tiết kiệm được đến 70% thời gian gõ code. Trụ cột 2 là Máy ảo thực thi CLR (Common Language Runtime) - trái tim vận hành toàn bộ hệ sinh thái .NET, che giấu sự phức tạp của phần cứng và hệ điều hành bên dưới, trực tiếp quản lý toàn bộ vòng đời ứng dụng: từ nạp mã, cấp phát bộ nhớ, thu gom rác cho đến kiểm soát bảo mật.",
    "speaker2": "Em hiểu rồi ạ! FCL giống như một siêu thị linh kiện phần mềm khổng lồ có sẵn mọi thứ, còn CLR là một tổng công trình sư tận tụy quản lý và vận hành toàn bộ công trường xây dựng phần mềm một cách an toàn và trơn tru."
  },
  "26": {
    "title": "Thế Giới Code: Quản Lý vs Không Quản Lý",
    "speaker1": "Nhìn lên Slide 26, các em cần phân biệt rõ hai thế giới mã nguồn trong kỹ thuật phần mềm: Mã được quản lý (Managed Code) và Mã không được quản lý (Unmanaged Code). Managed Code là mã được biên dịch ra mã trung gian MSIL và chạy hoàn toàn dưới sự giám hộ, bảo vệ chặt chẽ của máy ảo CLR; đây chính là mã nguồn mặc định của C# và VB.NET. Lợi ích vượt trội của nó là: không bao giờ bị rò rỉ bộ nhớ, ngăn chặn triệt để lỗi tràn bộ đệm (Buffer Overflow) - lỗ hổng bảo mật số một thế giới, và xử lý ngoại lệ an toàn xuyên suốt. Ngược lại, Unmanaged Code là mã biên dịch trực tiếp ra mã máy nhị phân của CPU như trong C hay C++ truyền thống, không có máy ảo giám sát. Lập trình viên phải tự quản lý từng con trỏ bộ nhớ, nếu sơ suất giải phóng sai hoặc truy cập vùng nhớ cấm, chương trình sẽ lập tức làm sập ứng dụng hoặc gây ra màn hình xanh chết chóc (BSoD) của hệ điều hành!",
    "speaker2": "Dạ thưa thầy, sự bảo vệ của Managed Code đối với các hệ thống lớn là quá quan trọng! Thảo nào các hệ thống ngân hàng, thương mại điện tử và dịch vụ công nghệ thông tin quy mô lớn hiện nay đều chuyển dịch mạnh mẽ sang sử dụng Managed Code trên nền tảng .NET để đảm bảo tính sẵn sàng và an ninh mạng tuyệt đối."
  },
  "27": {
    "title": "Kiến Trúc Thực Thi .NET: Hành Trình Của Dòng Code",
    "speaker1": "Slide 27 mổ xẻ một sơ đồ kiến trúc kinh điển mà mọi kỹ sư .NET đều phải nắm vững: Hành trình của một dòng code C# từ lúc viết đến khi thực thi trên CPU. Hành trình này chia làm 2 giai đoạn rõ rệt: Giai đoạn 1 là Biên dịch (Compile Time) - lập trình viên viết mã nguồn file *.cs, trình biên dịch C# (csc.exe) sẽ kiểm tra cú pháp và dịch toàn bộ thành Mã trung gian Microsoft Intermediate Language (MSIL) kèm siêu dữ liệu Metadata, đóng gói vào tệp *.dll hoặc *.exe. Giai đoạn 2 là Thực thi trên máy ảo CLR (Runtime Execution) - khi người dùng kích hoạt chạy chương trình, Trình biên dịch tức thời JIT Compiler (Just-In-Time) nằm trong CLR sẽ dịch từng đoạn mã trung gian MSIL này thành Mã máy bản địa (Native Machine Code) tối ưu riêng cho con chip CPU cụ thể của chiếc máy đó để thực thi. Câu hỏi rất hay! MSIL không phụ thuộc vào bất kỳ tập lệnh CPU của Intel, AMD hay ARM nào cả. Nhờ có tầng trung gian MSIL này, tệp *.dll sau khi biên dịch có thể được sao chép sang bất kỳ máy tính chạy Windows, Linux hay macOS nào, miễn là ở đó có cài đặt máy ảo CLR là chương trình sẽ chạy mượt mà ngay lập tức!",
    "speaker2": "Thưa thầy, vai trò mang tính sống còn của mã trung gian MSIL ở đây là gì ạ?"
  },
  "28": {
    "title": "Quyền Năng Vượt Nền Tảng (Platform Independence)",
    "speaker1": "Và đó chính là Quyền năng độc lập nền tảng (Platform Independence) được thể hiện trên slide 28: Triết lý 'Write Once, Run Anywhere' - Viết một lần, chạy mọi nơi của .NET! Một giải pháp phần mềm viết bằng C# chỉ cần biên dịch duy nhất một lần ra tệp MSIL, tệp đó có thể mang sang chạy trên máy chủ đám mây Linux Ubuntu, máy tính cá nhân Windows 11 hay laptop chạy macOS chip Apple Silicon mà không cần sửa đổi hay biên dịch lại bất kỳ dòng code nào. Điều này giúp các tập đoàn công nghệ tiết kiệm hàng triệu đô la chi phí chuyển đổi (porting). Lịch sử .NET đã trải qua bước tiến dài: Giai đoạn 2002-2019 với .NET Framework chủ yếu cho Windows; bước ngoặt năm 2016 với cuộc cách mạng .NET Core mã nguồn mở, siêu tốc và đa nền tảng; và ngày nay là sự hợp nhất đỉnh cao trên .NET 8 và .NET 9 hiện đại.",
    "speaker2": "Dạ thưa thầy, sinh viên chúng em thực sự được hưởng lợi rất lớn từ cuộc cách mạng đa nền tảng này! Chúng em có thể dùng máy tính Windows, Mac hay Linux để học tập và lập trình C# một cách hoàn toàn bình đẳng và đồng bộ."
  },
  "29": {
    "title": "Tương Tác Đa Ngôn Ngữ (Language Interoperability)",
    "speaker1": "Chưa dừng lại ở đó, nền tảng .NET còn sở hữu một năng lực độc nhất vô nhị: Khả năng tương tác đa ngôn ngữ (Language Interoperability) trên Slide 29. Trong cùng một hệ sinh thái .NET, dù một lập trình viên viết bằng C#, một đồng đội khác viết bằng Visual Basic .NET, và một chuyên gia khoa học dữ liệu viết bằng F#, toàn bộ các mã nguồn đó khi biên dịch đều quy tụ về cùng một định dạng chuẩn chung duy nhất là MSIL! Nhờ đó, rào cản ngôn ngữ bị xóa bỏ hoàn toàn: Một lớp đối tượng viết bằng C# có thể kế thừa trực tiếp một lớp viết bằng Visual Basic; một phương thức C# có thể bắt lỗi ngoại lệ Exception do mã F# ném ra; và tất cả đều dùng chung một kho thư viện FCL thống nhất.",
    "speaker2": "Tính năng này thật sự phi thường thầy ạ! Trong các dự án phần mềm doanh nghiệp lớn với hàng trăm kỹ sư, mỗi người có thể phát huy tối đa sở trường ngôn ngữ của mình mà toàn bộ hệ thống vẫn tích hợp ăn khớp hoàn hảo mà không gặp bất kỳ xung đột nào."
  },
  "30": {
    "title": "[CHECKPOINT 2] & [HANDS-ON LAB 2] Kiểm tra Nhanh & Thực hành CLI",
    "speaker1": "Rất tuyệt vời! Giờ là lúc chúng ta kiểm tra nhanh kiến thức Tiết 2 qua Checkpoint và thực hành Hands-on Lab 2 trên slide 30. Thầy có 2 câu hỏi: Câu 1: Mã nguồn C# khi biên dịch lần đầu tiên sẽ tạo ra loại mã nào? Đáp án đúng là gì các em? Chính xác! Câu 2: Thành phần nào trong kiến trúc .NET chịu trách nhiệm chuyển đổi mã MSIL sang mã máy bản địa ngay khi chương trình được khởi chạy? Hoàn hảo! Bây giờ là 10 phút Hands-on Lab 2. Thầy muốn cả lớp mở Terminal gõ lệnh kiểm tra phiên bản: dotnet --version. Sau đó khởi tạo một dự án C# mới bằng dòng lệnh CLI: dotnet new console -o HelloIT26M. Chuyển vào thư mục bằng cd HelloIT26M, rồi gõ lệnh dotnet run. Hãy quan sát và cảm nhận!",
    "speaker2": "Dạ thưa thầy, Câu 1 đáp án chính là Mã trung gian Microsoft Intermediate Language (MSIL/CIL) ạ! Dạ thưa thầy, đó chính là Trình biên dịch tức thời JIT Compiler nằm trong máy ảo CLR ạ! Thưa thầy, em vừa chạy thử rồi ạ! Dòng chữ 'Hello, World!' xuất hiện ngay trên màn hình terminal chỉ sau vài giây. Lệnh dotnet run đã tự động gọi csc biên dịch sinh ra tệp HelloIT26M.dll chứa mã MSIL, rồi kích hoạt CLR chạy thử nghiệm cực kỳ mượt mà thầy ạ!"
  },
  "31": {
    "title": "TIẾT 3: VISUAL STUDIO IDE & TEST-DRIVE ỨNG DỤNG ĐỒ HỌA PAINTER (GUI & EVENT-DRIVEN)",
    "speaker1": "Hoan nghênh các em bước vào Tiết 3 - tiết học hấp dẫn và bùng nổ nhất trong buổi học hôm nay: Khám phá Môi trường phát triển tích hợp Visual Studio IDE và Test-Drive ứng dụng đồ họa Painter theo mô hình Lập trình trực quan và Hướng sự kiện! Sau khi đã làm chủ nền tảng dòng lệnh Console ở hai tiết trước, giờ là lúc chúng ta tiến vào thế giới phát triển ứng dụng giao diện đồ họa người dùng (GUI) chuyên nghiệp.",
    "speaker2": "Dạ thưa thầy, sinh viên chúng em rất chờ đợi phần này ạ! Được tự tay tương tác với các nút bấm, chọn màu sắc, rê chuột vẽ tranh như các phần mềm thương mại thực thụ trên Windows chắc chắn sẽ đem lại cảm giác lập trình vô cùng sống động và hào hứng ạ!"
  },
  "32": {
    "title": "Hệ Điều Hành Windows & Nền Tảng Cho Ứng Dụng Desktop",
    "speaker1": "Nhìn lên Slide 32, mục 1.10 của giáo trình giới thiệu về Hệ điều hành Microsoft Windows - nền tảng môi trường máy chủ và máy khách phổ biến nhất hành tinh. Để các ứng dụng đồ họa của chúng ta có thể vận hành trơn tru, Windows cung cấp các dịch vụ hạ tầng cốt lõi: Quản lý bộ nhớ ảo đa cấp, điều phối định thời CPU đa nhiệm ưu tiên (Preemptive Multitasking) giúp các ứng dụng chạy đồng thời mà không chiếm dụng độc quyền hệ thống, hệ thống tệp tin bảo mật cao NTFS, và đặc biệt là hệ thống giao diện đồ họa người dùng GUI trực quan. Lịch sử Windows đã trải qua chặng đường tiến hóa kỳ vĩ: từ Windows 1.0 năm 1985 với giao diện đồ họa thô sơ trên nền DOS, kỷ nguyên bùng nổ 32-bit với Windows 95, 98, XP, cho đến Windows 10 và Windows 11 hiện đại với điện toán 64-bit, màn hình cảm ứng, tích hợp đám mây và trợ lý AI thông minh.",
    "speaker2": "Dạ, sự hỗ trợ mạnh mẽ của Windows về đồ họa và đa nhiệm chính là bệ đỡ hoàn hảo để các ứng dụng Windows Forms và WPF của lập trình viên C# phát huy tối đa hiệu năng trên hàng tỷ máy tính toàn cầu thầy nhỉ."
  },
  "33": {
    "title": "Visual Studio - IDE Số 1 Thế Giới Cho Lập Trình Viên C#",
    "speaker1": "Để hiện thực hóa các ứng dụng C# hiện đại, công cụ quyền lực nhất mà mọi kỹ sư phần mềm chuyên nghiệp sử dụng chính là Visual Studio IDE, được mô tả trong mục 1.11 trên Slide 33. Đây là môi trường phát triển tích hợp số một thế giới, hỗ trợ trọn vẹn toàn bộ vòng đời phát triển phần mềm: Nhóm công cụ Soạn thảo & Thiết kế gồm Code Editor với tính năng tô màu cú pháp, gợi ý mã thông minh IntelliSense và tự động sửa lỗi, cùng Form Designer cho phép thiết kế giao diện đồ họa bằng kéo thả trực quan. Nhóm công cụ Quản lý & Thuộc tính gồm Solution Explorer quản lý cây thư mục mã nguồn và thư viện tham chiếu, cùng Properties Window cho phép tinh chỉnh từng thông số kích thước, màu sắc, font chữ của các điều khiển. Nhóm công cụ Biên dịch & Gỡ lỗi với Build System biên dịch 1-click hoặc qua phím tắt F5, kết hợp Debugger chuyên nghiệp cho phép đặt điểm dừng (Breakpoints), soi biến và theo dõi vùng nhớ từng mili-giây.",
    "speaker2": "Giao diện Visual Studio tích hợp sẵn mọi thứ từ A đến Z thầy ạ! Chúng em không còn phải mở từng cửa sổ rời rạc để gõ lệnh, dịch file rồi chạy thử nữa; mọi thao tác đều được tự động hóa mượt mà ngay trên một màn hình làm việc chuyên nghiệp."
  },
  "34": {
    "title": "Cấu Trúc Giải Pháp: Solution (*.sln) & Project (*.csproj)",
    "speaker1": "Trong Visual Studio, các em cần phân biệt rõ cấu trúc phân cấp giữa Solution và Project trên slide 34, được trích xuất từ Hình 1.8 của sách. Solution (tệp *.sln) là một thùng chứa cấp cao nhất (Container), có nhiệm vụ gom nhóm và liên kết một hoặc nhiều Project có liên quan với nhau trong cùng một giải pháp phần mềm tổng thể. Bên trong Solution là các Project (tệp *.csproj), mỗi Project đại diện cho một chương trình độc lập, chứa toàn bộ mã nguồn C# (*.cs), các tệp cấu hình, hình ảnh, tài nguyên giao diện để biên dịch ra một tệp *.exe thực thi hoặc *.dll thư viện. Thầy lưu ý một thao tác chuẩn mực của kỹ sư: Khi mở một dự án phần mềm trong Visual Studio, các em phải luôn luôn nhấp đúp vào tệp có đuôi .sln để IDE nạp trọn vẹn toàn bộ cấu trúc dự án và các tham chiếu liên kết!",
    "speaker2": "Dạ em ghi nhớ quy tắc vàng này rồi ạ: Luôn mở tệp .sln chứ không mở riêng lẻ từng file .cs. Điều này đảm bảo toàn bộ thư viện và cấu hình dự án được nạp đầy đủ, tránh bị báo lỗi thiếu file khi biên dịch."
  },
  "35": {
    "title": "Case Study: Ứng Dụng Đồ Họa Painter (Visual C# GUI)",
    "speaker1": "Bây giờ là trọng tâm thực hành của Tiết 3: Mục 1.12 của giáo trình - Case Study Test-Drive ứng dụng đồ họa tương tác Painter trên slide 35! Đây là một ứng dụng Windows Forms hoàn chỉnh cho phép người dùng vẽ tranh tự do bằng chuột máy tính. Ứng dụng cung cấp các tùy chọn phong phú: Chọn màu cọ vẽ (Red - Đỏ, Blue - Xanh dương, Green - Xanh lá, Black - Đen); Chọn kích thước nét cọ (Small - Nhỏ, Medium - Vừa, Large - Lớn); Một vùng vẽ màu trắng Panel để người dùng rê chuột tạo tác phẩm nghệ thuật; và các nút bấm chức năng Undo để hoàn tác và Clear để xóa trắng bảng vẽ. Bài học sư phạm cốt lõi ở đây là: Sinh viên được nhìn thấy ngay thành quả trực quan sống động của lập trình C# ngay trong buổi học đầu tiên mà không cần phải vất vả viết hàng trăm dòng code thuật toán đồ họa phức tạp từ đầu, nhờ tận dụng các điều khiển có sẵn của nền tảng .NET!",
    "speaker2": "Thật tuyệt vời thầy ạ! Nhìn vào giao diện ứng dụng Painter này, em thấy nó giống hệt như một phiên bản thu nhỏ của phần mềm Paint quen thuộc trên máy tính Windows. Chúng em rất nóng lòng muốn mổ xẻ các thành phần bên trong nó ạ!"
  },
  "36": {
    "title": "Khảo Sát Các Điều Khiển GUI Chuẩn Trong Painter",
    "speaker1": "Quan sát Hình 1.10 trên slide 36, ứng dụng Painter được xây dựng từ 4 loại điều khiển GUI chuẩn mực trong .NET: Điều khiển 1 là GroupBox - chiếc khung viền có tiêu đề dùng để gom nhóm các điều khiển có liên quan với nhau về mặt ngữ nghĩa, ví dụ nhóm Color gom các màu, nhóm Size gom các kích thước. Điều khiển 2 là RadioButton - nút chọn hình tròn mang tính chất độc quyền; trong cùng một GroupBox, người dùng chỉ có thể chọn duy nhất 1 RadioButton tại một thời điểm, khi chọn một nút mới thì nút cũ sẽ tự động bỏ chọn! Điều khiển 3 là Panel - vùng không gian màu trắng đóng vai trò bề mặt tiếp nhận thao tác vẽ và bắt tọa độ chuột. Và Điều khiển 4 là Button - nút bấm hình chữ nhật kích hoạt các hành động tức thì như Undo hay Clear.",
    "speaker2": "Dạ thưa thầy, tính năng độc quyền loại trừ lẫn nhau của RadioButton trong GroupBox rất thông minh ạ! Nhờ đó mà người dùng không bao giờ rơi vào tình huống vô lý là vừa chọn nét cọ màu đỏ lại vừa chọn màu xanh cùng một lúc."
  },
  "37": {
    "title": "Cơ Chế Lập Trình Hướng Sự Kiện (Event-Driven Mechanism)",
    "speaker1": "Slide 37 giải thích bí mật vận hành đằng sau mọi ứng dụng đồ họa: Cơ chế Lập trình Hướng sự kiện (Event-Driven Mechanism). Khác hoàn toàn với các chương trình Console chạy tuần tự từ trên xuống dưới rồi kết thúc, một ứng dụng GUI sau khi khởi chạy sẽ rơi vào một vòng lặp trạng thái gọi là Event Loop - kiên nhẫn 'lắng nghe' mọi tương tác từ người dùng. Khi người dùng click chuột vào RadioButton, sự kiện CheckedChanged được kích hoạt; khi người dùng ấn nút chuột xuống mặt bảng vẽ, sự kiện MouseDown nổ ra; khi rê chuột, sự kiện MouseMove liên tục gửi tọa độ (X, Y); và khi bấm nút Clear, sự kiện Click phát tín hiệu. Mỗi sự kiện này sẽ tự động gọi một hàm tương ứng gọi là Trình xử lý sự kiện (Event Handler) để thực thi hành vi đổi màu cọ, vẽ đường nét hay xóa trắng tranh vẽ!",
    "speaker2": "À, em đã hiểu bản chất rồi ạ! Ứng dụng hướng sự kiện giống như một người phục vụ chu đáo: đứng lắng nghe yêu cầu của thực khách, thực khách gọi món nào thì lập tức thực hiện món đó. Người dùng chính là người làm chủ thứ tự vận hành của ứng dụng thông qua các thao tác chuột và bàn phím!"
  },
  "38": {
    "title": "[HANDS-ON LAB 3] Test-Drive Ứng Dụng Painter (Phòng máy - 20 Phút)",
    "speaker1": "Bây giờ là 20 phút thực hành sôi nổi nhất của Tiết 3: Hands-on Lab 3 tại phòng máy IT26M! Thầy yêu cầu tất cả các em: Mở Visual Studio 2022, tìm đến thư mục bài tập của Chương 1 và mở tệp giải pháp Painter.sln. Khảo sát giao diện thiết kế trong Windows Forms Designer, sau đó nhấn phím F5 hoặc nút Start màu xanh trên thanh công cụ để biên dịch và chạy ứng dụng. Khi cửa sổ Painter xuất hiện, chúng ta sẽ lần lượt thực hiện 3 bước vẽ một tác phẩm nghệ thuật hoàn chỉnh theo hướng dẫn của giáo trình!",
    "speaker2": "Dạ thưa thầy, em đã nhấn F5 và ứng dụng Painter đã khởi chạy thành công trên màn hình máy em rồi ạ! Cửa sổ ứng dụng hiện lên rất sắc nét, các nút RadioButton và vùng vẽ Panel trắng tinh đã sẵn sàng để thực hiện các nét vẽ đầu tiên ạ!"
  },
  "39": {
    "title": "Các Thao Tác Vẽ Trong Painter Test-Drive",
    "speaker1": "Các em hãy nhìn vào slide 39 và làm theo đúng 3 bước minh họa từ Hình 1.11 đến Hình 1.13 trong giáo trình: Bước 1 (Hình 1.11): Trong nhóm Color nhấp chọn RadioButton Red, trong nhóm Size nhấp chọn Small. Di chuyển chuột vào vùng Panel màu trắng, nhấn giữ chuột trái và rê chuột theo đường tròn uốn lượn để vẽ nên những cánh hoa màu đỏ rực rỡ. Bước 2 (Hình 1.12): Chuyển sang chọn RadioButton Green và kích thước Large. Kéo chuột một đường thẳng dài xuống dưới để vẽ thân hoa, rồi vẽ các vệt cỏ xanh mướt dưới gốc cây. Bước 3 (Hình 1.13): Chọn RadioButton Blue và kích thước Medium, nhấp chuột chấm những giọt mưa rơi nhẹ xung quanh bông hoa để hoàn tất một bức tranh thiên nhiên tuyệt đẹp!",
    "speaker2": "Tuyệt vời quá thầy ơi! Cả phòng máy các bạn đều đang hào hứng vẽ tranh. Từng nét chuột rê đến đâu là mực đỏ, mực xanh hiện lên đến đó rất mượt mà. Nếu lỡ tay vẽ chệch một nét, chúng em bấm nút Undo là nét vẽ lập tức biến mất; còn bấm nút Clear là toàn bộ tranh được xóa sạch bong để vẽ lại từ đầu. Trải nghiệm thực hành này làm chúng em vô cùng phấn khích với lập trình C# ạ!"
  },
  "40": {
    "title": "[CHECKPOINT 3] Kiểm tra Nhanh Kiến thức Tiết 3",
    "speaker1": "Để đúc kết trọn vẹn kiến thức của Tiết 3, chúng ta cùng làm Checkpoint 3 trên slide 40. Câu hỏi 1: Trong ứng dụng Painter, loại điều khiển nào đóng vai trò làm vùng không gian nền trắng để người dùng thao tác vẽ và bắt tọa độ chuột? Các phương án: 1. GroupBox, 2. RadioButton, 3. Panel, 4. Button. Hoàn toàn chính xác! Câu hỏi 2: Phím tắt chuẩn mực và nhanh nhất trong Visual Studio để biên dịch và khởi chạy ứng dụng là gì? Xuất sắc! Các em đã nắm vững cả tư duy điều khiển giao diện lẫn kỹ năng thao tác phím tắt của một lập trình viên chuyên nghiệp.",
    "speaker2": "Dạ thưa thầy, Câu hỏi 1 em chọn chắc chắn là phương án số 3: Điều khiển Panel ạ! Vì Panel chính là bề mặt tiếp nhận các sự kiện chuột và hiển thị các nét vẽ. Dạ thưa thầy, đó là phím F5 để chạy kèm gỡ lỗi Debug, hoặc tổ hợp phím Ctrl + F5 để chạy trực tiếp không cần debug ạ!"
  },
  "41": {
    "title": "Tổng Kết Toàn Diện Chương 1: Checklist Chuẩn Đầu Ra",
    "speaker1": "Nhìn lại hành trình 150 phút của buổi học hôm nay trên slide 41, thầy nhiệt liệt chúc mừng cả tập thể lớp IT26M! Chúng ta đã cùng nhau hoàn thành xuất sắc toàn diện cả 5 Chuẩn đầu ra (CLOs) đề ra từ đầu buổi: CLO 1.1: Nắm chắc kiến trúc 6 khối logic máy tính và thang bậc phân cấp dữ liệu từ Bit đến Big Data. CLO 1.2: Phân biệt rõ Compiler vs Interpreter, làm chủ bản chất tư duy Đối tượng với Class, Object, Đóng gói, Kế thừa và Đa hình. CLO 1.3: Thấu suốt cơ chế thực thi .NET từ C# sang MSIL, CLR và JIT Compiler, cùng lợi thế bảo mật của Managed Code. CLO 1.4: Làm chủ môi trường Visual Studio IDE với Solution, Project, Form Designer và Debugger. Và CLO 1.5: Trải nghiệm thành công mô hình Lập trình trực quan và Hướng sự kiện qua bài Test-Drive ứng dụng Painter!",
    "speaker2": "Thay mặt cho toàn thể sinh viên lớp IT26M, em xin gửi lời cảm ơn chân thành đến thầy ạ! Buổi học 3 tiết trôi qua cực kỳ nhanh và cuốn hút. Nhờ sự kết hợp nhuần nhuyễn giữa lý thuyết chuyên sâu và 3 bài thực hành sinh động, chúng em không chỉ hiểu tận gốc rễ cơ chế của máy tính mà còn tự tin làm chủ công cụ và có niềm đam mê mãnh liệt với ngôn ngữ C#!"
  },
  "42": {
    "title": "Bài Tập Về Nhà - Chương 1 & Chuẩn Bị Chương 2",
    "speaker1": "Trước khi kết thúc buổi học, thầy giao nhiệm vụ tự học về nhà trên Slide 42: Thứ nhất, các em đọc kỹ lại toàn bộ nội dung Chapter 1 trong giáo trình Visual C# How to Program từ trang 41 đến trang 72. Thứ hai, tự giác hoàn thành toàn bộ các câu hỏi tự lượng giá Self-Review Exercises từ 1.1 đến 1.29 ở cuối chương trong giáo trình. Thứ ba, cài đặt hoàn chỉnh phần mềm Visual Studio 2022 bản Community trên máy tính cá nhân ở nhà với gói workload '.NET desktop development'. Về phần chuẩn bị cho buổi học tới - Chương 2: Chúng ta sẽ chính thức bắt tay vào viết những dòng code C# đầu tiên: lệnh xuất dữ liệu Console.WriteLine, cấu trúc hàm Main, quy ước đặt tên biến, lệnh nhập dữ liệu Console.ReadLine, các toán tử số học và cấu trúc rẽ nhánh if. Chúc các em học tập thật tốt và hẹn gặp lại cả lớp vào buổi học tuần sau!",
    "speaker2": "Dạ vâng thưa thầy! Chúng em sẽ đọc kỹ giáo trình, hoàn thành đầy đủ bài tập Self-Review và cài đặt sẵn sàng Visual Studio 2022 trên máy tính cá nhân để chuẩn bị thật tốt cho Chương 2 ạ. Chúng em chào thầy và chúc thầy một ngày làm việc thật nhiều năng lượng ạ!"
  }
};

function initSlidePlayer() {
  renderSlide(AppState.currentSlide);

  const prevBtn = document.getElementById('prevSlideBtn');
  const nextBtn = document.getElementById('nextSlideBtn');
  const slideSelect = document.getElementById('slideNumberSelect');

  // Populate Slide Select Dropdown
  if (slideSelect) {
    slideSelect.innerHTML = '';
    for (let i = 1; i <= AppState.totalSlides; i++) {
      const opt = document.createElement('option');
      opt.value = i;
      opt.textContent = `Slide ${i}: ${SLIDE_TRANSCRIPTS[i]?.title.substring(0, 32)}...`;
      slideSelect.appendChild(opt);
    }

    slideSelect.addEventListener('change', (e) => {
      renderSlide(parseInt(e.target.value));
    });
  }

  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      if (AppState.currentSlide > 1) {
        renderSlide(AppState.currentSlide - 1);
      }
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      if (AppState.currentSlide < AppState.totalSlides) {
        renderSlide(AppState.currentSlide + 1);
      }
    });
  }

  // Audio Playback Controller
  const audioEl = document.getElementById('slideNarrationAudio');
  const playAudioBtn = document.getElementById('slideAudioPlayBtn');
  const audioStatus = document.getElementById('audioStatusText');
  const autoAdvanceCheck = document.getElementById('autoAdvanceAudioCheck');

  if (playAudioBtn && audioEl) {
    playAudioBtn.addEventListener('click', () => {
      if (audioEl.paused) {
        startOrResumeAudio();
      } else {
        pauseAudio();
      }
    });

    audioEl.addEventListener('play', () => {
      AppState.isPlayingAudio = true;
      playAudioBtn.innerHTML = '⏸️ Tạm Dừng';
      playAudioBtn.style.background = 'var(--accent-amber)';
      if (audioStatus) audioStatus.textContent = `Đang phát Slide ${AppState.currentSlide}...`;
    });

    audioEl.addEventListener('pause', () => {
      AppState.isPlayingAudio = false;
      playAudioBtn.innerHTML = '▶️ Tiếp Tục Nghe';
      playAudioBtn.style.background = 'var(--accent-green)';
      if (audioStatus) audioStatus.textContent = `Tạm dừng Slide ${AppState.currentSlide}`;
    });

    audioEl.addEventListener('timeupdate', () => {
      if (audioStatus && audioEl.duration) {
        const cur = formatTime(audioEl.currentTime);
        const dur = formatTime(audioEl.duration);
        audioStatus.textContent = `Đang phát Slide ${AppState.currentSlide} (${cur} / ${dur})`;
      }
    });

    audioEl.addEventListener('ended', () => {
      if (autoAdvanceCheck && autoAdvanceCheck.checked && AppState.currentSlide < AppState.totalSlides) {
        renderSlide(AppState.currentSlide + 1);
        playSlideAudio(AppState.currentSlide);
      } else {
        AppState.isPlayingAudio = false;
        playAudioBtn.innerHTML = '▶️ Nghe Lại Slide';
        playAudioBtn.style.background = 'var(--accent-green)';
        if (audioStatus) audioStatus.textContent = `Đã kết thúc Slide ${AppState.currentSlide}`;
      }
    });

    audioEl.addEventListener('error', () => {
      if (audioStatus) audioStatus.textContent = `Không có audio cho Slide ${AppState.currentSlide}`;
      AppState.isPlayingAudio = false;
      playAudioBtn.innerHTML = '▶️ Nghe Thuyết Minh';
      playAudioBtn.style.background = 'var(--accent-green)';
    });
  }

  // Keyboard navigation for slides
  document.addEventListener('keydown', (e) => {
    if (AppState.currentTab === 'video') {
      if (e.key === 'ArrowLeft' && AppState.currentSlide > 1) {
        renderSlide(AppState.currentSlide - 1);
      } else if (e.key === 'ArrowRight' && AppState.currentSlide < AppState.totalSlides) {
        renderSlide(AppState.currentSlide + 1);
      }
    }
  });
}

function formatTime(seconds) {
  if (isNaN(seconds)) return '00:00';
  const m = Math.floor(seconds / 60);
  const s = Math.floor(seconds % 60);
  return `${m < 10 ? '0' : ''}${m}:${s < 10 ? '0' : ''}${s}`;
}

function startOrResumeAudio() {
  const audioEl = document.getElementById('slideNarrationAudio');
  if (!audioEl) return;
  const targetSrc = `./VideoCShape/Chapter_01/audio/slide_${AppState.currentSlide}.mp3`;
  if (!audioEl.src.endsWith(`slide_${AppState.currentSlide}.mp3`)) {
    audioEl.src = targetSrc;
  }
  audioEl.play().catch(err => {
    console.warn("Audio autoplay blocked or failed:", err);
  });
}

function pauseAudio() {
  const audioEl = document.getElementById('slideNarrationAudio');
  if (audioEl) audioEl.pause();
}

function playSlideAudio(slideNum) {
  const audioEl = document.getElementById('slideNarrationAudio');
  if (!audioEl) return;
  audioEl.src = `./VideoCShape/Chapter_01/audio/slide_${slideNum}.mp3`;
  audioEl.play().catch(err => console.warn(err));
}

function renderSlide(slideNum) {
  AppState.currentSlide = slideNum;
  
  // Update Buttons & Counter
  const prevBtn = document.getElementById('prevSlideBtn');
  const nextBtn = document.getElementById('nextSlideBtn');
  const counter = document.getElementById('slideCounterText');
  const slideSelect = document.getElementById('slideNumberSelect');

  if (prevBtn) prevBtn.disabled = (slideNum === 1);
  if (nextBtn) nextBtn.disabled = (slideNum === AppState.totalSlides);
  if (counter) counter.textContent = `Slide ${slideNum} / ${AppState.totalSlides}`;
  if (slideSelect) slideSelect.value = slideNum;

  // Render Slide Display (trực tiếp hiển thị từng trang trích xuất từ Slide_Chapter_01.pdf)
  const slideDisplay = document.getElementById('slideDisplayFrame');
  const transcriptData = SLIDE_TRANSCRIPTS[slideNum] || {
    title: `Slide ${slideNum}`,
    speaker1: "Nội dung thuyết minh giảng viên.",
    speaker2: "Phản hồi của sinh viên."
  };

  if (slideDisplay) {
    const visualHtml = `
      <div style="position: relative; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; background: #000;">
        <img src="./VideoCShape/Chapter_01/images/slide-${slideNum}.png" 
             alt="Slide ${slideNum}: ${transcriptData.title}" 
             class="slide-image" 
             style="max-width: 100%; max-height: 100%; object-fit: contain; box-shadow: 0 4px 12px rgba(0,0,0,0.5);"
             onerror="this.onerror=null; this.parentElement.innerHTML='<div style=\\\'color:#fff;padding:2rem;text-align:center;\\\'>Không thể tải slide. <a href=\\\'./VideoCShape/Chapter_01/Slide_Chapter_01.pdf\\\' target=\\\'_blank\\\' style=\\\'color:#38bdf8;\\\'>Bấm vào đây để mở Slide_Chapter_01.pdf</a></div>';">
        <div style="position: absolute; bottom: 8px; right: 12px; background: rgba(0, 0, 0, 0.75); padding: 3px 10px; border-radius: 4px; font-size: 0.75rem; color: #38bdf8; font-weight: 600; pointer-events: none;">
          Slide_Chapter_01.pdf (Trang ${slideNum}/42)
        </div>
      </div>
    `;
    slideDisplay.innerHTML = visualHtml;
  }

  // Handle Audio transition if playing
  const audioEl = document.getElementById('slideNarrationAudio');
  const playAudioBtn = document.getElementById('slideAudioPlayBtn');
  const audioStatus = document.getElementById('audioStatusText');
  if (audioEl) {
    if (AppState.isPlayingAudio) {
      playSlideAudio(slideNum);
    } else {
      audioEl.src = `./VideoCShape/Chapter_01/audio/slide_${slideNum}.mp3`;
      if (playAudioBtn) {
        playAudioBtn.innerHTML = '▶️ Nghe Thuyết Minh';
        playAudioBtn.style.background = 'var(--accent-green)';
      }
      if (audioStatus) {
        audioStatus.textContent = `Sẵn sàng phát Slide ${slideNum}`;
      }
    }
  }

  // Render Transcript Dialogue
  const transcriptBody = document.getElementById('transcriptDialogueBody');
  if (transcriptBody) {
    transcriptBody.innerHTML = `
      <div class="dialogue-item dialogue-speaker-1">
        <span class="speaker-label">👨‍🏫 Người 1 (Giảng viên)</span>
        <p>${transcriptData.speaker1}</p>
      </div>
      <div class="dialogue-item dialogue-speaker-2">
        <span class="speaker-label">🧑‍🎓 Người 2 (Sinh viên IT26M)</span>
        <p>${transcriptData.speaker2}</p>
      </div>
    `;
  }
}

// ============================================================================
// THEATER VIEW & TRANSCRIPT CONTROLLER
// ============================================================================
function setVideoViewMode(mode) {
  const theaterContainer = document.getElementById('theaterPlayerContainer');
  const splitContainer = document.getElementById('splitPlayerContainer');
  const theaterBtn = document.getElementById('viewModeTheaterBtn');
  const splitBtn = document.getElementById('viewModeSplitBtn');

  if (mode === 'theater') {
    if (theaterContainer) theaterContainer.style.display = 'block';
    if (splitContainer) splitContainer.style.display = 'none';
    if (theaterBtn) theaterBtn.classList.add('active');
    if (splitBtn) splitBtn.classList.remove('active');
  } else {
    if (theaterContainer) theaterContainer.style.display = 'none';
    if (splitContainer) splitContainer.style.display = 'grid';
    if (theaterBtn) theaterBtn.classList.remove('active');
    if (splitBtn) splitBtn.classList.add('active');
  }
}
window.setVideoViewMode = setVideoViewMode;

function initTheaterTranscript() {
  const selectEl = document.getElementById('theaterTranscriptSlideSelect');
  if (!selectEl) return;

  selectEl.innerHTML = '';
  for (let i = 1; i <= AppState.totalSlides; i++) {
    const opt = document.createElement('option');
    opt.value = i;
    opt.textContent = `Slide ${i}: ${SLIDE_TRANSCRIPTS[i]?.title.substring(0, 36)}...`;
    selectEl.appendChild(opt);
  }

  selectEl.addEventListener('change', (e) => {
    renderTheaterTranscript(parseInt(e.target.value));
  });

  renderTheaterTranscript(1);
}

function renderTheaterTranscript(slideNum) {
  const bodyEl = document.getElementById('theaterTranscriptBody');
  if (!bodyEl) return;

  const data = SLIDE_TRANSCRIPTS[slideNum] || {
    title: `Slide ${slideNum}`,
    speaker1: "Nội dung thuyết minh giảng viên.",
    speaker2: "Phản hồi của sinh viên."
  };

  bodyEl.innerHTML = `
    <div style="margin-bottom: 1rem; padding: 0.75rem 1rem; background: var(--primary-light); border-radius: 6px; font-weight: 700; color: var(--primary-navy); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem;">
      <span>📌 Lời thoại Slide ${slideNum}: ${data.title}</span>
      <span style="font-size: 0.8rem; font-weight: 400; color: var(--text-muted);">Trích xuất từ VideoCShape/Chapter_01/script.txt</span>
    </div>
    <div class="transcript-dialogue-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1rem;">
      <div class="dialogue-item dialogue-speaker-1" style="height: 100%;">
        <span class="speaker-label">👨‍🏫 Người 1 (Giảng viên)</span>
        <p style="margin-top: 0.5rem; line-height: 1.6;">${data.speaker1}</p>
      </div>
      <div class="dialogue-item dialogue-speaker-2" style="height: 100%;">
        <span class="speaker-label">🧑‍🎓 Người 2 (Sinh viên IT26M)</span>
        <p style="margin-top: 0.5rem; line-height: 1.6;">${data.speaker2}</p>
      </div>
    </div>
  `;
}

// ============================================================================
// QUIZ ENGINE (40 CÂU HỎI TRẮC NGHIỆM CHUẨN HÓA)
// ============================================================================
function initQuizEngine() {
  renderQuizDashboard();
  renderQuestionPalette();
  renderCurrentQuestion();

  // Navigation Buttons
  const prevBtn = document.getElementById('prevQuestionBtn');
  const nextBtn = document.getElementById('nextQuestionBtn');
  const resetBtn = document.getElementById('resetQuizBtn');

  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      if (AppState.currentQuestionIndex > 0) {
        AppState.currentQuestionIndex--;
        renderCurrentQuestion();
        renderQuestionPalette();
      }
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      if (AppState.currentQuestionIndex < QUIZ_CHAPTER_01.length - 1) {
        AppState.currentQuestionIndex++;
        renderCurrentQuestion();
        renderQuestionPalette();
      }
    });
  }

  if (resetBtn) {
    resetBtn.addEventListener('click', () => {
      if (confirm('Bạn có chắc chắn muốn làm lại từ đầu toàn bộ 40 câu hỏi trắc nghiệm?')) {
        AppState.userAnswers = {};
        AppState.currentQuestionIndex = 0;
        renderQuizDashboard();
        renderQuestionPalette();
        renderCurrentQuestion();
      }
    });
  }

  // Filter Buttons
  const filterBtns = document.querySelectorAll('.quiz-filter-btn');
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      AppState.quizFilter = btn.getAttribute('data-filter');
      renderQuestionPalette();
    });
  });
}

function renderQuizDashboard() {
  const total = QUIZ_CHAPTER_01.length;
  let correctCount = 0;
  let answeredCount = 0;

  QUIZ_CHAPTER_01.forEach(q => {
    if (AppState.userAnswers.hasOwnProperty(q.id)) {
      answeredCount++;
      if (AppState.userAnswers[q.id] === q.correct) {
        correctCount++;
      }
    }
  });

  const progressPct = Math.round((answeredCount / total) * 100);
  const scorePct = answeredCount > 0 ? Math.round((correctCount / total) * 100) : 0;

  // DOM Elements
  const statProgress = document.getElementById('quizStatProgress');
  const statScore = document.getElementById('quizStatScore');
  const statAccuracy = document.getElementById('quizStatAccuracy');
  const progressBar = document.getElementById('quizProgressBar');

  if (statProgress) statProgress.textContent = `${answeredCount} / ${total}`;
  if (statScore) statScore.textContent = `${correctCount} câu đúng`;
  if (statAccuracy) statAccuracy.textContent = `${scorePct}% (${(correctCount * 10 / total).toFixed(1)} / 10)`;
  if (progressBar) progressBar.style.width = `${progressPct}%`;
}

function renderQuestionPalette() {
  const palette = document.getElementById('quizQuestionPalette');
  if (!palette) return;

  palette.innerHTML = '';
  QUIZ_CHAPTER_01.forEach((q, idx) => {
    const isAnswered = AppState.userAnswers.hasOwnProperty(q.id);
    const isCorrect = isAnswered && (AppState.userAnswers[q.id] === q.correct);
    const isIncorrect = isAnswered && !isCorrect;

    // Filter logic
    if (AppState.quizFilter === 'correct' && !isCorrect) return;
    if (AppState.quizFilter === 'incorrect' && !isIncorrect) return;
    if (AppState.quizFilter === 'unanswered' && isAnswered) return;

    const btn = document.createElement('button');
    btn.className = 'palette-btn';
    btn.textContent = q.id;

    if (idx === AppState.currentQuestionIndex) btn.classList.add('current');
    if (isCorrect) btn.classList.add('correct');
    if (isIncorrect) btn.classList.add('incorrect');

    btn.addEventListener('click', () => {
      AppState.currentQuestionIndex = idx;
      renderCurrentQuestion();
      renderQuestionPalette();
    });

    palette.appendChild(btn);
  });
}

function renderCurrentQuestion() {
  const q = QUIZ_CHAPTER_01[AppState.currentQuestionIndex];
  if (!q) return;

  const card = document.getElementById('quizQuestionCard');
  if (!card) return;

  const isAnswered = AppState.userAnswers.hasOwnProperty(q.id);
  const selectedIndex = isAnswered ? AppState.userAnswers[q.id] : null;

  // Prev / Next button states
  const prevBtn = document.getElementById('prevQuestionBtn');
  const nextBtn = document.getElementById('nextQuestionBtn');
  if (prevBtn) prevBtn.disabled = (AppState.currentQuestionIndex === 0);
  if (nextBtn) nextBtn.disabled = (AppState.currentQuestionIndex === QUIZ_CHAPTER_01.length - 1);

  // Question HTML
  const letters = ['A', 'B', 'C', 'D'];
  const optionsHtml = q.options.map((optText, optIdx) => {
    let btnClass = 'option-btn';
    if (isAnswered) {
      if (optIdx === q.correct) {
        btnClass += ' selected-correct';
      } else if (optIdx === selectedIndex) {
        btnClass += ' selected-incorrect';
      }
    }

    return `
      <button class="${btnClass}" ${isAnswered ? 'disabled' : ''} onclick="handleSelectOption(${q.id}, ${optIdx})">
        <span class="option-letter">${letters[optIdx]}</span>
        <span class="option-text">${optText}</span>
      </button>
    `;
  }).join('');

  card.innerHTML = `
    <div class="question-meta-tags">
      <span class="tag-badge tag-category">${q.category}</span>
      <span class="tag-badge tag-bloom">Bloom: ${q.bloom}</span>
      <span class="tag-badge" style="background: var(--bg-subtle);">Câu ${q.id} / ${QUIZ_CHAPTER_01.length}</span>
    </div>
    <h4 class="question-text">${q.question.replace(/\n/g, '<br>')}</h4>
    <div class="options-container">
      ${optionsHtml}
    </div>
    <div class="explanation-card ${isAnswered ? 'show' : ''}">
      <h5>💡 Giải thích chi tiết từ Giảng viên:</h5>
      <p>${q.explanation}</p>
    </div>
  `;
}

window.handleSelectOption = function(questionId, optionIndex) {
  AppState.userAnswers[questionId] = optionIndex;
  renderQuizDashboard();
  renderQuestionPalette();
  renderCurrentQuestion();
};

// ============================================================================
// EXERCISES HUB (BÀI TẬP CUỐI CHƯƠNG)
// ============================================================================
function initExerciseHub() {
  renderExerciseList();

  const filterBtns = document.querySelectorAll('.ex-filter-btn');
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      AppState.exerciseFilter = btn.getAttribute('data-filter');
      renderExerciseList();
    });
  });

  const searchInput = document.getElementById('exerciseSearchInput');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      renderExerciseList(e.target.value.toLowerCase().trim());
    });
  }
}

function renderExerciseList(searchKeyword = '') {
  const container = document.getElementById('exerciseListContainer');
  if (!container) return;

  const filtered = EXERCISES_CHAPTER_01.filter(item => {
    const matchFilter = (AppState.exerciseFilter === 'all') || (item.type === AppState.exerciseFilter);
    const matchSearch = !searchKeyword || 
      item.title.toLowerCase().includes(searchKeyword) ||
      item.number.toLowerCase().includes(searchKeyword) ||
      item.description.toLowerCase().includes(searchKeyword);
    return matchFilter && matchSearch;
  });

  if (filtered.length === 0) {
    container.innerHTML = `
      <div style="text-align: center; padding: 3rem; color: var(--text-muted); background: var(--bg-surface); border-radius: var(--radius-lg); border: 1px dashed var(--border-color);">
        <p style="font-size: 1.1rem; font-weight: 600;">Không tìm thấy bài tập nào phù hợp với bộ lọc!</p>
      </div>
    `;
    return;
  }

  container.innerHTML = filtered.map(item => {
    let badgeClass = 'ex-badge-self-check';
    let badgeLabel = 'Self-Review';
    if (item.type === 'exercises') {
      badgeClass = 'ex-badge-exercise';
      badgeLabel = 'Exercise';
    } else if (item.type === 'making-a-difference') {
      badgeClass = 'ex-badge-project';
      badgeLabel = 'Making a Difference';
    }

    const hasStarter = Boolean(item.starterCode);
    const hasExpected = Boolean(item.expectedOutput);
    const solutionOrAnswer = item.solutionCode || item.answer;

    return `
      <div class="exercise-card">
        <div class="exercise-card-header">
          <div class="exercise-title-group">
            <div style="display: flex; gap: 0.5rem; align-items: center; margin-bottom: 0.35rem;">
              <span class="ex-badge ${badgeClass}">${badgeLabel}</span>
              <span style="font-size: 0.8rem; font-weight: 700; color: var(--text-muted);">${item.number} (Trang ${item.page})</span>
              <span style="font-size: 0.8rem; color: var(--text-muted);">• ${item.category}</span>
            </div>
            <h4>${item.title}</h4>
          </div>
        </div>
        
        <p class="exercise-desc">${item.description.replace(/\n/g, '<br>')}</p>
        ${item.image ? `<div style="text-align: center; margin: 0.75rem 0;"><img src="${item.image}" alt="${item.title}" style="max-width: 100%; max-height: 380px; object-fit: contain; border-radius: 8px; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);"><div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 4px;">Hình minh họa giáo trình Deitel & Deitel</div></div>` : ''}
        
        ${item.hint ? `<div style="font-size: 0.85rem; color: var(--primary-cyan); background: var(--primary-light); padding: 0.6rem 0.85rem; border-radius: var(--radius-sm); margin-bottom: 0.75rem;"><strong>💡 Gợi ý:</strong> ${item.hint}</div>` : ''}

        ${hasExpected ? `
          <div style="margin-top: 0.5rem;">
            <span style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; color: var(--text-muted);">Kết quả xuất mong đợi (Console Output):</span>
            <div class="expected-output-box">${escapeHtml(item.expectedOutput)}</div>
          </div>
        ` : ''}

        ${hasStarter ? `
          <div style="margin-top: 0.5rem;">
            <span style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; color: var(--text-muted);">Khung mã nguồn khởi tạo (Starter Code):</span>
            <div class="code-container">
              <button class="btn-copy-code" onclick="copyCode(this, \`${escapeJsString(item.starterCode)}\`)">📋 Copy Code</button>
              <pre class="code-block"><code>${escapeHtml(item.starterCode)}</code></pre>
            </div>
          </div>
        ` : ''}

        <div>
          <button class="solution-toggle-btn" onclick="toggleSolution('${item.id}')">
            <span>🔑 Xem lời giải & phân tích chi tiết</span>
          </button>
          <div id="solution-${item.id}" class="solution-content">
            <div class="code-container">
              <button class="btn-copy-code" onclick="copyCode(this, \`${escapeJsString(solutionOrAnswer)}\`)">📋 Copy Lời giải</button>
              <pre class="code-block" style="border-left: 4px solid var(--accent-green); background: #0f172a;"><code>${escapeHtml(solutionOrAnswer)}</code></pre>
            </div>
          </div>
        </div>
      </div>
    `;
  }).join('');
}

window.toggleSolution = function(id) {
  const el = document.getElementById(`solution-${id}`);
  if (el) el.classList.toggle('open');
};

window.copyCode = function(btn, text) {
  navigator.clipboard.writeText(text).then(() => {
    const originalText = btn.innerHTML;
    btn.innerHTML = '✅ Đã sao chép!';
    btn.style.background = '#10B981';
    setTimeout(() => {
      btn.innerHTML = originalText;
      btn.style.background = '';
    }, 2000);
  });
};

function escapeHtml(str) {
  if (!str) return '';
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

function escapeJsString(str) {
  if (!str) return '';
  return str.replace(/\\/g, '\\\\').replace(/`/g, '\\`').replace(/\$/g, '\\$');
}

// ============================================================================
// CODE REPOSITORY MODAL / INLINE VIEWER
// ============================================================================
function initCodeRepository() {
  // Can be expanded to view any of the Chapter 1 code files
}

