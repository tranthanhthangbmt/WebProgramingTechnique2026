# KẾ HOẠCH BÀI GIẢNG VÀ PHÁT TRIỂN SLIDE BÀI GIẢNG ĐẠI HỌC
## HỌC PHẦN: KỸ THUẬT LẬP TRÌNH / LẬP TRÌNH C# & .NET
### CHƯƠNG 1: INTRODUCTION TO COMPUTERS, THE INTERNET AND VISUAL C#
**Đối tượng:** Lớp IT26M (Khóa 2026 -- Khoa Công nghệ Thông tin)  
**Thời lượng:** 01 buổi (03 tiết = 150 phút, kết hợp lý thuyết và thực hành tại chỗ)  
**Tài liệu tham khảo chính:** Textbook *Visual C# How to Program* (Deitel & Deitel) -- Chapter 1: *Introduction to Computers, the Internet and Visual C#*  
**Định dạng sản phẩm:** Slide LaTeX Beamer $\to$ Biên dịch PDF chuẩn học thuật quốc tế  
**Thư mục lưu trữ:** `Slides_CShape/`

---

## I. MỤC TIÊU BÀI HỌC (COURSE LEARNING OUTCOMES - CLOs)

Kết thúc buổi học 3 tiết này, sinh viên lớp IT26M có khả năng:

| Mã CLO | Mô tả chuẩn đầu ra | Thang đo Bloom |
| :--- | :--- | :--- |
| **CLO 1.1** | Giải thích được các khái niệm nền tảng về hệ thống máy tính: phần cứng, phần mềm, định luật Moore, 6 khối chức năng logic của máy tính (Input, Output, Memory, ALU, CPU, Secondary Storage) và cấu trúc phân cấp dữ liệu từ Bit $\to$ Byte/Character $\to$ Field $\to$ Record $\to$ File $\to$ Database $\to$ Big Data. | Level 2 (Understand) |
| **CLO 1.2** | Nắm vững tiến trình phát triển các thế hệ ngôn ngữ lập trình (Machine Language $\to$ Assembly $\to$ High-Level Language), cơ chế Biên dịch (Compiler) vs Thông dịch (Interpreter); các trụ cột cốt lõi của Công nghệ đối tượng (Class, Object, Attributes, Methods, Encapsulation, Inheritance, Polymorphism). | Level 2 (Understand) |
| **CLO 1.3** | Trình bày được kiến trúc nền tảng Microsoft .NET: Common Language Runtime (CLR), Managed Code vs Unmanaged Code, Microsoft Intermediate Language (MSIL/CIL), trình biên dịch Just-In-Time (JIT), tính độc lập nền tảng (Platform Independence) và khả năng tương tác đa ngôn ngữ (Language Interoperability) trên .NET Core / .NET 8+. | Level 3 (Apply) |
| **CLO 1.4** | Nắm vững cấu trúc giải pháp và công cụ trong Visual Studio IDE (Solution, Project, Code Editor, Windows Forms Designer, Solution Explorer, Properties Window, Toolbox); quy trình biên dịch, chạy và gỡ lỗi ứng dụng C#. | Level 3 (Apply) |
| **CLO 1.5** | Vận dụng mô hình Lập trình trực quan (Visual Programming) và Hướng sự kiện (Event-Driven Programming) để thực hành chạy thử (Test-Drive), phân tích và tương tác với ứng dụng đồ họa Painter thông qua các điều khiển GUI (Form, GroupBox, RadioButton, Panel, Button) và các sự kiện chuột. | Level 3 (Apply / Analyze) |

---

## II. MA TRẬN PHÂN BỔ THỜI GIAN & TIẾN TRÌNH DẠY HỌC (3 TIẾT)

Tổng thời lượng: 150 phút (3 tiết học đại học tích hợp, giải lao giữa giờ).

