# KẾ HOẠCH BÀI GIẢNG VÀ THIẾT KẾ SLIDE BÀI GIẢNG ĐẠI HỌC
## HỌC PHẦN: KỸ THUẬT LẬP TRÌNH (PROGRAMMING TECHNIQUES - C#)
### BÀI 4 (BUỔI 4): CHƯƠNG 2: NỀN TẢNG VỀ NGÔN NGỮ LẬP TRÌNH (TIẾP THEO)
#### BIỂU THỨC, CÁC PHÉP TOÁN, THAO TÁC BIT, CHUYỂN ĐỔI KIỂU DỮ LIỆU VÀ CÂU LỆNH GÁN

- **Đơn vị đào tạo:** Khoa Công nghệ Thông tin -- Trường Đại học Đông Á (UDA)  
- **Đối tượng người học:** Sinh viên năm nhất -- Lớp IT26M (Khóa tuyển sinh 2026)  
- **Thời lượng giảng dạy:** 01 buổi (03 tiết = 150 phút, tích hợp lý thuyết bản chất, phân tích code và thực hành trực tiếp)  
- **Vị trí học phần trong CTĐT:** Học phần cơ sở cốt lõi (04 tín chỉ -- 165 giờ học tập: 30 giờ lý thuyết, 15 giờ bài tập/thực hành tại lớp, 15 giờ thực tế/doanh nghiệp, 105 giờ tự học).  
- **Căn cứ đề cương chi tiết:** Đề cương học phần `CNTT.2026.27. Kỹ thuật lâp trình_C#_SV.pdf` (Mục 6, Bảng 6.1 -- Bài 4).  
- **Tài liệu tham khảo chuyên môn:**
  1. Đề cương chi tiết học phần Kỹ thuật lập trình C# (Khoa CNTT - Đại học Đông Á).
  2. Slide bài giảng và hướng dẫn thực hành đã hoàn thành: `Slides_CShape/Slide_Huong_Dan_Thuc_Hanh_CSharp_Chuong_1_den_3.pdf` & `Lab/Huong-Dan-Thuc-Hanh-Lap-Trinh-CSharp-Chuong-1-den-3-v2.docx`.
  3. Textbook chuẩn quốc tế: *Visual C# How to Program (6th Edition)* -- Paul Deitel & Harvey Deitel (Chương 3 & 4).
