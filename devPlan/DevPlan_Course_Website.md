# KẾ HOẠCH XÂY DỰNG WEBSITE MÔN HỌC KỸ THUẬT LẬP TRÌNH (4 TÍN CHỈ)
## CỔNG HỌC TẬP TRỰC TUYẾN & HỆ THỐNG QUẢN LÝ TÀI NGUYÊN THEO CHƯƠNG
**Học phần:** Kỹ thuật Lập trình (Programming Technique)  
**Khối lượng:** 4 Tín chỉ (Lý thuyết 45 tiết + Thực hành 30 tiết + Đồ án/Bài tập lớn)  
**Đối tượng:** Sinh viên ngành Công nghệ Thông tin -- Khóa 2026 (Lớp IT26M và các lớp chuyên ngành)  
**Giai đoạn 1:** Triển khai toàn diện cho **Chương 1: Introduction to Java Programming**  

---

## I. MỤC TIÊU VÀ ĐẶC TẢ HỆ THỐNG

### 1. Mục tiêu đào tạo của Cổng học tập
* Cung cấp một trung tâm tài nguyên số đồng bộ, hiện đại, chuẩn học thuật đại học cho sinh viên môn Kỹ thuật Lập trình.
* Tích hợp trọn vẹn 5 trụ cột sư phạm trong một giao diện duy nhất:
  1. **Đề cương & Lộ trình:** Kế hoạch học tập 4 tín chỉ, ma trận chuẩn đầu ra (CLOs).
  2. **Kho Tài liệu & Tài nguyên:** Giáo trình gốc tiếng Anh, bản dịch tiếng Việt, bộ slide PDF học thuật, mã nguồn mẫu, hướng dẫn cài đặt môi trường JDK/IDE.
  3. **Video & Slide Player:** Trình phát bài giảng thông minh tích hợp kịch bản đối thoại tương tác song song (Thầy - Trò).
  4. **Hệ thống Trắc nghiệm (Quiz Engine):** Bộ ngân hàng 40 câu hỏi trắc nghiệm chuẩn hóa, độ dài các đáp án phân bổ ngẫu nhiên để tránh thiên kiến đoán mò, chấm điểm tức thì và giải thích cặn kẽ.
  5. **Trung tâm Bài tập (Coding Hub):** Toàn bộ bài tập cuối chương từ giáo trình (Self-Check, Exercises, Programming Projects) có mã nguồn khởi tạo (Starter Code), kết quả mong đợi và lời giải mẫu đối chiếu.

### 2. Thiết kế Kiến trúc Giao diện (UI/UX)
* **Phong cách:** Academic Modern Portal (lấy cảm hứng từ MIT OpenCourseWare, Stanford CS106A và Harvard CS50).
* **Bảng màu chủ đạo:**
  * Primary: Deep Navy `#0F2C59` (Nghiêm túc, học thuật)
  * Secondary: Slate/Tech Blue `#1D5D9B` & Modern Cyan `#00A8CC`
  * Accent/Success: Emerald Green `#10B981` (Thực hành & Điểm số)
  * Warning/Notice: Warm Amber `#F59E0B`
  * Background: Clean Crisp `#F8FAFC` & Code Console Dark `#1E293B`
* **Công nghệ:** HTML5, CSS3 hiện đại (Grid, Flexbox, CSS Variables, Glassmorphism), Vanilla JavaScript tối ưu hiệu năng cao, không phụ thuộc thư viện ngoài nặng nề, tương thích 100% trên cả Desktop, Tablet và Smartphone.

---

## II. MA TRẬN TÀI NGUYÊN CHƯƠNG 1 (INTRODUCTION TO JAVA PROGRAMMING)

