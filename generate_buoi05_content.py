# -*- coding: utf-8 -*-
"""
Full Content Builder for:
Lab/Huong-Dan-Thuc-Hanh-Lap-Trinh-CSharp-Buoi-05.docx
BUỔI 5: NỀN TẢNG NGÔN NGỮ LẬP TRÌNH — BIỂU THỨC, TOÁN TỬ, BITWISE & ÉP KIỂU
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

from build_lab05_docx import (
    set_cell_background, set_cell_margins, set_table_borders,
    format_run, add_p, add_heading_1, add_heading_2, add_heading_3,
    add_code_block, add_callout, add_table_custom
)

def build_document():
    doc = docx.Document()

    # Configure Margins
    for s in doc.sections:
        s.top_margin = Inches(0.75)
        s.bottom_margin = Inches(0.75)
        s.left_margin = Inches(0.75)
        s.right_margin = Inches(0.75)

        # Header
        header = s.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("KỸ THUẬT LẬP TRÌNH C# (.NET 8) — TÀI LIỆU THỰC HÀNH BUỔI 05")
        format_run(hrun, "Segoe UI", 8.5, color_rgb=(148, 163, 184))

        # Footer
        footer = s.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.LEFT
        frun1 = fp.add_run("Khoa CNTT - Đại học Đông Á | Lớp IT26M Khóa 2026")
        format_run(frun1, "Segoe UI", 8.5, color_rgb=(148, 163, 184))

    # =========================================================================
    # COVER / HEADER BLOCK
    # =========================================================================
    p_inst = add_p(doc, "TRƯỜNG ĐẠI HỌC ĐÔNG Á — KHOA CÔNG NGHỆ THÔNG TIN", "Segoe UI", 10.0, bold=True, color_rgb=(30, 58, 138), align=WD_ALIGN_PARAGRAPH.CENTER)
    p_inst.paragraph_format.space_after = Pt(2)
    
    p_sub = add_p(doc, "BỘ MÔN KỸ THUẬT PHẦN MỀM & HỆ THỐNG THÔNG TIN", "Segoe UI", 9.0, italic=True, color_rgb=(100, 116, 139), align=WD_ALIGN_PARAGRAPH.CENTER)
    p_sub.paragraph_format.space_after = Pt(12)

    p_title = add_p(doc, "TÀI LIỆU HƯỚNG DẪN THỰC HÀNH VÀ BÀI TẬP LẬP TRÌNH C# CHUẨN MỰC", "Segoe UI", 16.0, bold=True, color_rgb=(30, 58, 138), align=WD_ALIGN_PARAGRAPH.CENTER)
    p_title.paragraph_format.space_after = Pt(4)

    p_sess = add_p(doc, "BUỔI 5: NỀN TẢNG NGÔN NGỮ LẬP TRÌNH — BIỂU THỨC, TOÁN TỬ, BITWISE & ÉP KIỂU", "Segoe UI", 12.5, bold=True, color_rgb=(37, 99, 235), align=WD_ALIGN_PARAGRAPH.CENTER)
    p_sess.paragraph_format.space_after = Pt(6)

    p_meta = add_p(doc, "Học phần: Kỹ thuật Lập trình (4 Tín chỉ: 3 LT + 1 TH/Đồ án) | Môi trường: Visual Studio 2022 / .NET 8.0 SDK\nĐối tượng: Sinh viên Lớp IT26M & Khóa 2026 | Thời lượng thực hành: 3 Tiết (150 Phút Tích hợp)", "Segoe UI", 9.2, italic=True, color_rgb=(75, 85, 99), align=WD_ALIGN_PARAGRAPH.CENTER)
    p_meta.paragraph_format.space_after = Pt(14)

    add_callout(doc, 
        "Tài liệu này được biên soạn bám sát theo đề cương chi tiết học phần Kỹ thuật Lập trình và chuẩn đầu ra ABET/AUN-QA. "
        "Mỗi phần kiến thức được cấu trúc chặt chẽ theo mô hình sư phạm 3 bước:\n"
        "1. Bài thực hành có lời giải chi tiết (Guided Practice): Phân tích giải thuật, mã nguồn chuẩn C#, giải thích dòng lệnh và kết quả chạy mẫu.\n"
        "2. Bài thực hành tương tự (In-class Drills): Sinh viên tự tay code tại phòng lab theo gợi ý và kiểm thử qua bảng Test Cases.\n"
        "3. Bài tập tự luyện / Về nhà (Homework Projects): Các bài toán thực tế nâng cao giúp sinh viên rèn luyện tư duy kỹ thuật phần mềm.",
        "MÔ HÌNH SƯ PHẠM VÀ PHƯƠNG PHÁP HỌC TẬP THỰC CHIẾN", "info")

    # Bảng Chuẩn đầu ra (CLOs)
    add_heading_2(doc, "Hệ Thống Chuẩn Đầu Ra Buổi 5 (Course Learning Outcomes - CLOs)")
    clo_headers = ["Mã CLO", "Mô tả chuẩn đầu ra kỳ vọng (Theo thang đo Bloom)", "Mức độ Bloom"]
    clo_rows = [
        ["CLO 5.1", "Giải thích bản chất biểu thức (Expressions), toán tử, toán hạng; chuyển đổi chuẩn xác các công thức toán - lý - tài chính sang biểu thức C# hợp lệ.", "Mức 2 & 3 (Hiểu & Áp dụng)"],
        ["CLO 5.2", "Vận dụng thành thạo và phân biệt chính xác phép chia nguyên vs chia thực, toán tử modulo %, cạm bẫy toán tử tăng/giảm (++x vs x++) và mô hình ô nhớ RAM.", "Mức 3 (Áp dụng)"],
        ["CLO 5.3", "Làm chủ toán tử logic đoản mạch (&&, ||) để bảo vệ chương trình chống lỗi runtime (chia cho 0, null reference) và xử lý sai số số thực IEEE 754 an toàn.", "Mức 3 & 4 (Áp dụng & Phân tích)"],
        ["CLO 5.4", "Làm chủ các phép toán Thao tác Bit (Bitwise: AND, OR, XOR, NOT, Shift), hiểu hệ mã bù 2 và ứng dụng vào thuật toán tối ưu, kỹ thuật mặt nạ bit (Bitmasking).", "Mức 3 & 4 (Áp dụng & Phân tích)"],
        ["CLO 5.5", "Phân tích và thực hiện chuẩn xác các cơ chế chuyển đổi kiểu dữ liệu (Implicit, Explicit Cast, Convert, TryParse); thiết lập khối checked bảo vệ chống tràn số.", "Mức 4 (Phân tích & Đánh giá)"]
    ]
    add_table_custom(doc, clo_headers, clo_rows, [1.0, 4.8, 1.2])

    # Bảng phân bổ thời gian thực hành
    add_heading_2(doc, "Bảng Phân Bổ Thời Lượng Thực Hành Phòng Lab (3 Tiết - 150 Phút)")
    timeline_headers = ["Tiết học", "Thời lượng", "Nội dung trọng tâm", "Sản phẩm đầu ra tại phòng máy"]
    timeline_rows = [
        ["Tiết 1", "50 phút", "Biểu thức, Toán tử Số học, So sánh, Logic đoản mạch & Cạm bẫy Tăng/Giảm (++x vs x++)", "Hoàn thành Bài 1.1, 1.2, 1.3 và vẽ bảng Trace biến thiên ô nhớ Bài 2.1, 2.2."],
        ["Tiết 2", "50 phút", "Thế giới nhị phân & Thao tác Bit (Bitwise: &, |, ^, ~, <<, >>), Bitmasking phân quyền", "Hoàn thành Bài 3.1 (Bit Hacks) và Module phân quyền tệp tin Bài 3.2, 3.3."],
        ["Tiết 3", "50 phút", "Ép kiểu dữ liệu, Module nhập liệu TryParse, Khối checked chống tràn số & Mini-Challenge", "Hoàn thành Module nhập liệu an toàn 4.1, 4.2 và nộp bài Mini-Challenge 5.1."]
    ]
    add_table_custom(doc, timeline_headers, timeline_rows, [0.8, 0.9, 3.5, 1.8])

    # =========================================================================
    # PHẦN I: BIỂU THỨC, TOÁN TỬ SỐ HỌC, SO SÁNH & CƠ CHẾ ĐOẢN MẠCH
    # =========================================================================
    add_heading_1(doc, "PHẦN I: BIỂU THỨC, TOÁN TỬ SỐ HỌC, SO SÁNH & LOGIC ĐOẢN MẠCH")
    
    add_p(doc, 
        "Biểu thức (Expression) là sự kết hợp có quy tắc cú pháp giữa các Toán hạng (Operands - biến, hằng số, lời gọi hàm) "
        "và Toán tử (Operators - +, -, *, /, %, ==, &&, ||...) nhằm tính toán và trả về MỘT giá trị duy nhất thuộc MỘT kiểu dữ liệu tĩnh xác định. "
        "Trong C#, mọi biểu thức đều được trình biên dịch kiểm tra kiểu nghiêm ngặt (Strict Type Safety).", "Segoe UI", 10.0)

    add_callout(doc,
        "1. Cạm bẫy chia nguyên: Trong C#, nếu cả 2 toán hạng của phép chia / đều là số nguyên (int), CPU sẽ thực hiện phép chia nguyên và vứt bỏ phần thập phân! "
        "Ví dụ: 5 / 2 = 2 (chứ không phải 2.5). Để chia ra số thực, bắt buộc ít nhất một toán hạng phải là số thực: 5.0 / 2 hoặc (double)5 / 2.\n"
        "2. Bẫy tử huyệt '=' và '==': Dấu '=' là toán tử gán (ghi đè ô nhớ), còn '==' là toán tử so sánh bằng (trả về bool).\n"
        "3. Sai số dấu phẩy động IEEE 754: 0.1 + 0.2 == 0.3 trả về false! Với số thực, luôn so sánh khoảng cách chênh lệch tuyệt đối: Math.Abs(a - b) < 1e-9.\n"
        "4. Cơ chế đoản mạch (Short-Circuit): Với '&&', nếu vế trái là false thì vế phải KHÔNG BAO GIỜ được tính! Với '||', nếu vế trái là true thì vế phải KHÔNG được tính. "
        "Ứng dụng cốt tử: if (b != 0 && (10 / b > 1)) ngăn chặn hoàn toàn lỗi DivideByZeroException!",
        "4 QUY TẮC SỐNG CÒN KHI LẬP TRÌNH BIỂU THỨC C#", "warning")

    # Bài 1.1
    add_heading_2(doc, "1. Bài Thực Hành Có Lời Giải 1.1: Tính Toán Hình Học & Đầu Tư Lãi Kép Lũy Tiến")
    add_p(doc, 
        "Mục tiêu: Rèn luyện kỹ năng chuyển đổi công thức toán học - tài chính phức tạp sang C#, sử dụng đúng kiểu double, "
        "áp dụng hàm thư viện Math.Sqrt(), Math.Pow() và định dạng hiển thị tiền tệ chuẩn xác.", "Segoe UI", 9.8, italic=True)
    
    add_p(doc, 
        "Đề bài: Viết chương trình Console cho phép:\n"
        "a) Nhập độ dài 3 cạnh tam giác a, b, c. Kiểm tra tính hợp lệ của tam giác. Nếu hợp lệ, tính chu vi và diện tích theo công thức Heron: "
        "S = sqrt(p * (p - a) * (p - b) * (p - c)) với p là nửa chu vi.\n"
        "b) Nhập số vốn gửi ngân hàng P, lãi suất năm r (%) và kỳ hạn t (năm). Tính số tiền nhận được cả gốc lẫn lãi theo công thức lãi kép lũy tiến: "
        "A = P * (1 + r / 100)^t.", "Segoe UI", 9.8)

    add_code_block(doc, 
"""using System;
using System.Globalization;

