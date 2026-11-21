# -*- coding: utf-8 -*-
"""
Script cập nhật Tab Lab 01 cho Chương 3:
1. index.html: Thêm nav button '7. Thực hành Lab 01' và tab pane 'tab-lab'
2. js/chapter_data.js: Thêm thuộc tính labHtml vào metadata Chương 3
3. js/app.js: Xử lý hiển thị tab Lab 01 khi ở Chương 3 và hàm setLabDoc chuyển đổi tài liệu
"""

import re

# ==============================================================================
# 1. CẬP NHẬT index.html
# ==============================================================================
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Thêm nút bấm vào nav-container sau tab codes
target_btn = '''        <button class="nav-tab-btn" data-tab="codes">
          <span class="tab-icon">💾</span>
          <span class="tab-label-full">6. Kho mã nguồn C#</span>
          <span class="tab-label-short">6. Mã nguồn</span>
        </button>'''

replacement_btn = '''        <button class="nav-tab-btn" data-tab="codes">
          <span class="tab-icon">💾</span>
          <span class="tab-label-full">6. Kho mã nguồn C#</span>
          <span class="tab-label-short">6. Mã nguồn</span>
        </button>
        <button class="nav-tab-btn" data-tab="lab" id="navTabBtnLab" style="display: none;">
          <span class="tab-icon">🧪</span>
          <span class="tab-label-full">7. Thực hành Lab 01</span>
          <span class="tab-label-short">7. Lab 01</span>
        </button>'''

if target_btn in html and 'id="navTabBtnLab"' not in html:
    html = html.replace(target_btn, replacement_btn)
    print("Added navTabBtnLab to index.html")
else:
    print("navTabBtnLab already present or target not found in index.html")

# Thêm tab pane tab-lab sau tab-codes
target_pane = '''    </div>

  </main>'''

replacement_pane = '''    </div>

    <!-- ====================================================================
         TAB 7: THỰC HÀNH LAB 01 (DÀNH RIÊNG CHO CHƯƠNG 3)
         ==================================================================== -->
    <div id="tab-lab" class="tab-pane">
      <!-- Nội dung động được tải từ CHAPTER_METADATA["3"].labHtml -->
    </div>

  </main>'''

if target_pane in html and 'id="tab-lab"' not in html:
    html = html.replace(target_pane, replacement_pane)
    print("Added tab-lab to index.html")
else:
    print("tab-lab already present or target not found in index.html")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# ==============================================================================
