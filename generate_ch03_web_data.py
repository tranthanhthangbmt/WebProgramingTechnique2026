# -*- coding: utf-8 -*-
"""
Generate complete Chapter 3 web data:
1. CHAPTER_METADATA['3'] for js/chapter_data.js
2. QUIZ_CHAPTER_03 for js/quiz_data.js
3. EXERCISES_CHAPTER_03 for js/exercises_data.js
4. INTERACTIVE_EXERCISES_DATA['3.1', '3.2', '3.4', '3.7', '3.9', '3.10', '3.11'] for js/interactive_exercises.js
5. Update js/app.js to support Chapter 3
6. Update index.html to enable Chapter 3 in dropdown and include js/transcripts_ch03.js
"""

import json
import os

BASE_DIR = r"i:\Course_UDA\Kỹ thuật lập trình\ebooks\new ebooks\WebProgramingTechnique2026"
JS_DIR = os.path.join(BASE_DIR, "js")

# ============================================================================
# 1. BUILD CHAPTER 3 METADATA
# ============================================================================
overview_html_ch3 = """
      <div class="overview-grid">
        
        <!-- Cột 1: Thông tin học phần & Mục tiêu Chương 3 -->
        <div class="academic-card">
          <div class="card-header-styled">
            <span style="font-size: 1.5rem;">🎓</span>
            <h3>Thông tin Học phần & Chương 3</h3>
          </div>
          <ul class="clo-list">
            <li><strong>Tên học phần:</strong> Kỹ thuật Lập trình (C# / .NET Programming Technique)</li>
            <li><strong>Chương 3:</strong> Introduction to C# App Programming (Lập trình Ứng dụng C# Cơ bản)</li>
            <li><strong>Đối tượng đào tạo:</strong> Lớp IT26M & Khóa 2026 — Khoa Công nghệ Thông tin</li>
            <li><strong>Thời lượng buổi học:</strong> 1 buổi (3 tiết = 150 phút, tích hợp lý thuyết & thực hành phòng máy)</li>
            <li><strong>Giáo trình chính:</strong> <em>Visual C# How to Program (6th Edition)</em> (Harvey Deitel & Paul Deitel), Chapter 3 (trang 105–145)</li>
            <li><strong>Môi trường phát triển:</strong> Visual Studio 2022 Community, .NET 8 / C# 12, Console & Windows Terminal</li>
          </ul>
        </div>

        <!-- Cột 2: 5 Chuẩn đầu ra (CLOs) Chương 3 -->
        <div class="academic-card">
          <div class="card-header-styled">
            <span style="font-size: 1.5rem;">🎯</span>
            <h3>Chuẩn đầu ra bài học (CLOs)</h3>
          </div>
          <ul class="clo-list">
            <li class="clo-item">
              <span class="clo-badge">CLO 3.1</span>
              <div><strong>Cấu trúc Console & Điểm khởi nhập:</strong> Giải thích cấu trúc chương trình C# cơ bản, vai trò phương thức <code>Main</code> (Entry Point), lớp (Class), chú thích (Comments) và hệ thống từ khóa (Keywords).</div>
            </li>
            <li class="clo-item">
              <span class="clo-badge">CLO 3.2</span>
              <div><strong>Xuất văn bản & Định dạng chuỗi:</strong> Sử dụng thành thạo <code>Console.Write</code>, <code>Console.WriteLine</code>, ký tự thoát Escape Sequences (<code>\\n</code>, <code>\\t</code>, <code>\\\"</code>) và kỹ thuật nội suy chuỗi hiện đại String Interpolation (<code>$</code>).</div>
            </li>
            <li class="clo-item">
              <span class="clo-badge">CLO 3.3</span>
              <div><strong>Khai báo Biến & Nhập liệu:</strong> Khai báo biến, phân tích kiểu số nguyên <code>int</code> 32-bit; sử dụng <code>Console.ReadLine()</code> và phương thức phân tích cú pháp <code>int.Parse()</code> để xử lý dữ liệu nhập từ bàn phím.</div>
            </li>
            <li class="clo-item">
              <span class="clo-badge">CLO 3.4</span>
              <div><strong>Khái niệm Bộ nhớ RAM:</strong> Vẽ sơ đồ và giải thích bản chất biến là các vị trí ô nhớ trong RAM; phân biệt cơ chế Ghi đè phá hủy (Destructive Write) và Đọc không phá hủy (Non-destructive Read).</div>
            </li>
            <li class="clo-item">
              <span class="clo-badge">CLO 3.5</span>
              <div><strong>Toán tử Số học & Rẽ nhánh if:</strong> Vận dụng các toán tử số học (<code>+</code>, <code>-</code>, <code>*</code>, <code>/</code>, <code>%</code>), quy tắc ưu tiên toán tử và cấu trúc rẽ nhánh <code>if</code> cùng 6 toán tử quan hệ (<code>==</code>, <code>!=</code>, <code>&lt;</code>, <code>&gt;</code>, <code>&lt;=</code>, <code>&gt;=</code>).</div>
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
                <strong>TIẾT 1 (50'): Nền tảng Console & Cú pháp C#</strong>
                <p>Khái niệm Console Apps, Lớp Welcome1.cs, Entry Point Main(), Chú thích, Dòng trống, Từ khóa C#, Tạo Console App trong Visual Studio, Trợ lý IntelliSense & Parameter Info. Kết thúc bằng <strong>[Chạy thử Console đầu tiên]</strong> (Ctrl+F5).</p>
              </div>
            </div>
            <div class="timeline-step">
              <div class="step-num">2</div>
              <div class="step-content">
                <strong>TIẾT 2 (50'): Định dạng Chuỗi & Escape Sequences</strong>
                <p>Lỗi cú pháp (Error List), Phân biệt Console.Write vs WriteLine (Welcome2.cs), Xuất nhiều dòng và Ký tự thoát (Welcome3.cs, bảng \\n, \\t, \\\"), String Interpolation $ (Welcome4.cs). Kết thúc bằng <strong>[Hands-on Lab 1: Tùy biến thiệp chào IT26M]</strong> (15').</p>
              </div>
            </div>
            <div class="timeline-step">
              <div class="step-num">3</div>
              <div class="step-content">
                <strong>TIẾT 3 (50'): Biến, RAM, Số học & Rẽ nhánh if</strong>
                <p>Khai báo biến int, Nhập liệu bàn phím int.Parse(Console.ReadLine()) (Addition.cs), Khái niệm ô nhớ RAM (Destructive vs Non-destructive), Toán tử +, -, *, /, %, Chia nguyên, Cấu trúc if và 6 toán tử so sánh (Comparison.cs). Kết thúc bằng <strong>[Hands-on Lab 2: Máy tính Mini]</strong> (20').</p>
              </div>
            </div>
          </div>
        </div>

      </div>
"""

