# -*- coding: utf-8 -*-
"""
Process Chapter 3 slides:
1. Verify Chapter_3_Introduction_to_CSharp_App_Programming_IT26M.pdf (45 pages).
2. Copy to Slides/slideChapter_03.pdf, VideoCShape/Chapter_03/slideChapter_03.pdf & Slide_Chapter_03.pdf.
3. Split into 4 parts (<= 15 slides each) in Slides_CShape/ and Slides/.
4. Render 45 high-res PNG images into VideoCShape/Chapter_03/images/slide-{i}.png.
5. Create VideoCShape/Chapter_03/index.html.
"""

import os
import shutil
import fitz

BASE_DIR = r"i:\Course_UDA\Kỹ thuật lập trình\ebooks\new ebooks\WebProgramingTechnique2026"
SRC_PDF = os.path.join(BASE_DIR, "Slides_CShape", "Chapter_3_Introduction_to_CSharp_App_Programming_IT26M.pdf")
SLIDES_DIR = os.path.join(BASE_DIR, "Slides")
SLIDES_CSHAPE_DIR = os.path.join(BASE_DIR, "Slides_CShape")
VIDEO_CH03_DIR = os.path.join(BASE_DIR, "VideoCShape", "Chapter_03")
IMAGES_DIR = os.path.join(VIDEO_CH03_DIR, "images")

os.makedirs(SLIDES_DIR, exist_ok=True)
os.makedirs(VIDEO_CH03_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)

# 1. Check source PDF
doc = fitz.open(SRC_PDF)
page_count = len(doc)
print(f"Source PDF has {page_count} pages.")
assert page_count == 45, f"Expected 45 pages, got {page_count}"

# 2. Copy to Slides and VideoCShape
dst_slides = os.path.join(SLIDES_DIR, "slideChapter_03.pdf")
dst_video1 = os.path.join(VIDEO_CH03_DIR, "slideChapter_03.pdf")
dst_video2 = os.path.join(VIDEO_CH03_DIR, "Slide_Chapter_03.pdf")

shutil.copyfile(SRC_PDF, dst_slides)
shutil.copyfile(SRC_PDF, dst_video1)
shutil.copyfile(SRC_PDF, dst_video2)
print("Copied slideChapter_03.pdf to Slides/ and VideoCShape/Chapter_03/")

# 3. Split into 4 parts (<= 15 slides)
parts = [
    {
        "name": "P1_Chapter03_Tong_Quan_Console_va_Cu_Phap.pdf",
        "alias": "P1_Chapter03.pdf",
        "start": 0,
        "end": 14  # Slides 1-15 (15 slides)
    },
    {
        "name": "P2_Chapter03_Dinh_Dang_Chuoi_va_Interpolation.pdf",
        "alias": "P2_Chapter03.pdf",
        "start": 15,
        "end": 24  # Slides 16-25 (10 slides)
    },
    {
        "name": "P3_Chapter03_Bien_Bo_Nho_va_Toan_Tu_So_Hoc.pdf",
        "alias": "P3_Chapter03.pdf",
        "start": 25,
        "end": 34  # Slides 26-35 (10 slides)
    },
    {
        "name": "P4_Chapter03_Cau_Truc_Dieu_Kien_va_So_Sanh.pdf",
        "alias": "P4_Chapter03.pdf",
        "start": 35,
        "end": 44  # Slides 36-45 (10 slides)
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
