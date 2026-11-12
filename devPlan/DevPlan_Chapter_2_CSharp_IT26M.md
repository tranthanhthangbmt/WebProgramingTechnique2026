# KẾ HOẠCH BÀI GIẢNG VÀ PHÁT TRIỂN SLIDE BÀI GIẢNG ĐẠI HỌC
## HỌC PHẦN: KỸ THUẬT LẬP TRÌNH / LẬP TRÌNH C# & .NET
### CHƯƠNG 2: INTRODUCTION TO VISUAL STUDIO AND VISUAL PROGRAMMING
**Đối tượng:** Lớp IT26M (Khóa 2026 -- Khoa Công nghệ Thông tin)  
**Thời lượng:** 01 buổi (03 tiết = 150 phút, kết hợp lý thuyết và thực hành tại chỗ)  
**Tài liệu tham khảo chính:** Textbook *Visual C# How to Program* (Deitel & Deitel) -- Chapter 2: *Introduction to Visual Studio and Visual Programming*  
**Định dạng sản phẩm:** Slide LaTeX Beamer $\to$ Biên dịch PDF chuẩn học thuật quốc tế (XeLaTeX, font Arial/Consolas)  
**Thư mục lưu trữ:** `Slides_CShape/`

---

## I. MỤC TIÊU BÀI HỌC (COURSE LEARNING OUTCOMES - CLOs)

Kết thúc buổi học 3 tiết này, sinh viên lớp IT26M có khả năng:

| Mã CLO | Mô tả chuẩn đầu ra | Thang đo Bloom |
| :--- | :--- | :--- |
| **CLO 2.1** | Giải thích được vai trò của Môi trường phát triển tích hợp (IDE - Integrated Development Environment) và triết lý Lập trình trực quan (Visual Programming / RAD - Rapid Application Development) trong công nghiệp phần mềm hiện đại. | Level 2 (Understand) |
| **CLO 2.2** | Khởi tạo, cấu hình và quản trị dự án phần mềm với mẫu Windows Forms Application; hiểu rõ vai trò và mối liên hệ giữa các tệp `.sln`, `.csproj`, `Form.cs`, `Form.Designer.cs`, `Program.cs`. | Level 3 (Apply) |
| **CLO 2.3** | Sử dụng thành thạo thanh Menu Bar, Standard Toolbar, phím tắt và kỹ thuật điều hướng không gian làm việc (Auto-Hide, Pinning, Docking windows, phím F1 Context-Sensitive Help). | Level 3 (Apply) |
| **CLO 2.4** | Phân tích và tương tác với các cửa sổ nòng cốt trong IDE: Solution Explorer, Toolbox (nhóm Common Controls), và Properties Window (thiết lập Design-Time properties, xem A-Z vs Categorized). | Level 4 (Analyze) |
| **CLO 2.5** | Vận dụng kỹ thuật kéo-thả trực quan để xây dựng ứng dụng hoàn chỉnh `ASimpleApp` (chứa Form, Label, PictureBox với tài nguyên hình ảnh), tùy biến màu sắc, font chữ, căn lề và thực thi ở Run Mode (F5 / Ctrl+F5). | Level 3 (Apply / Create) |

---

## II. MA TRẬN PHÂN BỔ THỜI GIAN & TIẾN TRÌNH DẠY HỌC (3 TIẾT)

Tổng thời lượng: 150 phút (3 tiết học đại học tích hợp, giải lao giữa giờ).

