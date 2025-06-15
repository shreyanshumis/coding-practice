package Tutorial;

public class program5 {
    public static void main(String[] args) {
        int n = 4; // Number of rows

        for (int i = 1; i <= n; i++) {
            // Print leading spaces
            for (int j = 1; j <= n - i; j++) {
                System.out.print(" ");
            }

            // Print digits
            for (int j = 1; j <= 2 * i - 1; j++) {
                System.out.print(i);
            }

            // Move to the next line
            System.out.println();
        }
    }
}
