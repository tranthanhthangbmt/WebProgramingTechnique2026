# KỸ THUẬT LẬP TRÌNH (4 TÍN CHỈ) — CỔNG HỌC TẬP TRỰC TUYẾN IT26M
> **Học phần:** Kỹ thuật Lập trình (Programming Technique) — 4 Tín chỉ (3 LT + 1 TH/Đồ án)  
> **Giáo trình chính:** *Building Java Programs: A Back to Basics Approach* (Stuart Reges & Marty Stepp)  
> **Khóa học:** 2026 — Lớp IT26M  
> **Nền tảng:** Web tĩnh chuẩn hóa, tương thích 100% với **GitHub Pages**  

---

## 🌟 TỔNG QUAN HỆ THỐNG

Cổng học tập trực tuyến môn **Kỹ thuật Lập trình (4 Tín chỉ)** là trung tâm học liệu số đồng bộ, hiện đại theo chuẩn đại học quốc tế (MIT OpenCourseWare / Harvard CS50). Hệ thống cung cấp lộ trình 19 chương môn học, tích hợp toàn diện bài giảng, tài liệu, video thuyết trình, kịch bản sư phạm, ngân hàng trắc nghiệm và bài tập thực hành theo từng chương.

Phiên bản hiện tại tập trung triển khai chuyên sâu cho **Chương 1: Introduction to Java Programming** (Thời lượng 3 tiết học tích hợp lý thuyết và thực hành).

---

## 🎯 CÁC PHÂN HỆ CHỨC NĂNG CHÍNH

### 1. 🗺️ Đề cương & Lộ trình 4 Tín chỉ (Curriculum Roadmap)
* Chi tiết thông tin học phần 4 tín chỉ (75 tiết: 45 LT + 30 TH phòng máy).
* Ma trận 5 Chuẩn đầu ra bài học (CLO 1.1 — 1.5).
* Kế hoạch bài giảng 3 tiết tích hợp (150 phút) kết hợp lý thuyết và 3 bài Hands-on Labs.
* Cây chương trình toàn khóa học 19 chương từ cơ bản đến nâng cao.

### 2. 📖 Kho Tài liệu & Tài nguyên Số (Resources & Docs)
* **Textbook Chương 1 (Tiếng Anh):** Bản PDF gốc từ giáo trình *Building Java Programs 5th Edition* (135 trang đầy đủ lý thuyết và bài tập).
* **Giáo trình Tiếng Việt:** Bản dịch tiếng Việt hoàn chỉnh hỗ trợ tra cứu song ngữ.
* **Slide Bài giảng Chính thức:** [`slideChapter_01.pdf`](./Videos/Chapter_01/slideChapter_01.pdf) gồm 41 slide độ phân giải cao (1376x768), chuẩn bài giảng đại học.
* **Slide Bổ trợ Beamer:** [`Chapter_1_Introduction_to_Java_IT26M.pdf`](./Slides/Chapter_1_Introduction_to_Java_IT26M.pdf) biên dịch từ XeLaTeX phục vụ in ấn tài liệu phát tay.
* **Kịch bản thoại Video:** [`scriptChapter01.txt`](./Videos/Chapter_01/scriptChapter01.txt) với toàn bộ lời thoại đối thoại song song giữa Giảng viên và Sinh viên IT26M cho 41 slide.
* **Bộ mã nguồn giáo khoa:** Kho mã nguồn Java kinh điển (`Hello`, `DrawBoxes`, `DrawFigures1-3`, `FightSong`, `SpaceRocket`).

### 3. 🎬 Trình phát Slide & Audio Thuyết minh Đồng bộ (Slide & Narration Player)
* Hiển thị trực tiếp 41 slide chất lượng cao trích xuất từ [`slideChapter_01.pdf`](./Videos/Chapter_01/slideChapter_01.pdf).
* Tích hợp thanh điều khiển: Chuyển slide trước/sau, danh sách chọn slide nhanh, phím tắt mũi tên trái/phải.
* **Hệ thống Audio thuyết minh:** Tích hợp 41 file âm thanh MP3 tương ứng với từng slide (`slide_1.mp3` đến `slide_41.mp3`), có nút Play/Pause, thanh thời gian và tính năng tự động chuyển trang khi nghe xong.
* **Kịch bản thoại sư phạm (Interactive Transcript):** Khung đối thoại song song Thầy & Trò đồng bộ thời gian thực theo từng slide.
* **Liên kết rạp chiếu độc lập:** Nút bấm mở trực tiếp trình phát toàn màn hình chuyên biệt tại [`Videos/Chapter_01/index.html`](./Videos/Chapter_01/index.html).

### 4. 📝 Ngân hàng Trắc nghiệm Chuẩn hóa (Interactive Quiz Engine)
* **40 câu hỏi trắc nghiệm** bao quát toàn bộ 5 chủ đề cốt lõi của Chương 1.
* **Đặc tính sư phạm nổi bật:** Độ dài các phương án lựa chọn (A, B, C, D) được **phân bổ ngẫu nhiên** (không thiên lệch về phương án dài nhất), loại bỏ hoàn toàn hiện tượng học sinh đoán mò đáp án theo độ dài câu.
* Gắn nhãn phân loại chủ đề và cấp độ tư duy theo thang đo Bloom (Remember, Understand, Apply, Analyze).
* Bảng điều hướng câu hỏi (Question Palette), chấm điểm tự động, tỷ lệ phần trăm và huy hiệu đánh giá năng lực.
* Lời giải thích cặn kẽ (Detailed Explanation) cho từng câu giúp sinh viên tự học và sửa lỗi sai tức thì.

