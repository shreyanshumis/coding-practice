import java.util.Scanner;
public class FactorialRecur1 {
    static int fact(int n) {
        if (n == 0 || n ==1) {
            return 1;
        }
        else return n * fact(n - 1);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number to find it's factorial");
        int fac = sc.nextInt();
        System.out.println("factorial is : " + fact(fac));
    }
}
