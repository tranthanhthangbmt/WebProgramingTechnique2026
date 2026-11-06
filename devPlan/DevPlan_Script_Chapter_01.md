# KẾ HOẠCH XÂY DỰNG KỊCH BẢN THUYẾT MINH VIDEO (SCRIPT)
## CHƯƠNG 1: INTRODUCTION TO JAVA PROGRAMMING
**Mã file đầu ra:** `Videos\Chapter_01\scriptChapter01.txt`  
**File slide cơ sở:** `Videos\Chapter_01\slideChapter_01.pdf` (Gồm 41 slides tương ứng)  
**Tài liệu giáo trình đối chiếu:** `Textbook\Chapter_1_Introduction to Java Programming.pdf`  
**Cấu trúc tham chiếu:** Chuẩn định dạng đối thoại hai nhân vật từ `Videos\Chapter_01\scriptDemo.txt`  
**Đối tượng người nghe:** Sinh viên chuyên ngành CNTT -- Lớp IT26M (Khóa 2026)  

---

## I. MỤC TIÊU & NGUYÊN TẮC THIẾT KẾ KỊCH BẢN

1. **Chuẩn format hai nhân vật (Người 1 & Người 2):**
   * **Người 1 (Thầy/Cô Giảng viên):** Người dẫn dắt học thuật, giải thích sâu sắc các nguyên lý cốt lõi (kiến trúc máy tính, nhị phân, JVM, Bytecode, cú pháp, phân loại lỗi, tư duy thiết kế Top-down decomposition, nguyên lý DRY). Giọng văn ấm áp, sư phạm, giàu tính truyền cảm hứng.
   * **Người 2 (Sinh viên IT26M):** Sinh viên thông minh, chăm chú, tích cực tương tác, biết đặt câu hỏi thắc mắc mở rộng vấn đề, liên hệ thực tế, tham gia giải đố tại các slide Checkpoint và hào hứng thực hiện các bài Lab.
2. **Khớp nối 1:1 với 41 Slide trong `slideChapter_01.pdf`:**
   * Mỗi slide bắt đầu bằng tiêu đề chuẩn: `Slide X: <Tên tiêu đề slide>`.
   * Nội dung lời thoại bám sát hình ảnh, mã nguồn Java, bảng biểu và sơ đồ trích xuất từ sách giáo khoa.
3. **Khai thác triệt để kiến thức từ Textbook gốc:**
   * Triết lý lập trình của Donald Knuth, sự ra đời của Java năm 1995 (Sun Microsystems, James Gosling).
   * Cơ chế WORA, Bytecode, JVM, javac/java.
   * Cấu trúc lớp, phương thức `main`, mảng đối số `args`, `println` vs `print`.
   * Ký tự thoát (Escape Sequences: `\n`, `\t`, `\"`, `\\`), quy ước CamelCase, chú thích (Comments).
   * Ba nhóm lỗi: Lỗi cú pháp (Syntax), Lỗi thực thi (Runtime / Exceptions), Lỗi ngữ nghĩa (Logic / Bugs).
   * Phân rã thủ tục (Procedural Decomposition), sơ đồ cấu trúc làm bánh (Make cake), Call Stack, và sự tiến hóa qua 3 thế hệ của Case Study `DrawFigures`.

---

## II. MA TRẬN 41 SLIDE & LỘ TRÌNH KỊCH BẢN CHI TIẾT

