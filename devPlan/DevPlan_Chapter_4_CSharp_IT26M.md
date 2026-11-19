# KẾ HOẠCH BÀI GIẢNG VÀ PHÁT TRIỂN SLIDE BÀI GIẢNG ĐẠI HỌC
## HỌC PHẦN: KỸ THUẬT LẬP TRÌNH / LẬP TRÌNH C# & .NET
### CHƯƠNG 4: INTRODUCTION TO CLASSES, OBJECTS, METHODS AND STRINGS (GIỚI THIỆU VỀ LỚP, ĐỐI TƯỢNG, PHƯƠNG THỨC VÀ CHUỖI)
**Đối tượng:** Lớp IT26M (Khóa 2026 -- Khoa Công nghệ Thông tin, Trường Đại học Đông Á)  
**Thời lượng:** 01 buổi (03 tiết = 150 phút, kết hợp lý thuyết sư phạm và thực hành phòng máy tại chỗ)  
**Tài liệu tham khảo chính:** Textbook *Visual C# How to Program (6th Edition)* (Deitel & Deitel) -- Chapter 4: *Introduction to Classes, Objects, Methods and strings* (Trang 146--181)  
**Định dạng sản phẩm:** Slide LaTeX Beamer $\to$ Biên dịch PDF chuẩn học thuật quốc tế (XeLaTeX, font Arial/Consolas, tỷ lệ 16:9 widescreen)  
**Thư mục lưu trữ:** `Slides_CShape/`, `Slides/slideChapter_04.pdf`, và `VideoCShape/Chapter_04/slideChapter_04.pdf`

---

## I. MỤC TIÊU BÀI HỌC (COURSE LEARNING OUTCOMES - CLOs)

Kết thúc buổi học 3 tiết này, sinh viên lớp IT26M đạt được 5 chuẩn đầu ra cốt lõi:

| Mã CLO | Mô tả chuẩn đầu ra môn học | Thang đo Bloom |
| :--- | :--- | :--- |
| **CLO 4.1** | Trình bày và phân biệt được các khái niệm cốt lõi của lập trình hướng đối tượng (OOP): Lớp (Class), Đối tượng (Object), Lớp điều khiển (Driver Class với phương thức `Main`), Kiểu tham chiếu (Reference Types) vs Kiểu giá trị (Value Types), toán tử `new` và giá trị mặc định của biến (`null`, `0`, `false`). | Level 2 (Understand) |
| **CLO 4.2** | Khai báo và sử dụng phương thức (Methods), phân biệt Tham số (Parameters) vs Đối số (Arguments), Biến cục bộ (Local Variables) vs Biến thể hiện (Instance Variables), áp dụng chỉ định truy cập `private` để thực hiện Đóng gói (Encapsulation) và Ẩn giấu dữ liệu (Data Hiding). | Level 3 (Apply) |
| **CLO 4.3** | Xây dựng Thuộc tính (Properties) với các bộ truy cập `get` và `set`, sử dụng từ khóa ngữ cảnh `value`, vận dụng Thuộc tính tự động (Auto-Implemented Properties `{ get; set; }`), và đọc/vẽ Sơ đồ lớp UML (UML Class Diagrams) chuẩn mực với 3 ngăn. | Level 3 (Apply) |
| **CLO 4.4** | Khởi tạo đối tượng bằng Hàm tạo (Constructors), phân biệt hàm tạo mặc định không tham số và hàm tạo tùy biến có tham số, quy tắc nạp chồng hàm tạo và vòng đời của đối tượng trong bộ nhớ Heap. | Level 3 (Apply) |
| **CLO 4.5** | Áp dụng kiểu dữ liệu số thực chính xác cao `decimal` (hậu tố `m`/`M`), xây dựng cơ chế Kiểm tra tính hợp lệ của dữ liệu (Data Validation) để bảo vệ trạng thái của đối tượng, định dạng hiển thị tiền tệ với chuỗi định dạng (`:C`) và phát triển ứng dụng ngân hàng đa tài khoản hoàn chỉnh. | Level 4 (Analyze / Create) |

---

## II. MA TRẬN PHÂN BỔ THỜI GIAN & TIẾN TRÌNH DẠY HỌC (3 TIẾT = 150 PHÚT)

