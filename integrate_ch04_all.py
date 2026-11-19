# -*- coding: utf-8 -*-
"""
Integrate Chapter 4 across:
1. js/quiz_data.js
2. js/exercises_data.js
3. js/interactive_exercises.js
4. js/chapter_data.js
5. js/app.js
6. index.html
"""

import json
import os
import re

BASE_DIR = r"i:\Course_UDA\Kỹ thuật lập trình\ebooks\new ebooks\WebProgramingTechnique2026"
JS_DIR = os.path.join(BASE_DIR, "js")

# ==============================================================================
# 1. Integrate js/quiz_data.js
# ==============================================================================
with open(os.path.join(JS_DIR, "quiz_ch04_snippet.json"), "r", encoding="utf-8") as f:
    quiz_ch4 = json.load(f)

quiz_js_path = os.path.join(JS_DIR, "quiz_data.js")
with open(quiz_js_path, "r", encoding="utf-8") as f:
    quiz_content = f.read()

if "QUIZ_CHAPTER_04" not in quiz_content:
    # Remove existing module.exports and window assignment block at the end if present
    quiz_content = re.sub(r"if \(typeof window !== 'undefined'\) \{[\s\S]*?\}\s*if \(typeof module !== 'undefined' && module\.exports\) \{[\s\S]*?\}", "", quiz_content).strip()
    
    quiz_ch4_str = "\n\n// " + "="*76 + "\n"
    quiz_ch4_str += "// NGÂN HÀNG CÂU HỎI TRẮC NGHIỆM CHƯƠNG 4: CLASSES, OBJECTS, METHODS AND STRINGS\n"
    quiz_ch4_str += "// (40 CÂU CÂN BẰNG ĐỘ DÀI & ĐÁP ÁN: 10 A, 10 B, 10 C, 10 D; 10 R1, 10 R2, 10 R3, 10 R4)\n"
    quiz_ch4_str += "// " + "="*76 + "\n"
    quiz_ch4_str += "const QUIZ_CHAPTER_04 = " + json.dumps(quiz_ch4, ensure_ascii=False, indent=2) + ";\n\n"
    quiz_ch4_str += "if (typeof window !== 'undefined') {\n"
    quiz_ch4_str += "  window.QUIZ_CHAPTER_01 = (typeof QUIZ_CHAPTER_01 !== 'undefined') ? QUIZ_CHAPTER_01 : [];\n"
    quiz_ch4_str += "  window.QUIZ_CHAPTER_02 = (typeof QUIZ_CHAPTER_02 !== 'undefined') ? QUIZ_CHAPTER_02 : [];\n"
    quiz_ch4_str += "  window.QUIZ_CHAPTER_03 = (typeof QUIZ_CHAPTER_03 !== 'undefined') ? QUIZ_CHAPTER_03 : [];\n"
    quiz_ch4_str += "  window.QUIZ_CHAPTER_04 = QUIZ_CHAPTER_04;\n"
    quiz_ch4_str += "}\n"
    quiz_ch4_str += "if (typeof module !== 'undefined' && module.exports) {\n"
    quiz_ch4_str += "  module.exports = { QUIZ_CHAPTER_01, QUIZ_CHAPTER_02, QUIZ_CHAPTER_03, QUIZ_CHAPTER_04 };\n"
    quiz_ch4_str += "}\n"
    
    with open(quiz_js_path, "w", encoding="utf-8") as f:
        f.write(quiz_content + quiz_ch4_str)
    print("Appended QUIZ_CHAPTER_04 to js/quiz_data.js")
else:
    print("QUIZ_CHAPTER_04 already in js/quiz_data.js")

# ==============================================================================
# 2. Integrate js/exercises_data.js
# ==============================================================================
with open(os.path.join(JS_DIR, "exercises_ch04_snippet.json"), "r", encoding="utf-8") as f:
    ex_ch4 = json.load(f)

ex_js_path = os.path.join(JS_DIR, "exercises_data.js")
with open(ex_js_path, "r", encoding="utf-8") as f:
    ex_content = f.read()

if "EXERCISES_CHAPTER_04" not in ex_content:
    ex_content = re.sub(r"if \(typeof window !== 'undefined'\) \{[\s\S]*?\}\s*if \(typeof module !== 'undefined' && module\.exports\) \{[\s\S]*?\}", "", ex_content).strip()
    
    ex_ch4_str = "\n\n// " + "="*76 + "\n"
    ex_ch4_str += "// HỆ THỐNG BÀI TẬP CHƯƠNG 4: CLASSES, OBJECTS, METHODS AND STRINGS\n"
    ex_ch4_str += "// " + "="*76 + "\n"
    ex_ch4_str += "const EXERCISES_CHAPTER_04 = " + json.dumps(ex_ch4, ensure_ascii=False, indent=2) + ";\n\n"
    ex_ch4_str += "if (typeof window !== 'undefined') {\n"
    ex_ch4_str += "  window.EXERCISES_CHAPTER_01 = (typeof EXERCISES_CHAPTER_01 !== 'undefined') ? EXERCISES_CHAPTER_01 : [];\n"
    ex_ch4_str += "  window.EXERCISES_CHAPTER_02 = (typeof EXERCISES_CHAPTER_02 !== 'undefined') ? EXERCISES_CHAPTER_02 : [];\n"
    ex_ch4_str += "  window.EXERCISES_CHAPTER_03 = (typeof EXERCISES_CHAPTER_03 !== 'undefined') ? EXERCISES_CHAPTER_03 : [];\n"
    ex_ch4_str += "  window.EXERCISES_CHAPTER_04 = EXERCISES_CHAPTER_04;\n"
    ex_ch4_str += "}\n"
    ex_ch4_str += "if (typeof module !== 'undefined' && module.exports) {\n"
    ex_ch4_str += "  module.exports = { EXERCISES_CHAPTER_01, EXERCISES_CHAPTER_02, EXERCISES_CHAPTER_03, EXERCISES_CHAPTER_04 };\n"
    ex_ch4_str += "}\n"
    
    with open(ex_js_path, "w", encoding="utf-8") as f:
        f.write(ex_content + ex_ch4_str)
    print("Appended EXERCISES_CHAPTER_04 to js/exercises_data.js")
