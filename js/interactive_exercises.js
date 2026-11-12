// ============================================================================
// HỌC PHẦN: KỸ THUẬT LẬP TRÌNH (4 TÍN CHỈ) - IT26M
// ENGINE BÀI TẬP TƯƠNG TÁC (INTERACTIVE EXERCISES ENGINE)
// HỖ TRỢ SINH VIÊN LÀM BÀI TRỰC TIẾP TRÊN WEB VÀ TỰ ĐỘNG CHẤM ĐÚNG / SAI
// ============================================================================

// Utility: Chuẩn hóa chuỗi (bỏ dấu tiếng Việt, chữ thường, bỏ khoảng trắng thừa) để so khớp linh hoạt
function normalizeExerciseText(str) {
  if (!str) return '';
  return str
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

// Kiểm tra câu trả lời sinh viên có khớp với một trong các từ khóa hợp lệ không
function matchAnswerKeywords(userInput, acceptableKeywords) {
  if (!userInput || !acceptableKeywords || acceptableKeywords.length === 0) return false;
  const normUser = normalizeExerciseText(userInput);
  if (!normUser) return false;

  return acceptableKeywords.some(kw => {
    const normKw = normalizeExerciseText(kw);
    // Khớp chính xác hoặc chứa từ khóa cốt lõi
    return normUser === normKw || normUser.includes(normKw) || normKw.includes(normUser);
  });
}

// ============================================================================
// DỮ LIỆU TƯƠNG TÁC CHI TIẾT (CHAPTER 2 & CHAPTER 1)
// ============================================================================
const INTERACTIVE_EXERCISES_DATA = {
  // --------------------------------------------------------------------------
  // CHƯƠNG 2
  // --------------------------------------------------------------------------
  "sre-2.1": {
    mode: "fill-blank",
    title: "Self-Review 2.1: Điền vào chỗ trống các khái niệm nền tảng",
    items: [
      {
        id: "a",
        label: "a)",
        prefix: "Kỹ thuật",
        suffix: "cho phép bạn tạo giao diện người dùng (GUI) mà không cần phải viết bất kỳ dòng mã lệnh nào.",
        acceptable: ["visual app development", "visual programming", "lap trinh truc quan", "lập trình trực quan", "keo tha", "kéo thả", "phat trien ung dung truc quan", "phát triển ứng dụng trực quan"],
        correctAnswer: "visual app development (phát triển ứng dụng trực quan / kéo thả)",
        explanation: "Mục 2.2: Lập trình trực quan (Visual Programming / RAD) cho phép kéo thả điều khiển từ Toolbox vào Form mà không cần code thủ công."
      },
      {
        id: "b",
        label: "b)",
        prefix: "Một",
        suffix: "là nhóm gồm một hoặc nhiều dự án (projects) cùng hợp thành một ứng dụng Visual C# hoàn chỉnh.",
        acceptable: ["solution", "giai phap", "giải pháp", "giai phap phan mem", "giải pháp phần mềm", "sln", ".sln"],
        correctAnswer: "solution (giải pháp phần mềm - tệp đuôi .sln)",
        explanation: "Mục 2.3: Một Solution là một container chứa một hoặc nhiều Project có liên quan với nhau."
      },
      {
        id: "c",
        label: "c)",
        prefix: "Tính năng",
        suffix: "cho phép tự động ẩn một cửa sổ làm việc trong IDE thành một tab ở mép màn hình.",
        acceptable: ["auto-hide", "autohide", "tu dong an", "tự động ẩn", "auto hide"],
        correctAnswer: "auto-hide (tự động ẩn)",
        explanation: "Mục 2.3: Tính năng Auto-Hide giúp mở rộng không gian thiết kế bằng cách thu gọn cửa sổ thành tab ghim."
      },
      {
        id: "d",
        label: "d)",
        prefix: "Một",
        suffix: "sẽ nổi lên khi con trỏ chuột dừng (hover) trên một biểu tượng nút bấm công cụ.",
        acceptable: ["tool tip", "tooltip", "chu giai cong cu", "chú giải công cụ", "chu thich cong cu", "chú giải"],
        correctAnswer: "tool tip (chú giải công cụ)",
        explanation: "Mục 2.3: Tooltip hiển thị tên nút lệnh và phím tắt thao tác nhanh khi rê chuột qua biểu tượng."
      },
      {
        id: "e",
        label: "e)",
        prefix: "Cửa sổ",
        suffix: "cho phép lập trình viên duyệt cây thư mục và quản lý toàn bộ các tệp tin trong giải pháp.",
        acceptable: ["solution explorer", "solutionexplorer", "quan ly giai phap", "quản lý giải pháp", "cay thu muc"],
        correctAnswer: "Solution Explorer (phím tắt Ctrl+Alt+L)",
        explanation: "Mục 2.4: Solution Explorer hiển thị phân cấp Solution, Project, References, Form1.cs và Program.cs."
      },
      {
        id: "f",
        label: "f)",
        prefix: "Danh sách các thuộc tính trong Properties window có thể được sắp xếp theo",
        suffix: "(Nhập: 'alphabetically' hoặc 'categorized', hoặc cả hai cách).",
        acceptable: ["alphabetically", "categorized", "theo bang chu cai", "theo bảng chữ cái", "theo chu cai", "theo nhom", "theo nhóm", "phan loai", "phân loại", "a-z", "a to z"],
        correctAnswer: "alphabetically (bảng chữ cái) hoặc categorized (theo nhóm phân loại)",
        explanation: "Mục 2.4: Nút Alphabetical xếp từ A-Z; nút Categorized nhóm theo Appearance, Behavior, Layout..."
      },
      {
        id: "g",
        label: "g)",
        prefix: "Thuộc tính",
        suffix: "của Form quy định dòng chữ hiển thị trên thanh tiêu đề của cửa sổ ứng dụng.",
        acceptable: ["text", "tieu de", "tiêu đề", "form text"],
        correctAnswer: "Text",
        explanation: "Mục 2.5: Thuộc tính Text quy định chuỗi văn bản xuất hiện trên Title Bar của Form."
      },
      {
        id: "h)",
        label: "h)",
        prefix: "Hộp công cụ",
        suffix: "chứa sẵn các linh kiện điều khiển đồ họa mà bạn có thể kéo thả vào Form.",
        acceptable: ["toolbox", "tool box", "hop cong cu", "hộp công cụ"],
        correctAnswer: "Toolbox (phím tắt Ctrl+Alt+X)",
        explanation: "Mục 2.4: Cửa sổ Toolbox chứa nhóm Common Controls: Button, Label, TextBox, PictureBox..."
      },
      {
        id: "i",
        label: "i)",
        prefix: "Tính năng",
        suffix: "hiển thị bài viết hướng dẫn phù hợp từ MSDN dựa trên đối tượng đang được chọn khi bấm phím F1.",
        acceptable: ["context-sensitive", "context sensitive", "context-sensitive help", "tro giup theo ngu canh", "trợ giúp theo ngữ cảnh", "ngu canh", "ngữ cảnh"],
        correctAnswer: "context-sensitive help (trợ giúp theo ngữ cảnh)",
        explanation: "Mục 2.3: Phím F1 tự động mở tài liệu trợ giúp tương ứng đúng với điều khiển đang được chọn."
      },
      {
        id: "j",
        label: "j)",
        prefix: "Thuộc tính",
        suffix: "quy định cách căn lề chuỗi văn bản (trái, phải, giữa) bên trong ranh giới của điều khiển Label.",
        acceptable: ["textalign", "text align", "can le", "căn lề", "canh le", "canh lề"],
        correctAnswer: "TextAlign",
        explanation: "Mục 2.5: Thuộc tính TextAlign cung cấp lưới 9 ô trực quan để căn chỉnh vị trí chữ (ví dụ MiddleCenter)."
      }
    ]
  },

  "sre-2.2": {
    mode: "true-false",
    title: "Self-Review 2.2: Nhận định Đúng / Sai và giải thích kỹ thuật",
    items: [
      {
        id: "a",
        label: "a)",
        statement: "Biểu tượng chiếc đinh ghim dùng để bật/tắt chế độ tự động ẩn (auto-hide), còn dấu X dùng để đóng cửa sổ.",
        correct: true,
        explanation: "Đúng (True). Biểu tượng pushpin chuyển giữa trạng thái Auto-Hide (ghim nằm ngang) và Docked (ghim cắm thẳng); dấu X đóng cửa sổ."
      },
      {
        id: "b",
        label: "b)",
        statement: "Các biểu tượng trên thanh công cụ chuẩn (toolbar) đại diện cho các lệnh thường dùng trên thanh menu bar.",
        correct: true,
        explanation: "Đúng (True). Toolbar đóng vai trò phím tắt đồ họa cho các lệnh phổ biến nhất trên Menu Bar (Save All, Open, Start...)."
      },
      {
        id: "c",
        label: "c)",
        statement: "Thanh công cụ toolbar chứa các biểu tượng đại diện cho các điều khiển đồ họa mà bạn có thể kéo thả vào Form.",
        correct: false,
        explanation: "Sai (False). Cửa sổ Toolbox mới là nơi chứa các điều khiển đồ họa kéo-thả; Toolbar chỉ chứa các lệnh thao tác IDE."
      },
      {
        id: "d",
        label: "d)",
        statement: "Cả Form và điều khiển Label đều sở hữu một thanh tiêu đề (title bar) hoàn chỉnh.",
        correct: false,
        explanation: "Sai (False). Chỉ có Form mới sở hữu thanh tiêu đề (title bar) có icon và nút điều khiển; Label là nhãn văn bản phẳng không có title bar."
      },
      {
        id: "e",
        label: "e)",
        statement: "Thuộc tính của các điều khiển chỉ có thể được chỉnh sửa bằng cách viết mã lệnh C# trong lúc chạy.",
        correct: false,
        explanation: "Sai (False). Lập trình viên có thể tùy biến thuộc tính ngay tại thời điểm thiết kế (Design-Time) thông qua Properties window."
      },
      {
        id: "f",
        label: "f)",
        statement: "Điều khiển PictureBox là điều khiển chuyên dụng để hiển thị các tệp hình ảnh đồ họa.",
        correct: true,
        explanation: "Đúng (True). PictureBox được thiết kế chuyên biệt để nạp và hiển thị các tệp đồ họa (.png, .jpg, .gif, .bmp)."
      },
      {
        id: "g",
        label: "g)",
        statement: "Các tệp tin mã nguồn Visual C# sử dụng phần mở rộng là .csharp.",
        correct: false,
        explanation: "Sai (False). Các tệp mã nguồn C# sử dụng phần mở rộng là .cs (ví dụ: Form1.cs, Program.cs)."
      },
      {
        id: "h",
        label: "h)",
        statement: "Màu nền của Form được thiết lập thông qua thuộc tính BackColor.",
        correct: true,
        explanation: "Đúng (True). Thuộc tính BackColor quy định màu nền của Form và hầu hết các điều khiển trong Windows Forms."
      }
    ]
  },

  "ex-2.3": {
    mode: "fill-blank",
    title: "Exercise 2.3: Điền vào chỗ trống các thao tác nâng cao trong IDE",
    items: [
      {
        id: "a",
        label: "a)",
        prefix: "Khi một nút hình dấu 3 chấm [...] (ellipsis button) được nhấp chọn, một",
        suffix: "sẽ được hiển thị.",
        acceptable: ["dialog", "dialog box", "hop thoai", "hộp thoại", "cua so hop thoai", "cửa sổ hộp thoại"],
        correctAnswer: "dialog / dialog box (hộp thoại)",
        explanation: "Mục 2.4: Nút [...] luôn kích hoạt một Dialog chuyên dụng (Font Dialog, Color Picker, Select Resource...)."
      },
      {
        id: "b",
        label: "b)",
        prefix: "Sử dụng trợ giúp",
        suffix: "giúp lập trình viên mở ngay lập tức bài viết hướng dẫn tương ứng với ngữ cảnh hiện tại.",
        acceptable: ["context-sensitive", "context sensitive", "ngu canh", "ngữ cảnh", "theo ngu canh", "theo ngữ cảnh", "f1"],
        correctAnswer: "context-sensitive (trợ giúp theo ngữ cảnh kích hoạt qua phím F1)",
        explanation: "Mục 2.3: F1 mở tài liệu trợ giúp chuẩn xác cho thành phần đang được kích hoạt."
      },
      {
        id: "c",
        label: "c)",
        prefix: "Khi bạn chọn một thuộc tính, phần mô tả ngắn gọn về thuộc tính đó sẽ hiển thị ở đáy của cửa sổ",
        suffix: ".",
        acceptable: ["properties", "properties window", "thuoctinh", "thuộc tính"],
        correctAnswer: "Properties (cụ thể là Description Pane ở chân cửa sổ Properties)",
        explanation: "Mục 2.4: Description Pane hiển thị tóm tắt ý nghĩa và kiểu dữ liệu của thuộc tính đang chọn."
      },
      {
        id: "d",
        label: "d)",
        prefix: "Thuộc tính",
        suffix: "quy định tệp tin hình ảnh nào sẽ được hiển thị bên trong khung PictureBox.",
        acceptable: ["image", "anh", "ảnh", "hinh anh", "hình ảnh"],
        correctAnswer: "Image",
        explanation: "Mục 2.5: Thuộc tính Image lưu tham chiếu đến hình ảnh tài nguyên của PictureBox."
      },
      {
        id: "e",
        label: "e)",
        prefix: "Menu",
        suffix: "trên Menu Bar chứa các lệnh quản lý, sắp xếp bố cục và khôi phục các cửa sổ làm việc.",
        acceptable: ["window", "cua so", "cửa sổ"],
        correctAnswer: "Window (chứa lệnh Reset Window Layout, chia tab)",
        explanation: "Mục 2.3: Menu Window cho phép chuyển đổi giữa các tab tài liệu và khôi phục bố cục giao diện mặc định."
      }
    ]
  },

  "ex-2.4": {
    mode: "true-false",
    title: "Exercise 2.4: Nhận định Đúng / Sai về hành vi thao tác và lập trình",
    items: [
      {
        id: "a",
        label: "a)",
        statement: "Bạn có thể thêm nhanh một điều khiển vào Form bằng cách nhấp đúp chuột lên biểu tượng của nó trong Toolbox.",
        correct: true,
        explanation: "Đúng (True). Nhấp đúp chuột vào điều khiển trong Toolbox sẽ tự động chèn nó vào góc trên bên trái của Form đang mở."
      },
      {
        id: "b",
        label: "b)",
        statement: "Các điều khiển Form, Label và PictureBox sở hữu tập hợp các thuộc tính hoàn toàn giống hệt nhau.",
        correct: false,
        explanation: "Sai (False). Mỗi điều khiển có thuộc tính đặc thù riêng: PictureBox có Image/SizeMode; Label có TextAlign; Form có FormBorderStyle/StartPosition."
      },
      {
        id: "c",
        label: "c)",
        statement: "Nếu máy tính có kết nối Internet, lập trình viên có thể duyệt web và đọc tài liệu ngay trong Visual Studio IDE.",
        correct: true,
        explanation: "Đúng (True). Visual Studio tích hợp sẵn trình duyệt web nội bộ (Web Browser pane) để tra cứu tài liệu MSDN trực tiếp."
      },
      {
        id: "d",
        label: "d)",
        statement: "Các nhà phát triển ứng dụng Visual C# thường tạo nên các phần mềm phức tạp quy mô lớn mà không cần viết bất kỳ dòng mã nào.",
        correct: false,
        explanation: "Sai (False). Kéo thả chỉ hỗ trợ dựng khung giao diện GUI; mọi ứng dụng thực tế đều phải viết mã C# xử lý nghiệp vụ, thuật toán và dữ liệu."
      },
      {
        id: "e",
        label: "e)",
        statement: "Nhấp vào biểu tượng mũi tên (hoặc dấu cộng/trừ) bên trái của một nút phân cấp (node) sẽ giúp mở rộng hoặc thu gọn nút đó.",
        correct: true,
        explanation: "Đúng (True). Thao tác này mở rộng (expand) hoặc thu gọn (collapse) các nhánh trong cây thư mục Solution Explorer hoặc Properties window."
      }
    ]
  },

  "ex-2.5": {
    mode: "concepts",
    title: "Exercise 2.5: Phân tích tính nhất quán trong trải nghiệm giao diện Visual Studio",
    items: [
      {
        id: "1",
        label: "1. Nút dấu ba chấm [...] (Ellipsis buttons):",
        placeholder: "Nêu vai trò và ví dụ minh họa của nút [...]...",
        keyConcepts: ["dialog", "hop thoai", "hộp thoại", "font", "image", "resource", "mo rong", "mở rộng"],
        standardAnswer: "Cơ chế: Báo hiệu sẽ mở một hộp thoại (Dialog) cấu hình phức tạp (Font Dialog, Color Picker, Select Resource) khi ô nhập đơn dòng không chứa đủ."
      },
      {
        id: "2",
        label: "2. Nút mũi tên trỏ xuống (Down-arrow buttons):",
        placeholder: "Nêu vai trò và ví dụ minh họa của nút mũi tên xuống...",
        keyConcepts: ["dropdown", "danh sach", "danh sách", "lua chon", "lựa chọn", "backcolor", "sizemode", "bang mau", "bảng màu"],
        standardAnswer: "Cơ chế: Cung cấp danh sách hữu hạn các giá trị hoặc bảng màu lựa chọn sẵn, ngăn ngừa gõ sai chính tả và tiết kiệm thời gian (BackColor, SizeMode, TextAlign)."
      },
      {
        id: "3",
        label: "3. Nhãn chú giải công cụ (Tool tips):",
        placeholder: "Nêu vai trò và ví dụ minh họa của Tooltip...",
        keyConcepts: ["tooltip", "chu giai", "chú giải", "phim tat", "phím tắt", "re chuot", "rê chuột", "hover"],
        standardAnswer: "Cơ chế: Hiển thị tên gọi, chức năng và phím tắt đi kèm khi con trỏ chuột dừng trên biểu tượng (ví dụ: Start (F5), Save All (Ctrl+Shift+S))."
      }
    ],
    overallConcept: "Nguyên lý Tính nhất quán (Consistency) giúp giảm tải nhận thức (Cognitive load), giúp lập trình viên học một lần và áp dụng ở mọi nơi."
  },

  "ex-2.6": {
    mode: "concepts",
    title: "Exercise 2.6: Định nghĩa các thuật ngữ trọng tâm của Chương 2",
    items: [
      {
        id: "a",
        label: "a) Project (Dự án):",
        placeholder: "Nhập định nghĩa về Project...",
        keyConcepts: ["tap hop", "tập hợp", "ma nguon", "mã nguồn", "tep", "tệp", ".csproj", "bien dich", "biên dịch", "exe", "dll"],
        standardAnswer: "Tập hợp các tệp mã nguồn C#, tài nguyên và cấu hình được quản lý bởi tệp .csproj để cùng biên dịch thành một sản phẩm phần mềm (.exe hoặc .dll)."
      },
      {
        id: "b",
        label: "b) IDE (Môi trường phát triển tích hợp):",
        placeholder: "Nhập định nghĩa về IDE...",
        keyConcepts: ["moi truong", "môi trường", "tich hop", "tích hợp", "soan thao", "soạn thảo", "bien dich", "biên dịch", "go loi", "gỡ lỗi", "debug"],
        standardAnswer: "Gói phần mềm đa năng cung cấp toàn diện các công cụ: soạn thảo code, thiết kế giao diện đồ họa, biên dịch và dò tìm sửa lỗi trên một giao diện thống nhất."
      },
      {
        id: "c",
        label: "c) Debug (Gỡ lỗi / Dò lỗi):",
        placeholder: "Nhập định nghĩa về Debug...",
        keyConcepts: ["go loi", "gỡ lỗi", "do loi", "dò lỗi", "sua loi", "sửa lỗi", "ngoai le", "ngoại lệ", "theo doi", "theo dõi", "bien", "biến", "f5"],
        standardAnswer: "Quy trình chạy ứng dụng dưới sự kiểm soát của Debugger nhằm phát hiện lỗi logic, theo dõi biến và phân tích luồng thực thi chương trình."
      },
      {
        id: "d",
        label: "d) Properties window (Cửa sổ Thuộc tính):",
        placeholder: "Nhập định nghĩa về Properties window...",
        keyConcepts: ["thuoctinh", "thuộc tính", "f4", "ngoai quan", "ngoại quan", "design-time", "thiet ke", "thiết kế", "cau hinh", "cấu hình"],
        standardAnswer: "Cửa sổ công cụ (F4) cho phép xem và thiết lập các thuộc tính ngoại quan, hành vi và bố cục của Form và điều khiển tại thời điểm thiết kế (Design-Time)."
      },
      {
        id: "e",
        label: "e) Dialogs (Hộp thoại):",
        placeholder: "Nhập định nghĩa về Dialogs...",
        keyConcepts: ["hop thoai", "hộp thoại", "cua so phu", "cửa sổ phụ", "thong bao", "thông báo", "xac nhan", "xác nhận", "cau hinh", "cấu hình"],
        standardAnswer: "Các cửa sổ phụ chuyên dụng bật lên tạm thời để giao tiếp với người dùng: hiển thị thông báo, nhận xác nhận hoặc hỗ trợ thiết lập tham số chi tiết."
      },
      {
        id: "f",
        label: "f) Visual Studio:",
        placeholder: "Nhập định nghĩa về Visual Studio...",
        keyConcepts: ["microsoft", "bo cong cu", "bộ công cụ", "phat trien", "phát triển", "da ngon ngu", "đa ngôn ngữ", "c#", ".net"],
        standardAnswer: "Bộ công cụ phát triển phần mềm đa năng hàng đầu của Microsoft, hỗ trợ lập trình C#/.NET đa nền tảng (Desktop, Web, Cloud, Mobile)."
      }
    ]
  },

  // Đồ án GUI Chapter 2
  "ex-2.7": {
    mode: "gui-project",
    title: "Exercise 2.7: Đồ án Thiết kế Giao diện Đồng hồ Bấm giờ (Stop Watch GUI)",
    checklist: [
      { id: "step1", text: "Tạo dự án Windows Forms đặt tên StopWatchGUI, đặt Text = 'Stop Watch', Size = 350, 220" },
      { id: "step2", text: "Thêm điều khiển RichTextBox hiển thị số '00:00:00', Font 28pt Bold, đặt ReadOnly = True" },
      { id: "step3", text: "Thêm 3 Buttons mang nhãn 'Start', 'Stop', 'Reset' kích thước 80x35" },
      { id: "step4", text: "Căn chỉnh hàng ngang bằng Snap Lines hoặc lệnh Format -> Align -> Middles" },
      { id: "step5", text: "Nhấn F5 chạy thử ứng dụng ở Run Mode và kiểm tra độ sắc nét giao diện" }
    ],
    codeKeywords: ["Stop Watch", "RichTextBox", "00:00:00", "ReadOnly", "btnStart", "btnStop", "btnReset", "Button"],
    sampleCode: `// Mã C# thiết kế giao diện Stop Watch
this.Text = "Stop Watch";
this.ClientSize = new System.Drawing.Size(340, 180);

RichTextBox rtbTimer = new RichTextBox();
rtbTimer.Text = "00:00:00";
rtbTimer.Font = new Font("Segoe UI", 28, FontStyle.Bold);
rtbTimer.Size = new Size(280, 65);
rtbTimer.Location = new Point(30, 25);
rtbTimer.ReadOnly = true;
this.Controls.Add(rtbTimer);

Button btnStart = new Button() { Text = "Start", Location = new Point(30, 110), Size = new Size(80, 35) };
Button btnStop = new Button() { Text = "Stop", Location = new Point(130, 110), Size = new Size(80, 35) };
Button btnReset = new Button() { Text = "Reset", Location = new Point(230, 110), Size = new Size(80, 35) };
this.Controls.AddRange(new Control[] { btnStart, btnStop, btnReset });`
  },

  "ex-2.8": {
    mode: "gui-project",
    title: "Exercise 2.8: Đồ án Thiết kế Màn hình Đăng nhập (Login Form GUI)",
    checklist: [
      { id: "step1", text: "Tạo dự án LoginFormGUI, đặt Text = 'Login Form', BackColor = Bisque (tông màu ấm)" },
      { id: "step2", text: "Thêm Label tiêu đề lớn 'Please Sign In', phông Bookman Old Style 14.25pt Bold" },
      { id: "step3", text: "Thêm 2 cặp Label & TextBox cho 'User Name:' và 'Password:'" },
      { id: "step4", text: "Thiết lập thuộc tính PasswordChar = '*' cho ô Password để ẩn mật khẩu" },
      { id: "step5", text: "Thêm CheckBox 'Remember me on this computer' và 2 nút 'OK', 'Cancel'" }
    ],
    codeKeywords: ["Login Form", "Please Sign In", "txtUser", "txtPass", "PasswordChar", "chkRemember", "OK", "Cancel"],
    sampleCode: `// Mã C# thiết kế giao diện Login Form
this.Text = "Login Form";
this.BackColor = Color.Bisque;
this.ClientSize = new Size(360, 240);

Label lblTitle = new Label() { Text = "Please Sign In", Font = new Font("Bookman Old Style", 14.25f, FontStyle.Bold), Location = new Point(30, 20) };
TextBox txtUser = new TextBox() { Location = new Point(130, 65), Width = 190 };
TextBox txtPass = new TextBox() { Location = new Point(130, 105), Width = 190, PasswordChar = '*' };
CheckBox chkRemember = new CheckBox() { Text = "Remember me on this computer", Location = new Point(130, 140) };
Button btnOK = new Button() { Text = "OK", Location = new Point(130, 180), Size = new Size(85, 30) };
Button btnCancel = new Button() { Text = "Cancel", Location = new Point(235, 180), Size = new Size(85, 30) };
this.Controls.AddRange(new Control[] { lblTitle, txtUser, txtPass, chkRemember, btnOK, btnCancel });`
  },

  "ex-2.9": {
    mode: "gui-project",
    title: "Exercise 2.9: Đồ án Thiết kế Bàn phím Máy tính Bỏ túi (Calculator GUI)",
    checklist: [
      { id: "step1", text: "Tạo dự án CalculatorGUI, đặt Text = 'Calculator', Size = 280, 360, FormBorderStyle = FixedDialog" },
      { id: "step2", text: "Thêm TextBox màn hình hiển thị số '0', ReadOnly = True, TextAlign = Right" },
      { id: "step3", text: "Thêm Panel có BorderStyle = Fixed3D để làm khung chứa bàn phím số" },
      { id: "step4", text: "Bài trí 20 nút bấm (các số 0-9, dấu chấm, C, C/E, +, -, *, /, =)" },
      { id: "step5", text: "Sử dụng lệnh Format -> Horizontal Spacing / Vertical Spacing -> Make Equal để các nút cách đều nhau" }
    ],
    codeKeywords: ["Calculator", "Fixed3D", "Panel", "TextBox", "ReadOnly", "TextAlign", "Right", "Button"],
    sampleCode: `// Bố trí bàn phím Calculator trong Panel Fixed3D
this.Text = "Calculator";
TextBox txtDisplay = new TextBox() { Text = "0", ReadOnly = true, TextAlign = HorizontalAlignment.Right, Width = 230, Location = new Point(15, 15) };
Panel pnlKeys = new Panel() { BorderStyle = BorderStyle.Fixed3D, Location = new Point(15, 50), Size = new Size(230, 230) };
this.Controls.AddRange(new Control[] { txtDisplay, pnlKeys });`
  },

  "ex-2.10": {
    mode: "gui-project",
    title: "Exercise 2.10: Đồ án Thiết kế Đồng hồ Báo thức Điện tử (Alarm Clock GUI)",
    checklist: [
      { id: "step1", text: "Tạo dự án AlarmClockGUI, đặt Text = 'Alarm Clock', Size = 438, 170" },
      { id: "step2", text: "Thêm màn hình Label đồng hồ điện tử: BackColor = Black, ForeColor = Silver, BorderStyle = Fixed3D, Font 12pt Bold" },
      { id: "step3", text: "Thêm GroupBox nhãn 'AM/PM' chứa 2 RadioButtons loại trừ lẫn nhau" },
      { id: "step4", text: "Bố trí 7 nút bấm chỉnh giờ, phút, giây, báo thức và nút Snooze" },
      { id: "step5", text: "Chạy thử F5 kiểm tra màu chữ bạc phát sáng trên nền đen" }
    ],
    codeKeywords: ["Alarm Clock", "Fixed3D", "Black", "Silver", "GroupBox", "RadioButton", "AM", "PM", "Label"],
    sampleCode: `// Giao diện Alarm Clock LED
this.Text = "Alarm Clock";
Label lblLED = new Label() { Text = "00:00:00", BackColor = Color.Black, ForeColor = Color.Silver, BorderStyle = BorderStyle.Fixed3D, Font = new Font("Segoe UI", 12, FontStyle.Bold), Size = new Size(100, 45) };
GroupBox grpAMPM = new GroupBox() { Text = "AM/PM", Size = new Size(100, 50) };
RadioButton rdoAM = new RadioButton() { Text = "AM", Location = new Point(10, 20), Checked = true };
RadioButton rdoPM = new RadioButton() { Text = "PM", Location = new Point(55, 20) };
grpAMPM.Controls.AddRange(new Control[] { rdoAM, rdoPM });`
  },

  "ex-2.11": {
    mode: "gui-project",
    title: "Exercise 2.11: Đồ án Thiết kế Máy Nghe Đài Bán Dẫn (Radio GUI)",
    checklist: [
      { id: "step1", text: "Tạo dự án RadioGUI, đặt Text = 'Radio', Size = 427, 194" },
      { id: "step2", text: "Thêm GroupBox 'Pre-set Stations' chứa 6 Buttons số 1 đến 6" },
      { id: "step3", text: "Thêm GroupBox 'Speakers' (chứa CheckBoxes Rear, Front) và Button 'Power On/Off'" },
      { id: "step4", text: "Thêm GroupBox 'Volume Control' chứa thanh trượt TrackBar và CheckBox Mute" },
      { id: "step5", text: "Thêm GroupBox 'Tuning' (Label tần số 92.9 nền đen chữ bạc và RadioButtons AM/FM)" },
      { id: "step6", text: "Thêm PictureBox nốt nhạc MusicNote.gif với SizeMode = StretchImage" }
    ],
    codeKeywords: ["Radio", "Pre-set Stations", "Speakers", "TrackBar", "Volume Control", "Tuning", "AM", "FM", "PictureBox", "StretchImage"],
    sampleCode: `// Giao diện Radio GUI phức hợp
this.Text = "Radio";
GroupBox grpVolume = new GroupBox() { Text = "Volume Control", Size = new Size(180, 75) };
TrackBar tbVol = new TrackBar() { Minimum = 0, Maximum = 100, Value = 50, Width = 150 };
grpVolume.Controls.Add(tbVol);
PictureBox picMusic = new PictureBox() { SizeMode = PictureBoxSizeMode.StretchImage, Size = new Size(55, 75) };`
  },

  // --------------------------------------------------------------------------
  // CHƯƠNG 1 (CÁC BÀI TẬP TIÊU BIỂU)
  // --------------------------------------------------------------------------
  "sre-1.1": {
    mode: "fill-blank",
    title: "Self-Review 1.1: Khái niệm Máy tính, Phần cứng & Phân cấp dữ liệu",
    items: [
      {
        id: "a",
        label: "a)",
        prefix: "Máy tính xử lý dữ liệu dưới sự điều khiển của các chuỗi chỉ thị được gọi là",
        suffix: ".",
        acceptable: ["computer programs", "chuong trinh may tinh", "chương trình máy tính", "phan mem", "phần mềm", "programs"],
        correctAnswer: "computer programs (chương trình máy tính / phần mềm)",
        explanation: "Chương trình máy tính hướng dẫn máy tính thực hiện các tác vụ theo thứ tự logic."
      },
      {
        id: "b",
        label: "b)",
        prefix: "Một chiếc máy tính bao gồm nhiều thiết bị vật lý khác nhau được gọi là",
        suffix: "(bàn phím, màn hình, chuột...).",
        acceptable: ["hardware", "phan cung", "phần cứng"],
        correctAnswer: "hardware (phần cứng)",
        explanation: "Phần cứng bao gồm các linh kiện điện tử vật lý cấu thành máy tính."
      },
      {
        id: "c",
        label: "c)",
        prefix: "Các phần tử dữ liệu được xử lý bởi máy tính tạo thành một",
        suffix: ", từ bits đến ký tự, trường, bản ghi, tệp tin.",
        acceptable: ["data hierarchy", "cau truc phan cap du lieu", "cấu trúc phân cấp dữ liệu", "phan cap du lieu", "phân cấp dữ liệu"],
        correctAnswer: "data hierarchy (cấu trúc phân cấp dữ liệu)",
        explanation: "Dữ liệu được tổ chức theo cấp độ tăng dần: bit -> character -> field -> record -> file -> database."
      },
      {
        id: "d",
        label: "d)",
        prefix: "Máy tính chỉ có thể trực tiếp hiểu được ngôn ngữ",
        suffix: "của chính nó, gồm các số 1 và 0.",
        acceptable: ["machine", "machine language", "may", "ngôn ngữ máy", "ngon ngu may", "nhi phan", "nhị phân"],
        correctAnswer: "machine (ngôn ngữ máy - machine language)",
        explanation: "CPU máy tính chỉ thực thi các chỉ thị mã máy nhị phân 0 và 1."
      },
      {
        id: "e",
        label: "e)",
        prefix: "Ba loại ngôn ngữ lập trình là ngôn ngữ máy,",
        suffix: "và ngôn ngữ bậc cao (Nhập: 'assembly languages' hoặc 'hợp ngữ').",
        acceptable: ["assembly", "assembly languages", "hop ngu", "hợp ngữ"],
        correctAnswer: "assembly languages (hợp ngữ)",
        explanation: "Hợp ngữ sử dụng các từ khóa viết tắt tiếng Anh (như ADD, MOV) thay thế cho mã nhị phân."
      },
      {
        id: "f",
        label: "f)",
        prefix: "Các chương trình dùng để dịch chương trình ngôn ngữ bậc cao sang ngôn ngữ máy được gọi là",
        suffix: ".",
        acceptable: ["compilers", "trinh bien dich", "trình biên dịch", "bien dich", "biên dịch"],
        correctAnswer: "compilers (các trình biên dịch)",
        explanation: "Trình biên dịch (Compiler) chuyển đổi toàn bộ mã nguồn bậc cao thành ngôn ngữ máy để thực thi."
      },
      {
        id: "g",
        label: "g)",
        prefix: "Một bộ vi xử lý",
        suffix: "tích hợp nhiều vi xử lý trên cùng một vi mạch (dual-core có 2 CPU, quad-core có 4 CPU).",
        acceptable: ["multicore", "da nhan", "đa nhân", "da loi", "đa lõi", "multi-core"],
        correctAnswer: "multicore (đa nhân / đa lõi)",
        explanation: "Kiến trúc đa nhân cho phép máy tính xử lý song song nhiều tác vụ đồng thời."
      },
      {
        id: "h",
        label: "h)",
        prefix: "Windows 10 đã giới thiệu nền tảng",
        suffix: "để xây dựng ứng dụng chạy trên PC, tablet, điện thoại, Xbox, HoloLens.",
        acceptable: ["uwp", "universal windows platform", "nen tang windows pho quat", "nền tảng windows phổ quát"],
        correctAnswer: "Universal Windows Platform (UWP)",
        explanation: "UWP cho phép phát triển ứng dụng đa thiết bị bằng mã nguồn C# thống nhất."
      }
    ]
  },

  "sre-1.4": {
    mode: "true-false",
    title: "Self-Review 1.4: Khảo sát nhận định toàn diện Chương 1",
    items: [
      {
        id: "a",
        label: "a)",
        statement: "Các đối tượng phần mềm mô hình hóa cả những khái niệm trừu tượng lẫn những sự vật trong thế giới thực.",
        correct: true,
        explanation: "Đúng (True). Đối tượng có thể mô hình hóa vật lý (ô tô, con người) hoặc trừu tượng (tài khoản ngân hàng, giao dịch, luồng xử lý)."
      },
      {
        id: "b",
        label: "b)",
        statement: "Mô hình cơ sở dữ liệu phổ biến nhất là cơ sở dữ liệu quan hệ, trong đó dữ liệu lưu trong các bảng gồm bản ghi và trường.",
        correct: true,
        explanation: "Đúng (True). RDBMS tổ chức dữ liệu thành các quan hệ (bảng) gồm hàng (record) và cột (field)."
      },
      {
        id: "c",
        label: "c)",
        statement: "Cơ sở dữ liệu là một tập hợp dữ liệu được tổ chức để dễ dàng truy cập và thao tác.",
        correct: true,
        explanation: "Đúng (True)."
      },
      {
        id: "d",
        label: "d)",
        statement: "Dữ liệu trên bộ nhớ thứ cấp mất nhiều thời gian truy xuất hơn, nhưng chi phí trên mỗi đơn vị lưu trữ cao hơn nhiều so với bộ nhớ chính RAM.",
        correct: false,
        explanation: "Sai (False). Chi phí trên mỗi đơn vị dung lượng của bộ nhớ thứ cấp (HDD/SSD) THẤP HƠN NHIỀU so với RAM."
      },
      {
        id: "e",
        label: "e)",
        statement: "Các ngôn ngữ bậc cao cho phép bạn viết các chỉ thị trông gần giống như tiếng Anh hàng ngày và chứa các biểu thức toán học thông dụng.",
        correct: true,
        explanation: "Đúng (True)."
      },
      {
        id: "f",
        label: "f)",
        statement: "Một đối tượng sở hữu các thuộc tính đi liền với nó trong suốt quá trình đối tượng được sử dụng trong chương trình.",
        correct: true,
        explanation: "Đúng (True)."
      },
      {
        id: "g",
        label: "g)",
        statement: "Giao thức TCP đảm bảo các thông điệp, bao gồm các phần được đánh số tuần tự gọi là bytes, được định tuyến chính xác.",
        correct: false,
        explanation: "Sai (False). Các mảnh dữ liệu được đánh số tuần tự trong TCP gọi là GÓI TIN (PACKETS), không phải bytes."
      },
      {
        id: "h",
        label: "h)",
        statement: "Dung lượng truyền tải trên Internet tăng lên khủng khiếp, trong khi chi phí phần cứng cũng tăng theo.",
        correct: false,
        explanation: "Sai (False). Chi phí phần cứng đã GIẢM MẠNH theo thời gian nhờ định luật Moore."
      },
      {
        id: "i",
        label: "i)",
        statement: "Bạn có thể xây dựng các ứng dụng trên nền web bằng C#.",
        correct: true,
        explanation: "Đúng (True) - Thông qua công nghệ ASP.NET / ASP.NET Core."
      },
      {
        id: "j",
        label: "j)",
        statement: "Ngôn ngữ Objective-C và Java là hai ngôn ngữ lập trình chủ chốt được sử dụng để phát triển các ứng dụng iOS cho iPhone, iPad.",
        correct: false,
        explanation: "Sai (False). Ngôn ngữ lập trình chính cho iOS của Apple là Swift và Objective-C; Java dùng cho Android."
      },
      {
        id: "k",
        label: "k)",
        statement: "Công nghệ JavaServer Pages (JSP) cho phép bạn tạo các ứng dụng web với C#.",
        correct: false,
        explanation: "Sai (False). Công nghệ web của C# là ASP.NET, còn JSP là của nền tảng Java."
      },
      {
        id: "l",
        label: "l)",
        statement: "CLR là máy ảo thực thi các chương trình .NET.",
        correct: true,
        explanation: "Đúng (True). Common Language Runtime (CLR) là máy ảo cốt lõi thực thi mã MSIL."
      }
    ]
  }
};

// ============================================================================
// HỆ THỐNG LƯU TRỮ VÀ KHÔI PHỤC KẾT QUẢ BÀI LÀM (LOCAL STORAGE)
// ============================================================================
const STORAGE_KEY_EXERCISES = 'uda_csharp_exercise_submissions_v1';

function getStoredExerciseSubmissions() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY_EXERCISES);
    return raw ? JSON.parse(raw) : {};
  } catch (e) {
    return {};
  }
}