```text
========================================================================================
TIẾT 1 (50'): TỔNG QUAN VISUAL STUDIO IDE, CẤU TRÚC DỰ ÁN & MENU / TOOLBAR
- 05': Khởi động buổi học, kết nối từ Chương 1 sang Chương 2, công bố 5 CLOs (CLO 2.1 - 2.5)
- 15': Khái niệm IDE, RAD và Lập trình trực quan (Visual Programming vs Console CLI)
- 15': Màn hình Start Page (Hình 2.1), New Project Dialog (Hình 2.3), mẫu Windows Forms App
- 15': Thanh Menu Bar (Hình 2.5, 2.6), Standard Toolbar (Hình 2.7, 2.8), Tooltips (Hình 2.9), F1 Help
- 10': [THỰC HÀNH 1] Khởi động Visual Studio, tạo Solution đầu tiên và khảo sát thanh công cụ
----------------------------------------------------------------------------------------
TIẾT 2 (50'): ĐIỀU HƯỚNG CỬA SỔ IDE, SOLUTION EXPLORER, TOOLBOX & PROPERTIES WINDOW
- 10': Kỹ thuật điều hướng không gian làm việc: Auto-Hide, Pinning, Docking (Hình 2.10, 2.11, 2.12)
- 15': Cửa sổ Solution Explorer: Cấu trúc phân cấp Solution, Project, References, Files (Hình 2.13, 2.14)
- 10': Cửa sổ Toolbox: Khám phá nhóm Common Controls (Button, Label, TextBox, PictureBox - Hình 2.15)
- 15': Cửa sổ Properties Window: Thuộc tính Design-Time, Categorized vs Alphabetical (Hình 2.16)
- 10': [THỰC HÀNH 2] Checkpoint Quiz & Bài tập sắp xếp cửa sổ, tùy biến thuộc tính Form
----------------------------------------------------------------------------------------
TIẾT 3 (50'): CASE STUDY THỰC HÀNH `ASimpleApp` (TEXT & IMAGE) & KIỂM THỬ ỨNG DỤNG
- 05': Giới thiệu Case Study `ASimpleApp`: Kiến trúc ứng dụng đồ họa hiển thị văn bản & hình ảnh
- 10': Bước 1 - 3: Tạo dự án, tùy biến Form (Text, Sizing Handles, BackColor - Hình 2.18 đến 2.23)
- 10': Bước 4 - 5: Thêm điều khiển Label, đổi Font, căn lề MiddleCenter (Hình 2.24 đến 2.28)
- 10': Bước 6 - 8: Thêm điều khiển PictureBox, nạp ảnh Resource, thiết lập SizeMode (Hình 2.29 đến 2.34)
- 10': Chạy thử ứng dụng: Phân biệt Design Mode vs Run Mode (F5 vs Ctrl+F5 - Hình 2.35)
- 20': [THỰC HÀNH 3] Hands-on Lab: Sinh viên tự tay xây dựng hoàn chỉnh `ASimpleApp` trên máy tính
- 05': Tổng kết checklist chuẩn đầu ra, giới thiệu 5 đồ án GUI bài tập cuối chương (Hình 2.36 - 2.40)
========================================================================================
```

---

## III. BẢN ĐỒ CÁC HÌNH ẢNH TRÍCH XUẤT TỪ SÁCH GIÁO KHOA

Tất cả các hình ảnh được trích xuất chất lượng cao từ file PDF gốc `textbook_CShape/Chapter_02.pdf` và lưu tại `Slides_CShape/images/`:

| Mã file hình ảnh | Số trang SGK | Tên hình trong SGK | Nội dung & Vai trò trong bài giảng |
| :--- | :---: | :--- | :--- |
| `fig2_01_start_page.png` | Trang 3 | Fig. 2.1: Start Page | Màn hình khởi động Visual Studio, danh sách dự án gần đây |
| `fig2_03_new_project_dialog.png` | Trang 5 | Fig. 2.3: New Project dialog | Hộp thoại tạo dự án mới, chọn Windows Forms Application |
| `fig2_04_design_view.png` | Trang 6 | Fig. 2.4: Design view of IDE | Khung nhìn thiết kế trực quan Design View với Form rỗng |
| `fig2_05_menu_bar.png` | Trang 7 | Fig. 2.5: Visual Studio menu bar | Thanh Menu Bar đầy đủ với 10 mục thực đơn chính |
| `fig2_07_standard_toolbar.png` | Trang 8 | Fig. 2.7: Standard toolbar | Thanh công cụ chuẩn chứa các nút lệnh thường dùng |
| `fig2_10_autohide.png` | Trang 10 | Fig. 2.10: Auto-hide feature | Minh họa tính năng tự động ẩn cửa sổ tiết kiệm không gian |
| `fig2_11_hidden_toolbox.png` | Trang 10 | Fig. 2.11: Hidden Toolbox | Hiển thị cửa sổ Toolbox dạng trượt khi bật Auto-Hide |
| `fig2_12_pinning_window.png` | Trang 11 | Fig. 2.12: Pinning down window | Tắt Auto-Hide bằng nút ghim (Pin icon) để cố định cửa sổ |
| `fig2_13_solution_explorer.png` | Trang 11 | Fig. 2.13: Solution Explorer | Cây phân cấp Solution, Project, Form1.cs và Program.cs |
| `fig2_14_solution_explorer_references.png` | Trang 12 | Fig. 2.14: References node | Nút References quản lý các thư viện liên kết FCL |
| `fig2_15_toolbox_common_controls.png` | Trang 13 | Fig. 2.15: Toolbox Common Controls | Danh sách điều khiển đồ họa thông dụng kéo-thả |
| `fig2_16_properties_window.png` | Trang 14 | Fig. 2.16: Properties window | Cửa sổ cấu hình thuộc tính của điều khiển đang chọn |
| `fig2_17_simple_app_executing.png` | Trang 15 | Fig. 2.17: Simple app executing | Mục tiêu thành phẩm: Ứng dụng `ASimpleApp` khi chạy |
| `fig2_18_new_project_asimpleapp.png` | Trang 16 | Fig. 2.18: New Project ASimpleApp | Thiết lập tên dự án `ASimpleApp` và đường dẫn lưu |
| `fig2_19_form_text_property.png` | Trang 16 | Fig. 2.19: Setting Form Text | Đổi tiêu đề Form qua thuộc tính `Text` trong Properties |
| `fig2_20_form_title_sizing.png` | Trang 17 | Fig. 2.20: Form with updated title | Form với tiêu đề mới và các điểm mút thay đổi kích thước |
| `fig2_21_resizing_form.png` | Trang 17 | Fig. 2.21: Resizing the Form | Thao tác kéo rê chuột vào sizing handle để mở rộng Form |
| `fig2_22_form_backcolor.png` | Trang 18 | Fig. 2.22: Changing Form BackColor| Bảng chọn màu Color Palette đổi màu nền Form |
| `fig2_23_form_new_backcolor.png` | Trang 18 | Fig. 2.23: Form new BackColor | Form sau khi được áp dụng màu nền `LightCyan` |
| `fig2_24_adding_label.png` | Trang 19 | Fig. 2.24: Adding Label to Form | Thao tác kéo thả điều khiển Label từ Toolbox vào Form |
| `fig2_25_gui_form_label.png` | Trang 19 | Fig. 2.25: GUI Form and Label | Form sau khi đã có Label với nội dung văn bản mới |
| `fig2_26_label_font_property.png` | Trang 20 | Fig. 2.26: Label Font property | Nút mở rộng `...` trên thuộc tính `Font` của Label |
| `fig2_27_font_dialog.png` | Trang 20 | Fig. 2.27: Font dialog | Hộp thoại chọn Font chữ, kiểu chữ Bold và kích cỡ 24pt |
| `fig2_28_centering_label.png` | Trang 21 | Fig. 2.28: Centering Label text | Thiết lập thuộc tính `TextAlign` thành `MiddleCenter` |
| `fig2_29_inserting_picturebox.png` | Trang 21 | Fig. 2.29: Inserting PictureBox | Thêm điều khiển PictureBox và căn bằng đường Snap Lines |
| `fig2_30_picturebox_image_prop.png` | Trang 22 | Fig. 2.30: Image property | Thiết lập thuộc tính `Image` của PictureBox |
| `fig2_31_select_resource_dialog.png` | Trang 22 | Fig. 2.31: Select Resource | Hộp thoại chọn tệp hình ảnh tài nguyên Project Resource |
| `fig2_33_scaling_image.png` | Trang 23 | Fig. 2.33: Scaling image | Chọn chế độ hiển thị `SizeMode` = `StretchImage` |
| `fig2_34_picturebox_displaying.png` | Trang 23 | Fig. 2.34: PictureBox displaying | Hình ảnh linh vật chú bọ được hiển thị vừa vặn trong khung |
| `fig2_35_ide_run_mode.png` | Trang 24 | Fig. 2.35: IDE in run mode | Trạng thái IDE khi ứng dụng đang chạy ở Run Mode |
| `fig2_36_stopwatch_gui.png` | Trang 29 | Fig. 2.36: Stop Watch GUI | Đồ án bài tập 2.7: Thiết kế giao diện Đồng hồ bấm giờ |
| `fig2_37_login_form_gui.png` | Trang 29 | Fig. 2.37: Login Form GUI | Đồ án bài tập 2.8: Thiết kế giao diện Đăng nhập hệ thống |
| `fig2_38_calculator_gui.png` | Trang 30 | Fig. 2.38: Calculator GUI | Đồ án bài tập 2.9: Thiết kế giao diện Máy tính bỏ túi |
| `fig2_39_alarm_clock_gui.png` | Trang 30 | Fig. 2.39: Alarm Clock GUI | Đồ án bài tập 2.10: Thiết kế giao diện Đồng hồ báo thức |
| `fig2_40_radio_gui.png` | Trang 31 | Fig. 2.40: Radio GUI | Đồ án bài tập 2.11: Thiết kế giao diện Máy nghe Radio |