# 2. XÂY DỰNG NỘI DUNG labHtml CHO CHƯƠNG 3
# ==============================================================================
lab_html_content = r'''
<div class="lab-container" style="display: flex; flex-direction: column; gap: 2rem;">
  
  <!-- Banner Giới thiệu Lab 01 -->
  <div class="academic-card" style="border-left: 5px solid #68217a; background: linear-gradient(to right, rgba(104, 33, 122, 0.05), rgba(15, 44, 89, 0.02));">
    <div class="card-header-styled">
      <span style="font-size: 2rem;">🧪</span>
      <div>
        <h3 style="font-size: 1.4rem; color: var(--primary-navy); margin-bottom: 0.35rem;">
          THỰC HÀNH LAB 01: LẬP TRÌNH THỦ TỤC & TƯ DUY THUẬT TOÁN C# (CHƯƠNG 1 - 3)
        </h3>
        <p style="color: var(--text-muted); font-size: 0.95rem; margin: 0; line-height: 1.5;">
          Học phần: <strong>Kỹ thuật Lập trình / Lập trình C# & .NET</strong> (4 Tín chỉ) — Dành cho Lớp <strong>IT26M</strong> & Khóa 2026.
          Tích hợp toàn diện Bộ Slide bài giảng số hóa và Giáo trình hướng dẫn thực hành chi tiết v2.0.
        </p>
      </div>
    </div>
    
    <div style="display: flex; flex-wrap: wrap; gap: 0.6rem; margin-top: 1.25rem;">
      <span class="clo-badge" style="background: rgba(104, 33, 122, 0.12); color: #68217a; border: 1px solid rgba(104, 33, 122, 0.3); font-weight: 600;">⏱️ Thời lượng: 180 phút phòng lab</span>
      <span class="clo-badge" style="background: rgba(15, 44, 89, 0.12); color: #0f2c59; border: 1px solid rgba(15, 44, 89, 0.3); font-weight: 600;">🎯 4 Giai đoạn chuẩn</span>
      <span class="clo-badge" style="background: rgba(30, 132, 73, 0.12); color: #1e8449; border: 1px solid rgba(30, 132, 73, 0.3); font-weight: 600;">💻 Visual Studio 2022 / .NET 8</span>
      <span class="clo-badge" style="background: rgba(225, 112, 18, 0.12); color: #e17012; border: 1px solid rgba(225, 112, 18, 0.3); font-weight: 600;">📝 Rubric đánh giá 10 điểm</span>
      <span class="clo-badge" style="background: rgba(29, 93, 155, 0.12); color: #1d5d9b; border: 1px solid rgba(29, 93, 155, 0.3); font-weight: 600;">🚀 Cầu nối sang OOP (Chương 4)</span>
    </div>
  </div>

  <!-- 2 Thẻ Tài Liệu PDF Chính Thức -->
  <div>
    <h3 class="resource-section-title">📖 2 Tài Liệu PDF Hướng Dẫn Thực Hành Chính Thức</h3>
    <div class="doc-grid">
      
      <!-- Doc 1: Slide bài giảng thực hành -->
      <div class="doc-card" style="border: 2px solid #68217a; box-shadow: 0 4px 14px rgba(104, 33, 122, 0.1);">
        <div>
          <div class="doc-type-icon" style="background: rgba(104, 33, 122, 0.12); color: #68217a;">📊</div>
          <h4 style="color: #68217a;">1. Slide Hướng Dẫn Thực Hành Lab (Chương 1 - 3 & Lab 01)</h4>
          <p style="line-height: 1.5; margin-bottom: 0.75rem;">
            Bộ slide bài giảng thực hành chính thức gồm <strong>56 trang</strong> định dạng widescreen 16:9 sắc nét.
            Hướng dẫn đầy đủ 4 giai đoạn trên phòng máy: khởi tạo project Console, I/O Stream & ép kiểu số học, rẽ nhánh <code>if...else</code>, 3 bẫy lỗi kinh điển và đề thi thử thách.
          </p>
          <div style="font-size: 0.82rem; color: var(--text-muted); background: var(--bg-subtle); padding: 0.4rem 0.6rem; border-radius: 4px; margin-bottom: 0.75rem;">
            📁 <strong>Tệp:</strong> <code>slide Chuong 03 - Lab 01_v2.pdf</code> • 56 Trang (16:9 HD) • 5.8 MB
          </div>
        </div>
        <div class="doc-meta" style="flex-wrap: wrap; gap: 0.5rem; justify-content: flex-end; border-top: 1px solid var(--border-color); padding-top: 0.75rem;">
          <button onclick="setLabDoc('slide')" class="btn-download" style="background: #68217a; color: white; border: none; cursor: pointer; font-weight: 600;">
            👁️ Xem Trực Tiếp
          </button>
          <a href="./Lab/slide%20Chuong%2003%20-%20Lab%2001_v2.pdf" target="_blank" class="btn-download" style="background: var(--primary-blue);">
            🔍 Mở Tab Mới
          </a>
          <a href="./Lab/slide%20Chuong%2003%20-%20Lab%2001_v2.pdf" download="slide Chuong 03 - Lab 01_v2.pdf" class="btn-download" style="background: var(--bg-subtle); color: var(--text-color); border: 1px solid var(--border-color);">
            📥 Tải PDF
          </a>
        </div>
      </div>

      <!-- Doc 2: Giáo trình hướng dẫn thực hành v2.0 -->
      <div class="doc-card" style="border: 2px solid var(--primary-navy); box-shadow: 0 4px 14px rgba(15, 44, 89, 0.1);">
        <div>
          <div class="doc-type-icon" style="background: rgba(15, 44, 89, 0.12); color: var(--primary-navy);">📘</div>
          <h4 style="color: var(--primary-navy);">2. Tài Liệu Hướng Dẫn Thực Hành & Bài Tập C# (v2.0)</h4>
          <p style="line-height: 1.5; margin-bottom: 0.75rem;">
            Tài liệu giáo trình thực hành chuẩn mực <strong>16 trang A4</strong>. Bao gồm: logic sư phạm, quy trình thao tác chuẩn Visual Studio, hướng dẫn chi tiết 7 bài tập cơ sở, 5 bài tự luyện tại lớp, đề thi độc lập (Tính tiền điện bậc thang & hóa đơn Console) kèm Rubric 10 điểm và 4 đồ án về nhà.
          </p>
          <div style="font-size: 0.82rem; color: var(--text-muted); background: var(--bg-subtle); padding: 0.4rem 0.6rem; border-radius: 4px; margin-bottom: 0.75rem;">
            📁 <strong>Tệp:</strong> <code>Huong-Dan-Thuc-Hanh-Lap-Trinh-CSharp-Chuong-1-den-3-v2.pdf</code> • 16 Trang A4 • 615 KB
          </div>
        </div>
        <div class="doc-meta" style="flex-wrap: wrap; gap: 0.5rem; justify-content: flex-end; border-top: 1px solid var(--border-color); padding-top: 0.75rem;">
          <button onclick="setLabDoc('guide')" class="btn-download" style="background: var(--primary-navy); color: white; border: none; cursor: pointer; font-weight: 600;">
            👁️ Xem Trực Tiếp
          </button>
          <a href="./Lab/Huong-Dan-Thuc-Hanh-Lap-Trinh-CSharp-Chuong-1-den-3-v2.pdf" target="_blank" class="btn-download" style="background: var(--primary-blue);">
            🔍 Mở Tab Mới
          </a>
          <a href="./Lab/Huong-Dan-Thuc-Hanh-Lap-Trinh-CSharp-Chuong-1-den-3-v2.pdf" download="Huong-Dan-Thuc-Hanh-Lap-Trinh-CSharp-Chuong-1-den-3-v2.pdf" class="btn-download" style="background: var(--bg-subtle); color: var(--text-color); border: 1px solid var(--border-color);">
            📥 Tải PDF
          </a>
        </div>
      </div>

    </div>
  </div>

  <!-- Interactive PDF Viewer Container -->
  <div class="academic-card" style="padding: 1.25rem; border: 1px solid var(--border-color); box-shadow: 0 4px 16px rgba(0,0,0,0.06);">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; margin-bottom: 1rem; border-bottom: 1px solid var(--border-color); padding-bottom: 0.75rem;">
      <div style="display: flex; align-items: center; gap: 0.6rem;">
        <span style="font-size: 1.5rem;">🖥️</span>
        <h4 id="labDocTitleDisplay" style="margin: 0; color: var(--primary-navy); font-size: 1.1rem; font-weight: 700;">
          Đang xem: Slide Hướng Dẫn Thực Hành Lab (slide Chuong 03 - Lab 01_v2.pdf)
        </h4>
      </div>
      <div style="display: flex; gap: 0.5rem; align-items: center; flex-wrap: wrap;">
        <button id="btnLabDocSlide" onclick="setLabDoc('slide')" style="padding: 0.45rem 0.9rem; border-radius: 6px; font-size: 0.85rem; font-weight: 600; cursor: pointer; border: 1px solid #68217a; background: #68217a; color: white; transition: all 0.2s;">
          📊 1. Slide Lab 01 (56 trang)
        </button>
        <button id="btnLabDocGuide" onclick="setLabDoc('guide')" style="padding: 0.45rem 0.9rem; border-radius: 6px; font-size: 0.85rem; font-weight: 600; cursor: pointer; border: 1px solid var(--border-color); background: var(--bg-subtle); color: var(--text-color); transition: all 0.2s;">
          📘 2. Giáo Trình Thực Hành (16 trang)
        </button>
        <a id="labDocExternalLink" href="./Lab/slide%20Chuong%2003%20-%20Lab%2001_v2.pdf" target="_blank" class="btn-download" style="padding: 0.45rem 0.9rem; font-size: 0.85rem; background: var(--primary-blue);" title="Mở trong tab riêng biệt">
          ↗️ Mở Tab Riêng
        </a>
      </div>
    </div>

    <!-- Khung iframe hiển thị PDF -->
    <div style="width: 100%; height: 820px; border-radius: 8px; overflow: hidden; background: #525659; box-shadow: inset 0 2px 8px rgba(0,0,0,0.2);">
      <iframe id="labPdfViewerIframe" src="./Lab/slide%20Chuong%2003%20-%20Lab%2001_v2.pdf" width="100%" height="100%" style="border: none;" title="Trình xem tài liệu PDF Lab 01"></iframe>
    </div>
  </div>

  <!-- Bảng Tóm Tắt 4 Giai Đoạn Phòng Lab & Tiêu Chí Chấm Điểm -->
  <div>
    <h3 class="resource-section-title">⏱️ Tóm Tắt 4 Giai Đoạn Phòng Lab (180 Phút) & Rubric 10 Điểm</h3>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem;">
      
      <!-- Giai đoạn 1 -->
      <div class="academic-card" style="border-top: 4px solid var(--primary-blue);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
          <h4 style="color: var(--primary-blue); margin: 0;">Giai đoạn 1: Chuẩn hóa VS (30')</h4>
          <span class="clo-badge" style="background: rgba(29, 93, 155, 0.12); color: #1d5d9b;">2.0 Điểm</span>
        </div>
        <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.5; margin-bottom: 0.5rem;">
          Khởi tạo đúng cấu trúc Console .NET, quản lý Solution Explorer, Error List, biên dịch Ctrl+F5 và kỹ thuật nhận diện 3 lỗi cú pháp cơ bản: CS1002 (; expected), CS1513 (} expected), CS0103.
        </p>
      </div>

      <!-- Giai đoạn 2 -->
      <div class="academic-card" style="border-top: 4px solid var(--accent-green);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
          <h4 style="color: var(--accent-green); margin: 0;">Giai đoạn 2: I/O & Phép Chia (60')</h4>
          <span class="clo-badge" style="background: rgba(30, 132, 73, 0.12); color: #1e8449;">2.5 Điểm</span>
        </div>
        <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.5; margin-bottom: 0.5rem;">
          Làm chủ Write vs WriteLine, luồng Console.ReadLine() chuỗi, ép kiểu int.Parse, double.Parse, phép chia nguyên / và chia dư %, String Interpolation $"", 4 bài tập có hướng dẫn (HCN, tròn, đổi giây, tách chữ số).
        </p>
      </div>

      <!-- Giai đoạn 3 -->
      <div class="academic-card" style="border-top: 4px solid var(--accent-orange);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
          <h4 style="color: var(--accent-orange); margin: 0;">Giai đoạn 3: Rẽ Nhánh & Tự Luyện (50')</h4>
          <span class="clo-badge" style="background: rgba(225, 112, 18, 0.12); color: #e17012;">2.5 Điểm</span>
        </div>
        <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.5; margin-bottom: 0.5rem;">
          Cấu trúc if...else if...else, 3 bẫy lỗi logic (= vs ==, dấu ; sau if, chia cho 0). Thực chiến độc lập 5 bài tập tự luyện tại lớp: Max 3 số, Năm nhuận, PT bậc nhất, Cước taxi lũy tiến, Phân loại tam giác.
        </p>
      </div>

      <!-- Giai đoạn 4 -->
      <div class="academic-card" style="border-top: 4px solid #68217a;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
          <h4 style="color: #68217a; margin: 0;">Giai đoạn 4: Thử Thách Tiền Điện (40')</h4>
          <span class="clo-badge" style="background: rgba(104, 33, 122, 0.12); color: #68217a;">3.0 Điểm</span>
        </div>
        <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.5; margin-bottom: 0.5rem;">
          Phần mềm tính BMI mẫu của giảng viên và Đề bài đánh giá năng lực độc lập: Hệ thống Tính tiền điện sinh hoạt bậc thang (4 bậc giá + thuế VAT 8%) & In hóa đơn thanh toán Console chuẩn mực.
        </p>
      </div>

    </div>
  </div>

  <!-- Khối Đồ Án Về Nhà -->
  <div class="academic-card" style="background: var(--bg-subtle); border-left: 5px solid var(--primary-blue);">
    <h4 style="color: var(--primary-navy); margin-bottom: 0.5rem;">🏠 Hệ thống 4 Đồ Án Tự Luyện Về Nhà (Homework Projects)</h4>
    <p style="font-size: 0.92rem; color: var(--text-muted); margin-bottom: 0.75rem;">
      Sinh viên hoàn thành tại nhà trước khi bước sang mô hình Lập trình Hướng đối tượng (OOP) ở Chương 4:
    </p>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 0.75rem; font-size: 0.88rem;">
      <div style="padding: 0.5rem 0.75rem; background: var(--bg-card); border-radius: 6px; border: 1px solid var(--border-color);">
        <strong>Bài 1:</strong> Máy tính chuyển đổi đơn vị đo (Metric Converter)
      </div>
      <div style="padding: 0.5rem 0.75rem; background: var(--bg-card); border-radius: 6px; border: 1px solid var(--border-color);">
        <strong>Bài 2:</strong> Mô phỏng máy rút tiền ATM (Cash Breakdown)
      </div>
      <div style="padding: 0.5rem 0.75rem; background: var(--bg-card); border-radius: 6px; border: 1px solid var(--border-color);">
        <strong>Bài 3:</strong> Kiểm tra ngày hợp lệ & Tìm ngày kế tiếp (Next Day)
      </div>
      <div style="padding: 0.5rem 0.75rem; background: var(--bg-card); border-radius: 6px; border: 1px solid var(--border-color);">
        <strong>Bài 4:</strong> Trò chơi Oẳn Tù Tì với máy tính (lớp Random)
      </div>
    </div>
  </div>

</div>
'''

