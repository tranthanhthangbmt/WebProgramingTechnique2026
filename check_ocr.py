# -*- coding: utf-8 -*-
for m in ["pytesseract", "easyocr", "fitz", "rapidocr_onnxruntime", "PIL"]:
    try:
        mod = __import__(m)
        print(f"{m}: available")
    except Exception as e:
        print(f"{m}: NOT available ({e})")
