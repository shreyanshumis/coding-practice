package Tutorial;

public class program6 {
    public static void main(String[] args) {
        int n = 3; // Number of rows

        for (int i = 1; i <= n; i++) {
            // Print leading spaces
            for (int j = 1; j <= n - i; j++) {
                System.out.print(" ");
            }

            // Print decreasing sequence
            for (int j = i; j >= 1; j--) {
                System.out.print(j);
            }

            // Print increasing sequence (excluding 1 for the middle row)
            for (int j = 2; j <= i; j++) {
                System.out.print(j);
            }

            // Move to the next line
            System.out.println();
        }
    }
}