namespace Buoi05_BaiThucHanh1_1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            Console.WriteLine("=== CHƯƠNG TRÌNH TÍNH TOÁN HÌNH HỌC & LÃI KÉP NGÂN HÀNG ===");

            // --- PHẦN A: TÍNH DIỆN TÍCH TAM GIÁC THEO CÔNG THỨC HERON ---
            Console.WriteLine("\\n--- [A] TÍNH DIỆN TÍCH TAM GIÁC (HERON) ---");
            Console.Write("Nhập độ dài cạnh a: ");
            double a = double.Parse(Console.ReadLine());
            Console.Write("Nhập độ dài cạnh b: ");
            double b = double.Parse(Console.ReadLine());
            Console.Write("Nhập độ dài cạnh c: ");
            double c = double.Parse(Console.ReadLine());

            // Kiểm tra điều kiện tồn tại tam giác bằng toán tử so sánh & logic
            if (a > 0 && b > 0 && c > 0 && (a + b > c) && (b + c > a) && (a + c > b))
            {
                double chuVi = a + b + c;
                double p = chuVi / 2.0; // Phép chia thực an toàn với 2.0
                double dienTich = Math.Sqrt(p * (p - a) * (p - b) * (p - c));

                Console.WriteLine($"-> Chu vi tam giác: {chuVi:F2}");
                Console.WriteLine($"-> Nửa chu vi p: {p:F2}");
                Console.WriteLine($"-> Diện tích tam giác (Heron): {dienTich:F4}");
            }
            else
            {
                Console.WriteLine("-> LỖI: Ba số vừa nhập không thể tạo thành một tam giác hợp lệ!");
            }

            // --- PHẦN B: TÍNH LÃI KÉP NGÂN HÀNG (COMPOUND INTEREST) ---
            Console.WriteLine("\\n--- [B] TÍNH LÃI KÉP NGÂN HÀNG ---");
            Console.Write("Nhập số tiền gửi ban đầu (VNĐ): ");
            double P = double.Parse(Console.ReadLine());
            Console.Write("Nhập lãi suất hàng năm (%/năm, ví dụ 7.5): ");
            double r = double.Parse(Console.ReadLine());
            Console.Write("Nhập kỳ hạn gửi (năm): ");
            int t = int.Parse(Console.ReadLine());

            // Công thức: A = P * (1 + r/100)^t
            // Lưu ý: Trong C# KHÔNG có toán tử mũ ^. Dấu ^ là XOR bit! Phải dùng Math.Pow()
            double tiLeLai = r / 100.0;
            double tongTien = P * Math.Pow(1.0 + tiLeLai, t);
            double tienLai = tongTien - P;

            CultureInfo cul = CultureInfo.GetCultureInfo("vi-VN");
            Console.WriteLine($"-> Số tiền gốc: {P.ToString("#,###", cul)} VNĐ");
            Console.WriteLine($"-> Tổng số tiền nhận được sau {t} năm: {tongTien.ToString("#,###", cul)} VNĐ");
            Console.WriteLine($"-> Tiền lãi thực nhận: {tienLai.ToString("#,###", cul)} VNĐ");
        }
    }
}""", "BaiThucHanh1_1_Heron_LaiKep.cs")

    add_p(doc, 
        "Phân tích chuyên sâu & Cạm bẫy kỹ thuật:\n"
        "• Tại dòng tính nửa chu vi: Viết p = chuVi / 2.0; để bảo đảm phép chia thực. Nếu vô tình khai báo chuVi là int và chia cho 2, phần thập phân sẽ bị mất hoàn toàn.\n"
        "• Tại dòng tính lãi kép: Tuyệt đối không viết P * (1 + r / 100) ^ t! Ký hiệu ^ trong C# là toán tử XOR thao tác trên bit nhị phân, sẽ dẫn đến kết quả sai hoàn toàn hoặc lỗi biên dịch. Bắt buộc phải gọi hàm Math.Pow(1.0 + tiLeLai, t).\n"
        "• Định dạng tiền tệ vi-VN: Sử dụng CultureInfo.GetCultureInfo(\"vi-VN\") giúp phân cách phần nghìn bằng dấu chấm chuẩn mực của ngân hàng Việt Nam.", "Segoe UI", 9.2)

    # Bài 1.2
    add_heading_2(doc, "2. Bài Thực Hành Có Lời Giải 1.2: Thẩm Định Học Bổng & Đoản Mạch Chống Lỗi Chia Cho 0")
    add_p(doc, 
        "Mục tiêu: Minh chứng trực quan sự khác biệt sống còn giữa toán tử logic đoản mạch (Short-Circuit: &&, ||) "
        "và toán tử logic không đoản mạch (&, |), phòng chống sập chương trình (Crash Protection).", "Segoe UI", 9.8, italic=True)

    add_code_block(doc, 
"""using System;

