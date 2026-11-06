# KẾ HOẠCH BÀI GIẢNG VÀ PHÁT TRIỂN SLIDE BÀI GIẢNG ĐẠI HỌC
## HỌC PHẦN: KỸ THUẬT LẬP TRÌNH / LẬP TRÌNH JAVA
### CHƯƠNG 1: INTRODUCTION TO JAVA PROGRAMMING
**Đối tượng:** Lớp IT26M (Khóa 2026 - Khoa Công nghệ Thông tin)  
**Thời lượng:** 01 buổi (03 tiết = 150 phút, kết hợp lý thuyết và thực hành tại chỗ)  
**Tài liệu tham khảo chính:** Textbook *Building Java Programs: A Back to Basics Approach* - Chapter 1: Introduction to Java Programming (Stuart Reges & Marty Stepp)  
**Định dạng sản phẩm:** Slide LaTeX Beamer $\to$ Biên dịch PDF chuẩn học thuật quốc tế  

---

## I. MỤC TIÊU BÀI HỌC (COURSE LEARNING OUTCOMES - CLOs)

Kết thúc buổi học 3 tiết này, sinh viên lớp IT26M có khả năng:

| Mã CLO | Mô tả chuẩn đầu ra | Thang đo Bloom |
| :--- | :--- | :--- |
| **CLO 1.1** | Giải thích được các khái niệm cơ bản về hệ thống tính toán: phần cứng/phần mềm, CPU, hệ nhị phân, sự khác biệt giữa trình biên dịch (Compiler) và trình thông dịch (Interpreter), vai trò của máy ảo JVM và mã Bytecode trong triết lý "Write Once, Run Anywhere". | Level 2 (Understand) |
| **CLO 1.2** | Nắm vững cấu trúc khung của một chương trình Java chuẩn (lớp, phương thức `main`, cặp ngoặc `{}`), phân biệt được `System.out.println` và `System.out.print`, sử dụng chính xác các ký tự thoát (Escape Sequences: `\"`, `\n`, `\t`, `\\`). | Level 3 (Apply) |
| **CLO 1.3** | Phân loại và nhận diện chính xác 3 loại lỗi lập trình: Lỗi cú pháp (Syntax Errors), Lỗi thực thi (Runtime Errors / Exceptions), và Lỗi ngữ nghĩa / logic (Logic Errors); đọc hiểu thông báo lỗi từ trình biên dịch để gỡ lỗi (debug). | Level 4 (Analyze) |
| **CLO 1.4** | Hiểu và vận dụng thành thạo kỹ thuật **Phân rã thủ tục (Procedural Decomposition)** và nguyên lý **DRY (Don't Repeat Yourself)**; biết cách khai báo và gọi các phương thức tĩnh (`static methods`); phân tích được luồng điều khiển (Flow of Control). | Level 4 (Analyze / Design) |
| **CLO 1.5** | Độc lập thực hành viết, biên dịch (CLI `javac` / IDE) và chạy (`java`) các chương trình Java có cấu trúc phân rã hoàn chỉnh để giải quyết bài toán vẽ hình nghệ thuật ASCII (Case Study `DrawFigures`). | Level 3 (Apply / Create) |

---

## II. MA TRẬN PHÂN BỔ THỜI GIAN & TIẾN TRÌNH DẠY HỌC (3 TIẾT)

Tổng thời lượng: 150 phút (3 tiết học đại học, giải lao giữa giờ).

```
========================================================================================
TIẾT 1 (50'): NỀN TẢNG TÍNH TOÁN & CHƯƠNG TRÌNH JAVA ĐẦU TIÊN
- 10': Khái niệm tính toán, CPU, Hệ nhị phân (Binary), Biên dịch vs Thông dịch
- 15': Kiến trúc Java, Bytecode, Máy ảo JVM, Mô hình "Write Once, Run Anywhere" (Hình 1.1)
- 10': Cấu trúc chương trình Java: Class, method main, câu lệnh xuất dữ liệu
- 15': [THỰC HÀNH 1] Cài đặt môi trường, viết Hello.java, biên dịch javac & chạy java
----------------------------------------------------------------------------------------
TIẾT 2 (50'): CÚ PHÁP, KÝ TỰ THOÁT & NGHỆ THUẬT GỠ LỖI (DEBUGGING)
- 15': Chuỗi ký tự, Escape Sequences (\n, \t, \", \\), Định danh (Identifiers), Quy ước CamelCase
- 15': Phân loại 3 loại lỗi: Syntax Errors, Runtime Exceptions, Logic Errors
- 10': Kỹ thuật đọc Compiler Messages & Chiến lược sửa lỗi từng bước
- 10': [THỰC HÀNH 2] Checkpoint Quiz & Lab sửa lỗi chương trình (Debug Challenge)
----------------------------------------------------------------------------------------
TIẾT 3 (50'): PHÂN RÃ THỦ TỤC (PROCEDURAL DECOMPOSITION) & CASE STUDY
- 15': Tư duy phân rã Top-down (Hình 1.2 Làm bánh), Phương thức tĩnh (Static Methods)
- 10': Phân tích luồng điều khiển (Flow of Control Diagrams) & Nguyên lý DRY
- 15': Case Study DrawFigures (Tiến hóa từ Bản 1 -> Bản 2 [Hình 1.3] -> Bản 3 [Hình 1.4])
- 10': [THỰC HÀNH 3] Mini-Project: Thiết kế chương trình vẽ Tàu vũ trụ Rocket / FightSong
========================================================================================
```

---

## III. BẢN ĐỒ CÁC HÌNH ẢNH TRÍCH XUẤT TỪ SÁCH GIÁO KHOA

Tất cả các hình ảnh được trích xuất trực tiếp từ file PDF gốc và tối ưu hóa hiển thị trong slide:

1. **`fig1_1_java_execution.png`** (Trích từ Trang 21, Hình 1.1 trong sách):
   * *Nội dung:* Quy trình tạo và thực thi chương trình Java (Trình soạn thảo $\to$ `Hello.java` $\to$ Trình biên dịch `javac` $\to$ Bytecode `Hello.class` $\to$ Máy ảo `JVM` $\to$ Thực thi phần cứng).
   * *Vị trí sử dụng:* Tiết 1 - Slide kiến trúc thực thi Java.
2. **`fig1_2_make_cake_decomposition.png`** (Trích từ Trang 66, Hình 1.2 trong sách):
   * *Nội dung:* Sơ đồ cấu trúc phân rã tác vụ thực tế "Làm bánh" (Make cake $\to$ Make batter, Bake, Make frosting, Frost cake).
   * *Vị trí sử dụng:* Tiết 3 - Slide mở đầu khái niệm Phân rã thủ tục (Procedural Decomposition).
3. **`fig_flow_of_control_drawboxes.png`** (Trích từ Trang 76 trong sách):
   * *Nội dung:* Sơ đồ luồng điều khiển từng bước khi phương thức `main` gọi phương thức phụ `drawBox` hai lần.
   * *Vị trí sử dụng:* Tiết 3 - Slide giải thích cơ chế chuyển giao quyền điều khiển (Transfer of Control).
4. **`fig_control_flow_step1.png` & `fig_control_flow_step2.png`** (Trích từ Trang 81, 82 trong sách):
   * *Nội dung:* Sự mở rộng luồng điều khiển đa cấp khi các hàm gọi lồng nhau (`foo()`, `bar()`, `baz()`).
   * *Vị trí sử dụng:* Tiết 3 - Slide nâng cao về Call Stack và luồng thực thi lồng nhau.
5. **`fig1_3_drawfigures2_decomposition.png`** (Trích từ Trang 92, Hình 1.3 trong sách):
   * *Nội dung:* Sơ đồ cấu trúc phân rã cấp 1 của chương trình `DrawFigures2` (main $\to$ drawDiamond, drawX, drawRocket).
   * *Vị trí sử dụng:* Tiết 3 - Slide phân tích Case Study Version 2.
6. **`fig1_4_drawfigures3_decomposition.png`** (Trích từ Trang 96, Hình 1.4 trong sách):
   * *Nội dung:* Sơ đồ phân rã hoàn chỉnh 2 cấp của chương trình `DrawFigures3` (main $\to$ Subfigures $\to$ Reusable Primitives: cone, v, box).
   * *Vị trí sử dụng:* Tiết 3 - Slide giải pháp triệt tiêu trùng lặp (DRY).

---

## IV. CẤU TRÚC CHI TIẾT CỦA BỘ SLIDE LATEX BEAMER

* **Theme:** Giao diện học thuật hiện đại dựa trên chuẩn Beamer (Madrid/metropolis style) với bảng màu chuyên nghiệp:
  * Primary Color: `Navy Blue` (`#0F2C59`) - Thể hiện tính học thuật, nghiêm túc.
  * Secondary Color: `Teal / Slate Blue` (`#005B96`) - Tạo điểm nhấn hiện đại.
  * Accent Color: `Warm Amber / Orange` (`#FF7315`) - Dành cho các hộp lưu ý (Notice / Warning), Checkpoint.
  * Success Color: `Forest Green` (`#1E8449`) - Dành cho phần thực hành (Hands-on Practice).
* **Package chính:**
  * Hỗ trợ tiếng Việt: UTF-8 với `babel` hoặc `fontspec`.
  * Trình bày mã nguồn: Gói `listings` cấu hình giao diện `Eclipse / VS Code Java Dark/Light`, đánh số dòng rõ ràng, highlight từ khóa, chuỗi, chú thích.
  * Khối thông tin: `tcolorbox` / Beamer blocks chuẩn (`block`, `exampleblock`, `alertblock`).
  * Bố cục: Hai cột (`columns`) linh hoạt giữa lý thuyết - sơ đồ hình ảnh và bài tập - kết quả in.

### Danh mục các phân đoạn Slide:
1. **Title & Giới thiệu:** Thông tin bài giảng, giảng viên, lớp IT26M, mục tiêu chuẩn đầu ra CLO.
2. **Tiết 1: Kiến trúc tính toán & Khởi đầu với Java (Slides 4 - 15)**
   * Khái niệm cơ bản: Phần cứng, Phần mềm, CPU, Dữ liệu nhị phân (0s và 1s).
   * Biên dịch (Compiler) vs Thông dịch (Interpreter).
   * Đặc thù của Java: Java Bytecode & Java Virtual Machine (JVM).
   * Quy trình biên dịch và chạy chương trình Java (Minh họa với **Hình 1.1**).
   * Cấu trúc chương trình Java đầu tiên: `Hello.java`.
   * Khảo sát chi tiết cú pháp: Lớp (`class`), phương thức `main`, lệnh `System.out.println()`.
   * **[LAB 1 - Live Coding]:** Hướng dẫn sinh viên viết, biên dịch bằng terminal `javac` và chạy `java`.
3. **Tiết 2: Cú pháp nâng cao, Ký tự thoát & Kỹ năng Debugging (Slides 16 - 28)**
   * Chuỗi ký tự (String) & Ký tự in đặc biệt.
   * Bảng quy tắc Ký tự thoát (Escape Sequences: `\n`, `\t`, `\"`, `\\`).
   * Định danh (Identifiers), từ khóa Java, chuẩn quy ước CamelCase.
   * Phong cách viết mã (Comments, Indentation, Readability).
   * Phân loại 3 nhóm lỗi lập trình kinh điển:
     * *Syntax Errors* (Lỗi ngữ pháp lúc biên dịch).
     * *Runtime Errors / Exceptions* (Lỗi sập chương trình khi chạy).
     * *Logic Errors* (Lỗi sai kết quả đầu ra).
   * Cách đọc thông báo lỗi từ trình biên dịch Java (javac compiler output).
   * **[Interactive Quiz & LAB 2]:** Tìm 3 lỗi trong đoạn mã và viết lệnh in ASCII Art có trích dẫn.
4. **Tiết 3: Phân rã thủ tục & Case Study Hoàn chỉnh (Slides 29 - 42)**
   * Vấn đề phức tạp và sự trùng lặp trong phần mềm.
   * Nguyên lý Phân rã Top-down (Minh họa với **Hình 1.2: Làm bánh**).
   * Khai báo và sử dụng Phương thức tĩnh (`static methods`).
   * Luồng điều khiển khi gọi phương thức (Minh họa với **Sơ đồ luồng DrawBoxes** và **foo/bar/baz**).
   * Case Study `DrawFigures`:
     * Vấn đề ở Phiên bản 1 (Mã nguồn nguyên khối, trùng lặp trầm trọng).
     * Cải tiến Phiên bản 2: Phân rã cấp 1 (Minh họa với **Hình 1.3**).
     * Cải tiến Phiên bản 3: Triệt tiêu hoàn toàn trùng lặp (Minh họa với **Hình 1.4**).
   * **[LAB 3 - Mini Project]:** Sinh viên thiết kế chương trình `FightSong` hoặc vẽ Tàu con thoi (Rocket) theo chuẩn phân rã 2 cấp.
5. **Tổng kết & Hướng dẫn tự học (Slides 43 - 46)**
   * Tóm tắt toàn bộ kiến thức trọng tâm Chương 1.
   * Bảng đối chiếu các câu lệnh và quy tắc cần ghi nhớ.
   * Bài tập tự rèn luyện về nhà (Self-Check & Programming Projects).
   * Q&A và chuẩn bị cho Chương 2 (Biến, Kiểu dữ liệu & Vòng lặp).

---

## V. KẾ HOẠCH TRIỂN KHAI VÀ KIỂM THỬ

1. [x] **Trích xuất & Xử lý tài nguyên ảnh:** Trích xuất toàn bộ hình sơ đồ giáo khoa từ `Chapter_1_Introduction to Java Programming.pdf` vào thư mục `Slides/images/`.
2. [ ] **Soạn thảo mã nguồn LaTeX Beamer:** Viết file `Slides/Chapter_1_Introduction_to_Java_IT26M.tex` đạt chuẩn sư phạm đại học, tích hợp đầy đủ tiếng Việt, code highlight, bài tập và sơ đồ.
3. [ ] **Biên dịch LaTeX sang PDF:** Chạy trình biên dịch (`xelatex` / `pdflatex`) để tạo file `Slides/Chapter_1_Introduction_to_Java_IT26M.pdf`.
4. [ ] **Kiểm tra chất lượng (QA):**
   * Kiểm tra không có lỗi tràn dòng (overfull hbox).
   * Đảm bảo font chữ tiếng Việt hiển thị đẹp, sắc nét.
   * Đảm bảo tất cả 6 hình ảnh từ sách hiển thị đúng tỉ lệ và vị trí sư phạm.
   * Đảm bảo tính cân đối giữa lý thuyết và các slide thực hành (Hands-on Labs).

