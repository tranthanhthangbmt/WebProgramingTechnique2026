# -*- coding: utf-8 -*-
"""
Generate js/chapter_data.js containing CHAPTER_METADATA for Chapter 1 and Chapter 2.
"""

import json

# Extract Chapter 1 current HTML from index.html for perfect fidelity
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

overview_ch1 = html.split('<div id="tab-overview" class="tab-pane active">')[1].split('<!-- ----------------------------------------------------------------------\n         TAB 2: TÀI LIỆU')[0].strip()
docs_ch1 = html.split('<div id="tab-docs" class="tab-pane">')[1].split('<!-- ----------------------------------------------------------------------\n         TAB 3: VIDEO')[0].strip()

# Build C# Code Repository for Chapter 1 (replacing legacy Java)
codes_ch1 = """
      <h3 class="resource-section-title">💾 Kho Mã nguồn Mẫu C# Chương 1 (Sẵn sàng Biên dịch & Chạy)</h3>
      <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1.5rem;">
        Các mã nguồn C# chuẩn mực theo giáo trình Deitel, có chú thích giải thích chi tiết và hỗ trợ sao chép 1-click.
      </p>

      <div style="display: flex; flex-direction: column; gap: 1.5rem;">

        <!-- Code 1: Welcome1.cs -->
        <div class="exercise-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <h4 style="color: var(--primary-navy);">1. Welcome1.cs — Chương trình Visual C# kinh điển đầu tiên</h4>
            <span class="clo-badge">Lab 1</span>
          </div>
          <div class="code-container">
            <button class="btn-copy-code" onclick="copyCode(this, `// Welcome1.cs - Chuong trinh C# dau tien\\nusing System;\\n\\nclass Welcome1 {\\n    static void Main() {\\n        Console.WriteLine(&quot;Welcome to Visual C#!&quot;);\\n    }\\n}`)">📋 Copy Code</button>
            <pre class="code-block"><code>// Welcome1.cs - Chương trình C# đầu tiên xuất văn bản ra màn hình console
using System;

class Welcome1
{
    // Điểm khởi nhập (Entry Point) của ứng dụng C#
    static void Main()
    {
        Console.WriteLine("Welcome to Visual C#!");
    } // kết thúc phương thức Main
} // kết thúc lớp Welcome1</code></pre>
          </div>
        </div>

        <!-- Code 2: Welcome4.cs -->
        <div class="exercise-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <h4 style="color: var(--primary-navy);">2. Welcome4.cs — Định dạng chuỗi nội suy (String Interpolation)</h4>
            <span class="clo-badge">Lab 2</span>
          </div>
          <div class="code-container">
            <button class="btn-copy-code" onclick="copyCode(this, `// Welcome4.cs - Dinh dang chuoi noi suy voi $\\nusing System;\\n\\nclass Welcome4 {\\n    static void Main() {\\n        string person = &quot;IT26M&quot;;\\n        Console.WriteLine($&quot;Chao mung cac lap trinh vien lop {person} den voi Visual C#!&quot;);\\n    }\\n}`)">📋 Copy Code</button>
            <pre class="code-block"><code>// Welcome4.cs - Định dạng chuỗi hiện đại với tính năng String Interpolation ($)
using System;

class Welcome4
{
    static void Main()
    {
        string course = "Kỹ thuật Lập trình";
        string classId = "IT26M";
        // Sử dụng toán tử $ để nhúng trực tiếp biến vào chuỗi
        Console.WriteLine($"Chào mừng sinh viên lớp {classId} đến với học phần {course}!");
    }
}</code></pre>
          </div>
        </div>

        <!-- Code 3: Addition.cs -->
        <div class="exercise-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <h4 style="color: var(--primary-navy);">3. Addition.cs — Nhập xuất dữ liệu và phép cộng số nguyên</h4>
            <span class="clo-badge">Lab 2</span>
          </div>
          <div class="code-container">
            <button class="btn-copy-code" onclick="copyCode(this, `// Addition.cs - Nhap 2 so nguyen tu ban phim va tinh tong\\nusing System;\\n\\nclass Addition {\\n    static void Main() {\\n        Console.Write(&quot;Nhap so nguyen thu nhat: &quot;);\\n        int number1 = int.Parse(Console.ReadLine());\\n\\n        Console.Write(&quot;Nhap so nguyen thu hai: &quot;);\\n        int number2 = int.Parse(Console.ReadLine());\\n\\n        int sum = number1 + number2;\\n        Console.WriteLine($&quot;Tong cua hai so la: {sum}&quot;);\\n    }\\n}`)">📋 Copy Code</button>
            <pre class="code-block"><code>// Addition.cs - Nhập 2 số nguyên từ bàn phím bằng Console.ReadLine và tính tổng
using System;

class Addition
{
    static void Main()
    {
        Console.Write("Nhập số nguyên thứ nhất: ");
        int number1 = int.Parse(Console.ReadLine()); // Đọc chuỗi và chuyển đổi sang kiểu số nguyên int

        Console.Write("Nhập số nguyên thứ hai: ");
        int number2 = int.Parse(Console.ReadLine());

        int sum = number1 + number2; // Thực hiện phép cộng trong bộ nhớ

        Console.WriteLine($"Tổng của {number1} và {number2} là: {sum}");
    }
}</code></pre>
          </div>
        </div>

      </div>
"""