function saveExerciseSubmission(exId, submissionData) {
  try {
    const data = getStoredExerciseSubmissions();
    data[exId] = submissionData;
    localStorage.setItem(STORAGE_KEY_EXERCISES, JSON.stringify(data));
  } catch (e) {
    console.error('Không thể lưu kết quả bài tập:', e);
  }
}

function clearExerciseSubmission(exId) {
  try {
    const data = getStoredExerciseSubmissions();
    delete data[exId];
    localStorage.setItem(STORAGE_KEY_EXERCISES, JSON.stringify(data));
  } catch (e) {
    console.error(e);
  }
}

// ============================================================================
// HÀM RENDER KHU VỰC BÀI TẬP TƯƠNG TÁC CHÍNH (HTML GENERATOR)
// ============================================================================
function generateInteractiveWorkspace(item) {
  const exId = item.id;
  const config = INTERACTIVE_EXERCISES_DATA[exId];
  const submission = getStoredExerciseSubmissions()[exId] || null;

  // Trường hợp 1: Dạng bài tập Điền vào chỗ trống (Fill in the blanks)
  if (config && config.mode === 'fill-blank') {
    return generateFillBlankUI(item, config, submission);
  }

  // Trường hợp 2: Dạng bài tập Đúng / Sai (True / False)
  if (config && config.mode === 'true-false') {
    return generateTrueFalseUI(item, config, submission);
  }

  // Trường hợp 3: Dạng bài tập Khái niệm / Định nghĩa thuật ngữ (Concepts / Terms)
  if (config && config.mode === 'concepts') {
    return generateConceptsUI(item, config, submission);
  }

  // Trường hợp 4: Dạng Đồ án Thiết kế GUI & Viết mã C# (GUI Project)
  if (config && config.mode === 'gui-project') {
    return generateGuiProjectUI(item, config, submission);
  }

  // Trường hợp 5: Bài tập tổng quát tự luận / code khác
  return generateGeneralExerciseUI(item, submission);
}