---

## IV. BỐ CỤC 44 SLIDE BÀI GIẢNG LATEX BEAMER

* **Theme:** Chuẩn Beamer Madrid Widescreen 16:9 (`aspectratio=169, 10pt`).
* **Bảng màu nhận diện học thuật:**
  * `Primary Navy` (`#0F2C59`): Màu chủ đạo học thuật đại học.
  * `Slate Blue` (`#1D5D9B`): Màu phụ và tiêu đề khối nội dung.
  * `CSharp Purple` (`#68217A`): Màu nhận diện đặc trưng của ngôn ngữ C# và Visual Studio.
  * `Accent Orange` (`#E17012`): Dành cho các câu hỏi Checkpoint, cảnh báo.
  * `Practice Green` (`#1E8449`): Dành cho các bài Hands-on Labs.
* **Cấu hình mã nguồn:** Package `listings` cấu hình syntax highlighting cho C# và Windows Forms code.

### Danh mục 44 Slide chi tiết:

#### PHẦN MỞ ĐẦU (Slides 1 - 4)
* **Slide 1:** Tiêu đề bài giảng: KỸ THUẬT LẬP TRÌNH C# -- CHƯƠNG 2 (Lớp IT26M, Khóa 2026).
* **Slide 2:** Mục tiêu bài học & Ma trận 5 Chuẩn đầu ra (CLO 2.1 -- 2.5).
* **Slide 3:** Tiến trình bài học 3 tiết (150 phút tích hợp lý thuyết và thực hành).
* **Slide 4:** Khởi động & Câu hỏi định hướng: Tại sao lập trình trực quan lại thay đổi ngành phần mềm?

#### TIẾT 1: TỔNG QUAN VISUAL STUDIO IDE, CẤU TRÚC DỰ ÁN & MENU / TOOLBAR (Slides 5 - 17)
* **Slide 5:** Phân đoạn Tiết 1: Tổng quan Visual Studio IDE & Thanh công cụ.
* **Slide 6:** Khái niệm IDE & Sự tiến hóa từ CLI sang Visual Programming.
* **Slide 7:** Triết lý RAD (Rapid Application Development) trong C# & Windows Forms.
* **Slide 8:** Khởi động Visual Studio & Màn hình Start Page (Hình 2.1).
* **Slide 9:** Hộp thoại New Project Dialog & Mẫu Windows Forms Application (Hình 2.3).
* **Slide 10:** Khảo sát Giao diện Thiết kế Design View (Hình 2.4).
* **Slide 11:** Thanh Menu Bar -- Tổng quan các menu chức năng (Hình 2.5, 2.6).
* **Slide 12:** Phân tích chức năng các Menu: File, Edit, View, Project, Build, Debug, Format.
* **Slide 13:** Thanh Công cụ Chuẩn Standard Toolbar (Hình 2.7, 2.8).
* **Slide 14:** Tính năng Tooltips & Phím tắt hữu ích trong IDE (Hình 2.9).
* **Slide 15:** Hệ thống Trợ giúp Context-Sensitive Help & Phím F1 (Hình 2.2).
* **Slide 16:** [CHECKPOINT 1] Trắc nghiệm củng cố Tiết 1 (IDE, Menu, Phím tắt).
* **Slide 17:** [HANDS-ON LAB 1] Tạo dự án đầu tiên & Khảo sát giao diện Visual Studio.

