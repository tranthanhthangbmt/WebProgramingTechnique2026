# -*- coding: utf-8 -*-
"""
Process Chapter 4 slides:
1. Verify Chapter_4_Introduction_to_Classes_Objects_Methods_and_strings_IT26M.pdf (45 pages).
2. Copy to:
   - Slides_CShape/Chapter_04.pdf
   - Slides/slideChapter_04.pdf & Slide_Chapter_04.pdf
   - VideoCShape/Chapter_04/slideChapter_04.pdf & Slide_Chapter_04.pdf
3. Split into 4 parts (<= 15 slides each) in Slides_CShape/ and Slides/.
4. Render 45 high-res PNG images into VideoCShape/Chapter_04/images/slide-{i}.png.
5. Create VideoCShape/Chapter_04/index.html.
"""

import os
import shutil
import fitz

BASE_DIR = r"i:\Course_UDA\Kỹ thuật lập trình\ebooks\new ebooks\WebProgramingTechnique2026"
SRC_PDF = os.path.join(BASE_DIR, "Slides_CShape", "Chapter_4_Introduction_to_Classes_Objects_Methods_and_strings_IT26M.pdf")
SLIDES_DIR = os.path.join(BASE_DIR, "Slides")
SLIDES_CSHAPE_DIR = os.path.join(BASE_DIR, "Slides_CShape")
VIDEO_CH04_DIR = os.path.join(BASE_DIR, "VideoCShape", "Chapter_04")
IMAGES_DIR = os.path.join(VIDEO_CH04_DIR, "images")
AUDIO_DIR = os.path.join(VIDEO_CH04_DIR, "audio")

os.makedirs(SLIDES_DIR, exist_ok=True)
os.makedirs(VIDEO_CH04_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(AUDIO_DIR, exist_ok=True)

# 1. Check source PDF
doc = fitz.open(SRC_PDF)
page_count = len(doc)
print(f"Source PDF has {page_count} pages.")
assert page_count == 45, f"Expected 45 pages, got {page_count}"

# 2. Copy to Master locations
dst_cshape_alias = os.path.join(SLIDES_CSHAPE_DIR, "Chapter_04.pdf")
dst_slides = os.path.join(SLIDES_DIR, "slideChapter_04.pdf")
dst_slides_alias = os.path.join(SLIDES_DIR, "Slide_Chapter_04.pdf")
dst_video1 = os.path.join(VIDEO_CH04_DIR, "slideChapter_04.pdf")
dst_video2 = os.path.join(VIDEO_CH04_DIR, "Slide_Chapter_04.pdf")

shutil.copyfile(SRC_PDF, dst_cshape_alias)
shutil.copyfile(SRC_PDF, dst_slides)
shutil.copyfile(SRC_PDF, dst_slides_alias)
shutil.copyfile(SRC_PDF, dst_video1)
shutil.copyfile(SRC_PDF, dst_video2)
print("Copied master PDF to Slides_CShape, Slides/ and VideoCShape/Chapter_04/")

# 3. Split into 4 parts (<= 15 slides)
parts = [
    {
        "name": "P1_Chapter04_Lop_DoiTuong_va_KieuThamChieu.pdf",
        "alias": "P1_Chapter04.pdf",
        "start": 0,
        "end": 14  # Slides 1-15 (15 slides)
    },
    {
        "name": "P2_Chapter04_ThuocTinh_Properties_va_AutoProps.pdf",
        "alias": "P2_Chapter04.pdf",
        "start": 15,
        "end": 26  # Slides 16-27 (12 slides)
    },
    {
        "name": "P3_Chapter04_HamKhoiTao_Constructor_va_UML.pdf",
        "alias": "P3_Chapter04.pdf",
        "start": 27,
        "end": 35  # Slides 28-36 (9 slides)
    },
    {
        "name": "P4_Chapter04_KieuDecimal_DinhDangTienTe_va_ATM.pdf",
        "alias": "P4_Chapter04.pdf",
        "start": 36,
        "end": 44  # Slides 37-45 (9 slides)
    }
]

for p in parts:
    sub_doc = fitz.open()
    sub_doc.insert_pdf(doc, from_page=p["start"], to_page=p["end"])
    
    # Save in Slides_CShape
    path_long_cs = os.path.join(SLIDES_CSHAPE_DIR, p["name"])
    path_short_cs = os.path.join(SLIDES_CSHAPE_DIR, p["alias"])
    sub_doc.save(path_long_cs)
    shutil.copyfile(path_long_cs, path_short_cs)
    
    # Save in Slides
    path_long_sl = os.path.join(SLIDES_DIR, p["name"])
    path_short_sl = os.path.join(SLIDES_DIR, p["alias"])
    shutil.copyfile(path_long_cs, path_long_sl)
    shutil.copyfile(path_long_cs, path_short_sl)
    
    print(f"Generated {p['name']} ({p['end'] - p['start'] + 1} slides)")

# 4. Render slide images (slide-1.png .. slide-45.png)
matrix = fitz.Matrix(2.0, 2.0) # 2x zoom for high retina crispness
for i, page in enumerate(doc):
    slide_num = i + 1
    pix = page.get_pixmap(matrix=matrix, alpha=False)
    img_path = os.path.join(IMAGES_DIR, f"slide-{slide_num}.png")
    pix.save(img_path)
    if slide_num % 10 == 0 or slide_num == 45:
        print(f"Rendered slide-{slide_num}.png ({pix.width}x{pix.height})")

doc.close()
print("All 45 slide images rendered successfully!")

# 5. Copy index.html from Chapter_03
ch03_index = os.path.join(BASE_DIR, "VideoCShape", "Chapter_03", "index.html")
ch04_index = os.path.join(VIDEO_CH04_DIR, "index.html")
if os.path.exists(ch03_index):
    shutil.copyfile(ch03_index, ch04_index)
    print("Created VideoCShape/Chapter_04/index.html from Chapter_03 template.")
