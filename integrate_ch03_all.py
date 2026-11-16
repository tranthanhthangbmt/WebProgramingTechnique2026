# -*- coding: utf-8 -*-
"""
Integrate Chapter 3 across:
1. js/quiz_data.js
2. js/exercises_data.js
3. js/interactive_exercises.js
4. js/app.js
5. index.html
"""

import json
import os
import re

BASE_DIR = r"i:\Course_UDA\Kỹ thuật lập trình\ebooks\new ebooks\WebProgramingTechnique2026"
JS_DIR = os.path.join(BASE_DIR, "js")

# 1. Integrate js/quiz_data.js
with open("js/quiz_ch03_snippet.json", "r", encoding="utf-8") as f:
    quiz_ch3 = json.load(f)

quiz_js_path = os.path.join(JS_DIR, "quiz_data.js")
with open(quiz_js_path, "r", encoding="utf-8") as f:
    quiz_content = f.read()

if "QUIZ_CHAPTER_03" not in quiz_content:
    # Ensure every question in quiz_ch3 has both 'correct' and 'answer'
    for q in quiz_ch3:
        q["answer"] = q["correct"]
    
    quiz_ch3_str = "\n\n// " + "="*76 + "\n"
    quiz_ch3_str += "// NGÂN HÀNG CÂU HỎI TRẮC NGHIỆM CHƯƠNG 3: INTRODUCTION TO C# APP PROGRAMMING\n"
    quiz_ch3_str += "// (40 CÂU CÂN BẰNG ĐỘ DÀI & ĐÁP ÁN: 10 A, 10 B, 10 C, 10 D; 10 R1, 10 R2, 10 R3, 10 R4)\n"
    quiz_ch3_str += "// " + "="*76 + "\n"
    quiz_ch3_str += "const QUIZ_CHAPTER_03 = " + json.dumps(quiz_ch3, ensure_ascii=False, indent=2) + ";\n\n"
    quiz_ch3_str += "if (typeof window !== 'undefined') {\n"
    quiz_ch3_str += "  window.QUIZ_CHAPTER_01 = (typeof QUIZ_CHAPTER_01 !== 'undefined') ? QUIZ_CHAPTER_01 : [];\n"
    quiz_ch3_str += "  window.QUIZ_CHAPTER_02 = (typeof QUIZ_CHAPTER_02 !== 'undefined') ? QUIZ_CHAPTER_02 : [];\n"
    quiz_ch3_str += "  window.QUIZ_CHAPTER_03 = QUIZ_CHAPTER_03;\n"
    quiz_ch3_str += "}\n"
    quiz_ch3_str += "if (typeof module !== 'undefined' && module.exports) {\n"
    quiz_ch3_str += "  module.exports = { QUIZ_CHAPTER_01, QUIZ_CHAPTER_02, QUIZ_CHAPTER_03 };\n"
    quiz_ch3_str += "}\n"
    
    # Also ensure QUIZ_CHAPTER_02 items have correct set if they only have answer
    # We can append quiz_ch3_str
    with open(quiz_js_path, "w", encoding="utf-8") as f:
        f.write(quiz_content + quiz_ch3_str)
    print("Appended QUIZ_CHAPTER_03 to js/quiz_data.js")
else:
    print("QUIZ_CHAPTER_03 already in js/quiz_data.js")

# 2. Integrate js/exercises_data.js
with open("js/exercises_ch03_snippet.json", "r", encoding="utf-8") as f:
    ex_ch3 = json.load(f)

ex_js_path = os.path.join(JS_DIR, "exercises_data.js")
with open(ex_js_path, "r", encoding="utf-8") as f:
    ex_content = f.read()

