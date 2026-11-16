# -*- coding: utf-8 -*-
import fitz
import os

pdf_path = r"VideoCShape\Chapter_03\slideChapter_03.pdf"
doc = fitz.open(pdf_path)
print(f"Total pages: {len(doc)}")

images_dir = r"VideoCShape\Chapter_03\images"
os.makedirs(images_dir, exist_ok=True)

matrix = fitz.Matrix(2.0, 2.0)
for i in range(len(doc)):
    page = doc[i]
    pix = page.get_pixmap(matrix=matrix, alpha=False)
    img_path = os.path.join(images_dir, f"slide-{i+1}.png")
    pix.save(img_path)
    if (i+1) % 10 == 0 or (i+1) == len(doc):
        print(f"Saved slide-{i+1}.png ({pix.width}x{pix.height})")

print("All 45 images updated from user's slideChapter_03.pdf!")
