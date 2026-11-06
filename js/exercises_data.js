// ============================================================================
// HỌC PHẦN: KỸ THUẬT LẬP TRÌNH (4 TÍN CHỈ) - IT26M
// BỘ DỮ LIỆU BÀI TẬP CUỐI CHƯƠNG 1 (BUILDING JAVA PROGRAMS - CH.1, P.103-135)
// GỒM 3 MỤC: SELF-CHECK PROBLEMS, EXERCISES, VÀ PROGRAMMING PROJECTS
// ============================================================================

const EXERCISES_CHAPTER_01 = [
  // ==========================================================================
  // PHẦN 1: SELF-CHECK PROBLEMS (TRANG 103 - 119)
  // ==========================================================================
  {
    id: "sc-1",
    type: "self-check",
    category: "1.1 Basic Computing Concepts",
    number: "Self-Check 1.1",
    page: 104,
    title: "Tại sao máy tính dùng số nhị phân?",
    description: "Giải thích tại sao các hệ thống máy tính hiện đại lại lưu trữ và xử lý thông tin dưới dạng các chuỗi số nhị phân (chỉ gồm các chữ số 0 và 1) thay vì sử dụng hệ thập phân quen thuộc?",
    hint: "Liên hệ cấu trúc vật lý của bóng bán dẫn (transistor) và điện áp trong mạch điện tử.",
    answer: "Máy tính được cấu tạo từ hàng tỷ vi mạch điện tử bán dẫn (transistor). Trong kỹ thuật điện tử, việc thiết kế mạch điện để nhận biết và duy trì ổn định hai trạng thái vật lý: 'BẬT / Điện áp cao' (đại diện cho bit 1) và 'TẮT / Điện áp thấp' (đại diện cho bit 0) là giải pháp đơn giản nhất, ít tiêu tốn năng lượng nhất và có khả năng chống nhiễu tín hiệu cực kỳ tin cậy so với việc phải phân biệt 10 mức điện áp khác nhau của hệ thập phân."
  },
  {
    id: "sc-2",
    type: "self-check",
    category: "1.1 Basic Computing Concepts",
    number: "Self-Check 1.2",
    page: 104,
    title: "Chuyển đổi số Thập phân sang Nhị phân",
    description: "Hãy chuyển đổi các số thập phân sau sang hệ nhị phân tương ứng:\na. 6\nb. 44\nc. 72\nd. 131",
    hint: "Sử dụng phương pháp phân tích theo lũy thừa của 2 hoặc chia liên tiếp cho 2 lấy phần dư.",
    answer: "a. 6 = 4 + 2 = (110)₂\nb. 44 = 32 + 8 + 4 = (101100)₂\nc. 72 = 64 + 8 = (1001000)₂\nd. 131 = 128 + 2 + 1 = (10000011)₂"
  },
  {
    id: "sc-3",
    type: "self-check",
    category: "1.1 Basic Computing Concepts",
    number: "Self-Check 1.3",
    page: 104,
    title: "Chuyển đổi số Nhị phân sang Thập phân",
    description: "Hãy xác định giá trị trong hệ thập phân của các số nhị phân sau:\na. 100₂\nb. 1011₂\nc. 101010₂\nd. 1001110₂",
    hint: "Nhân từng bit với trọng số 2^i tương ứng từ phải sang trái (bắt đầu từ 2^0).",
    answer: "a. 100₂ = 1×4 + 0×2 + 0×1 = 4\nb. 1011₂ = 1×8 + 0×4 + 1×2 + 1×1 = 11\nc. 101010₂ = 32 + 8 + 2 = 42\nd. 1001110₂ = 64 + 8 + 4 + 2 = 78"
  },
  {
    id: "sc-5",
    type: "self-check",
    category: "1.1 Basic Computing Concepts",
    number: "Self-Check 1.5",
    page: 105,
    title: "Phân biệt MyProgram.java và MyProgram.class",
    description: "Giải thích sự khác nhau về bản chất và mục đích sử dụng giữa file `MyProgram.java` và file `MyProgram.class`?",
    hint: "Mã nguồn do con người viết vs Mã bytecode cho máy ảo JVM thực thi.",
    answer: "- `MyProgram.java` là tệp mã nguồn văn bản thuần (plain text) do lập trình viên viết bằng cú pháp ngôn ngữ Java để con người đọc và chỉnh sửa.\n- `MyProgram.class` là tệp nhị phân chứa Java Bytecode được trình biên dịch `javac` sinh ra sau khi dịch tệp `.java`. Tệp này không dành cho người đọc mà dành cho máy ảo JVM nạp và thông dịch/JIT-compile sang mã máy để thực thi trên CPU."
  },
  {
    id: "sc-6",
    type: "self-check",
    category: "1.2 And Now—Java",
    number: "Self-Check 1.6",
    page: 105,
    title: "Nhận diện định danh (Identifiers) hợp lệ",
    description: "Trong các định danh sau, từ nào là hợp lệ trong Java? Nếu không hợp lệ, hãy giải thích lý do:\na. `miles`\nb. `Test`\nc. `a+b`\nd. `annual salary`\ne. `401k`\nf. `_average`\ng. `hi_there`\nh. `public`",
    hint: "Định danh chỉ gồm chữ cái, chữ số, _, $; không bắt đầu bằng số; không chứa dấu cách/phép toán; không trùng từ khóa.",
    answer: "- Hợp lệ: `miles`, `Test`, `_average`, `hi_there`.\n- KHÔNG hợp lệ:\n  + `a+b`: Chứa ký tự phép toán cộng `+`.\n  + `annual salary`: Chứa dấu cách (space).\n  + `401k`: Bắt đầu bằng chữ số (số 4).\n  + `public`: Trùng với từ khóa dành riêng (keyword) của Java."
  },
  {
    id: "sc-8",
    type: "self-check",
    category: "1.2 And Now—Java",
    number: "Self-Check 1.8",
    page: 106,
    title: "Dự đoán Output của Ký tự thoát (Escape Sequences)",
    description: "Đoạn mã sau sẽ in ra nội dung gì trên console?\n```java\nSystem.out.println(\"\\\\\\'\");\nSystem.out.println(\"\\\"\\\"\\\"\");\nSystem.out.println(\"C:\\nin\\the\\file.txt\");\n```",
    hint: "Chú ý \\\\ in 1 gạch chéo ngược, \\\" in nháy kép, \\n xuống dòng, \\t thụt lề tab.",
    answer: "Kết quả in ra chính xác:\n\\'\n\"\"\"\nC:\nin\the\file.txt"
  },
  {
    id: "sc-18",
    type: "self-check",
    category: "1.3 Program Errors",
    number: "Self-Check 1.18",
    page: 110,
    title: "Thám tử phát hiện 3 lỗi trong MyProgram",
    description: "Chỉ ra chính xác 3 lỗi cú pháp trong chương trình sau:\n```java\n1  public MyProgram {\n2      public static void main(String[] args) {\n3          System.out.println(\"This is a test;\n4          System.out.println(\"It contains two lines\");\n5      }\n6  }\n```",
    hint: "Kiểm tra khai báo lớp ở dòng 1 và chuỗi văn bản ở dòng 3.",
    answer: "1. Lỗi dòng 1: Thiếu từ khóa `class` giữa `public` và `MyProgram` (phải là `public class MyProgram`).\n2. Lỗi dòng 3: Chuỗi ký tự thiếu dấu ngoặc kép đóng `\"`.\n3. Lỗi dòng 3: Câu lệnh thiếu dấu ngoặc đơn đóng `)` trước dấu chấm phẩy (phải là `System.out.println(\"This is a test;\");`)."
  },
  {
    id: "sc-26",
    type: "self-check",
    category: "1.4 Procedural Decomposition",
    number: "Self-Check 1.26",
    page: 115,
    title: "Lần vết luồng điều khiển của hàm Confusing",
    description: "Xác định thứ tự in chính xác của chương trình sau khi chạy:\n```java\npublic class Confusing {\n    public static void method1() {\n        System.out.println(\"I am method 1.\");\n    }\n    public static void method2() {\n        method1();\n        System.out.println(\"I am method 2.\");\n    }\n    public static void method3() {\n        method2();\n        System.out.println(\"I am method 3.\");\n        method1();\n    }\n    public static void main(String[] args) {\n        method1();\n        method3();\n        method2();\n        method3();\n    }\n}\n```",
    hint: "Lần vết Call Stack từng lời gọi hàm từ main.",
    answer: "Kết quả in ra tuần tự gồm 11 dòng:\nI am method 1.\nI am method 1.\nI am method 2.\nI am method 3.\nI am method 1.\nI am method 1.\nI am method 2.\nI am method 1.\nI am method 2.\nI am method 3.\nI am method 1."
  },

  // ==========================================================================
  // PHẦN 2: EXERCISES - BÀI TẬP LẬP TRÌNH CỐT LÕI (TRANG 120 - 129)
  // ==========================================================================
  {
    id: "ex-1",
    type: "exercise",
    category: "Cú pháp & Chuỗi ký tự",
    number: "Exercise 1.1",
    page: 120,
    title: "Bài tập Stewie (In khối văn bản đặc biệt)",
    description: "Viết một chương trình Java hoàn chỉnh tên là `Stewie.java` in ra màn hình chính xác đoạn văn bản sau:\n```\n//////////////////////\n|| Victory is mine! ||\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n```",
    expectedOutput: "//////////////////////\n|| Victory is mine! ||\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\",
    hint: "Dấu gạch chéo xuôi `/` không cần escape, nhưng mỗi dấu gạch chéo ngược `\\` bắt buộc phải viết thành `\\\\`.",
    starterCode: `public class Stewie {
    public static void main(String[] args) {
        // TODO: In 22 dấu gạch chéo xuôi
        // TODO: In dòng || Victory is mine! ||
        // TODO: In 22 dấu gạch chéo ngược
    }
}`,
    solutionCode: `public class Stewie {
    public static void main(String[] args) {
        System.out.println("//////////////////////");
        System.out.println("|| Victory is mine! ||");
        System.out.println("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\");
    }
}`
  },
  {
    id: "ex-2",
    type: "exercise",
    category: "Cú pháp & Ký tự thoát",
    number: "Exercise 1.2",
    page: 120,
    title: "Bài tập Spikey (Đồ họa mũi tên gai ASCII)",
    description: "Viết chương trình `Spikey.java` in ra hình khối gai đối xứng sau:\n```\n  \\/\n \\\\//\n\\\\\\///\n///\\\\\\\n ///\\\\\n  /\\\n```",
    expectedOutput: "  \\/\n \\\\//\n\\\\\\///\n///\\\\\\\n ///\\\\\n  /\\",
    hint: "Đếm cẩn thận số lượng dấu cách ở đầu mỗi dòng và nhớ gấp đôi dấu gạch chéo ngược `\\` thành `\\\\`.",
    starterCode: `public class Spikey {
    public static void main(String[] args) {
        // Viết các câu lệnh println tại đây
    }
}`,
    solutionCode: `public class Spikey {
    public static void main(String[] args) {
        System.out.println("  \\/");
        System.out.println(" \\\\//");
        System.out.println("\\\\\\///");
        System.out.println("///\\\\\\");
        System.out.println(" ///\\\\");
        System.out.println("  /\\");
    }
}`
  },
  {
    id: "ex-3",
    type: "exercise",
    category: "Cú pháp cơ bản",
    number: "Exercise 1.3",
    page: 120,
    title: "Bài tập WellFormed (Đặc tả chương trình Java chuẩn)",
    description: "Viết chương trình `WellFormed.java` in ra đoạn văn bản mô tả cấu trúc chương trình Java:\n```\nA well-formed Java program has\na main method with { and }\nbraces.\n\nA System.out.println statement\nhas ( and ) and usually a\nString that starts and ends\nwith a \" character.\n(But we type \\\" instead!)\n```",
    expectedOutput: "A well-formed Java program has\na main method with { and }\nbraces.\n\nA System.out.println statement\nhas ( and ) and usually a\nString that starts and ends\nwith a \" character.\n(But we type \\\" instead!)",
    hint: "Sử dụng println() không tham số để tạo dòng trống và dùng \\\" để in dấu nháy kép, \\\\ để in dấu gạch chéo.",
    starterCode: `public class WellFormed {
    public static void main(String[] args) {
        // Viết các lệnh xuất văn bản
    }
}`,
    solutionCode: `public class WellFormed {
    public static void main(String[] args) {
        System.out.println("A well-formed Java program has");
        System.out.println("a main method with { and }");
        System.out.println("braces.");
        System.out.println();
        System.out.println("A System.out.println statement");
        System.out.println("has ( and ) and usually a");
        System.out.println("String that starts and ends");
        System.out.println("with a \" character.");
        System.out.println("(But we type \\\" instead!)");
    }
}`
  },
  {
    id: "ex-7",
    type: "exercise",
    category: "Phân rã thủ tục",
    number: "Exercise 1.7",
    page: 122,
    title: "Bài tập Mantra (In câu thần chú bằng phương thức tĩnh)",
    description: "Viết chương trình `Mantra.java` in ra câu thần chú sau 2 lần, cách nhau 1 dòng trống. Bắt buộc phải sử dụng ít nhất một phương thức tĩnh ngoài hàm `main` để thể hiện cấu trúc:\n```\nThere's one thing every coder must understand:\nThe System.out.println command.\n\nThere's one thing every coder must understand:\nThe System.out.println command.\n```",
    expectedOutput: "There's one thing every coder must understand:\nThe System.out.println command.\n\nThere's one thing every coder must understand:\nThe System.out.println command.",
    hint: "Tạo phương thức static void printMantra() chứa 2 lệnh in, sau đó gọi phương thức này 2 lần trong main.",
    starterCode: `public class Mantra {
    public static void main(String[] args) {
        // Gọi phương thức tại đây
    }
    
    // Khai báo phương thức tĩnh phụ tại đây
}`,
    solutionCode: `public class Mantra {
    public static void main(String[] args) {
        printMantra();
        System.out.println();
        printMantra();
    }

    public static void printMantra() {
        System.out.println("There's one thing every coder must understand:");
        System.out.println("The System.out.println command.");
    }
}`
  },
  {
    id: "ex-11",
    type: "exercise",
    category: "Phân rã thủ tục & DRY",
    number: "Exercise 1.11",
    page: 124,
    title: "Bài tập TwoRockets (Vẽ 2 tên lửa đứng cạnh nhau)",
    description: "Viết chương trình `TwoRockets.java` vẽ hai tên lửa đứng song song cạnh nhau như sau. Áp dụng phân rã thủ tục để loại bỏ trùng lặp:\n```\n   /\\       /\\\n  /  \\     /  \\\n /    \\   /    \\\n+------+ +------+\n|      | |      |\n|      | |      |\n+------+ +------+\n|United| |United|\n|States| |States|\n+------+ +------+\n|      | |      |\n|      | |      |\n+------+ +------+\n   /\\       /\\\n  /  \\     /  \\\n /    \\   /    \\\n```",
    expectedOutput: "   /\\       /\\\n  /  \\     /  \\\n /    \\   /    \\\n+------+ +------+\n|      | |      |\n|      | |      |\n+------+ +------+\n|United| |United|\n|States| |States|\n+------+ +------+\n|      | |      |\n|      | |      |\n+------+ +------+\n   /\\       /\\\n  /  \\     /  \\\n /    \\   /    \\",
    hint: "Tạo các phương thức: drawCones(), drawBoxSegment(), drawUnitedStates(). Lưu ý in cả hai tên lửa trên cùng một dòng lệnh println.",
    starterCode: `public class TwoRockets {
    public static void main(String[] args) {
        // Tổ chức lời gọi hàm
    }
}`,
    solutionCode: `public class TwoRockets {
    public static void main(String[] args) {
        drawCones();
        drawBoxSegment();
        drawUnitedStates();
        drawBoxSegment();
        drawCones();
    }

    public static void drawCones() {
        System.out.println("   /\\       /\\");
        System.out.println("  /  \\     /  \\");
        System.out.println(" /    \\   /    \\");
    }

    public static void drawBoxSegment() {
        System.out.println("+------+ +------+");
        System.out.println("|      | |      |");
        System.out.println("|      | |      |");
        System.out.println("+------+ +------+");
    }

    public static void drawUnitedStates() {
        System.out.println("|United| |United|");
        System.out.println("|States| |States|");
        System.out.println("+------+ +------+");
    }
}`
  },
  {
    id: "ex-12",
    type: "exercise",
    category: "Phân rã thủ tục & DRY",
    number: "Exercise 1.12",
    page: 125,
    title: "Bài tập FightSong (Bài hát cổ động)",
    description: "Viết chương trình `FightSong.java` in lời bài hát sau. Sử dụng ít nhất hai phương thức tĩnh phụ để thể hiện cấu trúc và triệt tiêu hoàn toàn sự trùng lặp (nguyên lý DRY):\n```\nGo, team, go!\nYou can do it.\n\nGo, team, go!\nYou can do it.\nYou're the best,\nIn the West.\nGo, team, go!\nYou can do it.\n\nGo, team, go!\nYou can do it.\nYou're the best,\nIn the West.\nGo, team, go!\nYou can do it.\n\nGo, team, go!\nYou can do it.\n```",
    expectedOutput: "Go, team, go!\nYou can do it.\n\nGo, team, go!\nYou can do it.\nYou're the best,\nIn the West.\nGo, team, go!\nYou can do it.\n\nGo, team, go!\nYou can do it.\nYou're the best,\nIn the West.\nGo, team, go!\nYou can do it.\n\nGo, team, go!\nYou can do it.",
    hint: "Phân rã thành 2 phương thức cơ bản: singGoTeam() và singMiddleChorus(), kết hợp phương thức singStanza().",
    starterCode: `public class FightSong {
    public static void main(String[] args) {
        // Viết cấu trúc điều khiển
    }
}`,
    solutionCode: `public class FightSong {
    public static void main(String[] args) {
        singGoTeam();
        System.out.println();
        singVerse();
        System.out.println();
        singVerse();
        System.out.println();
        singGoTeam();
    }

    public static void singVerse() {
        singGoTeam();
        singBestInWest();
        singGoTeam();
    }

    public static void singGoTeam() {
        System.out.println("Go, team, go!");
        System.out.println("You can do it.");
    }

    public static void singBestInWest() {
        System.out.println("You're the best,");
        System.out.println("In the West.");
    }
}`
  },
  {
    id: "ex-13",
    type: "exercise",
    category: "Phân rã thủ tục",
    number: "Exercise 1.13",
    page: 126,
    title: "Bài tập StarFigures (Vẽ các hình ngôi sao)",
    description: "Viết chương trình `StarFigures.java` vẽ 3 cụm hình ngôi sao như sau, loại bỏ mọi sự trùng lặp mã lệnh:\n```\n*****\n*****\n * *\n  *\n * *\n\n*****\n*****\n * *\n  *\n * *\n*****\n*****\n\n  *\n  *\n  *\n*****\n*****\n * *\n  *\n * *\n```",
    expectedOutput: "Đồ họa ASCII hình ngôi sao 3 cụm.",
    hint: "Nhận diện 3 khối nguyên tử: cụm 2 dòng 5 sao, cụm hình tia X (* * / * / * *), và cột 3 sao thẳng đứng.",
    starterCode: `public class StarFigures {
    public static void main(String[] args) {
        // Cấu trúc phân rã
    }
}`,
    solutionCode: `public class StarFigures {
    public static void main(String[] args) {
        figure1();
        System.out.println();
        figure2();
        System.out.println();
        figure3();
    }

    public static void figure1() {
        twoLines();
        xShape();
    }

    public static void figure2() {
        figure1();
        twoLines();
    }

    public static void figure3() {
        verticalLine();
        figure1();
    }

    public static void twoLines() {
        System.out.println("*****");
        System.out.println("*****");
    }

    public static void xShape() {
        System.out.println(" * *");
        System.out.println("  *");
        System.out.println(" * *");
    }

    public static void verticalLine() {
        System.out.println("  *");
        System.out.println("  *");
        System.out.println("  *");
    }
}`
  },
  {
    id: "ex-14",
    type: "exercise",
    category: "Phân rã thủ tục",
    number: "Exercise 1.14",
    page: 127,
    title: "Bài tập Lanterns (Vẽ đèn lồng lồng ghép)",
    description: "Viết chương trình `Lanterns.java` vẽ 3 chiếc đèn lồng hình tháp ngôi sao bằng cách phân rã cấu trúc theo mô hình đa cấp:\n```\n    *****\n  ********* \n*************\n\n    *****\n  ********* \n*************\n* | | | | | *\n*************\n    *****\n  ********* \n*************\n\n    *****\n  ********* \n*************\n    *****\n* | | | | | *\n* | | | | | *\n    *****\n    *****\n```",
    expectedOutput: "3 đèn lồng dạng tháp phân tầng.",
    hint: "Tách khối nón 3 tầng thành drawCone(), khối thanh chắn thành drawBars().",
    starterCode: `public class Lanterns {
    public static void main(String[] args) {
        // Gọi các tầng đèn lồng
    }
}`,
    solutionCode: `public class Lanterns {
    public static void main(String[] args) {
        drawCone();
        System.out.println();
        
        drawCone();
        drawBars();
        drawWideLine();
        drawCone();
        System.out.println();

        drawCone();
        drawShortLine();
        drawBars();
        drawBars();
        drawShortLine();
        drawShortLine();
    }

    public static void drawCone() {
        drawShortLine();
        System.out.println("  *********");
        drawWideLine();
    }

    public static void drawShortLine() {
        System.out.println("    *****");
    }

    public static void drawWideLine() {
        System.out.println("*************");
    }

    public static void drawBars() {
        System.out.println("* | | | | | *");
    }
}`
  },

  // ==========================================================================
  // PHẦN 3: PROGRAMMING PROJECTS - ĐỒ ÁN LẬP TRÌNH MINI (TRANG 130 - 135)
  // ==========================================================================
  {
    id: "proj-1",
    type: "project",
    category: "Đồ án Mini 1",
    number: "Project 1.1",
    page: 130,
    title: "Chương trình MISSISSIPPI (In chữ cái khối lớn)",
    description: "Viết chương trình `Mississippi.java` đánh vần từ MISSISSIPPI bằng các chữ cái dạng khối lớn (Block letters) cao 7 dòng. Yêu cầu thiết kế phương thức riêng cho mỗi chữ cái (M, I, S, P) và tái sử dụng triệt để.",
    expectedOutput: "M     M\nMM   MM\nM M M M\nM  M  M\nM     M\nM     M\nM     M\n\n(Tiếp tục với I, S, S, I, S, S, I, P, P, I)",
    hint: "Viết các phương thức: printM(), printI(), printS(), printP(). Trong main gọi: printM(); printI(); printS(); printS(); printI(); printS(); printS(); printI(); printP(); printP(); printI();",
    starterCode: `public class Mississippi {
    public static void main(String[] args) {
        // Đánh vần M-I-S-S-I-S-S-I-P-P-I
    }

    // Các phương thức in chữ khối M, I, S, P
}`,
    solutionCode: `public class Mississippi {
    public static void main(String[] args) {
        printM();
        printI();
        printS();
        printS();
        printI();
        printS();
        printS();
        printI();
        printP();
        printP();
        printI();
    }

    public static void printM() {
        System.out.println("M     M");
        System.out.println("MM   MM");
        System.out.println("M M M M");
        System.out.println("M  M  M");
        System.out.println("M     M");
        System.out.println("M     M");
        System.out.println("M     M");
        System.out.println();
    }

    public static void printI() {
        System.out.println("IIIII");
        System.out.println("  I  ");
        System.out.println("  I  ");
        System.out.println("  I  ");
        System.out.println("  I  ");
        System.out.println("  I  ");
        System.out.println("IIIII");
        System.out.println();
    }

    public static void printS() {
        System.out.println(" SSSSS ");
        System.out.println("S     S");
        System.out.println("S      ");
        System.out.println(" SSSSS ");
        System.out.println("      S");
        System.out.println("S     S");
        System.out.println(" SSSSS ");
        System.out.println();
    }

    public static void printP() {
        System.out.println("PPPPPP ");
        System.out.println("P     P");
        System.out.println("P     P");
        System.out.println("PPPPPP ");
        System.out.println("P      ");
        System.out.println("P      ");
        System.out.println("P      ");
        System.out.println();
    }
}`
  },
  {
    id: "proj-2",
    type: "project",
    category: "Đồ án Mini 2",
    number: "Project 1.2",
    page: 130,
    title: "Chương trình Letters (Soạn thư cá nhân hóa tái sử dụng)",
    description: "Đôi khi chúng ta gửi thư cho những người khác nhau với một số đoạn văn nội dung chung (ví dụ: kể về việc học, hỏi thăm sức khỏe, hoặc xin trợ cấp sinh hoạt). Viết chương trình `Letters.java` in 3 bức thư gửi cho Bố Mẹ, Bạn Thân và Anh Trai. Sử dụng các phương thức tĩnh để tái sử dụng các đoạn văn chung, triệt tiêu trùng lặp.",
    expectedOutput: "3 bức thư hoàn chỉnh có các đoạn văn chung được in tự động.",
    hint: "Tạo các phương thức: paragraphStudy(), paragraphHealth(), paragraphMoney(), paragraphLove().",
    starterCode: `public class Letters {
    public static void main(String[] args) {
        // In thư gửi Bố Mẹ, Bạn Thân, Anh Trai
    }
}`,
    solutionCode: `public class Letters {
    public static void main(String[] args) {
        letterToParents();
        System.out.println("----------------------------------------");
        letterToFriend();
        System.out.println("----------------------------------------");
        letterToBrother();
    }

    public static void letterToParents() {
        System.out.println("Kinh gui Bo Me,");
        paragraphStudy();
        paragraphMoney();
        System.out.println("Con yeu Bo Me nhieu!\n");
    }

    public static void letterToFriend() {
        System.out.println("Chao cau ban than,");
        paragraphStudy();
        paragraphHobbies();
        System.out.println("Cuoi tuan nay di cafe nhe!\n");
    }

    public static void letterToBrother() {
        System.out.println("Em chao anh hai,");
        paragraphHobbies();
        paragraphMoney();
        System.out.println("Chuc anh lam viec tot nhe!\n");
    }

    public static void paragraphStudy() {
        System.out.println("Hien tai em dang hoc mon Ky thuat Lap trinh Java 4 tin chi.");
        System.out.println("Mon hoc rat thu vi, co nhieu bai tap thuc hanh thuc te.");
    }

    public static void paragraphHobbies() {
        System.out.println("Dao nay nhom em dang lap trinh mot game nho rat vui.");
        System.out.println("Khi nao xong em se gui cho moi nguoi choi thu!");
    }

    public static void paragraphMoney() {
        System.out.println("Thang nay em can mua them tai lieu tham khao va tra tien sach.");
        System.out.println("Mong moi nguoi co the ho tro em mot khoan chi phi a!");
    }
}`
  },
  {
    id: "proj-3",
    type: "project",
    category: "Đồ án Mini 3",
    number: "Project 1.3",
    page: 131,
    title: "Bài hát tích lũy OldLady (Bài ca Con ruồi nuốt chửng)",
    description: "Viết chương trình `OldLady.java` in toàn bộ lời bài hát dân gian tích lũy 'There Was an Old Lady Who Swallowed a Fly' (Bà cụ nuốt con ruồi, nhện, chim, mèo, chó, dê, bò, ngựa). Sử dụng phương thức cho từng khổ thơ và tận dụng luồng điều khiển để loại bỏ trùng lặp điệp khúc tích lũy.",
    expectedOutput: "Lời bài hát với các khổ thơ tích lũy.",
    hint: "Tạo các phương thức cho từng điệp khúc: swallowFly(), swallowSpider(), swallowBird(), ... và chuỗi tích lũy.",
    starterCode: `public class OldLady {
    public static void main(String[] args) {
        // Cấu trúc phân tầng
    }
}`,
    solutionCode: `public class OldLady {
    public static void main(String[] args) {
        verse1();
        System.out.println();
        verse2();
        System.out.println();
        verse3();
        System.out.println();
        verse4();
        System.out.println();
        verse5();
    }

    public static void verse1() {
        System.out.println("There was an old lady who swallowed a fly.");
        dieRefrain();
    }

    public static void verse2() {
        System.out.println("There was an old lady who swallowed a spider,");
        System.out.println("That wriggled and iggled and jiggled inside her.");
        spiderFly();
    }

    public static void verse3() {
        System.out.println("There was an old lady who swallowed a bird,");
        System.out.println("How absurd to swallow a bird.");
        birdSpider();
    }

    public static void verse4() {
        System.out.println("There was an old lady who swallowed a cat,");
        System.out.println("Imagine that to swallow a cat.");
        catBird();
    }

    public static void verse5() {
        System.out.println("There was an old lady who swallowed a horse,");
        System.out.println("She died, of course.");
    }

    public static void catBird() {
        System.out.println("She swallowed the cat to catch the bird,");
        birdSpider();
    }

    public static void birdSpider() {
        System.out.println("She swallowed the bird to catch the spider,");
        spiderFly();
    }

    public static void spiderFly() {
        System.out.println("She swallowed the spider to catch the fly,");
        dieRefrain();
    }

    public static void dieRefrain() {
        System.out.println("I don't know why she swallowed that fly,");
        System.out.println("Perhaps she'll die.");
    }
}`
  }
];

if (typeof module !== 'undefined' && module.exports) {
  module.exports = EXERCISES_CHAPTER_01;
}

