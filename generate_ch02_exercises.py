# -*- coding: utf-8 -*-
import json

exercises = [
    # 2.1
    {
        "id": "2.1",
        "category": "self-review",
        "title": "Self-Review 2.1: Điền vào chỗ trống các khái niệm nền tảng",
        "description": "Củng cố các khái niệm cơ bản về môi trường phát triển ứng dụng trực quan Visual C#.",
        "question": "Điền từ hoặc cụm từ thích hợp vào chỗ trống trong các phát biểu sau:\n"
                  "a) Kỹ thuật _______ cho phép bạn tạo giao diện người dùng (GUI) mà không cần phải viết bất kỳ dòng mã lệnh nào.\n"
                  "b) Một _______ là nhóm gồm một hoặc nhiều dự án (projects) cùng hợp thành một ứng dụng Visual C# hoàn chỉnh.\n"
                  "c) Tính năng _______ cho phép tự động ẩn một cửa sổ làm việc trong IDE thành một tab ở mép màn hình.\n"
                  "d) Một _______ sẽ nổi lên khi con trỏ chuột dừng (hover) trên một biểu tượng nút bấm công cụ.\n"
                  "e) Cửa sổ _______ cho phép lập trình viên duyệt cây thư mục và quản lý toàn bộ các tệp tin trong giải pháp.\n"
                  "f) Danh sách các thuộc tính trong Properties window có thể được sắp xếp theo _______ hoặc theo _______.\n"
                  "g) Thuộc tính _______ của Form quy định dòng chữ hiển thị trên thanh tiêu đề của cửa sổ ứng dụng.\n"
                  "h) Hộp công cụ _______ chứa sẵn các linh kiện điều khiển đồ họa mà bạn có thể kéo thả vào Form.\n"
                  "i) Tính năng _______ hiển thị bài viết hướng dẫn phù hợp từ MSDN dựa trên đối tượng đang được chọn khi bấm phím F1.\n"
                  "j) Thuộc tính _______ quy định cách căn lề chuỗi văn bản (trái, phải, giữa) bên trong ranh giới của điều khiển Label.",
        "solution": "Đáp án chuẩn mực theo Giáo trình Deitel (trang 100):\n\n"
                    "a) **visual app development** (phát triển ứng dụng trực quan / lập trình kéo thả).\n"
                    "b) **solution** (giải pháp phần mềm - tệp đuôi .sln).\n"
                    "c) **auto-hide** (tự động ẩn - biểu tượng đinh ghim xoay ngang).\n"
                    "d) **tool tip** (chú giải công cụ kèm phím tắt trong ngoặc đơn).\n"
                    "e) **Solution Explorer** (cửa sổ quản trị cấu trúc dự án - phím tắt Ctrl+Alt+L).\n"
                    "f) **alphabetically** (theo bảng chữ cái từ A-Z), **categorically** (phân loại theo nhóm chủ đề: Appearance, Behavior, Layout...).\n"
                    "g) **Text** (thuộc tính quy định chuỗi tiêu đề hiển thị trên thanh tiêu đề Form).\n"
                    "h) **Toolbox** (hộp công cụ linh kiện đồ họa - phím tắt Ctrl+Alt+X).\n"
                    "i) **context-sensitive help** (trợ giúp theo ngữ cảnh kích hoạt bằng phím F1).\n"
                    "j) **TextAlign** (căn lề văn bản trong nhãn, cung cấp lưới 9 ô vuông 3x3 với giá trị tâm MiddleCenter).",
        "hints": "Xem lại Mục 2.2 đến 2.4 trong giáo trình Deitel: các cửa sổ nòng cốt, phím tắt F1, tính năng ghim pin và thuộc tính Form/Label.",
        "image": "extracted_images/fig2_18_solution_explorer.png"
    },
    # 2.2
    {
        "id": "2.2",
        "category": "self-review",
        "title": "Self-Review 2.2: Nhận định Đúng / Sai và giải thích kỹ thuật",
        "description": "Kiểm tra sự thấu hiểu về hành vi của các thành phần giao diện Visual Studio IDE.",
        "question": "Xác định các phát biểu sau là Đúng (True) hay Sai (False). Nếu Sai, hãy giải thích rõ lý do kỹ thuật:\n"
                  "a) Biểu tượng chiếc đinh ghim dùng để bật/tắt chế độ tự động ẩn (auto-hide), còn dấu X dùng để đóng cửa sổ.\n"
                  "b) Các biểu tượng trên thanh công cụ chuẩn (toolbar) đại diện cho các lệnh thường dùng trên thanh menu bar.\n"
                  "c) Thanh công cụ toolbar chứa các biểu tượng đại diện cho các điều khiển đồ họa mà bạn có thể kéo thả vào Form.\n"
                  "d) Cả Form và điều khiển Label đều sở hữu một thanh tiêu đề (title bar) hoàn chỉnh.\n"
                  "e) Thuộc tính của các điều khiển chỉ có thể được chỉnh sửa bằng cách viết mã lệnh C# trong lúc chạy.\n"
                  "f) Điều khiển PictureBox là điều khiển chuyên dụng để hiển thị các tệp hình ảnh đồ họa.\n"
                  "g) Các tệp tin mã nguồn Visual C# sử dụng phần mở rộng là .csharp.\n"
                  "h) Màu nền của Form được thiết lập thông qua thuộc tính BackColor.",
        "solution": "Phân tích và lời giải chuẩn mực theo Giáo trình Deitel (trang 100):\n\n"
                    "a) **True (Đúng)**. Biểu tượng đinh ghim (pushpin) bật/tắt chế độ auto-hide, còn nút dấu X màu đỏ/xám dùng để đóng hoàn toàn cửa sổ.\n"
                    "b) **True (Đúng)**. Toolbar đóng vai trò phím tắt trực quan đại diện cho các lệnh phổ biến nhất trên Menu Bar (Save All, Open, Start...).\n"
                    "c) **False (Sai)**. Cửa sổ **Toolbox** mới là nơi chứa các biểu tượng điều khiển để kéo thả vào Form; toolbar chỉ chứa các lệnh thao tác IDE.\n"
                    "d) **False (Sai)**. Chỉ có **Form** mới sở hữu thanh tiêu đề (title bar) có icon, tiêu đề và các nút thu phóng/đóng; Label chỉ là nhãn văn bản phẳng không có title bar.\n"
                    "e) **False (Sai)**. Thuộc tính điều khiển hoàn toàn có thể được tùy biến trực quan lúc thiết kế (Design-Time) thông qua cửa sổ **Properties Window** mà không cần viết một dòng mã nào.\n"
                    "f) **True (Đúng)**. PictureBox là điều khiển chuyên dụng để nạp và hiển thị các định dạng ảnh như PNG, JPG, GIF, BMP, ICO.\n"
                    "g) **False (Sai)**. Tệp mã nguồn Visual C# sử dụng phần mở rộng chuẩn mực là **.cs** (viết tắt của C Sharp), ví dụ: `Form1.cs`, `Program.cs`.\n"
                    "h) **True (Đúng)**. Thuộc tính `BackColor` (Background Color) quy định màu nền của Form cũng như của các điều khiển đồ họa.",
        "hints": "Phân biệt rạch ròi giữa Toolbar (lệnh IDE) và Toolbox (linh kiện kéo thả); đuôi tệp C# là .cs.",
        "image": "extracted_images/fig2_13_pushpin_icon.png"
    },
    # 2.3
    {
        "id": "2.3",
        "category": "self-review",
        "title": "Exercise 2.3: Điền vào chỗ trống các thao tác nâng cao trong IDE",
        "description": "Các thao tác với hộp thoại Dialog, trợ giúp F1 và menu Window.",
        "question": "Điền từ thích hợp vào chỗ trống trong các nhận định sau:\n"
                  "a) Khi một nút hình dấu 3 chấm [...] (ellipsis button) được nhấp chọn, một _______ sẽ được hiển thị.\n"
                  "b) Sử dụng trợ giúp _______ giúp lập trình viên mở ngay lập tức bài viết hướng dẫn tương ứng với ngữ cảnh hiện tại.\n"
                  "c) Khi bạn chọn một thuộc tính, phần mô tả ngắn gọn về thuộc tính đó sẽ hiển thị ở đáy của cửa sổ _______.\n"
                  "d) Thuộc tính _______ quy định tệp tin hình ảnh nào sẽ được hiển thị bên trong khung PictureBox.\n"
                  "e) Menu _______ trên Menu Bar chứa các lệnh quản lý, sắp xếp bố cục và khôi phục các cửa sổ làm việc.",
        "solution": "Đáp án chi tiết:\n\n"
                    "a) **dialog / dialog box** (hộp thoại - ví dụ: Font Dialog, Select Resource Dialog, Color Picker).\n"
                    "b) **context-sensitive** (trợ giúp theo ngữ cảnh kích hoạt qua phím F1).\n"
                    "c) **Properties** (cụ thể là khung mô tả Description Pane nằm ở chân cửa sổ Properties Window).\n"
                    "d) **Image** (thuộc tính lưu tham chiếu hình ảnh trong PictureBox).\n"
                    "e) **Window** (menu chứa lệnh Reset Window Layout, chia tab, quản lý màn hình làm việc).",
        "hints": "Mục 2.4 - 2.6 Deitel: Nút dấu 3 chấm [...] luôn mở hộp thoại đồ họa; menu Window quản trị layout.",
        "image": "extracted_images/fig2_27_font_dialog.png"
    },
    # 2.4
    {
        "id": "2.4",
        "category": "self-review",
        "title": "Exercise 2.4: Nhận định Đúng / Sai về hành vi thao tác và lập trình",
        "description": "Khảo sát các thao tác thực tế khi thiết kế Form và viết mã phần mềm.",
        "question": "Cho biết mỗi phát biểu sau là Đúng hay Sai. Giải thích ngắn gọn:\n"
                  "a) Bạn có thể thêm nhanh một điều khiển vào Form bằng cách nhấp đúp chuột lên biểu tượng của nó trong Toolbox.\n"
                  "b) Các điều khiển Form, Label và PictureBox sở hữu tập hợp các thuộc tính hoàn toàn giống hệt nhau.\n"
                  "c) Nếu máy tính có kết nối Internet, lập trình viên có thể duyệt web và đọc tài liệu ngay trong Visual Studio IDE.\n"
                  "d) Các nhà phát triển ứng dụng Visual C# thường tạo nên các phần mềm phức tạp quy mô lớn mà không cần viết bất kỳ dòng mã nào.\n"
                  "e) Nhấp vào biểu tượng mũi tên (hoặc dấu cộng/trừ) bên trái của một nút phân cấp (node) sẽ giúp mở rộng hoặc thu gọn nút đó.",
        "solution": "Phân tích và lời giải:\n\n"
                    "a) **True (Đúng)**. Ngoài việc kéo thả, nhấp đúp vào một điều khiển trong Toolbox sẽ tự động thêm ngay một đối tượng điều khiển đó vào góc trên bên trái của Form.\n"
                    "b) **False (Sai)**. Mặc dù cùng kế thừa từ lớp cha `Control` và có một số thuộc tính chung (như Size, Location, BackColor), mỗi điều khiển có các thuộc tính đặc thù riêng biệt: PictureBox có `Image`, `SizeMode`; Label có `TextAlign`; Form có `StartPosition`, `WindowState`, `FormBorderStyle`.\n"
                    "c) **True (Đúng)**. Visual Studio tích hợp sẵn trình duyệt web nội bộ (Web Browser pane) và tab Start Page/MSDN cho phép duyệt web trực tiếp.\n"
                    "d) **False (Sai)**. Lập trình trực quan WYSIWYG chỉ giúp thiết kế nhanh bộ khung giao diện (GUI). Mọi ứng dụng thực tế phức tạp đều bắt buộc phải viết mã C# xử lý logic thuật toán, cơ sở dữ liệu và xử lý ngoại lệ.\n"
                    "e) **True (Đúng)**. Biểu tượng mũi tên/dấu cộng trong cây thư mục Solution Explorer hoặc danh sách thuộc tính Categorized cho phép mở rộng (expand) hoặc thu gọn (collapse) các nhánh phân cấp.",
        "hints": "Xem lại tính năng nhấp đúp trong Toolbox; các ứng dụng thương mại luôn cần mã nguồn logic sự kiện.",
        "image": "extracted_images/fig2_19_toolbox_window.png"
    },
    # 2.5
    {
        "id": "2.5",
        "category": "self-review",
        "title": "Exercise 2.5: Phân tích tính nhất quán trong trải nghiệm giao diện Visual Studio",
        "description": "Giải thích vai trò của các mẫu thiết kế UI nhất quán: nút ba chấm [...], mũi tên xổ xuống, và tooltips.",
        "question": "Một số thành phần giao diện xuất hiện xuyên suốt trong Visual Studio thực hiện các hành vi tương tự nhau trong các ngữ cảnh khác nhau. Hãy giải thích và nêu ví dụ minh họa về cách hoạt động của:\n"
                  "1. Nút bấm hình dấu ba chấm [...] (ellipsis buttons).\n"
                  "2. Nút mũi tên trỏ xuống (down-arrow buttons).\n"
                  "3. Nhãn chú giải công cụ (tool tips).\n"
                  "Theo em, tại sao môi trường Visual Studio IDE lại được thiết kế theo phong cách nhất quán như vậy?",
        "solution": "Phân tích công thái học và nguyên lý thiết kế UI/UX nhất quán trong Visual Studio:\n\n"
                    "1. **Nút dấu ba chấm [...] (Ellipsis buttons):**\n"
                    "   - *Cơ chế:* Báo hiệu cho lập trình viên biết rằng khi bấm vào đây, một hộp thoại (Dialog) đầy đủ tính năng sẽ xuất hiện để cung cấp nhiều tùy chọn cấu hình phức tạp mà một ô nhập liệu đơn dòng không thể chứa hết.\n"
                    "   - *Ví dụ:* Nút `[...]` ở thuộc tính `Font` mở hộp thoại Font Dialog để chọn phông/kích cỡ; nút `[...]` ở thuộc tính `Image` mở hộp thoại Select Resource để duyệt và nạp tệp ảnh; nút `[...]` ở ô Location khi tạo dự án mới mở hộp thoại Browse Folder.\n\n"
                    "2. **Nút mũi tên xổ xuống (Down-arrow buttons):**\n"
                    "   - *Cơ chế:* Cung cấp một danh sách hữu hạn các giá trị hoặc tùy chọn cho trước (Dropdown list/Palette picker), ngăn ngừa người dùng gõ sai chính tả và tiết kiệm thời gian.\n"
                    "   - *Ví dụ:* Mũi tên ở thuộc tính `BackColor` mở bảng màu 3 tab (Custom, Web, System); mũi tên ở thuộc tính `SizeMode` liệt kê 5 giá trị enum (Normal, StretchImage, AutoSize, CenterImage, Zoom); mũi tên ở thuộc tính `TextAlign` hiển thị lưới 9 ô vuông trực quan.\n\n"
                    "3. **Chú giải công cụ (Tool tips):**\n"
                    "   - *Cơ chế:* Hỗ trợ người dùng nhận diện nhanh tên gọi và chức năng của một biểu tượng đồ họa trừu tượng kèm phím tắt thao tác nhanh.\n"
                    "   - *Ví dụ:* Rê chuột qua nút Start hiển thị `Start (F5)`, rê qua đĩa mềm hiển thị `Save All (Ctrl+Shift+S)`.\n\n"
                    "**Ý nghĩa thiết kế:** Triết lý thiết kế này tuân thủ nguyên lý **Tính nhất quán (Consistency)** trong công thái học phần mềm: Giúp giảm tải nhận thức (Cognitive load), giúp lập trình viên nhanh chóng hình thành phản xạ tự nhiên, học cách sử dụng một tính năng một lần và áp dụng được ở mọi ngóc ngách của công cụ.",
        "hints": "Mục 2.4 giáo trình Deitel: Nguyên lý nhất quán giúp tăng tốc độ phát triển và giảm thiểu sai sót.",
        "image": "extracted_images/fig2_28_textalign_grid.png"
    },
    # 2.6
    {
        "id": "2.6",
        "category": "self-review",
        "title": "Exercise 2.6: Định nghĩa các thuật ngữ trọng tâm của Chương 2",
        "description": "Giải thích ngắn gọn và chuẩn mực các khái niệm cốt lõi của môn học.",
        "question": "Hãy trình bày định nghĩa kỹ thuật ngắn gọn, súc tích cho 6 thuật ngữ sau:\n"
                  "a) Project\n"
                  "b) IDE\n"
                  "c) Debug\n"
                  "d) Properties window\n"
                  "e) Dialogs\n"
                  "f) Visual Studio",
        "solution": "Định nghĩa chuẩn hóa theo Giáo trình Deitel & Deitel:\n\n"
                    "a) **Project (Dự án):** Là một tập hợp các tệp mã nguồn C#, tệp cấu hình, tham chiếu thư viện và tài nguyên đồ họa được tổ chức lại để cùng biên dịch thành một sản phẩm phần mềm duy nhất (như một tệp thực thi `.exe` hoặc thư viện `.dll`), được quản lý bởi tệp định dạng `.csproj`.\n\n"
                    "b) **IDE (Integrated Development Environment - Môi trường Phát triển Tích hợp):** Gói phần mềm đa năng cung cấp toàn diện tất cả các công cụ cần thiết cho toàn bộ vòng đời phát triển phần mềm (soạn thảo code, thiết kế giao diện đồ họa, biên dịch mã, quản lý tài nguyên và dò tìm sửa lỗi) trên một giao diện thống nhất.\n\n"
                    "c) **Debug (Gỡ lỗi / Dò lỗi):** Quy trình chạy ứng dụng dưới sự kiểm soát và giám sát của công cụ Debugger nhằm phát hiện, theo dõi giá trị biến, phân tích luồng thực thi và loại bỏ các lỗi logic (bugs) hoặc các ngoại lệ bất thường (Exceptions).\n\n"
                    "d) **Properties window (Cửa sổ Thuộc tính):** Cửa sổ công cụ trong IDE (phím tắt F4) cho phép lập trình viên kiểm tra và cấu hình các thuộc tính ngoại quan (Appearance), hành vi (Behavior) và bố cục (Layout) của Form và các điều khiển đồ họa ngay tại thời điểm thiết kế (Design-Time).\n\n"
                    "e) **Dialogs (Hộp thoại):** Các cửa sổ phụ chuyên dụng bật lên tạm thời trên màn hình để giao tiếp với người dùng: hiển thị thông báo, nhận xác nhận, hoặc hỗ trợ thực hiện một tác vụ cấu hình chi tiết (ví dụ: Font Dialog, OpenFileDialog, Color Dialog).\n\n"
                    "f) **Visual Studio:** Bộ công cụ phát triển phần mềm hàng đầu thế giới do Microsoft phát triển, hỗ trợ lập trình đa ngôn ngữ (C#, F#, C++, VB.NET, TypeScript) và đa nền tảng (Desktop, Web, Cloud, Mobile, Game, AI).",
        "hints": "Mục 2.1 - 2.5 Deitel: Nắm vững vai trò của từng công cụ trong vòng đời phát triển phần mềm.",
        "image": "extracted_images/fig2_20_properties_window.png"
    },
    # 2.7
    {
        "id": "2.7",
        "category": "project",
        "title": "Exercise 2.7: Đồ án Thiết kế Giao diện Đồng hồ Bấm giờ (Stop Watch GUI)",
        "description": "Tạo giao diện người dùng hoàn chỉnh cho ứng dụng đồng hồ bấm giờ thể thao theo Hình 2.36 giáo trình Deitel.",
        "question": "Hãy tạo giao diện đồ họa cho ứng dụng Stop Watch như minh họa tại Hình 2.36 trong giáo trình:\n"
                  "1. Form: Đổi thuộc tính `Text` thành 'Stop Watch', chỉnh kích thước phù hợp.\n"
                  "2. Màn hình thời gian: Thêm điều khiển `RichTextBox` hiển thị số to `00:00:00`, căn lề và định vị ở nửa trên của Form.\n"
                  "3. Bảng điều khiển: Thêm một `GroupBox` hoặc bố trí hàng ngang 3 điều khiển `Button` mang nhãn lần lượt là 'Start', 'Stop', và 'Reset'.\n"
                  "4. Căn chỉnh lề: Sử dụng đường Snap Lines để căn thẳng hàng các nút bấm và tạo khoảng cách đối xứng hai bên.",
        "solution": "Hướng dẫn từng bước thiết kế giao diện Stop Watch GUI:\n\n"
                    "**Bước 1: Thiết lập Form chính:**\n"
                    "- Mở Visual Studio, tạo dự án Windows Forms Application đặt tên `StopWatchGUI`.\n"
                    "- Chọn Form1, mở Properties Window (F4), đặt thuộc tính `Text` = `Stop Watch`.\n"
                    "- Đặt thuộc tính `Size` = `350, 220`, `StartPosition` = `CenterScreen`.\n\n"
                    "**Bước 2: Thêm màn hình hiển thị số RichTextBox:**\n"
                    "- Kéo thả điều khiển `RichTextBox` từ Toolbox vào nửa trên của Form.\n"
                    "- Đặt thuộc tính `Text` = `00:00:00`.\n"
                    "- Nhấp nút `[...]` ở thuộc tính `Font`: chọn phông `Segoe UI` (hoặc `Consolas`), kiểu `Bold`, cỡ chữ `28 pt`.\n"
                    "- Đặt thuộc tính `ReadOnly` = `True` (ngăn người dùng gõ sửa số).\n"
                    "- Đặt thuộc tính `Size` = `280, 60`, căn giữa theo chiều ngang của Form.\n\n"
                    "**Bước 3: Thêm các nút bấm điều khiển (Buttons):**\n"
                    "- Kéo 3 điều khiển `Button` vào nửa dưới của Form:\n"
                    "  + Button 1: `(Name)` = `btnStart`, `Text` = `Start`, `Size` = `80, 35`.\n"
                    "  + Button 2: `(Name)` = `btnStop`, `Text` = `Stop`, `Size` = `80, 35`.\n"
                    "  + Button 3: `(Name)` = `btnReset`, `Text` = `Reset`, `Size` = `80, 35`.\n"
                    "- Chọn cả 3 nút, vào menu `Format -> Align -> Middles` và `Format -> Horizontal Spacing -> Make Equal` để các nút thẳng hàng và cách đều nhau tăm tắp.\n\n"
                    "**Bước 4: Kiểm thử giao diện:**\n"
                    "- Nhấn phím `F5` để chạy ứng dụng ở Run Mode và kiểm tra độ sắc nét của giao diện.",
        "hints": "Mục 2.7 Deitel: RichTextBox cho phép hiển thị phông chữ lớn, đặt ReadOnly để người dùng không sửa số giờ.",
        "image": "extracted_images/fig2_36_stopwatch_gui.png",
        "code": "// Mã C# khởi tạo giao diện Form Stop Watch\n"
                "this.Text = \"Stop Watch\";\n"
                "this.ClientSize = new System.Drawing.Size(340, 180);\n\n"
                "// RichTextBox hiển thị đồng hồ\n"
                "RichTextBox rtbTimer = new RichTextBox();\n"
                "rtbTimer.Text = \"00:00:00\";\n"
                "rtbTimer.Font = new Font(\"Segoe UI\", 28, FontStyle.Bold);\n"
                "rtbTimer.Size = new Size(280, 65);\n"
                "rtbTimer.Location = new Point(30, 25);\n"
                "rtbTimer.ReadOnly = true;\n"
                "this.Controls.Add(rtbTimer);\n\n"
                "// Các nút bấm điều khiển\n"
                "Button btnStart = new Button() { Text = \"Start\", Location = new Point(30, 110), Size = new Size(80, 35) };\n"
                "Button btnStop = new Button() { Text = \"Stop\", Location = new Point(130, 110), Size = new Size(80, 35) };\n"
                "Button btnReset = new Button() { Text = \"Reset\", Location = new Point(230, 110), Size = new Size(80, 35) };\n"
                "this.Controls.AddRange(new Control[] { btnStart, btnStop, btnReset });"
    },
    # 2.8
    {
        "id": "2.8",
        "category": "project",
        "title": "Exercise 2.8: Đồ án Thiết kế Màn hình Đăng nhập (Login Form GUI)",
        "description": "Xây dựng giao diện đăng nhập chuẩn doanh nghiệp có Username, Password và nút kiểm ghi nhớ theo Hình 2.37 giáo trình Deitel.",
        "question": "Hãy thiết kế giao diện Màn hình Đăng nhập (Login Form) theo Hình 2.37 trong giáo trình Deitel:\n"
                  "1. Form: Đặt `Text` = 'Login Form', `BackColor` = tông màu ấm hài hòa.\n"
                  "2. Tiêu đề: Thêm Label tiêu đề lớn 'Please Sign In', phông `Bookman Old Style` (hoặc `Georgia`), `14.25 pt Bold`.\n"
                  "3. Nhãn & Hộp nhập liệu: Thêm Label 'User Name:' đi kèm `TextBox`, Label 'Password:' đi kèm `TextBox` (đặt thuộc tính `PasswordChar` = '*').\n"
                  "4. Tùy chọn: Thêm `CheckBox` với nhãn 'Remember me on this computer'.\n"
                  "5. Nút bấm: Thêm hai nút 'OK' và 'Cancel' ở phía dưới.",
        "solution": "Hướng dẫn chi tiết xây dựng Login Form GUI:\n\n"
                    "**Bước 1: Tùy biến thuộc tính Form:**\n"
                    "- Tạo dự án `LoginFormGUI`.\n"
                    "- Chọn Form, đặt `Text` = `Login Form`, `Size` = `380, 280`, `FormBorderStyle` = `FixedDialog`.\n"
                    "- Đặt `BackColor` = `Bisque` (hoặc `NavajoWhite` trong tab Web).\n\n"
                    "**Bước 2: Thêm nhãn tiêu đề chào mừng:**\n"
                    "- Kéo điều khiển `Label` đặt ở đỉnh Form, `Text` = `Please Sign In`.\n"
                    "- Font: `Bookman Old Style`, `14.25pt`, `Bold`.\n\n"
                    "**Bước 3: Thêm các điều khiển nhập thông tin:**\n"
                    "- Label 1: `Text` = `User Name:`, `Location` = `(30, 70)`.\n"
                    "- TextBox 1: `(Name)` = `txtUserName`, `Location` = `(130, 68)`, `Size` = `190, 25`.\n"
                    "- Label 2: `Text` = `Password:`, `Location` = `(30, 110)`.\n"
                    "- TextBox 2: `(Name)` = `txtPassword`, `Location` = `(130, 108)`, `Size` = `190, 25`, thiết lập thuộc tính `PasswordChar` = `*` để che dấu mật khẩu.\n\n"
                    "**Bước 4: Thêm CheckBox và Buttons:**\n"
                    "- CheckBox: `Text` = `Remember me on this computer`, `Location` = `(130, 145)`.\n"
                    "- Button OK: `Text` = `OK`, `Location` = `(130, 185)`, `Size` = `85, 30`.\n"
                    "- Button Cancel: `Text` = `Cancel`, `Location` = `(235, 185)`, `Size` = `85, 30`.\n\n"
                    "**Bước 5: Hoàn thiện:**\n"
                    "- Bấm `F5` chạy thử. Thử gõ vào ô Password để chiêm ngưỡng ký tự ngôi sao `*` xuất hiện an toàn!",
        "hints": "Mục 2.8 Deitel: Thuộc tính PasswordChar che mật khẩu; dùng Snap Lines để căn thẳng hàng hai TextBox.",
        "image": "extracted_images/fig2_37_login_form_gui.png",
        "code": "// Mã C# thiết kế giao diện Login Form\n"
                "this.Text = \"Login Form\";\n"
                "this.BackColor = Color.Bisque;\n"
                "this.ClientSize = new Size(360, 240);\n\n"
                "Label lblTitle = new Label() {\n"
                "    Text = \"Please Sign In\",\n"
                "    Font = new Font(\"Bookman Old Style\", 14.25f, FontStyle.Bold),\n"
                "    AutoSize = true,\n"
                "    Location = new Point(30, 20)\n"
                "};\n\n"
                "TextBox txtUser = new TextBox() { Location = new Point(130, 65), Width = 190 };\n"
                "TextBox txtPass = new TextBox() { Location = new Point(130, 105), Width = 190, PasswordChar = '*' };\n"
                "CheckBox chkRemember = new CheckBox() { Text = \"Remember me on this computer\", Location = new Point(130, 140), AutoSize = true };\n"
                "Button btnOK = new Button() { Text = \"OK\", Location = new Point(130, 180), Size = new Size(85, 30) };\n"
                "Button btnCancel = new Button() { Text = \"Cancel\", Location = new Point(235, 180), Size = new Size(85, 30) };\n\n"
                "this.Controls.AddRange(new Control[] { lblTitle, txtUser, txtPass, chkRemember, btnOK, btnCancel });"
    },
    # 2.9
    {
        "id": "2.9",
        "category": "project",
        "title": "Exercise 2.9: Đồ án Thiết kế Bàn phím Máy tính Bỏ túi (Calculator GUI)",
        "description": "Sử dụng các khung chứa Panel có viền Fixed3D để bài trí 20 nút bấm máy tính khoa học theo Hình 2.38 giáo trình Deitel.",
        "question": "Hãy tạo giao diện Bàn phím Máy tính Bỏ túi (Calculator GUI) theo Hình 2.38 trong giáo trình:\n"
                  "1. Form: Đặt `Text` = 'Calculator', kích thước khoảng `260, 240`.\n"
                  "2. Màn hình kết quả: Thêm `TextBox` ở đỉnh, đặt `Text` = '0', `TextAlign` = `Right` (căn lề phải), kích thước kéo dài theo chiều ngang.\n"
                  "3. Panel 1 (Số 0-9): Thêm Panel kích thước `90, 120`, đặt `BorderStyle` = `Fixed3D` (hiệu ứng lõm xuống), chứa các nút số 0-9 và dấu chấm.\n"
                  "4. Panel 2 (Toán tử): Thêm Panel kích thước `62, 120`, `BorderStyle` = `Fixed3D`, chứa các nút phép tính `*`, `/`, `-`, `+`, `=`.\n"
                  "5. Panel 3 (Xóa & Nguồn): Thêm Panel kích thước `54, 62`, `BorderStyle` = `Fixed3D`, chứa các nút `C`, `C/A`, `OFF`.\n"
                  "6. Kích thước nút: Nút số `23, 23`; nút '00' `52, 23`; nút 'OFF' `54, 23`; nút '+' kéo dài `23, 81`; nút 'C' và 'C/A' `44, 23`.",
        "solution": "Hướng dẫn chi tiết xây dựng Calculator GUI chuẩn mực:\n\n"
                    "**Bước 1: Khởi tạo Form và Màn hình TextBox:**\n"
                    "- Tạo dự án `CalculatorGUI`, đặt `Text` = `Calculator`, `ClientSize` = `240, 200`.\n"
                    "- Thêm `TextBox` ở tọa độ `(15, 15)`, `Width` = `210`.\n"
                    "- Trong Properties Window, chỉnh `Text` = `0`, `TextAlign` = `Right` (chữ số căn sát lề phải chuẩn máy tính).\n\n"
                    "**Bước 2: Tạo và phân bố 3 khung Panel chứa linh kiện:**\n"
                    "- *Panel Số (panelNumbers):* `Location` = `(15, 55)`, `Size` = `90, 120`, `BorderStyle` = `Fixed3D`.\n"
                    "- *Panel Toán tử (panelOperators):* `Location` = `(115, 55)`, `Size` = `62, 120`, `BorderStyle` = `Fixed3D`.\n"
                    "- *Panel Lệnh (panelCommands):* `Location` = `(185, 55)`, `Size` = `54, 120`, `BorderStyle` = `Fixed3D`.\n\n"
                    "**Bước 3: Đặt các nút bấm (Buttons) vào bên trong từng Panel:**\n"
                    "- Kéo các nút bấm thả trực tiếp vào bề mặt của từng Panel tương ứng.\n"
                    "- Đặt thuộc tính `Size` chuẩn theo giáo trình:\n"
                    "  + Các phím `0` đến `9`, dấu `.`, `*`, `/`, `-`, `=` có kích thước vuông vắn `23, 23`.\n"
                    "  + Phím `00` có kích thước ngang gấp đôi `52, 23`.\n"
                    "  + Phím `+` có kích thước dọc trải dài `23, 81`.\n"
                    "  + Phím `C` (Clear) và `C/A` (Clear All) có kích thước `44, 23`.\n"
                    "  + Phím `OFF` có kích thước `54, 23`.\n\n"
                    "**Bước 4: Kiểm thử giao diện:**\n"
                    "- Nhấn `F5` chạy thử. Các Panel lõm `Fixed3D` tạo hiệu ứng chiều sâu nổi khối cực kỳ đẹp mắt!",
        "hints": "Mục 2.9 Deitel: Panel giúp gom nhóm điều khiển logic; thuộc tính BorderStyle = Fixed3D tạo hiệu ứng khắc lõm chuyên nghiệp.",
        "image": "extracted_images/fig2_38_calculator_gui.png",
        "code": "// Mã C# xây dựng Calculator GUI bằng Panel\n"
                "this.Text = \"Calculator\";\n"
                "this.ClientSize = new Size(250, 190);\n\n"
                "TextBox txtDisplay = new TextBox() {\n"
                "    Text = \"0\",\n"
                "    TextAlign = HorizontalAlignment.Right,\n"
                "    Location = new Point(15, 12),\n"
                "    Width = 220\n"
                "};\n"
                "this.Controls.Add(txtDisplay);\n\n"
                "// 3 Khung Panel lõm Fixed3D\n"
                "Panel pnlNum = new Panel() { Location = new Point(15, 45), Size = new Size(90, 130), BorderStyle = BorderStyle.Fixed3D };\n"
                "Panel pnlOp = new Panel() { Location = new Point(115, 45), Size = new Size(65, 130), BorderStyle = BorderStyle.Fixed3D };\n"
                "Panel pnlCmd = new Panel() { Location = new Point(190, 45), Size = new Size(55, 130), BorderStyle = BorderStyle.Fixed3D };\n"
                "this.Controls.AddRange(new Control[] { pnlNum, pnlOp, pnlCmd });"
    },
    # 2.10
    {
        "id": "2.10",
        "category": "project",
        "title": "Exercise 2.10: Đồ án Thiết kế Đồng hồ Báo thức Điện tử (Alarm Clock GUI)",
        "description": "Kết hợp GroupBox tiêu đề, RadioButton loại trừ và màn hình Label số điện tử nền đen chữ bạc theo Hình 2.39 giáo trình Deitel.",
        "question": "Hãy thiết kế giao diện Đồng hồ Báo thức (Alarm Clock GUI) theo Hình 2.39 trong giáo trình:\n"
                  "1. Form: Đặt `Text` = 'Alarm Clock', `Font` = `Segoe UI 9pt`, `Size` = `438, 170`.\n"
                  "2. Bảng nút điều khiển: Bố trí 7 `Button` điều khiển chức năng ('Hour', 'Minute', 'Second', 'Alarm', 'Snooze'...) căn lề đối xứng.\n"
                  "3. Khung phân nhóm buổi: Thêm `GroupBox` có `Text` = 'AM/PM', kích thước `100, 50`, đặt ở chính giữa theo trục ngang.\n"
                  "4. Nút chọn buổi: Đặt hai `RadioButton` có nhãn 'AM' và 'PM' bên trong GroupBox.\n"
                  "5. Màn hình đồng hồ số điện tử: Thêm `Label` có `Text` = '00:00:00', `BorderStyle` = `Fixed3D`, `BackColor` = `Black`, `ForeColor` = `Silver` (trong tab Web), `Font` = `12pt Bold`.",
        "solution": "Hướng dẫn chi tiết xây dựng Alarm Clock GUI:\n\n"
                    "**Bước 1: Thiết lập Form chính:**\n"
                    "- Tạo dự án `AlarmClockGUI`, đặt `Text` = `Alarm Clock`, `Size` = `438, 170`.\n"
                    "- Đặt phông chữ mặc định của Form là `Segoe UI 9pt`.\n\n"
                    "**Bước 2: Thiết kế màn hình hiển thị đồng hồ LED số điện tử:**\n"
                    "- Kéo thả điều khiển `Label` vào Form, đặt `Text` = `00:00:00`.\n"
                    "- Đặt `BorderStyle` = `Fixed3D` (tạo khung màn hình LED lõm).\n"
                    "- Chuyển `BackColor` sang màu `Black` (đen tuyền).\n"
                    "- Chuyển `ForeColor` sang màu `Silver` (trong tab Web) để chữ số phát sáng nổi bật trên nền đen.\n"
                    "- Chỉnh `Font` = `12pt Bold`, căn lề `TextAlign` = `MiddleCenter`.\n\n"
                    "**Bước 3: Thêm GroupBox và RadioButton:**\n"
                    "- Kéo `GroupBox` từ Toolbox vào Form, đổi `Text` = `AM/PM`, đặt `Size` = `100, 50`.\n"
                    "- Kéo hai điều khiển `RadioButton` thả vào bên trong GroupBox: một nút `Text` = `AM`, một nút `Text` = `PM`.\n"
                    "- Lưu ý: RadioButton đặt trong cùng một GroupBox sẽ tự động có tính chất loại trừ lẫn nhau (chỉ được chọn 1 trong 2).\n\n"
                    "**Bước 4: Bố trí 7 nút bấm chức năng (Buttons):**\n"
                    "- Thêm các nút bấm chỉnh giờ, phút, giây, báo thức và nút Snooze hoãn báo thức xung quanh màn hình LED.\n"
                    "- Dùng tính năng Snap Lines để căn thẳng hàng các nút đối xứng hai bên.\n\n"
                    "**Bước 5: Chạy thử nghiệm:**\n"
                    "- Bấm `F5` chạy thử. Màn hình đồng hồ LED nền đen chữ bạc trông y hệt một chiếc đồng hồ điện tử thực thụ!",
        "hints": "Mục 2.10 Deitel: GroupBox hiển thị đường viền và tiêu đề; RadioButton cho phép chọn duy nhất 1 tùy chọn; màu Silver trên nền Black tạo phong cách đồng hồ số LED.",
        "image": "extracted_images/fig2_39_alarm_clock_gui.png",
        "code": "// Mã C# thiết kế Alarm Clock GUI\n"
                "this.Text = \"Alarm Clock\";\n"
                "this.ClientSize = new Size(420, 135);\n"
                "this.Font = new Font(\"Segoe UI\", 9);\n\n"
                "// Màn hình số LED điện tử\n"
                "Label lblDisplay = new Label() {\n"
                "    Text = \"00:00:00\",\n"
                "    BackColor = Color.Black,\n"
                "    ForeColor = Color.Silver,\n"
                "    Font = new Font(\"Segoe UI\", 12, FontStyle.Bold),\n"
                "    TextAlign = ContentAlignment.MiddleCenter,\n"
                "    BorderStyle = BorderStyle.Fixed3D,\n"
                "    Size = new Size(95, 35),\n"
                "    Location = new Point(160, 20)\n"
                "};\n\n"
                "// GroupBox AM/PM\n"
                "GroupBox grpAMPM = new GroupBox() {\n"
                "    Text = \"AM/PM\",\n"
                "    Size = new Size(100, 50),\n"
                "    Location = new Point(160, 65)\n"
                "};\n"
                "RadioButton rdoAM = new RadioButton() { Text = \"AM\", Location = new Point(10, 20), Width = 40, Checked = true };\n"
                "RadioButton rdoPM = new RadioButton() { Text = \"PM\", Location = new Point(55, 20), Width = 40 };\n"
                "grpAMPM.Controls.AddRange(new Control[] { rdoAM, rdoPM });\n\n"
                "this.Controls.AddRange(new Control[] { lblDisplay, grpAMPM });"
    },
    # 2.11
    {
        "id": "2.11",
        "category": "project",
        "title": "Exercise 2.11: Đồ án Thiết kế Máy Nghe Đài Bán Dẫn (Radio GUI)",
        "description": "Tích hợp đầy đủ các điều khiển phức hợp: 4 GroupBoxes, 6 Buttons cài kênh, 2 CheckBoxes loa, TrackBar âm lượng, RadioButton AM/FM và PictureBox nốt nhạc theo Hình 2.40 giáo trình Deitel.",
        "question": "Hãy tạo giao diện Máy Nghe Đài Radio (Radio GUI) theo Hình 2.40 trong giáo trình Deitel:\n"
                  "1. Form: Đặt `Text` = 'Radio', `Font` = `Segoe UI 9pt`, `Size` = `427, 194`.\n"
                  "2. Khung Pre-set Stations: GroupBox `180, 55` chứa 6 Button số `1` đến `6` (kích thước `23, 23`).\n"
                  "3. Khung Speakers: GroupBox `120, 55` chứa 2 CheckBox 'Rear' và 'Front'.\n"
                  "4. Nút nguồn: Button 'Power On/Off' kích thước `75, 55`.\n"
                  "5. Khung Volume Control: GroupBox `180, 70` chứa CheckBox 'Mute' và thanh trượt `TrackBar` chỉnh âm lượng.\n"
                  "6. Khung Tuning: GroupBox `120, 70` chứa Label tần số số '92.9' (nền Black, chữ Silver, 12pt bold) và 2 RadioButton 'AM', 'FM'.\n"
                  "7. Hình ảnh: Thêm PictureBox hiển thị linh vật nốt nhạc `MusicNote.gif` (`SizeMode` = `StretchImage`, kích thước `55, 70`).",
        "solution": "Hướng dẫn chi tiết xây dựng kiệt tác giao diện Radio GUI:\n\n"
                    "**Bước 1: Thiết lập Form chính:**\n"
                    "- Tạo dự án `RadioGUI`, đặt `Text` = `Radio`, `Size` = `427, 194`.\n"
                    "- Đặt phông chữ chung của Form là `Segoe UI 9pt`.\n\n"
                    "**Bước 2: Hàng điều khiển trên (Top row):**\n"
                    "- *GroupBox 'Pre-set Stations':* `Size` = `180, 55`, `Location` = `(15, 12)`. Bên trong đặt 6 nút bấm vuông kích thước `23, 23` mang nhãn `1, 2, 3, 4, 5, 6`.\n"
                    "- *GroupBox 'Speakers':* `Size` = `120, 55`, `Location` = `(205, 12)`. Bên trong đặt 2 `CheckBox` mang nhãn `Rear` và `Front`.\n"
                    "- *Nút 'Power On/Off':* `Size` = `75, 55`, `Location` = `(335, 12)`, `Text` = `Power On/Off`.\n\n"
                    "**Bước 3: Hàng điều khiển dưới (Bottom row):**\n"
                    "- *GroupBox 'Volume Control':* `Size` = `180, 75`, `Location` = `(15, 75)`. Đặt một `CheckBox` mang nhãn `Mute` và một thanh kéo `TrackBar` chỉnh âm lượng.\n"
                    "- *GroupBox 'Tuning':* `Size` = `120, 75`, `Location` = `(205, 75)`:\n"
                    "  + Thêm `Label` hiển thị đài `92.9`: `Size` = `50, 44`, `BackColor` = `Black`, `ForeColor` = `Silver`, `Font` = `12pt Bold`, `TextAlign` = `MiddleCenter`, `AutoSize` = `False`.\n"
                    "  + Thêm 2 `RadioButton` nhãn `AM` và `FM` đặt dọc bên cạnh nhãn số.\n"
                    "- *Khung ảnh PictureBox:* `Size` = `55, 75`, `Location` = `(345, 75)`. Đặt thuộc tính `SizeMode` = `StretchImage`, nạp hình ảnh nốt nhạc `MusicNote.gif` qua hộp thoại Select Resource.\n\n"
                    "**Bước 4: Kiểm thử và thưởng thức:**\n"
                    "- Nhấn phím `F5` để chạy ứng dụng. Kéo thanh trượt TrackBar, bấm các nút chọn đài và tận hưởng giao diện đầy sống động!",
        "hints": "Mục 2.11 Deitel: TrackBar tạo thanh kéo âm lượng; AutoSize = False của Label cho phép chỉnh kích thước tự do; SizeMode = StretchImage giúp ảnh nốt nhạc vừa vặn khung hình.",
        "image": "extracted_images/fig2_40_radio_gui.png",
        "code": "// Mã C# xây dựng Radio GUI hoàn chỉnh\n"
                "this.Text = \"Radio\";\n"
                "this.ClientSize = new Size(415, 160);\n"
                "this.Font = new Font(\"Segoe UI\", 9);\n\n"
                "// 1. GroupBox Pre-set Stations\n"
                "GroupBox grpStations = new GroupBox() { Text = \"Pre-set Stations\", Location = new Point(12, 10), Size = new Size(180, 60) };\n"
                "for (int i = 1; i <= 6; i++) {\n"
                "    grpStations.Controls.Add(new Button() { Text = i.ToString(), Size = new Size(24, 25), Location = new Point(10 + (i-1)*27, 22) });\n"
                "}\n\n"
                "// 2. GroupBox Speakers\n"
                "GroupBox grpSpeakers = new GroupBox() { Text = \"Speakers\", Location = new Point(200, 10), Size = new Size(120, 60) };\n"
                "grpSpeakers.Controls.Add(new CheckBox() { Text = \"Rear\", Location = new Point(10, 25), Width = 50 });\n"
                "grpSpeakers.Controls.Add(new CheckBox() { Text = \"Front\", Location = new Point(65, 25), Width = 50 });\n\n"
                "// 3. Power Button\n"
                "Button btnPower = new Button() { Text = \"Power On/Off\", Location = new Point(330, 15), Size = new Size(75, 55) };\n\n"
                "// 4. Volume Control & TrackBar\n"
                "GroupBox grpVol = new GroupBox() { Text = \"Volume Control\", Location = new Point(12, 75), Size = new Size(180, 75) };\n"
                "grpVol.Controls.Add(new CheckBox() { Text = \"Mute\", Location = new Point(10, 18), Width = 55 });\n"
                "grpVol.Controls.Add(new TrackBar() { Location = new Point(10, 40), Width = 160, Height = 25 });\n\n"
                "// 5. Tuning & Frequency Display\n"
                "GroupBox grpTune = new GroupBox() { Text = \"Tuning\", Location = new Point(200, 75), Size = new Size(120, 75) };\n"
                "Label lblFreq = new Label() {\n"
                "    Text = \"92.9\", AutoSize = false, Size = new Size(50, 42), Location = new Point(10, 22),\n"
                "    BackColor = Color.Black, ForeColor = Color.Silver, Font = new Font(\"Segoe UI\", 12, FontStyle.Bold),\n"
                "    TextAlign = ContentAlignment.MiddleCenter\n"
                "};\n"
                "grpTune.Controls.Add(lblFreq);\n"
                "grpTune.Controls.Add(new RadioButton() { Text = \"AM\", Location = new Point(65, 20), Width = 45 });\n"
                "grpTune.Controls.Add(new RadioButton() { Text = \"FM\", Location = new Point(65, 45), Width = 45, Checked = true });\n\n"
                "// 6. PictureBox MusicNote\n"
                "PictureBox picNote = new PictureBox() {\n"
                "    Location = new Point(340, 75), Size = new Size(60, 75),\n"
                "    SizeMode = PictureBoxSizeMode.StretchImage,\n"
                "    BorderStyle = BorderStyle.FixedSingle\n"
                "};\n\n"
                "this.Controls.AddRange(new Control[] { grpStations, grpSpeakers, btnPower, grpVol, grpTune, picNote });"
    }
]

# Output as JavaScript string
js_content = "// ============================================================================\n"
js_content += "// HỌC PHẦN: KỸ THUẬT LẬP TRÌNH (4 TÍN CHỈ) - IT26M\n"
js_content += "// BỘ DỮ LIỆU BÀI TẬP CUỐI CHƯƠNG 2: INTRODUCTION TO VISUAL STUDIO AND VISUAL PROGRAMMING\n"
js_content += "// (VISUAL C# HOW TO PROGRAM - DEITEL & DEITEL - CH.2, TRANG 99-104)\n"
js_content += "// GỒM: SELF-REVIEW EXERCISES (2.1 - 2.6) VÀ GUI DESIGN PROJECTS (2.7 - 2.11)\n"
js_content += "// ============================================================================\n"
js_content += "const EXERCISES_CHAPTER_02 = " + json.dumps(exercises, ensure_ascii=False, indent=2) + ";\n"

with open("js/exercises_ch02.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Generated {len(exercises)} exercises into js/exercises_ch02.js successfully!")