### 5. 💻 Trung tâm Bài tập Cuối chương (Coding Hub)
Trích xuất 19 bài tập kinh điển từ phần cuối Chương 1 giáo trình:
* **8 Bài tập Tự kiểm tra (Self-Check Problems):** Nhị phân, định danh hợp lệ, ký tự thoát, tìm lỗi trong code, lần vết hàm lồng nhau.
* **8 Bài tập Lập trình (Exercises):** `Stewie`, `Spikey`, `WellFormed`, `Mantra`, `TwoRockets`, `FightSong`, `StarFigures`, `Lanterns`.
* **3 Đồ án Mini (Programming Projects):** Chữ in lớn `MISSISSIPPI`, In thư tín `Letters`, Bài ca tích lũy `The Old Lady`.
* Mỗi bài tập đều đi kèm: Đề bài chi tiết, Output mẫu mong đợi, Mã nguồn khởi tạo (Starter Code), Lời giải hoàn chỉnh (Solution) và nút Copy 1-click.

---

## 📁 CẤU TRÚC THƯ MỤC DỰ ÁN

```text
WebProgramingTechnique2026/
├── index.html                    # Trang chủ cổng học tập (SPA đa phân hệ)
├── README.md                     # Tài liệu giới thiệu và hướng dẫn triển khai
├── .nojekyll                     # Tệp cấu hình bắt buộc cho GitHub Pages
├── css/
│   └── style.css                 # Giao diện học thuật, Dark/Light theme, Responsive
├── js/
│   ├── app.js                    # Bộ điều khiển chính: Tabs, Slide player, Audio, Quiz
│   ├── quiz_data.js              # Ngân hàng 40 câu hỏi trắc nghiệm chuẩn hóa
│   └── exercises_data.js         # Dữ liệu 19 bài tập cuối chương và lời giải mẫu
├── devPlan/
│   ├── DevPlan_Course_Website.md # Kế hoạch xây dựng cổng học tập môn học
│   ├── DevPlan_Chapter_1_Java_IT26M.md # Kế hoạch bài giảng 3 tiết học
│   └── DevPlan_Script_Chapter_01.md    # Kế hoạch kịch bản đối thoại 41 slide
├── Videos/
│   └── Chapter_01/
│       ├── slideChapter_01.pdf   # Slide chính thức Chương 1 (41 trang 1376x768)
│       ├── index.html            # Trình phát rạp chiếu độc lập có thuyết minh
│       ├── scriptChapter01.txt   # Kịch bản đối thoại hoàn chỉnh 41 slide
│       ├── slides_png/           # 41 hình ảnh slide chất lượng cao (slide_1 đến slide_41)
│       ├── audio/                # 41 tệp âm thanh thuyết minh (slide_1 đến slide_41.mp3)
│       └── images/               # Kho tài nguyên ảnh gốc
├── Slides/
│   ├── slideChapter_01.pdf       # Bản sao chép slide chính thức
│   ├── Chapter_1_Introduction_to_Java_IT26M.pdf # Slide học thuật Beamer
│   └── Chapter_1_Introduction_to_Java_IT26M.tex # Mã nguồn LaTeX Beamer
├── Textbook/
│   └── Chapter_1_Introduction to Java Programming.pdf # Giáo trình tiếng Anh
├── textbook_vi/
│   └── Building Java Programs_ A Back - Stuart Reges - Vietnamese.pdf # Giáo trình dịch
└── Labs/
    └── src/                      # Mã nguồn bài tập thực hành trên lớp (Labs 1, 2, 3)
```

---

## 🚀 HƯỚNG DẪN ĐƯA LÊN GITHUB PAGES

Trang web được thiết kế 100% bằng Vanilla HTML5, CSS3 và JavaScript hiện đại, sử dụng toàn bộ đường dẫn tương đối (`./`), không cần cấu hình Node.js backend hay build step.

### Bước 1: Khởi tạo Git và thêm tệp
Mở terminal tại thư mục gốc của dự án (`WebProgramingTechnique2026`) và chạy:
```bash
git init
git add .
git commit -m "feat: Cong thong tin hoc tap mon Ky thuat Lap trinh 2026 - Chuong 1"
```

### Bước 2: Tạo Repository trên GitHub và đẩy code lên
1. Đăng nhập vào tài khoản [GitHub](https://github.com) của bạn.
2. Tạo một Repository mới (ví dụ: `KyThuatLapTrinh2026` hoặc `WebProgramingTechnique2026`), chọn chế độ **Public**.
3. Liên kết và đẩy toàn bộ mã nguồn lên:
```bash
git branch -M main
git remote add origin https://github.com/<tai-khoan-github-cua-ban>/<ten-repository>.git
git push -u origin main
```

### Bước 3: Kích hoạt GitHub Pages
1. Trong giao diện GitHub Repository, bấm vào tab **Settings** (ở thanh menu trên cùng).
2. Ở thanh điều hướng bên trái, chọn mục **Pages** (dưới nhóm *Code and automation*).
3. Tại phần **Build and deployment**:
   * **Source:** Chọn `Deploy from a branch`.
   * **Branch:** Chọn nhánh `main` và thư mục `/ (root)`.
4. Bấm **Save**.
5. Đợi khoảng 1 - 2 phút để GitHub tiến hành deploy. Đường link trang web sẽ xuất hiện ở đầu trang:
   ```text
   https://<tai-khoan-github-cua-ban>.github.io/<ten-repository>/
   ```

---

## 👨‍🏫 THÔNG TIN GIẢNG VIÊN & HỖ TRỢ
* **Học phần:** Kỹ thuật Lập trình (4 Tín chỉ)
* **Khoa / Viện:** Khoa Công nghệ Thông tin
* **Lớp phụ trách:** IT26M
* **Năm học:** 2026