// ----------------------------------------------------------------------------
// 1. GIAO DIỆN ĐIỀN VÀO CHỖ TRỐNG (FILL-IN-THE-BLANK)
// ----------------------------------------------------------------------------
function generateFillBlankUI(item, config, submission) {
  const exId = item.id;
  const hasSubmitted = Boolean(submission);
  const userAnswers = submission ? (submission.answers || {}) : {};
  const score = submission ? submission.score : 0;
  const total = config.items.length;
  const percent = total > 0 ? Math.round((score / total) * 100) : 0;

  const itemsHtml = config.items.map((sub, idx) => {
    const currentVal = userAnswers[sub.id] || '';
    const isCorrect = submission && submission.itemResults && submission.itemResults[sub.id] === true;
    const isWrong = submission && submission.itemResults && submission.itemResults[sub.id] === false;

    let inputBorderClass = '';
    let feedbackBadge = '';

    if (hasSubmitted) {
      if (isCorrect) {
        inputBorderClass = 'input-correct';
        feedbackBadge = `<span class="sub-badge-correct">✅ Chính xác!</span>`;
      } else {
        inputBorderClass = 'input-wrong';
        feedbackBadge = `
          <div class="sub-feedback-wrong">
            <span class="sub-badge-wrong">❌ Chưa đúng</span>
            <span class="sub-answer-reveal"><strong>Đáp án chuẩn:</strong> ${escapeHtml(sub.correctAnswer)}</span>
            ${sub.explanation ? `<div class="sub-expl-text">💡 ${escapeHtml(sub.explanation)}</div>` : ''}
          </div>
        `;
      }
    }

    return `
      <div class="ex-interactive-row" id="row-${exId}-${sub.id}">
        <div class="ex-sub-label">${sub.label}</div>
        <div class="ex-sub-body">
          <div class="ex-sentence-wrapper">
            ${sub.prefix ? `<span>${escapeHtml(sub.prefix)}</span>` : ''}
            <span class="blank-input-wrapper">
              <input 
                type="text" 
                id="input-${exId}-${sub.id}" 
                class="ex-blank-input ${inputBorderClass}" 
                placeholder="...nhập từ/cụm từ..." 
                value="${escapeHtml(currentVal)}"
                data-ex-id="${exId}"
                data-sub-id="${sub.id}"
                autocomplete="off"
                onkeypress="if(event.key === 'Enter') focusNextBlank('${exId}', ${idx})"
              >
            </span>
            ${sub.suffix ? `<span>${escapeHtml(sub.suffix)}</span>` : ''}
          </div>
          <div class="ex-sub-feedback" id="feedback-${exId}-${sub.id}">${feedbackBadge}</div>
        </div>
      </div>
    `;
  }).join('');

  return `
    <div class="interactive-workspace" id="workspace-${exId}">
      <div class="workspace-header">
        <div class="workspace-title">
          <span>✍️ KHU VỰC LÀM BÀI TRỰC TIẾP (ĐIỀN VÀO CHỖ TRỐNG)</span>
        </div>
        <div class="workspace-hint-note">Gõ đáp án vào các ô trống và nhấn nút Kiểm tra để xem kết quả đánh giá tự động.</div>
      </div>

      ${hasSubmitted ? renderScoreBanner(score, total, percent) : ''}

      <div class="ex-items-container">
        ${itemsHtml}
      </div>

      <div class="ex-action-buttons">
        <button type="button" class="btn-check-exercise" onclick="submitFillBlank('${exId}')">
          🚀 Nộp bài & Kiểm tra kết quả
        </button>
        <button type="button" class="btn-reset-exercise" onclick="resetExercise('${exId}')">
          🔄 Làm lại
        </button>
      </div>
    </div>
  `;
}