docs_html_ch3 = """
      <h3 class="resource-section-title">📖 Sách giáo trình & Slide bài giảng số hóa Chương 3</h3>
      <div class="doc-grid">
        
        <!-- Doc 1: Textbook Chapter 3 -->
        <div class="doc-card">
          <div>
            <div class="doc-type-icon">📕</div>
            <h4>Textbook C# Chương 3 (Bản gốc Deitel & Deitel)</h4>
            <p>Giáo trình <em>Visual C# How to Program (6th Edition)</em> - Chapter 3: Introduction to C# App Programming. 41 trang đầy đủ lý thuyết, hình minh họa trực quan, Self-Review Exercises và các bài tập lập trình 3.7 - 3.32.</p>
          </div>
          <div class="doc-meta">
            <span>PDF • 41 Trang (Trang 105–145)</span>
            <a href="./textbook_CShape/Chapter_03.pdf" target="_blank" class="btn-download">📥 Xem & Tải về</a>
          </div>
        </div>

        <!-- Doc 2: Slide Video Player 45 Slides -->
        <div class="doc-card" style="border: 2px solid var(--primary-cyan); position: relative;">
          <div style="position: absolute; top: -10px; right: 12px; background: var(--primary-cyan); color: #fff; font-size: 0.7rem; font-weight: 700; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">
            ⭐ Slide Trình Chiếu Chính Thức
          </div>
          <div>
            <div class="doc-type-icon">🎬</div>
            <h4>Slide Bài giảng Chính thức (slideChapter_03.pdf)</h4>
            <p>Bộ 45 slide chuẩn mực chính thức của Chương 3, tích hợp sơ đồ bộ nhớ RAM, phân tích cú pháp chi tiết Welcome1..4, Addition, Comparison, và bảng thứ tự ưu tiên toán tử.</p>
          </div>
          <div class="doc-meta">
            <span>PDF • 45 Trang (1.47 MB)</span>
            <div style="display: flex; gap: 0.5rem;">
              <a href="./VideoCShape/Chapter_03/slideChapter_03.pdf" target="_blank" class="btn-download">📥 Tải Slide PDF</a>
              <a href="#tab-video" onclick="switchTab('video')" class="btn-download" style="background: var(--bg-subtle); color: var(--text-main); border: 1px solid var(--border-color);">▶️ Trình Chiếu</a>
            </div>
          </div>
        </div>

        <!-- Doc 3: XeLaTeX Beamer Academic Slides -->
        <div class="doc-card">
          <div>
            <div class="doc-type-icon">📊</div>
            <h4>Slide XeLaTeX Beamer Chuẩn Đại học (45 Trang)</h4>
            <p>Bộ slide XeLaTeX Madrid widescreen 16:9, màu học thuật UniNavy / CSharpPurple, font chuẩn Arial & Consolas, chia cấu trúc 3 tiết học tích hợp và 2 bài Hands-on Labs phòng máy.</p>
          </div>
          <div class="doc-meta">
            <span>PDF • 45 Trang (1.47 MB)</span>
            <a href="./Slides_CShape/Chapter_3_Introduction_to_CSharp_App_Programming_IT26M.pdf" target="_blank" class="btn-download">📥 Tải Slide XeLaTeX</a>
          </div>
        </div>

        <!-- Doc 4: Bộ 4 Phần Slide Chia nhỏ (<= 15 slides) -->
        <div class="doc-card" style="grid-column: 1 / -1;">
          <div>
            <div class="doc-type-icon">📑</div>
            <h4>Bộ Slide Phân chia Theo Cấu trúc PX_... (Mỗi phần không quá 15 slide)</h4>
            <p>Được chia nhỏ chuẩn hóa phục vụ in ấn, trình chiếu từng tiết học và tải lên các nền tảng học tập trực tuyến:</p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; margin-top: 1rem;">
              <div style="padding: 0.8rem; background: var(--bg-subtle); border-radius: 6px; border: 1px solid var(--border-color);">
                <strong>P1: Tổng quan Console & Cú pháp</strong>
                <p style="font-size: 0.85rem; color: var(--text-muted); margin: 0.3rem 0;">15 Slide (Slide 1–15)</p>
                <a href="./Slides_CShape/P1_Chapter03_Tong_Quan_Console_va_Cu_Phap.pdf" target="_blank" class="btn-download" style="padding: 4px 8px; font-size: 0.8rem;">📥 Tải P1 (15 slide)</a>
              </div>
              <div style="padding: 0.8rem; background: var(--bg-subtle); border-radius: 6px; border: 1px solid var(--border-color);">
                <strong>P2: Định dạng Chuỗi & Escape Sequences</strong>
                <p style="font-size: 0.85rem; color: var(--text-muted); margin: 0.3rem 0;">10 Slide (Slide 16–25)</p>
                <a href="./Slides_CShape/P2_Chapter03_Dinh_Dang_Chuoi_va_Interpolation.pdf" target="_blank" class="btn-download" style="padding: 4px 8px; font-size: 0.8rem;">📥 Tải P2 (10 slide)</a>
              </div>
              <div style="padding: 0.8rem; background: var(--bg-subtle); border-radius: 6px; border: 1px solid var(--border-color);">
                <strong>P3: Biến, RAM & Toán tử Số học</strong>
                <p style="font-size: 0.85rem; color: var(--text-muted); margin: 0.3rem 0;">10 Slide (Slide 26–35)</p>
                <a href="./Slides_CShape/P3_Chapter03_Bien_Bo_Nho_va_Toan_Tu_So_Hoc.pdf" target="_blank" class="btn-download" style="padding: 4px 8px; font-size: 0.8rem;">📥 Tải P3 (10 slide)</a>
              </div>
              <div style="padding: 0.8rem; background: var(--bg-subtle); border-radius: 6px; border: 1px solid var(--border-color);">
                <strong>P4: Cấu trúc Rẽ nhánh if & So sánh</strong>
                <p style="font-size: 0.85rem; color: var(--text-muted); margin: 0.3rem 0;">10 Slide (Slide 36–45)</p>
                <a href="./Slides_CShape/P4_Chapter03_Cau_Truc_Dieu_Kien_va_So_Sanh.pdf" target="_blank" class="btn-download" style="padding: 4px 8px; font-size: 0.8rem;">📥 Tải P4 (10 slide)</a>
              </div>
            </div>
          </div>
        </div>

        <!-- Doc 5: Kịch bản thuyết minh Script.txt -->
        <div class="doc-card">
          <div>
            <div class="doc-type-icon">📜</div>
            <h4>Kịch bản Thuyết minh Song song (script.txt)</h4>
            <p>Toàn bộ 45 lượt đối thoại song song giữa Giảng viên và Sinh viên IT26M, giải thích cặn kẽ từng câu lệnh C#, cơ chế cấp phát ô nhớ và các mẹo lập trình thực chiến.</p>
          </div>
          <div class="doc-meta">
            <span>TXT • 45 Slide (37.8 KB)</span>
            <a href="./VideoCShape/Chapter_03/script.txt" target="_blank" class="btn-download">📥 Xem Kịch bản TXT</a>
          </div>
        </div>

      </div>
"""

