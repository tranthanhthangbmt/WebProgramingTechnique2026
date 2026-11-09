# KẾ HOẠCH PHÁT TRIỂN CỔNG HỌC TẬP KỸ THUẬT LẬP TRÌNH C# & .NET (4 TÍN CHỈ)
## CHƯƠNG 1: INTRODUCTION TO COMPUTERS, THE INTERNET AND VISUAL C#
**Học phần:** Kỹ thuật Lập trình (Programming Technique — C# / .NET)  
**Khối lượng:** 4 Tín chỉ (45 tiết lý thuyết + 30 tiết thực hành phòng máy & đồ án)  
**Đối tượng:** Sinh viên ngành Công nghệ Thông tin — Khóa 2026 (Lớp IT26M)  
**Giáo trình chính:** *Visual C# How to Program (6th Edition)* — Harvey Deitel & Paul Deitel  
**Nền tảng công nghệ:** Visual Studio 2022 Community, .NET 8 / C# 12, HTML5/CSS3/Vanilla JS (GitHub Pages Ready)  

---

## I. MỤC TIÊU VÀ ĐẶC TẢ HỆ THỐNG C# CHƯƠNG 1

### 1. Mục tiêu chuyển đổi từ Java sang C#
* Đồng bộ hóa toàn diện cổng thông tin học tập sang ngôn ngữ **C# và nền tảng .NET 8** theo đúng chương trình đào tạo của Khoa CNTT.
* Tích hợp đầy đủ 6 phân hệ cốt lõi:
  1. **Đề cương & Lộ trình:** 5 Chuẩn đầu ra (CLO 1.1 -- 1.5), tiến trình 3 tiết học tích hợp lý thuyết và 3 bài Hands-on Labs.
  2. **Tài liệu & Tài nguyên:** Giáo trình gốc `textbook_CShape/Chapter_01.pdf`, Slide chính thức `VideoCShape/Chapter_01/Slide_Chapter_01.pdf` (42 slide), Slide Beamer học thuật `Slides_CShape/Chapter_1_Introduction_to_CSharp_IT26M.pdf`, Kịch bản thoại `VideoCShape/Chapter_01/script.txt`, Hướng dẫn cài đặt Visual Studio 2022.
  3. **Video & Slide Player:** Tích hợp rạp chiếu video `VideoCShape/Chapter_01/index.html` (42 slide HD kèm audio và tự động chuyển trang) và chế độ đối chiếu Split View.
  4. **Ngân hàng Trắc nghiệm (40 câu):** 40 câu hỏi trắc nghiệm chuẩn hóa bao quát toàn bộ nội dung Chương 1 của giáo trình Deitel, độ dài các đáp án A/B/C/D được phân bổ ngẫu nhiên để triệt tiêu thiên kiến đoán mò, có giải thích cơ chế chi tiết.
  5. **Trung tâm Bài tập (29 bài tập có hình ảnh):** Trích xuất trọn vẹn 100% bài tập từ trang 67 đến 72 trong giáo trình C# (Self-Review Exercises 1.1 -- 1.6, Exercises 1.7 -- 1.25, Making-a-Difference 1.26 -- 1.29), dịch toàn bộ sang tiếng Việt, nhúng hình ảnh minh họa trích xuất từ sách, kèm gợi ý và đáp án chi tiết.
  6. **Kho Mã nguồn Mẫu C#:** Các mã nguồn thực chiến sẵn sàng biên dịch và chạy: `Program.cs` Console, chu trình .NET CLI, kiến trúc ứng dụng đồ họa Windows Forms `PainterForm.cs` và mô hình lập trình hướng sự kiện (Event-Driven).

---

## II. MA TRẬN TÀI NGUYÊN SỐ HÓA CHƯƠNG 1 C#

| Hạng mục | Đường dẫn tệp tin trong Workspace | Vai trò trên Cổng học tập |
| :--- | :--- | :--- |
| **Giáo trình gốc** | `textbook_CShape/Chapter_01.pdf` (32 trang) | Tài liệu học tập, tra cứu bài tập và lý thuyết |
| **Slide chính thức** | `VideoCShape/Chapter_01/Slide_Chapter_01.pdf` (42 trang) | Trình chiếu web, tải PDF, phát video bài giảng |
| **Slide Beamer in ấn** | `Slides_CShape/Chapter_1_Introduction_to_CSharp_IT26M.pdf` | Bản in học thuật phát tay (handout) phòng máy |
| **Kịch bản thoại** | `VideoCShape/Chapter_01/script.txt` (63.6 KB, 42 slide) | Lời thoại tương tác Thầy & Trò đồng bộ video |
| **Audio thuyết minh** | `VideoCShape/Chapter_01/audio/slide_1.mp3` -- `slide_42.mp3` | Âm thanh giọng đọc bài giảng từng slide |
| **Hình ảnh slide trích xuất**| `VideoCShape/Chapter_01/images/slide-1.png` -- `slide-42.png` | Hiển thị trình duyệt slide siêu tốc |
| **Hình ảnh bài tập SGK** | `extracted_images/fig1_*.png` (Hình 1.2, 1.3, 1.4, 1.8, 1.10--1.13)| Nhúng trực tiếp vào các thẻ bài tập tương ứng |
| **Trắc nghiệm chuẩn hóa** | `js/quiz_data.js` (40 câu hỏi C# chuẩn mực) | Hệ thống thi trắc nghiệm trực tuyến chấm điểm tức thì |
| **Bộ bài tập cuối chương**| `js/exercises_data.js` (29 bài tập có giải & hình) | Trung tâm bài tập tự luyện và đánh giá năng lực |
| **Mã nguồn mẫu C#** | Tab 6 trên `index.html` | Sao chép 1-click mã nguồn C# và lệnh .NET CLI |

---

## III. MA TRẬN 40 CÂU HỎI TRẮC NGHIỆM CHƯƠNG 1 C# (TRIỆT TIÊU THIÊN KIẾN ĐỘ DÀI)

### 1. Đặc tả Cân bằng Độ dài & Phân bổ Vị trí (Anti-Length-Bias Optimization)
* **Phân bố vị trí đáp án đúng:** Đúng 10 câu A, 10 câu B, 10 câu C, 10 câu D (phân bổ ngẫu nhiên, tối đa 2 câu liên tiếp trùng vị trí, không lặp chu kỳ).
* **Phân bố độ dài đáp án đúng (Rank distribution):**
  * **Hạng 1 (Đáp án đúng là phương án NGẮN NHẤT):** Đúng 10 câu (25.0%).
  * **Hạng 2 (Đáp án đúng là phương án NGẮN THỨ NHÌ):** Đúng 10 câu (25.0%).
  * **Hạng 3 (Đáp án đúng là phương án DÀI THỨ NHÌ):** Đúng 10 câu (25.0%).
  * **Hạng 4 (Đáp án đúng là phương án DÀI NHẤT):** Đúng 10 câu (25.0%).
* **Độ lệch độ dài trong mỗi câu:** Cực kỳ tự nhiên và hài hòa (trung bình chỉ **21.8 ký tự**, tối đa 33 ký tự giữa phương án ngắn nhất và dài nhất), tất cả các phương án nhiễu đều là câu kỹ thuật hoàn chỉnh và giàu tính học thuật.
* **Tối ưu hóa Câu 5 (đặc tính RAM - phản ánh phản hồi từ sinh viên):** Đáp án đúng (khả biến - volatile) nằm ở vị trí B và là lựa chọn ngắn nhất (79 ký tự so với 93, 101, 109 ký tự của các phương án nhiễu), triệt tiêu hoàn toàn khả năng nhận diện đáp án dựa vào câu dài nhất.

### 2. Ma trận 8 Chủ đề Cốt lõi theo Giáo trình Deitel & Deitel
* **Nhóm 2 (Câu 9 -- 14):** Cấu trúc phân cấp dữ liệu (Bit $\to$ Byte $\to$ Field $\to$ Record $\to$ File $\to$ Database $\to$ Big Data) và Bảng đo lường dung lượng Byte ($2^{10}=1024$ từ KB đến YB).
* **Nhóm 3 (Câu 15 -- 19):** Các thế hệ ngôn ngữ lập trình (Machine Language, Assembly Mnemonics, High-Level), Trình biên dịch (Compiler) vs Thông dịch (Interpreter) và Cơ chế Lai (Hybrid Approach).
* **Nhóm 4 (Câu 20 -- 25):** Công nghệ đối tượng (OOP): Thuộc tính vs Hành vi, Lớp (Class/Blueprint) vs Đối tượng (Object/Instance trong RAM), 3 trụ cột (Đóng gói, Kế thừa, Đa hình), nguyên lý Tái sử dụng phần mềm (Software Reuse).
* **Nhóm 5 (Câu 26 -- 29):** Lịch sử C# (Microsoft, Anders Hejlsberg, năm 2000, nguồn gốc dấu `#` và 4 dấu cộng `++`), các đặc trưng: Pure OOP, Type-safe, Garbage Collection (GC) thu gom rác tự động, `async`/`await`.
* **Nhóm 6 (Câu 30 -- 34):** Kiến trúc Microsoft .NET: Thư viện lớp FCL, Máy ảo CLR, Mã được quản lý (Managed Code) vs Mã không quản lý (Unmanaged Code), Mã trung gian MSIL và Trình biên dịch tức thời JIT.
* **Nhóm 7 (Câu 35 -- 36):** Tính Độc lập nền tảng (.NET Core / .NET 8) và Khả năng Tương tác đa ngôn ngữ (C#, VB.NET, F# cùng biên dịch ra MSIL).
* **Nhóm 8 (Câu 37 -- 40):** Môi trường Visual Studio IDE (Solution `.sln` vs Project `.csproj`), Lập trình trực quan và Hướng sự kiện (Event-Driven, Event Loop), Case Study ứng dụng Painter (GroupBox, RadioButton độc quyền, Panel vùng vẽ, Button).

---

## IV. DANH MỤC 29 BÀI TẬP GIÁO TRÌNH C# (CHUYỂN NGỮ TIẾNG VIỆT & KÈM HÌNH)

1. **Self-Review Exercises 1.1:** Điền vào chỗ trống về Máy tính, Phần cứng, Phân cấp dữ liệu và Ngôn ngữ máy *(Kèm Hình 1.2)*.
2. **Self-Review Exercises 1.2:** Điền vào chỗ trống về Công nghệ đối tượng, Lớp, Lời gọi phương thức, Kế thừa và C# hướng sự kiện *(Kèm Hình 1.10)*.
3. **Self-Review Exercises 1.3:** Điền vào chỗ trống về CLR, Managed Code, Độc lập nền tảng, IDE Visual Studio *(Kèm Hình 1.8)*.
4. **Self-Review Exercises 1.4:** Đúng / Sai cho 12 nhận định toàn diện Chương 1 (Bộ nhớ thứ cấp, gói tin TCP packets, ASP.NET...).
5. **Self-Review Exercises 1.5:** Sắp xếp thứ tự các đơn vị đo lường byte tăng dần từ KB đến PB *(Kèm Bảng Hình 1.4)*.
6. **Self-Review Exercises 1.6:** Mô tả chu trình biên dịch hai giai đoạn: C# Source $\to$ MSIL $\to$ JIT $\to$ Machine code.
7. **Exercises 1.7:** Điền vào chỗ trống về Khối logic, Hệ thống nhúng, Trường dữ liệu, Hệ điều hành và Tái sử dụng *(Kèm Hình 1.3)*.
8. **Exercises 1.8:** Điền vào chỗ trống về UML, World Wide Web, Máy ảo CLR, Chuyển mã Porting, Microsoft Azure và Reuse *(Kèm Hình 1.13)*.
9. **Exercises 1.9:** Đúng / Sai cho 9 nhận định mở rộng (Giá trị bit 0-1, Unicode siêu tập của ASCII, C# đa nền tảng...).
10. **Exercises 1.10:** Ưu điểm và nhược điểm then chốt của Trình thông dịch (Interpreter) so với Trình biên dịch (Compiler).
11. **Exercises 1.11:** Ưu thế của tính năng `async`/`await` trong C# so với mô hình đa luồng (multithreading) kiểu cũ.
12. **Exercises 1.12:** Định luật Moore đã nâng cao năng lực của máy tính cá nhân và thiết bị di động như thế nào.
13. **Exercises 1.13:** Tại sao việc thuê tài nguyên điện toán đám mây (Cloud Computing) đôi khi tốt hơn mua phần cứng vật lý.
14. **Exercises 1.14:** Phân loại thành phần: Phần cứng, Phần mềm hay Kết hợp cả hai (Memory Unit, WWW, FCL, ALU, OS).
15. **Exercises 1.15:** Đúng hay Sai về ứng dụng .NET và Thư viện lớp FCL (4 nhận định).
16. **Exercises 1.16:** Viết dạng đầy đủ và giải nghĩa các từ viết tắt chuyên ngành: ASCII, JITC, TCP/IP, OOAD, UWP, GPS.
17. **Exercises 1.17:** Lợi ích then chốt và hạn chế / điểm đánh đổi của nền tảng .NET và máy ảo CLR.
18. **Exercises 1.18:** Quy trình phân tích và thiết kế hướng đối tượng (OOAD) giúp xây dựng hệ thống lớn ra sao.
19. **Exercises 1.19:** Phân tích sâu sắc ẩn dụ chiếc xe ô tô trong lập trình hướng đối tượng *(Kèm Hình 1.2 Part 2)*.
20. **Exercises 1.20:** Thành tựu then chốt mang tính lịch sử của Ngôn ngữ Mô hình hóa Hợp nhất (UML).
21. **Exercises 1.21:** Lợi ích hàng đầu của mạng Internet trong giai đoạn sơ khai (ARPANET).
22. **Exercises 1.22:** Năng lực then chốt của World Wide Web trong chia sẻ thông tin toàn cầu.
23. **Exercises 1.23:** Tầm nhìn kiến trúc cốt lõi của sáng kiến Microsoft .NET.
24. **Exercises 1.24:** Thư viện lớp FCL tạo thuận lợi và tăng tốc quy trình phát triển ứng dụng .NET ra sao.
25. **Exercises 1.25:** Lợi ích lớn khác của OOP bên cạnh việc tái sử dụng phần mềm (Tính dễ bảo trì và khả năng mở rộng).
26. **Making-a-Difference 1.26:** Dự án Chạy thử: Máy tính Dấu chân Carbon (Carbon Footprint Calculator) & Công thức tính phát thải CO₂.
27. **Making-a-Difference 1.27:** Dự án Chạy thử: Máy tính Chỉ số khối cơ thể (BMI Calculator) & Logic phân loại WHO.
28. **Making-a-Difference 1.28:** Phân tích Hướng đối tượng: Các thuộc tính động cơ và bộ pin của Lớp Xe lai điện (`HybridVehicle`).
29. **Making-a-Difference 1.29:** Thuật toán Xử lý ngôn ngữ trung tính giới tính, phân tích lỗi 'woperchild' và giải pháp Regex / Trie.

---

## V. TỔNG KẾT VÀ KIỂM TRA ĐỒNG BỘ
* Website hoạt động trơn tru tại địa chỉ local `http://127.0.0.1:5500/index.html` và sẵn sàng triển khai trên GitHub Pages.
* Không có lỗi console JavaScript; dữ liệu câu hỏi trắc nghiệm, bài tập có hình ảnh và kịch bản thuyết minh được nạp chính xác 100%.