# Build Chapter 2 Overview HTML
overview_ch2 = """
      <div class="overview-grid">
        
        <!-- Cột 1: Thông tin học phần & Mục tiêu Chương 2 -->
        <div class="academic-card">
          <div class="card-header-styled">
            <span style="font-size: 1.5rem;">🎓</span>
            <h3>Thông tin Học phần & Chương 2</h3>
          </div>
          <ul class="clo-list">
            <li><strong>Tên học phần:</strong> Kỹ thuật Lập trình (C# / .NET Programming Technique)</li>
            <li><strong>Chương 2:</strong> Introduction to Visual Studio and Visual Programming</li>
            <li><strong>Đối tượng đào tạo:</strong> Lớp IT26M & Khóa 2026 — Khoa Công nghệ Thông tin</li>
            <li><strong>Thời lượng buổi học:</strong> 1 buổi (3 tiết = 150 phút, tích hợp lý thuyết & thực hành tại chỗ)</li>
            <li><strong>Giáo trình tham khảo:</strong> <em>Visual C# How to Program (6th Edition)</em> (Harvey Deitel & Paul Deitel), Chapter 2 (trang 73–104)</li>
            <li><strong>Môi trường phát triển:</strong> Visual Studio 2022 Community, .NET 8 / Windows Forms</li>
          </ul>
        </div>

        <!-- Cột 2: 5 Chuẩn đầu ra (CLOs) Chương 2 -->
        <div class="academic-card">
          <div class="card-header-styled">
            <span style="font-size: 1.5rem;">🎯</span>
            <h3>Chuẩn đầu ra bài học (CLOs)</h3>
          </div>
          <ul class="clo-list">
            <li class="clo-item">
              <span class="clo-badge">CLO 2.1</span>
              <div><strong>Bản chất IDE & Triết lý RAD:</strong> Giải thích vai trò của Môi trường phát triển tích hợp (IDE) và phương pháp Phát triển ứng dụng nhanh (RAD / Visual Programming) trong công nghiệp phần mềm.</div>
            </li>
            <li class="clo-item">
              <span class="clo-badge">CLO 2.2</span>
              <div><strong>Quản trị Dự án Windows Forms:</strong> Khởi tạo, cấu hình và quản trị dự án; phân tích mối quan hệ giữa các tệp <code>.sln</code>, <code>.csproj</code>, <code>Form.cs</code>, <code>Form.Designer.cs</code> và <code>Program.cs</code>.</div>
            </li>
            <li class="clo-item">
              <span class="clo-badge">CLO 2.3</span>
              <div><strong>Điều khiển Menu & Không gian IDE:</strong> Sử dụng thành thạo Menu Bar, Standard Toolbar, phím tắt và kỹ thuật điều hướng cửa sổ (Auto-Hide, Pinning, Ghép nối Docking, F1 Help).</div>
            </li>
            <li class="clo-item">
              <span class="clo-badge">CLO 2.4</span>
              <div><strong>Cửa sổ Nòng cốt & Thuộc tính:</strong> Khai thác Solution Explorer, Toolbox (nhóm Common Controls), và Properties Window (cấu hình Design-Time, xem A-Z vs Categorized).</div>
            </li>
            <li class="clo-item">
              <span class="clo-badge">CLO 2.5</span>
              <div><strong>Xây dựng Hoàn chỉnh ASimpleApp:</strong> Vận dụng kỹ thuật kéo-thả để xây dựng ứng dụng đồ họa đầu tay (Form, Label, PictureBox với tài nguyên ảnh), tùy biến màu, font, căn lề và thực thi ở Run Mode.</div>
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
                <strong>TIẾT 1 (50'): Tổng quan IDE & Menus</strong>
                <p>Khái niệm IDE, Triết lý RAD, Màn hình Start Page, Hộp thoại New Project, Khung nhìn Design View, Thanh Menu Bar (Build, Debug, Format), Standard Toolbar, Tooltips, F1 Help. Kết thúc bằng <strong>[Hands-on Lab 1: Khởi tạo Solution]</strong> (15').</p>
              </div>
            </div>
            <div class="timeline-step">
              <div class="step-num">2</div>
              <div class="step-content">
                <strong>TIẾT 2 (50'): Cửa sổ Nòng cốt & Điều hướng</strong>
                <p>Kỹ thuật Auto-Hide & Pinning, Docking & Tab Groups, Solution Explorer (.sln, .csproj, Form1.cs, Form1.Designer.cs), Thư viện References, Toolbox, Properties Window. Kết thúc bằng <strong>[Hands-on Lab 2: Tùy biến Form]</strong> (15').</p>
              </div>
            </div>
            <div class="timeline-step">
              <div class="step-num">3</div>
              <div class="step-content">
                <strong>TIẾT 3 (50'): Case Study 'ASimpleApp' & Đồ án</strong>
                <p>10 bước xây dựng ASimpleApp (Form Text/BackColor, Label Font/TextAlign, PictureBox Snap Lines/Image Resource/SizeMode, Run Mode). Kết thúc bằng <strong>[Hands-on Lab 3: Hoàn thiện ASimpleApp]</strong> (20'), Checklist CLOs & 5 Đồ án GUI về nhà.</p>
              </div>
            </div>
          </div>
        </div>

      </div>
"""

