# -*- coding: utf-8 -*-
import easyocr
import time

print("Initializing EasyOCR...")
t0 = time.time()
reader = easyocr.Reader(['vi', 'en'], gpu=False)
t1 = time.time()
print(f"Reader initialized in {t1 - t0:.2f}s")

img_path = r"VideoCShape\Chapter_03\images\slide-1.png"
res = reader.readtext(img_path, detail=0)
t2 = time.time()
print(f"Read slide 1 in {t2 - t1:.2f}s")
print("Slide 1 Text:")
print(" | ".join(res[:10]))