# ==============================================================================
# 3. CẬP NHẬT js/chapter_data.js
# ==============================================================================
with open('js/chapter_data.js', 'r', encoding='utf-8') as f:
    ch_data = f.read()

import json
# Tạo chuỗi json escaped cho labHtml
lab_html_json = json.dumps(lab_html_content.strip(), ensure_ascii=False)

# Chèn labHtml vào "3": { ... }
# Tìm vị trí "codesHtml" của Chapter 3
pos_ch3 = ch_data.find('"3": {')
if pos_ch3 != -1:
    pos_ch3_end = ch_data.find('"4": {', pos_ch3)
    # Tìm "codesHtml" bên trong Chapter 3
    pos_codes = ch_data.find('"codesHtml":', pos_ch3)
    if pos_codes != -1 and (pos_ch3_end == -1 or pos_codes < pos_ch3_end):
        # Kiểm tra xem labHtml đã có chưa
        pos_lab = ch_data.find('"labHtml":', pos_ch3)
        if pos_lab != -1 and (pos_ch3_end == -1 or pos_lab < pos_ch3_end):
            print("labHtml already exists in Chapter 3 metadata.")
        else:
            # Chèn "labHtml": ..., ngay trước "codesHtml":
            insert_str = f'"labHtml": {lab_html_json},\n    '
            ch_data = ch_data[:pos_codes] + insert_str + ch_data[pos_codes:]
            print("Inserted labHtml into Chapter 3 metadata.")