# Build Chapter 2 Docs HTML
docs_ch2 = """
      <h3 class="resource-section-title">📖 Sách giáo trình & Slide bài giảng số hóa Chương 2</h3>
      <div class="doc-grid">
        
        <!-- Doc 1: Textbook Chapter 2 -->
        <div class="doc-card">
          <div>
            <div class="doc-type-icon">📕</div>
            <h4>Textbook C# Chương 2 (Bản gốc Deitel & Deitel)</h4>
            <p>Giáo trình <em>Visual C# How to Program (6th Edition)</em> - Chapter 2: Introduction to Visual Studio and Visual Programming. 32 trang đầy đủ lý thuyết, hình vẽ minh họa, bài tập Self-Review và 5 Đồ án GUI Exercises 2.7 - 2.11.</p>
          </div>
          <div class="doc-meta">
            <span>PDF • 32 Trang (Trang 73–104)</span>
            <a href="./textbook_CShape/Chapter_02.pdf" target="_blank" class="btn-download">📥 Xem & Tải về</a>
          </div>
        </div>

        <!-- Doc 2: Slide Video Player 45 Slides -->
        <div class="doc-card" style="border: 2px solid var(--primary-cyan); position: relative;">
          <div style="position: absolute; top: -10px; right: 12px; background: var(--primary-cyan); color: #fff; font-size: 0.7rem; font-weight: 700; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">
            ⭐ Slide Trình Chiếu Chính Thức
          </div>
          <div>
            <div class="doc-type-icon">🎬</div>
            <h4>Slide Bài giảng Chính thức (slideChapter_02.pdf)</h4>
            <p>Bộ 45 slide chuẩn mực chính thức của Chương 2, tích hợp đầy đủ sơ đồ giao diện IDE, giải phẫu cấu trúc tệp tin, kỹ thuật điều hướng cửa sổ và 10 bước xây dựng ứng dụng đồ họa ASimpleApp.</p>
          </div>
          <div class="doc-meta">
            <span>PDF • 45 Trang (33.5 MB)</span>
            <div style="display: flex; gap: 0.5rem;">
              <a href="./VideoCShape/Chapter_02/slideChapter_02.pdf" target="_blank" class="btn-download">📥 Xem & Tải PDF</a>
              <a href="#tab-video" onclick="switchTab('video')" class="btn-download" style="background: var(--bg-subtle); color: var(--text-main); border: 1px solid var(--border-color);">▶️ Trình Chiếu</a>
            </div>
          </div>
        </div>

        <!-- Doc 3: XeLaTeX Beamer Academic Slides -->
        <div class="doc-card">
          <div>
            <div class="doc-type-icon">📊</div>
            <h4>Slide XeLaTeX Beamer Chuẩn Đại học (47 Trang)</h4>
            <p>Bộ slide XeLaTeX Madrid widescreen 16:9, màu học thuật UniNavy / CSharpPurple, font chuẩn Arial & Consolas, chia cấu trúc 3 tiết học tích hợp và 3 bài Hands-on Labs phòng máy.</p>
          </div>
          <div class="doc-meta">
            <span>PDF • 47 Trang (581 KB)</span>
            <a href="./Slides_CShape/Chapter_2_Visual_Studio_and_Visual_Programming_IT26M.pdf" target="_blank" class="btn-download">📥 Tải Slide XeLaTeX</a>
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
                <strong>P1: Tổng quan IDE & Menus</strong>
                <p style="font-size: 0.85rem; color: var(--text-muted); margin: 0.3rem 0;">12 Slide (Trang 1–12)</p>
                <a href="./Slides_CShape/P1_Chapter02_Tong_Quan_IDE_va_Menus.pdf" target="_blank" class="btn-download" style="padding: 4px 8px; font-size: 0.8rem;">📥 Tải P1 (12 slide)</a>
              </div>
              <div style="padding: 0.8rem; background: var(--bg-subtle); border-radius: 6px; border: 1px solid var(--border-color);">
                <strong>P2: Điều hướng & Solution Explorer</strong>
                <p style="font-size: 0.85rem; color: var(--text-muted); margin: 0.3rem 0;">12 Slide (Trang 13–24)</p>
                <a href="./Slides_CShape/P2_Chapter02_Dieu_Huong_va_Solution_Explorer.pdf" target="_blank" class="btn-download" style="padding: 4px 8px; font-size: 0.8rem;">📥 Tải P2 (12 slide)</a>
              </div>
              <div style="padding: 0.8rem; background: var(--bg-subtle); border-radius: 6px; border: 1px solid var(--border-color);">
                <strong>P3: Toolbox, Properties & Form</strong>
                <p style="font-size: 0.85rem; color: var(--text-muted); margin: 0.3rem 0;">12 Slide (Trang 25–36)</p>
                <a href="./Slides_CShape/P3_Chapter02_Toolbox_Properties_va_Form.pdf" target="_blank" class="btn-download" style="padding: 4px 8px; font-size: 0.8rem;">📥 Tải P3 (12 slide)</a>
              </div>
              <div style="padding: 0.8rem; background: var(--bg-subtle); border-radius: 6px; border: 1px solid var(--border-color);">
                <strong>P4: ASimpleApp & 5 Đồ án GUI</strong>
                <p style="font-size: 0.85rem; color: var(--text-muted); margin: 0.3rem 0;">11 Slide (Trang 37–47)</p>
                <a href="./Slides_CShape/P4_Chapter02_ASimpleApp_va_Do_An_GUI.pdf" target="_blank" class="btn-download" style="padding: 4px 8px; font-size: 0.8rem;">📥 Tải P4 (11 slide)</a>
              </div>
            </div>
          </div>
        </div>

        <!-- Doc 5: Kịch bản thuyết minh Script.txt -->
        <div class="doc-card">
          <div>
            <div class="doc-type-icon">📜</div>
            <h4>Kịch bản Thuyết minh Song song (script.txt)</h4>
            <p>Toàn bộ 45 lượt đối thoại song song giữa Giảng viên và Sinh viên IT26M, giải thích cặn kẽ từng thao tác IDE, thuộc tính đối tượng và mẹo lập trình thực chiến.</p>
          </div>
          <div class="doc-meta">
            <span>TXT • 45 Slide (62.1 KB)</span>
            <a href="./VideoCShape/Chapter_02/script.txt" target="_blank" class="btn-download">📥 Xem Kịch bản TXT</a>
          </div>
        </div>

      </div>
"""