// ----------------------------------------------------------------------------
// 2. GIAO DIỆN NHẬN ĐỊNH ĐÚNG / SAI (TRUE / FALSE)
// ----------------------------------------------------------------------------
function generateTrueFalseUI(item, config, submission) {
  const exId = item.id;
  const hasSubmitted = Boolean(submission);
  const userAnswers = submission ? (submission.answers || {}) : {};
  const score = submission ? submission.score : 0;
  const total = config.items.length;
  const percent = total > 0 ? Math.round((score / total) * 100) : 0;

  const itemsHtml = config.items.map((sub, idx) => {
    const selectedVal = userAnswers[sub.id]; // true, false hoặc undefined
    const isCorrect = submission && submission.itemResults && submission.itemResults[sub.id] === true;
    const isWrong = submission && submission.itemResults && submission.itemResults[sub.id] === false;

    let trueActive = selectedVal === true ? 'active-choice' : '';
    let falseActive = selectedVal === false ? 'active-choice' : '';

    let feedbackBadge = '';
    if (hasSubmitted) {
      if (isCorrect) {
        feedbackBadge = `
          <div class="sub-feedback-correct">
            <span class="sub-badge-correct">✅ Chính xác!</span>
            <div class="sub-expl-text">💡 ${escapeHtml(sub.explanation)}</div>
          </div>
        `;
      } else {
        const correctStr = sub.correct ? 'Đúng (True)' : 'Sai (False)';
        feedbackBadge = `
          <div class="sub-feedback-wrong">
            <span class="sub-badge-wrong">❌ Chưa chính xác (Đáp án đúng là: ${correctStr})</span>
            <div class="sub-expl-text">💡 ${escapeHtml(sub.explanation)}</div>
          </div>
        `;
      }
    }

    return `
      <div class="ex-interactive-row tf-row" id="row-${exId}-${sub.id}">
        <div class="ex-sub-label">${sub.label}</div>
        <div class="ex-sub-body">
          <p class="tf-statement-text">${escapeHtml(sub.statement)}</p>
          
          <div class="tf-btn-group" id="tf-group-${exId}-${sub.id}">
            <button 
              type="button" 
              class="tf-choice-btn btn-true ${trueActive}" 
              onclick="selectTFChoice('${exId}', '${sub.id}', true)"
              data-choice="true"
            >
              ✓ Đúng (True)
            </button>
            <button 
              type="button" 
              class="tf-choice-btn btn-false ${falseActive}" 
              onclick="selectTFChoice('${exId}', '${sub.id}', false)"
              data-choice="false"
            >
              ✕ Sai (False)
            </button>
          </div>

          <div class="ex-sub-feedback" id="feedback-${exId}-${sub.id}">${feedbackBadge}</div>
        </div>
      </div>
    `;
  }).join('');

  return `
    <div class="interactive-workspace" id="workspace-${exId}">
      <div class="workspace-header">
        <div class="workspace-title">
          <span>⚖️ KHU VỰC LÀM BÀI TRỰC TIẾP (NHẬN ĐỊNH ĐÚNG / SAI)</span>
        </div>
        <div class="workspace-hint-note">Nhấp chọn Đúng (True) hoặc Sai (False) cho từng nhận định bên dưới rồi bấm Kiểm tra kết quả.</div>
      </div>

      ${hasSubmitted ? renderScoreBanner(score, total, percent) : ''}

      <div class="ex-items-container">
        ${itemsHtml}
      </div>

      <div class="ex-action-buttons">
        <button type="button" class="btn-check-exercise" onclick="submitTrueFalse('${exId}')">
          🚀 Nộp bài & Kiểm tra kết quả
        </button>
        <button type="button" class="btn-reset-exercise" onclick="resetExercise('${exId}')">
          🔄 Làm lại
        </button>
      </div>
    </div>
  `;
}

