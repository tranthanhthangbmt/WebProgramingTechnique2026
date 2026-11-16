import fitz

parts = [
    ('Slides_CShape/P1_Chapter03_Tong_Quan_Console_va_Cu_Phap.pdf', 1),
    ('Slides_CShape/P2_Chapter03_Dinh_Dang_Chuoi_va_Interpolation.pdf', 16),
    ('Slides_CShape/P3_Chapter03_Bien_Bo_Nho_va_Toan_Tu_So_Hoc.pdf', 26),
    ('Slides_CShape/P4_Chapter03_Cau_Truc_Dieu_Kien_va_So_Sanh.pdf', 36)
]

with open('p_slides_text.txt', 'w', encoding='utf-8') as out:
    for filename, start_idx in parts:
        doc = fitz.open(filename)
        for i, page in enumerate(doc):
            slide_num = start_idx + i
            text = page.get_text().strip()
            out.write(f"=== SLIDE {slide_num} ===\n{text}\n\n")

print("Exported all 45 slides text to p_slides_text.txt")