else:
    print("EXERCISES_CHAPTER_04 already in js/exercises_data.js")

# ==============================================================================
# 3. Integrate js/interactive_exercises.js
# ==============================================================================
with open(os.path.join(JS_DIR, "interactive_ch04_snippet.json"), "r", encoding="utf-8") as f:
    interactive_ch4 = json.load(f)

interactive_js_path = os.path.join(JS_DIR, "interactive_exercises.js")
with open(interactive_js_path, "r", encoding="utf-8") as f:
    interactive_content = f.read()

if '"4.1":' not in interactive_content:
    ch4_interactive_blocks = []
    for k, v in interactive_ch4.items():
        ch4_interactive_blocks.append(f'  "{k}": ' + json.dumps(v, ensure_ascii=False, indent=4))
    
    injection = "  // --------------------------------------------------------------------------\n"
    injection += "  // CHƯƠNG 4: CLASSES, OBJECTS, METHODS AND STRINGS\n"
    injection += "  // --------------------------------------------------------------------------\n"
    injection += ",\n".join(ch4_interactive_blocks) + ",\n\n"
    
    pattern = r"(const INTERACTIVE_EXERCISES_DATA\s*=\s*\{)"
    m = re.search(pattern, interactive_content)
    if m:
        pos = m.end()
        new_interactive = interactive_content[:pos] + "\n" + injection + interactive_content[pos:]
        with open(interactive_js_path, "w", encoding="utf-8") as f:
            f.write(new_interactive)
        print("Injected Chapter 4 interactive exercises into js/interactive_exercises.js")
    else:
        print("Warning: Could not find INTERACTIVE_EXERCISES_DATA definition")
else:
    print("Chapter 4 interactive exercises already present in js/interactive_exercises.js")