#### TIẾT 2: ĐIỀU HƯỚNG CỬA SỔ IDE, SOLUTION EXPLORER, TOOLBOX & PROPERTIES (Slides 18 - 29)
* **Slide 18:** Phân đoạn Tiết 2: Điều hướng IDE, Solution Explorer, Toolbox & Properties.
* **Slide 19:** Tính năng Auto-Hide & Nút ghim cửa sổ Pin Icon (Hình 2.10, 2.11, 2.12).
* **Slide 20:** Kỹ thuật Docking, Tách tab và Quản lý Layout cửa sổ trong Visual Studio.
* **Slide 21:** Cửa sổ Solution Explorer: Cấu trúc phân cấp Solution & Project (Hình 2.13).
* **Slide 22:** Chi tiết các tệp: `.sln`, `.csproj`, `Form.cs`, `Form.Designer.cs`, `Program.cs`.
* **Slide 23:** Nút References: Quản lý thư viện phụ thuộc và Assemblies (Hình 2.14).
* **Slide 24:** Cửa sổ Toolbox: Tổng quan kho linh kiện điều khiển GUI.
* **Slide 25:** Nhóm Common Controls: Button, Label, TextBox, PictureBox... (Hình 2.15).
* **Slide 26:** Cửa sổ Properties Window: Xem và thiết lập thuộc tính Design-Time (Hình 2.16).
* **Slide 27:** Hai chế độ xem Properties: Alphabetical vs Categorized & Hộp Description.
* **Slide 28:** [CHECKPOINT 2] Trắc nghiệm củng cố Tiết 2 (Solution Explorer, Toolbox, Properties).
* **Slide 29:** [HANDS-ON LAB 2] Sắp xếp không gian làm việc & Tùy biến thuộc tính Form.

#### TIẾT 3: CASE STUDY THỰC HÀNH `ASimpleApp` (TEXT & IMAGE) & KIỂM THỬ (Slides 30 - 43)
* **Slide 30:** Phân đoạn Tiết 3: Case Study Thực hành `ASimpleApp` & Kiểm thử GUI.
* **Slide 31:** Giới thiệu Case Study: Ứng dụng đồ họa `ASimpleApp` (Hình 2.17).
* **Slide 32:** Phân tích kiến trúc giao diện `ASimpleApp` (Form, Label, PictureBox).
* **Slide 33:** Bước 1: Khởi tạo dự án `ASimpleApp` trong Visual Studio (Hình 2.18).
* **Slide 34:** Bước 2: Tùy biến Form -- Thuộc tính `Text` & Sizing Handles (Hình 2.19, 2.20, 2.21).
* **Slide 35:** Bước 3: Tùy biến Form -- Bảng màu chọn `BackColor` (Hình 2.22, 2.23).
* **Slide 36:** Bước 4: Thêm điều khiển Label & Đổi `Text` ("Welcome to Visual C#!") (Hình 2.24, 2.25).
* **Slide 37:** Bước 5: Tùy biến Label -- Hộp thoại Font Dialog & Căn lề `TextAlign` (Hình 2.26, 2.27, 2.28).
* **Slide 38:** Bước 6: Thêm điều khiển PictureBox & Căn chỉnh Snap Lines (Hình 2.29, 2.30).
* **Slide 39:** Bước 7: Nạp ảnh Project Resource & Thuộc tính `SizeMode` (Hình 2.31, 2.33, 2.34).
* **Slide 40:** Bước 8: Khởi chạy và Phân biệt Chế độ Design Mode vs Run Mode (Hình 2.35).
* **Slide 41:** [HANDS-ON LAB 3] Thực hành xây dựng hoàn chỉnh ứng dụng `ASimpleApp` (20 phút).
* **Slide 42:** [CHECKPOINT 3] Trắc nghiệm tổng kết Chương 2 (Properties, Controls, Run Mode).
* **Slide 43:** Tổng kết Checklist Chuẩn đầu ra (CLO 2.1 - 2.5) & Nhiệm vụ tự học.

