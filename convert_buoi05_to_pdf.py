# -*- coding: utf-8 -*-
"""
Convert Lab/Huong-Dan-Thuc-Hanh-Lap-Trinh-CSharp-Buoi-05.docx to PDF
using Word COM (win32com)
"""
import os
import sys

def convert_to_pdf():
    docx_path = os.path.abspath("Lab/Huong-Dan-Thuc-Hanh-Lap-Trinh-CSharp-Buoi-05.docx")
    pdf_path = os.path.abspath("Lab/Huong-Dan-Thuc-Hanh-Lap-Trinh-CSharp-Buoi-05.pdf")

    if not os.path.exists(docx_path):
        print(f"Error: {docx_path} not found.")
        return False

    print(f"Converting:\n  Input:  {docx_path}\n  Output: {pdf_path}")
    try:
        import win32com.client
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False
        doc = word.Documents.Open(docx_path)
        # 17 = wdFormatPDF
        doc.SaveAs(pdf_path, FileFormat=17)
        doc.Close()
        word.Quit()
        print("Conversion to PDF successful via Word COM!")
        return True
    except Exception as e:
        print(f"Word COM conversion failed: {e}")
        return False

if __name__ == "__main__":
    convert_to_pdf()
