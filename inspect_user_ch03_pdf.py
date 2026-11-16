# -*- coding: utf-8 -*-
import fitz
import os
import datetime

pdf_path = r"VideoCShape\Chapter_03\slideChapter_03.pdf"
stat = os.stat(pdf_path)
mtime = datetime.datetime.fromtimestamp(stat.st_mtime)

print(f"File: {pdf_path}")
print(f"Size: {stat.st_size} bytes")
print(f"Modified time: {mtime}")

doc = fitz.open(pdf_path)
print(f"Total pages: {len(doc)}")

output_txt = r"VideoCShape\Chapter_03\slide_readable.txt"
with open(output_txt, "w", encoding="utf-8") as out:
    for i in range(len(doc)):
        text = doc[i].get_text().strip()
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        title = lines[0] if lines else f"Slide {i+1}"
        out.write(f"\n=== SLIDE {i+1} ===\n")
        out.write(text + "\n")
        print(f"Slide {i+1}: {title} (lines: {len(lines)})")

print(f"Wrote full slide text to {output_txt}")