# ==============================================================================
# 4. Integrate js/chapter_data.js (CHAPTER_METADATA["4"])
# ==============================================================================
ch4_meta = {
    "id": 4,
    "title": "Chương 4: Introduction to Classes, Objects, Methods and strings",
    "heroTitle": "CHƯƠNG 4: CLASSES, OBJECTS, METHODS AND STRINGS",
    "heroDesc": "Lập trình hướng đối tượng (OOP), lớp và đối tượng, cấp phát bộ nhớ Managed Heap và Stack, kiểu tham chiếu vs kiểu giá trị, nguyên lý đóng gói (Encapsulation), biến thể hiện private, thuộc tính C# (Properties) get/set, Auto-Implemented Properties, hàm khởi tạo (Constructors), nạp chồng hàm tạo, kiểu số thực 128-bit decimal, cơ chế Data Validation, định dạng tiền tệ chuyên nghiệp :C và xây dựng Mini ATM System.",
    "pills": [
        "⏱️ Thời lượng: 3 Tiết (150')",
        "🎯 5 Chuẩn đầu ra (CLO 4.1 - 4.5)",
        "📝 40 Câu trắc nghiệm chuẩn hóa",
        "💻 15 Bài tập giáo khoa & Dự án Mini ATM"
    ],
    "totalSlides": 45,
    "videoDir": "./VideoCShape/Chapter_04",
    "slidePdf": "./VideoCShape/Chapter_04/slideChapter_04.pdf",
    "slideName": "slideChapter_04.pdf",
    "overviewHtml": """
      <div class="overview-grid">
        
        <!-- Cột 1: Thông tin học phần & Mục tiêu Chương 4 -->
        <div class="academic-card">
          <div class="card-header-styled">
            <span style="font-size: 1.5rem;">🎓</span>
            <h3>Thông tin Học phần & Chương 4</h3>
          </div>
          <ul class="clo-list">
            <li><strong>Tên học phần:</strong> Kỹ thuật Lập trình (C# / .NET Programming Technique)</li>
            <li><strong>Chương 4:</strong> Introduction to Classes, Objects, Methods and strings</li>
            <li><strong>Đối tượng đào tạo:</strong> Lớp IT26M & Khóa 2026 — Khoa Công nghệ Thông tin</li>
            <li><strong>Thời lượng buổi học:</strong> 1 buổi (3 tiết = 150 phút, tích hợp lý thuyết & thực hành phòng máy)</li>
            <li><strong>Giáo trình chính:</strong> <em>Visual C# How to Program (6th Edition)</em> (Harvey Deitel & Paul Deitel), Chapter 4 (trang 146–181)</li>
            <li><strong>Môi trường phát triển:</strong> Visual Studio 2022 Community, .NET 8 / C# 12, OOP Architecture</li>
          </ul>
        </div>

        <!-- Cột 2: 5 Chuẩn đầu ra (CLOs) Chương 4 -->
        <div class="academic-card">
          <div class="card-header-styled">
            <span style="font-size: 1.5rem;">🎯</span>
            <h3>Chuẩn đầu ra bài học (CLOs)</h3>
          </div>
          <ul class="clo-list">
            <li class="clo-item">
              <span class="clo-badge">CLO 4.1</span>
              <div><strong>Lớp, Đối tượng & Vùng nhớ:</strong> Phân biệt rõ bản chất Lớp (Class) vs Đối tượng (Object), toán tử <code>new</code>, Managed Heap vs Stack và Kiểu Tham chiếu vs Kiểu Giá trị (null).</div>
            </li>
            <li class="clo-item">
              <span class="clo-badge">CLO 4.2</span>
              <div><strong>Đóng gói & Phương thức:</strong> Khai báo lớp, biến thể hiện <code>private</code>, phương thức <code>SetName</code>/<code>GetName</code>, và sơ đồ lớp UML 3 ngăn chuẩn quốc tế.</div>
            </li>
            <li class="clo-item">
              <span class="clo-badge">CLO 4.3</span>
              <div><strong>Thuộc tính C# (Properties):</strong> Sử dụng bộ truy cập <code>get</code>/<code>set</code>, từ khóa ngữ cảnh <code>value</code>, UML <code>«property»</code> và cú pháp Auto-Implemented Properties (<code>{ get; set; }</code>).</div>
            </li>
            <li class="clo-item">
              <span class="clo-badge">CLO 4.4</span>
              <div><strong>Hàm khởi tạo (Constructors):</strong> Định nghĩa constructor khởi tạo trạng thái hợp lệ cho đối tượng, nạp chồng constructor và quy tắc thu hồi default constructor.</div>
            </li>
            <li class="clo-item">
              <span class="clo-badge">CLO 4.5</span>
              <div><strong>Kiểu Decimal, Validation & ATM:</strong> Ứng dụng kiểu 128-bit <code>decimal</code> (hậu tố <code>m</code>), Data Validation, định dạng tiền tệ <code>:C</code>, tái cấu trúc mã nguồn và xây dựng Mini ATM System.</div>
            </li>
          </ul>
        </div>

        <!-- Cột 3: Tiến trình 3 Tiết Tích hợp -->
        <div class="academic-card">
          <div class="card-header-styled">
            <span style="font-size: 1.5rem;">⏱️</span>
            <h3>Tiến trình 3 Tiết Tích hợp (150')</h3>
          </div>
          <div class="timeline-container">
            <div class="timeline-step">
              <div class="step-num">1</div>
              <div class="step-content">
                <strong>TIẾT 1 (50'): Cơ sở Hướng đối tượng & Lớp Account</strong>
                <p>OOP vs Lập trình thủ tục, Driver Class <code>AccountTest.cs</code>, toán tử <code>new</code>, phân tích Managed Heap & Stack, biến thể hiện <code>private name</code>, phương thức <code>SetName</code>/<code>GetName</code>, sơ đồ lớp UML 3 ngăn. Kết thúc bằng <strong>[Lab 1: Dự án AccountApp]</strong> (15').</p>
              </div>
            </div>
            <div class="timeline-step">
              <div class="step-num">2</div>
              <div class="step-content">
                <strong>TIẾT 2 (50'): Thuộc tính Properties & Hàm tạo Constructors</strong>
                <p>Thuộc tính C# (Properties), bộ truy cập <code>get</code>/<code>set</code>, từ khóa ngữ cảnh <code>value</code>, Auto-Implemented Properties, Constructor tùy biến, sự biến mất của default constructor, Constructor Overloading. Kết thúc bằng <strong>[Lab 2: Nâng cấp Auto-Properties & Constructor]</strong> (15').</p>
              </div>
            </div>
            <div class="timeline-step">
              <div class="step-num">3</div>
              <div class="step-content">
                <strong>TIẾT 3 (50'): Kiểu Decimal, Data Validation & Dự án Ngân hàng ATM</strong>
                <p>Sai số nhị phân <code>double</code>/<code>float</code>, kiểu 128-bit <code>decimal</code> (hậu tố <code>m</code>), cơ chế Data Validation, phương thức <code>Deposit</code>, định dạng tiền tệ <code>:C</code>, 4 cạm bẫy OOP, tái cấu trúc <code>DisplayAccount</code>, phương thức <code>Withdraw</code>. Kết thúc bằng <strong>[Lab 3: Xây dựng Mini ATM System]</strong> (25').</p>
              </div>
            </div>
          </div>
        </div>

      </div>

      <!-- Khung lộ trình 19 chương môn học -->
      <div class="academic-card" style="margin-top: 1.5rem;">
        <div class="card-header-styled">
          <span style="font-size: 1.5rem;">🗺️</span>
          <h3>Cây chương trình toàn khóa học (Curriculum Roadmap 19 Chương)</h3>
        </div>
        <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 1rem;">
          Chương 4 là bước ngoặt bản lề chuyển dịch toàn bộ tư duy của sinh viên IT26M từ lập trình cấu trúc sang lập trình hướng đối tượng (OOP) hiện đại.
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 0.75rem; font-size: 0.85rem;">
          <div style="padding: 0.75rem; background: var(--bg-subtle); border-radius: 6px; color: var(--text-muted);">Chương 1: Introduction to Computers, Internet & C#</div>
          <div style="padding: 0.75rem; background: var(--bg-subtle); border-radius: 6px; color: var(--text-muted);">Chương 2: Visual Studio & Visual Programming</div>
          <div style="padding: 0.75rem; background: var(--bg-subtle); border-radius: 6px; color: var(--text-muted);">Chương 3: Introduction to C# App Programming</div>
          <div style="padding: 0.75rem; background: var(--primary-light); border-radius: 6px; font-weight: 700; color: var(--primary-navy);">
            ⭐ Chương 4: Classes, Objects, Methods and strings (Đang học)
          </div>
          <div style="padding: 0.75rem; background: var(--bg-subtle); border-radius: 6px; color: var(--text-muted);">Chương 5: Control Statements: Part 1</div>
          <div style="padding: 0.75rem; background: var(--bg-subtle); border-radius: 6px; color: var(--text-muted);">Chương 6: Control Statements: Part 2</div>
          <div style="padding: 0.75rem; background: var(--bg-subtle); border-radius: 6px; color: var(--text-muted);">Chương 7: Methods: A Deeper Look</div>
          <div style="padding: 0.75rem; background: var(--bg-subtle); border-radius: 6px; color: var(--text-muted);">Chương 8: Arrays; Exception Handling</div>
          <div style="padding: 0.75rem; background: var(--bg-subtle); border-radius: 6px; color: var(--text-muted);">Chương 9: LINQ and the List Collection</div>
          <div style="padding: 0.75rem; background: var(--bg-subtle); border-radius: 6px; color: var(--text-muted);">Chương 10 - 20: OOP Inheritance, Polymorphism & Windows Forms</div>
        </div>
      </div>
    """,
    "docsHtml": """
      <h3 class="resource-section-title">📖 Sách giáo trình & Slide bài giảng số hóa Chương 4</h3>
      <div class="doc-grid">
        
        <!-- Doc 1: Textbook Chapter 4 -->
        <div class="doc-card">
          <div>
            <div class="doc-type-icon">📕</div>
            <h4>Textbook C# Chương 4 (Bản gốc Deitel & Deitel)</h4>
            <p>Giáo trình <em>Visual C# How to Program (6th Edition)</em> - Chapter 4: Introduction to Classes, Objects, Methods and strings. 36 trang đầy đủ lý thuyết, bài tập Self-Review và 15 bài tập lập trình hướng đối tượng.</p>
          </div>
          <div class="doc-meta">
            <span>PDF • 36 Trang (Trang 146–181)</span>
            <a href="./textbook_CShape/Chapter_04.pdf" target="_blank" class="btn-download">📥 Xem & Tải về</a>
          </div>
        </div>

        <!-- Doc 2: Slide Video Player 45 Slides -->
        <div class="doc-card" style="border: 2px solid var(--primary-cyan); position: relative;">
          <div style="position: absolute; top: -10px; right: 12px; background: var(--primary-cyan); color: #fff; font-size: 0.7rem; font-weight: 700; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">
            ⭐ Slide Trình Chiếu Chính Thức
          </div>
          <div>
            <div class="doc-type-icon">🎬</div>
            <h4>Slide Bài giảng Chính thức (slideChapter_04.pdf)</h4>
            <p>Bộ 45 slide chuẩn mực chính thức của Chương 4, tích hợp đầy đủ sơ đồ bộ nhớ Heap/Stack, sơ đồ lớp UML 3 ngăn, hình minh họa đóng gói và trọn vẹn mã nguồn lớp Account ngân hàng.</p>
          </div>
          <div class="doc-meta">
            <span>PDF • 45 Trang (774 KB)</span>
            <div style="display: flex; gap: 0.5rem;">
              <a href="./VideoCShape/Chapter_04/slideChapter_04.pdf" target="_blank" class="btn-download">📥 Xem & Tải PDF</a>
              <a href="#tab-video" onclick="switchTab('video')" class="btn-download" style="background: var(--bg-subtle); color: var(--text-main); border: 1px solid var(--border-color);">▶️ Trình Chiếu</a>
            </div>
          </div>
        </div>

        <!-- Doc 3: XeLaTeX Beamer Academic Slides -->
        <div class="doc-card">
          <div>
            <div class="doc-type-icon">📊</div>
            <h4>Slide XeLaTeX Beamer Chuẩn Đại học (45 Trang)</h4>
            <p>Bộ slide XeLaTeX Madrid widescreen 16:9, bảng màu học thuật UniNavy / CSharpPurple, font chuẩn Arial & Consolas, chia cấu trúc 3 tiết học tích hợp và 3 bài Hands-on Labs phòng máy.</p>
          </div>
          <div class="doc-meta">
            <span>PDF • 45 Trang (774 KB)</span>
            <a href="./Slides_CShape/Chapter_4_Introduction_to_Classes_Objects_Methods_and_strings_IT26M.pdf" target="_blank" class="btn-download">📥 Tải Slide XeLaTeX</a>
          </div>
        </div>

        <!-- Doc 4: Bộ 4 Phần Slide Chia nhỏ (<= 15 slides) -->
        <div class="doc-card" style="grid-column: 1 / -1;">
          <div>
            <div class="doc-type-icon">📑</div>
            <h4>Bộ Slide Phân chia Theo Cấu trúc PX_... (Mỗi phần không quá 15 slide)</h4>
            <p>Được chia nhỏ chuẩn hóa phục vụ in ấn, trình chiếu từng tiết học và tải lên các nền tảng học tập trực tuyến LMS:</p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; margin-top: 1rem;">
              <div style="padding: 0.8rem; background: var(--bg-subtle); border-radius: 6px; border: 1px solid var(--border-color);">
                <strong>P1: Lớp, Đối tượng & Tham chiếu</strong>
                <p style="font-size: 0.85rem; color: var(--text-muted); margin: 0.3rem 0;">15 Slide (Trang 1–15)</p>
                <a href="./Slides_CShape/P1_Chapter04_Lop_DoiTuong_va_KieuThamChieu.pdf" target="_blank" class="btn-download" style="padding: 4px 8px; font-size: 0.8rem;">📥 Tải P1 (15 slide)</a>
              </div>
              <div style="padding: 0.8rem; background: var(--bg-subtle); border-radius: 6px; border: 1px solid var(--border-color);">
                <strong>P2: Thuộc tính & Auto-Properties</strong>
                <p style="font-size: 0.85rem; color: var(--text-muted); margin: 0.3rem 0;">12 Slide (Trang 16–27)</p>
                <a href="./Slides_CShape/P2_Chapter04_ThuocTinh_Properties_va_AutoProps.pdf" target="_blank" class="btn-download" style="padding: 4px 8px; font-size: 0.8rem;">📥 Tải P2 (12 slide)</a>
              </div>
              <div style="padding: 0.8rem; background: var(--bg-subtle); border-radius: 6px; border: 1px solid var(--border-color);">
                <strong>P3: Hàm tạo (Constructor) & UML</strong>
                <p style="font-size: 0.85rem; color: var(--text-muted); margin: 0.3rem 0;">9 Slide (Trang 28–36)</p>
                <a href="./Slides_CShape/P3_Chapter04_HamKhoiTao_Constructor_va_UML.pdf" target="_blank" class="btn-download" style="padding: 4px 8px; font-size: 0.8rem;">📥 Tải P3 (9 slide)</a>
              </div>
              <div style="padding: 0.8rem; background: var(--bg-subtle); border-radius: 6px; border: 1px solid var(--border-color);">
                <strong>P4: Kiểu Decimal, Validation & ATM</strong>
                <p style="font-size: 0.85rem; color: var(--text-muted); margin: 0.3rem 0;">9 Slide (Trang 37–45)</p>
                <a href="./Slides_CShape/P4_Chapter04_KieuDecimal_DinhDangTienTe_va_ATM.pdf" target="_blank" class="btn-download" style="padding: 4px 8px; font-size: 0.8rem;">📥 Tải P4 (9 slide)</a>
              </div>
            </div>
          </div>
        </div>

        <!-- Doc 5: Kịch bản thuyết minh Script.txt -->
        <div class="doc-card">
          <div>
            <div class="doc-type-icon">📜</div>
            <h4>Kịch bản Thuyết minh Song song (script.txt)</h4>
            <p>Toàn bộ 45 lượt đối thoại song song giữa Giảng viên và Sinh viên IT26M, giải thích cặn kẽ từng dòng lệnh C#, mô hình ô nhớ Heap/Stack, cơ chế đóng gói và các cạm bẫy lập trình.</p>
          </div>
          <div class="doc-meta">
            <span>TXT • 45 Slide (62.2 KB)</span>
            <a href="./VideoCShape/Chapter_04/script.txt" target="_blank" class="btn-download">📥 Xem Kịch bản TXT</a>
          </div>
        </div>

      </div>
    """,
    "codesHtml": """
      <h3 class="resource-section-title">💾 Kho Mã nguồn Mẫu C# Chương 4: Lập trình Hướng đối tượng</h3>
      <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1.5rem;">
        Mã nguồn hoàn chỉnh từ phiên bản cơ bản đến phiên bản nghiệp vụ ngân hàng hoàn chỉnh theo giáo trình Deitel, hỗ trợ sao chép 1-click.
      </p>

      <div style="display: flex; flex-direction: column; gap: 1.5rem;">

        <!-- Code 1: Account.cs cơ bản -->
        <div class="exercise-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <h4 style="color: var(--primary-navy);">1. Account.cs (Hình 4.2) — Lớp Account Cơ bản với Biến private & Get/Set Methods</h4>
            <span class="clo-badge">Tiết 1</span>
          </div>
          <div class="code-container">
            <button class="btn-copy-code" onclick="copyCode(this, `// Fig. 4.2: Account.cs\\n// A simple Account class that contains a private instance variable name and methods to set and get its value.\\nclass Account {\\n   private string name;\\n   public void SetName(string accountName) { name = accountName; }\\n   public string GetName() { return name; }\\n}`)">📋 Copy Code</button>
            <pre class="code-block"><code>// Fig. 4.2: Account.cs
// Lớp Account cơ bản chứa biến thể hiện private name và các phương thức Set/Get
class Account
{
   private string name; // Biến thể hiện (instance variable) ẩn giấu dữ liệu

   // Phương thức thiết lập tên tài khoản
   public void SetName(string accountName)
   {
      name = accountName; // Lưu tên vào biến thể hiện
   }

   // Phương thức lấy tên tài khoản
   public string GetName()
   {
      return name; // Trả về giá trị của biến name cho nơi gọi
   }
}</code></pre>
          </div>
        </div>

        <!-- Code 2: AccountTest.cs cơ bản -->
        <div class="exercise-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <h4 style="color: var(--primary-navy);">2. AccountTest.cs (Hình 4.1) — Chương trình Lái thử (Driver Class) Khởi tạo Đối tượng</h4>
            <span class="clo-badge">Tiết 1</span>
          </div>
          <div class="code-container">
            <button class="btn-copy-code" onclick="copyCode(this, `// Fig. 4.1: AccountTest.cs\\nusing System;\\nclass AccountTest {\\n   static void Main() {\\n      Account myAccount = new Account();\\n      Console.WriteLine($&quot;Initial name is: {myAccount.GetName()}&quot;);\\n      Console.Write(&quot;Enter the name: &quot;);\\n      string theName = Console.ReadLine();\\n      myAccount.SetName(theName);\\n      Console.WriteLine($&quot;myAccount's name is: {myAccount.GetName()}&quot;);\\n   }\\n}`)">📋 Copy Code</button>
            <pre class="code-block"><code>// Fig. 4.1: AccountTest.cs
// Tạo và thao tác với một đối tượng Account
using System;

class AccountTest
{
   static void Main()
   {
      // Sử dụng toán tử new để cấp phát đối tượng Account trên Managed Heap
      Account myAccount = new Account();

      // Hiển thị giá trị ban đầu của biến name (trả về null)
      Console.WriteLine($"Initial name is: {myAccount.GetName()}");

      // Nhắc và đọc tên do người dùng nhập từ bàn phím
      Console.Write("Enter the name: ");
      string theName = Console.ReadLine();
      myAccount.SetName(theName); // Truyền đối số vào phương thức SetName

      // Hiển thị tên đã được lưu trong đối tượng myAccount
      Console.WriteLine($"myAccount's name is: {myAccount.GetName()}");
   }
}</code></pre>
          </div>
        </div>

        <!-- Code 3: Account.cs với Property & Constructor -->
        <div class="exercise-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <h4 style="color: var(--primary-navy);">3. Account.cs (Hình 4.8) — Lớp Account với Thuộc tính Property & Hàm tạo Constructor</h4>
            <span class="clo-badge">Tiết 2</span>
          </div>
          <div class="code-container">
            <button class="btn-copy-code" onclick="copyCode(this, `// Fig. 4.8: Account.cs\\nclass Account {\\n   public string Name { get; set; }\\n   public Account(string accountName) {\\n      Name = accountName;\\n   }\\n}`)">📋 Copy Code</button>
            <pre class="code-block"><code>// Fig. 4.8: Account.cs
// Áp dụng Thuộc tính Tự động (Auto-Implemented Property) và Constructor
class Account
{
   // Thuộc tính tự động: C# tự sinh biến backing field ẩn và logic get/set
   public string Name { get; set; }

   // Hàm khởi tạo (Constructor) có tham số để khởi tạo trạng thái đối tượng
   public Account(string accountName)
   {
      Name = accountName; // Gọi bộ set của thuộc tính Name
   }
}</code></pre>
          </div>
        </div>

        <!-- Code 4: Account.cs Toàn diện với Decimal, Validation & Deposit -->
        <div class="exercise-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <h4 style="color: var(--primary-navy);">4. Account.cs (Hình 4.11) — Lớp Account Ngân hàng Hoàn chỉnh với Decimal & Validation</h4>
            <span class="clo-badge">Tiết 3</span>
          </div>
          <div class="code-container">
            <button class="btn-copy-code" onclick="copyCode(this, `// Fig. 4.11: Account.cs\\nusing System;\\nclass Account {\\n   public string Name { get; set; }\\n   private decimal balance;\\n   public Account(string accountName, decimal initialBalance) {\\n      Name = accountName;\\n      Balance = initialBalance;\\n   }\\n   public decimal Balance {\\n      get { return balance; }\\n      private set { if (value &gt; 0.0m) balance = value; }\\n   }\\n   public void Deposit(decimal depositAmount) {\\n      if (depositAmount &gt; 0.0m) balance = balance + depositAmount;\\n   }\\n}`)">📋 Copy Code</button>
            <pre class="code-block"><code>// Fig. 4.11: Account.cs
// Lớp Account ngân hàng hoàn chỉnh: Kiểu 128-bit decimal, Data Validation và Deposit
using System;

class Account
{
   public string Name { get; set; } // Thuộc tính tự động lưu tên
   private decimal balance; // Biến thể hiện lưu số dư tiền tệ chính xác cao

   // Constructor nhận 2 tham số: tên và số dư khởi tạo
   public Account(string accountName, decimal initialBalance)
   {
      Name = accountName;
      Balance = initialBalance; // Gọi bộ set để kiểm tra tính hợp lệ
   }

   // Thuộc tính Balance: Cho phép đọc công khai nhưng chỉ nội bộ lớp mới được sửa
   public decimal Balance
   {
      get
      {
         return balance;
      }
      private set // Bảo mật: Chỉ nội bộ Account mới được gán giá trị
      {
         // Kiểm tra tính hợp lệ (Data Validation): số dư ban đầu phải dương
         if (value > 0.0m)
         {
            balance = value;
         }
      }
   }

   // Phương thức nghiệp vụ nạp tiền: Chỉ nạp khi số tiền dương
   public void Deposit(decimal depositAmount)
   {
      if (depositAmount > 0.0m)
      {
         balance = balance + depositAmount; // Cộng dồn số dư an toàn
      }
   }
}</code></pre>
          </div>
        </div>

        <!-- Code 5: Mini ATM Refactoring DisplayAccount & Withdraw -->
        <div class="exercise-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <h4 style="color: var(--primary-navy);">5. Mini ATM Refactoring & Withdraw — Tái cấu trúc DRY và Rút tiền chống Thấu chi</h4>
            <span class="clo-badge">Lab 3</span>
          </div>
          <div class="code-container">
            <button class="btn-copy-code" onclick="copyCode(this, `// Refactored DisplayAccount & Withdraw method\\npublic static void DisplayAccount(Account accountToDisplay) {\\n   Console.WriteLine($&quot;{accountToDisplay.Name}'s balance: {accountToDisplay.Balance:C}&quot;);\\n}\\n\\n// Withdraw method with overdraft protection\\npublic void Withdraw(decimal withdrawalAmount) {\\n   if (withdrawalAmount &gt; 0.0m) {\\n      if (withdrawalAmount &lt;= Balance) {\\n         balance = balance - withdrawalAmount;\\n      } else {\\n         Console.WriteLine(&quot;Withdrawal amount exceeded account balance.&quot;);\\n      }\\n   }\\n}`)">📋 Copy Code</button>
            <pre class="code-block"><code>// Phương thức dùng chung hiển thị tài khoản theo nguyên lý DRY (Exercise 4.13)
public static void DisplayAccount(Account accountToDisplay)
{
   // Sử dụng ký tự định dạng :C để tự động xuất đơn vị tiền tệ chuẩn quốc tế
   Console.WriteLine($"{accountToDisplay.Name}'s balance: {accountToDisplay.Balance:C}");
}

// Phương thức rút tiền có cơ chế chống thấu chi (Exercise 4.9 & Lab 3)
public void Withdraw(decimal withdrawalAmount)
{
   if (withdrawalAmount > 0.0m)
   {
      // Kiểm tra số tiền rút không được vượt quá số dư hiện có
      if (withdrawalAmount <= Balance)
      {
         balance = balance - withdrawalAmount; // Trừ tiền thành công
      }
      else
      {
         // Thông báo cảnh báo chuẩn nghiệp vụ ngân hàng
         Console.WriteLine("Withdrawal amount exceeded account balance.");
      }
   }
}</code></pre>
          </div>
        </div>

      </div>
    """
}

