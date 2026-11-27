# -*- coding: utf-8 -*-
"""
Generator for:
Lab/Huong-Dan-Thuc-Hanh-Lap-Trinh-CSharp-Buoi-05.docx
BUỔI 5: NỀN TẢNG NGÔN NGỮ LẬP TRÌNH — BIỂU THỨC, TOÁN TỬ, BITWISE & ÉP KIỂU
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>'))

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_table_borders(table, color="CBD5E1", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideV w:val="none"/>'
        f'<w:left w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def format_run(run, font_name="Segoe UI", size_pt=10.0, bold=False, italic=False, color_rgb=(31, 41, 55)):
    run.font.name = font_name
    run.font.size = Pt(size_pt)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = RGBColor(*color_rgb)

def add_p(doc, text="", font_name="Segoe UI", size_pt=10.0, bold=False, italic=False, 
          color_rgb=(31, 41, 55), space_before=0, space_after=4, align=WD_ALIGN_PARAGRAPH.LEFT):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    if text:
        r = p.add_run(text)
        format_run(r, font_name, size_pt, bold, italic, color_rgb)
    return p

def add_heading_1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    format_run(r, "Segoe UI", 13.0, bold=True, color_rgb=(30, 58, 138)) # Primary Navy
    pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="12" w:space="4" w:color="3B82F6"/></w:pBdr>')
    p._p.get_or_add_pPr().append(pBdr)
    return p

def add_heading_2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    format_run(r, "Segoe UI", 11.5, bold=True, color_rgb=(37, 99, 235)) # Royal Blue
    return p

def add_heading_3(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    format_run(r, "Segoe UI", 10.5, bold=True, color_rgb=(8, 145, 178)) # Teal / Cyan
    return p

def add_code_block(doc, code_str, title=None):
    if title:
        tp = doc.add_paragraph()
        tp.paragraph_format.space_before = Pt(6)
        tp.paragraph_format.space_after = Pt(2)
        tp.paragraph_format.keep_with_next = True
        r = tp.add_run(f"💻 Mã nguồn C# minh họa: {title}")
        format_run(r, "Segoe UI", 9.2, bold=True, color_rgb=(15, 23, 42))

    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    
    cell = tbl.cell(0, 0)
    cell.width = Inches(7.0)
    set_cell_background(cell, "F8FAFC")
    set_cell_margins(cell, top=100, bottom=100, left=150, right=150)

    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>'
        f'<w:left w:val="single" w:sz="24" w:space="0" w:color="2563EB"/>'
        f'<w:bottom w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>'
        f'<w:right w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)

    lines = code_str.strip().split("\n")
    for i, line in enumerate(lines):
        p = cell.paragraphs[0] if i == 0 else cell.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.15
        
        stripped = line.strip()
        color = (15, 23, 42)
        italic = False
        bold = False
        
        if stripped.startswith("//") or stripped.startswith("/*") or stripped.startswith("*"):
            color = (100, 116, 139) # Slate comments
            italic = True
        elif stripped.startswith("using ") or stripped.startswith("namespace ") or stripped.startswith("class ") or stripped.startswith("static void Main"):
            color = (147, 51, 234) # Purple
            bold = True
        elif "Console.WriteLine" in line or "Console.Write" in line or "Console.ReadLine" in line:
            color = (37, 99, 235) # Blue
        elif "checked" in line or "try" in line or "catch" in line:
            color = (220, 38, 38) # Red keyword
            bold = True

        r = p.add_run(line)
        format_run(r, "Consolas", 8.8, bold=bold, italic=italic, color_rgb=color)

    post_p = doc.add_paragraph()
    post_p.paragraph_format.space_before = Pt(0)
    post_p.paragraph_format.space_after = Pt(3)

def add_callout(doc, text, title="LƯU Ý CỐT LÕI TỪ GIẢNG VIÊN", callout_type="info"):
    colors = {
        "info": {"bg": "EFF6FF", "border": "2563EB", "title": (30, 58, 138), "icon": "💡"},
        "warning": {"bg": "FEF2F2", "border": "DC2626", "title": (153, 27, 27), "icon": "⚠️"},
        "success": {"bg": "F0FDF4", "border": "16A34A", "title": (22, 101, 52), "icon": "✅"},
        "tip": {"bg": "FAF5FF", "border": "9333EA", "title": (107, 33, 168), "icon": "🎯"}
    }
    cfg = colors.get(callout_type, colors["info"])

    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False

    cell = tbl.cell(0, 0)
    cell.width = Inches(7.0)
    set_cell_background(cell, cfg["bg"])
    set_cell_margins(cell, top=100, bottom=100, left=140, right=140)

    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="none"/>'
        f'<w:left w:val="single" w:sz="24" w:space="0" w:color="{cfg["border"]}"/>'
        f'<w:bottom w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)

    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    r_icon = p.add_run(f"{cfg['icon']} {title}\n")
    format_run(r_icon, "Segoe UI", 9.2, bold=True, color_rgb=cfg["title"])

    r_text = p.add_run(text)
    format_run(r_text, "Segoe UI", 9.0, color_rgb=(31, 41, 55))

    post_p = doc.add_paragraph()
    post_p.paragraph_format.space_before = Pt(0)
    post_p.paragraph_format.space_after = Pt(3)

def add_table_custom(doc, headers, rows_data, col_widths=None):
    tbl = doc.add_table(rows=len(rows_data) + 1, cols=len(headers))
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    set_table_borders(tbl, color="CBD5E1", sz="4")

    # Header Row
    hdr_cells = tbl.rows[0].cells
    for i, h_text in enumerate(headers):
        hdr_cells[i].text = h_text
        set_cell_background(hdr_cells[i], "1E3A8A")
        set_cell_margins(hdr_cells[i], top=90, bottom=90, left=110, right=110)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            format_run(r, "Segoe UI", 9.0, bold=True, color_rgb=(255, 255, 255))

    # Data Rows
    for r_idx, row in enumerate(rows_data):
        row_cells = tbl.rows[r_idx + 1].cells
        bg = "F8FAFC" if (r_idx % 2 == 1) else "FFFFFF"
        for c_idx, val in enumerate(row):
            row_cells[c_idx].text = str(val)
            set_cell_background(row_cells[c_idx], bg)
            set_cell_margins(row_cells[c_idx], top=70, bottom=70, left=110, right=110)
            p = row_cells[c_idx].paragraphs[0]
            if c_idx == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            for r in p.runs:
                format_run(r, "Segoe UI", 8.8, color_rgb=(31, 41, 55))

    if col_widths:
        for row in tbl.rows:
            for c_idx, w in enumerate(col_widths):
                row.cells[c_idx].width = Inches(w)

    post_p = doc.add_paragraph()
    post_p.paragraph_format.space_before = Pt(0)
    post_p.paragraph_format.space_after = Pt(3)

print("Framework initialized successfully.")