# Build Chapter 2 Codes HTML
codes_ch2 = """
      <h3 class="resource-section-title">💾 Kho Mã nguồn Mẫu C# Chương 2: Windows Forms GUI</h3>
      <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1.5rem;">
        Mã nguồn hoàn chỉnh của Case Study ASimpleApp và các đồ án thiết kế giao diện GUI theo giáo trình Deitel, hỗ trợ sao chép 1-click.
      </p>

      <div style="display: flex; flex-direction: column; gap: 1.5rem;">

        <!-- Code 1: ASimpleApp Form1.cs -->
        <div class="exercise-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <h4 style="color: var(--primary-navy);">1. Case Study 'ASimpleApp' — Form1.cs (Mã nguồn Logic Nghiệp vụ)</h4>
            <span class="clo-badge">Lab 3</span>
          </div>
          <div class="code-container">
            <button class="btn-copy-code" onclick="copyCode(this, `// Form1.cs - Case Study ASimpleApp\\nusing System;\\nusing System.Windows.Forms;\\n\\nnamespace ASimpleApp {\\n    public partial class Form1 : Form {\\n        public Form1() {\\n            InitializeComponent();\\n        }\\n    }\\n}`)">📋 Copy Code</button>
            <pre class="code-block"><code>// Form1.cs - Lãnh địa của lập trình viên: viết logic nghiệp vụ và xử lý sự kiện
using System;
using System.Drawing;
using System.Windows.Forms;

namespace ASimpleApp
{
    // Áp dụng kỹ thuật partial class để ghép với Form1.Designer.cs
    public partial class Form1 : Form
    {
        public Form1()
        {
            // Nạp toàn bộ các điều khiển đồ họa do IDE sinh ra
            InitializeComponent();
        }
    }
}</code></pre>
          </div>
        </div>

        <!-- Code 2: ASimpleApp Form1.Designer.cs -->
        <div class="exercise-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <h4 style="color: var(--primary-navy);">2. Case Study 'ASimpleApp' — Form1.Designer.cs (Phương thức InitializeComponent)</h4>
            <span class="clo-badge">Lab 3</span>
          </div>
          <div class="code-container">
            <button class="btn-copy-code" onclick="copyCode(this, `// Form1.Designer.cs - Sinh ma tu dong boi Form Designer\\nnamespace ASimpleApp {\\n    partial class Form1 {\\n        private System.ComponentModel.IContainer components = null;\\n        private System.Windows.Forms.Label label1;\\n        private System.Windows.Forms.PictureBox pictureBox1;\\n\\n        private void InitializeComponent() {\\n            this.label1 = new System.Windows.Forms.Label();\\n            this.pictureBox1 = new System.Windows.Forms.PictureBox();\\n            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();\\n            this.SuspendLayout();\\n\\n            // label1\\n            this.label1.Font = new System.Drawing.Font(&quot;Segoe UI&quot;, 24F, System.Drawing.FontStyle.Bold);\\n            this.label1.Location = new System.Drawing.Point(12, 9);\\n            this.label1.Name = &quot;label1&quot;;\\n            this.label1.Size = new System.Drawing.Size(460, 60);\\n            this.label1.Text = &quot;Welcome to Visual C# Programming!&quot;;\\n            this.label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;\\n\\n            // pictureBox1\\n            this.pictureBox1.Location = new System.Drawing.Point(120, 80);\\n            this.pictureBox1.Name = &quot;pictureBox1&quot;;\\n            this.pictureBox1.Size = new System.Drawing.Size(240, 180);\\n            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;\\n\\n            // Form1\\n            this.BackColor = System.Drawing.Color.LightCyan;\\n            this.ClientSize = new System.Drawing.Size(484, 281);\\n            this.Controls.Add(this.pictureBox1);\\n            this.Controls.Add(this.label1);\\n            this.Name = &quot;Form1&quot;;\\n            this.Text = &quot;A Simple App&quot;;\\n            this.ResumeLayout(false);\\n        }\\n    }\\n}`)">📋 Copy Code</button>
            <pre class="code-block"><code>// Form1.Designer.cs - Toàn bộ mã nguồn khởi tạo đối tượng do IDE tự động sinh ra
namespace ASimpleApp
{
    partial class Form1
    {
        private System.ComponentModel.IContainer components = null;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.PictureBox pictureBox1;

        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();

            // Cấu hình thuộc tính cho Label
            this.label1.Font = new System.Drawing.Font("Segoe UI", 24F, System.Drawing.FontStyle.Bold);
            this.label1.Location = new System.Drawing.Point(12, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(460, 60);
            this.label1.Text = "Welcome to Visual C# Programming!";
            this.label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;

            // Cấu hình thuộc tính cho PictureBox
            this.pictureBox1.Location = new System.Drawing.Point(120, 80);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(240, 180);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;

            // Cấu hình thuộc tính cho Form chính
            this.BackColor = System.Drawing.Color.LightCyan;
            this.ClientSize = new System.Drawing.Size(484, 281);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "A Simple App";
            this.ResumeLayout(false);
        }
    }
}</code></pre>
          </div>
        </div>

        <!-- Code 3: Program.cs -->
        <div class="exercise-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <h4 style="color: var(--primary-navy);">3. Program.cs — Điểm Khởi nhập (Entry Point) của Ứng dụng Windows Forms</h4>
            <span class="clo-badge">Lab 1</span>
          </div>
          <div class="code-container">
            <button class="btn-copy-code" onclick="copyCode(this, `// Program.cs\\nusing System;\\nusing System.Windows.Forms;\\n\\nnamespace ASimpleApp {\\n    static class Program {\\n        [STAThread]\\n        static void Main() {\\n            Application.EnableVisualStyles();\\n            Application.SetCompatibleTextRenderingDefault(false);\\n            Application.Run(new Form1());\\n        }\\n    }\\n}`)">📋 Copy Code</button>
            <pre class="code-block"><code>using System;
using System.Windows.Forms;

namespace ASimpleApp
{
    static class Program
    {
        // Điểm bắt đầu thực thi của toàn bộ ứng dụng
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            // Khởi tạo và nạp Form chính lên màn hình
            Application.Run(new Form1());
        }
    }
}</code></pre>
          </div>
        </div>

        <!-- Code 4: CalculatorGUI.cs -->
        <div class="exercise-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <h4 style="color: var(--primary-navy);">4. Exercise 2.9: CalculatorGUI.cs — Bàn phím Máy tính với 3 Panels Fixed3D</h4>
            <span class="clo-badge">Đồ án GUI</span>
          </div>
          <div class="code-container">
            <button class="btn-copy-code" onclick="copyCode(this, `// CalculatorGUI.cs\\n// Thiet ke may tinh bo tui su dung Panel BorderStyle = Fixed3D\\n`)">📋 Copy Code</button>
            <pre class="code-block"><code>// CalculatorGUI.cs - Thiết kế giao diện bàn phím máy tính bỏ túi
using System;
using System.Drawing;
using System.Windows.Forms;

public class CalculatorForm : Form
{
    public CalculatorForm()
    {
        this.Text = "Calculator";
        this.ClientSize = new Size(260, 200);

        TextBox txtDisplay = new TextBox() {
            Text = "0",
            TextAlign = HorizontalAlignment.Right,
            Location = new Point(15, 12),
            Width = 230
        };
        this.Controls.Add(txtDisplay);

        // 3 Khung Panel tạo hiệu ứng viền lõm Fixed3D
        Panel pnlNum = new Panel() { Location = new Point(15, 45), Size = new Size(95, 135), BorderStyle = BorderStyle.Fixed3D };
        Panel pnlOp = new Panel() { Location = new Point(120, 45), Size = new Size(65, 135), BorderStyle = BorderStyle.Fixed3D };
        Panel pnlCmd = new Panel() { Location = new Point(195, 45), Size = new Size(50, 135), BorderStyle = BorderStyle.Fixed3D };
        this.Controls.AddRange(new Control[] { pnlNum, pnlOp, pnlCmd });
    }
}</code></pre>
          </div>
        </div>

      </div>
"""