codes_html_ch3 = """
      <h3 class="resource-section-title">💾 Kho Mã nguồn Mẫu C# Chương 3: Console Applications</h3>
      <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1.5rem;">
        Mã nguồn chuẩn mực theo giáo trình Deitel, sẵn sàng sao chép 1-click, biên dịch và thực thi ngay với .NET 8 CLI hoặc Visual Studio 2022.
      </p>

      <div style="display: flex; flex-direction: column; gap: 1.5rem;">

        <!-- Code 1: Welcome1.cs -->
        <div class="exercise-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <h4 style="color: var(--primary-navy);">1. Welcome1.cs — Ứng dụng Console đầu tiên in một dòng văn bản</h4>
            <span class="clo-badge">CLO 3.1</span>
          </div>
          <div class="code-container">
            <button class="btn-copy-code" onclick="copyCode(this, `// Fig. 3.1: Welcome1.cs\\n// Text-displaying app.\\nusing System;\\n\\nclass Welcome1\\n{\\n   // Main method begins execution of C# app\\n   static void Main()\\n   {\\n      Console.WriteLine(&quot;Welcome to C# Programming!&quot;);\\n   } // end Main\\n} // end class Welcome1`)">📋 Copy Code</button>
            <pre class="code-block"><code>// Fig. 3.1: Welcome1.cs
// Text-displaying app.
using System;

class Welcome1
{
   // Main method begins execution of C# app
   static void Main()
   {
      Console.WriteLine("Welcome to C# Programming!");
   } // end Main
} // end class Welcome1</code></pre>
          </div>
        </div>

        <!-- Code 2: Welcome2 & Welcome3.cs -->
        <div class="exercise-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <h4 style="color: var(--primary-navy);">2. Welcome3.cs — In nhiều dòng văn bản bằng ký tự thoát (Escape Sequences)</h4>
            <span class="clo-badge">CLO 3.2</span>
          </div>
          <div class="code-container">
            <button class="btn-copy-code" onclick="copyCode(this, `// Fig. 3.11: Welcome3.cs\\n// Displaying multiple lines of text with a single statement.\\nusing System;\\n\\nclass Welcome3\\n{\\n   static void Main()\\n   {\\n      Console.WriteLine(&quot;Welcome to\\nC# Programming!&quot;);\\n   }\\n}`)">📋 Copy Code</button>
            <pre class="code-block"><code>// Fig. 3.11: Welcome3.cs
// Displaying multiple lines of text with a single statement.
using System;

class Welcome3
{
   static void Main()
   {
      // Sử dụng ký tự thoát \\n để xuống dòng trong cùng 1 câu lệnh
      Console.WriteLine("Welcome to\\nC# Programming!");
   }
}</code></pre>
          </div>
        </div>

        <!-- Code 3: Welcome4.cs -->
        <div class="exercise-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <h4 style="color: var(--primary-navy);">3. Welcome4.cs — Định dạng chuỗi nội suy hiện đại (String Interpolation)</h4>
            <span class="clo-badge">CLO 3.2</span>
          </div>
          <div class="code-container">
            <button class="btn-copy-code" onclick="copyCode(this, `// Fig. 3.13: Welcome4.cs\\n// Inserting values with string interpolation.\\nusing System;\\n\\nclass Welcome4\\n{\\n   static void Main()\\n   {\\n      string person = &quot;Paul&quot;;\\n      Console.WriteLine($&quot;Welcome to C# Programming, {person}!&quot;);\\n   }\\n}`)">📋 Copy Code</button>
            <pre class="code-block"><code>// Fig. 3.13: Welcome4.cs
// Inserting values with string interpolation.
using System;

class Welcome4
{
   static void Main()
   {
      string person = "Paul"; // Khai báo biến chuỗi
      
      // Ký tự $ kích hoạt String Interpolation, nhúng trực tiếp biến {person}
      Console.WriteLine($"Welcome to C# Programming, {person}!");
   }
}</code></pre>
          </div>
        </div>

        <!-- Code 4: Addition.cs -->
        <div class="exercise-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <h4 style="color: var(--primary-navy);">4. Addition.cs — Nhập dữ liệu từ bàn phím, ép kiểu int.Parse và tính tổng</h4>
            <span class="clo-badge">CLO 3.3 & 3.4</span>
          </div>
          <div class="code-container">
            <button class="btn-copy-code" onclick="copyCode(this, `// Fig. 3.14: Addition.cs\\n// Displaying the sum of two numbers input from the keyboard.\\nusing System;\\n\\nclass Addition\\n{\\n   static void Main()\\n   {\\n      int number1;\\n      int number2;\\n      int sum;\\n\\n      Console.Write(&quot;Enter first integer: &quot;);\\n      number1 = int.Parse(Console.ReadLine());\\n\\n      Console.Write(&quot;Enter second integer: &quot;);\\n      number2 = int.Parse(Console.ReadLine());\\n\\n      sum = number1 + number2;\\n\\n      Console.WriteLine($&quot;Sum is {sum}&quot;);\\n   }\\n}`)">📋 Copy Code</button>
            <pre class="code-block"><code>// Fig. 3.14: Addition.cs
// Displaying the sum of two numbers input from the keyboard.
using System;

class Addition
{
   static void Main()
   {
      int number1; // Khai báo biến số nguyên thứ nhất
      int number2; // Khai báo biến số nguyên thứ hai
      int sum;     // Khai báo biến lưu tổng

      Console.Write("Enter first integer: "); // Câu nhắc không xuống dòng
      number1 = int.Parse(Console.ReadLine()); // Đọc chuỗi và chuyển sang int

      Console.Write("Enter second integer: ");
      number2 = int.Parse(Console.ReadLine());

      sum = number1 + number2; // Thực hiện phép cộng trong bộ nhớ

      Console.WriteLine($"Sum is {sum}"); // Hiển thị kết quả bằng nội suy chuỗi
   }
}</code></pre>
          </div>
        </div>

        <!-- Code 5: Comparison.cs -->
        <div class="exercise-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <h4 style="color: var(--primary-navy);">5. Comparison.cs — So sánh hai số nguyên sử dụng câu lệnh rẽ nhánh if</h4>
            <span class="clo-badge">CLO 3.5</span>
          </div>
          <div class="code-container">
            <button class="btn-copy-code" onclick="copyCode(this, `// Fig. 3.21: Comparison.cs\\n// Comparing integers using if statements, equality operators\\n// and relational operators.\\nusing System;\\n\\nclass Comparison\\n{\\n   static void Main()\\n   {\\n      Console.Write(&quot;Enter first integer: &quot;);\\n      int number1 = int.Parse(Console.ReadLine());\\n\\n      Console.Write(&quot;Enter second integer: &quot;);\\n      int number2 = int.Parse(Console.ReadLine());\\n\\n      if (number1 == number2)\\n      {\\n         Console.WriteLine($&quot;{number1} == {number2}&quot;);\\n      }\\n\\n      if (number1 != number2)\\n      {\\n         Console.WriteLine($&quot;{number1} != {number2}&quot;);\\n      }\\n\\n      if (number1 &lt; number2)\\n      {\\n         Console.WriteLine($&quot;{number1} &lt; {number2}&quot;);\\n      }\\n\\n      if (number1 &gt; number2)\\n      {\\n         Console.WriteLine($&quot;{number1} &gt; {number2}&quot;);\\n      }\\n\\n      if (number1 &lt;= number2)\\n      {\\n         Console.WriteLine($&quot;{number1} &lt;= {number2}&quot;);\\n      }\\n\\n      if (number1 &gt;= number2)\\n      {\\n         Console.WriteLine($&quot;{number1} &gt;= {number2}&quot;);\\n      }\\n   }\\n}`)">📋 Copy Code</button>
            <pre class="code-block"><code>// Fig. 3.21: Comparison.cs
// Comparing integers using if statements, equality operators
// and relational operators.
using System;

class Comparison
{
   static void Main()
   {
      Console.Write("Enter first integer: ");
      int number1 = int.Parse(Console.ReadLine());

      Console.Write("Enter second integer: ");
      int number2 = int.Parse(Console.ReadLine());

      if (number1 == number2)
      {
         Console.WriteLine($"{number1} == {number2}");
      }

      if (number1 != number2)
      {
         Console.WriteLine($"{number1} != {number2}");
      }

      if (number1 &lt; number2)
      {
         Console.WriteLine($"{number1} &lt; {number2}");
      }

      if (number1 &gt; number2)
      {
         Console.WriteLine($"{number1} &gt; {number2}");
      }

      if (number1 &lt;= number2)
      {
         Console.WriteLine($"{number1} &lt;= {number2}");
      }

      if (number1 &gt;= number2)
      {
         Console.WriteLine($"{number1} &gt;= {number2}");
      }
   }
}</code></pre>
          </div>
        </div>

        <!-- Code 6: Product.cs -->
        <div class="exercise-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <h4 style="color: var(--primary-navy);">6. Exercise 3.6: Product.cs — Ứng dụng tính tích của ba số nguyên</h4>
            <span class="clo-badge">Self-Review 3.6</span>
          </div>
          <div class="code-container">
            <button class="btn-copy-code" onclick="copyCode(this, `// Exercise 3.6: Product.cs\\n// Calculating the product of three integers.\\nusing System;\\n\\nclass Product\\n{\\n   static void Main()\\n   {\\n      Console.Write(&quot;Enter first integer: &quot;);\\n      int x = int.Parse(Console.ReadLine());\\n\\n      Console.Write(&quot;Enter second integer: &quot;);\\n      int y = int.Parse(Console.ReadLine());\\n\\n      Console.Write(&quot;Enter third integer: &quot;);\\n      int z = int.Parse(Console.ReadLine());\\n\\n      int result = x * y * z;\\n      Console.WriteLine($&quot;Product is {result}&quot;);\\n   }\\n}`)">📋 Copy Code</button>
            <pre class="code-block"><code>// Exercise 3.6: Product.cs
// Calculating the product of three integers.
using System;

class Product
{
   static void Main()
   {
      Console.Write("Enter first integer: ");
      int x = int.Parse(Console.ReadLine());

      Console.Write("Enter second integer: ");
      int y = int.Parse(Console.ReadLine());

      Console.Write("Enter third integer: ");
      int z = int.Parse(Console.ReadLine());

      int result = x * y * z; // Tính tích của ba số nguyên
      Console.WriteLine($"Product is {result}");
   }
}</code></pre>
          </div>
        </div>

      </div>
"""

