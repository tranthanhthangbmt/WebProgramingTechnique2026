# -*- coding: utf-8 -*-
"""
Sync Chapter 4 transcripts from VideoCShape/Chapter_04/script.txt to js/transcripts_ch04.js
"""

import json
import re
import os

src_script = r"VideoCShape\Chapter_04\script.txt"
dest_js = r"js\transcripts_ch04.js"

with open(src_script, "r", encoding="utf-8") as f:
    text = f.read()

# Pattern to parse slides
slides = re.split(r'\n(?=Slide \d+:)', text.strip())
transcripts = {}

for s in slides:
    lines = [l.strip() for l in s.split('\n') if l.strip()]
    if not lines:
        continue
    m = re.match(r'Slide (\d+):\s*(.*)', lines[0])
    if not m:
        continue
    slide_num = m.group(1)
    slide_title = m.group(2)
    
    sp1_parts = []
    sp2_parts = []
    
    current_sp = None
    for line in lines[1:]:
        if line.startswith("Người 1:"):
            current_sp = 1
            sp1_parts.append(line.replace("Người 1:", "").strip())
        elif line.startswith("Người 2:"):
            current_sp = 2
            sp2_parts.append(line.replace("Người 2:", "").strip())
        else:
            if current_sp == 1:
                sp1_parts.append(line)
            elif current_sp == 2:
                sp2_parts.append(line)
                
    transcripts[slide_num] = {
        "title": slide_title,
        "speaker1": " ".join(sp1_parts),
        "speaker2": " ".join(sp2_parts)
    }

js_content = "// ============================================================================\n"
js_content += "// LỜI THUYẾT MINH VIDEO & ĐỐI THOẠI BÀI GIẢNG CHƯƠNG 4 (45 SLIDES)\n"
js_content += "// ============================================================================\n"
js_content += "const SLIDE_TRANSCRIPTS_CHAPTER_04 = " + json.dumps(transcripts, ensure_ascii=False, indent=2) + ";\n\n"
js_content += "if (typeof window !== 'undefined') {\n"
js_content += "  window.SLIDE_TRANSCRIPTS_CHAPTER_04 = SLIDE_TRANSCRIPTS_CHAPTER_04;\n"
js_content += "}\n"
js_content += "if (typeof module !== 'undefined' && module.exports) {\n"
js_content += "  module.exports = { SLIDE_TRANSCRIPTS_CHAPTER_04 };\n"
js_content += "}\n"

with open(dest_js, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Generated {dest_js} with {len(transcripts)} slides!")