// ----------------------------------------------------------------------------
// 3. GIAO DIỆN ĐỊNH NGHĨA KHÁI NIỆM & TỰ LUẬN (CONCEPTS & TERMS)
// ----------------------------------------------------------------------------
function generateConceptsUI(item, config, submission) {
  const exId = item.id;
  const hasSubmitted = Boolean(submission);
  const userAnswers = submission ? (submission.answers || {}) : {};
  const score = submission ? submission.score : 0;
  const total = config.items.length;
  const percent = total > 0 ? Math.round((score / total) * 100) : 0;

  const itemsHtml = config.items.map((sub, idx) => {
    const currentVal = userAnswers[sub.id] || '';
    const isMatched = submission && submission.itemResults && submission.itemResults[sub.id] === true;

    let feedbackBadge = '';
    if (hasSubmitted) {
      if (isMatched) {
        feedbackBadge = `
          <div class="sub-feedback-correct">
            <span class="sub-badge-correct">✅ Đạt chuẩn! (Đã nêu trúng các từ khóa cốt lõi)</span>
            <div class="model-answer-box">
              <strong>📖 Định nghĩa chuẩn Deitel:</strong> ${escapeHtml(sub.standardAnswer)}
            </div>
          </div>
        `;
      } else {
        feedbackBadge = `
          <div class="sub-feedback-wrong">
            <span class="sub-badge-wrong">⚠️ Cần bổ sung thêm từ khóa chuyên môn</span>
            <div class="model-answer-box">
              <strong>📖 Định nghĩa chuẩn Deitel:</strong> ${escapeHtml(sub.standardAnswer)}
            </div>
          </div>
        `;
      }
    }

    return `
      <div class="ex-interactive-row concept-row" id="row-${exId}-${sub.id}">
        <div class="ex-sub-label">${sub.label}</div>
        <div class="ex-sub-body">
          <textarea 
            id="input-${exId}-${sub.id}" 
            class="ex-concept-textarea" 
            placeholder="${escapeHtml(sub.placeholder || 'Trình bày định nghĩa ngắn gọn...')}"
            rows="2"
          >${escapeHtml(currentVal)}</textarea>
          <div class="ex-sub-feedback" id="feedback-${exId}-${sub.id}">${feedbackBadge}</div>
        </div>
      </div>
    `;
  }).join('');

  return `
    <div class="interactive-workspace" id="workspace-${exId}">
      <div class="workspace-header">
        <div class="workspace-title">
          <span>🧠 KHU VỰC THỬ THÁCH ĐỊNH NGHĨA & PHÂN TÍCH KHÁI NIỆM</span>
        </div>
        <div class="workspace-hint-note">Tự diễn giải ngắn gọn bằng lời của bạn. Hệ thống sẽ phân tích các từ khóa kỹ thuật cốt lõi và so sánh với giáo trình.</div>
      </div>

      ${hasSubmitted ? renderScoreBanner(score, total, percent) : ''}

      <div class="ex-items-container">
        ${itemsHtml}
      </div>

      <div class="ex-action-buttons">
        <button type="button" class="btn-check-exercise" onclick="submitConcepts('${exId}')">
          🚀 Phân tích từ khóa & Kiểm tra kết quả
        </button>
        <button type="button" class="btn-reset-exercise" onclick="resetExercise('${exId}')">
          🔄 Làm lại
        </button>
      </div>
    </div>
  `;
}