- **Thư mục lưu trữ kế hoạch:** `I:\Course_UDA\Kỹ thuật lập trình\ebooks\new ebooks\WebProgramingTechnique2026\devPlan\`
- **Tệp kế hoạch:** `DevPlan_Buoi_04_CSharp_IT26M.md`

---

## I. BỐI CẢNH SƯ PHẠM VÀ ĐỊNH HƯỚNG TIẾP CẬN

### 1. Phân tích bối cảnh người học (Lớp IT26M sau Buổi 1, 2, 3 và Thực hành Lab 01)
- **Kiến thức đã tích lũy:**
  - *Buổi 1 (Chương 1):* Đã làm quen với tư duy "Bài toán - Thuật toán - Chương trình", cấu trúc nền tảng .NET và IDE Visual Studio.
  - *Buổi 2 (Chương 2):* Đã nắm được cấu trúc một ứng dụng Console Application, hàm `Main()`, các từ khóa cơ bản, quy tắc viết mã nguồn và biên dịch.
  - *Buổi 3 (Chương 2):* Đã học về các kiểu dữ liệu nguyên thủy (`int`, `double`, `char`, `string`, `bool`), khái niệm biến, hằng số (`const`), lệnh nhập `Console.ReadLine()` và xuất `Console.WriteLine()`.
  - *Buổi thực hành Lab 01 (Tổng hợp Chương 1-3):* Sinh viên đã trực tiếp gõ mã và chạy các bài toán số học đơn giản (tính chu vi diện tích hình chữ nhật/hình tròn, tách chữ số, đổi giây ra giờ-phút-giây, kiểm tra chẵn lẻ, so sánh 2 số).
- **Thực trạng và rào cản nhận thức của sinh viên năm nhất sau Lab 01:**
  - Sinh viên thường làm bài theo dạng "thuộc lòng mẫu cú pháp" nhưng **chưa hiểu sâu bản chất xử lý của máy tính và bộ nhớ**.
  - Rất hay gặp lỗi chia nguyên mất dữ liệu (ví dụ: `double x = 5 / 2;` ra `2.0` thay vì `2.5`).
  - Lẫn lộn giữa phép gán `=` và phép so sánh bằng `==`.
  - Chưa phân biệt được toán tử logic đoản mạch (`&&`, `||`) với toán tử logic không đoản mạch (`&`, `|`).
  - Gặp bế tắc khi gặp các biểu thức có toán tử tăng giảm tiền tố/hậu tố (`++x`, `x++`).
  - Chưa từng làm việc với cấp độ bit/byte nhị phân, dẫn đến sợ hãi khi nghe đến thao tác bit (Bitwise).
  - Hoàn toàn chưa có ý thức về nguy cơ tràn số (Integer Overflow) khi thực hiện các phép nhân/cộng dữ liệu lớn.

### 2. Định hướng sư phạm cốt lõi: "TẠI SAO TUYỆT ĐỐI CHƯA DẠY HƯỚNG ĐỐI TƯỢNG (OOP) VÀO LÚC NÀY?"
1. **Tránh quá tải nhận thức (Cognitive Overload):**
   - Sinh viên năm nhất chưa có nền tảng vững vàng về luồng điều khiển, kiểu dữ liệu và mô hình bộ nhớ. Nếu đưa ngay các khái niệm trừu tượng như Lớp (Class), Đối tượng (Object), Khởi tạo (`new`), Đóng gói (Encapsulation), Kế thừa (Inheritance), Đa hình (Polymorphism)... sinh viên sẽ bị choáng ngợp, dẫn đến việc "học vẹt", sao chép mã mà không hiểu chương trình hoạt động thế nào.
2. **Tuân thủ chặt chẽ chuẩn mực Đề cương Đại học Đông Á:**
   - Theo Bảng 6.1 của Đề cương chi tiết:
     - **Bài 4:** Nền tảng về ngôn ngữ lập trình (Biểu thức, toán tử, thao tác bit, ép kiểu, câu lệnh gán).
     - **Bài 5 & 6:** Hàm và cấu trúc chương trình (Chia nhỏ chương trình thành các hàm thủ tục, truyền tham số `ref`/`out`, Generic hàm cơ bản).
     - **Bài 7, 8, 9:** Cấu trúc điều khiển (Lưu đồ thuật toán, rẽ nhánh `if-else`, `switch-case`, các vòng lặp `for`, `while`, `do-while`).
     - **Lập trình Hướng đối tượng:** Được thiết kế dành riêng cho học phần tiếp theo (hoặc giai đoạn sau khi đã vững lập trình thủ tục).
3. **Mục tiêu chiến lược của Buổi 04:**
   - Đóng vai trò là **"Trụ cột rèn luyện kỹ thuật cơ bản" (Foundational Procedural Backbone)**.
   - Toàn bộ mã nguồn minh họa đều viết dạng **Lập trình cấu trúc / thủ tục (Procedural Programming)** bên trong lớp chứa đơn giản `class Program` và phương thức `static void Main()`.
   - Giúp sinh viên nắm chắc 100% cách máy tính lưu trữ bit, tính toán biểu thức, ép kiểu dữ liệu và thứ tự ưu tiên, xây dựng nền tảng tư duy toán-tin vững chắc trước khi bước vào học Hàm (Buổi 5).

---

## II. MỤC TIÊU BÀI HỌC (COURSE LEARNING OUTCOMES - CLOs)

Kết thúc Buổi 4 (150 phút), sinh viên đạt được các chuẩn đầu ra sau theo thang đo nhận thức Bloom:

| Mã CLO | Mô tả Chuẩn đầu ra bài học | Thang đo Bloom | CĐR HP (Bảng 3.1) |
| :--- | :--- | :---: | :---: |
| **CLO 4.1** | **Trình bày được bản chất của Biểu thức (Expressions) trong C#:** Phân biệt rõ toán tử (operators), toán hạng (operands), giá trị trả về và kiểu dữ liệu của biểu thức; biết chuyển đổi chính xác các công thức toán học/khoa học/kinh tế sang biểu thức C#. | Level 2 (Understand) | CLO1 |
| **CLO 4.2** | **Làm chủ và phân biệt chính xác 4 nhóm toán tử căn bản:**<br>- Nhóm số học (`+`, `-`, `*`, `/`, `%`) -- phân biệt chia nguyên vs chia thực.<br>- Nhóm quan hệ & bình đẳng (`<`, `<=`, `>`, `>=`, `==`, `!=`).<br>- Nhóm logic (`&&`, `||`, `!`, `^`) -- giải thích cơ chế đánh giá đoản mạch (Short-circuit Evaluation).<br>- Nhóm tăng/giảm (`++`, `--`) -- phân biệt tuyệt đối giữa Tiền tố (Prefix) và Hậu tố (Postfix). | Level 3 (Apply) & Level 4 (Analyze) | CLO1 |
| **CLO 4.3** | **Hiểu bản chất và vận dụng được các phép toán Thao tác Bit (Bitwise Operators):**<br>- Hiểu biểu diễn nhị phân, số bù 2 (Two's complement) và các toán tử AND (`&`), OR (`\|`), XOR (`^`), NOT (`~`), dịch bit (`<<`, `>>`).<br>- Ứng dụng thao tác bit vào các bài toán kỹ thuật: kiểm tra số chẵn/lẻ siêu tốc, nhân/chia lũy thừa 2, và kỹ thuật mặt nạ bit (Bitmasking) để quản lý cờ trạng thái/quyền hạn người dùng. | Level 3 (Apply) | CLO1 |
| **CLO 4.4** | **Phân tích và thực hiện chuẩn xác việc Chuyển đổi kiểu dữ liệu (Type Conversion):**<br>- Phân biệt Ép kiểu ngầm định (Implicit Widening) và Ép kiểu tường minh (Explicit Narrowing).<br>- Sử dụng thành thạo toán tử ép kiểu `(type)`, lớp `Convert`, các phương thức `Parse()` và `TryParse()`.<br>- Nhận biết hiện tượng tràn số (Integer Overflow) và sử dụng từ khóa `checked`/`unchecked` để bảo vệ chương trình. | Level 4 (Analyze) | CLO1 |
| **CLO 4.5** | **Vận dụng câu lệnh gán, toán tử gán phức hợp và Bảng thứ tự ưu tiên:**<br>- Sử dụng thuần thục các toán tử gán phức hợp (`+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `|=`, `<<=`, `>>=`).<br>- Thuộc và vận dụng chính xác bảng thứ tự ưu tiên (Precedence) và hướng kết hợp (Associativity); hình thành thói quen dùng ngoặc đơn `()` để viết biểu thức trong sáng. | Level 3 (Apply) | CLO1, CLO5 |

---

## III. PHÂN BỔ THỜI GIAN & TIẾN TRÌNH DẠY HỌC (3 TIẾT = 150 PHÚT)

