// ============================================================================
// HỌC PHẦN: KỸ THUẬT LẬP TRÌNH / LẬP TRÌNH JAVA
// LỚP: IT26M - KHÓA 2026
// BÀI THỰC HÀNH TIẾT 3 (LAB 3 - LỰA CHỌN B): BÀI HÁT CỔ ĐỘNG (FIGHT SONG)
// ÁP DỤNG NGUYÊN LÝ PHÂN RÃ THỦ TỤC & TRIỆT TIÊU TRÙNG LẶP (DRY)
// ============================================================================

public class FightSong {
    public static void main(String[] args) {
        singGoTeam();
        System.out.println();
        singChorus();
        System.out.println();
        singChorus();
        System.out.println();
        singGoTeam();
    }

    // Phương thức in đoạn điệp khúc chính gồm câu cổ động và lời khích lệ
    public static void singChorus() {
        singGoTeam();
        singEncourage();
        singGoTeam();
    }

    // Khối nguyên tử 1: Câu cổ động "Go, team, go!"
    public static void singGoTeam() {
        System.out.println("Go, team, go!");
        System.out.println("You can do it.");
    }

    // Khối nguyên tử 2: Lời khích lệ "You're the best, In the West."
    public static void singEncourage() {
        System.out.println("You're the best,");
        System.out.println("In the West.");
    }
}

