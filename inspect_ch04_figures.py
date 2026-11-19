import fitz
import os

doc = fitz.open('textbook_CShape/Chapter_04.pdf')
out_dir = 'Slides_CShape/images'
os.makedirs(out_dir, exist_ok=True)

print("Scanning Chapter 4 PDF for figures...")

# We can find text blocks and figure lines
figures = [
    ("fig4_01_accounttest_app", 3, "Fig. 4.1"),
    ("fig4_02_account_class", 6, "Fig. 4.2"),
    ("fig4_03_uml_account", 10, "Fig. 4.3"),
    ("fig4_04_conceptual_object", 13, "Fig. 4.4"),
    ("fig4_05_accounttest_properties", 13, "Fig. 4.5"),
    ("fig4_06_account_properties", 15, "Fig. 4.6"),
    ("fig4_07_uml_properties", 17, "Fig. 4.7"),
    ("fig4_08_account_constructor", 18, "Fig. 4.8"),
    ("fig4_09_accounttest_constructor", 19, "Fig. 4.9"),
    ("fig4_10_uml_constructor", 21, "Fig. 4.10"),
    ("fig4_11_account_balance", 21, "Fig. 4.11"),
    ("fig4_12_accounttest_balance", 24, "Fig. 4.12"),
    ("fig4_13_format_specifiers", 26, "Fig. 4.13"),
    ("fig4_14_uml_balance", 27, "Fig. 4.14"),
]

for name, page_1based, fig_tag in figures:
    p_idx = page_1based - 1
    page = doc[p_idx]
    # Find instances of fig_tag
    rects = page.search_for(fig_tag)
    print(f"Page {page_1based} ({fig_tag}): found {len(rects)} search hits")
    for r in rects:
        print(f"   Hit at: {r}")