| Hạng mục | Tài nguyên tương ứng trong Workspace | Tính năng trên Website |
| :--- | :--- | :--- |
| **Giáo trình tiếng Anh** | `Textbook/Chapter_1_Introduction to Java Programming.pdf` | Tích hợp xem trực tiếp / tải về |
| **Giáo trình tiếng Việt** | `textbook_vi/Building Java Programs_ A Back - Stuart Reges - Vietnamese.pdf` | Liên kết tra cứu thuật ngữ song ngữ |
| **Slide Chính thức Chương 1** | `Videos/Chapter_01/slideChapter_01.pdf` (41 slides) | **Tài liệu slide chính thức của môn học:** Trình chiếu web tương tác, tải PDF, mở rạp chiếu |
| **Slide Bổ trợ Beamer** | `Slides/Chapter_1_Introduction_to_Java_IT26M.pdf` | Bản in học thuật Beamer Widescreen 16:9 |
| **Kịch bản thoại Video** | `Videos/Chapter_01/scriptChapter01.txt` | Hiển thị song song Thầy & Trò theo từng slide |
| **Audio thuyết minh** | `Videos/Chapter_01/audio/slide_1.mp3` - `slide_41.mp3` | Tích hợp trình phát âm thanh đồng bộ từng slide |
| **Mã nguồn mẫu giáo khoa** | `all code 5th/Chapter_01/*.java` & `Labs/src/*.java` | Trình duyệt code highlight, copy 1-click |
| **Ngân hàng trắc nghiệm** | 40 câu hỏi chuẩn hóa bao quát 5 chủ đề cốt lõi | Chấm điểm, lọc câu hỏi, xem lời giải |
| **Bài tập cuối chương** | Self-Check (p.103), Exercises (p.120), Projects (p.130) | Mô tả đề bài, output mẫu, starter code & giải |

---

## III. ĐẶC TẢ CHI TIẾT CÁC PHÂN HỆ CHỨC NĂNG

### Phân hệ 1: Header, Navigation & Cây chương trình 19 chương
* Header cố định chứa logo môn học, thanh tìm kiếm nhanh, nút chuyển tab và menu chọn chương.
* Danh mục 19 chương môn Kỹ thuật Lập trình:
  * **Chương 1 (Đang mở):** Nhập môn Lập trình Java & Phân rã thủ tục.
  * **Chương 2 -- 19 (Lộ trình tiếp theo):** Dữ liệu nguyên thủy & Vòng lặp, Tham số & Đồ họa, Cấu trúc rẽ nhánh, Vòng lặp bất định, Xử lý tệp (File I/O), Mảng (Arrays), Lập trình Hướng đối tượng (OOP Classes), Kế thừa & Đa hình (Inheritance & Interfaces)...

### Phân hệ 2: Kho Tài nguyên & Tài liệu Số (Documents & Resources)
* Thẻ tải nhanh Giáo trình, Slide PDF, Bảng tra cứu cú pháp (Cheatsheet).
* Hướng dẫn thiết lập môi trường lập trình (JDK 21, VS Code, IntelliJ IDEA).
* Trình đọc mã nguồn mẫu trực quan có syntax highlighting cho:
  * `Hello.java`, `Hello2.java`, `Hello3.java`
  * `DrawBoxes.java`, `DrawBoxes2.java`
  * `DrawFigures1.java`, `DrawFigures2.java`, `DrawFigures3.java`
  * `FightSong.java`, `SpaceRocket.java`, `EscapeChallenge.java`

### Phân hệ 3: Trình phát Video & Slide kèm Kịch bản Đối thoại (Video & Transcript Player)
* Trình phát slide tương tác tuần tự 41 slide của Chương 1.
* Thanh điều khiển: Next, Prev, chọn slide từ danh sách, phóng to toàn màn hình.
* Khung hiển thị kịch bản thoại (Interactive Transcript) đồng bộ theo từng slide, phân biệt rõ màu sắc giữa:
  * 👨‍🏫 **Người 1 (Giảng viên):** Giải thích lý thuyết, mã nguồn, dẫn dắt câu hỏi.
  * 🧑‍🎓 **Người 2 (Sinh viên IT26M):** Đặt câu hỏi thắc mắc, phân tích đáp án, chia sẻ kinh nghiệm gõ lệnh.