```text
========================================================================================================
TIẾT 1 (50 PHÚT): BIỂU THỨC, CÁC PHÉP TOÁN CƠ BẢN VÀ CẠM BẪY TOÁN TỬ TĂNG/GIẢM
--------------------------------------------------------------------------------------------------------
00' - 05' (05p): Khởi động buổi học, kết nối kinh nghiệm từ Lab 01, công bố 5 CLOs của Buổi 4.
05' - 15' (10p): 2.9 Biểu thức (Expressions) trong C#: Cấu tạo toán tử + toán hạng, giá trị và kiểu trả về.
15' - 25' (10p): 2.10.1 Toán tử số học nâng cao: Chia nguyên vs chia thực, toán tử chia dư `%`, số thực IEEE 754.
25' - 35' (10p): 2.10.2 Toán tử so sánh & Toán tử logic: Cơ chế đoản mạch (Short-circuit) `&&`, `||` vs `&`, `|`.
35' - 45' (10p): 2.10.3 Toán tử tăng/giảm: Phân tích cơ chế bộ nhớ giữa Tiền tố (`++x`) và Hậu tố (`x++`).
45' - 50' (05p): [CHECKPOINT 1] Bài tập nhanh trắc nghiệm & dự đoán kết quả in ra màn hình.
--------------------------------------------------------------------------------------------------------
TIẾT 2 (50 PHÚT): THAO TÁC BIT (BITWISE), CƠ CHẾ BÙ 2 VÀ KỸ THUẬT MẶT NẠ BIT (BITMASK)
--------------------------------------------------------------------------------------------------------
50' - 60' (10p): 2.11.1 Bản chất nhị phân trong máy tính: Bit, Byte, biểu diễn số bù 2 (Two's Complement).
60' - 75' (15p): 2.11.2 Các toán tử bitwise: AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), dịch bit (`<<`, `>>`).
75' - 90' (15p): 2.11.3 Ứng dụng thực tế của Bitwise:
                 - Kiểm tra chẵn lẻ bằng `(n & 1) == 0`.
                 - Nhân/chia lũy thừa 2 bằng phép dịch bit `n << k`, `n >> k`.
                 - Kỹ thuật mặt nạ bit (Bitmasking): Bật, tắt, kiểm tra cờ trạng thái (Permission Flags).
90' - 100' (10p): [CHECKPOINT 2] Thao tác trực tiếp trên máy: Viết chương trình quản lý quyền hạn tệp tin bằng bit.
--------------------------------------------------------------------------------------------------------
GIẢI LAO GIỮA GIỜ (10 PHÚT) - Cho sinh viên thư giãn não bộ trước phần ép kiểu phức tạp
--------------------------------------------------------------------------------------------------------
TIẾT 3 (50 PHÚT): CHUYỂN ĐỔI KIỂU, BẢO VỆ TRÀN SỐ, TOÁN TỬ GÁN & TỔNG KẾT
--------------------------------------------------------------------------------------------------------
100' - 115' (15p): 2.12 Chuyển đổi kiểu dữ liệu (Type Conversion):
                   - Ép kiểu ngầm định (Implicit Widening) vs Ép kiểu tường minh (Explicit Narrowing).
                   - So sánh `(int)x` vs `Convert.ToInt32()` vs `int.Parse()` / `int.TryParse()`.
115' - 125' (10p): Hiện tượng tràn số (Integer Overflow) & Cặp từ khóa bảo vệ `checked` / `unchecked`.
125' - 135' (10p): 2.13 Câu lệnh gán, Biểu thức gán & Toán tử gán phức hợp (`+=`, `*=`, `<<=`, ...).
135' - 145' (10p): Bảng thứ tự ưu tiên (Precedence) & Hướng kết hợp (Associativity) - Quy tắc dùng dấu ngoặc `()`.
145' - 150' (05p): [TỔNG KẾT & GIAO BÀI TẬP] Review checklist CLOs, giới thiệu bài tập về nhà và cầu nối Buổi 5 (Hàm).
========================================================================================================
```

---

## IV. CẤU TRÚC CHI TIẾT HỆ THỐNG SLIDE DỰ KIẾN (42 SLIDES)

Slide được biên soạn để xuất bản dưới dạng Slide bài giảng đại học tỷ lệ 16:9, chuẩn giao diện học thuật (Dark Navy / Indigo / Cyan):

### PHẦN 1: MỞ ĐẦU & TỔNG QUAN (Slide 01 -- 04)
- **Slide 01: [Trang bìa]**
  - Tiêu đề: **BÀI 4: BIỂU THỨC, CÁC PHÉP TOÁN, THAO TÁC BIT VÀ CHUYỂN ĐỔI KIỂU DỮ LIỆU**
  - Phụ đề: *Chương 2 (Tiếp theo): Nền tảng về ngôn ngữ lập trình C#*
  - Giảng viên & Khoa: Khoa Công nghệ Thông tin -- Đại học Đông Á
  - Đối tượng: Lớp IT26M -- Khóa 2026.
- **Slide 02: [Bối cảnh kết nối] Từ Lab 01 đến Buổi 04**
  - Điểm lại thành quả Lab 01: Đã nhập xuất, tính toán cơ bản, làm quen cấu trúc rẽ nhánh `if`.
  - Vấn đề nảy sinh trong Lab 01: Lỗi chia $5/2 = 2$, nhầm lẫn gán `=` và so sánh `==`, bối rối trước tràn số.
  - Sứ mệnh Buổi 04: "Làm chủ máy tính từ cấp độ Bit, Toán tử đến Biểu thức an toàn".
- **Slide 03: [Mục tiêu bài học] 5 Chuẩn đầu ra (CLO 4.1 -- CLO 4.5)**
  - Trình bày dạng bảng trực quan tương ứng với thang đo Bloom và CĐR học phần UDA.
- **Slide 04: [Lộ trình bài giảng - Agenda]**
  - 5 chặng đường kiến thức: Biểu thức $\to$ Các phép toán $\to$ Thao tác Bit $\to$ Chuyển đổi kiểu $\to$ Toán tử gán & Thứ tự ưu tiên.

---

### PHẦN 2: MỤC 2.9 -- BIỂU THỨC TRONG C# (EXPRESSIONS) (Slide 05 -- 08)
- **Slide 05: [Khái niệm] Biểu thức là gì?**
  - Định nghĩa chuẩn: Biểu thức là sự kết hợp có quy tắc giữa **toán tử (operators)**, **toán hạng (operands - biến, hằng, literal, lời gọi hàm)** để tính ra **một giá trị duy nhất** thuộc một kiểu dữ liệu xác định.
  - Sơ đồ giải phẫu biểu thức: `c = a + b * 2;` (chỉ ra đâu là toán tử, toán hạng, giá trị tính toán).
- **Slide 06: [Phân loại biểu thức]**
  - Biểu thức số học (Arithmetic Expressions): Kết quả là số (`int`, `double`, `decimal`).
  - Biểu thức quan hệ/logic (Boolean Expressions): Kết quả là `true` hoặc `false`.
  - Biểu thức chuỗi (String Expressions): Thao tác ghép chuỗi (`+`, Interpolation `$"..."`).