chapter_data_js_path = os.path.join(JS_DIR, "chapter_data.js")
with open(chapter_data_js_path, "r", encoding="utf-8") as f:
    chapter_data_content = f.read()

if '"4":' not in chapter_data_content:
    # We find where CHAPTER_METADATA ends or right after "3": { ... }
    # Let's format ch4_meta as JSON string
    ch4_json_str = json.dumps(ch4_meta, ensure_ascii=False, indent=2)
    # Indent it by 2 spaces
    indented_ch4 = ",\n  \"4\": " + ch4_json_str + "\n};\n"
    
    # Replace the last `};\n` before window.CHAPTER_METADATA
    pattern = r"\};\s*(?=if \(typeof window !== 'undefined'\))"
    new_chapter_data = re.sub(pattern, indented_ch4, chapter_data_content)
    with open(chapter_data_js_path, "w", encoding="utf-8") as f:
        f.write(new_chapter_data)
    print("Injected CHAPTER_METADATA['4'] into js/chapter_data.js")
else:
    print("CHAPTER_METADATA['4'] already in js/chapter_data.js")

# ==============================================================================
# 5. Update js/app.js
# ==============================================================================
app_js_path = os.path.join(JS_DIR, "app.js")
with open(app_js_path, "r", encoding="utf-8") as f:
    app_content = f.read()