meta_ch3 = {
    "id": 3,
    "title": "Chương 3: Introduction to C# App Programming",
    "heroTitle": "CHƯƠNG 3: INTRODUCTION TO C# APP PROGRAMMING",
    "heroDesc": "Lập trình ứng dụng Console cơ bản, lớp và phương thức Main, câu lệnh Console.Write/WriteLine, ký tự thoát Escape Sequences, định dạng chuỗi nội suy String Interpolation ($), biến và quản lý ô nhớ RAM, các toán tử số học (+, -, *, /, %), cấu trúc rẽ nhánh if và toán tử so sánh quan hệ.",
    "pills": [
        "⏱️ Thời lượng: 3 Tiết (150')",
        "🎯 5 Chuẩn đầu ra (CLO 3.1 - 3.5)",
        "📝 40 Câu trắc nghiệm chuẩn hóa",
        "💻 12 Bài tập giáo khoa & Code thực hành"
    ],
    "totalSlides": 45,
    "videoDir": "./VideoCShape/Chapter_03",
    "slidePdf": "./VideoCShape/Chapter_03/slideChapter_03.pdf",
    "slideName": "slideChapter_03.pdf",
    "overviewHtml": overview_html_ch3,
    "docsHtml": docs_html_ch3,
    "codesHtml": codes_html_ch3
}

# Update js/chapter_data.js
ch_data_path = os.path.join(JS_DIR, "chapter_data.js")
with open(ch_data_path, "r", encoding="utf-8") as f:
    ch_data_content = f.read()

# Parse existing CHAPTER_METADATA by executing in Python or regex
if '"3":' not in ch_data_content:
    # insert before the last "};"
    last_brace_idx = ch_data_content.rfind("};")
    if last_brace_idx != -1:
        prefix = ch_data_content[:last_brace_idx].rstrip()
        if not prefix.endswith(","):
            prefix += ",\n"
        ch3_str = '  "3": ' + json.dumps(meta_ch3, ensure_ascii=False, indent=2) + "\n};\n"
        new_ch_data = prefix + ch3_str
        with open(ch_data_path, "w", encoding="utf-8") as f:
            f.write(new_ch_data)
        print("Appended Chapter 3 to js/chapter_data.js")
    else:
        print("Warning: Could not find closing '};' in chapter_data.js")
else:
    print("Chapter 3 already in js/chapter_data.js, updating...")

print("Step 1 done.")