// ----------------------------------------------------------------------------
// 4. GIAO DIỆN ĐỒ ÁN THIẾT KẾ GUI & VIẾT MÃ C# (GUI PROJECTS)
// ----------------------------------------------------------------------------
function generateGuiProjectUI(item, config, submission) {
  const exId = item.id;
  const hasSubmitted = Boolean(submission);
  const checkedSteps = submission ? (submission.checkedSteps || {}) : {};
  const userCode = submission ? (submission.code || '') : '';
  const codeAnalysis = submission ? (submission.codeAnalysis || null) : null;

  const checklistHtml = config.checklist.map((step, idx) => {
    const isChecked = checkedSteps[step.id] === true;
    return `
      <label class="project-check-item">
        <input 
          type="checkbox" 
          id="chk-${exId}-${step.id}" 
          ${isChecked ? 'checked' : ''}
          onchange="updateProjectChecklist('${exId}')"
        >
        <span class="checkmark-label">${escapeHtml(step.text)}</span>
      </label>
    `;
  }).join('');

  let analysisResultHtml = '';
  if (codeAnalysis) {
    analysisResultHtml = `
      <div class="code-analysis-report">
        <div style="font-weight: 700; margin-bottom: 0.5rem; color: ${codeAnalysis.passed ? 'var(--accent-green)' : '#f59e0b'};">
          ${codeAnalysis.passed ? '✅ Mã nguồn C# đạt chuẩn các điều khiển yêu cầu!' : '⚠️ Mã C# chưa xuất hiện đầy đủ các điều khiển / thuộc tính mong đợi'}
        </div>
        <div class="analysis-tags">
          ${codeAnalysis.details.map(d => `<span class="tag ${d.found ? 'tag-found' : 'tag-missing'}">${d.found ? '✓' : '✗'} ${escapeHtml(d.term)}</span>`).join('')}
        </div>
      </div>
    `;
  }

  return `
    <div class="interactive-workspace" id="workspace-${exId}">
      <div class="workspace-header">
        <div class="workspace-title">
          <span>🛠️ BẢNG KIỂM TIẾN ĐỘ THỰC HÀNH & KIỂM TRA MÃ C# TRỰC TIẾP</span>
        </div>
        <div class="workspace-hint-note">Thực hành kéo thả trong Visual Studio, đánh dấu các bước đã hoàn thành và dán mã C# để kiểm tra tự động.</div>
      </div>

      <div class="project-checklist-box">
        <h5 style="margin-bottom: 0.75rem; font-size: 0.95rem; color: var(--primary-cyan);">📋 Checklist các tiêu chí đồ án:</h5>
        ${checklistHtml}
      </div>

      <div class="project-code-sandbox">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
          <label style="font-weight: 600; font-size: 0.85rem; color: var(--text-muted);">💻 Dán mã C# khởi tạo hoặc Designer của bạn vào đây để kiểm tra:</label>
          <button type="button" class="btn-sample-code" onclick="fillProjectSampleCode('${exId}')">Nạp mã gợi ý</button>
        </div>
        <textarea 
          id="code-input-${exId}" 
          class="project-code-textarea" 
          placeholder="// Dán mã Form1.cs hoặc Form1.Designer.cs của bạn tại đây để kiểm tra..."
          rows="5"
        >${escapeHtml(userCode)}</textarea>

        <div id="code-feedback-${exId}">${analysisResultHtml}</div>
      </div>

      <div class="ex-action-buttons">
        <button type="button" class="btn-check-exercise" onclick="submitGuiProject('${exId}')">
          🔍 Kiểm tra mã C# & Đánh giá đồ án
        </button>
        <button type="button" class="btn-reset-exercise" onclick="resetExercise('${exId}')">
          🔄 Đặt lại
        </button>
      </div>
    </div>
  `;
}

