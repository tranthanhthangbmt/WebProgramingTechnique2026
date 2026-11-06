// ============================================================================
// HỌC PHẦN: KỸ THUẬT LẬP TRÌNH (4 TÍN CHỈ) - IT26M
// APPLICATION LOGIC (PORTAL CONTROLLER, QUIZ ENGINE, EXERCISE HUB, SLIDE PLAYER)
// ============================================================================

// State Management
const AppState = {
  currentTab: 'overview',
  currentSlide: 1,
  totalSlides: 41,
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
  1: {
    title: "KỸ THUẬT LẬP TRÌNH / JAVA - CHƯƠNG 1",
    speaker1: "Chào các em sinh viên lớp IT26M. Hôm nay chúng ta chính thức bắt đầu môn học Kỹ thuật Lập trình với Chương 1: Giới thiệu về Lập trình Java - Introduction to Java Programming. Đây là môn học nền tảng đặc biệt quan trọng, giúp các em chuyển đổi tư duy từ người sử dụng máy tính thành người làm chủ công nghệ.",
    speaker2: "Dạ chào thầy! Chúng em đã nghe nói rất nhiều về sự phổ biến và sức mạnh của ngôn ngữ Java trong các hệ thống doanh nghiệp lớn, ứng dụng Android và ngân hàng. Chúng em rất háo hức muốn biết hành trình lập trình Java sẽ bắt đầu từ đâu ạ."
  },
  2: {
    title: "Mục tiêu học tập bài học (Course Learning Outcomes – CLOs)",
    speaker1: "Chúng ta cùng nhìn vào 5 chuẩn đầu ra (CLOs) của buổi học hôm nay: Hiểu bản chất kiến trúc tính toán, JVM và Bytecode (CLO 1.1); Viết thành thạo khung chương trình, print/println, ký tự thoát (CLO 1.2); Phân loại 3 nhóm lỗi và biết cách gỡ lỗi (CLO 1.3); Nắm vững tư duy Phân rã thủ tục và DRY (CLO 1.4); và độc lập xây dựng chương trình hoàn chỉnh (CLO 1.5).",
    speaker2: "Dạ thưa thầy, các mục tiêu này được thiết kế theo thang đo Bloom từ hiểu, áp dụng đến phân tích và sáng tạo rất rõ ràng. Nó giúp chúng em vừa nắm vững lý thuyết nền tảng, vừa có kỹ năng code thực chiến ngay tại lớp."
  },
  3: {
    title: "Lộ trình buổi học 3 tiết (Tích hợp Lý thuyết & Thực hành)",
    speaker1: "Buổi học kéo dài 3 tiết (150 phút), theo mô hình đào tạo kỹ thuật hiện đại: Lý thuyết tương tác đi liền với Thực hành tại chỗ. Tiết 1: Nền tảng hệ thống, kiến trúc Java và viết chương trình đầu tiên. Tiết 2: Cú pháp chuỗi, ký tự thoát, quy ước đặt tên và nghệ thuật chẩn đoán lỗi. Tiết 3: Tư duy kiến trúc, phân rã thủ tục qua Case Study DrawFigures.",
    speaker2: "Thật tuyệt vời ạ! Việc được thực hành trực tiếp trên máy tính ngay sau mỗi phần lý thuyết sẽ giúp sinh viên chúng em hiểu sâu bản chất và không bị bỡ ngỡ khi làm bài tập."
  },
  4: {
    title: "TIẾT 1: NỀN TẢNG HỆ THỐNG TÍNH TOÁN, KIẾN TRÚC MÁY ẢO JVM & CHƯƠNG TRÌNH ĐẦU TIÊN",
    speaker1: "Chúng ta cùng bước vào Tiết 1: Nền tảng hệ thống tính toán, kiến trúc máy ảo JVM và xây dựng chương trình Java đầu tiên.",
    speaker2: "Chúng em đã sẵn sàng rồi thưa thầy!"
  },
  5: {
    title: "1.1 Tại sao chúng ta cần học lập trình? (Why Programming?)",
    speaker1: "Giáo sư Donald Knuth - người đoạt giải Turing - có câu nói bất hủ: 'Người ta thường nói rằng một người không thực sự hiểu điều gì đó cho đến khi dạy nó cho người khác. Nhưng trên thực tế, một người chỉ thực sự hiểu thấu đáo một vấn đề khi dạy nó cho máy tính, tức là diễn đạt nó dưới dạng một thuật toán'. Máy tính là một thiết bị vạn năng, và lập trình chính là ngôn ngữ để chúng ta truyền dạy tư duy của mình cho cỗ máy đó.",
    speaker2: "Lời dạy của Giáo sư Knuth sâu sắc quá thầy ạ. Để điều khiển được máy tính, ta cần nắm rõ phần cứng gồm CPU thực thi phép tính, RAM lưu tạm tốc độ cao, ổ cứng SSD lưu vĩnh viễn và các thiết bị I/O."
  },
  6: {
    title: "Thế giới số & Biểu diễn dữ liệu bằng Hệ nhị phân (Binary)",
    speaker1: "Tại sao máy tính hiện đại lại chỉ sử dụng số nhị phân 0 và 1 mà không dùng hệ thập phân? Vì phần cứng máy tính cấu tạo từ hàng tỷ bóng bán dẫn transistor, việc duy trì hai trạng thái vật lý bật (điện áp cao - bit 1) và tắt (điện áp thấp - bit 0) là bền vững và chống nhiễu tin cậy nhất. 8 bit ghép lại thành 1 Byte biểu diễn được 256 giá trị từ 0 đến 255.",
    speaker2: "Dạ em thấy ví dụ trên slide rất rõ: (1011)₂ trong hệ cơ số 2 bằng 1x8 + 0x4 + 1x2 + 1x1 = 11 trong hệ thập phân. Mọi văn bản, hình ảnh, mã Java cuối cùng đều quy về các chuỗi bit 0 và 1 này!"
  },
  7: {
    title: "Cơ chế thực thi: Trình biên dịch (Compiler) vs. Thông dịch (Interpreter)",
    speaker1: "Ngôn ngữ C/C++ dùng Compiler dịch toàn bộ mã sang Mã máy trực tiếp (Native Code), chạy cực nhanh nhưng bị phụ thuộc nền tảng (file .exe trên Windows không chạy được trên macOS hay Linux). Còn Python dùng Interpreter đọc chạy từng dòng, linh hoạt nhưng tốc độ chậm. Java đã giải quyết bài toán này bằng một bước đột phá!",
    speaker2: "Dạ đó là triết lý 'Write Once, Run Anywhere' (Viết một lần, chạy mọi nơi) nổi tiếng của Java phải không thầy?"
  },
  8: {
    title: "Kiến trúc đột phá của Java: Máy ảo JVM & Mã Bytecode",
    speaker1: "Chính xác! Trình biên dịch javac không dịch ra mã máy thật của CPU, mà dịch file .java thành Java Bytecode chứa trong file .class. Bytecode là tập lệnh của máy ảo Java Virtual Machine (JVM). Mỗi hệ điều hành (Windows, Linux, macOS) chỉ cần cài đặt một bản JVM tương ứng để thực thi file .class đó.",
    speaker2: "À, em hiểu rồi! Nhờ JVM mà code Java độc lập hoàn toàn với phần cứng. Và để lập trình, chúng em bắt buộc phải cài đặt bộ công cụ JDK (gồm JRE, JVM và compiler javac)."
  },
  9: {
    title: "Quy trình phát triển chương trình Java: Edit -> Compile -> Run",
    speaker1: "Hình 1.1 giáo trình minh họa chu trình 3 bước kinh điển: Bước 1 - Soạn thảo mã nguồn Hello.java; Bước 2 - Biên dịch bằng lệnh 'javac Hello.java', nếu đúng cú pháp sẽ sinh ra file bytecode Hello.class; Bước 3 - Thực thi bằng lệnh 'java Hello' để JVM nạp bytecode và xuất kết quả ra màn hình.",
    speaker2: "Sơ đồ trực quan quá thầy ạ. Dòng chảy từ Hello.java qua javac ra Hello.class, rồi JVM nạp vào máy tính xuất ra dòng chữ 'Hello, world!'."
  },
  10: {
    title: "1.2 Chương trình Java hoàn chỉnh đầu tiên (Hello.java)",
    speaker1: "Trong Java có quy tắc vàng: Mọi mã lệnh đều phải nằm bên trong một lớp (class). Và nếu lớp khai báo là 'public class Hello' thì bắt buộc tên file lưu trên đĩa phải là 'Hello.java', khớp 100% từng chữ hoa chữ thường. Cặp ngoặc nhọn { } dùng để đóng gói phạm vi khối lệnh.",
    speaker2: "Dạ thưa thầy, nếu em vô tình lưu file là hello.java viết thường thì javac sẽ báo lỗi ngay vì Java phân biệt hoa thường cực kỳ nghiêm ngặt!"
  },
  11: {
    title: "Mổ xẻ phương thức main – Điểm bắt đầu của mọi ứng dụng",
    speaker1: "Dòng lệnh 'public static void main(String[] args)' là trái tim của ứng dụng: public cho phép JVM gọi từ bên ngoài; static là phương thức cấp lớp không cần tạo đối tượng; void báo phương thức không trả về giá trị; main là tên chuẩn JVM tìm kiếm; và String[] args là mảng tham số nhận dữ liệu dòng lệnh.",
    speaker2: "Bảng giải thích này rất rõ ràng, từng từ khóa đều có sứ mệnh riêng và cấu thành một quy ước chặt chẽ."
  },
  12: {
    title: "Lệnh xuất dữ liệu: println vs. print",
    speaker1: "Lệnh System.out.println in nội dung và tự động đẩy con trỏ xuống dòng mới (newline). Lệnh System.out.print in nội dung nhưng giữ nguyên con trỏ ở cuối dòng để lệnh in tiếp theo nối đuôi vào. Mọi câu lệnh trong Java bắt buộc kết thúc bằng dấu chấm phẩy ;.",
    speaker2: "Em thấy ví dụ rất rõ: Ba lệnh print 'Xin ', 'chao ', và println 'IT26M!' nối thành 1 dòng duy nhất 'Xin chao IT26M!'. Còn System.out.println(); không tham số sẽ tạo ra 1 dòng trống."
  },
  13: {
    title: "[CHECKPOINT 1] Kiểm tra nhanh lý thuyết Tiết 1",
    speaker1: "Câu 1: Lệnh in nào hợp lệ trong Java? Câu 2: Vai trò của file có đuôi .class là gì?",
    speaker2: "Dạ Câu 1 em chọn C vì System viết hoa chữ S, out và println viết thường. Câu 2 là B: File .class chứa Bytecode độc lập nền tảng để JVM nạp chạy trên mọi máy tính ạ!"
  },
  14: {
    title: "[HANDS-ON LAB 1] Thực hành tại chỗ: Viết, biên dịch & chạy Java",
    speaker1: "15 phút thực hành: Mở Terminal gõ 'javac -version', tạo file WelcomeIT26M.java, biên dịch bằng 'javac WelcomeIT26M.java', quan sát file .class xuất hiện và chạy bằng 'java WelcomeIT26M'.",
    speaker2: "Em chạy thành công rồi thầy ơi! Dòng chữ 'Chao mung lop IT26M den voi Java!' và khẩu hiệu WORA đã xuất hiện mượt mà trên terminal!"
  },
  15: {
    title: "TIẾT 2: CHUỖI KÝ TỰ, KÝ TỰ THOÁT & KỸ NĂNG DEBUGGING",
    speaker1: "Chúng ta bước sang Tiết 2: Khám phá chuỗi ký tự, các ký tự thoát đặc biệt và rèn luyện kỹ năng quan trọng bậc nhất: Kỹ năng chẩn đoán và gỡ lỗi (Debugging).",
    speaker2: "Em rất mong chờ tiết này vì khi mới học lập trình, em rất sợ gặp lỗi đỏ lòm trên màn hình ạ."
  },
  16: {
    title: "Chuỗi ký tự (String Literals) & Thách thức khi xuất ký tự đặc biệt",
    speaker1: "Chuỗi ký tự là dãy chữ nằm trong cặp ngoặc kép. Nhưng nếu ta muốn in chính dấu ngoặc kép: Giáo viên nói: \"Java rất thú vị!\", trình biên dịch sẽ hiểu lầm ngoặc kép đó là dấu đóng chuỗi và báo lỗi cú pháp ngay.",
    speaker2: "Vậy giải pháp là chúng ta sử dụng Ký tự thoát (Escape Sequences) bắt đầu bằng dấu gạch chéo ngược backslash đúng không thầy?"
  },
  17: {
    title: "Bảng ký tự thoát chuẩn trong Java (Escape Sequences)",
    speaker1: "Bảng quy tắc gồm: \\t (tab căn cột), \\n (xuống dòng mới), \\\" (in dấu ngoặc kép), và \\\\ (in một dấu gạch chéo ngược). Dấu gạch chéo ngược sẽ tước bỏ ý nghĩa cú pháp của ký tự đi liền sau nó.",
    speaker2: "Quy luật rất dễ nhớ ạ! Cứ muốn in 1 dấu gạch chéo ngược thì ta gõ hai dấu liên tiếp: \\\\."
  },
  18: {
    title: "Định danh (Identifiers) & Từ khóa chuẩn Java",
    speaker1: "Định danh là tên do lập trình viên đặt. 3 quy tắc sống còn: Chỉ gồm chữ cái, chữ số, _, $; KHÔNG được bắt đầu bằng chữ số (diem1 hợp lệ, 1diem là lỗi); và KHÔNG trùng với 50+ từ khóa Java (public, class, static, void, if, for...).",
    speaker2: "Và Java phân biệt hoa thường nên biến TotalScore và totalScore là hai biến hoàn toàn khác nhau thưa thầy."
  },
  19: {
    title: "Phong cách lập trình chuẩn đại học: Quy ước CamelCase & Comments",
    speaker1: "Quy ước CamelCase chuẩn quốc tế: Tên Lớp viết UpperCamelCase (Hello, StudentManager); Tên Phương thức và Biến viết lowerCamelCase (drawDiamond, totalScore). Chú thích gồm: // cho 1 dòng; /* */ cho nhiều dòng; và /** */ cho tài liệu Javadoc.",
    speaker2: "Em nhớ lời thầy dặn: 'Code viết ra cho con người đọc hiểu trước, máy tính hiểu sau'. Thụt lề nhất quán 4 khoảng trắng giúp mã nguồn cực kỳ chuyên nghiệp."
  },
  20: {
    title: "1.3 Phân loại lỗi lập trình: 3 nhóm lỗi kinh điển",
    speaker1: "Lỗi trong lập trình gồm 3 nhóm: 1. Lỗi cú pháp (Syntax Errors) phát hiện lúc biên dịch; 2. Lỗi thực thi (Runtime Errors / Exceptions) làm chương trình sập khi đang chạy; 3. Lỗi ngữ nghĩa / logic (Logic Errors) - chương trình chạy không sập nhưng kết quả sai lệch so với yêu cầu.",
    speaker2: "Lỗi logic là nguy hiểm nhất vì máy tính không thể tự phát hiện, chỉ có lập trình viên kiểm thử cẩn thận mới tìm ra được!"
  },
  21: {
    title: "Kỹ năng đọc thông báo lỗi từ Trình biên dịch (javac)",
    speaker1: "Thông báo lỗi javac gồm: Tên file, số dòng, mô tả lỗi, và con trỏ ^ chỉ vị trí. Hai mẹo vàng: Luôn sửa lỗi đầu tiên trong danh sách trước; và nếu dòng báo lỗi trông hoàn toàn đúng, hãy kiểm tra kỹ dòng ngay phía trước nó!",
    speaker2: "Nhờ biết cách đọc thông báo lỗi mà em không còn hoảng sợ khi gặp lỗi dài dòng nữa, compiler đang chỉ đường rất tận tình."
  },
  22: {
    title: "[CHECKPOINT 2] Thử tài thám tử chẩn đoán lỗi",
    speaker1: "Tìm 3 lỗi cú pháp trong đoạn code MyProgram trên slide 22?",
    speaker2: "Dạ: Dòng 1 thiếu từ khóa 'class' (public class MyProgram); Dòng 2 hàm main bị viết hoa chữ M (sửa thành main); Dòng 3 thiếu dấu ngoặc kép đóng và dấu chấm phẩy ạ!"
  },
  23: {
    title: "[HANDS-ON LAB 2] Thực hành Debug & Chuỗi ký tự thoát",
    speaker1: "Thực hành Lab 2: Viết EscapeChallenge.java in đường dẫn C:\\Java\\IT26M, khẩu hiệu ngoặc kép \"Học là phải hành!\" và tam giác ASCII.",
    speaker2: "Em đã hoàn thành! Dùng \\\\ cho đường dẫn, \\\" cho khẩu hiệu và \\t cho khoảng cách tab, output hiển thị chuẩn từng khoảng cách!"
  },
  24: {
    title: "TIẾT 3: PHÂN RÃ THỦ TỤC, PHƯƠNG THỨC TĨNH & CASE STUDY DRAWFIGURES",
    speaker1: "Chào mừng các em đến với Tiết 3: Nâng tầm tư duy kiến trúc phần mềm với kỹ thuật Phân rã thủ tục (Procedural Decomposition) và Case Study DrawFigures.",
    speaker2: "Đây là phần em mong đợi nhất để học cách viết code có cấu trúc như các kỹ sư phần mềm thực thụ!"
  },
  25: {
    title: "1.4 Vấn đề của bài toán lớn & Tư duy Phân rã Top-down",
    speaker1: "Cạm bẫy của chương trình nguyên khối là dồn tất cả code vào main, dẫn đến mã nguồn dài, rối rắm và trùng lặp mã nguồn nghiêm trọng. Giải pháp là tư duy Top-down: Chia bài toán lớn thành các bài toán con đơn giản hơn. Nguyên lý vàng: DRY - Don't Repeat Yourself (Đừng bao giờ lặp lại chính mình)!",
    speaker2: "Nguyên lý DRY rất ngắn gọn nhưng là kim chỉ nam để không phải copy-paste code nhiều lần."
  },
  26: {
    title: "Ví dụ thực tế: Phân rã tác vụ 'Làm bánh' (Make Cake)",
    speaker1: "Hình 1.2 giáo trình: Tác vụ 'Make cake' được phân rã thành 4 công đoạn lớn: Make batter, Bake, Make frosting, Frost cake. Ở công đoạn 'Make batter' lại chia nhỏ thành: Trộn bột khô, Đánh bơ đường, Cho trứng, v.v. Mỗi chiếc hộp trong sơ đồ cấu trúc này tương ứng với một Phương thức tĩnh (static method) trong Java!",
    speaker2: "Ví dụ làm bánh quá trực quan thầy ơi! Cứ chia nhỏ thành các nhiệm vụ độc lập thì việc phức tạp đến mấy cũng quản lý dễ dàng."
  },
  27: {
    title: "Phương thức tĩnh (Static Methods): Cú pháp Khai báo & Lời gọi",
    speaker1: "Cú pháp khai báo: public static void tenHam() { các lệnh; }. Khi gọi thực thi trong main: tenHam();. Hàm drawBox() gói 4 lệnh in hộp, khi main cần 2 hộp chỉ việc gọi drawBox() hai lần. Lưu ý: Mọi phương thức phải nằm độc lập trong class, không lồng hàm này trong hàm khác!",
    speaker2: "Khai báo 1 lần duy nhất và tái sử dụng vô số lần ở bất cứ đâu trong chương trình."
  },
  28: {
    title: "Luồng điều khiển khi gọi phương thức (Flow of Control)",
    speaker1: "Sơ đồ DrawBoxes trang 76: Chương trình luôn chạy từ dòng 1 của main. Khi gặp lời gọi drawBox(), CPU tạm dừng main, chuyển giao quyền điều khiển sang thân hàm drawBox chạy 4 lệnh, khi chạm ngoặc đóng } thì quay trở lại (return) đúng vị trí rời đi ở main để chạy tiếp câu lệnh kế.",
    speaker2: "Các mũi tên trên sơ đồ minh họa rất rõ quá trình nhảy sang hàm con rồi quay về, chương trình không chạy thẳng tuột mà có sự điều phối nhịp nhàng."
  },
  29: {
    title: "Luồng điều khiển đa cấp & Khái niệm Ngăn xếp gọi hàm (Call Stack)",
    speaker1: "Khi hàm lồng nhau (main gọi foo, foo gọi bar, bar gọi baz), CPU dùng cấu trúc Call Stack theo nguyên tắc LIFO (Vào sau ra trước) để nhớ đường về. Hàm baz gọi sau cùng sẽ xong trước và lấy ra khỏi stack, quay về bar, rồi về foo, rồi về main. Phân rã mang lại 2 lợi ích: Cấu trúc hóa và Triệt tiêu trùng lặp!",
    speaker2: "Khái niệm Call Stack rất hay, giúp chúng em hiểu sâu cách CPU quản lý bộ nhớ khi chạy các chương trình phức tạp."
  },
  30: {
    title: "1.5 Case Study: Bài toán vẽ hình ASCII nghệ thuật (DrawFigures)",
    speaker1: "Bài toán yêu cầu in 3 hình: Kim cương (Diamond), Chữ X, và Tên lửa vũ trụ (Rocket). Các em hãy quan sát xem có những hình khối nhỏ nào xuất hiện lặp lại ở nhiều nơi?",
    speaker2: "Dạ: Kim cương gồm nón xuôi ở trên và nón ngược ở dưới. Chữ X gồm nón ngược ở trên và nón xuôi ở dưới. Còn Tên lửa có nón xuôi ở đỉnh, 2 thân hộp ở giữa và nón xuôi ở đuôi! Rất nhiều hình con bị lặp lại!"
  },
  31: {
    title: "Phiên bản 1 (DrawFigures1): Tiếp cận Ngây thơ (Naïve Approach)",
    speaker1: "Phiên bản 1 dồn hơn 30 dòng lệnh println vào main. Cụm nón xuôi bị copy-paste 3 lần, nón ngược lặp 2 lần, hình hộp lặp 2 lần. Nếu muốn mở rộng hình rộng thêm 2 dấu cách, ta phải đi tìm và sửa thủ công ở hơn 30 nơi khác nhau, rất dễ sót lỗi!",
    speaker2: "Đúng là cơn ác mộng khi bảo trì code, mã nguồn dài dòng và cực kỳ khó quản lý."
  },
  32: {
    title: "Phiên bản 2 (DrawFigures2): Phân rã Cấp 1 theo Khối hình",
    speaker1: "Phiên bản 2 (Hình 1.3) phân rã cấp 1: main ngắn gọn gọi drawDiamond(), drawX(), drawRocket(). Nhưng bên trong thân 3 hàm này, các lệnh in nón xuôi và nón ngược vẫn bị copy-paste lặp lại!",
    speaker2: "Tức là mới chỉ cải thiện cấu trúc, chứ chưa triệt tiêu được trùng lặp mã nguồn ạ."
  },
  33: {
    title: "Phiên bản 3 (DrawFigures3): Phân rã Hoàn chỉnh 2 Cấp (Triệt tiêu trùng lặp)",
    speaker1: "Hình 1.4 giáo trình: Mô hình kiến trúc 3 tầng: Tầng 1 (main) điều phối; Tầng 2 là các khối hình lớn (drawDiamond, drawX, drawRocket); Tầng 3 là các khối nguyên thủy tái sử dụng tối đa (drawCone, drawV, drawBox).",
    speaker2: "Kiến trúc 3 tầng quá đẹp! Tầng đáy vẽ các nét cơ sở, Tầng giữa lắp ghép thành bức tranh hoàn chỉnh, và Tầng đỉnh chỉ việc gọi chạy."
  },
  34: {
    title: "Mã nguồn hoàn chỉnh đạt chuẩn: DrawFigures3.java",
    speaker1: "DrawFigures3.java: drawDiamond chỉ gọi drawCone() và drawV(). drawX gọi drawV() và drawCone(). drawRocket gọi drawCone(), 2 lần drawBox(), rồi drawCone(). Mã nguồn trong sáng, không trùng lặp một dòng nào!",
    speaker2: "Nếu sau này muốn sửa kích thước hộp, em chỉ cần sửa đúng 1 chỗ trong hàm drawBox() ở Tầng 3 là toàn bộ hai thân hộp tên lửa tự động cập nhật đẹp theo!"
  },
  35: {
    title: "So sánh & Đánh giá 3 thế hệ thiết kế",
    speaker1: "Bảng so sánh: Bản 1 nguyên khối, trùng lặp cao, bảo trì kém; Bản 2 cấu trúc khá nhưng vẫn lặp code; Bản 3 đạt điểm 10 tuyệt đối: phân tầng rõ rệt, triệt tiêu 100% trùng lặp, tái sử dụng tối đa và bảo trì tại 1 điểm duy nhất.",
    speaker2: "Bảng so sánh này giúp chúng em thấm nhuần giá trị của tư duy thiết kế kiến trúc trước khi gõ code."
  },
  36: {
    title: "[CHECKPOINT 3] Dự đoán luồng thực thi hàm lồng nhau",
    speaker1: "TraceTest: main gọi first(), rồi gọi second(). Trong second() in 2, gọi first(), rồi in 3. Màn hình in ra thứ tự nào?",
    speaker2: "Dạ: main gọi first() in 1. Sau đó second() in 2, gọi first() in 1, rồi in 3. Kết quả là 1, 2, 1, 3 -> Đáp án B thưa thầy!"
  },
  37: {
    title: "[HANDS-ON LAB 3] Mini-Project: Thiết kế chương trình Rocket/FightSong",
    speaker1: "20 phút thi đua Lab 3: Chọn viết SpaceRocket (2 tên lửa đứng cạnh nhau có logo IT26M, triệt tiêu 100% trùng lặp) hoặc FightSong (bài hát cổ động có điệp khúc lặp lại). Yêu cầu phân rã tối thiểu 2 cấp!",
    speaker2: "Em chọn bài SpaceRocket ạ! Em tạo các hàm nguyên thủy vẽ mũi, thân, động cơ, ngọn lửa ở Tầng 3, hàm vẽ tên lửa đơn ở Tầng 2 và main ráp lại!"
  },
  38: {
    title: "Tổng kết toàn bộ kiến thức Chương 1 (Checklist Chuẩn đầu ra)",
    speaker1: "Chúng ta đã hoàn thành trọn vẹn 5 chuẩn đầu ra: Hiểu kiến trúc phần cứng, nhị phân, JVM (CLO 1.1); Viết cấu trúc class, main, lệnh in, ký tự thoát (CLO 1.2); Phân loại và gỡ 3 loại lỗi (CLO 1.3); Nắm vững phân rã Top-down và Call Stack (CLO 1.4); và Tự tay thiết kế chương trình đa tầng (CLO 1.5).",
    speaker2: "Em cảm thấy rất tự hào vì chỉ trong 3 tiết học, lớp chúng em đã tiếp thu được lượng kiến thức nền tảng đồ sộ và vững chắc."
  },
  39: {
    title: "Bảng tra cứu nhanh cú pháp cốt lõi (Java Quick Cheatsheet)",
    speaker1: "Cheatsheet tóm tắt: Khung class, hàm main, 4 ký tự thoát (\\n, \\t, \\\", \\\\), cú pháp hàm tĩnh và 3 quy tắc vàng cần nhớ. Các em hãy lưu lại để tra cứu nhanh khi làm bài tập nhé.",
    speaker2: "Slide này rất tiện lợi để chúng em ôn tập nhanh trước kỳ thi và tra cứu khi code đồ án ạ."
  },
  40: {
    title: "Nhiệm vụ tự học & Bài tập về nhà cho lớp IT26M",
    speaker1: "Về nhà: Đọc lại toàn bộ Chương 1 giáo trình (trang 1-102); làm bài tập Self-Check; nộp bài Mantra và TwoRockets lên LMS. Thử sức với Project 1 in chữ MISSISSIPPI khối lớn. Và đọc trước Chương 2: Primitive Data and Definite Loops nhé!",
    speaker2: "Vâng thưa thầy, chúng em sẽ làm đầy đủ bài tập trên hệ thống LMS và nghiên cứu trước Chương 2 ạ."
  },
  41: {
    title: "CẢM ƠN CÁC BẠN SINH VIÊN LỚP IT26M!",
    speaker1: "Thầy xin chân thành cảm ơn sự tập trung, hăng say và nỗ lực tuyệt vời của toàn thể sinh viên lớp IT26M trong suốt buổi học hôm nay. Chúc các em luôn giữ vững ngọn lửa đam mê với công nghệ!",
    speaker2: "Chúng em cảm ơn thầy rất nhiều vì bài giảng quá cuốn hút, dễ hiểu và tràn đầy cảm hứng ạ! Hẹn gặp lại thầy trong buổi học tới!",
    speaker1: "Chào tạm biệt các em. Hẹn gặp lại vào tuần sau!"
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
  const targetSrc = `./Videos/Chapter_01/audio/slide_${AppState.currentSlide}.mp3`;
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
  audioEl.src = `./Videos/Chapter_01/audio/slide_${slideNum}.mp3`;
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

  // Render Slide Display (trực tiếp hiển thị từng trang trích xuất từ slideChapter_01.pdf)
  const slideDisplay = document.getElementById('slideDisplayFrame');
  const transcriptData = SLIDE_TRANSCRIPTS[slideNum] || {
    title: `Slide ${slideNum}`,
    speaker1: "Nội dung thuyết minh giảng viên.",
    speaker2: "Phản hồi của sinh viên."
  };

  if (slideDisplay) {
    const visualHtml = `
      <div style="position: relative; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; background: #000;">
        <img src="./Videos/Chapter_01/slides_png/slide_${slideNum}.png" 
             alt="Slide ${slideNum}: ${transcriptData.title}" 
             class="slide-image" 
             style="max-width: 100%; max-height: 100%; object-fit: contain; box-shadow: 0 4px 12px rgba(0,0,0,0.5);"
             onerror="this.onerror=null; this.parentElement.innerHTML='<div style=\\\'color:#fff;padding:2rem;text-align:center;\\\'>Không thể tải slide. <a href=\\\'./Videos/Chapter_01/slideChapter_01.pdf\\\' target=\\\'_blank\\\' style=\\\'color:#38bdf8;\\\'>Bấm vào đây để mở slideChapter_01.pdf</a></div>';">
        <div style="position: absolute; bottom: 8px; right: 12px; background: rgba(0, 0, 0, 0.75); padding: 3px 10px; border-radius: 4px; font-size: 0.75rem; color: #38bdf8; font-weight: 600; pointer-events: none;">
          slideChapter_01.pdf (Trang ${slideNum}/41)
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
      audioEl.src = `./Videos/Chapter_01/audio/slide_${slideNum}.mp3`;
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
    let badgeLabel = 'Self-Check';
    if (item.type === 'exercise') {
      badgeClass = 'ex-badge-exercise';
      badgeLabel = 'Exercise';
    } else if (item.type === 'project') {
      badgeClass = 'ex-badge-project';
      badgeLabel = 'Programming Project';
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

