import time
from PIL import Image
import easyocr

reader = easyocr.Reader(['vi', 'en'], gpu=False)

titles = []
for i in range(1, 46):
    img_path = f"VideoCShape/Chapter_03/images/slide-{i}.png"
    img = Image.open(img_path)
    w, h = img.size
    
    # Crop top 25% for header/title
    crop_box = (0, 0, w, int(h * 0.25))
    cropped = img.crop(crop_box)
    
    # Resize cropped title to width 800
    cw, ch = cropped.size
    new_w = 800
    new_h = int(ch * (new_w / cw))
    resized = cropped.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    temp_path = "temp_title.png"
    resized.save(temp_path)
    
    results = reader.readtext(temp_path, detail=0)
    title_text = " ".join(results)
    titles.append((i, title_text))
    print(f"Slide {i}: {title_text}")

with open("ocr_titles_summary.txt", "w", encoding="utf-8") as f:
    for i, t in titles:
        f.write(f"Slide {i}: {t}\n")