#### TỔNG KẾT & BÀI TẬP VỀ NHÀ (Slide 44)
* **Slide 44:** Giới thiệu 5 Đồ án thiết kế GUI bài tập cuối chương (Stop Watch, Login, Calculator, Alarm Clock, Radio - Hình 2.36 - 2.40) & Chuẩn bị Chương 3.

---

## V. QUY TRÌNH BIÊN DỊCH VÀ XUẤT BẢN

```bash
# Di chuyển vào thư mục Slides_CShape
cd "I:\Course_UDA\Kỹ thuật lập trình\ebooks\new ebooks\WebProgramingTechnique2026\Slides_CShape"

# Biên dịch bằng xelatex (2 lần để đồng bộ trang, nav và toc)
xelatex -interaction=nonstopmode Chapter_2_Visual_Studio_and_Visual_Programming_IT26M.tex
xelatex -interaction=nonstopmode Chapter_2_Visual_Studio_and_Visual_Programming_IT26M.tex
```

---

## VI. DANH MỤC PHÂN CHIA SLIDE THEO CẤU TRÚC PX_... (MỖI PHẦN KHÔNG QUÁ 15 SLIDES)

Nhằm tối ưu hóa cho việc trình chiếu, in ấn và nạp vào các nền tảng giảng dạy trực tuyến, toàn bộ 47 slide của Chương 2 được chia nhỏ thành **4 phần chuẩn hóa**, mỗi phần đều đảm bảo **$\le 15$ slide**:

| Tên tệp tin xuất bản (`PX_...`) | Số trang | Số slide | Nội dung & Chủ đề sư phạm |
| :--- | :---: | :---: | :--- |
| **`P1_Chapter02_Tong_Quan_IDE_va_Menus.pdf`**<br>*(hoặc `P1_Chapter02.pdf`)* | Trang 1 -- 12 | **12 slide** ($\le 15$) | **Tổng quan IDE, Triết lý RAD & Menu Bar:** Khởi động, CLOs 2.1 - 2.5, Start Page, New Project WinForms, Design View, phân tích hệ thống Menu Bar (Build, Debug, Format). |
| **`P2_Chapter02_Dieu_Huong_va_Solution_Explorer.pdf`**<br>*(hoặc `P2_Chapter02.pdf`)* | Trang 13 -- 24 | **12 slide** ($\le 15$) | **Thanh Công cụ, Phím tắt, Điều hướng & Solution Explorer:** Standard Toolbar, F1 Help, Checkpoint 1, Lab 1, Auto-Hide, Pinning, Docking, Solution Explorer (.sln, .csproj, Form.Designer.cs, References). |
| **`P3_Chapter02_Toolbox_Properties_va_Form.pdf`**<br>*(hoặc `P3_Chapter02.pdf`)* | Trang 25 -- 36 | **12 slide** ($\le 15$) | **Toolbox, Properties Window & Khởi tạo Form:** Common Controls (Button, Label, PictureBox), Properties Window (Categorized vs A-Z), Checkpoint 2, Lab 2, khởi tạo Case Study `ASimpleApp` (Form Text, BackColor). |
| **`P4_Chapter02_ASimpleApp_va_Do_An_GUI.pdf`**<br>*(hoặc `P4_Chapter02.pdf`)* | Trang 37 -- 47 | **11 slide** ($\le 15$) | **Case Study ASimpleApp Hoàn thiện & 5 Đồ án GUI:** Thêm Label, Font Dialog 24pt Bold, TextAlign MiddleCenter, PictureBox Snap Lines, nạp ảnh Resource, SizeMode StretchImage, Run Mode, Lab 3, Checkpoint 3, 5 Đồ án GUI cuối chương. |

---

## VII. KỊCH BẢN THUYẾT MINH SONG SONG (`script.txt`) CHO VIDEO & SLIDE PLAYER

Đã hoàn thành biên soạn tệp kịch bản thuyết minh hội thoại hai chiều (Thầy & Trò) cho toàn bộ 45 slide của Chương 2 tại:
`VideoCShape\Chapter_02\script.txt` (62,135 bytes, chuẩn UTF-8).