```text
========================================================================================
TIẾT 1 (50'): NỀN TẢNG TÍNH TOÁN, TỔ CHỨC MÁY TÍNH & PHÂN CẤP DỮ LIỆU
- 05': Giới thiệu học phần, mục tiêu chuẩn đầu ra (CLO 1.1 - 1.5), tâm thế học tập IT26M
- 15': Khái niệm phần cứng, phần mềm, định luật Moore; 6 khối chức năng logic (Hình 1.2)
- 15': Phân cấp dữ liệu từ Bit đến Database (Hình 1.3), bảng đo lường dung lượng byte (Hình 1.4)
- 15': [THỰC HÀNH 1] Khảo sát phần cứng máy tính phòng máy, kiểm tra CPU, RAM và đổi nhị phân
----------------------------------------------------------------------------------------
TIẾT 2 (50'): TIẾN HÓA NGÔN NGỮ, CÔNG NGHỆ ĐỐI TƯỢNG & KIẾN TRÚC MICROSOFT .NET
- 10': Các thế hệ ngôn ngữ lập trình (Machine -> Assembly -> High-level), Compiler vs Interpreter
- 15': Công nghệ đối tượng: Tư duy hướng đối tượng (OOAD), Class vs Object, Đóng gói, Kế thừa
- 15': Kiến trúc Microsoft .NET: CLR, Managed Code, MSIL, JIT Compiler, Độc lập nền tảng (.NET Core/8)
- 10': [THỰC HÀNH 2] Checkpoint Quiz & Khảo sát chu trình biên dịch .NET (dotnet CLI / csc)
----------------------------------------------------------------------------------------
TIẾT 3 (50'): VISUAL STUDIO IDE & TEST-DRIVE ỨNG DỤNG ĐỒ HỌA PAINTER (GUI & EVENT-DRIVEN)
- 10': Ngôn ngữ C# hiện đại: OOP, Event-Driven, Visual Programming, Async/await
- 15': Khám phá Visual Studio IDE: Solution, Projects, Designer, Toolbox, Properties Window
- 20': [THỰC HÀNH 3] Hands-on Lab: Test-Drive ứng dụng Painter (GroupBox, RadioButton, Panel, vẽ)
- 05': Tổng kết checklist chuẩn đầu ra, giao bài tập tự học cuối chương (Self-Review Exercises)
========================================================================================
```

---

## III. BẢN ĐỒ CÁC HÌNH ẢNH TRÍCH XUẤT TỪ SÁCH GIÁO KHOA

Tất cả các hình ảnh được trích xuất và crop chất lượng cao (300 DPI) từ file PDF gốc `textbook_CShape/Chapter_01.pdf` và lưu tại `Slides_CShape/images/`:

1. **`fig1_2_logical_units_p1.png` & `fig1_2_logical_units_p2.png`** (Trích từ Trang 6-7, Hình 1.2 trong sách):
   * *Nội dung:* Bảng đặc tả 6 khối chức năng logic của máy tính: Input, Output, Memory, ALU, CPU, Secondary Storage.
   * *Vị trí sử dụng:* Tiết 1 -- Slide 8 & 9 (Tổ chức máy tính).
2. **`fig1_3_data_hierarchy.png`** (Trích từ Trang 8, Hình 1.3 trong sách):
   * *Nội dung:* Sơ đồ phân cấp dữ liệu thực tế từ Bit `1` $\to$ Byte `01001010` (ký tự ASCII 'J') $\to$ Field `Judy` $\to$ Record `Judy Green` $\to$ File nhân sự.
   * *Vị trí sử dụng:* Tiết 1 -- Slide 12 (Phân cấp dữ liệu).
3. **`fig1_4_byte_measurements.png`** (Trích từ Trang 10, Hình 1.4 trong sách):
   * *Nội dung:* Bảng đo lường dung lượng bộ nhớ từ Kilobyte (KB) đến Yottabyte (YB).
   * *Vị trí sử dụng:* Tiết 1 -- Slide 13 (Đo lường dung lượng byte).
4. **`fig1_8_painter_solution.png`** (Trích từ Trang 24, Hình 1.8 trong sách):
   * *Nội dung:* Cấu trúc thư mục ứng dụng Painter và tệp giải pháp `Painter.sln`.
   * *Vị trí sử dụng:* Tiết 3 -- Slide 35 (Cấu trúc Solution Visual Studio).
5. **`fig1_10_painter_app_gui.png`** (Trích từ Trang 25, Hình 1.10 trong sách):
   * *Nội dung:* Giao diện ứng dụng Painter đang chạy trên Windows với các nhãn chú thích: GroupBoxes, RadioButtons, Panel, Buttons.
   * *Vị trí sử dụng:* Tiết 3 -- Slide 37 (Khảo sát các điều khiển GUI).
6. **`fig1_11_drawing_petals.png`** (Trích từ Trang 26, Hình 1.11 trong sách):
   * *Nội dung:* Thao tác vẽ cánh hoa bằng cọ màu đỏ kích thước nhỏ.
   * *Vị trí sử dụng:* Tiết 3 -- Slide 39 (Thực hành Painter Test-Drive Bước 1).
7. **`fig1_12_drawing_stem_grass.png`** (Trích từ Trang 26, Hình 1.12 trong sách):
   * *Nội dung:* Thao tác vẽ thân hoa và thảm cỏ bằng cọ màu xanh lá kích thước lớn.
   * *Vị trí sử dụng:* Tiết 3 -- Slide 39 (Thực hành Painter Test-Drive Bước 2).