// ----------------------------------------------------------------------------
// 5. GIAO DIỆN TỰ LUẬN TỔNG QUÁT (GENERAL EXERCISES)
// ----------------------------------------------------------------------------
function generateGeneralExerciseUI(item, submission) {
  const exId = item.id;
  const userText = submission ? (submission.text || '') : '';
  const hasSubmitted = Boolean(submission);

  return `
    <div class="interactive-workspace" id="workspace-${exId}">
      <div class="workspace-header">
        <div class="workspace-title">
          <span>📝 KHU VỰC TỰ LUYỆN TẬP & ĐỐI CHIẾU KẾT QUẢ</span>
        </div>
        <div class="workspace-hint-note">Nhập câu trả lời hoặc suy nghĩ của bạn trước khi bấm 'Kiểm tra & Đối chiếu đáp án chuẩn'.</div>
      </div>

      <textarea 
        id="general-input-${exId}" 
        class="ex-concept-textarea" 
        placeholder="Nhập câu trả lời, phân tích hoặc lời giải của bạn vào đây..."
        rows="3"
      >${escapeHtml(userText)}</textarea>

      ${hasSubmitted ? `
        <div class="sub-feedback-correct" style="margin-top: 0.75rem;">
          <span class="sub-badge-correct">✅ Đã hoàn thành nộp bài!</span>
          <div class="sub-expl-text">Bạn đã hoàn thành bài tập này. Hãy đối chiếu câu trả lời của bạn với lời giải chi tiết bên dưới.</div>
        </div>
      ` : ''}

      <div class="ex-action-buttons">
        <button type="button" class="btn-check-exercise" onclick="submitGeneralExercise('${exId}')">
          🚀 Gửi bài & Mở khóa lời giải chi tiết
        </button>
        <button type="button" class="btn-reset-exercise" onclick="resetExercise('${exId}')">
          🔄 Làm lại
        </button>
      </div>
    </div>
  `;
}

// ----------------------------------------------------------------------------
// RENDER BANNER ĐIỂM SỐ (SCORE BANNER)
// ----------------------------------------------------------------------------
function renderScoreBanner(score, total, percent) {
  let badgeColor = '#10b981';
  let badgeText = '🏆 Xuất sắc — Bạn đã làm chủ kiến thức mục này!';
  if (percent < 50) {
    badgeColor = '#ef4444';
    badgeText = '💪 Cần ôn tập thêm! Hãy xem lại phần giải thích và thử làm lại nhé.';
  } else if (percent < 80) {
    badgeColor = '#f59e0b';
    badgeText = '👏 Khá tốt! Đã nắm được các điểm mấu chốt.';
  }

  return `
    <div class="ex-score-banner" style="border-left-color: ${badgeColor};">
      <div class="score-main-row">
        <div class="score-number-pill" style="background: ${badgeColor};">
          ${score} / ${total} câu đúng (${percent}%)
        </div>
        <div class="score-comment" style="color: ${badgeColor}; font-weight: 700;">
          ${badgeText}
        </div>
      </div>
      <div class="score-progress-bar">
        <div class="score-progress-fill" style="width: ${percent}%; background: ${badgeColor};"></div>
      </div>
    </div>
  `;
}