* **Cấu trúc kịch bản:**
  - Bám sát 100% cấu trúc của `scriptDemo.txt`.
  - Mỗi slide gồm tiêu đề chuẩn: `Slide X: <Tiêu đề>`
  - Lời thoại `Người 1:` (Giảng viên) truyền tải kiến thức sư phạm chuyên sâu, giải thích cơ chế, định hướng tư duy kỹ sư phần mềm.
  - Lời thoại `Người 2:` (Sinh viên IT26M) phản hồi, tương tác, đặt câu hỏi đúng trọng tâm kỹ thuật và đúc kết bài học.
  - Các slide phân tách nhau bằng đúng một dòng trống (`\n\n`), bên trong slide các lượt thoại ngăn cách bằng xuống dòng đơn (`\n`).

---

## VIII. TÍCH HỢP TOÀN DIỆN VÀO CỔNG THÔNG TIN HỌC TẬP TRỰC TUYẾN (WEB PORTAL)

Cổng thông tin môn học tại `index.html` đã được nâng cấp toàn diện lên kiến trúc **Đa chương học (Multi-Chapter Dynamic Controller)**, hỗ trợ chuyển đổi mượt mà giữa Chương 1 và Chương 2 thông qua dropdown `chapterSelector`:

### 1. Đồng bộ hóa 6 Tab chức năng cho Chương 2:
- **Tab 1: Đề cương & Lộ trình:** Hiển thị thông tin học phần 4 tín chỉ, 5 chuẩn đầu ra CLO 2.1 -- CLO 2.5 và lộ trình tích hợp 3 tiết (150 phút).
- **Tab 2: Tài liệu & Tài nguyên:** Liên kết tải trực tiếp giáo trình `textbook_CShape/Chapter_02.pdf`, slide tổng `VideoCShape/Chapter_02/slideChapter_02.pdf` và 4 tập slide phân nhỏ `P1_...` đến `P4_...` chuẩn $\le 15$ slides.
- **Tab 3: Video & Slide Player (Đã khắc phục đồng bộ iframe):**
  - Tích hợp hàm `updateVideoTab(ch)` trong `js/app.js` tự động cập nhật `chapterVideoIframe.src` trỏ chính xác về `./VideoCShape/Chapter_02/index.html`.
  - Đồng bộ 45 slide chất lượng cao (`images/slide-1.png` $\to$ `slide-45.png`), 45 audio giọng đọc AI thuyết minh (`audio/slide_1.mp3` $\to$ `slide_45.mp3`), tiến trình thời gian và số slide hiển thị chính xác `1 / 45`.
  - Cập nhật toàn bộ các nút liên kết (`📄 Mở slideChapter_02.pdf`, `📥 Tải slideChapter_02.pdf`, `📥 Tải Script (.txt)` từ `VideoCShape/Chapter_02/script.txt`).
  - Hỗ trợ cả 2 chế độ: Rạp chiếu toàn màn hình (Theater View) và Trình duyệt đối chiếu từng trang (Split View).
- **Tab 4: Trắc nghiệm chuẩn hóa (40 câu):** Ngân hàng 40 câu hỏi trắc nghiệm `QUIZ_CHAPTER_02` bám sát giáo trình Deitel & Deitel; cân bằng tuyệt đối 10 A, 10 B, 10 C, 10 D; độ dài đáp án ngẫu nhiên triệt tiêu hoàn toàn thiên vị; gắn nhãn Bloom và giải thích chuyên sâu.
- **Tab 5: Bài tập cuối chương (Đã chuẩn hóa toàn diện cấu trúc & hình ảnh):**
  - **Khắc phục lỗi hiển thị ảnh:** Phân biệt chính xác giữa các bài tập lý thuyết (Self-Review 2.1 -- 2.6 không có hình trong textbook, thiết lập `image: null`) và 5 Đồ án GUI 2.7 -- 2.11 (Stop Watch, Login Form, Calculator, Alarm Clock, Radio có hình ảnh thực tế `fig2_36_*.png` đến `fig2_40_*.png`). Thêm cơ chế tự động ẩn `onerror` bảo vệ UI.
  - **Khắc phục lỗi undefined:** Chuẩn hóa các trường dữ liệu `number` (*Self-Review 2.1*, *Exercise 2.3*...), `page` (*Trang 100, 101, 102, 103*), `type` (*self-review, exercises, making-a-difference*), `solutionCode` / `answer`, `hint` và `starterCode`.
  - Hiển thị đầy đủ nội dung bài tập, gợi ý, khung code khởi tạo C# và lời giải phân tích chi tiết.