# Construct CHAPTER_METADATA object
metadata = {
    1: {
        "id": 1,
        "title": "Chương 1: Introduction to Computers, the Internet and Visual C#",
        "heroTitle": "CHƯƠNG 1: INTRODUCTION TO COMPUTERS, THE INTERNET AND VISUAL C#",
        "heroDesc": "Nền tảng hệ thống máy tính, định luật Moore, 6 khối chức năng logic, cấu trúc phân cấp dữ liệu, tiến hóa ngôn ngữ, công nghệ đối tượng (OOP), kiến trúc Microsoft .NET (CLR, MSIL, JIT), Visual Studio IDE và Test-Drive ứng dụng đồ họa tương tác Painter.",
        "pills": [
            "⏱️ Thời lượng: 3 Tiết (150')",
            "🎯 5 Chuẩn đầu ra (CLO)",
            "📝 40 Câu trắc nghiệm chuẩn hóa",
            "💻 29 Bài tập giáo khoa & Making-a-Difference"
        ],
        "totalSlides": 42,
        "videoDir": "./VideoCShape/Chapter_01",
        "slidePdf": "./VideoCShape/Chapter_01/Slide_Chapter_01.pdf",
        "slideName": "Slide_Chapter_01.pdf",
        "overviewHtml": overview_ch1,
        "docsHtml": docs_ch1,
        "codesHtml": codes_ch1
    },
    2: {
        "id": 2,
        "title": "Chương 2: Introduction to Visual Studio and Visual Programming",
        "heroTitle": "CHƯƠNG 2: INTRODUCTION TO VISUAL STUDIO AND VISUAL PROGRAMMING",
        "heroDesc": "Môi trường phát triển tích hợp (IDE), triết lý phát triển ứng dụng nhanh (RAD), cấu trúc dự án Windows Forms, thanh Menu Bar & Toolbar, phím tắt & trợ giúp ngữ cảnh F1, kỹ thuật điều hướng cửa sổ (Auto-Hide, Pinning, Docking), Solution Explorer, Toolbox, Properties Window và Case Study 'ASimpleApp'.",
        "pills": [
            "⏱️ Thời lượng: 3 Tiết (150')",
            "🎯 5 Chuẩn đầu ra (CLO 2.1 - 2.5)",
            "📝 40 Câu trắc nghiệm chuẩn hóa",
            "💻 11 Bài tập giáo khoa & Đồ án GUI"
        ],
        "totalSlides": 45,
        "videoDir": "./VideoCShape/Chapter_02",
        "slidePdf": "./VideoCShape/Chapter_02/slideChapter_02.pdf",
        "slideName": "slideChapter_02.pdf",
        "overviewHtml": overview_ch2,
        "docsHtml": docs_ch2,
        "codesHtml": codes_ch2
    }
}

js_output = "// ============================================================================\n"
js_output += "// HỌC PHẦN: KỸ THUẬT LẬP TRÌNH (4 TÍN CHỈ) - IT26M\n"
js_output += "// METADATA & TEMPLATES CHO CÁC CHƯƠNG HỌC (MULTI-CHAPTER PORTAL CONTROLLER)\n"
js_output += "// ============================================================================\n"
js_output += "const CHAPTER_METADATA = " + json.dumps(metadata, ensure_ascii=False, indent=2) + ";\n"

with open("js/chapter_data.js", "w", encoding="utf-8") as f:
    f.write(js_output)

print("Saved js/chapter_data.js successfully!")

