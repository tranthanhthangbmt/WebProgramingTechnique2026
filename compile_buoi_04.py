# -*- coding: utf-8 -*-
import subprocess
import os
import sys

# Step 1: Run create_tex_buoi_04.py
print("Running create_tex_buoi_04.py...")
res = subprocess.run([sys.executable, "create_tex_buoi_04.py"], capture_output=True, text=True, encoding="utf-8")
print(res.stdout)
if res.returncode != 0:
    print("Error generating tex:", res.stderr)
    sys.exit(1)

# Step 2: Compile with xelatex
tex_dir = os.path.abspath("Slides_CShape")
tex_file = "Slide_Buoi_04_NenTangLapTrinh_CSharp_IT26M.tex"
pdf_file = "Slide_Buoi_04_NenTangLapTrinh_CSharp_IT26M.pdf"

print(f"Compiling {tex_file} with XeLaTeX in {tex_dir}...")
cmd = ["xelatex", "-interaction=nonstopmode", tex_file]

compile_res = subprocess.run(cmd, cwd=tex_dir, capture_output=True, text=True, encoding="utf-8", errors="replace")
print("XeLaTeX Pass 1 Return code:", compile_res.returncode)

# Check for errors in log
log_file = os.path.join(tex_dir, "Slide_Buoi_04_NenTangLapTrinh_CSharp_IT26M.log")
if os.path.exists(log_file):
    with open(log_file, "r", encoding="utf-8", errors="replace") as f:
        log_lines = f.readlines()
    err_lines = [line for line in log_lines if line.startswith("!") or "Fatal error" in line or "Error:" in line]
    if err_lines:
        print("Log error snippets (first 10):")
        for l in err_lines[:10]:
            print("  ", l.strip())

# Second pass for totalframenumber
if compile_res.returncode == 0:
    print("Running XeLaTeX Pass 2 for cross-references...")
    subprocess.run(cmd, cwd=tex_dir, capture_output=True, text=True, encoding="utf-8", errors="replace")

# Check output pdf
pdf_path = os.path.join(tex_dir, pdf_file)
if os.path.exists(pdf_path):
    size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
    print(f"SUCCESS: Generated {pdf_path} ({size_mb:.2f} MB)")
else:
    print(f"FAILED: {pdf_path} not found.")