8. **`fig1_13_drawing_complete.png`** (Trích từ Trang 27, Hình 1.13 trong sách):
   * *Nội dung:* Bức vẽ hoàn chỉnh có thêm những giọt mưa màu xanh dương kích thước vừa.
   * *Vị trí sử dụng:* Tiết 3 -- Slide 39 (Thực hành Painter Test-Drive Hoàn tất).

---

## IV. BỐ CỤC 42 SLIDE BÀI GIẢNG LATEX BEAMER

* **Theme:** Chuẩn Beamer Madrid Widescreen 16:9 cao cấp.
* **Bảng màu nhận diện học thuật:**
  * `Primary Navy` (`#0F2C59`): Màu chủ đạo học thuật đại học.
  * `Slate Blue` (`#1D5D9B`): Màu phụ và tiêu đề khối nội dung.
  * `CSharp Purple` (`#68217A`): Màu nhận diện đặc trưng của ngôn ngữ C# và .NET.
  * `Accent Orange` (`#E17012`): Dành cho các câu hỏi Checkpoint, cảnh báo.
  * `Practice Green` (`#1E8449`): Dành cho các bài Hands-on Labs.
* **Cấu hình mã nguồn:** Package `listings` cấu hình syntax highlighting cho C#, MSIL và Terminal console.

### Danh mục 42 Slide chi tiết:

#### PHẦN MỞ ĐẦU (Slides 1 - 4)
* **Slide 1:** Tiêu đề bài giảng: KỸ THUẬT LẬP TRÌNH C# -- CHƯƠNG 1 (Lớp IT26M, Khóa 2026).
* **Slide 2:** Mục tiêu bài học & Ma trận 5 Chuẩn đầu ra (CLO 1.1 -- 1.5).
* **Slide 3:** Lộ trình bài học 3 tiết tích hợp Lý thuyết & 3 bài Thực hành tại chỗ.
* **Slide 4:** Tổng quan vị thế của C# và nền tảng .NET trong phát triển phần mềm doanh nghiệp hiện đại.