namespace Buoi05_BaiThucHanh1_2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            Console.WriteLine("=== THẨM ĐỊNH HỌC BỔNG & THỬ NGHIỆM ĐOẢN MẠCH ===");

            Console.Write("Nhập điểm GPA tích lũy (thang điểm 4.0): ");
            double gpa = double.Parse(Console.ReadLine());
            Console.Write("Nhập điểm rèn luyện (thang điểm 100): ");
            int drl = int.Parse(Console.ReadLine());
            Console.Write("Nhập số môn thi lại / trượt: ");
            int soMonTruot = int.Parse(Console.ReadLine());

            // Biểu thức xét học bổng: GPA >= 3.6 VÀ DRL >= 85 VÀ Không có môn trượt
            bool duDieuKien = (gpa >= 3.6) && (drl >= 85) && (soMonTruot == 0);

            Console.WriteLine($"-> Kết quả xét duyệt học bổng xuất sắc: {(duDieuKien ? "ĐƯỢC DUYỆT" : "KHÔNG ĐẠT")}");

            // --- THỬ NGHIỆM ĐOẢN MẠCH PHÒNG VỆ CHIA CHO 0 ---
            Console.WriteLine("\\n--- KIỂM TRA ĐOẢN MẠCH TRÁNH LỖI DIVIDEBYZERO ---");
            Console.Write("Nhập số lượng thành viên nhóm dự án (n): ");
            int n = int.Parse(Console.ReadLine());
            int tongQuy = 1000000;

            // Kỹ thuật đoản mạch an toàn: Nếu n == 0, vế trái (n > 0) trả về false.
            // Nhờ toán tử &&, CPU dừng ngay và KHÔNG THỰC THI (tongQuy / n > 200000)
            if (n > 0 && (tongQuy / n >= 200000))
            {
                Console.WriteLine($"-> Hợp lệ: Mỗi thành viên nhận {tongQuy / n:N0} VNĐ (Đủ định mức).");
            }
            else
            {
                Console.WriteLine("-> Không hợp lệ hoặc nhóm chưa có thành viên (Bảo vệ an toàn, không sập chương trình).");
            }
        }
    }
}""", "BaiThucHanh1_2_DoanMach.cs")

    # Bài 1.3 - Tương tự
    add_heading_2(doc, "3. Bài Thực Hành Tương Tự 1.3: Tính Cước Vận Tải Hàng Không (Air Cargo Billing)")
    add_p(doc, 
        "Đề bài: Trong ngành hàng không, cước vận chuyển được tính dựa trên Trọng lượng tính cước (Chargeable Weight) "
        "là giá trị lớn nhất giữa Trọng lượng thực tế (Gross Weight - kg) và Trọng lượng thể tích (Dimensional Weight - kg). "
        "Công thức: Dimensional Weight = (Dài * Rộng * Cao) / 5000 (các kích thước tính bằng cm).\n"
        "Giá cước quy định:\n"
        "• Dưới 10 kg: 55,000 VNĐ / kg.\n"
        "• Từ 10 kg đến dưới 50 kg: 45,000 VNĐ / kg.\n"
        "• Từ 50 kg trở lên: 35,000 VNĐ / kg.\n"
        "Nếu là hàng nguy hiểm (hóa chất, pin lithium: isHazardous = true), phụ phí bảo hiểm là 20% trên tổng cước. "
        "Hãy viết chương trình C# tính tổng tiền cước thanh toán.", "Segoe UI", 9.8)

    add_p(doc, 
        "Gợi ý thuật toán & Khung code:\n"
        "1. Khai báo các biến: double dai, rong, cao, weightGross;\n"
        "2. Tính: double weightVol = (dai * rong * cao) / 5000.0;\n"
        "3. Tính trọng lượng tính cước: double chargeableWeight = Math.Max(weightGross, weightVol);\n"
        "4. Dùng cấu trúc if...else if để xác định đơn giá; tính phụ phí nếu cờ isHazardous == true.", "Segoe UI", 9.2, italic=True)

    add_heading_3(doc, "Bảng Test Cases Kiểm Thử Bài 1.3:")
    tc_1_3_headers = ["Test Case", "Dài x Rộng x Cao (cm)", "Trọng lượng thực (kg)", "Hàng nguy hiểm?", "Kết quả kỳ vọng (VNĐ)"]
    tc_1_3_rows = [
        ["TC 01", "30 x 20 x 10", "4.0", "False", "Chargeable: 4.0 kg -> 220,000 VNĐ"],
        ["TC 02", "50 x 50 x 50", "15.0", "False", "Chargeable: 25.0 kg -> 1,125,000 VNĐ"],
        ["TC 03", "40 x 30 x 20", "8.0", "True", "Chargeable: 9.6 kg -> 633,600 VNĐ (gồm 20% phụ phí)"],
        ["TC 04", "80 x 60 x 50", "60.0", "True", "Chargeable: 60.0 kg -> 2,520,000 VNĐ"]
    ]
    add_table_custom(doc, tc_1_3_headers, tc_1_3_rows, [0.8, 1.8, 1.5, 1.2, 1.7])

    # Bài 1.4 - Về nhà
    add_heading_2(doc, "4. Bài Tập Tự Luyện Về Nhà 1.4: Giải Hệ Phương Trình Bậc Nhất 2 Ẩn (Định Thức Cramer)")
    add_p(doc, 
        "Đề bài: Viết chương trình C# giải và biện luận hệ phương trình bậc nhất hai ẩn số:\n"
        "   a1*x + b1*y = c1\n"
        "   a2*x + b2*y = c2\n"
        "Sử dụng phương pháp định thức Cramer:\n"
        "• D = a1 * b2 - a2 * b1\n"
        "• Dx = c1 * b2 - c2 * b1\n"
        "• Dy = a1 * c2 - a2 * c1\n"
        "Yêu cầu xử lý an toàn số thực: Do sai số dấu phẩy động, kiểm tra D == 0 bằng Math.Abs(D) < 1e-9.\n"
        "• Nếu |D| >= 1e-9: Hệ có nghiệm duy nhất x = Dx / D, y = Dy / D.\n"
        "• Nếu |D| < 1e-9: Kiểm tra |Dx| < 1e-9 và |Dy| < 1e-9: Nếu đúng -> Hệ có vô số nghiệm; Ngược lại -> Hệ vô nghiệm.", "Segoe UI", 9.8)

    # =========================================================================
    # PHẦN II: TOÁN TỬ TĂNG/GIẢM (++ / --) & MÔ HÌNH Ô NHỚ RAM
    # =========================================================================
    add_heading_1(doc, "PHẦN II: TOÁN TỬ TĂNG/GIẢM (++ / --) & MÔ HÌNH Ô NHỚ RAM")

    add_p(doc, 
        "Toán tử tăng (++) và giảm (--) là hai toán tử một ngôi (Unary) phổ biến nhất nhưng cũng là nguồn gốc gây nhầm lẫn "
        "lớn nhất cho người mới bắt đầu lập trình. Sự khác biệt cốt lõi nằm ở THỜI ĐIỂM cập nhật giá trị vào ô nhớ RAM:\n"
        "• Tiền tố (++x, --x): Tăng hoặc giảm giá trị biến trong ô nhớ TRƯỚC, sau đó trả về giá trị MỚI để tham gia vào biểu thức.\n"
        "• Hậu tố (x++, x--): Lấy giá trị HIỆN TẠI (cũ) của biến để tham gia tính toán biểu thức TRƯỚC, sau đó mới tăng giá trị trong ô nhớ lên 1 đơn vị.", "Segoe UI", 10.0)

    # Bài 2.1
    add_heading_2(doc, "1. Bài Thực Hành Có Lời Giải 2.1: Truy Vết Ô Nhớ Trong Hệ Thống Cấp Số Vé Tự Động")
    add_p(doc, 
        "Mục tiêu: Mổ xẻ từng chu kỳ vi xử lý, vẽ bảng Trace ô nhớ RAM để hiểu cặn kẽ hành vi của x++ và ++x.", "Segoe UI", 9.8, italic=True)

    add_code_block(doc, 
"""using System;