- **Tab 6: Kho mã nguồn C#:** Toàn bộ mã nguồn C# Windows Forms chuẩn mực (.NET 8): `Form1.cs`, `Form1.Designer.cs`, `Program.cs`, `CalculatorGUI.cs` có nút 1-click sao chép.

### 3. Hệ thống làm bài tập tương tác & Chấm điểm tự động trên Web (Interactive Exercises Engine):
Chuyển đổi hoàn toàn phương thức học từ **"chỉ xem đáp án thụ động"** sang **"tương tác làm bài trực tiếp & kiểm tra kết quả Đúng / Sai"**:
- **Tệp mở rộng `js/interactive_exercises.js`:**
  - **Dạng Điền vào chỗ trống (`fill-blank` - ví dụ Self-Review 2.1, Exercise 2.3...):** Nhúng trực tiếp ô nhập `<input>` vào từng vị trí chỗ trống `_______` trong câu; thuật toán chuẩn hóa không dấu/chữ thường linh hoạt so khớp từ khóa tiếng Anh/tiếng Việt; tự động đánh dấu viền xanh lá `✅ Chính xác!` hoặc đỏ `❌ Chưa đúng` kèm đáp án chuẩn và phân tích Deitel.
  - **Dạng Nhận định Đúng / Sai (`true-false` - ví dụ Self-Review 2.2, Exercise 2.4...):** Cung cấp các nút chip bấm chọn `[ ✓ Đúng (True) ]` và `[ ✕ Sai (False) ]`; kiểm tra kết quả ngay lập tức và giải thích cặn kẽ bản chất kỹ thuật cho từng nhận định.
  - **Dạng Thuật ngữ & Tự luận (`concepts` - ví dụ Exercise 2.5, 2.6):** Soạn thảo trực tiếp định nghĩa; phân tích tỷ lệ xuất hiện của các từ khóa chuyên ngành cốt lõi và hiển thị định nghĩa chuẩn học thuật song song.
  - **Dạng Đồ án GUI & Viết mã C# (`gui-project` - ví dụ Exercise 2.7 đến 2.11):** Bảng kiểm (Checklist) tiến độ từng bước thiết kế trong Visual Studio; Trình kiểm tra mã nguồn C# tự động phân tích điều khiển, thuộc tính và sự kiện (RichTextBox, ReadOnly, Button, TrackBar...).
  - **Banner tổng kết điểm số:** Tự động tính số câu đúng (ví dụ: `9/10 câu đúng (90%)`), xếp loại (*Xuất sắc / Khá tốt / Cần ôn tập*) và lưu trạng thái vào `localStorage` của trình duyệt.
  - **Hỗ trợ đầy đủ phím Enter và Responsive di động:** Bấm Enter tự động chuyển sang câu tiếp theo; co dãn 100% chiều ngang màn hình điện thoại.
- `js/chapter_data.js`: Quản lý metadata và template HTML động cho từng chương (`CHAPTER_METADATA`).
- `js/transcripts_ch01.js` & `js/transcripts_ch02.js`: Lưu trữ toàn bộ kịch bản thuyết minh cho từng chương.
- `js/quiz_data.js`: Chứa ngân hàng trắc nghiệm chuẩn hóa `QUIZ_CHAPTER_01` và `QUIZ_CHAPTER_02`.
- `js/exercises_data.js`: Chứa ngân hàng bài tập và đồ án `EXERCISES_CHAPTER_01` và `EXERCISES_CHAPTER_02`.
- `js/app.js`: Bộ điều khiển trung tâm (`switchChapter(ch)`, `renderSlide()`, `playSlideAudio()`, `initQuizEngine()`, `initExerciseHub()`).




