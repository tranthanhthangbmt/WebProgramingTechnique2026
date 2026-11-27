# -*- coding: utf-8 -*-
"""
Script to generate the complete, production-grade LaTeX Beamer slide for Buổi 04:
Bài 4: Chương 2 (Tiếp theo): Nền tảng về ngôn ngữ lập trình - Biểu thức, Các phép toán, Thao tác bit, Chuyển đổi kiểu dữ liệu và Câu lệnh gán.
Học phần: Kỹ thuật lập trình (C# & .NET) - Lớp IT26M, Đại học Đông Á (UDA).
"""

import os

tex_content = r"""\documentclass[aspectratio=169, 10pt]{beamer}

% --- GÓI HỌC THUẬT & FONT TIẾNG VIỆT CHO XELATEX ---
\usepackage{fontspec}
\setmainfont{Arial}
\setsansfont{Arial}
\setmonofont{Consolas}

\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{multicol}
\usepackage{listings}
\usepackage{xcolor}
\usepackage{tikz}
\usetikzlibrary{shapes,arrows,positioning,fit,backgrounds,calc}
\usepackage{tcolorbox}
\tcbuselibrary{skins,breakable,listings}

% --- ĐỊNH NGHĨA BẢNG MÀU CHUẨN ĐẠI HỌC & C# .NET ---
\definecolor{UniNavy}{RGB}{15, 44, 89}        % Xanh hải quân chủ đạo (#0F2C59)
\definecolor{UniBlue}{RGB}{29, 93, 155}       % Xanh Slate (#1D5D9B)
\definecolor{CSharpPurple}{RGB}{104, 33, 122} % Tím nhận diện C# & Visual Studio (#68217A)
\definecolor{UniLightBlue}{RGB}{232, 241, 252}% Nền xanh nhạt
\definecolor{UniOrange}{RGB}{225, 112, 18}    % Cam nhấn mạnh (#E17012)
\definecolor{UniGreen}{RGB}{30, 132, 73}      % Xanh lá thực hành (#1E8449)
\definecolor{UniDark}{RGB}{33, 37, 41}        % Màu chữ chính / nền console
\definecolor{CodeBg}{RGB}{248, 249, 250}      % Nền code
\definecolor{CSharpKeyword}{RGB}{0, 0, 255}   % Xanh dương từ khóa C#
\definecolor{CSharpString}{RGB}{163, 21, 21}  % Đỏ chuỗi C#
\definecolor{CSharpComment}{RGB}{0, 128, 0}   % Xanh lá chú thích C#
\definecolor{AlertRed}{RGB}{192, 57, 43}      % Đỏ cảnh báo lỗi

% --- CẤU HÌNH THEME BEAMER MADRID WIDESCREEN ---
\usetheme{Madrid}
\usecolortheme{whale}

\setbeamercolor{palette primary}{bg=UniNavy, fg=white}
\setbeamercolor{palette secondary}{bg=CSharpPurple, fg=white}
\setbeamercolor{palette tertiary}{bg=UniNavy!85, fg=white}
\setbeamercolor{palette quaternary}{bg=UniNavy, fg=white}

\setbeamercolor{structure}{fg=UniNavy}
\setbeamercolor{titlelike}{parent=structure, fg=UniNavy}
\setbeamercolor{frametitle}{bg=UniNavy, fg=white}
\setbeamercolor{frametitle continuation}{fg=white}
\setbeamercolor{normal text}{fg=UniDark}

% Cấu hình khối thông tin (Blocks)
\setbeamercolor{block title}{bg=UniBlue, fg=white}
\setbeamercolor{block body}{bg=UniLightBlue!40, fg=UniDark}
\setbeamercolor{block title example}{bg=UniGreen, fg=white}
\setbeamercolor{block body example}{bg=UniGreen!10, fg=UniDark}
\setbeamercolor{block title alerted}{bg=UniOrange, fg=white}
\setbeamercolor{block body alerted}{bg=UniOrange!10, fg=UniDark}

% Cấu hình Footline chuyên nghiệp
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{footline}{
  \leavevmode%
  \hbox{%
    \begin{beamercolorbox}[wd=.35\paperwidth,ht=2.5ex,dp=1.1ex,left,leftskip=2ex]{author in head/foot}%
      \usebeamerfont{author in head/foot}\textbf{Lớp IT26M} | Kỹ thuật Lập trình C\#
    \end{beamercolorbox}%
    \begin{beamercolorbox}[wd=.45\paperwidth,ht=2.5ex,dp=1.1ex,center]{title in head/foot}%
      \usebeamerfont{title in head/foot}Buổi 04: Biểu Thức, Toán Tử \& Thao Tác Bit
    \end{beamercolorbox}%
    \begin{beamercolorbox}[wd=.20\paperwidth,ht=2.5ex,dp=1.1ex,right,rightskip=2ex]{date in head/foot}%
      \usebeamerfont{date in head/foot}\insertframenumber{} / \inserttotalframenumber
    \end{beamercolorbox}%
  }%
  \vskip0pt%
}

% --- CẤU HÌNH GÓI LISTINGS CHO C# & TERMINAL ---
\lstdefinelanguage{CSharpCustom}{
  keywords={abstract, as, base, bool, break, byte, case, catch, char, checked, class, const, continue, decimal, default, delegate, do, double, else, enum, event, explicit, extern, false, finally, fixed, float, for, foreach, goto, if, implicit, in, int, interface, internal, is, lock, long, namespace, new, null, object, operator, out, override, params, private, protected, public, readonly, ref, return, sbyte, sealed, short, sizeof, stackalloc, static, string, struct, switch, this, throw, true, try, typeof, uint, ulong, unchecked, unsafe, ushort, using, virtual, void, volatile, while, async, await, var},
  keywordstyle=\color{CSharpKeyword}\bfseries,
  ndkeywords={Console, String, Math, Convert, int, double, float, char, bool, long, byte, short, decimal},
  ndkeywordstyle=\color{CSharpPurple}\bfseries,
  sensitive=true,
  comment=[l]{//},
  morecomment=[s]{/*}{*/},
  commentstyle=\color{CSharpComment}\itshape,
  stringstyle=\color{CSharpString},
  morestring=[b]",
  morestring=[b]'
}

\lstset{
  language=CSharpCustom,
  basicstyle=\ttfamily\scriptsize,
  numbers=left,
  numberstyle=\tiny\color{gray},
  stepnumber=1,
  numbersep=6pt,
  backgroundcolor=\color{CodeBg},
  frame=single,
  rulecolor=\color{black!20},
  tabsize=4,
  showstringspaces=false,
  breaklines=true,
  breakatwhitespace=true,
  columns=flexible,
  keepspaces=true,
  xleftmargin=12pt,
  framexleftmargin=10pt
}

\lstdefinestyle{terminalStyle}{
  basicstyle=\ttfamily\scriptsize\color{white},
  backgroundcolor=\color{UniDark},
  frame=single,
  rulecolor=\color{UniNavy},
  numbers=none,
  xleftmargin=6pt,
  framexleftmargin=6pt
}

% --- THÔNG TIN TRANG TIÊU ĐỀ ---
\title[\textbf{Kỹ thuật Lập trình C\# -- Buổi 04}]{\textbf{\LARGE KỸ THUẬT LẬP TRÌNH C\#}}
\subtitle{\textbf{\large Bài 4: Biểu Thức, Các Phép Toán, Thao Tác Bit \& Chuyển Đổi Kiểu}}
\author[\textbf{Khoa CNTT -- IT26M}]{\textbf{BÀI GIẢNG ĐẠI HỌC CHÍNH QUY (3 TIẾT TÍCH HỢP)}\\Chương 2 (Tiếp theo): Nền tảng về ngôn ngữ lập trình C\#}
\institute[\textbf{Lớp IT26M}]{\textbf{Khoa Công nghệ Thông tin -- Trường Đại học Đông Á (UDA)}\\\textbf{Đối tượng:} Sinh viên năm nhất -- Lớp IT26M (Khóa tuyển sinh 2026)}
\date[\textbf{2026}]{\textbf{Học kỳ I -- Năm học 2026}}

\begin{document}

% ==============================================================================
% SLIDE 01: TRANG TIÊU ĐỀ BÀI GIẢNG
% ==============================================================================
\begin{frame}[plain]
  \titlepage
  \begin{center}
    \scriptsize \color{gray} Bản quyền bài giảng thuộc Bộ môn Kỹ thuật Lập trình -- Khoa Công nghệ Thông tin, Đại học Đông Á
  \end{center}
\end{frame}

% ==============================================================================
% SLIDE 02: BỐI CẢNH SƯ PHẠM: TỪ LAB 01 ĐẾN BUỔI 04
% ==============================================================================
\begin{frame}{Bối cảnh Sư phạm: Từ Thực hành Lab 01 đến Buổi 04}
  \begin{columns}[T]
    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniLightBlue!30,colframe=UniBlue,title=\textbf{Thành quả đã đạt được từ Lab 01},fonttitle=\small\bfseries]
        \begin{itemize}\small
          \item Đã làm chủ thao tác IDE Visual Studio và cấu trúc một chương trình Console chuẩn.
          \item Khai báo biến, hằng số, nhập từ bàn phím (\texttt{Console.ReadLine}) và xuất (\texttt{Console.WriteLine}).
          \item Làm quen với cấu trúc rẽ nhánh cơ bản \texttt{if...else}.
        \end{itemize}
      \end{tcolorbox}
    \end{column}

    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniOrange!10,colframe=UniOrange,title=\textbf{Rào cản nhận thức cần vượt qua},fonttitle=\small\bfseries]
        \begin{itemize}\small
          \item \textbf{Cạm bẫy chia nguyên:} \texttt{5 / 2} ra kết quả \texttt{2} thay vì \texttt{2.5}!
          \item \textbf{Nhầm lẫn tai hại:} Dấu gán \texttt{=} và dấu so sánh bằng \texttt{==}.
          \item \textbf{Khủng hoảng tăng/giảm:} Bối rối trước \texttt{x++} và \texttt{++x}.
          \item \textbf{Bế tắc trước cấp độ Bit:} Chưa hiểu cách máy tính lưu trữ và thao tác dữ liệu nhị phân.
        \end{itemize}
      \end{tcolorbox}
    \end{column}
  \end{columns}

  \vspace{2mm}
  \begin{alertblock}{\textbf{Triết lý đào tạo của Buổi 04: "Làm chủ máy tính từ cấp độ Bit đến Biểu thức"}}
    Chưa vội học Lập trình hướng đối tượng (OOP) khi chưa nắm vững bản chất toán tử, mô hình ô nhớ và ép kiểu. Buổi 04 giúp bạn xây dựng nền tảng tư duy toán-tin vững chắc 100\% trước khi học Hàm và Cấu trúc điều khiển phức tạp.
  \end{alertblock}
\end{frame}

% ==============================================================================
% SLIDE 03: MỤC TIÊU BÀI HỌC & CHUẨN ĐẦU RA (CLOs)
% ==============================================================================
\begin{frame}{Mục tiêu Bài học \& Chuẩn đầu ra (CLOs)}
  \begin{block}{\textbf{5 Chuẩn đầu ra sinh viên cần đạt được sau buổi học 3 tiết (Đề cương UDA):}}
    \begin{itemize}\small
      \item \textbf{CLO 4.1 (Understand / Apply):} Giải thích bản chất của \textbf{Biểu thức (Expressions)}, phân biệt rõ toán tử, toán hạng và giá trị trả về; chuyển đổi chính xác các công thức toán - lý - kinh tế sang biểu thức C\#.
      \item \textbf{CLO 4.2 (Analyze / Apply):} Vận dụng thành thạo và phân biệt chính xác 4 nhóm toán tử: Số học (chia nguyên vs chia thực), So sánh, Logic (cơ chế đoản mạch \texttt{\&\&}, \texttt{||}), và Toán tử tăng/giảm (Tiền tố \texttt{++x} vs Hậu tố \texttt{x++}).
      \item \textbf{CLO 4.3 (Understand / Apply):} Làm chủ các phép toán \textbf{Thao tác Bit (Bitwise)} (\texttt{\&}, \texttt{|}, \texttt{\textasciicircum}, \texttt{\textasciitilde}, \texttt{<<}, \texttt{>>}), biểu diễn số bù 2; ứng dụng kiểm tra chẵn/lẻ siêu tốc và kỹ thuật mặt nạ bit (\textbf{Bitmasking}) quản lý quyền hạn.
      \item \textbf{CLO 4.4 (Analyze / Evaluate):} Phân tích và thực hiện chuẩn xác \textbf{Chuyển đổi kiểu dữ liệu}: Ép kiểu ngầm định vs Tường minh, phân biệt \texttt{(type)}, \texttt{Convert}, \texttt{Parse}, \texttt{TryParse}, và kiểm soát lỗi tràn số với \texttt{checked}/\texttt{unchecked}.
      \item \textbf{CLO 4.5 (Apply):} Vận dụng câu lệnh gán, toán tử gán phức hợp (\texttt{+=}, \texttt{*=}, \texttt{<<=}), làm chủ \textbf{Bảng thứ tự ưu tiên và hướng kết hợp} của các toán tử trong C\#.
    \end{itemize}
  \end{block}
\end{frame}

% ==============================================================================
% SLIDE 04: TIẾN TRÌNH BÀI HỌC 3 TIẾT (AGENDA)
% ==============================================================================
\begin{frame}{Tiến trình Bài học 3 Tiết (150 Phút Tích hợp)}
  \begin{columns}[T]
    \begin{column}{0.32\textwidth}
      \begin{tcolorbox}[colback=UniNavy!5,colframe=UniNavy,title=\textbf{TIẾT 1 (50')},fonttitle=\small\bfseries]
        \textbf{Biểu Thức \& Toán Tử}
        \begin{itemize}\scriptsize
          \item 2.9 Biểu thức trong C\#
          \item Cấu tạo: Toán tử + Toán hạng
          \item Chuyển đổi công thức thực tế
          \item 2.10.1 Toán tử số học nâng cao
          \item Cạm bẫy chia nguyên \& Modulo \%
          \item 2.10.2 So sánh \& Logic đoản mạch
          \item 2.10.3 Tiền tố (\texttt{++x}) vs Hậu tố (\texttt{x++})
          \item \textbf{[CHECKPOINT 1]:} Mini-Quiz
        \end{itemize}
      \end{tcolorbox}
    \end{column}

    \begin{column}{0.32\textwidth}
      \begin{tcolorbox}[colback=CSharpPurple!5,colframe=CSharpPurple,title=\textbf{TIẾT 2 (50')},fonttitle=\small\bfseries]
        \textbf{Thao Tác Bit (Bitwise)}
        \begin{itemize}\scriptsize
          \item 2.11.1 Hệ nhị phân \& Số bù 2
          \item 2.11.2 Toán tử Bitwise (\&, |, \textasciicircum, \textasciitilde)
          \item Phép dịch bit (\texttt{<<}, \texttt{>>})
          \item Nhân chia nhanh lũy thừa 2
          \item Kiểm tra chẵn/lẻ bằng Bit
          \item 2.11.3 Kỹ thuật Mặt nạ bit (Bitmask)
          \item Quản lý quyền hạn (Flags)
          \item \textbf{[CHECKPOINT 2]:} Thực hành Bit
        \end{itemize}
      \end{tcolorbox}
    \end{column}

    \begin{column}{0.32\textwidth}
      \begin{tcolorbox}[colback=UniGreen!5,colframe=UniGreen,title=\textbf{TIẾT 3 (50')},fonttitle=\small\bfseries]
        \textbf{Ép Kiểu \& Thứ Tự Ưu Tiên}
        \begin{itemize}\scriptsize
          \item 2.12 Ép kiểu Ngầm định vs Tường minh
          \item \texttt{(type)} vs \texttt{Convert} vs \texttt{TryParse}
          \item Hiểm họa tràn số (Overflow)
          \item Khối bảo vệ \texttt{checked}/\texttt{unchecked}
          \item 2.13 Câu lệnh gán \& Gán phức hợp
          \item Bảng thứ tự ưu tiên 10 cấp
          \item Quy tắc dùng ngoặc đơn \texttt{()}
          \item \textbf{[CHALLENGE]:} Mini-Challenge
        \end{itemize}
      \end{tcolorbox}
    \end{column}
  \end{columns}
\end{frame}

% ==============================================================================
% SLIDE 05: MỤC 2.9 - BIỂU THỨC TRONG C# (EXPRESSIONS)
% ==============================================================================
\begin{frame}{Mục 2.9: Biểu Thức trong C\# (Expressions)}
  \begin{block}{\textbf{Định nghĩa chuẩn khoa học:}}
    Một \textbf{biểu thức (expression)} là một cấu trúc cú pháp được tạo thành từ các \textbf{toán hạng (operands)} và các \textbf{toán tử (operators)} tuân theo các quy tắc ngữ pháp của C\#, và luôn được máy tính đánh giá để trả về \textbf{MỘT giá trị duy nhất} thuộc \textbf{MỘT kiểu dữ liệu xác định}.
  \end{block}

  \begin{center}
    \begin{tikzpicture}[scale=0.85, every node/.style={transform shape}]
      % Sơ đồ giải phẫu biểu thức
      \node[draw=UniNavy, fill=UniLightBlue!50, rounded corners, inner sep=8pt] (expr) at (0,0) {\Large \texttt{total = price * quantity + tax;}};
      \node[above=0.6cm of expr, text=UniNavy, font=\bfseries] {Giải phẫu một biểu thức gán hoàn chỉnh:};
      
      \draw[<-, thick, red] (-3.1,-0.4) -- (-3.1,-1.2) node[below, font=\scriptsize\bfseries, text=red] {Toán hạng vế trái (Biến)};
      \draw[<-, thick, blue] (-1.9,-0.4) -- (-1.9,-1.2) node[below, font=\scriptsize\bfseries, text=blue] {Toán tử gán};
      \draw[<-, thick, purple] (-0.8,-0.4) -- (-0.8,-1.2) node[below, font=\scriptsize\bfseries, text=purple] {Toán hạng};
      \draw[<-, thick, UniGreen] (0.2,-0.4) -- (0.2,-1.2) node[below, font=\scriptsize\bfseries, text=UniGreen] {Toán tử nhân};
      \draw[<-, thick, purple] (1.3,-0.4) -- (1.3,-1.2) node[below, font=\scriptsize\bfseries, text=purple] {Toán hạng};
      \draw[<-, thick, UniGreen] (2.3,-0.4) -- (2.3,-1.2) node[below, font=\scriptsize\bfseries, text=UniGreen] {Toán tử cộng};
    \end{tikzpicture}
  \end{center}

  \begin{itemize}\small
    \item \textbf{Toán tử (Operators):} Ký hiệu quy định thao tác tính toán (\texttt{+}, \texttt{-}, \texttt{*}, \texttt{/}, \texttt{=}, \dots).
    \item \textbf{Toán hạng (Operands):} Dữ liệu tham gia tính toán (hằng số, biến, literal, lời gọi hàm).
  \end{itemize}
\end{frame}

% ==============================================================================
% SLIDE 06: PHÂN LOẠI BIỂU THỨC TRONG C#
% ==============================================================================
\begin{frame}[fragile]{Phân Loại Biểu Thức trong C\#}
  \begin{table}[h]
    \centering
    \small
    \begin{tabularx}{\textwidth}{l p{4.2cm} p{3.8cm} l}
      \toprule
      \textbf{Loại biểu thức} & \textbf{Đặc điểm \& Phép toán} & \textbf{Ví dụ mã nguồn C\#} & \textbf{Kiểu kết quả} \\
      \midrule
      \textbf{Biểu thức Số học} & Sử dụng các toán tử số học (\texttt{+}, \texttt{-}, \texttt{*}, \texttt{/}, \texttt{\%}) & \texttt{(a + b) * c / 2} & \texttt{int}, \texttt{double} \\
      \addlinespace
      \textbf{Biểu thức Quan hệ} & So sánh giá trị hai vế (\texttt{<}, \texttt{<=}, \texttt{>}, \texttt{>=}, \texttt{==}, \texttt{!=}) & \texttt{age >= 18} & \texttt{bool} (\texttt{true}/\texttt{false}) \\
      \addlinespace
      \textbf{Biểu thức Logic} & Kết hợp nhiều điều kiện (\texttt{\&\&}, \texttt{||}, \texttt{!}) & \texttt{score >= 8.0 \&\& gpa > 3.2} & \texttt{bool} \\
      \addlinespace
      \textbf{Biểu thức Chuỗi} & Ghép chuỗi (\texttt{+}) hoặc Nội suy chuỗi (\texttt{\$"..."}) & \texttt{\$"SV: \{name\}, Tuoi: \{age\}"} & \texttt{string} \\
      \addlinespace
      \textbf{Biểu thức Gán} & Tính toán vế phải và gán kết quả vào biến vế trái & \texttt{x = y + 10} & Kiểu của biến \\
      \bottomrule
    \end{tabularx}
  \end{table}

  \begin{exampleblock}{\textbf{Quy tắc vàng của Trình biên dịch C\#:}}
    Mỗi biểu thức luôn có một \textbf{Kiểu dữ liệu xác định (Type)} tại thời điểm biên dịch. Trình biên dịch sẽ kiểm tra tính tương thích kiểu một cách nghiêm ngặt (Strict Type Safety).
  \end{exampleblock}
\end{frame}

% ==============================================================================
% SLIDE 07: CHUYỂN ĐỔI CÔNG THỨC THỰC TẾ SANG C#
% ==============================================================================
\begin{frame}[fragile]{Chuyển Đổi Công thức Thực tế sang Biểu thức C\#}
  \begin{columns}[T]
    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniLightBlue!30,colframe=UniBlue,title=\textbf{Công thức Toán học / Vật lý},fonttitle=\small\bfseries]
        \begin{itemize}\small
          \item \textbf{Định lý Pythagoras:}
            $$c = \sqrt{a^2 + b^2}$$
          \item \textbf{Biệt thức Delta phương trình bậc 2:}
            $$\Delta = b^2 - 4ac$$
          \item \textbf{Diện tích tam giác (Công thức Heron):}
            $$S = \sqrt{p(p-a)(p-b)(p-c)}$$
          \item \textbf{Công thức tính Lãi kép ngân hàng:}
            $$A = P \times (1 + r)^t$$
        \end{itemize}
      \end{tcolorbox}
    \end{column}

    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=CodeBg,colframe=UniNavy,title=\textbf{Biểu thức C\# Tương ứng},fonttitle=\small\bfseries]
\begin{lstlisting}[numbers=none]
// Pythagoras
double c = Math.Sqrt(a * a + b * b);

// Delta bac 2
double delta = b * b - 4 * a * c;

// Heron (p la nua chu vi)
double p = (a + b + c) / 2.0;
double s = Math.Sqrt(p * (p-a) * (p-b) * (p-c));

// Lai kep (A: tong tien, P: goc, r: lai, t: ky han)
double A = P * Math.Pow(1 + r, t);
\end{lstlisting}
      \end{tcolorbox}
    \end{column}
  \end{columns}

  \begin{alertblock}{\textbf{Lưu ý sư phạm quan trọng:}}
    Trong đại số, viết $4ac$ máy tính không hiểu! Bắt buộc phải viết toán tử nhân tường minh: \texttt{4 * a * c}. Không có toán tử lũy thừa dạng dấu mũ \texttt{\textasciicircum}; dấu \texttt{\textasciicircum} trong C\# là phép toán \textbf{XOR bit}!
  \end{alertblock}
\end{frame}

% ==============================================================================
% SLIDE 08: TÁC DỤNG PHỤ VÀ NGUYÊN TẮC VIẾT BIỂU THỨC
% ==============================================================================
\begin{frame}[fragile]{Tác Dụng Phụ (Side-Effects) trong Biểu Thức}
  \begin{block}{\textbf{Khái niệm Tác dụng phụ (Side-Effect):}}
    Một biểu thức được gọi là có tác dụng phụ nếu ngoài việc trả về một giá trị tính toán, nó còn \textbf{làm thay đổi trạng thái của các ô nhớ (biến)} trong chương trình.
  \end{block}

  \begin{columns}[T]
    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=AlertRed!10,colframe=AlertRed,title=\textbf{Mã nguồn có Side-Effect phức tạp (Tránh)},fonttitle=\small\bfseries]
\begin{lstlisting}[numbers=none]
// NGUY HIEM: Kho doan, de loi!
int a = 5;
int b = a++ + ++a * a--;
Console.WriteLine(b); 
// Ket qua phu thuoc trat tu tinh toan!
\end{lstlisting}
      \end{tcolorbox}
    \end{column}

    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniGreen!10,colframe=UniGreen,title=\textbf{Mã nguồn Tường minh \& Trong sáng (Khuyên dùng)},fonttitle=\small\bfseries]
\begin{lstlisting}[numbers=none]
// CHUAN MUC: Tach thanh tung dong ro rang
int a = 5;
a++; // a = 6
int term1 = a;
a++; // a = 7
int term2 = a * a;
a--; // a = 6
int b = term1 + term2;
\end{lstlisting}
      \end{tcolorbox}
    \end{column}
  \end{columns}

  \vspace{2mm}
  \begin{exampleblock}{\textbf{Lời khuyên từ Kỹ sư Phần mềm (KISS Principle - Keep It Simple, Stupid):}}
    Viết code không phải để giải đố! Hãy ưu tiên mã nguồn dễ đọc, dễ hiểu, dễ kiểm thử. Tránh lạm dụng toán tử tăng giảm trong các biểu thức số học phức tạp.
  \end{exampleblock}
\end{frame}

% ==============================================================================
% SLIDE 09: MỤC 2.10 - CÁC PHÉP TOÁN TRONG C# (OPERATORS)
% ==============================================================================
\begin{frame}{Mục 2.10: Hệ Thống Các Phép Toán trong C\#}
  \begin{columns}[T]
    \begin{column}{0.48\textwidth}
      \begin{block}{\textbf{Phân loại theo Số lượng Toán hạng:}}
        \begin{itemize}\small
          \item \textbf{Toán tử 1 ngôi (Unary):} Chỉ tác động lên 1 toán hạng:
            \begin{itemize}\footnotesize
              \item Đổi dấu: \texttt{+x}, \texttt{-x}
              \item Tăng/giảm: \texttt{++x}, \texttt{x++}, \texttt{--x}, \texttt{x--}
              \item Phủ định logic: \texttt{!flag}
              \item Đảo bit: \texttt{\textasciitilde x}
              \item Ép kiểu: \texttt{(int)d}
            \end{itemize}
          \item \textbf{Toán tử 2 ngôi (Binary):} Tác động lên 2 toán hạng:
            \begin{itemize}\footnotesize
              \item Số học: \texttt{a + b}, \texttt{a * b}, \texttt{a / b}, \texttt{a \% b}
              \item So sánh: \texttt{a > b}, \texttt{a == b}
              \item Logic: \texttt{a \&\& b}, \texttt{a || b}
              \item Thao tác bit: \texttt{a \& b}, \texttt{a | b}, \texttt{a << 2}
            \end{itemize}
          \item \textbf{Toán tử 3 ngôi (Ternary):} Toán tử điều kiện \texttt{? :}:
            \begin{itemize}\footnotesize
              \item \texttt{string status = (score >= 5.0) ? "Đậu" : "Rớt";}
            \end{itemize}
        \end{itemize}
      \end{block}
    \end{column}

    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniNavy!5,colframe=UniNavy,title=\textbf{4 Nhóm Toán tử Nòng cốt Buổi 4},fonttitle=\small\bfseries]
        \begin{enumerate}\small
          \item \textbf{Nhóm 1: Toán tử số học nâng cao}
            \begin{itemize}\footnotesize
              \item Chia nguyên (\texttt{/}) vs Chia thực.
              \item Toán tử lấy phần dư (\texttt{\%}) và ứng dụng.
            \end{itemize}
          \item \textbf{Nhóm 2: Toán tử so sánh \& Logic}
            \begin{itemize}\footnotesize
              \item Phân biệt sống còn \texttt{=} và \texttt{==}.
              \item Cơ chế đoản mạch (\texttt{\&\&}, \texttt{||}).
            \end{itemize}
          \item \textbf{Nhóm 3: Toán tử tăng/giảm}
            \begin{itemize}\footnotesize
              \item Tiền tố (\texttt{++x}) vs Hậu tố (\texttt{x++}).
            \end{itemize}
          \item \textbf{Nhóm 4: Toán tử thao tác bit}
            \begin{itemize}\footnotesize
              \item \texttt{\&}, \texttt{|}, \texttt{\textasciicircum}, \texttt{\textasciitilde}, \texttt{<<}, \texttt{>>}.
            \end{itemize}
        \end{enumerate}
      \end{tcolorbox}
    \end{column}
  \end{columns}
\end{frame}

% ==============================================================================
% SLIDE 10: TOÁN TỬ SỐ HỌC: CHIA NGUYÊN VÀ MODULO
% ==============================================================================
\begin{frame}[fragile]{Toán Tử Số Học: Phép Chia Nguyên vs Chia Thực \& Modulo \%}
  \begin{columns}[T]
    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=AlertRed!10,colframe=AlertRed,title=\textbf{Cạm bẫy tử huyệt: Phép chia số nguyên},fonttitle=\small\bfseries]
\begin{lstlisting}[numbers=none]
// CA HAI TOAN HANG LA INT:
int a = 7;
int b = 2;
int div1 = a / b;       // div1 = 3 (cat cut!)
double div2 = a / b;    // div2 = 3.0 (VAN SAI!)

// GIAI PHAP: EP KIEU SANG SO THUC
double div3 = (double)a / b; // 3.5 (DUNG!)
double div4 = 7.0 / 2;       // 3.5 (DUNG!)
\end{lstlisting}
        \footnotesize \textbf{Quy tắc:} Nếu cả 2 toán hạng là số nguyên, kết quả luôn là số nguyên (phần thập phân bị loại bỏ hoàn toàn -- truncation).
      \end{tcolorbox}
    \end{column}

    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniGreen!10,colframe=UniGreen,title=\textbf{Ứng dụng thực tế của Modulo (\%)},fonttitle=\small\bfseries]
\begin{lstlisting}[numbers=none]
// 1. Kiem tra so chan / le
bool isEven = (n % 2 == 0);

// 2. Lay chu so hang don vi
int lastDigit = number % 10;

// 3. Quy doi giay sang giay le trong phut
int seconds = totalSeconds % 60;

// 4. Vong tron tuan hoan (Circular index)
index = (index + 1) % MAX_SLOTS;
\end{lstlisting}
        \footnotesize \textbf{Toán tử \texttt{\%}:} Trả về phần dư của phép chia. $7 \pmod 2 = 1$, $10 \pmod 3 = 1$.
      \end{tcolorbox}
    \end{column}
  \end{columns}
\end{frame}

% ==============================================================================
% SLIDE 11: TOÁN TỬ SO SÁNH: BẪY NHẦM LẪN = VÀ ==
% ==============================================================================
\begin{frame}[fragile]{Toán Tử So Sánh: Cảnh Báo Bẫy Tử Huyệt "=" và "=="}
  \begin{table}[h]
    \centering
    \small
    \begin{tabularx}{0.95\textwidth}{c l c c}
      \toprule
      \textbf{Toán tử} & \textbf{Ý nghĩa toán học} & \textbf{Ví dụ C\#} & \textbf{Kết quả (khi $x = 10, y = 20$)} \\
      \midrule
      \texttt{<} & Nhỏ hơn & \texttt{x < y} & \texttt{true} \\
      \texttt{<=} & Nhỏ hơn hoặc bằng & \texttt{x <= 10} & \texttt{true} \\
      \texttt{>} & Lớn hơn & \texttt{x > y} & \texttt{false} \\
      \texttt{>=} & Lớn hơn hoặc bằng & \texttt{y >= 25} & \texttt{false} \\
      \textbf{\texttt{==}} & \textbf{So sánh bằng} & \textbf{\texttt{x == y}} & \textbf{\texttt{false}} \\
      \texttt{!=} & Khác nhau (Không bằng) & \texttt{x != y} & \texttt{true} \\
      \bottomrule
    \end{tabularx}
  \end{table}

  \begin{columns}[T]
    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=AlertRed!10,colframe=AlertRed,title=\textbf{Lỗi kinh điển: Nhầm lẫn '=' và '=='},fonttitle=\small\bfseries]
        \begin{itemize}\footnotesize
          \item \texttt{=} : Toán tử \textbf{GÁN} (Lưu giá trị vào biến).
          \item \texttt{==} : Toán tử \textbf{SO SÁNH} (Trả về \texttt{true}/\texttt{false}).
          \item Trong C\#, viết \texttt{if (x = 5)} bị compiler chặn với lỗi \textbf{CS0029} (Cannot implicitly convert type 'int' to 'bool'). Đây là cơ chế bảo vệ an toàn của C\#!
        \end{itemize}
      \end{tcolorbox}
    \end{column}

    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniLightBlue!30,colframe=UniBlue,title=\textbf{So sánh số thực double với sai số Epsilon},fonttitle=\small\bfseries]
        \begin{itemize}\footnotesize
          \item Số thực dấu phẩy động (IEEE 754) luôn có sai số tính toán:
          \item \texttt{0.1 + 0.2 == 0.3} $\to$ \textbf{\texttt{false}}! (vì $0.1+0.2 = 0.30000000000000004$)
          \item \textbf{Cách so sánh chuẩn:}
            $$\text{Math.Abs}(a - b) < 1e-9$$
        \end{itemize}
      \end{tcolorbox}
    \end{column}
  \end{columns}
\end{frame}

% ==============================================================================
% SLIDE 12: TOÁN TỬ LOGIC VÀ BẢNG CHÂN TRỊ
% ==============================================================================
\begin{frame}{Toán Tử Logic (Boolean Operators) \& Bảng Chân Trị}
  \begin{columns}[T]
    \begin{column}{0.50\textwidth}
      \begin{table}[h]
        \centering
        \footnotesize
        \begin{tabular}{c c c c c}
          \toprule
          \textbf{A} & \textbf{B} & \textbf{A \&\& B} & \textbf{A || B} & \textbf{A \textasciicircum{} B} \\
          \midrule
          \texttt{false} & \texttt{false} & \texttt{false} & \texttt{false} & \texttt{false} \\
          \texttt{false} & \texttt{true}  & \texttt{false} & \texttt{true}  & \texttt{true}  \\
          \texttt{true}  & \texttt{false} & \texttt{false} & \texttt{true}  & \texttt{true}  \\
          \texttt{true}  & \texttt{true}  & \texttt{true}  & \texttt{true}  & \texttt{false} \\
          \bottomrule
        \end{tabular}
      \end{table}

      \begin{table}[h]
        \centering
        \footnotesize
        \begin{tabular}{c c}
          \toprule
          \textbf{A} & \textbf{!A (Phủ định)} \\
          \midrule
          \texttt{true} & \texttt{false} \\
          \texttt{false} & \texttt{true} \\
          \bottomrule
        \end{tabular}
      \end{table}
    \end{column}

    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniNavy!5,colframe=UniNavy,title=\textbf{Ý nghĩa thực tế trong Lập trình},fonttitle=\small\bfseries]
        \begin{itemize}\small
          \item \textbf{Phép VÀ (\texttt{\&\&}):} Đạt học bổng khi \texttt{gpa >= 3.6 \&\& renLuyen >= 80}. (Cả hai điều kiện đều phải thỏa mãn).
          \item \textbf{Phép HOẶC (\texttt{||}):} Được miễn thi khi \texttt{isGiaiQG || isIelts8}. (Chỉ cần một điều kiện đúng).
          \item \textbf{Phép PHỦ ĐỊNH (\texttt{!}):} \texttt{!isLoggedIn} (Nếu chưa đăng nhập thì chuyển sang màn hình Login).
          \item \textbf{Phép XOR (\texttt{\textasciicircum}):} Đúng khi một trong hai đúng nhưng không được cùng đúng.
        \end{itemize}
      \end{tcolorbox}
    \end{column}
  \end{columns}
\end{frame}

% ==============================================================================
% SLIDE 13: CƠ CHẾ ĐÁNH GIÁ ĐOẢN MẠCH (SHORT-CIRCUIT EVALUATION)
% ==============================================================================
\begin{frame}[fragile]{Cơ Chế Đánh Giá Đoản Mạch (Short-Circuit Evaluation)}
  \begin{alertblock}{\textbf{Bản chất cơ chế Đoản Mạch (Short-Circuit):}}
    Trong C\#, các toán tử \texttt{\&\&} và \texttt{||} thực hiện đánh giá lười (Lazy Evaluation): Nếu kết quả của toàn bộ biểu thức đã có thể xác định ngay từ vế trái, máy tính sẽ \textbf{BỎ QUA HOÀN TOÀN và KHÔNG BAO GIỜ TÍNH TOÁN vế phải}!
  \end{alertblock}

  \begin{columns}[T]
    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniGreen!10,colframe=UniGreen,title=\textbf{Đoản mạch VÀ (\&\&): Dừng khi gặp FALSE},fonttitle=\small\bfseries]
\begin{lstlisting}[numbers=none]
int b = 0;
// Neu b == 0, ve trai la FALSE.
// Ve phai (10 / b > 1) SE KHONG BAO GIO CHAY!
if (b != 0 && (10 / b > 1))
{
    Console.WriteLine("Phep chia an toan!");
}
// -> An toan 100%, tranh crash chia cho 0!
\end{lstlisting}
      \end{tcolorbox}
    \end{column}

    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniGreen!10,colframe=UniGreen,title=\textbf{Đoản mạch HOẶC (||): Dừng khi gặp TRUE},fonttitle=\small\bfseries]
\begin{lstlisting}[numbers=none]
bool isAdmin = true;
// Neu isAdmin la TRUE, toan bo bieu thuc la TRUE.
// Phuong thuc CheckDatabase() KHONG BI GOI!
if (isAdmin || CheckDatabase())
{
    Console.WriteLine("Quyen truy cap hop le!");
}
// -> Tiet kiem tai nguyen CPU va Database!
\end{lstlisting}
      \end{tcolorbox}
    \end{column}
  \end{columns}

  \begin{block}{\textbf{So sánh với toán tử \& và |:}}
    Toán tử \texttt{\&} và \texttt{|} \textbf{không đoản mạch}: Chúng bắt buộc tính toán cả 2 vế dù vế trái có là gì. Viết \texttt{if (b != 0 \& (10 / b > 1))} khi $b=0$ sẽ văng lỗi \textbf{DivideByZeroException} ngay lập tức!
  \end{block}
\end{frame}

% ==============================================================================
% SLIDE 14: TOÁN TỬ TĂNG/GIẢM: TIỀN TỐ VS HẬU TỐ
% ==============================================================================
\begin{frame}[fragile]{Toán Tử Tăng/Giảm: Tiền Tố (++x) vs Hậu Tố (x++)}
  \begin{columns}[T]
    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniLightBlue!30,colframe=UniBlue,title=\textbf{Toán tử Tiền tố (Prefix: ++x, --x)},fonttitle=\small\bfseries]
        \begin{itemize}\small
          \item \textbf{Cơ chế:} Giá trị biến được \textbf{TĂNG/GIẢM TRƯỚC}, sau đó giá trị mới được đưa vào biểu thức.
          \item \textbf{Khẩu quyết:} \textit{"Tăng trước rồi mới dùng!"}
        \end{itemize}
\begin{lstlisting}[numbers=none]
int a = 5;
int b = ++a; 
// 1. a tang len 6
// 2. Lay 6 gan cho b
// Ket qua: a = 6, b = 6
\end{lstlisting}
      \end{tcolorbox}
    \end{column}

    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=CSharpPurple!10,colframe=CSharpPurple,title=\textbf{Toán tử Hậu tố (Postfix: x++, x--)},fonttitle=\small\bfseries]
        \begin{itemize}\small
          \item \textbf{Cơ chế:} Giá trị \textbf{HIỆN TẠI} của biến được đưa vào biểu thức TRƯỚC, sau đó ô nhớ mới được \textbf{TĂNG/GIẢM}.
          \item \textbf{Khẩu quyết:} \textit{"Dùng giá trị cũ trước rồi mới tăng!"}
        \end{itemize}
\begin{lstlisting}[numbers=none]
int c = 5;
int d = c++; 
// 1. Lay 5 gan cho d truoc
// 2. c moi tang len 6
// Ket qua: c = 6, d = 5
\end{lstlisting}
      \end{tcolorbox}
    \end{column}
  \end{columns}

  \begin{center}
    \small \textbf{Tóm tắt trực quan:}\quad \texttt{int b = ++a;} $\implies a=6, b=6$ \quad$\Big|$\quad \texttt{int d = c++;} $\implies c=6, d=5$.
  \end{center}
\end{frame}

% ==============================================================================
% SLIDE 15: MỔ XẺ CƠ CHẾ Ô NHỚ RAM CỦA ++X VÀ X++
% ==============================================================================
\begin{frame}{Mổ Xẻ Cơ Chế Ô Nhớ RAM: Từng Bước Đánh Giá (Trace Step-by-Step)}
  \begin{center}
    \begin{tikzpicture}[scale=0.88, every node/.style={transform shape}]
      % Kịch bản 1: Tiền tố
      \node[draw=UniNavy, fill=UniLightBlue!30, font=\bfseries, minimum width=6.5cm, align=center] at (0, 3) {Kịch bản A: Tiền tố (\texttt{int b = ++a;})};
      \node[draw, rectangle, minimum width=1.5cm, minimum height=0.8cm, fill=white] (a1) at (-1.5, 1.8) {5};
      \node[above=0.1cm of a1, font=\scriptsize\bfseries] {Ô nhớ \texttt{a}};
      \node[draw, rectangle, minimum width=1.5cm, minimum height=0.8cm, fill=white] (b1) at (1.5, 1.8) {?};
      \node[above=0.1cm of b1, font=\scriptsize\bfseries] {Ô nhớ \texttt{b}};

      \draw[->, thick, red] (a1) to[bend left=30] node[above, font=\tiny\bfseries] {1. CPU tăng a $\to$ 6} (-1.5, 0.4);
      \node[draw, rectangle, minimum width=1.5cm, minimum height=0.8cm, fill=green!20] (a1_new) at (-1.5, 0.4) {6};
      \draw[->, thick, blue] (a1_new) -- node[above, font=\tiny\bfseries] {2. Ghi 6 vào b} (1.5, 0.4);
      \node[draw, rectangle, minimum width=1.5cm, minimum height=0.8cm, fill=green!20] (b1_new) at (1.5, 0.4) {6};

      % Vạch ngăn cách
      \draw[dashed, gray] (4, 3.2) -- (4, -0.5);

      % Kịch bản 2: Hậu tố
      \node[draw=CSharpPurple, fill=CSharpPurple!10, font=\bfseries, minimum width=6.5cm, align=center] at (8, 3) {Kịch bản B: Hậu tố (\texttt{int d = c++;})};
      \node[draw, rectangle, minimum width=1.5cm, minimum height=0.8cm, fill=white] (c1) at (6.5, 1.8) {5};
      \node[above=0.1cm of c1, font=\scriptsize\bfseries] {Ô nhớ \texttt{c}};
      \node[draw, rectangle, minimum width=1.5cm, minimum height=0.8cm, fill=white] (d1) at (9.5, 1.8) {?};
      \node[above=0.1cm of d1, font=\scriptsize\bfseries] {Ô nhớ \texttt{d}};

      \draw[->, thick, blue] (c1) -- node[above, font=\tiny\bfseries] {1. Ghi giá trị cũ (5) vào d} (9.5, 1.8);
      \node[draw, rectangle, minimum width=1.5cm, minimum height=0.8cm, fill=green!20] (d1_new) at (9.5, 0.4) {5};
      \draw[->, thick, red] (c1) to[bend left=30] node[left, font=\tiny\bfseries] {2. Sau đó tăng c $\to$ 6} (6.5, 0.4);
      \node[draw, rectangle, minimum width=1.5cm, minimum height=0.8cm, fill=green!20] (c1_new) at (6.5, 0.4) {6};
    \end{tikzpicture}
  \end{center}

  \begin{alertblock}{\textbf{Kết luận sống còn:}}
    Dù là \texttt{++x} hay \texttt{x++}, sau khi câu lệnh kết thúc thì biến \texttt{x} \textbf{luôn luôn tăng lên 1 đơn vị}. Sự khác nhau duy nhất nằm ở: \textbf{Giá trị được trả ra để tính toán biểu thức là giá trị mới hay giá trị cũ!}
  \end{alertblock}
\end{frame}

% ==============================================================================
% SLIDE 16: THỬ THÁCH CÂU HỎI BẪY: PHÂN TÍCH BIỂU THỨC PHỨC HỢP
% ==============================================================================
\begin{frame}[fragile]{Thử Thách Câu Hỏi Bẫy: Giải Mã Biểu Thức Tăng/Giảm Phức Hợp}
  \begin{exampleblock}{\textbf{Bài toán phỏng vấn kiểm tra bản chất:}}
    Đoạn mã C\# sau đây sẽ in ra màn hình giá trị của \texttt{result} và \texttt{x} bằng bao nhiêu?
\begin{lstlisting}[numbers=none]
int x = 10;
int result = x++ * 2 + ++x;
Console.WriteLine($"result = {result}, x = {x}");
\end{lstlisting}
  \end{exampleblock}

  \begin{tcolorbox}[colback=UniLightBlue!30,colframe=UniNavy,title=\textbf{Phân tích từng bước (Step-by-Step Tracing)},fonttitle=\small\bfseries]
    \begin{enumerate}\small
      \item Ban đầu: $x = 10$.
      \item Gặp toán hạng $x++$:
        \begin{itemize}\footnotesize
          \item Giá trị trả ra biểu thức là giá trị cũ: \textbf{10}.
          \item Ngay sau đó, ô nhớ $x$ được tăng lên: $x = 11$.
        \end{itemize}
      \item Phép nhân có độ ưu tiên cao hơn cộng: $10 \times 2 = \mathbf{20}$.
      \item Gặp toán hạng $++x$:
        \begin{itemize}\footnotesize
          \item Ô nhớ $x$ đang là 11, được tăng ngay lên: $x = 12$.
          \item Giá trị mới được trả ra biểu thức: \textbf{12}.
        \end{itemize}
      \item Thực hiện phép cộng: $20 + 12 = \mathbf{32}$.
      \item Gán kết quả: $\text{result} = 32$, giá trị cuối cùng của $x = 12$.
    \end{enumerate}
  \end{tcolorbox}
\end{frame}

% ==============================================================================
% SLIDE 17: CHECKPOINT TIẾT 1: MINI-QUIZ
% ==============================================================================
\begin{frame}[fragile]{Checkpoint Tiết 1: Trắc Nghiệm Củng Cố Nhận Thức}
  \begin{columns}[T]
    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniNavy!5,colframe=UniNavy,title=\textbf{Câu hỏi 1: Phép chia nguyên},fonttitle=\small\bfseries]
        Giá trị của biến \texttt{val} sau câu lệnh sau là gì?
        \texttt{double val = 9 / 2;}
        \begin{itemize}\footnotesize
          \item[A.] 4.5
          \item[B.] 4.0
          \item[C.] 4
          \item[D.] Báo lỗi biên dịch
        \end{itemize}
        \textbf{Đáp án:} \textcolor{UniGreen}{\textbf{B (4.0)}} (Chia nguyên $9/2=4$, sau đó gán vào double thành 4.0).
      \end{tcolorbox}

      \begin{tcolorbox}[colback=UniNavy!5,colframe=UniNavy,title=\textbf{Câu hỏi 2: Đoản mạch},fonttitle=\small\bfseries]
        Cho \texttt{int x = 5; bool res = (x > 10 \&\& ++x > 2);} Giá trị của \texttt{x} sau đó là:
        \begin{itemize}\footnotesize
          \item[A.] 5 \quad [B.] 6 \quad [C.] 11
        \end{itemize}
        \textbf{Đáp án:} \textcolor{UniGreen}{\textbf{A (5)}} (Vế trái sai $\to$ đoản mạch dừng lại, \texttt{++x} không chạy!).
      \end{tcolorbox}
    \end{column}

    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniNavy!5,colframe=UniNavy,title=\textbf{Câu hỏi 3: Tiền tố vs Hậu tố},fonttitle=\small\bfseries]
        Cho đoạn mã:
\begin{lstlisting}[numbers=none]
int p = 4;
int q = p++ + p++;
\end{lstlisting}
        Giá trị của \texttt{q} và \texttt{p} lần lượt là:
        \begin{itemize}\footnotesize
          \item[A.] $q = 8, p = 6$
          \item[B.] $q = 9, p = 6$
          \item[C.] $q = 10, p = 5$
          \item[D.] $q = 9, p = 5$
        \end{itemize}
        \textbf{Giải thích:} $p++$ đầu tiên trả về $4$ ($p$ thành $5$). $p++$ thứ hai trả về $5$ ($p$ thành $6$). Tổng $q = 4 + 5 = \mathbf{9}$, $p = \mathbf{6}$.\\
        \textbf{Đáp án:} \textcolor{UniGreen}{\textbf{B}}.
      \end{tcolorbox}
    \end{column}
  \end{columns}
\end{frame}

% ==============================================================================
% SLIDE 18: MỤC 2.11 - CÁC PHÉP TOÁN THAO TÁC BIT (BITWISE)
% ==============================================================================
\begin{frame}{Mục 2.11: Bản Chất Máy Tính: Hệ Nhị Phân \& Số Bù 2}
  \begin{block}{\textbf{Thế giới nhị phân bên trong máy vi tính:}}
    Mọi dữ liệu (số nguyên, số thực, văn bản, hình ảnh) trong máy tính đều được lưu trữ dưới dạng các dãy bit \textbf{0} và \textbf{1} (tương ứng hai trạng thái đóng/ngắt mạch điện).
    \begin{itemize}\small
      \item $1 \text{ Byte} = 8 \text{ bits}$. Kiểu \texttt{int} trong C\# chiếm \textbf{4 Bytes = 32 bits}.
      \item Bit ngoài cùng bên phải gọi là \textbf{LSB} (Least Significant Bit - Bit có trọng số thấp nhất).
      \item Bit ngoài cùng bên trái gọi là \textbf{MSB} (Most Significant Bit - Bit dấu: $0$ là số dương, $1$ là số âm).
    \end{itemize}
  \end{block}

  \begin{tcolorbox}[colback=UniLightBlue!30,colframe=UniBlue,title=\textbf{Biểu diễn số nguyên có dấu: Mã bù 2 (Two's Complement)},fonttitle=\small\bfseries]
    Để biểu diễn số âm $-X$ trong máy tính:
    \begin{enumerate}\small
      \item Lấy dạng nhị phân của số dương $X$.
      \item \textbf{Đảo tất cả các bit} (0 thành 1, 1 thành 0) $\to$ Thu được Mã bù 1.
      \item \textbf{Cộng thêm 1} vào kết quả $\to$ Thu được Mã bù 2 (Biểu diễn của $-X$).
    \end{enumerate}
    \textbf{Ví dụ với 8 bit:}
    Số $+5 = \texttt{0000 0101}_2 \implies \text{Đảo bit: } \texttt{1111 1010}_2 \implies \text{Cộng 1: } \texttt{1111 1011}_2 = -5$.
  \end{tcolorbox}
\end{frame}

% ==============================================================================
% SLIDE 19: TOÁN TỬ AND BIT (&) VÀ OR BIT (|)
% ==============================================================================
\begin{frame}[fragile]{Toán Tử Bitwise: AND Bit (\&) và OR Bit (|)}
  \begin{columns}[T]
    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniNavy!5,colframe=UniNavy,title=\textbf{Phép AND Bit (\&): Lọc / Xóa Bit},fonttitle=\small\bfseries]
        \textbf{Quy tắc:} Bit kết quả bằng \textbf{1} khi và chỉ khi CẢ HAI bit tương ứng đều bằng 1.
        \begin{table}[h]
          \centering
          \scriptsize
          \begin{tabular}{c c c}
            \toprule
            \textbf{Bit 1} & \textbf{Bit 2} & \textbf{Bit 1 \& Bit 2} \\
            \midrule
            0 & 0 & 0 \\
            0 & 1 & 0 \\
            1 & 0 & 0 \\
            1 & 1 & \textbf{1} \\
            \bottomrule
          \end{tabular}
        \end{table}
        \textbf{Tính toán cụ thể ($12 \ \& \ 10$):}
\begin{lstlisting}[numbers=none]
  12 = 0 0 0 0  1 1 0 0
& 10 = 0 0 0 0  1 0 1 0
------------------------
   8 = 0 0 0 0  1 0 0 0 (Ket qua: 8)
\end{lstlisting}
      \end{tcolorbox}
    \end{column}

    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=CSharpPurple!5,colframe=CSharpPurple,title=\textbf{Phép OR Bit (|): Bật / Gộp Bit},fonttitle=\small\bfseries]
        \textbf{Quy tắc:} Bit kết quả bằng \textbf{1} khi CÓ ÍT NHẤT MỘT trong hai bit bằng 1.
        \begin{table}[h]
          \centering
          \scriptsize
          \begin{tabular}{c c c}
            \toprule
            \textbf{Bit 1} & \textbf{Bit 2} & \textbf{Bit 1 | Bit 2} \\
            \midrule
            0 & 0 & 0 \\
            0 & 1 & \textbf{1} \\
            1 & 0 & \textbf{1} \\
            1 & 1 & \textbf{1} \\
            \bottomrule
          \end{tabular}
        \end{table}
        \textbf{Tính toán cụ thể ($12 \ | \ 10$):}
\begin{lstlisting}[numbers=none]
  12 = 0 0 0 0  1 1 0 0
| 10 = 0 0 0 0  1 0 1 0
------------------------
  14 = 0 0 0 0  1 1 1 0 (Ket qua: 14)
\end{lstlisting}
      \end{tcolorbox}
    \end{column}
  \end{columns}
\end{frame}

% ==============================================================================
% SLIDE 20: TOÁN TỬ XOR BIT (^) VÀ NOT BIT (~)
% ==============================================================================
\begin{frame}[fragile]{Toán Tử Bitwise: XOR Bit (\textasciicircum) và NOT Bit (\textasciitilde)}
  \begin{columns}[T]
    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniLightBlue!30,colframe=UniBlue,title=\textbf{Phép XOR Bit (\textasciicircum): Đảo Trạng Thái},fonttitle=\small\bfseries]
        \textbf{Quy tắc:} Bằng \textbf{1} khi 2 bit KHÁC NHAU; bằng \textbf{0} khi 2 bit GIỐNG NHAU.
\begin{lstlisting}[numbers=none]
  12 = 0 0 0 0  1 1 0 0
^ 10 = 0 0 0 0  1 0 1 0
------------------------
   6 = 0 0 0 0  0 1 1 0 (Ket qua: 6)
\end{lstlisting}
        \textbf{Tính chất kỳ diệu của XOR:}
        \begin{itemize}\footnotesize
          \item $A \oplus A = 0$ (XOR với chính mình bằng 0)
          \item $A \oplus 0 = A$ (XOR với 0 không đổi)
          \item $(A \oplus B) \oplus B = A$ (Ứng dụng mã hóa bảo mật đối xứng cơ bản!)
        \end{itemize}
      \end{tcolorbox}
    \end{column}

    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=AlertRed!10,colframe=AlertRed,title=\textbf{Phép NOT Bit (\textasciitilde): Đảo Tất Cả Bit},fonttitle=\small\bfseries]
        \textbf{Quy tắc:} Đổi toàn bộ bit 0 thành 1, bit 1 thành 0 (Bù 1).
\begin{lstlisting}[numbers=none]
int x = 5; // ...0000 0101
int y = ~x;
// ...1111 1010
// Trong he ma bu 2, gia tri la: -6!
\end{lstlisting}
        \begin{alertblock}{\textbf{Công thức bù 2 trong C\#:}}
          $$\mathbf{\sim x = -(x + 1)}$$
          Ví dụ: \texttt{\textasciitilde 5 = -6}, \texttt{\textasciitilde 0 = -1}, \texttt{\textasciitilde(-10) = 9}.
        \end{alertblock}
      \end{tcolorbox}
    \end{column}
  \end{columns}
\end{frame}

% ==============================================================================
% SLIDE 21: TOÁN TỬ DỊCH BIT (SHIFT OPERATORS: << VÀ >>)
% ==============================================================================
\begin{frame}[fragile]{Toán Tử Dịch Bit (Shift Operators): << và >>}
  \begin{columns}[T]
    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniGreen!10,colframe=UniGreen,title=\textbf{Dịch trái (Left Shift: \texttt{x << k})},fonttitle=\small\bfseries]
        \begin{itemize}\small
          \item Đẩy tất cả các bit sang trái $k$ vị trí.
          \item Các vị trí trống bên phải \textbf{luôn được chèn số 0}.
          \item \textbf{Ý nghĩa toán học:} Tương đương phép nhân:
            $$\mathbf{x \times 2^k}$$
        \end{itemize}
\begin{lstlisting}[numbers=none]
int x = 5; // 0000 0101 (5)
int r = x << 1; // 0000 1010 = 10 (5 * 2^1)
int s = x << 3; // 0010 1000 = 40 (5 * 2^3)
\end{lstlisting}
      \end{tcolorbox}
    \end{column}

    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniOrange!10,colframe=UniOrange,title=\textbf{Dịch phải (Right Shift: \texttt{x >> k})},fonttitle=\small\bfseries]
        \begin{itemize}\small
          \item Đẩy tất cả các bit sang phải $k$ vị trí.
          \item Số nguyên có dấu giữ nguyên bit dấu (Arithmetic shift).
          \item \textbf{Ý nghĩa toán học:} Tương đương phép chia nguyên:
            $$\mathbf{x / 2^k}$$
        \end{itemize}
\begin{lstlisting}[numbers=none]
int val = 40; // 0010 1000 (40)
int div1 = val >> 1; // 0001 0100 = 20 (40 / 2)
int div2 = val >> 3; // 0000 0101 = 5  (40 / 8)
\end{lstlisting}
      \end{tcolorbox}
    \end{column}
  \end{columns}

  \begin{exampleblock}{\textbf{Hiệu năng phần cứng:}}
    Phép dịch bit được vi xử lý (CPU) thực thi trong \textbf{1 chu kỳ xung nhịp (clock cycle)}, nhanh hơn nhiều so với mạch nhân và mạch chia số học!
  \end{exampleblock}
\end{frame}

% ==============================================================================
% SLIDE 22: ỨNG DỤNG KỸ THUẬT 1: THUẬT TOÁN TỐI ƯU VỚI BITWISE
% ==============================================================================
\begin{frame}[fragile]{Ứng Dụng Kỹ Thuật 1: Thuật Toán Tối Ưu Bằng Bitwise}
  \begin{columns}[T]
    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniLightBlue!30,colframe=UniBlue,title=\textbf{1. Kiểm tra Chẵn / Lẻ siêu tốc},fonttitle=\small\bfseries]
\begin{lstlisting}[numbers=none]
// Thay vi dung n % 2 == 0 cham hon:
if ((n & 1) == 0)
{
    Console.WriteLine("So Chan");
}
else
{
    Console.WriteLine("So Le");
}
\end{lstlisting}
        \footnotesize \textbf{Bản chất:} Mọi số lẻ đều có bit cuối cùng (LSB) là 1. Số chẵn có bit cuối là 0. AND với 1 sẽ cô lập bit cuối cùng này!
      \end{tcolorbox}
    \end{column}

    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=CSharpPurple!10,colframe=CSharpPurple,title=\textbf{2. Kiểm tra Số Lũy thừa của 2},fonttitle=\small\bfseries]
\begin{lstlisting}[numbers=none]
// Kiem tra n co dang 2^k (1, 2, 4, 8, 16...):
bool isPowerOfTwo = (n > 0) && ((n & (n - 1)) == 0);
\end{lstlisting}
        \footnotesize \textbf{Bản chất:} Lũy thừa của 2 chỉ có đúng duy nhất một bit 1 (ví dụ $8 = 1000_2$). Khi đó $n - 1$ đảo toàn bộ bit phía sau ($7 = 0111_2$). Phép AND sẽ triệt tiêu về 0!
      \end{tcolorbox}
    \end{column}
  \end{columns}

  \vspace{2mm}
  \begin{tcolorbox}[colback=UniGreen!10,colframe=UniGreen,title=\textbf{3. Hoán đổi 2 số không cần biến phụ (XOR Swap Trick)},fonttitle=\small\bfseries]
\begin{lstlisting}[numbers=none]
int a = 15, b = 27;
a = a ^ b; // a tam luu thong tin hoa tron
b = a ^ b; // b nhan lai gia tri ban dau cua a (27 ^ 15 ^ 27 = 15)
a = a ^ b; // a nhan lai gia tri ban dau cua b (27 ^ 15 ^ 15 = 27)
// Ket qua: a = 27, b = 15 ma khong ton 1 byte bo nho phu!
\end{lstlisting}
  \end{tcolorbox}
\end{frame}

% ==============================================================================
% SLIDE 23: ỨNG DỤNG KỸ THUẬT 2: KỸ THUẬT MẶT NẠ BIT (BITMASKING)
% ==============================================================================
\begin{frame}[fragile]{Ứng Dụng Kỹ Thuật 2: Mặt Nạ Bit (Bitmasking) \& Quản Lý Cờ Quyền Hạn}
  \begin{block}{\textbf{Bài toán thực tế trong Công nghiệp Phần mềm:}}
    Một tệp tin có 4 quyền: \textbf{Read (Đọc)}, \textbf{Write (Ghi)}, \textbf{Execute (Thực thi)}, \textbf{Delete (Xóa)}. Làm sao lưu toàn bộ 4 quyền này chỉ trong \textbf{1 số nguyên duy nhất} thay vì tạo 4 biến \texttt{bool}?
  \end{block}

  \begin{table}[h]
    \centering
    \small
    \begin{tabular}{l c c c}
      \toprule
      \textbf{Tên quyền (Permission Flag)} & \textbf{Biểu diễn nhị phân} & \textbf{Giá trị thập phân} & \textbf{Định nghĩa C\#} \\
      \midrule
      \texttt{READ} & \texttt{0000 0001} & 1 & \texttt{1 << 0} \\
      \texttt{WRITE} & \texttt{0000 0010} & 2 & \texttt{1 << 1} \\
      \texttt{EXECUTE} & \texttt{0000 0100} & 4 & \texttt{1 << 2} \\
      \texttt{DELETE} & \texttt{0000 1000} & 8 & \texttt{1 << 3} \\
      \bottomrule
    \end{tabular}
  \end{table}

  \begin{columns}[T]
    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniLightBlue!30,colframe=UniBlue,title=\textbf{4 Thao tác nòng cốt với Bitmask},fonttitle=\scriptsize\bfseries]
        \begin{itemize}\scriptsize
          \item \textbf{1. Bật bit (Set):} Dùng toán tử OR (\texttt{|})
          \item \textbf{2. Kiểm tra bit (Test):} Dùng toán tử AND (\texttt{\&})
          \item \textbf{3. Tắt bit (Clear):} Dùng AND với NOT (\texttt{\& \textasciitilde})
          \item \textbf{4. Đảo bit (Toggle):} Dùng toán tử XOR (\texttt{\textasciicircum})
        \end{itemize}
      \end{tcolorbox}
    \end{column}

    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=CodeBg,colframe=UniNavy,title=\textbf{Cú pháp mẫu C\#},fonttitle=\scriptsize\bfseries]
\begin{lstlisting}[numbers=none]
// Bat quyen WRITE
perm = perm | WRITE;
// Kiem tra co quyen READ khong?
bool canRead = (perm & READ) != 0;
// Tat quyen DELETE
perm = perm & (~DELETE);
\end{lstlisting}
      \end{tcolorbox}
    \end{column}
  \end{columns}
\end{frame}

% ==============================================================================
% SLIDE 24: MÃ NGUỒN MẪU: CHƯƠNG TRÌNH PHÂN QUYỀN VỚI BITWISE
% ==============================================================================
\begin{frame}[fragile]{Mã Nguồn Mẫu: Chương Trình Quản Lý Quyền Hạn Tệp Tin}
\begin{lstlisting}
using System;

class BitmaskPermissionsDemo
{
    static void Main()
    {
        Console.OutputEncoding = System.Text.Encoding.UTF8;
        const int READ = 1, WRITE = 2, EXECUTE = 4, DELETE = 8;
        int userPerm = 0; // Ban dau khong co quyen

        // 1. Cap quyen READ va WRITE cho nguoi dung
        userPerm = userPerm | READ | WRITE;
        Console.WriteLine($"Quyen hien tai: {Convert.ToString(userPerm, 2).PadLeft(4, '0')} (Thap phan: {userPerm})");

        // 2. Kiem tra xem co quyen WRITE khong?
        bool hasWrite = (userPerm & WRITE) != 0;
        Console.WriteLine($"Nguoi dung co quyen GHI khong? -> {hasWrite}");

        // 3. Tuoc (xoa) quyen WRITE
        userPerm = userPerm & (~WRITE);
        Console.WriteLine($"Sau khi tuoc quyen GHI: {Convert.ToString(userPerm, 2).PadLeft(4, '0')}");

        // 4. Toggle quyen EXECUTE (neu chua co thi bat, co roi thi tat)
        userPerm = userPerm ^ EXECUTE;
        Console.WriteLine($"Sau khi toggle EXECUTE: {Convert.ToString(userPerm, 2).PadLeft(4, '0')}");
    }
}
\end{lstlisting}
\end{frame}

% ==============================================================================
% SLIDE 25: CHECKPOINT TIẾT 2: THỰC HÀNH TẠI LỚP
% ==============================================================================
\begin{frame}[fragile]{Checkpoint Tiết 2: Thực Hành Thao Tác Bit Tại Lớp}
  \begin{tcolorbox}[colback=UniLightBlue!30,colframe=UniBlue,title=\textbf{Thử thách 5 phút: Viết biểu thức Bitwise},fonttitle=\small\bfseries]
    Cho một số nguyên \texttt{int N} và một vị trí bit \texttt{k} (từ 0 đến 31). Hãy viết các biểu thức C\# tương ứng cho các yêu cầu sau:
    \begin{enumerate}\small
      \item Tạo một mặt nạ bit (\texttt{mask}) chỉ có duy nhất bit thứ $k$ bằng 1.
      \item Kiểm tra xem bit thứ $k$ của số $N$ đang là 0 hay 1.
      \item Bật bit thứ $k$ của $N$ lên 1 (giữ nguyên các bit khác).
      \item Tắt bit thứ $k$ của $N$ về 0 (giữ nguyên các bit khác).
    \end{enumerate}
  \end{tcolorbox}

  \begin{tcolorbox}[colback=UniGreen!10,colframe=UniGreen,title=\textbf{Lời giải chuẩn xác từ Giảng viên},fonttitle=\small\bfseries]
\begin{lstlisting}[numbers=none]
// 1. Tao mask bit thu k:
int mask = 1 << k;

// 2. Kiem tra bit thu k:
bool isBitSet = (N & (1 << k)) != 0;

// 3. Bat bit thu k:
N = N | (1 << k);

// 4. Tat bit thu k:
N = N & (~(1 << k));
\end{lstlisting}
  \end{tcolorbox}
\end{frame}

% ==============================================================================
% SLIDE 26: MỤC 2.12 - CHUYỂN ĐỔI KIỂU DỮ LIỆU (TYPE CONVERSION)
% ==============================================================================
\begin{frame}{Mục 2.12: Bản Chất Hệ Thống Kiểu \& Tại Sao Cần Ép Kiểu?}
  \begin{block}{\textbf{C\# là Ngôn ngữ Kiểm tra Kiểu Tĩnh Mạnh Mẽ (Strongly-Typed):}}
    Trong C\#, mỗi biến bắt buộc phải có một kiểu dữ liệu cố định. Máy tính quản lý kích thước bộ nhớ và cách diễn giải nhị phân hoàn toàn khác nhau cho từng kiểu:
    \begin{itemize}\small
      \item \texttt{byte} (8 bit, 0 đến 255) $\ne$ \texttt{int} (32 bit, $-2 \times 10^9$ đến $+2 \times 10^9$).
      \item Số nguyên \texttt{int} (lưu bù 2) $\ne$ Số thực \texttt{double} (64 bit, lưu dấu phẩy động IEEE 754).
      \item Chuỗi ký tự \texttt{string} là một mảng văn bản Unicode trong bộ nhớ Heap.
    \end{itemize}
  \end{block}

  \begin{columns}[T]
    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniLightBlue!30,colframe=UniBlue,title=\textbf{Nhu cầu thực tế cần chuyển đổi kiểu},fonttitle=\small\bfseries]
        \begin{itemize}\footnotesize
          \item Người dùng nhập từ bàn phím luôn là \textbf{chuỗi ký tự} (\texttt{string}), phải đổi sang số để tính toán.
          \item Tính trung bình cộng của các số nguyên phải đưa về số thực (\texttt{double}).
          \item Tương tác với các thư viện cũ hoặc phần cứng yêu cầu kiểu nhỏ hơn (\texttt{byte}, \texttt{short}).
        \end{itemize}
      \end{tcolorbox}
    \end{column}

    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=CSharpPurple!10,colframe=CSharpPurple,title=\textbf{2 Cơ chế chuyển đổi cốt lõi},fonttitle=\small\bfseries]
        \begin{enumerate}\footnotesize
          \item \textbf{Ép kiểu Ngầm định (Implicit Widening):} Tự động chuyển đổi, 100\% an toàn, không mất dữ liệu.
          \item \textbf{Ép kiểu Tường minh (Explicit Narrowing):} Bắt buộc lập trình viên ra lệnh, tiềm ẩn rủi ro mất mát dữ liệu hoặc tràn số!
        \end{enumerate}
      \end{tcolorbox}
    \end{column}
  \end{columns}
\end{frame}

% ==============================================================================
% SLIDE 27: ÉP KIỂU NGẦM ĐỊNH (IMPLICIT WIDENING)
% ==============================================================================
\begin{frame}[fragile]{Ép Kiểu Ngầm Định (Implicit Type Conversion / Widening)}
  \begin{block}{\textbf{Nguyên tắc hoạt động:}}
    Xảy ra \textbf{hoàn toàn tự động} bởi trình biên dịch khi chuyển đổi từ một kiểu dữ liệu có \textbf{miền giá trị nhỏ hơn} sang kiểu dữ liệu có \textbf{miền giá trị lớn hơn} (Widening Conversion). Đảm bảo \textbf{không bao giờ bị mất mát dữ liệu}.
  \end{block}

  \begin{center}
    \begin{tikzpicture}[scale=0.9, every node/.style={transform shape}]
      \node[draw=UniNavy, fill=UniLightBlue!20, font=\bfseries] (byte) at (0,0) {\texttt{byte} (8b)};
      \node[draw=UniNavy, fill=UniLightBlue!30, font=\bfseries] (short) at (2.4,0) {\texttt{short} (16b)};
      \node[draw=UniNavy, fill=UniLightBlue!40, font=\bfseries] (int) at (4.8,0) {\texttt{int} (32b)};
      \node[draw=UniNavy, fill=UniLightBlue!60, font=\bfseries] (long) at (7.2,0) {\texttt{long} (64b)};
      \node[draw=CSharpPurple, fill=CSharpPurple!20, font=\bfseries] (float) at (9.6,0) {\texttt{float} (32b)};
      \node[draw=CSharpPurple, fill=CSharpPurple!40, font=\bfseries] (double) at (12.0,0) {\texttt{double} (64b)};

      \draw[->, thick, red] (byte) -- (short);
      \draw[->, thick, red] (short) -- (int);
      \draw[->, thick, red] (int) -- (long);
      \draw[->, thick, red] (long) -- (float);
      \draw[->, thick, red] (float) -- (double);
      
      \node[above=0.4cm of int, font=\scriptsize\bfseries, text=red] {Chiều chuyển đổi ngầm định an toàn (Tự động mở rộng)};
    \end{tikzpicture}
  \end{center}

  \begin{tcolorbox}[colback=CodeBg,colframe=UniNavy,title=\textbf{Mã nguồn minh họa ép kiểu ngầm định},fonttitle=\small\bfseries]
\begin{lstlisting}[numbers=none]
int numInt = 12345;
long numLong = numInt;    // Tu dong mo rong tu 32 bit len 64 bit (Hop le!)
double numDouble = numInt; // Tu dong chuyen tu so nguyen sang so thuc 12345.0 (Hop le!)
\end{lstlisting}
  \end{tcolorbox}
\end{frame}

% ==============================================================================
% SLIDE 28: ÉP KIỂU TƯỜNG MINH (EXPLICIT NARROWING)
% ==============================================================================
\begin{frame}[fragile]{Ép Kiểu Tường Minh (Explicit Narrowing / Cast Operator)}
  \begin{alertblock}{\textbf{Nguyên tắc hoạt động:}}
    Áp dụng khi chuyển từ kiểu có miền giá trị lớn sang kiểu nhỏ hơn, hoặc từ số thực sang số nguyên. Bắt buộc lập trình viên phải ghi rõ kiểu đích trong cặp ngoặc đơn: \texttt{(Kiểu\_Đích)biểu\_thức}.
  \end{alertblock}

  \begin{columns}[T]
    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=AlertRed!10,colframe=AlertRed,title=\textbf{Rủi ro 1: Mất độ chính xác (Precision Loss)},fonttitle=\small\bfseries]
\begin{lstlisting}[numbers=none]
double pi = 3.14159265;
int truncatedPi = (int)pi; 
// truncatedPi = 3
// TOAN BO PHAN THAP PHAN BI CAT CUT!
// Khong phai lam tron, ma la cat bo!
\end{lstlisting}
      \end{tcolorbox}
    \end{column}

    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=AlertRed!10,colframe=AlertRed,title=\textbf{Rủi ro 2: Tràn số âm thầm (Data Overflow)},fonttitle=\small\bfseries]
\begin{lstlisting}[numbers=none]
int largeNumber = 300;
// byte chi chua duoc tu 0 den 255
byte b = (byte)largeNumber; 
// b = 44! (300 % 256 = 44)
// DU LIEU BI SAI LECH HOAN TOAN!
\end{lstlisting}
      \end{tcolorbox}
    \end{column}
  \end{columns}

  \begin{exampleblock}{\textbf{Cảnh báo sư phạm:}}
    Chỉ thực hiện ép kiểu tường minh khi bạn chắc chắn 100\% giá trị đang nằm trong miền an toàn của kiểu đích, hoặc bạn cố tình muốn cắt bỏ phần thập phân!
  \end{exampleblock}
\end{frame}

% ==============================================================================
% SLIDE 29: SO SÁNH (TYPE) VS CONVERT VS PARSE
% ==============================================================================
\begin{frame}[fragile]{So Sánh Các Phương Pháp Chuyển Đổi Kiểu}
  \begin{table}[h]
    \centering
    \small
    \begin{tabularx}{\textwidth}{l p{3.6cm} p{3.4cm} p{3.4cm}}
      \toprule
      \textbf{Tiêu chí} & \textbf{Toán tử \texttt{(type)}} & \textbf{Lớp \texttt{Convert}} & \textbf{Phương thức \texttt{Parse()}} \\
      \midrule
      \textbf{Mục đích} & Ép kiểu trực tiếp giữa các kiểu số tương thích & Đa năng, chuyển đổi linh hoạt giữa nhiều kiểu & Chuyên chuyển từ chuỗi (\texttt{string}) sang kiểu số \\
      \addlinespace
      \textbf{Cắt thập phân} & \textbf{Cắt cụt} (\texttt{(int)3.9 = 3}) & \textbf{Làm tròn ngân hàng} (\texttt{Convert.ToInt32(3.9) = 4}) & Không áp dụng với chuỗi số thực \\
      \addlinespace
      \textbf{Xử lý \texttt{null}} & Lỗi biên dịch nếu kiểu nguyên thủy & \textbf{An toàn}: Trả về 0 & Văng ngoại lệ \texttt{ArgumentNullException} \\
      \addlinespace
      \textbf{Chuỗi sai định dạng} & Không hỗ trợ ép chuỗi sang số & Văng ngoại lệ \texttt{FormatException} & Văng ngoại lệ \texttt{FormatException} \\
      \bottomrule
    \end{tabularx}
  \end{table}

  \begin{exampleblock}{\textbf{Khái niệm Làm tròn ngân hàng (Banker's Rounding trong \texttt{Convert}):}}
    Nếu phần thập phân chính xác là $.5$, nó sẽ làm tròn về \textbf{số chẵn gần nhất}:
    \texttt{Convert.ToInt32(2.5)} $\to$ \textbf{2};\quad \texttt{Convert.ToInt32(3.5)} $\to$ \textbf{4}. Điều này giúp triệt tiêu sai số tích lũy trong tài chính.
  \end{exampleblock}
\end{frame}

% ==============================================================================
% SLIDE 30: KỸ THUẬT LẬP TRÌNH PHÒNG THỦ VỚI TRYPARSE
% ==============================================================================
\begin{frame}[fragile]{Kỹ Thuật Lập Trình Phòng Thủ: Phương Thức TryParse()}
  \begin{alertblock}{\textbf{Vấn đề của \texttt{int.Parse()}:}}
    Khi người dùng nhập chuỗi không hợp lệ (ví dụ: \texttt{"abc"}, \texttt{"12a"}), \texttt{int.Parse()} sẽ văng ngoại lệ làm \textbf{chương trình bị sập ngay lập tức (Crash)}!
  \end{alertblock}

  \begin{columns}[T]
    \begin{column}{0.52\textwidth}
      \begin{tcolorbox}[colback=UniGreen!10,colframe=UniGreen,title=\textbf{Giải pháp phòng thủ chuẩn mực: \texttt{int.TryParse()}},fonttitle=\small\bfseries]
\begin{lstlisting}[numbers=none]
Console.Write("Nhap tuoi cua ban: ");
string input = Console.ReadLine();

// Su dung TryParse de kiem tra an toan
if (int.TryParse(input, out int age) && age > 0)
{
    Console.WriteLine($"Tuoi hop le: {age}");
}
else
{
    Console.WriteLine("Loi: Vui long nhap so nguyen hop le!");
}
\end{lstlisting}
      \end{tcolorbox}
    \end{column}

    \begin{column}{0.44\textwidth}
      \begin{tcolorbox}[colback=UniLightBlue!30,colframe=UniBlue,title=\textbf{Giải mã cú pháp \texttt{TryParse}},fonttitle=\small\bfseries]
        \begin{itemize}\small
          \item \textbf{Giá trị trả về:} Kiểu \texttt{bool} (\texttt{true} nếu đổi thành công, \texttt{false} nếu thất bại).
          \item \textbf{Từ khóa \texttt{out}:} Nơi lưu trữ kết quả chuyển đổi nếu thành công.
          \item \textbf{Ưu thế tuyệt đối:} Không bao giờ văng lỗi ngoại lệ, giúp chương trình chạy ổn định 100\%.
        \end{itemize}
      \end{tcolorbox}
    \end{column}
  \end{columns}
\end{frame}

% ==============================================================================
% SLIDE 31: HIỂM HỌA TRÀN SỐ & KHỐI CHECKED / UNCHECKED
% ==============================================================================
\begin{frame}[fragile]{Hiểm Họa Tràn Số (Integer Overflow) \& Khối checked / unchecked}
  \begin{columns}[T]
    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=AlertRed!10,colframe=AlertRed,title=\textbf{Mặc định trong C\#: Tràn số âm thầm!},fonttitle=\small\bfseries]
\begin{lstlisting}[numbers=none]
int max = int.MaxValue; // 2,147,483,647
int result = max + 1;
Console.WriteLine(result); 
// IN RA: -2,147,483,648!
// So duong cong 1 thanh so am cuc dai!
\end{lstlisting}
        \footnotesize \textbf{Hậu quả:} Lỗ hổng bảo mật nghiêm trọng hoặc tính toán sai tiền tệ trong các hệ thống ngân hàng, thương mại điện tử!
      \end{tcolorbox}
    \end{column}

    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniGreen!10,colframe=UniGreen,title=\textbf{Giải pháp bảo vệ: Khối \texttt{checked}},fonttitle=\small\bfseries]
\begin{lstlisting}[numbers=none]
try
{
    checked
    {
        int max = int.MaxValue;
        int result = max + 1; // Phat hien tran so!
    }
}
catch (OverflowException ex)
{
    Console.WriteLine("Canh bao: Tran so he thong!");
}
\end{lstlisting}
        \footnotesize \textbf{Cơ chế:} Khối \texttt{checked} ép trình thực thi CLR ném ra \texttt{OverflowException} ngay khi xảy ra tràn số.
      \end{tcolorbox}
    \end{column}
  \end{columns}

  \begin{center}
    \small \textbf{Khối \texttt{unchecked}:} Bỏ qua kiểm tra tràn số để đạt hiệu năng tối đa (dùng khi bạn biết chắc hoặc cố tình quay vòng bit).
  \end{center}
\end{frame}

% ==============================================================================
% SLIDE 32: TỔNG KẾT 4 NGUYÊN TẮC VÀNG KHI CHUYỂN ĐỔI KIỂU
% ==============================================================================
\begin{frame}{Tổng Kết 4 Nguyên Tắc Vàng Khi Chuyển Đổi Kiểu Dữ Liệu}
  \begin{columns}[T]
    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniLightBlue!30,colframe=UniBlue,title=\textbf{Nguyên Tắc 1 \& 2},fonttitle=\small\bfseries]
        \begin{itemize}\small
          \item \textbf{1. Ưu tiên ép kiểu ngầm định (Widening):}
            Luôn để C\# tự động mở rộng kiểu dữ liệu khi chuyển từ kiểu nhỏ sang lớn. An toàn và không mất dữ liệu.
          \item \textbf{2. Ép kiểu số thực TRƯỚC phép chia:}
            Muốn phép chia có phần thập phân, bắt buộc ép kiểu ít nhất một toán hạng trước khi chia:
            $$\texttt{double avg = (double)sum / count;}$$
        \end{itemize}
      \end{tcolorbox}
    \end{column}

    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniGreen!10,colframe=UniGreen,title=\textbf{Nguyên Tắc 3 \& 4},fonttitle=\small\bfseries]
        \begin{itemize}\small
          \item \textbf{3. Luôn dùng \texttt{TryParse()} cho dữ liệu nhập:}
            Tuyệt đối không dùng \texttt{int.Parse()} trần trụi với dữ liệu từ bàn phím hoặc tệp tin bên ngoài để tránh crash chương trình.
          \item \textbf{4. Bọc các phép toán nhạy cảm trong \texttt{checked}:}
            Đối với các phép tính tài chính, tiền tệ, hoặc vòng lặp tính giai thừa/lũy thừa lớn, luôn dùng khối \texttt{checked} hoặc chuyển sang kiểu \texttt{long}/\texttt{decimal}.
        \end{itemize}
      \end{tcolorbox}
    \end{column}
  \end{columns}
\end{frame}

% ==============================================================================
% SLIDE 33: MỤC 2.13 - CÂU LỆNH GÁN VÀ BIỂU THỨC GÁN
% ==============================================================================
\begin{frame}[fragile]{Mục 2.13: Bản Chất Câu Lệnh Gán Đơn Thuần (=)}
  \begin{block}{\textbf{Cú pháp chuẩn mực:}}
    \centering \Large \texttt{variable = expression;}
  \end{block}

  \begin{columns}[T]
    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniLightBlue!30,colframe=UniBlue,title=\textbf{Quy luật thực thi của máy tính},fonttitle=\small\bfseries]
        \begin{enumerate}\small
          \item \textbf{Bước 1:} Toàn bộ biểu thức ở \textbf{vế phải (RHS)} được đánh giá và tính toán hoàn chỉnh trước.
          \item \textbf{Bước 2:} Kết quả vừa tính được \textbf{ghi đè vào vị trí ô nhớ} của biến ở \textbf{vế trái (LHS)}.
          \item \textbf{Quy tắc L-Value:} Vế trái bắt buộc phải là một biến (ô nhớ có thể ghi được).
        \end{enumerate}
      \end{tcolorbox}
    \end{column}

    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=AlertRed!10,colframe=AlertRed,title=\textbf{Các lỗi cú pháp kinh điển},fonttitle=\small\bfseries]
\begin{lstlisting}[numbers=none]
// LOI BIEN DICH (L-Value invalid):
10 = x;          // Sai! 10 la hang so
x + 5 = y;       // Sai! Ve trai la bieu thuc

// DUNG:
x = 10;
y = x + 5;
\end{lstlisting}
      \end{tcolorbox}
    \end{column}
  \end{columns}
\end{frame}

% ==============================================================================
% SLIDE 34: CÁC TOÁN TỬ GÁN PHỨC HỢP (COMPOUND ASSIGNMENTS)
% ==============================================================================
\begin{frame}[fragile]{Các Toán Tử Gán Phức Hợp (Compound Assignment Operators)}
  \begin{table}[h]
    \centering
    \small
    \begin{tabularx}{\textwidth}{c l l p{4cm}}
      \toprule
      \textbf{Toán tử} & \textbf{Ví dụ mã nguồn} & \textbf{Biểu thức tương đương} & \textbf{Ý nghĩa thực tế} \\
      \midrule
      \texttt{+=} & \texttt{sum += x;} & \texttt{sum = sum + x;} & Tích lũy tổng dồn \\
      \texttt{-=} & \texttt{balance -= fee;} & \texttt{balance = balance - fee;} & Trừ bớt số dư \\
      \texttt{*=} & \texttt{factorial *= i;} & \texttt{factorial = factorial * i;} & Tính tích lũy thừa / giai thừa \\
      \texttt{/=} & \texttt{n /= 10;} & \texttt{n = n / 10;} & Cắt bỏ chữ số cuối cùng \\
      \texttt{\%=} & \texttt{sec \%= 60;} & \texttt{sec = sec \% 60;} & Lấy số dư sau khi chia \\
      \texttt{\&=} & \texttt{flags \&= \textasciitilde WRITE;} & \texttt{flags = flags \& (\textasciitilde WRITE);} & Xóa cờ quyền hạn \\
      \texttt{|=} & \texttt{flags |= READ;} & \texttt{flags = flags | READ;} & Bật cờ quyền hạn \\
      \texttt{<<=} & \texttt{x <<= 2;} & \texttt{x = x << 2;} & Nhân nhanh cho 4 \\
      \texttt{>>=} & \texttt{x >>= 1;} & \texttt{x = x >> 1;} & Chia nguyên nhanh cho 2 \\
      \bottomrule
    \end{tabularx}
  \end{table}

  \begin{exampleblock}{\textbf{Lợi ích:}}
    Mã nguồn ngắn gọn, trực quan, giảm thiểu lỗi lặp lại tên biến và được trình biên dịch tối ưu hóa mã máy (CIL bytecode).
  \end{exampleblock}
\end{frame}

% ==============================================================================
% SLIDE 35: ĐIỂM TINH TẾ CỦA TOÁN TỬ GÁN PHỨC HỢP
% ==============================================================================
\begin{frame}[fragile]{Điểm Tinh Tế Của Toán Tử Gán Phức Hợp: Tự Động Ép Kiểu}
  \begin{alertblock}{\textbf{Hiện tượng thú vị mà 90\% người học C\# không để ý:}}
    Trong C\#, mọi phép toán số học giữa các kiểu nguyên nhỏ hơn \texttt{int} (\texttt{byte}, \texttt{short}) đều \textbf{tự động được nâng lên kiểu \texttt{int}} trước khi tính toán!
  \end{alertblock}

  \begin{columns}[T]
    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=AlertRed!10,colframe=AlertRed,title=\textbf{Cách viết thông thường (Bị lỗi!)} ,fonttitle=\small\bfseries]
\begin{lstlisting}[numbers=none]
byte b = 10;

// LOI BIEN DICH CS0266:
// Phep tinh (b + 5) cho ra kieu INT.
// Khong the gan nguoc lai cho BYTE!
b = b + 5; 

// Bat buoc phai ep kieu thu cong:
b = (byte)(b + 5);
\end{lstlisting}
      \end{tcolorbox}
    \end{column}

    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniGreen!10,colframe=UniGreen,title=\textbf{Dùng toán tử gán phức hợp (Hợp lệ 100\%!)},fonttitle=\small\bfseries]
\begin{lstlisting}[numbers=none]
byte b = 10;

// BIEN DICH THANH CONG 100%!
b += 5; 

// Ly do: C# tu dong chen ep kieu 
// ngam dinh ve kieu cua ve trai:
// b = (byte)(b + 5);
\end{lstlisting}
      \end{tcolorbox}
    \end{column}
  \end{columns}

  \begin{exampleblock}{\textbf{Kết luận kỹ thuật:}}
    Toán tử gán phức hợp \texttt{b += 5} không chỉ ngắn gọn hơn mà còn \textbf{tự động ép kiểu đích ngầm định}, giúp bạn viết mã nguồn sạch sẽ hơn!
  \end{exampleblock}
\end{frame}

% ==============================================================================
% SLIDE 36: BIỂU THỨC GÁN CHUỖI & HƯỚNG KẾT HỢP PHẢI-SANG-TRÁI
% ==============================================================================
\begin{frame}[fragile]{Biểu Thức Gán Chuỗi (Chained Assignment) \& Hướng Kết Hợp}
  \begin{block}{\textbf{Gán nhiều biến cùng lúc (Chained Assignment):}}
    Trong C\#, phép gán \texttt{=} bản thân nó cũng là \textbf{một biểu thức} và trả về giá trị của vế phải. Do đó, bạn có thể gán chuỗi:
    \centering \Large \texttt{a = b = c = 100;}
  \end{block}

  \begin{center}
    \begin{tikzpicture}[scale=0.9, every node/.style={transform shape}]
      \node[draw=UniNavy, fill=UniLightBlue!30, font=\Large\ttfamily, inner sep=10pt] (chain) at (0,0) {a = b = c = 100;};
      
      % Mũi tên từ phải sang trái
      \draw[->, very thick, red] (1.8, -0.6) -- node[below, font=\scriptsize\bfseries] {Bước 1: c = 100 (trả về 100)} (0.8, -0.6);
      \draw[->, very thick, blue] (0.7, -0.6) -- node[below, font=\scriptsize\bfseries] {Bước 2: b = 100 (trả về 100)} (-0.4, -0.6);
      \draw[->, very thick, UniGreen] (-0.5, -0.6) -- node[below, font=\scriptsize\bfseries] {Bước 3: a = 100} (-1.6, -0.6);
    \end{tikzpicture}
  \end{center}

  \begin{tcolorbox}[colback=CSharpPurple!10,colframe=CSharpPurple,title=\textbf{Hướng kết hợp từ Phải sang Trái (Right-to-Left Associativity)},fonttitle=\small\bfseries]
    Toán tử gán là một trong số ít các toán tử kết hợp từ \textbf{PHẢI SANG TRÁI}:
    $$\texttt{a = (b = (c = 100));}$$
    Biểu thức \texttt{c = 100} được thực thi trước $\implies$ kết quả 100 gán tiếp cho biến \texttt{b} $\implies$ kết quả gán tiếp cho biến \texttt{a}.
  \end{tcolorbox}
\end{frame}

% ==============================================================================
% SLIDE 37: BẢNG THỨ TỰ ƯU TIÊN TOÁN TỬ (OPERATOR PRECEDENCE)
% ==============================================================================
\begin{frame}{Bảng Thứ Tự Ưu Tiên Các Toán Tử (Từ Cao Xuống Thấp)}
  \begin{table}[h]
    \centering
    \scriptsize
    \begin{tabularx}{\textwidth}{c l p{5.5cm} l}
      \toprule
      \textbf{Cấp} & \textbf{Nhóm toán tử} & \textbf{Các toán tử trong nhóm} & \textbf{Hướng kết hợp} \\
      \midrule
      \textbf{1} & Toán tử chính (Primary) & \texttt{()}, \texttt{x++}, \texttt{x--}, truy cập thành viên \texttt{.} & Trái sang Phải \\
      \textbf{2} & Toán tử 1 ngôi (Unary) & \texttt{++x}, \texttt{--x}, \texttt{+x}, \texttt{-x}, \texttt{!}, \texttt{\textasciitilde}, \texttt{(type)} & \textbf{Phải sang Trái} \\
      \textbf{3} & Nhân / Chia / Lấy dư & \texttt{*}, \texttt{/}, \texttt{\%} & Trái sang Phải \\
      \textbf{4} & Cộng / Trừ & \texttt{+}, \texttt{-} & Trái sang Phải \\
      \textbf{5} & Dịch bit (Shift) & \texttt{<<}, \texttt{>>} & Trái sang Phải \\
      \textbf{6} & Quan hệ (Relational) & \texttt{<}, \texttt{<=}, \texttt{>}, \texttt{>=}, \texttt{is}, \texttt{as} & Trái sang Phải \\
      \textbf{7} & Bình đẳng (Equality) & \texttt{==}, \texttt{!=} & Trái sang Phải \\
      \textbf{8} & Bitwise AND, XOR, OR & \texttt{\&} sau đó đến \texttt{\textasciicircum} sau đó đến \texttt{|} & Trái sang Phải \\
      \textbf{9} & Logic AND, OR & \texttt{\&\&} sau đó đến \texttt{||} & Trái sang Phải \\
      \textbf{10} & Điều kiện (Ternary) & \texttt{? :} & \textbf{Phải sang Trái} \\
      \textbf{11} & Phép gán (Assignment) & \texttt{=}, \texttt{+=}, \texttt{-=}, \texttt{*=}, \texttt{/=}, \texttt{\%=}, \texttt{\&=}, \texttt{|=}, \texttt{<<=}, \dots & \textbf{Phải sang Trái} \\
      \bottomrule
    \end{tabularx}
  \end{table}
\end{frame}

% ==============================================================================
% SLIDE 38: HƯỚNG KẾT HỢP CỦA TOÁN TỬ (ASSOCIATIVITY)
% ==============================================================================
\begin{frame}[fragile]{Hướng Kết Hợp Của Toán Tử (Associativity)}
  \begin{block}{\textbf{Khái niệm Hướng kết hợp (Associativity):}}
    Khi hai toán tử có \textbf{CÙNG CẤP ĐỘ ƯU TIÊN} nằm cạnh nhau trong một biểu thức, hướng kết hợp sẽ quyết định toán tử nào được tính toán trước.
  \end{block}

  \begin{columns}[T]
    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniLightBlue!30,colframe=UniBlue,title=\textbf{Kết hợp từ Trái sang Phải (Left-to-Right)},fonttitle=\small\bfseries]
        Áp dụng cho đại đa số toán tử 2 ngôi (\texttt{+}, \texttt{-}, \texttt{*}, \texttt{/}, \texttt{\%}, \texttt{<<}, \texttt{\&\&}, \dots):
\begin{lstlisting}[numbers=none]
int result = 100 / 10 / 2;
// Phep tinh dien ra tu trai sang phai:
// (100 / 10) = 10
// Sau do: 10 / 2 = 5
// (Neu tu phai sang trai se ra 100 / 5 = 20 -> SAI!)
\end{lstlisting}
      \end{tcolorbox}
    \end{column}

    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=CSharpPurple!10,colframe=CSharpPurple,title=\textbf{Kết hợp từ Phải sang Trái (Right-to-Left)},fonttitle=\small\bfseries]
        Áp dụng cho: Toán tử 1 ngôi, Toán tử gán, Toán tử điều kiện \texttt{? :}:
\begin{lstlisting}[numbers=none]
// 1. Phep gan:
a = b = c = 10; // c=10 truoc -> b=10 -> a=10

// 2. Toan tu dieu kien long nhau:
int x = a > 0 ? 1 : b > 0 ? 2 : 3;
// Tuong duong: a > 0 ? 1 : (b > 0 ? 2 : 3)
\end{lstlisting}
      \end{tcolorbox}
    \end{column}
  \end{columns}
\end{frame}

% ==============================================================================
% SLIDE 39: QUY TẮC VÀNG DÙNG DẤU NGOẶC ĐƠN ()
% ==============================================================================
\begin{frame}[fragile]{Quy Tắc Vàng Của Kỹ Sư Phần Mềm: Luôn Dùng Ngoặc Đơn ()}
  \begin{alertblock}{\textbf{Đừng đánh đố trí nhớ của con người!}}
    Trong công nghiệp phát triển phần mềm, không ai khuyến khích lập trình viên phải "nhớ như in" 11 cấp độ ưu tiên của bảng toán tử để rồi viết những biểu thức mơ hồ, khó hiểu!
  \end{alertblock}

  \begin{columns}[T]
    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=AlertRed!10,colframe=AlertRed,title=\textbf{Biểu thức thiếu ngoặc (Code Smell - Dễ lỗi)},fonttitle=\small\bfseries]
\begin{lstlisting}[numbers=none]
// NGUY HIEM:
// Toan tu bitwise co uu tien THAP HON toan tu so sanh!
if (n & 1 == 0) 
// Compiler se danh gia (1 == 0) truoc!
// Tuong duong: if (n & false) -> LOI BIEN DICH!
\end{lstlisting}
      \end{tcolorbox}
    \end{column}

    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniGreen!10,colframe=UniGreen,title=\textbf{Biểu thức dùng ngoặc đơn (Chuẩn mực)},fonttitle=\small\bfseries]
\begin{lstlisting}[numbers=none]
// CHUAN MUC & AN TOAN 100%:
// Dung cap ngoac don de chi dinh ro rang:
if ((n & 1) == 0) 
{
    Console.WriteLine("So Chan");
}
// Ro rang, tuong minh, khong the loi!
\end{lstlisting}
      \end{tcolorbox}
    \end{column}
  \end{columns}

  \vspace{2mm}
  \begin{exampleblock}{\textbf{Châm ngôn kỹ thuật:}}
    \textit{"Explicit is better than implicit"} (Tường minh luôn tốt hơn ngầm định). Hãy hào phóng đặt dấu ngoặc đơn \texttt{()} để bảo vệ mã nguồn của bạn!
  \end{exampleblock}
\end{frame}

% ==============================================================================
% SLIDE 40: CASE STUDY TỔNG HỢP: ĐÁNH GIÁ BIỂU THỨC PHỨC HỢP
% ==============================================================================
\begin{frame}[fragile]{Case Study Tổng Hợp: Giải Phẫu Biểu Thức Phức Hợp}
  \begin{block}{\textbf{Bài toán đánh giá biểu thức:}}
    \centering \large \texttt{bool check = 5 + 3 * 2 > 10 \&\& (4 << 1) == 8;}
  \end{block}

  \begin{center}
    \begin{tikzpicture}[scale=0.88, every node/.style={transform shape}]
      % Các bước tính
      \node[draw=UniNavy, fill=UniLightBlue!20, font=\scriptsize\bfseries] (step1) at (-4, 2) {Bước 1: Ngoặc đơn};
      \node[below=0.1cm of step1, font=\tiny] {\texttt{(4 << 1) = 8}};

      \node[draw=UniNavy, fill=UniLightBlue!20, font=\scriptsize\bfseries] (step2) at (-1.3, 2) {Bước 2: Phép nhân};
      \node[below=0.1cm of step2, font=\tiny] {\texttt{3 * 2 = 6}};

      \node[draw=UniNavy, fill=UniLightBlue!20, font=\scriptsize\bfseries] (step3) at (1.3, 2) {Bước 3: Phép cộng};
      \node[below=0.1cm of step3, font=\tiny] {\texttt{5 + 6 = 11}};

      \node[draw=UniNavy, fill=UniLightBlue!20, font=\scriptsize\bfseries] (step4) at (4, 2) {Bước 4: So sánh >};
      \node[below=0.1cm of step4, font=\tiny] {\texttt{11 > 10 -> true}};

      \node[draw=UniNavy, fill=UniLightBlue!20, font=\scriptsize\bfseries] (step5) at (-2, 0.2) {Bước 5: So sánh ==};
      \node[below=0.1cm of step5, font=\tiny] {\texttt{8 == 8 -> true}};

      \node[draw=UniGreen, fill=UniGreen!20, font=\scriptsize\bfseries] (step6) at (2, 0.2) {Bước 6: Logic \&\&};
      \node[below=0.1cm of step6, font=\tiny] {\texttt{true \&\& true -> true}};

      \draw[->, thick, gray] (step1) to[bend left=15] (step5);
      \draw[->, thick, gray] (step2) -- (step3);
      \draw[->, thick, gray] (step3) -- (step4);
      \draw[->, thick, gray] (step4) to[bend left=15] (step6);
      \draw[->, thick, gray] (step5) -- (step6);
    \end{tikzpicture}
  \end{center}

  \begin{tcolorbox}[colback=UniLightBlue!30,colframe=UniNavy,title=\textbf{Kết quả thực thi},fonttitle=\small\bfseries]
    Biến \texttt{check} nhận giá trị \textbf{\texttt{true}}. Quá trình thực thi diễn ra tuần tự và chuẩn xác theo đúng cây cú pháp (Abstract Syntax Tree) của trình biên dịch C\#!
  \end{tcolorbox}
\end{frame}

% ==============================================================================
% SLIDE 41: THỬ THÁCH TẠI LỚP (MINI-CHALLENGE 10 PHÚT)
% ==============================================================================
\begin{frame}[fragile]{Thử Thách Tại Lớp: Mini-Challenge (10 Phút)}
  \begin{tcolorbox}[colback=UniOrange!10,colframe=UniOrange,title=\textbf{Đề bài Thực hành Mini-Challenge phòng máy},fonttitle=\small\bfseries]
    Hãy mở Visual Studio, tạo một Solution mới tên là \texttt{Buoi04\_MiniChallenge} và viết chương trình Console hoàn thành 4 yêu cầu sau:
    \begin{enumerate}\small
      \item Nhập vào từ bàn phím một số nguyên \texttt{N} bằng phương thức an toàn \texttt{int.TryParse()}.
      \item Kiểm tra \texttt{N} là số chẵn hay số lẻ bằng \textbf{Toán tử thao tác Bit} (\texttt{\& 1}).
      \item Sử dụng \textbf{phép dịch bit} để tính và in ra giá trị của $N \times 8$ (\texttt{<< 3}) và $N / 4$ (\texttt{>> 2}).
      \item Tính giá trị trung bình cộng của $N$ và $15$ dưới dạng \textbf{số thực chính xác} (ép kiểu tường minh).
      \item Viết một khối \texttt{try...catch} có chứa \texttt{checked} để thực hiện phép tính \texttt{int.MaxValue + N} và thông báo nếu xảy ra tràn số.
    \end{enumerate}
  \end{tcolorbox}
\end{frame}

% ==============================================================================
% SLIDE 42: LỜI GIẢI MẪU MINI-CHALLENGE
% ==============================================================================
\begin{frame}[fragile]{Lời Giải Mẫu Mini-Challenge}
\begin{lstlisting}
using System;

class MiniChallengeSolution
{
    static void Main()
    {
        Console.OutputEncoding = System.Text.Encoding.UTF8;
        Console.Write("Nhap so nguyen N: ");
        if (!int.TryParse(Console.ReadLine(), out int n))
        {
            Console.WriteLine("Du lieu khong hop le!"); return;
        }

        // 1. Kiem tra chan le bang Bitwise
        Console.WriteLine($"1. {n} la: {((n & 1) == 0 ? "So Chan" : "So Le")}");

        // 2. Nhan 8 va Chia 4 bang dich bit
        Console.WriteLine($"2. N * 8 = {n << 3}; N / 4 = {n >> 2}");

        // 3. Trung binh cong so thuc
        double avg = (n + 15) / 2.0;
        Console.WriteLine($"3. Trung binh cong voi 15: {avg:F2}");

        // 4. Kiem tra tran so voi checked
        try {
            checked { int overflowVal = int.MaxValue + n; }
        } catch (OverflowException) {
            Console.WriteLine("4. Canh bao: Xay ra tran so nguyen (Overflow)!");
        }
    }
}
\end{lstlisting}
\end{frame}

% ==============================================================================
% SLIDE 43: HỆ THỐNG BÀI TẬP TỰ LUYỆN VỀ NHÀ
% ==============================================================================
\begin{frame}{Hệ Thống Bài Tập Tự Luyện Về Nhà (Homework Projects)}
  \begin{columns}[T]
    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=UniLightBlue!30,colframe=UniBlue,title=\textbf{Bài 1: Công thức Hình học \& Vật lý},fonttitle=\small\bfseries]
        \begin{itemize}\small
          \item Tính khoảng cách Euclid giữa 2 điểm trong không gian 2D:
            $$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$
          \item Tính quãng đường và vận tốc rơi tự do sau $t$ giây ($g = 9.81 m/s^2$).
          \item \textit{Yêu cầu:} Dùng \texttt{double.TryParse()} an toàn.
        \end{itemize}
      \end{tcolorbox}

      \begin{tcolorbox}[colback=UniGreen!10,colframe=UniGreen,title=\textbf{Bài 2: Tối ưu Bitwise \& Flags},fonttitle=\small\bfseries]
        \begin{itemize}\small
          \item Viết chương trình hoán đổi 2 số bằng toán tử XOR (\texttt{\textasciicircum}).
          \item Xây dựng hệ thống quản lý cờ trạng thái sinh viên (Đã nộp học phí, Đã điểm danh, Cán bộ lớp).
        \end{itemize}
      \end{tcolorbox}
    \end{column}

    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=CSharpPurple!10,colframe=CSharpPurple,title=\textbf{Bài 3: Tài chính \& Kiểm soát Tràn số},fonttitle=\small\bfseries]
        \begin{itemize}\small
          \item Viết phần mềm tính tiền tiết kiệm gửi ngân hàng với số tiền hàng tỷ đồng.
          \item Áp dụng khối \texttt{checked} để cảnh báo nếu tính toán bị tràn số nguyên.
          \item Hướng dẫn so sánh kết quả khi dùng kiểu \texttt{int}, \texttt{long} và \texttt{decimal}.
        \end{itemize}
      \end{tcolorbox}

      \begin{tcolorbox}[colback=UniNavy!5,colframe=UniNavy,title=\textbf{Quy cách nộp bài},fonttitle=\small\bfseries]
        \begin{itemize}\small
          \item Nén thư mục Solution theo định dạng: \texttt{MSSV\_HoTen\_Buoi04.zip}.
          \item Đẩy lên kho lưu trữ cá nhân hoặc nộp qua Cổng học tập trực tuyến UDA.
        \end{itemize}
      \end{tcolorbox}
    \end{column}
  \end{columns}
\end{frame}

% ==============================================================================
% SLIDE 44: TỔNG KẾT CHUẨN ĐẦU RA & CẦU NỐI BUỔI 05
% ==============================================================================
\begin{frame}{Tổng Kết Chuẩn Đầu Ra \& Cầu Nối Sang Buổi 05}
  \begin{columns}[T]
    \begin{column}{0.50\textwidth}
      \begin{tcolorbox}[colback=UniLightBlue!30,colframe=UniBlue,title=\textbf{Checklist Hoàn thành Chuẩn đầu ra},fonttitle=\small\bfseries]
        \begin{itemize}\small
          \item[$\checkmark$] \textbf{CLO 4.1:} Hiểu bản chất biểu thức và chuyển đổi công thức thực tế sang C\#.
          \item[$\checkmark$] \textbf{CLO 4.2:} Phân biệt chia nguyên, phép gán \texttt{=}, so sánh \texttt{==}, đoản mạch và \texttt{++x} vs \texttt{x++}.
          \item[$\checkmark$] \textbf{CLO 4.3:} Nắm vững số bù 2, thao tác bit và kỹ thuật Bitmasking.
          \item[$\checkmark$] \textbf{CLO 4.4:} Làm chủ ép kiểu ngầm định/tường minh, \texttt{TryParse()} và xử lý tràn số với \texttt{checked}.
          \item[$\checkmark$] \textbf{CLO 4.5:} Vận dụng toán tử gán phức hợp và bảng thứ tự ưu tiên.
        \end{itemize}
      \end{tcolorbox}
    \end{column}

    \begin{column}{0.48\textwidth}
      \begin{tcolorbox}[colback=CSharpPurple!10,colframe=CSharpPurple,title=\textbf{Cầu nối sang Buổi 05 (Hàm \& Thủ tục)},fonttitle=\small\bfseries]
        \begin{itemize}\small
          \item \textbf{Vấn đề đặt ra:} Khi chương trình lớn dần, nếu viết hàng trăm dòng lệnh trong hàm \texttt{Main()} thì mã nguồn sẽ trở nên hỗn loạn, trùng lặp và cực kỳ khó sửa lỗi!
          \item \textbf{Giải pháp Buổi 05:}
            \begin{itemize}\footnotesize
              \item Tư duy "Chia để trị" (Divide and Conquer).
              \item Xây dựng và gọi \textbf{Hàm (Functions / Methods)}.
              \item Truyền tham số giá trị vs tham chiếu (\texttt{ref}, \texttt{out}).
            \end{itemize}
        \end{itemize}
      \end{tcolorbox}
    \end{column}
  \end{columns}

  \begin{center}
    \vspace{2mm}
    \large \textbf{CẢM ƠN CÁC EM SINH VIÊN LỚP IT26M ĐÃ THAM GIA BUỔI HỌC!}\\
    \small \color{gray} Chúc các em luyện tập tốt và hẹn gặp lại tại Buổi 05!
  \end{center}
\end{frame}

\end{document}
"""

out_file = os.path.join("Slides_CShape", "Slide_Buoi_04_NenTangLapTrinh_CSharp_IT26M.tex")
with open(out_file, "w", encoding="utf-8") as f:
    f.write(tex_content)

print(f"Successfully generated {out_file} ({len(tex_content)} chars)")