namespace Buoi05_BaiThucHanh2_1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            Console.WriteLine("=== GIẢI MÃ CƠ CHẾ Ô NHỚ RAM VỚI TOÁN TỬ TĂNG / GIẢM ===");

            int ticketCounter = 100;
            Console.WriteLine($"[Ban đầu] Ô nhớ ticketCounter = {ticketCounter}");

            // Trường hợp 1: Hậu tố ticketCounter++
            // 1. Trả về giá trị hiện tại (100) gán cho currentCustomer
            // 2. Ô nhớ ticketCounter tăng lên 101
            int currentCustomer = ticketCounter++;
            Console.WriteLine($"[Sau ticketCounter++] Khách nhận vé: {currentCustomer} | Ô nhớ hiện tại: {ticketCounter}");

            // Trường hợp 2: Tiền tố ++ticketCounter
            // 1. Ô nhớ ticketCounter tăng từ 101 lên 102
            // 2. Trả về giá trị mới (102) gán cho vipCustomer
            int vipCustomer = ++ticketCounter;
            Console.WriteLine($"[Sau ++ticketCounter] Khách VIP nhận vé: {vipCustomer} | Ô nhớ hiện tại: {ticketCounter}");

            // Thử thách bẫy phức hợp
            int a = 5;
            int b = 10;
            // Giải phẫu: ++a tăng a lên 6, trả về 6
            // b++ lấy giá trị cũ là 10 ra nhân với 2 thành 20, sau đó b mới tăng lên 11
            // c = 6 + 20 = 26
            int c = ++a + b++ * 2;
            Console.WriteLine($"\\n[Mổ xẻ biểu thức c = ++a + b++ * 2]");
            Console.WriteLine($"-> Giá trị a = {a} (kỳ vọng: 6)");
            Console.WriteLine($"-> Giá trị b = {b} (kỳ vọng: 11)");
            Console.WriteLine($"-> Giá trị c = {c} (kỳ vọng: 26)");
        }
    }
}""", "BaiThucHanh2_1_MemoryTrace.cs")

    add_heading_3(doc, "Bảng Biến Thiên Ô Nhớ RAM (Trace Table) Của Biểu Thức: c = ++a + b++ * 2")
    trace_headers = ["Bước", "Toán tử / Thao tác", "Ô nhớ a", "Ô nhớ b", "Giá trị tạm thời vế phải", "Ô nhớ c"]
    trace_rows = [
        ["0", "Khởi tạo ban đầu", "5", "10", "Chưa có", "Chưa có"],
        ["1", "Thực hiện tiền tố ++a", "6", "10", "a tăng lên 6, trả về giá trị 6", "Chưa có"],
        ["2", "Thực hiện hậu tố b++", "6", "11 (sau khi lấy)", "Lấy 10 để tính toán, sau đó b lên 11", "Chưa có"],
        ["3", "Thực hiện nhân: 10 * 2", "6", "11", "Kết quả phép nhân = 20", "Chưa có"],
        ["4", "Thực hiện cộng: 6 + 20", "6", "11", "Kết quả phép cộng = 26", "26 (được ghi đè)"]
    ]
    add_table_custom(doc, trace_headers, trace_rows, [0.6, 2.0, 0.8, 1.2, 1.6, 0.8])

    # Bài 2.2 - Tương tự
    add_heading_2(doc, "2. Bài Thực Hành Tương Tự 2.2: Hệ Thống Xử Phạt Vi Phạm Giao Thông & Bảng Trace")
    add_p(doc, 
        "Đề bài: Cho đoạn mã nguồn C# sau:\n"
        "   int x = 4, y = 7;\n"
        "   int diemPhat = x++ * 3 - --y + ++x * 2;\n"
        "Yêu cầu:\n"
        "1. Hãy dựng Bảng biến thiên ô nhớ RAM từng bước để dự đoán giá trị cuối cùng của x, y và diemPhat.\n"
        "2. Viết chương trình C# để kiểm chứng kết quả dự đoán của em.\n"
        "3. Rút ra bài học vì sao trong thực tế kỹ thuật phần mềm, ta KHÔNG NÊN viết biểu thức lạm dụng tăng giảm trên cùng một biến.", "Segoe UI", 9.8)

    # Bài 2.3 - Về nhà
    add_heading_2(doc, "3. Bài Tập Tự Luyện Về Nhà 2.3: Bộ Thử Thách 5 Câu Đố Ô Nhớ (C# Memory Puzzles)")
    add_p(doc, 
        "Hãy xác định giá trị in ra màn hình của 5 đoạn mã sau mà không cần chạy máy tính, sau đó viết code C# kiểm chứng:\n"
        "Câu 1: int a = 1; a = a++; Console.WriteLine(a);  (Gợi ý: Cực kỳ cẩn thận với hành vi gán lại cho chính nó!)\n"
        "Câu 2: int x = 3; int y = ++x + ++x; Console.WriteLine($\"{x}, {y}\");\n"
        "Câu 3: int m = 10; int n = m-- - --m; Console.WriteLine($\"{m}, {n}\");\n"
        "Câu 4: int p = 5; bool res = (p++ > 5) && (++p > 6); Console.WriteLine($\"{p}, {res}\"); (Gợi ý: Đoản mạch!)\n"
        "Câu 5: int q = 2; int ans = q++ + q++ * q++; Console.WriteLine($\"{q}, {ans}\");", "Segoe UI", 9.8)

    # =========================================================================
    # PHẦN III: THẾ GIỚI NHỊ PHÂN & CÁC PHÉP TOÁN THAO TÁC BIT (BITWISE)
    # =========================================================================
    add_heading_1(doc, "PHẦN III: THẾ GIỚI NHỊ PHÂN & CÁC PHÉP TOÁN THAO TÁC BIT (BITWISE)")

    add_p(doc, 
        "Để trở thành một kỹ sư phần mềm thực thụ, sinh viên không thể chỉ nhìn máy tính ở tầng trừu tượng bề nổi mà phải "
        "hiểu sâu kiến trúc phần cứng! Mọi dữ liệu (số nguyên, số thực, văn bản, hình ảnh) bên dưới thanh ghi CPU và RAM "
        "đều là các dãy bit nhị phân 0 và 1 (đóng/ngắt transistor). Kiểu int trong C# chiếm 4 bytes = 32 bits. "
        "Số nguyên có dấu được biểu diễn bằng hệ Mã Bù 2 (Two's Complement): Muốn lấy số đối -X, ta đảo toàn bộ bit của X rồi cộng thêm 1.", "Segoe UI", 10.0)

    add_callout(doc,
        "1. Toán tử AND bit (&): Chỉ bằng 1 khi CẢ HAI bit cùng bằng 1. Ứng dụng: Lọc bit, kiểm tra bit.\n"
        "2. Toán tử OR bit (|): Bằng 1 khi CÓ ÍT NHẤT MỘT bit bằng 1. Ứng dụng: Bật bit, gộp quyền hạn.\n"
        "3. Toán tử XOR bit (^): Bằng 1 khi HAI BIT KHÁC NHAU. Ứng dụng: Đảo bit, mã hóa đối xứng, hoán vị.\n"
        "4. Toán tử NOT đảo bit (~): Đổi 0 thành 1 và 1 thành 0. Số bù 2: ~x = -(x + 1).\n"
        "5. Dịch trái (<< k): Dịch các bit sang trái k vị trí, chèn số 0 vào đuôi bên phải. Tương đương NHÂN VỚI 2^k siêu tốc!\n"
        "6. Dịch phải (>> k): Dịch các bit sang phải k vị trí. Tương đương CHIA NGUYÊN CHO 2^k siêu tốc!",
        "TỔNG KẾT BẢNG PHÉP TOÁN BITWISE VÀ HIỆU NĂNG TÍNH TOÁN", "tip")

    # Bài 3.1
    add_heading_2(doc, "1. Bài Thực Hành Có Lời Giải 3.1: Bộ Thư Viện Tối Ưu Hóa Vi Xử Lý Bằng Bitwise (Bit Hacks)")
    add_p(doc, 
        "Mục tiêu: Xây dựng 4 hàm thuật toán kinh điển sử dụng bitwise thay cho các phép toán số học nặng nề, "
        "hiểu bản chất thực thi ở mức thanh ghi vi xử lý.", "Segoe UI", 9.8, italic=True)

    add_code_block(doc, 
"""using System;