// ============================================================================
// HÀM XỬ LÝ SỰ KIỆN SUBMIT VÀ ĐÁNH GIÁ (INTERACTIVE ACTIONS)
// ============================================================================

// 1. Submit Điền vào chỗ trống
window.submitFillBlank = function(exId) {
  const config = INTERACTIVE_EXERCISES_DATA[exId];
  if (!config) return;

  const answers = {};
  const itemResults = {};
  let score = 0;

  config.items.forEach(sub => {
    const inputEl = document.getElementById(`input-${exId}-${sub.id}`);
    const userVal = inputEl ? inputEl.value.trim() : '';
    answers[sub.id] = userVal;

    const isMatch = matchAnswerKeywords(userVal, sub.acceptable);
    itemResults[sub.id] = isMatch;
    if (isMatch) score++;
  });

  saveExerciseSubmission(exId, {
    mode: 'fill-blank',
    answers,
    itemResults,
    score,
    timestamp: Date.now()
  });

  // Re-render exercise
  refreshExerciseCard(exId);
};

// 2. Chọn True/False
window.selectTFChoice = function(exId, subId, choiceVal) {
  const group = document.getElementById(`tf-group-${exId}-${subId}`);
  if (!group) return;

  const btnTrue = group.querySelector('.btn-true');
  const btnFalse = group.querySelector('.btn-false');

  if (choiceVal === true) {
    btnTrue.classList.add('active-choice');
    btnFalse.classList.remove('active-choice');
  } else {
    btnFalse.classList.add('active-choice');
    btnTrue.classList.remove('active-choice');
  }

  // Tự động lưu lựa chọn tạm thời
  window[`_temp_tf_${exId}_${subId}`] = choiceVal;
};

// 3. Submit True / False
window.submitTrueFalse = function(exId) {
  const config = INTERACTIVE_EXERCISES_DATA[exId];
  if (!config) return;

  const answers = {};
  const itemResults = {};
  let score = 0;

  config.items.forEach(sub => {
    let chosenVal = window[`_temp_tf_${exId}_${sub.id}`];
    // Nếu chưa bấm chọn trong phiên hiện tại, kiểm tra DOM active
    if (chosenVal === undefined) {
      const group = document.getElementById(`tf-group-${exId}-${sub.id}`);
      if (group) {
        if (group.querySelector('.btn-true.active-choice')) chosenVal = true;
        else if (group.querySelector('.btn-false.active-choice')) chosenVal = false;
      }
    }

    answers[sub.id] = chosenVal;
    const isCorrect = chosenVal === sub.correct;
    itemResults[sub.id] = isCorrect;
    if (isCorrect) score++;
  });

  saveExerciseSubmission(exId, {
    mode: 'true-false',
    answers,
    itemResults,
    score,
    timestamp: Date.now()
  });

  refreshExerciseCard(exId);
};

// 4. Submit Tự luận / Khái niệm
window.submitConcepts = function(exId) {
  const config = INTERACTIVE_EXERCISES_DATA[exId];
  if (!config) return;

  const answers = {};
  const itemResults = {};
  let score = 0;

  config.items.forEach(sub => {
    const inputEl = document.getElementById(`input-${exId}-${sub.id}`);
    const userVal = inputEl ? inputEl.value.trim() : '';
    answers[sub.id] = userVal;

    const isMatch = matchAnswerKeywords(userVal, sub.keyConcepts);
    itemResults[sub.id] = isMatch;
    if (isMatch) score++;
  });

  saveExerciseSubmission(exId, {
    mode: 'concepts',
    answers,
    itemResults,
    score,
    timestamp: Date.now()
  });

  refreshExerciseCard(exId);
};

// 5. Submit GUI Project
window.submitGuiProject = function(exId) {
  const config = INTERACTIVE_EXERCISES_DATA[exId];
  if (!config) return;

  // Lấy checklist
  const checkedSteps = {};
  let checkedCount = 0;
  config.checklist.forEach(step => {
    const chk = document.getElementById(`chk-${exId}-${step.id}`);
    const isChecked = chk ? chk.checked : false;
    checkedSteps[step.id] = isChecked;
    if (isChecked) checkedCount++;
  });

  // Phân tích mã nguồn
  const codeEl = document.getElementById(`code-input-${exId}`);
  const userCode = codeEl ? codeEl.value : '';

  let codeAnalysis = null;
  if (config.codeKeywords && config.codeKeywords.length > 0) {
    const details = config.codeKeywords.map(term => {
      const found = normalizeExerciseText(userCode).includes(normalizeExerciseText(term));
      return { term, found };
    });
    const foundCount = details.filter(d => d.found).length;
    codeAnalysis = {
      passed: foundCount >= Math.ceil(config.codeKeywords.length * 0.6),
      foundCount,
      totalCount: config.codeKeywords.length,
      details
    };
  }

  saveExerciseSubmission(exId, {
    mode: 'gui-project',
    checkedSteps,
    code: userCode,
    codeAnalysis,
    score: checkedCount,
    timestamp: Date.now()
  });

  refreshExerciseCard(exId);
};

// 6. Nạp mã mẫu cho GUI Project
window.fillProjectSampleCode = function(exId) {
  const config = INTERACTIVE_EXERCISES_DATA[exId];
  if (!config || !config.sampleCode) return;
  const codeEl = document.getElementById(`code-input-${exId}`);
  if (codeEl) {
    codeEl.value = config.sampleCode;
  }
};

// 7. Cập nhật checkbox checklist
window.updateProjectChecklist = function(exId) {
  // Tự động lưu tiến độ checklist
  const config = INTERACTIVE_EXERCISES_DATA[exId];
  if (!config) return;
  const checkedSteps = {};
  config.checklist.forEach(step => {
    const chk = document.getElementById(`chk-${exId}-${step.id}`);
    if (chk) checkedSteps[step.id] = chk.checked;
  });
  const sub = getStoredExerciseSubmissions()[exId] || {};
  sub.checkedSteps = checkedSteps;
  saveExerciseSubmission(exId, sub);
};

// 8. Submit bài tập tổng quát
window.submitGeneralExercise = function(exId) {
  const inputEl = document.getElementById(`general-input-${exId}`);
  const textVal = inputEl ? inputEl.value.trim() : '';

  saveExerciseSubmission(exId, {
    mode: 'general',
    text: textVal,
    score: 1,
    timestamp: Date.now()
  });

  refreshExerciseCard(exId);

  // Mở luôn đáp án chi tiết
  const solEl = document.getElementById(`solution-${exId}`);
  if (solEl) solEl.classList.add('open');
};

// 9. Reset bài làm
window.resetExercise = function(exId) {
  clearExerciseSubmission(exId);
  // Xóa các biến tạm
  const keys = Object.keys(window).filter(k => k.startsWith(`_temp_tf_${exId}`));
  keys.forEach(k => delete window[k]);
  refreshExerciseCard(exId);
};

// 10. Chuyển con trỏ sang ô tiếp theo khi nhấn Enter
window.focusNextBlank = function(exId, currentIdx) {
  const config = INTERACTIVE_EXERCISES_DATA[exId];
  if (!config || !config.items) return;
  if (currentIdx + 1 < config.items.length) {
    const nextSub = config.items[currentIdx + 1];
    const nextInput = document.getElementById(`input-${exId}-${nextSub.id}`);
    if (nextInput) nextInput.focus();
  } else {
    // Nhấn Enter ở ô cuối cùng -> Nộp bài luôn
    submitFillBlank(exId);
  }
};

// 11. Refresh lại DOM của card sau khi submit / reset
function refreshExerciseCard(exId) {
  if (typeof renderExerciseList === 'function') {
    // Giữ vị trí cuộn trang để không bị giật
    const scrollY = window.scrollY;
    renderExerciseList(document.getElementById('exerciseSearchInput')?.value || '');
    window.scrollTo(0, scrollY);
  }
}

// Gắn vào window để truy xuất toàn cục an toàn
if (typeof window !== 'undefined') {
  window.INTERACTIVE_EXERCISES_DATA = INTERACTIVE_EXERCISES_DATA;
  window.generateInteractiveWorkspace = generateInteractiveWorkspace;
  window.getStoredExerciseSubmissions = getStoredExerciseSubmissions;
}