```text
========================================================================================
TIẾT 1 (50'): LỚP, ĐỐI TƯỢNG, BIẾN THỂ HIỆN & PHƯƠNG THỨC SET/GET (Slides 1 - 16)
- 05': Khởi động buổi học, công bố 5 CLOs, kết nối từ Tư duy thủ tục (Chương 3) sang OOP (Chương 4)
- 15': Case Study AccountTest.cs (Hình 4.1) & Driver Class: Khởi tạo đối tượng với 'new', kiểu tham chiếu vs kiểu giá trị
- 10': Khai báo lớp Account.cs (Hình 4.2): Biến thể hiện private, phương thức SetName và GetName
- 10': Phân biệt Instance Variables vs Local Variables; Sơ đồ lớp UML 3 ngăn (Hình 4.3)
- 10': [THỰC HÀNH 1 & CHECKPOINT 1] Tạo dự án đa lớp trong VS, code cặp lớp Account & AccountTest
----------------------------------------------------------------------------------------
TIẾT 2 (50'): THUỘC TÍNH (PROPERTIES), AUTO-PROPERTIES & HÀM TẠO (CONSTRUCTORS) (Slides 17 - 29)
- 10': Thuộc tính (Properties) trong C#: Thay thế Set/Get bằng get và set accessors, từ khóa 'value' (Hình 4.5, 4.6)
- 10': Sơ đồ UML «property» (Hình 4.7) & Thuộc tính tự động C# (Auto-Implemented Properties { get; set; })
- 15': Khởi tạo đối tượng với Hàm tạo (Constructors - Hình 4.8, 4.9): Cú pháp, quy tắc đặt tên, nạp chồng
- 10': Phân biệt Hàm tạo mặc định vs Hàm tạo tùy biến; Sơ đồ lớp UML với Constructor (Hình 4.10)
- 05': [THỰC HÀNH 2 & CHECKPOINT 2] Nâng cấp lớp Account với Auto-Properties và Constructor 2 tham số
----------------------------------------------------------------------------------------
TIẾT 3 (50'): XỬ LÝ TIỀN TỆ DECIMAL, VALIDATION DỮ LIỆU & LAB TỔNG HỢP ATM (Slides 30 - 45)
- 10': Kiểu dữ liệu decimal (128-bit, hậu tố m) trong ứng dụng tài chính; Bổ sung biến balance và property Balance (Hình 4.11)
- 10': Data Validation: Chống nạp số âm; Phương thức nghiệp vụ ngân hàng Deposit(decimal)
- 10': Test-Drive giao dịch nạp tiền (AccountTest.cs - Hình 4.12); Ký tự định dạng tiền tệ ':C' & bảng format specifiers (Hình 4.13)
- 15': [THỰC HÀNH 3] Hands-on Lab: Lập trình hệ thống ATM Mini (mở rộng phương thức Withdraw và DisplayAccount)
- 05': Tổng kết checklist chuẩn đầu ra 5 CLOs, giới thiệu đồ án bài tập lớn & dặn dò Chương 5
========================================================================================
```

---

## III. BẢN ĐỒ HÌNH ẢNH & TÀI NGUYÊN TRÍCH XUẤT TỪ SÁCH GIÁO KHOA

Tất cả các hình ảnh được trích xuất ở độ phân giải cao 300 DPI và lưu trữ tại `Slides_CShape/images/`:

| Mã file hình ảnh | Trang SGK | Tên hình trong SGK | Nội dung & Vai trò trong bài giảng |
| :--- | :---: | :--- | :--- |
| `fig4_01_accounttest_app.png` | Trang 3 (148) | Fig. 4.1: AccountTest.cs | Khởi tạo và thao tác đối tượng Account bằng phương thức Set/Get |
| `fig4_02_account_class.png` | Trang 6 (151) | Fig. 4.2: Account.cs | Lớp Account với biến thể hiện private name và phương thức SetName/GetName |
| `fig4_03_uml_account.png` | Trang 10 (155) | Fig. 4.3: UML class diagram | Sơ đồ lớp UML 3 ngăn: Tên lớp, Thuộc tính (- name: string), Phương thức (+ SetName, + GetName) |
| `fig4_04_conceptual_object.png`| Trang 13 (158) | Fig. 4.4: Conceptual view | Mô hình trực quan đối tượng Account với lớp vỏ bảo vệ dữ liệu private |
| `fig4_05_accounttest_properties_p1.png` | Trang 13 (158) | Fig. 4.5: AccountTest Part 1 | Khởi tạo đối tượng AccountTest sử dụng cú pháp Thuộc tính (Property) |
| `fig4_05_accounttest_properties_p2.png` | Trang 14 (159) | Fig. 4.5: AccountTest Part 2 | Thiết lập và truy xuất thuộc tính Name của myAccount |
| `fig4_06_account_properties.png` | Trang 15 (160) | Fig. 4.6: Account.cs (Property) | Lớp Account thay thế SetName/GetName bằng thuộc tính Name { get; set; } |
| `fig4_07_uml_properties.png` | Trang 17 (162) | Fig. 4.7: UML with property | Sơ đồ UML biểu diễn thuộc tính với stereotype `«property»` |
| `fig4_08_account_constructor.png` | Trang 18 (163) | Fig. 4.8: Account.cs (Constructor) | Lớp Account bổ sung hàm tạo khởi tạo tên tài khoản |
| `fig4_09_accounttest_constructor_p1.png`| Trang 19 (164) | Fig. 4.9: AccountTest Constructor P1 | Khởi tạo hai đối tượng account1 ("Jane Green") và account2 ("John Blue") |
| `fig4_09_accounttest_constructor_p2.png`| Trang 20 (165) | Fig. 4.9: AccountTest Constructor P2 | In tên hai đối tượng và màn hình thực thi kết quả |
| `fig4_10_uml_constructor.png` | Trang 21 (166) | Fig. 4.10: UML constructor | Sơ đồ UML biểu diễn hàm tạo Account(accountName: string) |
| `fig4_11_account_balance_p1.png` | Trang 21 (166) | Fig. 4.11: Account.cs Balance P1 | Lớp Account với biến decimal balance và hàm tạo 2 tham số |
| `fig4_11_account_balance_p2.png` | Trang 22 (167) | Fig. 4.11: Account.cs Balance P2 | Thuộc tính Balance có validation và phương thức Deposit(decimal) |
| `fig4_12_accounttest_balance_p1.png` | Trang 24 (169) | Fig. 4.12: AccountTest Balance P1 | Tạo 2 tài khoản có số dư ban đầu, in số dư định dạng tiền tệ |
| `fig4_12_accounttest_balance_p2.png` | Trang 25 (170) | Fig. 4.12: AccountTest Balance P2 | Nhập tiền nạp, gọi phương thức Deposit và in số dư cập nhật |
| `fig4_13_format_specifiers.png` | Trang 26 (171) | Fig. 4.13: String format specifiers | Bảng tra cứu các ký tự định dạng chuỗi: C, D, E, F, G, N, P |
| `fig4_14_uml_balance.png` | Trang 27 (172) | Fig. 4.14: UML complete Account | Sơ đồ UML toàn diện của lớp Account hoàn chỉnh (Properties & Methods) |

---

## IV. CẤU TRÚC CHI TIẾT 45 SLIDE BÀI GIẢNG BEAMER