### Phân hệ 4: Hệ thống Trắc nghiệm Ôn tập (Interactive 40-Question Quiz)
* **Nguyên tắc thiết kế sư phạm quan trọng:** Độ dài các phương án lựa chọn (A, B, C, D) được phân bổ ngẫu nhiên, không để đáp án đúng luôn là đáp án dài nhất, triệt tiêu hoàn toàn hiện tượng đoán mò theo chiều dài câu chữ.
* **Ngân hàng 40 câu hỏi phân bổ cân đối:**
  * Nhóm 1 (Câu 1 - 8): Kiến trúc phần cứng, CPU, RAM, Hệ nhị phân (Binary) và Biểu diễn dữ liệu.
  * Nhóm 2 (Câu 9 - 16): Trình biên dịch vs Thông dịch, Mã Bytecode, Máy ảo JVM, Bộ công cụ JDK/JRE và chu trình Edit-Compile-Run.
  * Nhóm 3 (Câu 17 - 24): Cấu trúc Class, Hàm `main`, Lệnh xuất dữ liệu `print`/`println`, Quy tắc đặt tên file.
  * Nhóm 4 (Câu 25 - 32): Chuỗi ký tự (String), Ký tự thoát (`\"`, `\n`, `\t`, `\\`), Định danh (Identifiers), Quy ước CamelCase, Chú thích (Comments).
  * Nhóm 5 (Câu 33 - 40): Ba nhóm lỗi lập trình (Syntax, Runtime, Logic), Phương pháp Debug, Phân rã thủ tục (Top-down decomposition), Phương thức tĩnh, Luồng điều khiển (Call Stack), và Case Study `DrawFigures`.
* **Tính năng tương tác:**
  * Làm bài từng câu, xem kết quả ngay hoặc nộp toàn bộ bài thi.
  * Thống kê tỷ lệ điểm số, huy hiệu đánh giá năng lực (Xuất sắc / Khá / Cần ôn thêm).
  * Bộ lọc câu hỏi: Tất cả / Câu đúng / Câu sai / Câu chưa làm.
  * Lời giải thích cặn kẽ (Detailed Explanation) cho từng câu hỏi giúp sinh viên hiểu rõ vì sao đúng, vì sao sai.

### Phân hệ 5: Trung tâm Bài tập Cuối chương (End-of-Chapter Coding Hub)
Trích xuất toàn diện từ phần cuối Chương 1 giáo trình:
1. **Mục Self-Check Problems:**
   * Bài 1: Tại sao máy tính dùng số nhị phân?
   * Bài 2: Đổi số thập phân sang nhị phân (6, 44, 72, 131).
   * Bài 3: Đổi số nhị phân sang thập phân (100, 1011, 101010, 1001110).
   * Bài 5: Khác biệt giữa file `.java` và file `.class`?
   * Bài 6: Nhận diện các định danh (Identifiers) hợp lệ trong Java.
   * Bài 8-10: Dự đoán kết quả in của các lệnh có ký tự thoát phức tạp.
   * Bài 18: Thám tử phát hiện 3 lỗi trong chương trình `MyProgram`.
   * Bài 26: Lần vết luồng điều khiển của hàm `Confusing`.
2. **Mục Exercises (Bài tập lập trình cốt lõi):**
   * Exercise 1: `Stewie` (In khối văn bản "Victory is mine!" kẹp giữa các dấu gạch chéo).
   * Exercise 2: `Spikey` (Vẽ mũi tên gai ASCII đối xứng).
   * Exercise 3: `WellFormed` (In đặc tả chương trình Java chuẩn).
   * Exercise 7: `Mantra` (In câu thần chú bằng phương thức tĩnh).
   * Exercise 11: `TwoRockets` (Vẽ 2 tên lửa đứng cạnh nhau có phân rã).
   * Exercise 12: `FightSong` (Bài hát cổ động triệt tiêu 100% trùng lặp).
   * Exercise 13: `StarFigures` (Vẽ các hình ngôi sao đối xứng).
   * Exercise 14: `Lanterns` (Vẽ đèn lồng lồng ghép).