# Update getCurrentQuiz
old_quiz = """function getCurrentQuiz() {
  if (AppState.currentChapter === 3) {
    return (typeof QUIZ_CHAPTER_03 !== 'undefined') ? QUIZ_CHAPTER_03 : [];
  }
  if (AppState.currentChapter === 2) {
    return (typeof QUIZ_CHAPTER_02 !== 'undefined') ? QUIZ_CHAPTER_02 : [];
  }
  return (typeof QUIZ_CHAPTER_01 !== 'undefined') ? QUIZ_CHAPTER_01 : [];
}"""

new_quiz = """function getCurrentQuiz() {
  if (AppState.currentChapter === 4) {
    return (typeof QUIZ_CHAPTER_04 !== 'undefined') ? QUIZ_CHAPTER_04 : [];
  }
  if (AppState.currentChapter === 3) {
    return (typeof QUIZ_CHAPTER_03 !== 'undefined') ? QUIZ_CHAPTER_03 : [];
  }
  if (AppState.currentChapter === 2) {
    return (typeof QUIZ_CHAPTER_02 !== 'undefined') ? QUIZ_CHAPTER_02 : [];
  }
  return (typeof QUIZ_CHAPTER_01 !== 'undefined') ? QUIZ_CHAPTER_01 : [];
}"""