namespace Buoi05_BaiThucHanh3_1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            Console.WriteLine("=== BỘ THƯ VIỆN TOÁN TỬ BITWISE & BIT HACKS C# ===");

            // 1. KIỂM TRA CHẴN LẺ SIÊU TỐC VỚI PHÉP & 1
            // Bit ngoài cùng bên phải (LSB) của số lẻ luôn là 1, số chẵn luôn là 0
            int n = 42;
            bool isEven = (n & 1) == 0;
            Console.WriteLine($"1. Kiểm tra số {n}: {(isEven ? "SỐ CHẴN" : "SỐ LẺ")} (Bằng n & 1)");

            // 2. NHÂN / CHIA LŨY THỪA 2 BẰNG PHÉP DỊCH BIT << VÀ >>
            int x = 25;
            int nhan8 = x << 3;  // 25 * 2^3 = 25 * 8 = 200
            int chia4 = x >> 2;  // 25 / 2^2 = 25 / 4 = 6
            Console.WriteLine($"2. Nhân chia nhanh số {x}:");
            Console.WriteLine($"   -> {x} << 3 (tương đương {x} * 8) = {nhan8}");
            Console.WriteLine($"   -> {x} >> 2 (tương đương {x} / 4) = {chia4}");

            // 3. HOÁN VỊ HAI BIẾN KHÔNG DÙNG BIẾN TẠM (XOR SWAP ALGORITHM)
            int num1 = 15; // Nhị phân: 0000 1111
            int num2 = 27; // Nhị phân: 0001 1011
            Console.WriteLine($"3. Hoán vị ban đầu: num1 = {num1}, num2 = {num2}");
            num1 = num1 ^ num2; // num1 chứa thông tin khác biệt của cả hai
            num2 = num1 ^ num2; // num2 được giải mã thành giá trị cũ của num1
            num1 = num1 ^ num2; // num1 được giải mã thành giá trị cũ của num2
            Console.WriteLine($"   -> Sau hoán vị XOR: num1 = {num1}, num2 = {num2}");

            // 4. KIỂM TRA MỘT SỐ CÓ PHẢI LÀ LŨY THỪA CỦA 2 KHÔNG
            // Một số là lũy thừa của 2 chỉ có đúng duy nhất 1 bit 1 (vd: 8 = 1000, 16 = 10000).
            // Do đó n & (n - 1) sẽ luôn triệt tiêu bit 1 đó và bằng 0!
            int testNum = 64;
            bool isPowerOfTwo = (testNum > 0) && ((testNum & (testNum - 1)) == 0);
            Console.WriteLine($"4. Số {testNum} có phải lũy thừa của 2 không? -> {isPowerOfTwo}");

            // 5. HIỂN THỊ DẠNG NHỊ PHÂN ĐẦY ĐỦ 8 BIT
            byte b = 45;
            string binaryStr = Convert.ToString(b, 2).PadLeft(8, '0');
            Console.WriteLine($"5. Số {b} trong hệ nhị phân 8-bit: {binaryStr}");
        }
    }
}""", "BaiThucHanh3_1_BitHacks.cs")

    # Bài 3.2
    add_heading_2(doc, "2. Bài Thực Hành Có Lời Giải 3.2: Hệ Thống Phân Quyền Bằng Kỹ Thuật Bitmasking")
    add_p(doc, 
        "Mục tiêu: Áp dụng kỹ thuật Mặt nạ bit (Bitmasking) để quản lý hàng loạt quyền hạn truy cập tệp tin "
        "hoặc tài nguyên hệ thống trong một biến số nguyên duy nhất, tối ưu hóa bộ nhớ và tốc độ truy vấn.", "Segoe UI", 9.8, italic=True)

    add_code_block(doc, 
"""using System;

namespace Buoi05_BaiThucHanh3_2
{
    class Program
    {
        // Định nghĩa các cờ quyền hạn (Permissions Flags) dưới dạng lũy thừa của 2
        const byte PERM_READ    = 1 << 0; // 0000 0001 (1) - Quyền Đọc
        const byte PERM_WRITE   = 1 << 1; // 0000 0010 (2) - Quyền Ghi
        const byte PERM_EXECUTE = 1 << 2; // 0000 0100 (4) - Quyền Thực thi
        const byte PERM_DELETE  = 1 << 3; // 0000 1000 (8) - Quyền Xóa

        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            Console.WriteLine("=== HỆ THỐNG QUẢN LÝ PHÂN QUYỀN TỆP TIN BẰNG BITMASKING ===");

            // 1. Khởi tạo người dùng: ban đầu chỉ có quyền ĐỌC và THỰC THI
            // Dùng toán tử OR bit (|) để gộp quyền
            byte userPerms = (byte)(PERM_READ | PERM_EXECUTE); // 0000 0101 (5)
            PrintPermissions("Khởi tạo ban đầu", userPerms);

            // 2. Thao tác THÊM quyền: Cấp thêm quyền GHI (Write)
            // Cú pháp: userPerms |= PERM_WRITE;
            userPerms |= PERM_WRITE; // 0000 0101 | 0000 0010 = 0000 0111 (7)
            PrintPermissions("Sau khi cấp thêm quyền GHI", userPerms);

            // 3. Thao tác KIỂM TRA quyền: Kiểm tra người dùng có quyền XÓA (Delete) không?
            // Dùng toán tử AND bit (&): (userPerms & PERM_DELETE) != 0
            bool canDelete = (userPerms & PERM_DELETE) != 0;
            Console.WriteLine($"-> Người dùng có quyền XÓA không? {(canDelete ? "CÓ" : "KHÔNG")}");

            bool canWrite = (userPerms & PERM_WRITE) != 0;
            Console.WriteLine($"-> Người dùng có quyền GHI không? {(canWrite ? "CÓ" : "KHÔNG")}");

            // 4. Thao tác THU HỒI quyền: Tước bỏ quyền THỰC THI (Execute)
            // Cú pháp: userPerms &= ~PERM_EXECUTE;
            // Giải thích: ~PERM_EXECUTE đảo bit (1111 1011), sau đó AND sẽ xóa đúng bit đó về 0
            userPerms &= (byte)(~PERM_EXECUTE);
            PrintPermissions("Sau khi thu hồi quyền THỰC THI", userPerms);

            // 5. Thao tác ĐẢO quyền (Toggle): Nếu chưa có thì thêm, có rồi thì xóa
            // Dùng toán tử XOR bit (^)
            userPerms ^= PERM_DELETE;
            PrintPermissions("Sau khi Toggle quyền XÓA (bật lên)", userPerms);
        }

