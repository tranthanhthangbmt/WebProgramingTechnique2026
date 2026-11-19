import fitz
import os

doc = fitz.open('textbook_CShape/Chapter_04.pdf')
out_dir = 'Slides_CShape/images'
os.makedirs(out_dir, exist_ok=True)

# List of figures with page index (0-based) and approximate bounding box [x0, y0, x1, y1]
# Page size is typically ~468 x ~648 pt
fig_configs = [
    # Fig 4.1: AccountTest.cs (Page 3, index 2)
    ("fig4_01_accounttest_app.png", 2, fitz.Rect(50, 230, 420, 560)),
    # Fig 4.2: Account.cs (Page 6, index 5)
    ("fig4_02_account_class.png", 5, fitz.Rect(50, 95, 420, 340)),
    # Fig 4.3: UML Class Diagram Account (Page 10, index 9)
    ("fig4_03_uml_account.png", 9, fitz.Rect(60, 220, 410, 400)),
    # Fig 4.4: Conceptual view of Account object (Page 13, index 12)
    ("fig4_04_conceptual_object.png", 12, fitz.Rect(60, 90, 410, 230)),
    # Fig 4.5 Part 1: AccountTest with properties (Page 13, index 12)
    ("fig4_05_accounttest_properties_p1.png", 12, fitz.Rect(50, 460, 420, 610)),
    # Fig 4.5 Part 2: AccountTest with properties (Page 14, index 13)
    ("fig4_05_accounttest_properties_p2.png", 13, fitz.Rect(50, 90, 420, 400)),
    # Fig 4.6: Account.cs with property (Page 15, index 14)
    ("fig4_06_account_properties.png", 14, fitz.Rect(50, 360, 420, 620)),
    # Fig 4.7: UML Class Diagram Account with Property (Page 17, index 16)
    ("fig4_07_uml_properties.png", 16, fitz.Rect(60, 150, 410, 290)),
    # Fig 4.8: Account.cs with constructor (Page 18, index 17)
    ("fig4_08_account_constructor.png", 17, fitz.Rect(50, 325, 420, 505)),
    # Fig 4.9 Part 1: AccountTest with constructor (Page 19, index 18)
    ("fig4_09_accounttest_constructor_p1.png", 18, fitz.Rect(50, 520, 420, 620)),
    # Fig 4.9 Part 2: AccountTest with constructor (Page 20, index 19)
    ("fig4_09_accounttest_constructor_p2.png", 19, fitz.Rect(50, 90, 420, 430)),
    # Fig 4.10: UML Class Diagram with constructor (Page 21, index 20)
    ("fig4_10_uml_constructor.png", 20, fitz.Rect(60, 110, 410, 260)),
    # Fig 4.11: Account.cs with Balance & validation (Page 21-22, index 20 & 21)
    ("fig4_11_account_balance_p1.png", 20, fitz.Rect(50, 580, 420, 625)),
    ("fig4_11_account_balance_p2.png", 21, fitz.Rect(50, 90, 420, 540)),
    # Fig 4.12: AccountTest.cs monetary (Page 24-25, index 23 & 24)
    ("fig4_12_accounttest_balance_p1.png", 23, fitz.Rect(50, 300, 420, 630)),
    ("fig4_12_accounttest_balance_p2.png", 24, fitz.Rect(50, 90, 420, 610)),
    # Fig 4.13: string format specifiers table (Page 26, index 25)
    ("fig4_13_format_specifiers.png", 25, fitz.Rect(50, 100, 420, 400)),
    # Fig 4.14: UML Class Diagram with Balance (Page 27, index 26)
    ("fig4_14_uml_balance.png", 26, fitz.Rect(60, 380, 410, 630)),
]

zoom = 3.0  # 3x scale for crisp rendering
mat = fitz.Matrix(zoom, zoom)

for filename, p_idx, rect in fig_configs:
    page = doc[p_idx]
    pix = page.get_pixmap(matrix=mat, clip=rect)
    out_path = os.path.join(out_dir, filename)
    pix.save(out_path)
    print(f"Saved: {out_path} ({pix.width}x{pix.height})")

print("All figures successfully extracted!")