- **Slide 07: [Chuyển đổi công thức thực tế sang C#]**
  - Minh họa các công thức toán - lý - kinh tế:
    - Công thức Heron: $S = \sqrt{p(p-a)(p-b)(p-c)} \to$ `Math.Sqrt(p * (p - a) * (p - b) * (p - c))`
    - Phương trình bậc 2 (Delta): $\Delta = b^2 - 4ac \to$ `delta = b * b - 4 * a * c`
    - Lãi kép: $A = P(1 + r)^t \to$ `A = P * Math.Pow(1 + r, t)`
- **Slide 08: [Bài học kinh nghiệm] Biểu thức không hoàn chỉnh và tác dụng phụ (Side-effects)**
  - Khái niệm biểu thức có tác dụng phụ: Biểu thức vừa trả về giá trị, vừa làm thay đổi trạng thái của ô nhớ (ví dụ: `x++`, `a = b + 1`).
  - Lời khuyên viết mã: Tránh viết các biểu thức quá phức tạp gây khó hiểu (Keep It Simple).

---

### PHẦN 3: MỤC 2.10 -- CÁC PHÉP TOÁN TRONG C# (OPERATORS) (Slide 09 -- 17)
- **Slide 09: [Tổng quan các nhóm phép toán]**
  - Phân loại theo số lượng toán hạng: Toán tử 1 ngôi (Unary), 2 ngôi (Binary), 3 ngôi (Ternary `? :`).
  - Phân loại theo chức năng: Số học, So sánh, Logic, Tăng/giảm, Thao tác bit, Gán.
- **Slide 10: [Toán tử số học] Đào sâu phép chia `/` và chia dư `%`**
  - Cạm bẫy chia nguyên: `int / int` luôn cho kết quả `int` (cắt cụt phần thập phân, truncation towards zero).
  - So sánh:
    - `7 / 2` cho kết quả `3`
    - `7.0 / 2` hoặc `7 / 2.0` cho kết quả `3.5`
  - Ý nghĩa thực tế của toán tử modulo `%`:
    - Tìm chữ số cuối cùng (`n % 10`), kiểm tra bội số, kiểm tra tính chẵn lẻ (`n % 2 == 0`), thuật toán vòng tròn tuần hoàn (circular buffer: `index = (index + 1) % MAX`).
- **Slide 11: [Toán tử so sánh (Relational & Equality)]**
  - Bảng tra cứu: `<`, `<=`, `>`, `>=`, `==`, `!=`.
  - Cảnh báo bẫy tử huyệt số 1 của sinh viên: **Nhầm lẫn giữa `=` (phép gán) và `==` (so sánh bằng)**.
  - So sánh hai số thực dấu phẩy động (`double`): Tại sao KHÔNG NÊN so sánh `d1 == d2` mà phải dùng sai số $\epsilon$: `Math.Abs(d1 - d2) < 1e-9`.
- **Slide 12: [Toán tử Logic] Bảng chân trị và các phép `&&`, `||`, `!`, `^`**
  - Phép VÀ (`&&`): Đúng khi cả hai cùng đúng.
  - Phép HOẶC (`||`): Đúng khi có ít nhất một vế đúng.
  - Phép PHỦ ĐỊNH (`!`): Đảo ngược giá trị logic.
  - Phép XOR logic (`^`): Đúng khi đúng một trong hai (khác nhau).
- **Slide 13: [Chuyên sâu kỹ thuật] Cơ chế đánh giá đoản mạch (Short-Circuit Evaluation)**
  - Cơ chế hoạt động của `&&`: Nếu vế trái là `false`, C# **dừng ngay lập tức** và không bao giờ tính toán vế phải.
  - Cơ chế hoạt động của `||`: Nếu vế trái là `true`, C# **dừng ngay lập tức** và không bao giờ tính toán vế phải.
  - Phân biệt với `&` và `|` (Toán tử logic không đoản mạch - luôn tính cả 2 vế).
  - Ứng dụng sống còn: Tránh lỗi chia cho 0 hoặc tham chiếu null:
    - `if (b != 0 && a / b > 2)` $\to$ An toàn 100%, không bao giờ bị `DivideByZeroException`!
- **Slide 14: [Toán tử tăng/giảm] Tiền tố (`++x`) vs Hậu tố (`x++`)**
  - Định nghĩa bản chất:
    - `++x` (Prefix - Tiền tố): Tăng giá trị của `x` lên 1 TRƯỚC, sau đó mới lấy giá trị mới đưa vào biểu thức.
    - `x++` (Postfix - Hậu tố): Lấy giá trị HIỆN TẠI của `x` đưa vào biểu thức TRƯỚC, sau đó mới tăng `x` lên 1.
  - Tương tự cho giảm tiền tố `--x` và giảm hậu tố `x--`.
- **Slide 15: [Mổ xẻ bộ nhớ] Minh họa từng bước (Trace Step-by-Step) của `++`**
  - So sánh trực quan:
    ```csharp
    int a = 5; int b = ++a; // a = 6, b = 6
    int c = 5; int d = c++; // c = 6, d = 5
    ```
  - Sơ đồ ô nhớ RAM giải thích quá trình lưu tạm (temporary evaluation).
- **Slide 16: [Thử thách câu hỏi bẫy] Phân tích biểu thức phức tạp**
  - Phân tích: `int x = 10; int y = x++ + ++x;` $\to$ Kết quả `y` và `x` bằng bao nhiêu? (Giải thích bước: $10 + 12 = 22, x = 12$).
  - Lời khuyên chuẩn mực công nghiệp: "KHÔNG BAO GIỜ viết code lạm dụng `++` nhiều lần trong cùng một câu lệnh" (Unspecified behavior / Code smell).
- **Slide 17: [Checkpoint Tiết 1] Mini-Quiz củng cố**
  - 3 câu trắc nghiệm nhanh kiểm tra nhận thức Tiết 1.

---

### PHẦN 4: MỤC 2.11 -- CÁC PHÉP TOÁN THAO TÁC BIT (BITWISE OPERATORS) (Slide 18 -- 25)
- **Slide 18: [Bản chất máy tính] Thế giới nhị phân (Binary) và Biểu diễn số nguyên**
  - Máy tính chỉ hiểu 0 và 1 (Điện áp cao/thấp).
  - Kiểu `byte` (8 bit), `short` (16 bit), `int` (32 bit), `long` (64 bit).
  - Khái niệm bit có trọng số lớn nhất (MSB - Most Significant Bit) và nhỏ nhất (LSB - Least Significant Bit).
  - Biểu diễn số nguyên có dấu: Mã bù 2 (Two's Complement) -- cách máy tính biểu diễn số âm.
- **Slide 19: [Toán tử AND bit (`&`) và OR bit (`|`)]**
  - Phép `&`: Bit kết quả là 1 khi và chỉ khi cả 2 bit tương ứng là 1 (Ứng dụng: Lọc bit, xóa bit).
  - Phép `|`: Bit kết quả là 1 khi có ít nhất 1 bit tương ứng là 1 (Ứng dụng: Gộp bit, bật bit).
  - Ví dụ tính toán cụ thể trên giấy với 2 số: $12$ (`0000 1100`) và $10$ (`0000 1010`).
- **Slide 20: [Toán tử XOR bit (`^`) và NOT bit (`~`)]**
  - Phép XOR bit `^`: Bit kết quả là 1 khi 2 bit khác nhau; bằng 0 khi 2 bit giống nhau (Ứng dụng: Đảo trạng thái bit, mã hóa đơn giản, hoán đổi 2 số không cần biến phụ).
  - Phép NOT bit `~` (Bù 1): Đảo tất cả các bit: 0 thành 1, 1 thành 0.
  - Công thức bù 2 trong C#: `~x = -(x + 1)`.
- **Slide 21: [Toán tử Dịch Bit (Shift Operators)] `<<` và `>>`**
  - Dịch trái `x << k`: Đẩy các bit sang trái $k$ vị trí, chèn các bit 0 vào bên phải.
    - *Ý nghĩa toán học:* Tương đương phép nhân $x \times 2^k$ (nhanh vượt trội so với phép nhân số học).
  - Dịch phải `x >> k`: Đẩy các bit sang phải $k$ vị trí.
    - *Ý nghĩa toán học:* Tương đương phép chia nguyên $x / 2^k$.
  - Dịch bit số học (Arithmetic shift giữ dấu cho số âm).
- **Slide 22: [Ứng dụng Kỹ thuật 1] Tối ưu thuật toán cơ bản bằng Bitwise**
  - 1. Kiểm tra số chẵn lẻ siêu tốc: `if ((n & 1) == 0)` $\to$ Kiểm tra LSB, nhanh hơn `n % 2 == 0`.
  - 2. Kiểm tra một số nguyên dương có phải lũy thừa của 2: `(n > 0) && ((n & (n - 1)) == 0)`.
  - 3. Nhân chia nhanh: `x << 1` (nhân 2), `x >> 1` (chia 2).
- **Slide 23: [Ứng dụng Kỹ thuật 2] Kỹ thuật Mặt nạ bit (Bitmasking) & Quản lý cờ trạng thái**
  - Bài toán thực tế: Quản lý quyền truy cập tệp tin (File Permissions):
    - Đọc (Read) = 1 (`001`)
    - Ghi (Write) = 2 (`010`)
    - Thực thi (Execute) = 4 (`100`)
  - Bật quyền (Set): `permissions = permissions | WRITE;`
  - Tắt quyền (Clear): `permissions = permissions & (~WRITE);`
  - Đảo quyền (Toggle): `permissions = permissions ^ WRITE;`
  - Kiểm tra quyền (Check): `bool canWrite = (permissions & WRITE) != 0;`
- **Slide 24: [Code Walkthrough] Chương trình Console quản lý phân quyền bằng Bitwise**
  - Trình bày mã nguồn chuẩn mực, rõ ràng, thực thi và in kết quả nhị phân ra màn hình bằng `Convert.ToString(val, 2).PadLeft(8, '0')`.
- **Slide 25: [Checkpoint Tiết 2] Thực hành tay đôi (Pair Coding mini)**
  - Sinh viên làm bài tập 5 phút: Viết biểu thức bitwise kiểm tra xem bit thứ 3 của một số nguyên có đang bật hay không.

---

### PHẦN 5: MỤC 2.12 -- CHUYỂN ĐỔI KIỂU DỮ LIỆU (TYPE CONVERSION) (Slide 26 -- 32)
- **Slide 26: [Vấn đề cốt lõi] Tại sao cần chuyển đổi kiểu dữ liệu?**
  - C# là ngôn ngữ kiểm tra kiểu tĩnh mạnh mẽ (Strongly-typed & Type-safe).
  - Dữ liệu nhập từ bàn phím luôn là `string`, cần đổi sang `int`, `double` để tính toán.
  - Kết quả phép chia hai số nguyên cần được lưu trữ ở biến số thực `double`.
- **Slide 27: [Ép kiểu ngầm định] Implicit Type Conversion (Widening)**
  - Xảy ra tự động khi chuyển từ kiểu có miền giá trị nhỏ hơn sang kiểu lớn hơn, **hoàn toàn an toàn và không mất mát dữ liệu**.
  - Chuỗi chuyển đổi an toàn: `byte` $\to$ `short` $\to$ `int` $\to$ `long` $\to$ `float` $\to$ `double`.
  - Ví dụ: `int a = 100; double b = a;`
- **Slide 28: [Ép kiểu tường minh] Explicit Casting (Narrowing)**
  - Bắt buộc lập trình viên phải chủ động chỉ định kiểu đích trong dấu ngoặc: `(targetType)value`.
  - Áp dụng khi chuyển từ kiểu lớn sang kiểu nhỏ, hoặc từ số thực sang số nguyên.
  - **Nguy cơ tiềm ẩn:**
    - Mất độ chính xác (Precision Loss): `double pi = 3.14159; int p = (int)pi;` $\to$ `p` nhận giá trị `3` (phần thập phân bị cắt cụt).
    - Tràn số (Overflow): `int big = 300; byte b = (byte)big;` $\to$ `b` nhận giá trị `44` ($300 \pmod{256}$).
- **Slide 29: [So sánh các phương pháp chuyển đổi] Ép kiểu `(type)` vs `Convert` vs `Parse`**
  - Bảng so sánh 3 phương pháp kinh điển trong C#:
    - Toán tử ép kiểu `(type)`: Chỉ áp dụng giữa các kiểu số tương thích.
    - Phương thức `Parse()` (`int.Parse`, `double.Parse`): Chuyên dùng chuyển từ chuỗi văn bản (`string`) sang kiểu số. Ném ra ngoại lệ nếu chuỗi không hợp lệ.
    - Lớp `Convert` (`Convert.ToInt32`, `Convert.ToDouble`): Đa năng, chuyển đổi giữa nhiều kiểu khác nhau, xử lý an toàn với `null` (trả về 0), áp dụng cơ chế làm tròn ngân hàng (Banker's Rounding).
- **Slide 30: [Kỹ thuật nâng cao] Chuyển đổi an toàn với `TryParse()`**
  - Giới thiệu phương thức phòng thủ: `int.TryParse(input, out int result)`.
  - Giải thích tại sao `TryParse()` ưu việt hơn `Parse()`: Không làm chương trình bị sập (crash) khi người dùng nhập sai định dạng.
- **Slide 31: [Bảo vệ chống tràn số] Khối `checked` và `unchecked`**
  - Mặc định trong C#: Các phép toán số nguyên diễn ra ở chế độ `unchecked` (tràn số âm thầm, không báo lỗi, vòng tròn số nguyên).
  - Hậu quả nghiêm trọng trong các hệ thống tài chính/y tế/hàng không.
  - Giải pháp C#: Sử dụng từ khóa `checked` để ép phát sinh ngoại lệ `System.OverflowException` khi xảy ra tràn số:
    ```csharp
    checked {
        int max = int.MaxValue;
        int err = max + 1; // Ném ngoại lệ System.OverflowException!
    }
    ```
- **Slide 32: [Tổng kết quy tắc chuyển đổi] 4 nguyên tắc vàng**
  - 1. Luôn ưu tiên ngầm định nếu có thể.
  - 2. Ép kiểu số thực trước phép chia để tránh chia nguyên: `double avg = (double)sum / count;`.
  - 3. Dùng `TryParse()` cho dữ liệu nhập từ bên ngoài.
  - 4. Dùng `checked` cho các phép tính nhạy cảm về tràn số.

---

### PHẦN 6: MỤC 2.13 -- CÂU LỆNH GÁN, TOÁN TỬ GÁN & THỨ TỰ ƯU TIÊN (Slide 33 -- 40)
- **Slide 33: [Bản chất phép gán] Toán tử gán đơn thuần (`=`)**
  - Cú pháp: `variable = expression;`
  - Quy tắc thực thi: Vế phải (RHS - Right Hand Side) luôn được **đánh giá và tính toán hoàn chỉnh trước**, sau đó giá trị mới được **ghi đè vào vùng nhớ** của biến ở vế trái (LHS - Left Hand Side).
  - Vế trái bắt buộc phải là một biến (L-value / vị trí nhớ có thể ghi được), không thể là hằng số hay biểu thức (`5 = a;` là lỗi biên dịch).
- **Slide 34: [Toán tử gán phức hợp] Compound Assignment Operators**
  - Khái niệm: Viết ngắn gọn và tối ưu cho thao tác cập nhật biến dựa trên giá trị hiện tại.
  - Nhóm số học: `+=`, `-=`, `*=`, `/=`, `%=`.
  - Nhóm bitwise: `&=`, `|=`, `^=`, `<<=`, `>>=`.
  - Phân tích tương đương: `x += 5;` tương đương `x = x + 5;`.
- **Slide 35: [Điểm tinh tế của toán tử gán phức hợp] Tự động ép kiểu**
  - Phân tích ví dụ sâu sắc:
    ```csharp
    byte b = 10;
    b = (byte)(b + 5); // Phải ép kiểu tường minh vì b + 5 ra int
    b += 5;            // Hợp lệ 100%! C# tự động ép kiểu ngầm định về byte
    ```
- **Slide 36: [Biểu thức gán chuỗi & Hướng kết hợp phải-sang-trái]**
  - Gán nhiều biến cùng lúc: `a = b = c = 100;`
  - C# thực hiện từ phải sang trái (Right-to-Left): `c = 100` tính trước $\to$ gán cho `b` $\to$ gán cho `a`.
- **Slide 37: [Bảng tổng hợp Thứ tự ưu tiên (Precedence Table)]**
  - Trình bày bảng phân cấp 8 tầng ưu tiên từ cao xuống thấp:
    1. Toán tử chính (Primary): `()`, `x++`, `x--`
    2. Toán tử 1 ngôi (Unary): `++x`, `--x`, `+`, `-`, `!`, `~`, `(type)`
    3. Nhân/chia/dư (Multiplicative): `*`, `/`, `%`
    4. Cộng/trừ (Additive): `+`, `-`
    5. Dịch bit (Shift): `<<`, `>>`
    6. Quan hệ & Bình đẳng (Relational & Equality): `<`, `<=`, `>`, `>=`, `==`, `!=`
    7. Thao tác bit (Bitwise): `&` $\to$ `^` $\to$ `|`
    8. Logic (Logical): `&&` $\to$ `||`
    9. Toán tử điều kiện (Conditional): `? :`
    10. Toán tử gán (Assignment): `=`, `+=`, `-=`, ...
- **Slide 38: [Hướng kết hợp (Associativity)]**
  - Hầu hết toán tử 2 ngôi kết hợp từ Trái sang Phải (Left-to-Right).
  - Ngoại lệ quan trọng kết hợp từ Phải sang Trái (Right-to-Left): Toán tử 1 ngôi, Toán tử điều kiện `?:`, Toán tử gán `=`.
- **Slide 39: [Quy tắc vàng của kỹ sư phần mềm] Đừng đánh đố trí nhớ!**
  - Không bao giờ dựa dẫm vào việc người khác nhớ chính xác bảng ưu tiên 10 cấp.
  - **Quy tắc vàng:** Sử dụng dấu ngoặc đơn `()` để phân nhóm biểu thức một cách tường minh, dễ đọc, dễ bảo trì và loại bỏ 100% rủi ro hiểu nhầm.
- **Slide 40: [Case Study tổng hợp] Phân tích biểu thức phức hợp hoàn chỉnh**
  - Bài toán: Phân tích và tính giá trị biểu thức:
    `int result = 5 + 3 * 2 > 10 && (4 << 1) == 8;`
  - Đi từng bước theo đúng cây phân cấp (Syntax Tree).

---

### PHẦN 7: BÀI TẬP THỬ THÁCH & ĐỊNH HƯỚNG BƯỚC TIẾP THEO (Slide 41 -- 42)
- **Slide 41: [Thử thách tại lớp - Mini-Challenge 10 phút]**
  - Đề bài: Viết một chương trình Console C# nhận vào 1 số nguyên `x`, thực hiện:
    1. Kiểm tra `x` chẵn hay lẻ bằng toán tử bitwise.
    2. Dùng phép dịch bit để in ra giá trị $x \times 8$ và $x / 4$.
    3. Tính trung bình cộng của `x` và $10$ dưới dạng số thực chính xác 2 chữ số thập phân.
    4. Thử cộng `int.MaxValue` với `1` trong khối `checked` để quan sát phản ứng của Visual Studio.
- **Slide 42: [Tổng kết bài học & Cầu nối sang Buổi 05]**
  - Checklist hoàn thành 5 CLOs.
  - Dặn dò hoàn thành bài tập về nhà trong tệp hướng dẫn.
  - Cầu nối sang Buổi 5: *"Tại sao chúng ta không nên viết tất cả mã nguồn trong hàm Main? Làm thế nào để chia nhỏ chương trình thành các Hàm (Functions/Methods) có thể tái sử dụng?"*.

---

## V. HỆ THỐNG MÃ NGUỒN MINH HỌA & CASE STUDIES CHUẨN MỰC

Toàn bộ các ví dụ đều được viết theo phong cách **Lập trình thủ tục chuẩn mực (Procedural C#)**, không lạm dụng OOP, có chú thích chi tiết từng dòng lệnh:

### 1. Case Study 1: Phân biệt `++x` và `x++` trong biểu thức phức tạp
```csharp
using System;

class PrefixVsPostfixDemo
{
    static void Main()
    {
        Console.OutputEncoding = System.Text.Encoding.UTF8;
        Console.WriteLine("=== MINH HỌA TOÁN TỬ TĂNG GIẢM TIỀN TỐ VÀ HẬU TỐ ===");

        // Trường hợp 1: Biểu thức đơn giản
        int a = 5;
        int b = ++a; // a tăng lên 6 trước, sau đó gán 6 cho b
        Console.WriteLine($"Tiền tố: a = 5 -> b = ++a => a = {a}, b = {b}");

        int c = 5;
        int d = c++; // Gán 5 cho d trước, sau đó c mới tăng lên 6
        Console.WriteLine($"Hậu tố:  c = 5 -> d = c++ => c = {c}, d = {d}");

        // Trường hợp 2: Biểu thức số học phức hợp
        int x = 10;
        int result = x++ * 2 + ++x;
        // Phân tích:
        // Bước 1: x++ trả về 10, sau đó x trở thành 11
        // Bước 2: 10 * 2 = 20
        // Bước 3: ++x tăng x từ 11 lên 12, trả về 12
        // Bước 4: 20 + 12 = 32
        Console.WriteLine($"\nBiểu thức: x = 10 -> result = x++ * 2 + ++x");
        Console.WriteLine($"Kết quả: result = {result}, x cuối cùng = {x}");
    }
}
```

### 2. Case Study 2: Làm chủ Thao tác Bit (Bitwise Operators & Bitmasking)
```csharp
using System;

class BitwiseMasteryDemo
{
    static void Main()
    {
        Console.OutputEncoding = System.Text.Encoding.UTF8;
        Console.WriteLine("=== BẬC THẦY THAO TÁC BIT VÀ MẶT NẠ BIT (BITMASK) ===");

        // 1. Kiểm tra số chẵn lẻ bằng Bitwise AND
        int number = 47;
        bool isEven = (number & 1) == 0;
        Console.WriteLine($"Số {number} là: {(isEven ? "Số Chẵn" : "Số Lẻ")}");

        // 2. Nhân / Chia bằng dịch bit
        int val = 12;
        int multipliedBy8 = val << 3; // 12 * 2^3 = 96
        int dividedBy4 = val >> 2;    // 12 / 2^2 = 3
        Console.WriteLine($"\n{val} << 3 (x 8) = {multipliedBy8}");
        Console.WriteLine($"{val} >> 2 (/ 4) = {dividedBy4}");

        // 3. Quản lý quyền hạn hệ thống bằng Bit Flags
        const int PERM_READ    = 1 << 0; // 0001 (1)
        const int PERM_WRITE   = 1 << 1; // 0010 (2)
        const int PERM_EXECUTE = 1 << 2; // 0100 (4)
        const int PERM_DELETE  = 1 << 3; // 1000 (8)

        int userPermission = 0; // Chưa có quyền gì

        // Bật quyền READ và WRITE (Dùng toán tử OR '|')
        userPermission = userPermission | PERM_READ | PERM_WRITE;
        Console.WriteLine($"\nQuyền ban đầu (READ + WRITE): {Convert.ToString(userPermission, 2).PadLeft(4, '0')}");

        // Kiểm tra xem có quyền WRITE không (Dùng toán tử AND '&')
        bool canWrite = (userPermission & PERM_WRITE) != 0;
        Console.WriteLine($"Người dùng có quyền GHI không? {canWrite}");

        // Tắt quyền WRITE (Dùng AND với NOT '~')
        userPermission = userPermission & (~PERM_WRITE);
        Console.WriteLine($"Sau khi tước quyền WRITE:     {Convert.ToString(userPermission, 2).PadLeft(4, '0')}");

        // Đảo quyền EXECUTE (Dùng XOR '^')
        userPermission = userPermission ^ PERM_EXECUTE;
        Console.WriteLine($"Sau khi toggle quyền EXECUTE:  {Convert.ToString(userPermission, 2).PadLeft(4, '0')}");
    }
}
```

### 3. Case Study 3: Chuyển đổi kiểu dữ liệu & Bắt lỗi tràn số với `checked`
```csharp
using System;

class TypeCastingAndOverflowDemo
{
    static void Main()
    {
        Console.OutputEncoding = System.Text.Encoding.UTF8;
        Console.WriteLine("=== CHUYỂN ĐỔI KIỂU DỮ LIỆU VÀ KIỂM SOÁT TRÀN SỐ ===");

        // 1. Cạm bẫy phép chia số nguyên
        int tongDiem = 29;
        int soMon = 4;
        double diemTB_Sai = tongDiem / soMon;               // 29 / 4 = 7 -> gán vào double thành 7.0
        double diemTB_Dung = (double)tongDiem / soMon;       // 29.0 / 4 = 7.25
        Console.WriteLine($"Điểm trung bình (SAI):  {diemTB_Sai}");
        Console.WriteLine($"Điểm trung bình (ĐÚNG): {diemTB_Dung}");

        // 2. Chuyển đổi an toàn với TryParse
        string input = "2026";
        if (int.TryParse(input, out int namHoc))
        {
            Console.WriteLine($"\nChuyển đổi thành công: Năm học = {namHoc}");
        }

        // 3. Hiểm họa tràn số (Integer Overflow)
        Console.WriteLine("\n--- THÍ NGHIỆM TRÀN SỐ ---");
        int maxInt = int.MaxValue; // 2,147,483,647
        Console.WriteLine($"Giá trị cực đại int: {maxInt}");

        // Mặc định (unchecked): Tràn số âm thầm
        int tranSo = maxInt + 1;
        Console.WriteLine($"Cộng 1 khi unchecked (BỊ SAI): {tranSo}"); // Ra số âm: -2,147,483,648

        // Bảo vệ với khối checked
        try
        {
            checked
            {
                Console.WriteLine("Đang thực hiện phép tính trong khối checked...");
                int loiTranSo = maxInt + 1; // Sẽ ném ra ngoại lệ OverflowException
            }
        }
        catch (OverflowException ex)
        {
            Console.WriteLine($"=> BẮT ĐƯỢC LỖI NGUY HIỂM: {ex.Message}");
            Console.WriteLine("Khối checked đã bảo vệ an toàn cho hệ thống phần mềm!");
        }
    }
}
```

---

## VI. BẢNG TỔNG HỢP CÁC BẪY LỖI NHẬN THỨC & GIẢI PHÁP SƯ PHẠM

| STT | Bẫy lỗi sinh viên năm nhất thường gặp | Hậu quả trong chương trình | Giải pháp sư phạm trên lớp |
| :---: | :--- | :--- | :--- |
| **1** | Viết `double x = 5 / 2;` nghĩ rằng `x` sẽ bằng `2.5`. | `x` nhận giá trị `2.0`, mất phần thập phân âm thầm. | Dạy nguyên tắc "Toán tử đánh giá kiểu của toán hạng trước". Bắt buộc ép kiểu ít nhất 1 toán hạng: `(double)5 / 2` hoặc `5.0 / 2`. |
| **2** | Viết `if (x = 5)` thay vì `if (x == 5)`. | Trong C#, compiler chặn lại với lỗi CS0029 (Cannot implicitly convert type 'int' to 'bool'). | Nhấn mạnh sự khác nhau giữa hành động GÁN (`=`) và hành động HỎI SO SÁNH (`==`). Khen ngợi cơ chế an toàn của C# so với C/C++. |
| **3** | Lẫn lộn giữa `&&`, `||` (logic) và `&`, `|` (bitwise). | Dẫn đến lỗi logic hoặc mất cơ chế đoản mạch, gây crash chương trình khi kiểm tra điều kiện kết hợp. | Dùng phép ví von: "Cặp đôi `&&` là nhân viên thông minh (thấy sai là nghỉ ngay), còn `&` là nhân viên máy móc (bắt làm cả 2 dù vô ích)". |
| **4** | Lạm dụng `++x` và `x++` lung tung trong biểu thức dài. | Kết quả tính toán sai lệch, mã nguồn trở thành "thách thức giải đố" không ai bảo trì được. | Nêu chuẩn mực viết mã sạch: Chỉ dùng `x++` độc lập trên một dòng lệnh hoặc trong bước nhảy vòng lặp. |
| **5** | Không biết hiện tượng tràn số nguyên. | Khi làm việc với dữ liệu tích lũy (ví dụ tính giai thừa, nhân tiền tệ), số dương biến thành số âm kỳ quái. | Cho chạy trực tiếp đoạn code `int.MaxValue + 1` để gây sốc nhận thức (Shock pedagogy), sau đó giới thiệu giải pháp `checked` và kiểu `long`. |
| **6** | Ép kiểu từ `double` sang `int` làm tròn sai. | `(int)3.99` ra `3` thay vì `4` (cắt cụt phần thập phân, không làm tròn). | Phân biệt rõ giữa *Cắt cụt (Truncate)* của toán tử `(int)` và *Làm tròn (Round)* của `Math.Round()` hoặc `Convert.ToInt32()`. |

---

## VII. HỆ THỐNG BÀI TẬP TỰ LUYỆN VỀ NHÀ (HOMEWORK ASSIGNMENTS)

### Bài tập 1: Xây dựng biểu thức hình học và vật lý
Viết chương trình Console C# tính toán:
1. Độ dài cạnh huyền tam giác vuông theo định lý Pythagoras: $c = \sqrt{a^2 + b^2}$.
2. Vận tốc và quãng đường rơi tự do sau thời gian $t$ giây: $v = g \times t$, $s = \frac{1}{2} g \times t^2$ (lấy $g = 9.81 m/s^2$).
- *Yêu cầu:* Nhập dữ liệu an toàn bằng `double.TryParse()`, xuất kết quả làm tròn 2 chữ số thập phân.

### Bài tập 2: Tối ưu hóa kiểm tra Bitwise và Hoán đổi giá trị
Viết chương trình không sử dụng biến phụ (No temporary variable) để:
1. Hoán đổi giá trị của 2 số nguyên $a$ và $b$ bằng toán tử XOR bit (`^`).
2. Nhập vào một số nguyên $N$ và một vị trí bit $k$ (từ 0 đến 31). Hãy viết các hàm kiểm tra bit thứ $k$ đang bật hay tắt, bật bit thứ $k$, và tắt bit thứ $k$.

### Bài tập 3: Phòng chống tràn số trong bài toán tài chính
Viết chương trình tính lãi đơn và lãi kép cho một khoản tiền gửi tiết kiệm lớn:
- Vốn gốc $P$ (VNĐ), lãi suất $r$ (%/năm), kỳ hạn gửi $n$ (năm).
- Thử nghiệm với số tiền lớn (hàng tỷ đồng). Đặt toàn bộ phép tính trong khối `checked` để phát hiện ngay lập tức nếu giá trị vượt quá giới hạn của `int` và hướng dẫn sinh viên chuyển đổi sang dùng `long` hoặc `decimal`.

---

## VIII. KẾ HOẠCH BÀN GIAO VÀ TRIỂN KHAI TIẾP THEO

1. **Tạo tài liệu kế hoạch:** Lưu tệp này tại `I:\Course_UDA\Kỹ thuật lập trình\ebooks\new ebooks\WebProgramingTechnique2026\devPlan\DevPlan_Buoi_04_CSharp_IT26M.md`.
2. **Biên soạn bộ Slide XeLaTeX Beamer hoàn chỉnh:**
   - Biên dịch thành file PDF `Slides_CShape/Slide_Buoi_04_NenTangLapTrinh_CSharp.pdf`.
   - Đảm bảo tỷ lệ 16:9, màu sắc tương thích với bộ slide chuẩn UDA, font chữ Arial/Consolas.
3. **Cập nhật Cổng học tập trực tuyến (Course Portal):**
   - Đưa nội dung Buổi 4 và slide vào hệ thống bài giảng trực tuyến môn học để sinh viên IT26M có thể tải về và ôn tập trước khi lên lớp.