#### TIẾT 1: NỀN TẢNG TÍNH TOÁN, TỔ CHỨC MÁY TÍNH & PHÂN CẤP DỮ LIỆU (Slides 5 - 16)
* **Slide 5:** 1.1 Khái niệm cốt lõi: Phần cứng (Hardware) & Phần mềm (Software).
* **Slide 6:** 1.2 Máy tính & Internet trong Đời sống & Nghiên cứu (Y tế điện tử, GPS, Robot, Tự hành).
* **Slide 7:** 1.3 Phần cứng máy tính: Tốc độ tính toán & Định luật Moore (Moore's Law).
* **Slide 8:** 1.3.2 Tổ chức máy tính: 6 khối chức năng logic -- Phần 1: Input, Output, Memory (Hình 1.2 Part 1).
* **Slide 9:** 1.3.2 Tổ chức máy tính: 6 khối chức năng logic -- Phần 2: ALU, CPU, Secondary Storage (Hình 1.2 Part 2).
* **Slide 10:** Sơ đồ dòng dữ liệu và tương tác giữa 6 khối kiến trúc máy tính.
* **Slide 11:** 1.4 Phân cấp dữ liệu (Data Hierarchy): Từ Bit đến Big Data.
* **Slide 12:** Minh họa Phân cấp dữ liệu trong thực tế: Bit, Byte 'J', Field, Record, File (Hình 1.3).
* **Slide 13:** Bảng đo lường dung lượng dữ liệu: Từ Kilobyte (KB) đến Yottabyte (YB) (Hình 1.4).
* **Slide 14:** [CHECKPOINT 1] 2 câu trắc nghiệm nhanh kiểm tra kiến thức Phần cứng & Phân cấp dữ liệu.
* **Slide 15:** [HANDS-ON LAB 1] Khảo sát phần cứng hệ thống (Task Manager / CLI `wmic cpu`), tính toán nhị phân.
* **Slide 16:** Tổng kết Tiết 1: Điểm mấu chốt cần ghi nhớ trước giờ giải lao.

#### TIẾT 2: TIẾN HÓA NGÔN NGỮ, CÔNG NGHỆ ĐỐI TƯỢNG & NỀN TẢNG .NET (Slides 17 - 32)
* **Slide 17:** Khởi động Tiết 2: 1.5 Các thế hệ ngôn ngữ lập trình.
* **Slide 18:** Ngôn ngữ máy (Machine Language) & Hợp ngữ (Assembly Language).
* **Slide 19:** Ngôn ngữ bậc cao (High-Level Language): Biên dịch (Compiler) vs Thông dịch (Interpreter).
* **Slide 20:** 1.6 Công nghệ Đối tượng (Object Technology): Khái niệm và nguồn cảm hứng tự nhiên.
* **Slide 21:** Phân biệt Lớp (Class) và Đối tượng (Object) qua mô hình Ô tô & Tài khoản ngân hàng.
* **Slide 22:** Các trụ cột OOP: Thuộc tính (Attributes), Hành vi (Methods), Đóng gói (Encapsulation), Kế thừa (Inheritance).
* **Slide 23:** 1.7 Internet và World Wide Web: ARPANET, TCP/IP, Web 1.0 $\to$ Web 2.0 $\to$ Điện toán đám mây (Cloud).
* **Slide 24:** 1.8 Ngôn ngữ C#: Lịch sử hình thành (Anders Hejlsberg) & Triết lý thiết kế thanh lịch.
* **Slide 25:** Các phong cách lập trình hỗ trợ trong C#: OOP, Hướng sự kiện, Lập trình trực quan, Generic & Async/Await.
* **Slide 26:** 1.9 Nền tảng Microsoft .NET: Tầm nhìn kiến trúc & Thư viện lớp .NET (FCL).
* **Slide 27:** Kiến trúc thực thi .NET: Mã nguồn C# $\to$ Trình biên dịch C# $\to$ MSIL/CIL $\to$ CLR JIT $\to$ Native Code.
* **Slide 28:** Khái niệm Managed Code (Mã được quản lý) & Các dịch vụ của CLR (Garbage Collection, Bảo mật).
* **Slide 29:** Tính độc lập nền tảng (Platform Independence) & Sự tiến hóa sang .NET Core / .NET 8 Đa nền tảng.
* **Slide 30:** Khả năng tương tác đa ngôn ngữ (Language Interoperability) qua trung gian mã MSIL.
* **Slide 31:** [CHECKPOINT 2] Trắc nghiệm nhanh củng cố kiến thức OOP & Cơ chế thực thi .NET CLR / MSIL.
* **Slide 32:** [HANDS-ON LAB 2] Thử nghiệm biên dịch chương trình C# qua Command Line (`dotnet new console`, `dotnet run`).

#### TIẾT 3: VISUAL STUDIO IDE & TEST-DRIVE ỨNG DỤNG PAINTER (Slides 33 - 42)
* **Slide 33:** Khởi động Tiết 3: 1.10 Hệ điều hành Windows & Hệ sinh thái Microsoft.
* **Slide 34:** 1.11 Môi trường Phát triển Tích hợp: Visual Studio IDE (Giao diện, Tính năng trợ giúp IntelliSense).
* **Slide 35:** Cấu trúc Solution & Project trong Visual Studio (Tệp `.sln`, `.csproj`, Solution Explorer) (Hình 1.8).
* **Slide 36:** 1.12 Case Study: Giới thiệu Ứng dụng Đồ họa Painter (Visual C# GUI App).
* **Slide 37:** Khảo sát các điều khiển đồ họa (GUI Controls): Form, GroupBox, RadioButton, Panel, Button (Hình 1.10).
* **Slide 38:** Cơ chế Lập trình Hướng sự kiện (Event-Driven): Sự kiện tương tác chuột (`MouseDown`, `MouseMove`).
* **Slide 39:** [HANDS-ON LAB 3] Test-Drive Painter App: Mở Solution, Build, Chạy & Thử nghiệm vẽ hình (Hình 1.11 -- 1.13).
* **Slide 40:** [CHECKPOINT 3] Trắc nghiệm củng cố về Visual Studio & Mô hình GUI Event-Driven.
* **Slide 41:** Tổng kết Chương 1: Checklist 5 Chuẩn đầu ra (CLO 1.1 -- 1.5) lớp IT26M đã đạt được.
* **Slide 42:** Nhiệm vụ tự học & Chuẩn bị Chương 2: Nhập môn Cú pháp C# & Viết ứng dụng console đầu tiên.

---

## V. KẾ HOẠCH BIÊN DỊCH VÀ XÁC MINH SẢN PHẨM

1. [x] Khảo sát chi tiết giáo trình `textbook_CShape/Chapter_01.pdf` (32 trang, 12 phần nội dung).
2. [x] Trích xuất và cắt xén hình ảnh minh họa chất lượng cao vào `Slides_CShape/images/`.
3. [x] Lập kế hoạch bài giảng 3 tiết và lưu vào `devPlan/DevPlan_Chapter_1_CSharp_IT26M.md`.
4. [ ] Soạn thảo mã nguồn LaTeX Beamer `Slides_CShape/Chapter_1_Introduction_to_CSharp_IT26M.tex` (42 frames hoàn chỉnh).
5. [ ] Biên dịch bằng XeLaTeX sang tệp PDF `Slides_CShape/Chapter_1_Introduction_to_CSharp_IT26M.pdf`.
6. [ ] Kiểm tra thẩm mỹ, căn chỉnh tỷ lệ 16:9, đảm bảo font tiếng Việt hiển thị sắc nét và chuẩn mực đại học.