# Update getCurrentExercises
old_ex = """function getCurrentExercises() {
  if (AppState.currentChapter === 3) {
    return (typeof EXERCISES_CHAPTER_03 !== 'undefined') ? EXERCISES_CHAPTER_03 : [];
  }
  if (AppState.currentChapter === 2) {
    return (typeof EXERCISES_CHAPTER_02 !== 'undefined') ? EXERCISES_CHAPTER_02 : [];
  }
  return (typeof EXERCISES_CHAPTER_01 !== 'undefined') ? EXERCISES_CHAPTER_01 : [];
}"""

new_ex = """function getCurrentExercises() {
  if (AppState.currentChapter === 4) {
    return (typeof EXERCISES_CHAPTER_04 !== 'undefined') ? EXERCISES_CHAPTER_04 : [];
  }
  if (AppState.currentChapter === 3) {
    return (typeof EXERCISES_CHAPTER_03 !== 'undefined') ? EXERCISES_CHAPTER_03 : [];
  }
  if (AppState.currentChapter === 2) {
    return (typeof EXERCISES_CHAPTER_02 !== 'undefined') ? EXERCISES_CHAPTER_02 : [];
  }
  return (typeof EXERCISES_CHAPTER_01 !== 'undefined') ? EXERCISES_CHAPTER_01 : [];
}"""

