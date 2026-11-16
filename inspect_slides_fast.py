import cv2
import easyocr
import numpy as np

reader = easyocr.Reader(['vi', 'en'], gpu=False)

slides_to_check = [4, 5, 6, 16, 17, 18, 19, 20, 21, 33, 34, 35, 37, 38, 39, 44, 45]

for num in slides_to_check:
    img_path = f"VideoCShape/Chapter_03/images/slide-{num}.png"
    img = cv2.imread(img_path)
    h, w = img.shape[:2]
    new_w = 900
    new_h = int(h * (new_w / w))
    resized = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)
    
    res = reader.readtext(resized, detail=0)
    print(f"=== SLIDE {num} ===")
    print(" | ".join(res[:12]))
