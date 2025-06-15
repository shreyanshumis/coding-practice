public class PatternRecursion2 {
    static void pat2(int n) {
        if (n > 0) {
            for (int i = n; i > 0; i--) {
                System.out.print("*");
            }
            System.out.println("");
            pat2(n - 1);
        }
    }

    public static void main(String[] args) {
        pat2(3);
    }
}