        static void PrintPermissions(string title, byte perms)
        {
            string bin = Convert.ToString(perms, 2).PadLeft(8, '0');
            Console.WriteLine($"\\n[{title}] Mã nhị phân: {bin} (Giá trị thập phân: {perms})");
            Console.WriteLine($"   - Quyền Đọc (Read):       {((perms & PERM_READ) != 0 ? "BẬT" : "TẮT")}");
            Console.WriteLine($"   - Quyền Ghi (Write):      {((perms & PERM_WRITE) != 0 ? "BẬT" : "TẮT")}");
            Console.WriteLine($"   - Quyền Chạy (Execute):   {((perms & PERM_EXECUTE) != 0 ? "BẬT" : "TẮT")}");
            Console.WriteLine($"   - Quyền Xóa (Delete):     {((perms & PERM_DELETE) != 0 ? "BẬT" : "TẮT")}");
        }
    }
}""", "BaiThucHanh3_2_Bitmasking_Permissions.cs")

    # Bài 3.3 - Tương tự
    add_heading_2(doc, "3. Bài Thực Hành Tương Tự 3.3: Hệ Thống Giám Sát 8 Cảm Biến IoT Nhà Máy Thông Minh")
    add_p(doc, 
        "Đề bài: Một trạm IoT trong nhà máy công nghiệp gửi về trung tâm giám sát một byte duy nhất (8 bit) "
        "để báo cáo trạng thái của 8 cảm biến. Quy ước vị trí bit (từ 0 đến 7) như sau:\n"
        "• Bit 0 (1): Cảm biến Nhiệt độ quá ngưỡng (Overheat)\n"
        "• Bit 1 (2): Cảm biến Khói / Cháy (Smoke/Fire)\n"
        "• Bit 2 (4): Cửa kho mở (Door Open)\n"
        "• Bit 3 (8): Áp suất bình khí nén bất thường (High Pressure)\n"
        "• Bit 4 (16): Cảm biến Rung lắc động cơ (Vibration Alert)\n"
        "• Bit 5 (32): Độ ẩm không khí vượt chuẩn (High Humidity)\n"
        "• Bit 6 (64): Nguồn điện phụ dự phòng đang bật (Backup Power On)\n"
        "• Bit 7 (128): Toàn hệ thống đang ở chế độ Bảo trì (Maintenance Mode)\n"
        "Hãy viết chương trình C# cho phép:\n"
        "1. Nhập vào một số nguyên từ 0 đến 255 biểu thị byte cảm biến nhận được.\n"
        "2. Giải mã và in ra danh sách các cảm biến đang ở trạng thái BÁO ĐỘNG.\n"
        "3. Kích hoạt còi báo động khẩn cấp (Emergency Alarm) nếu CÓ ÍT NHẤT MỘT trong hai sự cố: "
        "(Nhiệt độ quá ngưỡng VÀ Khói/Cháy) HOẶC Áp suất bình khí nén bất thường.", "Segoe UI", 9.8)

    add_heading_3(doc, "Bảng Test Cases Kiểm Thử Bài 3.3:")
    tc_3_3_headers = ["Test Case", "Giá trị byte nhập", "Dạng nhị phân 8-bit", "Danh sách cảnh báo giải mã", "Còi khẩn cấp?"]
    tc_3_3_rows = [
        ["TC 01", "3", "0000 0011", "Bit 0 (Nhiệt độ) & Bit 1 (Khói/Cháy)", "CÓ (Cháy + Quá nhiệt)"],
        ["TC 02", "8", "0000 1000", "Bit 3 (Áp suất bình khí nén)", "CÓ (Áp suất bất thường)"],
        ["TC 03", "36", "0010 0100", "Bit 2 (Cửa mở) & Bit 5 (Độ ẩm cao)", "KHÔNG (Chỉ cảnh báo thường)"],
        ["TC 04", "128", "1000 0000", "Bit 7 (Đang chế độ Bảo trì)", "KHÔNG (Hệ thống an toàn)"]
    ]
    add_table_custom(doc, tc_3_3_headers, tc_3_3_rows, [0.8, 1.2, 1.3, 2.5, 1.2])

    # Bài 3.4 - Về nhà
    add_heading_2(doc, "4. Bài Tập Tự Luyện Về Nhà 3.4: Thuật Toán Mã Hóa & Giải Mã Đối Xứng XOR Cipher")
    add_p(doc, 
        "Đề bài: Phép toán XOR có tính chất đối xứng toán học kỳ diệu: (A ^ K) ^ K = A. "
        "Dựa trên nguyên lý này, hãy viết chương trình Console cho phép:\n"
        "1. Người dùng nhập vào một chuỗi văn bản bất kỳ (ví dụ: \"HELLO IT26M\").\n"
        "2. Nhập một khóa bí mật (Secret Key) là một ký tự char (ví dụ: 'K').\n"
        "3. Thực hiện mã hóa từng ký tự của chuỗi bằng phép XOR với khóa: char encrypted = (char)(c ^ key);\n"
        "4. In chuỗi đã mã hóa ra màn hình (dưới dạng mã Hex hoặc ký tự).\n"
        "5. Thực hiện giải mã lại chuỗi đã mã hóa bằng chính khóa bí mật đó và chứng minh chuỗi phục hồi 100% nguyên vẹn.", "Segoe UI", 9.8)

    # =========================================================================
    # PHẦN IV: CHUYỂN ĐỔI KIỂU DỮ LIỆU & PHÒNG THỦ CHỐNG TRÀN SỐ
    # =========================================================================
    add_heading_1(doc, "PHẦN IV: CHUYỂN ĐỔI KIỂU DỮ LIỆU & PHÒNG THỦ CHỐNG TRÀN SỐ")

    add_p(doc, 
        "C# là ngôn ngữ có tính an toàn kiểu cao (Strongly Typed). Mỗi kiểu dữ liệu được máy tính cấp phát kích thước bit "
        "và cách giải mã khác nhau. Chúng ta có hai cơ chế chuyển đổi chính:\n"
        "• Ép kiểu ngầm định (Implicit Widening): Xảy ra tự động khi chuyển từ kiểu có kích thước nhỏ sang kiểu có kích thước lớn hơn "
        "(vd: int -> double). Không bao giờ làm mất dữ liệu.\n"
        "• Ép kiểu tường minh (Explicit Narrowing): Phải viết cú pháp ép kiểu (type) trước biểu thức. Có nguy cơ mất mát dữ liệu "
        "do cắt cụt phần thập phân hoặc tràn số nguyên (vd: (int)3.99 ra 3).", "Segoe UI", 10.0)

    add_heading_2(doc, "Bảng So Sánh 4 Phương Pháp Chuyển Đổi Kiểu Trong C#")
    conv_headers = ["Phương thức", "Cú pháp", "Hành vi với số thực", "Xử lý khi chuỗi không hợp lệ", "Khuyên dùng khi nào?"]
    conv_rows = [
        ["Toán tử ép kiểu", "(int)d", "Cắt cụt phần thập phân (Truncate), không làm tròn.", "Báo lỗi lúc biên dịch nếu kiểu không tương thích.", "Chuyển đổi số học cơ bản (double -> int, int -> long)."],
        ["Convert.ToInt32()", "Convert.ToInt32(val)", "Làm tròn ngân hàng (Banker's Rounding: .5 làm tròn về số chẵn).", "Ném FormatException nếu chuỗi sai; trả về 0 nếu null.", "Chuyển đổi đa năng an toàn với giá trị null."],
        ["int.Parse()", "int.Parse(str)", "Không hỗ trợ chuỗi số thực; chỉ parse số nguyên.", "Ném ngoại lệ FormatException hoặc OverflowException làm SẬP app!", "Chỉ dùng khi 100% chắc chắn chuỗi nhập chuẩn."],
        ["int.TryParse()", "int.TryParse(str, out res)", "Trả về bool (true/false), không bao giờ ném ngoại lệ gây sập app.", "Nếu sai: trả về false và gán res = 0. Không bao giờ crash!", "CHUẨN VÀNG: Bắt buộc dùng cho toàn bộ nhập liệu Console/UI."]
    ]
    add_table_custom(doc, conv_headers, conv_rows, [1.3, 1.2, 1.5, 1.8, 1.2])

    # Bài 4.1
    add_heading_2(doc, "1. Bài Thực Hành Có Lời Giải 4.1: Module Nhập Liệu An Toàn Tuyệt Đối (Defensive Input Reader)")
    add_p(doc, 
        "Mục tiêu: Xây dựng kỹ năng lập trình phòng thủ (Defensive Programming), đảm bảo chương trình không bao giờ bị sập "
        "dù người dùng cố tình nhập chuỗi rác, chữ cái hoặc ký tự đặc biệt.", "Segoe UI", 9.8, italic=True)

    add_code_block(doc, 
"""using System;

namespace Buoi05_BaiThucHanh4_1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            Console.WriteLine("=== MODULE NHẬP LIỆU PHÒNG THỦ AN TOÀN TUYỆT ĐỐI ===");

            int tuoi = ReadIntSafe("Nhập tuổi sinh viên (từ 18 đến 60): ", 18, 60);
            double diemGPA = ReadDoubleSafe("Nhập điểm GPA (từ 0.0 đến 4.0): ", 0.0, 4.0);

            Console.WriteLine("\\n-> XÁC NHẬN DỮ LIỆU ĐÃ NHẬP HỢP LỆ:");
            Console.WriteLine($"   Tuổi: {tuoi} tuổi");
            Console.WriteLine($"   Điểm GPA: {diemGPA:F2}");
        }

        // Hàm đọc số nguyên an toàn với int.TryParse và vòng lặp while
        static int ReadIntSafe(string prompt, int minVal, int maxVal)
        {
            int result;
            while (true)
            {
                Console.Write(prompt);
                string input = Console.ReadLine();

                // Dùng TryParse: Trả về true nếu chuyển đổi thành công, false nếu người dùng nhập rác
                if (int.TryParse(input, out result))
                {
                    if (result >= minVal && result <= maxVal)
                    {
                        return result; // Hợp lệ, trả về kết quả
                    }
                    Console.WriteLine($"[LỖI] Giá trị phải nằm trong khoảng [{minVal} - {maxVal}]! Vui lòng nhập lại.");
                }
                else
                {
                    Console.WriteLine("[LỖI] Dữ liệu nhập không phải là số nguyên hợp lệ! Vui lòng nhập lại.");
                }
            }
        }

        // Hàm đọc số thực an toàn với double.TryParse
        static double ReadDoubleSafe(string prompt, double minVal, double maxVal)
        {
            double result;
            while (true)
            {
                Console.Write(prompt);
                string input = Console.ReadLine();

                if (double.TryParse(input, out result))
                {
                    if (result >= minVal && result <= maxVal)
                    {
                        return result;
                    }
                    Console.WriteLine($"[LỖI] Giá trị phải nằm trong khoảng [{minVal:F1} - {maxVal:F1}]! Vui lòng nhập lại.");
                }
                else
                {
                    Console.WriteLine("[LỖI] Dữ liệu nhập không phải là số thực hợp lệ! Vui lòng nhập lại.");
                }
            }
        }
    }
}""", "BaiThucHanh4_1_DefensiveInput.cs")

    # Bài 4.2
    add_heading_2(doc, "2. Bài Thực Hành Có Lời Giải 4.2: Mô Phỏng Thảm Họa Tràn Số & Khối checked Bảo Vệ")
    add_p(doc, 
        "Mục tiêu: Hiểu rõ hiện tượng tràn số nguyên (Integer Overflow) và cơ chế quay vòng (Wrap-around); "
        "biết cách dùng từ khóa checked và bắt ngoại lệ OverflowException trong hệ thống tài chính.", "Segoe UI", 9.8, italic=True)

    add_code_block(doc, 
"""using System;