if "EXERCISES_CHAPTER_03" not in ex_content:
    ex_ch3_str = "\n\n// " + "="*76 + "\n"
    ex_ch3_str += "// HỆ THỐNG BÀI TẬP CHƯƠNG 3: INTRODUCTION TO C# APP PROGRAMMING\n"
    ex_ch3_str += "// " + "="*76 + "\n"
    ex_ch3_str += "const EXERCISES_CHAPTER_03 = " + json.dumps(ex_ch3, ensure_ascii=False, indent=2) + ";\n\n"
    ex_ch3_str += "if (typeof window !== 'undefined') {\n"
    ex_ch3_str += "  window.EXERCISES_CHAPTER_01 = (typeof EXERCISES_CHAPTER_01 !== 'undefined') ? EXERCISES_CHAPTER_01 : [];\n"
    ex_ch3_str += "  window.EXERCISES_CHAPTER_02 = (typeof EXERCISES_CHAPTER_02 !== 'undefined') ? EXERCISES_CHAPTER_02 : [];\n"
    ex_ch3_str += "  window.EXERCISES_CHAPTER_03 = EXERCISES_CHAPTER_03;\n"
    ex_ch3_str += "}\n"
    ex_ch3_str += "if (typeof module !== 'undefined' && module.exports) {\n"
    ex_ch3_str += "  module.exports = { EXERCISES_CHAPTER_01, EXERCISES_CHAPTER_02, EXERCISES_CHAPTER_03 };\n"
    ex_ch3_str += "}\n"
    
    with open(ex_js_path, "w", encoding="utf-8") as f:
        f.write(ex_content + ex_ch3_str)
    print("Appended EXERCISES_CHAPTER_03 to js/exercises_data.js")
else:
    print("EXERCISES_CHAPTER_03 already in js/exercises_data.js")

# 3. Integrate js/interactive_exercises.js
with open("js/interactive_ch03_snippet.json", "r", encoding="utf-8") as f:
    interactive_ch3 = json.load(f)

interactive_js_path = os.path.join(JS_DIR, "interactive_exercises.js")
with open(interactive_js_path, "r", encoding="utf-8") as f:
    interactive_content = f.read()

# We can insert Chapter 3 into INTERACTIVE_EXERCISES_DATA right before generateInteractiveWorkspace
target_str = "function generateInteractiveWorkspace(item) {"
if '"3.1":' not in interactive_content and target_str in interactive_content:
    ch3_interactive_blocks = []
    for k, v in interactive_ch3.items():
        ch3_interactive_blocks.append(f'  "{k}": ' + json.dumps(v, ensure_ascii=False, indent=4))
    
    injection = "  // --------------------------------------------------------------------------\n"
    injection += "  // CHƯƠNG 3: INTRODUCTION TO C# APP PROGRAMMING\n"
    injection += "  // --------------------------------------------------------------------------\n"
    injection += ",\n".join(ch3_interactive_blocks) + ",\n\n"
    
    # Find the end of INTERACTIVE_EXERCISES_DATA object
    # In interactive_exercises.js, let's see where INTERACTIVE_EXERCISES_DATA ends
    pattern = r"(const INTERACTIVE_EXERCISES_DATA\s*=\s*\{)"
    m = re.search(pattern, interactive_content)
    if m:
        # insert right at the beginning of INTERACTIVE_EXERCISES_DATA
        pos = m.end()
        new_interactive = interactive_content[:pos] + "\n" + injection + interactive_content[pos:]
        with open(interactive_js_path, "w", encoding="utf-8") as f:
            f.write(new_interactive)
        print("Injected Chapter 3 interactive exercises into js/interactive_exercises.js")
    else:
        print("Warning: Could not find INTERACTIVE_EXERCISES_DATA definition")
else:
    print("Chapter 3 interactive exercises already present or target not found.")

# 4. Update js/app.js to support Chapter 3
app_js_path = os.path.join(JS_DIR, "app.js")
with open(app_js_path, "r", encoding="utf-8") as f:
    app_content = f.read()

# Update getCurrentQuiz
old_quiz = """function getCurrentQuiz() {
  if (AppState.currentChapter === 2) {
    return (typeof QUIZ_CHAPTER_02 !== 'undefined') ? QUIZ_CHAPTER_02 : [];
  }
  return (typeof QUIZ_CHAPTER_01 !== 'undefined') ? QUIZ_CHAPTER_01 : [];
}"""

new_quiz = """function getCurrentQuiz() {
  if (AppState.currentChapter === 3) {
    return (typeof QUIZ_CHAPTER_03 !== 'undefined') ? QUIZ_CHAPTER_03 : [];
  }
  if (AppState.currentChapter === 2) {
    return (typeof QUIZ_CHAPTER_02 !== 'undefined') ? QUIZ_CHAPTER_02 : [];
  }
  return (typeof QUIZ_CHAPTER_01 !== 'undefined') ? QUIZ_CHAPTER_01 : [];
}"""