3. **Mục Programming Projects (Đồ án lập trình mini):**
   * Project 1: `MISSISSIPPI` (In các chữ cái khối lớn lặp lại với phân rã tối ưu).
   * Project 2: `Letters` (In các bức thư gửi người thân áp dụng tái sử dụng đoạn văn).
   * Project 3: `There Was an Old Lady Who Swallowed a Fly` (Bài hát tích lũy có cấu trúc phân tầng phức hợp).

---

## IV. KẾ HOẠCH TRIỂN KHAI VÀ BÀN GIAO

1. [x] Lập kế hoạch kiến trúc và lưu vào `devPlan/DevPlan_Course_Website.md`.
2. [x] Xây dựng file dữ liệu câu hỏi trắc nghiệm `js/quiz_data.js` (40 câu chuẩn hóa, độ dài đáp án ngẫu nhiên, giải thích chi tiết, gắn nhãn Bloom & chủ đề).
3. [x] Xây dựng file dữ liệu bài tập cuối chương `js/exercises_data.js` (19 bài tập: 8 Self-Check, 8 Exercises, 3 Projects có starter code, output mong đợi & giải mẫu).
4. [x] Xây dựng file giao diện chính `index.html` tích hợp thanh điều hướng, tabs chức năng, tài nguyên, video/script player, quiz engine và exercise hub.
5. [x] Chuẩn hóa Slide chính thức: Trích xuất 41 slide độ nét cao từ `Videos/Chapter_01/slideChapter_01.pdf` vào `Videos/Chapter_01/slides_png/` phục vụ trình chiếu web tốc độ cao và cung cấp link tải trực tiếp.
6. [x] Xây dựng hệ thống phong cách thẩm mỹ `css/style.css` (Dark/Light mode, Responsive, Academic Glassmorphism) và kịch bản tương tác mượt mà `js/app.js` (Slide sync, Audio narration, Interactive Quiz, Exercise filter & Code copying).
7. [x] Tích hợp Audio thuyết minh đồng bộ: 41 file audio MP3 trong `Videos/Chapter_01/audio/` tích hợp trực tiếp vào trình phát bài giảng với nút Play/Pause và tự động chuyển slide.
8. [x] Kiểm thử toàn diện: Node.js syntax check (0 lỗi), local HTTP web server test (HTTP 200, 31.3 KB HTML, tải đầy đủ CSS & JS).
9. [x] Đóng gói và chuẩn bị đưa lên GitHub Pages: Đường dẫn tương đối (`./`), tạo file `.nojekyll` và tài liệu hướng dẫn triển khai `README.md`.

---

## V. HƯỚNG DẪN TRIỂN KHAI LÊN GITHUB PAGES

Cổng thông tin được thiết kế 100% tĩnh (Static SPA) với các đường dẫn tài nguyên tương đối (`./`), sẵn sàng triển khai trực tiếp lên GitHub Pages:

### Bước 1: Khởi tạo Git và Commit mã nguồn
```bash
git init
git add .
git commit -m "feat: Initial release of Programming Technique 2026 Course Website (Chapter 1)"
```

### Bước 2: Liên kết với Remote Repository trên GitHub
```bash
git branch -M main
git remote add origin https://github.com/<tai-khoan-cua-ban>/<ten-repo>.git
git push -u origin main
```

### Bước 3: Kích hoạt GitHub Pages
1. Truy cập vào kho chứa trên GitHub: `Settings` > `Pages`.
2. Tại mục **Build and deployment** > **Source**: Chọn **Deploy from a branch**.
3. Tại mục **Branch**: Chọn `main` và thư mục `/ (root)`.
4. Nhấn **Save**.
5. Sau 1 - 2 phút, GitHub sẽ cung cấp đường link website chính thức:  
   `https://<tai-khoan-cua-ban>.github.io/<ten-repo>/`

