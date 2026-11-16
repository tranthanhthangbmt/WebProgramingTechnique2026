# -*- coding: utf-8 -*-
import os, re, subprocess

with open("generate_ch03_beamer.py", "r", encoding="utf-8") as f:
    code = f.read()

# Replace \captionof{figure}{\scriptsize (text)} with {\centering\scriptsize (text)\par}
code = re.sub(
    r'\\captionof\{figure\}\{\\scriptsize ([^}]+)\}',
    r'{\\centering\\scriptsize \\textbf{\1}\\par}',
    code
)

# Fix unescaped & in slide 27
code = code.replace(r"\textbf{Ý nghĩa & Ký hiệu:}", r"\textbf{Ý nghĩa \& Ký hiệu:}")

# In Comparison.cs (Slide 37), make listing basicstyle tiny so it fits perfectly
code = code.replace(
    r"\begin{lstlisting}" + "\nusing System;\n\nclass Comparison",
    r"\begin{lstlisting}[basicstyle=\ttfamily\tiny]" + "\nusing System;\n\nclass Comparison"
)

with open("generate_ch03_beamer.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Updated generate_ch03_beamer.py!")