namespace Buoi05_BaiThucHanh4_2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            Console.WriteLine("=== HIỂM HỌA TRÀN SỐ VÀ CƠ CHẾ PHÒNG VỆ VỚI CHECKED ===");

            int maxInt = int.MaxValue; // 2,147,483,647
            Console.WriteLine($"1. Giá trị số nguyên int lớn nhất (int.MaxValue): {maxInt:N0}");

            // --- TRƯỜNG HỢP 1: MẶC ĐỊNH KHÔNG CÓ CHECKED (NGUY HIỂM) ---
            // CPU âm thầm quay vòng bit: 0111...1111 cộng 1 thành 1000...0000 (chính là số âm nhỏ nhất!)
            int amThamTran = maxInt + 1;
            Console.WriteLine($"\\n[Mặc định không checked] maxInt + 1 = {amThamTran:N0}");
            Console.WriteLine("-> NGUY HIỂM: Tài khoản ngân hàng từ dương 2.1 tỷ bị biến thành âm 2.1 tỷ mà không báo lỗi!");

            // --- TRƯỜNG HỢP 2: DÙNG KHỐI CHECKED VÀ TRY...CATCH BẢO VỆ ---
            Console.WriteLine("\\n--- KÍCH HOẠT LÁ CHẮN CHECKED BẢO VỆ GIAO DỊCH ---");
            try
            {
                checked
                {
                    Console.WriteLine("Đang thực hiện giao dịch cộng thêm 100 VNĐ vào tài khoản...");
                    int ketQua = maxInt + 100; // Phép tính này sẽ bị chặn đứng ngay lập tức!
                    Console.WriteLine($"Giao dịch thành công: {ketQua}");
                }
            }
            catch (OverflowException ex)
            {
                Console.WriteLine($"[CẢNH BÁO BẢO MẬT] Bắt được ngoại lệ: {ex.GetType().Name}");
                Console.WriteLine("-> Hệ thống đã ngăn chặn thảm họa tràn số thành công! Giao dịch được rollback an toàn.");
            }
        }
    }
}""", "BaiThucHanh4_2_IntegerOverflow.cs")

    # Bài 4.3 - Tương tự
    add_heading_2(doc, "3. Bài Thực Hành Tương Tự 4.3: Máy Thu Ngân Siêu Thị & So Sánh Banker's Rounding")
    add_p(doc, 
        "Đề bài: Viết chương trình mô phỏng máy thu ngân siêu thị. Khi tính tiền hóa đơn, hệ thống cần làm tròn các số tiền lẻ.\n"
        "Hãy viết code so sánh kết quả của 3 phương pháp làm tròn trên cùng một danh sách 5 số thực tiền tệ:\n"
        "• Danh sách: 12.5, 13.5, 14.5, 15.5, 16.5\n"
        "1. Ép kiểu cắt cụt: (int)val\n"
        "2. Phương thức Convert.ToInt32(val) (Làm tròn ngân hàng - Banker's Rounding: .5 làm tròn về số chẵn gần nhất)\n"
        "3. Làm tròn học đường thông thường: Math.Round(val, MidpointRounding.AwayFromZero)\n"
        "Xuất bảng so sánh và giải thích tại sao ngành ngân hàng lại chọn quy tắc Banker's Rounding để tránh sai lệch thống kê hàng tỷ đồng.", "Segoe UI", 9.8)

    # Bài 4.4 - Về nhà
    add_heading_2(doc, "4. Bài Tập Tự Luyện Về Nhà 4.4: Bộ Giải Mã Gói Tin Mạng (Packet Header Decoder)")
    add_p(doc, 
        "Đề bài: Một thiết bị mạng truyền về một mảng 4 bytes Header của gói tin dữ liệu:\n"
        "• Byte 0: Mã giao thức (Protocol ID - giá trị từ 1 đến 10).\n"
        "• Byte 1: Loại gói tin (Packet Type: 1 = SYN, 2 = ACK, 3 = DATA, 4 = FIN).\n"
        "• Byte 2 & Byte 3: Độ dài gói tin (Payload Length - 16 bit, được ghép từ Byte 2 dịch trái 8 bit OR với Byte 3).\n"
        "Yêu cầu:\n"
        "1. Nhập vào 4 số nguyên biểu thị 4 bytes của Header.\n"
        "2. Kiểm tra ép kiểu an toàn: Mỗi byte phải nằm trong đoạn [0, 255].\n"
        "3. Sử dụng phép toán dịch bit: int payloadLength = (b2 << 8) | b3; để tái tạo độ dài gói tin 16-bit.\n"
        "4. Tính mã kiểm tra Checksum đơn giản bằng phép XOR cả 4 bytes: byte checksum = (byte)(b0 ^ b1 ^ b2 ^ b3);\n"
        "5. Xuất báo cáo cấu trúc gói tin hoàn chỉnh ra màn hình.", "Segoe UI", 9.8)

    # =========================================================================
    # PHẦN V: TOÁN TỬ GÁN PHỨC HỢP, THỨ TỰ ƯU TIÊN & THỬ THÁCH TỔNG HỢP
    # =========================================================================
    add_heading_1(doc, "PHẦN V: TOÁN TỬ GÁN PHỨC HỢP, THỨ TỰ ƯU TIÊN & THỬ THÁCH TỔNG HỢP")

    add_p(doc, 
        "Bản chất câu lệnh gán: variable = expression;. Quy trình thực thi gồm 2 bước dứt khoát: "
        "Bước 1: Toàn bộ biểu thức ở vế phải (R-Value) được đánh giá hoàn chỉnh. "
        "Bước 2: Kết quả ghi đè vào vị trí ô nhớ ở vế trái (L-Value). Do đó vế trái bắt buộc phải là một biến có ô nhớ ghi được.\n"
        "Các toán tử gán phức hợp (+=, -=, *=, /=, %=, <<=, >>=, &=, |=, ^=) có một ĐIỂM TINH TẾ CỰC KỲ QUAN TRỌNG: "
        "Chúng tự động ép kiểu ngầm định về kiểu của vế trái! Ví dụ: short s = 5; s += 1; hoàn toàn hợp lệ, "
        "nhưng s = s + 1; sẽ báo lỗi biên dịch CS0266 vì s + 1 tự động nâng lên kiểu int!", "Segoe UI", 10.0)

    # Bài 5.1 - Mini Challenge
    add_heading_2(doc, "1. Bài Thực Hành Có Lời Giải 5.1: Mini-Challenge 15 Phút Thực Chiến Phòng Máy")
    add_p(doc, 
        "Mục tiêu: Đánh giá tổng hợp toàn diện kiến thức Buổi 5 qua 5 nhiệm vụ thực chiến liên hoàn trong 15 phút.", "Segoe UI", 9.8, italic=True)

    add_code_block(doc, 
"""using System;

