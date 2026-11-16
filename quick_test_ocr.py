import time
from PIL import Image
import easyocr

t0 = time.time()
reader = easyocr.Reader(['vi', 'en'], gpu=False)
print(f"Reader init: {time.time() - t0:.2f}s")

for i in [1, 2, 5, 10, 20]:
    t1 = time.time()
    img_path = f"VideoCShape/Chapter_03/images/slide-{i}.png"
    img = Image.open(img_path)
    # Resize to width 960
    w, h = img.size
    new_w = 960
    new_h = int(h * (new_w / w))
    img_resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    temp_path = f"VideoCShape/Chapter_03/images/thumb_{i}.png"
    img_resized.save(temp_path)
    
    results = reader.readtext(temp_path, detail=0)
    print(f"Slide {i} ({time.time() - t1:.2f}s): {' | '.join(results[:5])}")
