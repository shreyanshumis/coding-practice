
public class Fibonacci {
    public static void main(String[] args) {
        int n = 10; // Change n to the desired number of Fibonacci numbers
        generateFibonacci(n);
    }

    public static void generateFibonacci(int n) {
        long first = 0;
        long second = 1;

        System.out.println("Fibonacci Sequence:");
        System.out.print(first + " " + second + " ");

        for (int i = 2; i < n; i++) {
            long next = first + second;
            System.out.print(next + " ");
            first = second;
            second = next;
        }
    }

}