# Update getCurrentExercises
old_ex = """function getCurrentExercises() {
  if (AppState.currentChapter === 2) {
    return (typeof EXERCISES_CHAPTER_02 !== 'undefined') ? EXERCISES_CHAPTER_02 : [];
  }
  return (typeof EXERCISES_CHAPTER_01 !== 'undefined') ? EXERCISES_CHAPTER_01 : [];
}"""

new_ex = """function getCurrentExercises() {
  if (AppState.currentChapter === 3) {
    return (typeof EXERCISES_CHAPTER_03 !== 'undefined') ? EXERCISES_CHAPTER_03 : [];
  }
  if (AppState.currentChapter === 2) {
    return (typeof EXERCISES_CHAPTER_02 !== 'undefined') ? EXERCISES_CHAPTER_02 : [];
  }
  return (typeof EXERCISES_CHAPTER_01 !== 'undefined') ? EXERCISES_CHAPTER_01 : [];
}"""

# Update getCurrentTranscripts
old_tr = """function getCurrentTranscripts() {
  if (AppState.currentChapter === 2) {
    return (typeof SLIDE_TRANSCRIPTS_CHAPTER_02 !== 'undefined') ? SLIDE_TRANSCRIPTS_CHAPTER_02 : {};
  }
  if (typeof SLIDE_TRANSCRIPTS_CHAPTER_01 !== 'undefined') {
    return SLIDE_TRANSCRIPTS_CHAPTER_01;
  }
  if (typeof SLIDE_TRANSCRIPTS !== 'undefined') {
    return SLIDE_TRANSCRIPTS;
  }
  return {};
}"""

new_tr = """function getCurrentTranscripts() {
  if (AppState.currentChapter === 3) {
    return (typeof SLIDE_TRANSCRIPTS_CHAPTER_03 !== 'undefined') ? SLIDE_TRANSCRIPTS_CHAPTER_03 : {};
  }
  if (AppState.currentChapter === 2) {
    return (typeof SLIDE_TRANSCRIPTS_CHAPTER_02 !== 'undefined') ? SLIDE_TRANSCRIPTS_CHAPTER_02 : {};
  }
  if (typeof SLIDE_TRANSCRIPTS_CHAPTER_01 !== 'undefined') {
    return SLIDE_TRANSCRIPTS_CHAPTER_01;
  }
  if (typeof SLIDE_TRANSCRIPTS !== 'undefined') {
    return SLIDE_TRANSCRIPTS;
  }
  return {};
}"""

if old_quiz in app_content:
    app_content = app_content.replace(old_quiz, new_quiz)
if old_ex in app_content:
    app_content = app_content.replace(old_ex, new_ex)
if old_tr in app_content:
    app_content = app_content.replace(old_tr, new_tr)

# Also ensure quiz checking handles both q.correct and q.answer:
# Search for `if (AppState.userAnswers[q.id] === q.correct)` -> `q.correct !== undefined ? q.correct : q.answer`
app_content = re.sub(
    r"AppState\.userAnswers\[q\.id\] === q\.correct",
    "AppState.userAnswers[q.id] === (q.correct !== undefined ? q.correct : q.answer)",
    app_content
)
app_content = re.sub(
    r"optIdx === q\.correct",
    "optIdx === (q.correct !== undefined ? q.correct : q.answer)",
    app_content
)

with open(app_js_path, "w", encoding="utf-8") as f:
    f.write(app_content)
print("Updated js/app.js successfully!")

# 5. Update index.html
index_html_path = os.path.join(BASE_DIR, "index.html")
with open(index_html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Enable Chapter 3 option
html_content = html_content.replace(
    '<option value="3" disabled>Chương 3: Introduction to C# App Programming</option>',
    '<option value="3">Chương 3: Introduction to C# App Programming</option>'
)

# Add transcripts_ch03.js script tag
if "transcripts_ch03.js" not in html_content:
    html_content = html_content.replace(
        '<script src="./js/transcripts_ch02.js"></script>',
        '<script src="./js/transcripts_ch02.js"></script>\n  <script src="./js/transcripts_ch03.js"></script>'
    )
    print("Added transcripts_ch03.js to index.html")

with open(index_html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Updated index.html successfully!")
print("ALL INTEGRATION COMPLETED!")