# Cập nhật pills của Chapter 3 nếu chưa có
old_pills = '"💻 12 Bài tập giáo khoa C#"'
new_pills = '"💻 12 Bài tập giáo khoa C#",\n      "🧪 1 Bài Thực hành Lab 01"'
if old_pills in ch_data and new_pills not in ch_data:
    ch_data = ch_data.replace(old_pills, new_pills)
    print("Updated pills for Chapter 3.")

with open('js/chapter_data.js', 'w', encoding='utf-8') as f:
    f.write(ch_data)


# ==============================================================================
# 4. CẬP NHẬT js/app.js
# ==============================================================================
with open('js/app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Hàm setLabDoc
set_lab_doc_code = '''
// ============================================================================
// LAB 01 DOCUMENT SWITCHER (SLIDE VS GIÁO TRÌNH)
// ============================================================================
function setLabDoc(docKey) {
  const iframe = document.getElementById('labPdfViewerIframe');
  const titleDisplay = document.getElementById('labDocTitleDisplay');
  const externalLink = document.getElementById('labDocExternalLink');
  const btnSlide = document.getElementById('btnLabDocSlide');
  const btnGuide = document.getElementById('btnLabDocGuide');

  if (docKey === 'guide') {
    const guideUrl = './Lab/Huong-Dan-Thuc-Hanh-Lap-Trinh-CSharp-Chuong-1-den-3-v2.pdf';
    if (iframe) iframe.src = guideUrl;
    if (titleDisplay) titleDisplay.innerHTML = 'Đang xem: Giáo trình Hướng dẫn Thực hành v2.0 (Huong-Dan-Thuc-Hanh-Lap-Trinh-CSharp-Chuong-1-den-3-v2.pdf)';
    if (externalLink) externalLink.href = guideUrl;
    if (btnGuide) {
      btnGuide.style.background = 'var(--primary-navy)';
      btnGuide.style.color = 'white';
      btnGuide.style.borderColor = 'var(--primary-navy)';
    }
    if (btnSlide) {
      btnSlide.style.background = 'var(--bg-subtle)';
      btnSlide.style.color = 'var(--text-color)';
      btnSlide.style.borderColor = 'var(--border-color)';
    }
  } else {
    const slideUrl = './Lab/slide%20Chuong%2003%20-%20Lab%2001_v2.pdf';
    if (iframe) iframe.src = slideUrl;
    if (titleDisplay) titleDisplay.innerHTML = 'Đang xem: Slide Hướng dẫn Thực hành Lab (slide Chuong 03 - Lab 01_v2.pdf)';
    if (externalLink) externalLink.href = slideUrl;
    if (btnSlide) {
      btnSlide.style.background = '#68217a';
      btnSlide.style.color = 'white';
      btnSlide.style.borderColor = '#68217a';
    }
    if (btnGuide) {
      btnGuide.style.background = 'var(--bg-subtle)';
      btnGuide.style.color = 'var(--text-color)';
      btnGuide.style.borderColor = 'var(--border-color)';
    }
  }
}
window.setLabDoc = setLabDoc;
'''

if 'function setLabDoc' not in app_js:
    app_js += set_lab_doc_code
    print("Added setLabDoc function to app.js")

# Cập nhật updateChapterStaticContent để nạp tab-lab
target_update_static = '''  // Tab 6: Codes
  const tabCodes = document.getElementById('tab-codes');
  if (tabCodes && meta.codesHtml) {
    tabCodes.innerHTML = meta.codesHtml;
  }'''

replacement_update_static = '''  // Tab 6: Codes
  const tabCodes = document.getElementById('tab-codes');
  if (tabCodes && meta.codesHtml) {
    tabCodes.innerHTML = meta.codesHtml;
  }

  // Tab 7: Lab 01 (Dành riêng cho Chương 3)
  const tabLab = document.getElementById('tab-lab');
  if (tabLab) {
    if (chapterNum === 3 && meta.labHtml) {
      tabLab.innerHTML = meta.labHtml;
    } else {
      tabLab.innerHTML = '';
    }
  }'''

if target_update_static in app_js and '// Tab 7: Lab 01' not in app_js:
    app_js = app_js.replace(target_update_static, replacement_update_static)
    print("Updated updateChapterStaticContent in app.js")

# Cập nhật switchChapter để hiển thị/ẩn nút navTabBtnLab
target_switch_chapter = '''  // Update static tab contents (Overview, Docs, Codes) & Hero Banner
  updateChapterStaticContent(chapterNum);'''

replacement_switch_chapter = '''  // Hiển thị nút Tab Lab 01 riêng cho Chương 3
  const labTabBtn = document.getElementById('navTabBtnLab');
  if (labTabBtn) {
    if (chapterNum === 3) {
      labTabBtn.style.display = 'inline-flex';
    } else {
      labTabBtn.style.display = 'none';
      if (AppState.currentTab === 'lab') {
        switchTab('overview');
      }
    }
  }

  // Update static tab contents (Overview, Docs, Codes, Lab) & Hero Banner
  updateChapterStaticContent(chapterNum);'''

if target_switch_chapter in app_js and 'navTabBtnLab' not in app_js:
    app_js = app_js.replace(target_switch_chapter, replacement_switch_chapter)
    print("Updated switchChapter in app.js")

# Cập nhật initChapterSelector để kiểm tra ban đầu
target_init_selector = '''    const initialVal = parseInt(selector.value, 10);
    if (initialVal >= 2 && initialVal <= 4) {
      switchChapter(initialVal);
    } else {
      updateVideoTab(1);
    }'''

replacement_init_selector = '''    const initialVal = parseInt(selector.value, 10);
    const labTabBtn = document.getElementById('navTabBtnLab');
    if (labTabBtn) {
      labTabBtn.style.display = (initialVal === 3) ? 'inline-flex' : 'none';
    }
    if (initialVal >= 2 && initialVal <= 4) {
      switchChapter(initialVal);
    } else {
      updateVideoTab(1);
    }'''

if target_init_selector in app_js and 'labTabBtn.style.display = (initialVal === 3)' not in app_js:
    app_js = app_js.replace(target_init_selector, replacement_init_selector)
    print("Updated initChapterSelector in app.js")

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print("ALL FILES UPDATED SUCCESSFULLY!")
