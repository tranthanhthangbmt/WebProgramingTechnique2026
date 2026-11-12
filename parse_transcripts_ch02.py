# -*- coding: utf-8 -*-
import json

with open("VideoCShape/Chapter_02/script.txt", "r", encoding="utf-8") as f:
    text = f.read()

slides_raw = text.split("\n\n")
transcripts = {}

for s in slides_raw:
    lines = [l.strip() for l in s.split("\n") if l.strip()]
    if not lines:
        continue
    # Line 0: Slide X: <Title>
    header = lines[0]
    slide_num = header.split(":")[0].replace("Slide", "").strip()
    title = header.split(":", 1)[1].strip() if ":" in header else f"Slide {slide_num}"
    
    p1_parts = []
    p2_parts = []
    
    for l in lines[1:]:
        if l.startswith("Người 1:"):
            p1_parts.append(l.replace("Người 1:", "").strip())
        elif l.startswith("Người 2:"):
            p2_parts.append(l.replace("Người 2:", "").strip())
            
    transcripts[slide_num] = {
        "title": title,
        "speaker1": " ".join(p1_parts),
        "speaker2": " ".join(p2_parts)
    }

print(f"Parsed {len(transcripts)} slides from Chapter 2 script.txt")

js_code = "const SLIDE_TRANSCRIPTS_CHAPTER_02 = " + json.dumps(transcripts, ensure_ascii=False, indent=2) + ";\n"
with open("js/transcripts_ch02.js", "w", encoding="utf-8") as f:
    f.write(js_code)

print("Saved js/transcripts_ch02.js successfully!")