```text
SLIDE 01: [BÌA] Kỹ thuật Lập trình C# & .NET - Chương 4: Lớp, Đối tượng, Phương thức và Chuỗi
SLIDE 02: [CLOs] 5 Chuẩn đầu ra bài học (Course Learning Outcomes) theo Thang đo Bloom
SLIDE 03: [AGENDA] Lộ trình bài học 3 tiết tích hợp lý thuyết & thực hành phòng máy
SLIDE 04: [TƯ DUY OOP] Cuộc chuyển dịch tư duy: Lập trình Thủ tục sang Lập trình Hướng đối tượng
SLIDE 05: [TIẾT 1 BÌA] TIẾT 1: LỚP, ĐỐI TƯỢNG, BIẾN THỂ HIỆN & PHƯƠNG THỨC SET / GET
SLIDE 06: [CASE STUDY 1] Lái thử lớp Account: Chương trình AccountTest.cs (Hình 4.1)
SLIDE 07: [DRIVER CLASS] Khái niệm Driver Class, Toán tử new & Khởi tạo Đối tượng trong Bộ nhớ
SLIDE 08: [KIỂU DỮ LIỆU] Kiểu Tham chiếu (Reference Types) vs Kiểu Giá trị (Value Types) & Giá trị null
SLIDE 09: [KHAI BÁO LỚP] Khai báo lớp Account.cs & Biến thể hiện private name (Hình 4.2)
SLIDE 10: [PHƯƠNG THỨC] Phương thức SetName: Khái niệm Tham số (Parameter) & Kiểu void
SLIDE 11: [PHƯƠNG THỨC] Phương thức GetName: Câu lệnh return & Kiểu trả về (Return Type)
SLIDE 12: [PHẠM VI BIẾN] Phân biệt Biến thể hiện (Instance Variables) vs Biến cục bộ (Local Variables)
SLIDE 13: [UML CLASS DIAGRAM] Sơ đồ lớp UML 3 ngăn chuẩn công nghiệp cho lớp Account (Hình 4.3)
SLIDE 14: [VISUAL STUDIO] Tổ chức dự án đa tệp lớp (Multiple Class Files) trong Solution Explorer
SLIDE 15: [NGUYÊN LÝ PHẦN MỀM] Đóng gói (Encapsulation) & Ẩn giấu dữ liệu (Data Hiding - Hình 4.4)
SLIDE 16: [CHECKPOINT 1 & LAB 1] Trắc nghiệm củng cố Tiết 1 & Thực hành tạo cặp lớp Account - AccountTest
SLIDE 17: [TIẾT 2 BÌA] TIẾT 2: THUỘC TÍNH (PROPERTIES), AUTO-PROPERTIES & HÀM TẠO (CONSTRUCTORS)
SLIDE 18: [THUỘC TÍNH C#] Giới thiệu Thuộc tính (Properties): Cú pháp C# thanh lịch (Hình 4.5)
SLIDE 19: [CẤU TRÚC PROPERTY] Phân tích bộ truy cập get và set trong lớp Account (Hình 4.6)
SLIDE 20: [TỪ KHÓA VALUE] Từ khóa ngữ cảnh 'value' và cơ chế nạp giá trị ngầm định trong set
SLIDE 21: [UML PROPERTY] Biểu diễn Thuộc tính trong Sơ đồ lớp UML với «property» (Hình 4.7)
SLIDE 22: [AUTO-PROPERTIES] Thuộc tính Tự động (Auto-Implemented Properties): Cú pháp { get; set; }
SLIDE 23: [SO SÁNH PROPERTY] Thuộc tính Tự động vs Thuộc tính có Biến hậu thuẫn (Backing Field)
SLIDE 24: [VẤN ĐỀ KHỞI TẠO] Tại sao cần Hàm tạo (Constructors)? Hạn chế của việc gán giá trị sau khi tạo
SLIDE 25: [HÀM TẠO C#] Khai báo Hàm tạo trong lớp Account: Quy tắc đặt tên và cú pháp (Hình 4.8)
SLIDE 26: [KHỞI TẠO ĐỐI TƯỢNG] Khởi tạo nhiều đối tượng với đối số trong AccountTest.cs (Hình 4.9)
SLIDE 27: [HÀM TẠO MẶC ĐỊNH] Phân biệt Hàm tạo mặc định không tham số vs Hàm tạo tùy biến
SLIDE 28: [UML CONSTRUCTOR] Sơ đồ lớp UML biểu diễn Hàm tạo Account(accountName: string) (Hình 4.10)
SLIDE 29: [CHECKPOINT 2 & LAB 2] Trắc nghiệm Tiết 2 & Thực hành nâng cấp Account với Auto-Props & Constructor
SLIDE 30: [TIẾT 3 BÌA] TIẾT 3: XỬ LÝ TIỀN TỆ DECIMAL, VALIDATION DỮ LIỆU & LAB TỔNG HỢP ATM
SLIDE 31: [KIỂU DECIMAL] Bài toán Tài chính: Tại sao cấm dùng double/float và bắt buộc dùng decimal?
SLIDE 32: [ĐẶC TÍNH DECIMAL] Cấu trúc 128-bit, 28-29 chữ số chính xác và hậu tố m / M trong C#
SLIDE 33: [ACCOUNT NÂNG CẤP] Bổ sung biến balance và Thuộc tính Balance cho lớp Account (Hình 4.11)
SLIDE 34: [DATA VALIDATION] Cơ chế Kiểm tra tính hợp lệ dữ liệu trong Constructor và Property
SLIDE 35: [NGHIỆP VỤ NGÂN HÀNG] Phương thức Deposit(decimal depositAmount) nạp tiền an toàn
SLIDE 36: [TEST-DRIVE SỐ DƯ] Khảo sát AccountTest.cs: Khởi tạo số dư ban đầu và in tiền tệ (Hình 4.12 P1)
SLIDE 37: [TEST-DRIVE NẠP TIỀN] Khảo sát AccountTest.cs: Nhập tiền nạp bàn phím và cập nhật (Hình 4.12 P2)
SLIDE 38: [FORMAT SPECIFIER] Kỹ thuật định dạng chuỗi tiền tệ với ký tự ':C' (Currency Format)
SLIDE 39: [BẢNG ĐỊNH DẠNG] Bảng các ký tự định dạng chuỗi thông dụng trong .NET (Hình 4.13: C, D, E, F, G, N, P)
SLIDE 40: [UML TOÀN DIỆN] Sơ đồ lớp UML toàn diện của lớp Account hoàn chỉnh (Hình 4.14)
SLIDE 41: [LỖI KINH ĐIỂN] Các bẫy lập trình kinh điển trong OOP C# và biện pháp phòng tránh
SLIDE 42: [REFACTORING] Tái cấu trúc mã nguồn: Viết phương thức dùng chung DisplayAccount (Ex 4.13)
SLIDE 43: [MỞ RỘNG NGHIỆP VỤ] Thiết kế phương thức Rút tiền Withdraw và kiểm tra thấu chi (Ex 4.11)
SLIDE 44: [HANDS-ON LAB 3] Xây dựng Hệ thống Quản lý Tài khoản Ngân hàng ATM Mini (25 Phút)
SLIDE 45: [TỔNG KẾT & DẶN DÒ] Bảng Checklist 5 CLOs, Khảo sát bài tập lớn & Chuẩn bị Chương 5
```