# Update getCurrentTranscripts
old_tr = """function getCurrentTranscripts() {
  if (AppState.currentChapter === 3) {
    return (typeof SLIDE_TRANSCRIPTS_CHAPTER_03 !== 'undefined') ? SLIDE_TRANSCRIPTS_CHAPTER_03 : {};
  }
  if (AppState.currentChapter === 2) {
    return (typeof SLIDE_TRANSCRIPTS_CHAPTER_02 !== 'undefined') ? SLIDE_TRANSCRIPTS_CHAPTER_02 : {};
  }
  if (typeof SLIDE_TRANSCRIPTS_CHAPTER_01 !== 'undefined') {
    return SLIDE_TRANSCRIPTS_CHAPTER_01;
  }
  if (typeof SLIDE_TRANSCRIPTS !== 'undefined') {
    return SLIDE_TRANSCRIPTS;
  }
  return {};
}"""

new_tr = """function getCurrentTranscripts() {
  if (AppState.currentChapter === 4) {
    return (typeof SLIDE_TRANSCRIPTS_CHAPTER_04 !== 'undefined') ? SLIDE_TRANSCRIPTS_CHAPTER_04 : {};
  }
  if (AppState.currentChapter === 3) {
    return (typeof SLIDE_TRANSCRIPTS_CHAPTER_03 !== 'undefined') ? SLIDE_TRANSCRIPTS_CHAPTER_03 : {};
  }
  if (AppState.currentChapter === 2) {
    return (typeof SLIDE_TRANSCRIPTS_CHAPTER_02 !== 'undefined') ? SLIDE_TRANSCRIPTS_CHAPTER_02 : {};
  }
  if (typeof SLIDE_TRANSCRIPTS_CHAPTER_01 !== 'undefined') {
    return SLIDE_TRANSCRIPTS_CHAPTER_01;
  }
  if (typeof SLIDE_TRANSCRIPTS !== 'undefined') {
    return SLIDE_TRANSCRIPTS;
  }
  return {};
}"""

