
public class EvenOdd100_150 {
    public static void main(String[] args) {
        System.out.println("Even nos:");
        for (int i = 100; i <= 150; i++) {
            if (i % 2 == 0) {
                System.out.println(i);
            }
        }

        System.out.println("Odd nos:");
        for (int j = 101; j <= 150; j++) {
            if (j % 2 != 0) {
                System.out.println(j);
            }
        }
    }
}