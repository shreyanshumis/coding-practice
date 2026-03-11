import java.util.Scanner;

public class Calculator_Method {
    static double sum(double a, double b) {
        return a + b;
    }

    static double sub(double a, double b) {
        return a - b;
    }

    static double multiply(double a, double b) {
        return a * b;
    }

    static double divide(double a, double b) {
        return a / b;
    }

    static double mod(double a, double b) {
        return a % b;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter two numbers");
        double x = sc.nextDouble();
        double y = sc.nextDouble();
        System.out.println("What do you want to do? \npress '+' for addition\n'-' for subtraction\n'*' for multiplication\n'/' for division\n'%' for modulus");
        System.out.println("Press 'e' to exit");
        char choice = sc.next().charAt(0);
        switch (choice) {
            case '+' -> System.out.println(sum(x, y));
            case '-' -> System.out.println(sub(x, y));
            case '*' -> System.out.println(multiply(x, y));
            case '/' -> System.out.println(divide(x, y));
            case '%' -> System.out.println(mod(x, y));
            case 'e' -> System.exit(0);
            default -> System.out.println("Invalid input");
        }
    }
}