# Update switchChapter
old_switch = "if (chapterNum !== 1 && chapterNum !== 2 && chapterNum !== 3) return;"
new_switch = "if (chapterNum !== 1 && chapterNum !== 2 && chapterNum !== 3 && chapterNum !== 4) return;"

# Update initChapterSelector
old_init_sel = "if (initialVal === 2 || initialVal === 3) {"
new_init_sel = "if (initialVal >= 2 && initialVal <= 4) {"

if old_quiz in app_content:
    app_content = app_content.replace(old_quiz, new_quiz)
if old_ex in app_content:
    app_content = app_content.replace(old_ex, new_ex)
if old_tr in app_content:
    app_content = app_content.replace(old_tr, new_tr)
if old_switch in app_content:
    app_content = app_content.replace(old_switch, new_switch)
if old_init_sel in app_content:
    app_content = app_content.replace(old_init_sel, new_init_sel)

with open(app_js_path, "w", encoding="utf-8") as f:
    f.write(app_content)
print("Updated js/app.js successfully!")

# ==============================================================================
# 6. Update index.html
# ==============================================================================
index_html_path = os.path.join(BASE_DIR, "index.html")
with open(index_html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Enable Chapter 4 option
html_content = html_content.replace(
    '<option value="4" disabled>Chương 4: Introduction to Classes, Objects, Methods and strings</option>',
    '<option value="4">Chương 4: Introduction to Classes, Objects, Methods and strings</option>'
)

# Add transcripts_ch04.js script tag
if "transcripts_ch04.js" not in html_content:
    html_content = html_content.replace(
        '<script src="./js/transcripts_ch03.js"></script>',
        '<script src="./js/transcripts_ch03.js"></script>\n  <script src="./js/transcripts_ch04.js"></script>'
    )
    print("Added transcripts_ch04.js to index.html")

with open(index_html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Updated index.html successfully!")
print("ALL CHAPTER 4 INTEGRATION COMPLETED SUCCESSFULLY!")