namespace Buoi05_MiniChallenge
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            Console.WriteLine("=== THỬ THÁCH MINI-CHALLENGE 15 PHÚT TỔNG HỢP BUỔI 05 ===");

            // NHIỆM VỤ 1: Nhập số nguyên dương N an toàn bằng int.TryParse
            int n;
            while (true)
            {
                Console.Write("1. Nhập số nguyên dương N (1 <= N <= 1000): ");
                if (int.TryParse(Console.ReadLine(), out n) && n >= 1 && n <= 1000)
                {
                    Console.WriteLine($"   -> Xác nhận N = {n}");
                    break;
                }
                Console.WriteLine("   [Lỗi] Vui lòng nhập số nguyên trong khoảng [1 - 1000]!");
            }

            // NHIỆM VỤ 2: Kiểm tra chẵn lẻ bằng toán tử bitwise & 1
            bool isEven = (n & 1) == 0;
            Console.WriteLine($"2. Kiểm tra chẵn/lẻ bằng (n & 1): Số {n} là {(isEven ? "SỐ CHẴN" : "SỐ LẺ")}");

            // NHIỆM VỤ 3: Dịch bit nhân 8 (<< 3) và chia 4 (>> 2)
            int nNhan8 = n << 3;
            int nChia4 = n >> 2;
            Console.WriteLine($"3. Thao tác dịch bit:");
            Console.WriteLine($"   -> N << 3 (N * 8) = {nNhan8}");
            Console.WriteLine($"   -> N >> 2 (N / 4) = {nChia4}");

            // NHIỆM VỤ 4: Tính trung bình cộng của N với 15 dưới dạng số thực
            // Bắt buộc ép kiểu để có phép chia thực
            double trungBinh = (n + 15) / 2.0;
            Console.WriteLine($"4. Trung bình cộng ({n} + 15) / 2.0 = {trungBinh:F2}");

            // NHIỆM VỤ 5: Bảo vệ chống tràn số với checked khi cộng int.MaxValue
            Console.WriteLine("5. Kiểm thử phòng vệ chống tràn số với checked:");
            try
            {
                checked
                {
                    int nguyCo = int.MaxValue;
                    Console.WriteLine($"   Đang thử nghiệm cộng N ({n}) với int.MaxValue ({nguyCo:N0})...");
                    int ketQua = nguyCo + n; // Tràn số chắc chắn xảy ra!
                    Console.WriteLine($"   Kết quả: {ketQua}");
                }
            }
            catch (OverflowException)
            {
                Console.WriteLine("   -> THÀNH CÔNG: Đã chặn đứng OverflowException bằng lá chắn checked!");
            }

            Console.WriteLine("\\n=== HOÀN THÀNH XUẤT SẮC CẢ 5 NHIỆM VỤ MINI-CHALLENGE ===");
        }
    }
}""", "MiniChallenge_Buoi05.cs")

    # Bài 5.2 - Tương tự
    add_heading_2(doc, "2. Bài Thực Hành Tương Tự 5.2: Cỗ Máy Sinh Bảng Chân Trị Tự Động (Truth Table Generator)")
    add_p(doc, 
        "Đề bài: Viết chương trình C# tự động tính toán và in ra Bảng Chân Trị (Truth Table) hoàn chỉnh cho biểu thức logic: "
        "F = (A && B) || (!A && C) với 3 biến nhị phân A, B, C (chạy qua tất cả 8 tổ hợp từ 000 đến 111).\n"
        "Yêu cầu:\n"
        "1. Dùng 3 vòng lặp for lồng nhau duyệt qua A, B, C nhận giá trị true/false.\n"
        "2. Xuất bảng định dạng đẹp mắt với các cột: A | B | C | (A && B) | (!A && C) | Kết quả F.\n"
        "3. Đếm xem có bao nhiêu tổ hợp cho kết quả F = true.", "Segoe UI", 9.8)

    # Bài 5.3 - Capstone Project
    add_heading_2(doc, "3. Đồ Án Mini Cuối Buổi 5.3 (Capstone Challenge): Hệ Thống Quản Lý Kho Hàng Thông Minh")
    add_p(doc, 
        "Đề bài: Xây dựng ứng dụng Console hoàn chỉnh mô phỏng 'Hệ Thống Quản Lý Kho Hàng & Giám Sát Lô Sản Phẩm' "
        "(Smart Inventory & Sensor Tagging System) tích hợp toàn bộ các kỹ năng đã học trong Buổi 5.\n\n"
        "Yêu cầu chức năng chi tiết:\n"
        "1. Nhập liệu an toàn (CLO 5.5): Sử dụng hàm TryParse để nhập Mã lô hàng (int), Số lượng thùng hàng (int), "
        "Đơn giá mỗi thùng (double), và Trọng lượng mỗi thùng (kg).\n"
        "2. Quản lý trạng thái bằng Bitmasking (CLO 5.4): Mỗi lô hàng được gắn 1 byte cờ trạng thái gồm các bit:\n"
        "   • Bit 0 (1): Hàng dễ vỡ (Fragile)\n"
        "   • Bit 1 (2): Cần bảo quản đông lạnh (Cold Storage)\n"
        "   • Bit 2 (4): Hàng hóa chất nguy hiểm (Hazardous Material)\n"
        "   • Bit 3 (8): Đã kiểm định hải quan đạt chuẩn (Customs Passed)\n"
        "   • Bit 4 (16): Ưu tiên xuất kho hỏa tốc (Express Dispatch)\n"
        "Cho phép người dùng bật/tắt các cờ trạng thái trên lô hàng thông qua menu chọn số.\n"
        "3. Tính toán tài chính an toàn (CLO 5.1 & 5.5): Tính Tổng giá trị lô hàng = Số lượng * Đơn giá. "
        "Sử dụng khối checked để bắt lỗi tràn số nếu kho hàng nhập số lượng cực lớn. "
        "Tính thuế VAT (8%) và phụ phí bảo quản (nếu có cờ Đông lạnh thì cộng thêm 5% phụ phí, nếu có cờ Hóa chất thì cộng 10% phụ phí).\n"
        "4. Đánh giá xuất kho bằng Logic đoản mạch (CLO 5.3): Lô hàng CHỈ ĐƯỢC PHÉP XUẤT KHO khi:\n"
        "   Đã kiểm định hải quan VÀ (Không phải hàng hóa chất HOẶC Có chứng nhận an toàn riêng).", "Segoe UI", 9.8)

    add_heading_3(doc, "Bảng Tiêu Chí Đánh Giá & Chấm Điểm Rubric Đồ Án Mini 5.3 (Thang Điểm 10):")
    rubric_headers = ["Tiêu chí đánh giá", "Trọng số", "Yêu cầu đạt điểm tối đa"]
    rubric_rows = [
        ["1. Nhập liệu an toàn (Defensive Input)", "2.0 điểm", "Sử dụng hoàn toàn TryParse, không bao giờ để chương trình sập khi nhập chuỗi ký tự sai hoặc số âm."],
        ["2. Xử lý Bitmasking phân cờ trạng thái", "3.0 điểm", "Sử dụng đúng các toán tử |, &, ~, ^ để bật cờ, kiểm tra cờ và xóa cờ trạng thái lô hàng."],
        ["3. Tính toán tài chính & Khối checked", "2.0 điểm", "Tính đúng tổng tiền, thuế VAT, phụ phí; có khối checked bảo vệ chống tràn số khi nhân số lượng lớn."],
        ["4. Logic đoản mạch thẩm định xuất kho", "1.5 điểm", "Biểu thức điều kiện đoản mạch kết hợp chuẩn xác, không có bẫy logic."],
        ["5. Clean Code & Giao diện Console chuyên nghiệp", "1.5 điểm", "Mã nguồn thụt lề chuẩn, đặt tên biến có ý nghĩa theo chuẩn C#, menu điều hướng rõ ràng, định dạng tiền tệ đẹp."]
    ]
    add_table_custom(doc, rubric_headers, rubric_rows, [2.2, 1.0, 3.8])

    # =========================================================================
    # PHẦN VI: HƯỚNG DẪN TỰ ĐÁNH GIÁ, DEBUGGING & NỘP BÀI
    # =========================================================================
    add_heading_1(doc, "PHẦN VI: HƯỚNG DẪN TỰ ĐÁNH GIÁ, DEBUGGING & NỘP BÀI")

    add_p(doc, 
        "Trong quá trình lập trình tại phòng lab, sinh viên thường xuyên gặp phải các thông báo lỗi biên dịch của C#. "
        "Dưới đây là Bảng tra cứu các mã lỗi phổ biến nhất liên quan đến biểu thức và kiểu dữ liệu cùng biện pháp xử lý nhanh:", "Segoe UI", 10.0)

    err_headers = ["Mã lỗi C#", "Nguyên nhân bản chất", "Cách khắc phục chuẩn mực"]
    err_rows = [
        ["CS0029", "Không thể chuyển đổi ngầm định kiểu dữ liệu (Cannot implicitly convert type 'A' to 'B').", "Thêm toán tử ép kiểu tường minh (type) hoặc gọi Convert.ToXxx() / Parse()."],
        ["CS0103", "Tên biến không tồn tại trong ngữ cảnh hiện tại (The name 'x' does not exist in the current context).", "Kiểm tra xem biến đã được khai báo trước khi dùng chưa, hoặc sai phạm vi khối lệnh { }."],
        ["CS0019", "Toán tử không thể áp dụng cho hai toán hạng (Operator '+' cannot be applied to operands).", "Kiểm tra kiểu của hai vế; ví dụ không thể lấy bool cộng với int."],
        ["CS0266", "Thu hẹp kiểu dữ liệu bị chặn (An explicit conversion exists. Are you missing a cast?).", "Thêm ép kiểu tường minh (int), ví dụ khi gán kết quả phép chia double về biến int."],
        ["CS0131", "Vế trái của câu lệnh gán phải là một biến, thuộc tính hoặc chỉ mục (The left-hand side must be a variable).", "Kiểm tra nhầm lẫn dấu '=' với '==', hoặc viết biểu thức ở vế trái (vd: x + 1 = 10)."]
    ]
    add_table_custom(doc, err_headers, err_rows, [1.1, 2.7, 3.2])

    add_callout(doc,
        "Quy chuẩn nộp bài thực hành phòng lab:\n"
        "1. Tạo thư mục theo cú pháp: [MSSV]_[HoVaTen]_LabBuoi05 (Ví dụ: 123456_NguyenVanA_LabBuoi05).\n"
        "2. Đặt toàn bộ các Solution bài thực hành vào thư mục trên.\n"
        "3. Xóa thư mục bin/ và obj/ để giảm dung lượng trước khi nén thành tệp .ZIP.\n"
        "4. Nộp lên hệ thống E-Learning Đại học Đông Á đúng thời hạn quy định.",
        "QUY CHUẨN ĐÓNG GÓI VÀ NỘP BÀI THỰC HÀNH", "success")

    # Save Document
    out_dir = os.path.join(os.getcwd(), "Lab")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "Huong-Dan-Thuc-Hanh-Lap-Trinh-CSharp-Buoi-05.docx")
    doc.save(out_path)
    print(f"Successfully generated Word document at:\n{out_path}")
    return out_path

if __name__ == "__main__":
    build_document()