| Slide | Tiêu đề Slide | Nội dung trọng tâm lời thoại |
| :---: | :--- | :--- |
| **1** | Kỹ thuật Lập trình / Java - Chương 1: Introduction to Java Programming | Giới thiệu môn học, khởi đầu hành trình lập trình Java cho sinh viên IT26M. |
| **2** | Mục tiêu học tập bài học (Course Learning Outcomes -- CLOs) | Giảng viên phổ biến 5 chuẩn đầu ra CLO 1.1 đến CLO 1.5; sinh viên liên hệ thực tế. |
| **3** | Lộ trình buổi học 3 tiết (Tích hợp Lý thuyết & Thực hành) | Định hướng tiến trình 3 tiết học cân bằng giữa lý thuyết và live-coding. |
| **4** | TIẾT 1: Nền tảng hệ thống tính toán, kiến trúc JVM & chương trình đầu tiên | Chuyển cảnh sang Tiết 1 -- Bước khởi đầu xây dựng nền tảng. |
| **5** | 1.1 Tại sao chúng ta cần học lập trình? (Why Programming?) | Bản chất của lập trình, trích dẫn Donald Knuth, phần cứng CPU, RAM, Ổ cứng. |
| **6** | Thế giới số & Biểu diễn dữ liệu bằng Hệ nhị phân (Binary) | Tại sao dùng 0 và 1 (transistor), chuyển đổi cơ số 2 sang cơ số 10. |
| **7** | Cơ chế thực thi: Trình biên dịch (Compiler) vs. Thông dịch (Interpreter) | So sánh C/C++ và Python; vấn đề phụ thuộc nền tảng của mã máy trực tiếp. |
| **8** | Kiến trúc đột phá của Java: Máy ảo JVM & Mã Bytecode | Giải pháp WORA của Java; phân biệt bộ công cụ JDK, JRE và JVM. |
| **9** | Quy trình phát triển chương trình Java: Edit $\to$ Compile $\to$ Run | Phân tích sâu Hình 1.1 từ giáo trình: `Hello.java` $\to$ `javac` $\to$ `Hello.class` $\to$ `java`. |
| **10** | 1.2 Chương trình Java hoàn chỉnh đầu tiên (Hello.java) | Mổ xẻ `public class Hello`, quy tắc vàng: tên file trùng tên class công khai. |
| **11** | Mổ xẻ phương thức main -- Điểm bắt đầu của mọi ứng dụng | Ý nghĩa của từng từ khóa: `public`, `static`, `void`, `main`, `String[] args`. |
| **12** | Lệnh xuất dữ liệu: println vs. print | Sự khác biệt về con trỏ và bước xuống dòng mới newline qua ví dụ trực quan. |
| **13** | [CHECKPOINT 1] Kiểm tra nhanh lý thuyết Tiết 1 | Người 2 trả lời trắc nghiệm, Người 1 phân tích hoa-thường và vai trò file `.class`. |
| **14** | [HANDS-ON LAB 1] Thực hành tại chỗ: Viết, biên dịch & chạy Java | Thao tác dòng lệnh CLI (`javac`, `java`), quan sát file `.class` thực tế. |
| **15** | TIẾT 2: Chuỗi ký tự, Ký tự thoát & Kỹ năng chẩn đoán, gỡ lỗi | Chuyển cảnh sang Tiết 2 -- Nâng cao cú pháp và làm chủ kỹ năng Debug. |
| **16** | Chuỗi ký tự (String Literals) & Thách thức khi xuất ký tự đặc biệt | Khái niệm String literal; bế tắc khi muốn in dấu ngoặc kép hoặc gạch chéo. |
| **17** | Bảng ký tự thoát chuẩn trong Java (Escape Sequences) | Bảng tra cứu `\n`, `\t`, `\"`, `\\`; cách hoạt động của ký tự đảo nghĩa backslash. |
| **18** | Định danh (Identifiers) & Từ khóa chuẩn Java | Quy tắc đặt tên biến/lớp, cấm bắt đầu bằng số, phân biệt chữ hoa-thường, từ khóa cấm. |
| **19** | Phong cách lập trình chuẩn đại học: Quy ước CamelCase & Comments | UpperCamelCase, lowerCamelCase; 3 loại chú thích (`//`, `/* */`, Javadoc `/** */`). |
| **20** | 1.3 Phân loại lỗi lập trình: 3 nhóm lỗi kinh điển | Tổng quan và so sánh: Lỗi cú pháp (Syntax), Lỗi thực thi (Runtime), Lỗi logic. |
| **21** | Kỹ năng đọc thông báo lỗi từ Trình biên dịch (javac) | Mổ xẻ format lỗi: tên file, số dòng, mô tả lỗi, vị trí con trỏ `^`; kinh nghiệm sửa lỗi đầu tiên. |
| **22** | [CHECKPOINT 2] Thử tài thám tử chẩn đoán lỗi | Người 2 chẩn đoán 3 lỗi trong đoạn code mẫu; Người 1 chốt quy tắc bắt buộc. |
| **23** | [HANDS-ON LAB 2] Thực hành Debug & Chuỗi ký tự thoát | Thử thách viết `EscapeChallenge.java` in đường dẫn Windows và biểu tượng ASCII. |
| **24** | TIẾT 3: Phân rã thủ tục, Phương thức tĩnh & Case Study DrawFigures | Chuyển cảnh sang Tiết 3 -- Tư duy kỹ nghệ phần mềm và thiết kế kiến trúc. |
| **25** | 1.4 Vấn đề của bài toán lớn & Tư duy Phân rã Top-down | Hiểm họa của mã nguồn nguyên khối (Monolithic); nguyên lý DRY (Don't Repeat Yourself). |
| **26** | Ví dụ thực tế: Phân rã tác vụ "Làm bánh" (Make Cake) | Phân tích sâu Hình 1.2: Từ mục tiêu lớn $\to$ các công đoạn $\to$ thao tác cơ sở. |
| **27** | Phương thức tĩnh (Static Methods): Cú pháp Khai báo & Lời gọi | Cách khai báo `public static void name()`; cách gọi trong `main`; quy tắc không lồng hàm. |
| **28** | Luồng điều khiển khi gọi phương thức (Flow of Control) | Phân tích sơ đồ luồng `DrawBoxes`: Tạm dừng `main`, chuyển giao quyền, quay về (return). |
| **29** | Luồng điều khiển đa cấp & Khái niệm Ngăn xếp gọi hàm (Call Stack) | Phân tích sơ đồ `foo/bar/baz`; cơ chế LIFO của Call Stack; 2 lợi ích: Structure & DRY. |
| **30** | 1.5 Case Study: Bài toán vẽ hình ASCII nghệ thuật (DrawFigures) | Đặt đề bài: Vẽ Kim cương, Chữ X, Tên lửa vũ trụ; nhận diện các hình khối lặp lại. |
| **31** | Phiên bản 1 (DrawFigures1): Tiếp cận Ngây thơ (Naïve Approach) | Mổ xẻ 30+ dòng lệnh dồn trong `main`; chỉ ra điểm yếu chí mạng khi cần chỉnh sửa. |
| **32** | Phiên bản 2 (DrawFigures2): Phân rã Cấp 1 theo Khối hình | Phân tích Hình 1.3: Tách `drawDiamond`, `drawX`, `drawRocket`; nhận xét phần còn lặp lại. |
| **33** | Phiên bản 3 (DrawFigures3): Phân rã Hoàn chỉnh 2 Cấp | Phân tích Hình 1.4: Kiến trúc 3 tầng (Điều phối $\to$ Khối hình $\to$ Khối nguyên thủy). |
| **34** | Mã nguồn hoàn chỉnh đạt chuẩn: DrawFigures3.java | Đọc hiểu mã nguồn phân tầng mẫu mực; cách tái sử dụng `drawCone`, `drawV`, `drawBox`. |
| **35** | So sánh & Đánh giá 3 thế hệ thiết kế | Bảng đối chiếu cấu trúc, độ trùng lặp, khả năng tái sử dụng và khả năng bảo trì. |
| **36** | [CHECKPOINT 3] Dự đoán luồng thực thi hàm lồng nhau | Phân tích bài toán lần vết (TraceTest) thứ tự in `first()` và `second()`. |
| **37** | [HANDS-ON LAB 3] Mini-Project: Thiết kế chương trình Rocket/FightSong | Hướng dẫn sinh viên tự tay thiết kế chương trình phân rã 2 cấp hoàn chỉnh tại lớp. |
| **38** | Tổng kết toàn bộ kiến thức Chương 1 (Checklist Chuẩn đầu ra) | Rà soát toàn bộ chuẩn đầu ra CLO 1.1 đến CLO 1.5; khẳng định năng lực sinh viên. |
| **39** | Bảng tra cứu nhanh cú pháp cốt lõi (Java Quick Cheatsheet) | Bảng tóm tắt các cú pháp phải nhớ: class, main, escape sequence, static method. |
| **40** | Nhiệm vụ tự học & Bài tập về nhà cho lớp IT26M | Giao bài tập LMS, Self-Check, Programming Projects; dặn dò chuẩn bị cho Chương 2. |
| **41** | CẢM ƠN CÁC BẠN SINH VIÊN LỚP IT26M! | Lời kết, khích lệ tinh thần học tập, thông báo buổi học tiếp theo. |

---

## III. TIẾN TRÌNH THỰC HIỆN

1. [x] Lập kế hoạch chi tiết và lưu vào `devPlan/DevPlan_Script_Chapter_01.md`.
2. [ ] Soạn thảo toàn văn `Videos/Chapter_01/scriptChapter01.txt` chuẩn định dạng, ngôn từ hấp dẫn, sư phạm, chuyên nghiệp.
3. [ ] Kiểm tra tính chính xác, nhất quán với 41 slide của `Videos/Chapter_01/slideChapter_01.pdf` và tài liệu gốc.

