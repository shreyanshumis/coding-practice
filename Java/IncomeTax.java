import java.util.Scanner;

public class IncomeTax {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your income per annum");
        float income = sc.nextFloat();
        float tax = 0.0f;

        if (income< 250000.0){
            System.out.println("No income tax");
        } else if (income>= 250000.0 && income< 500000.0) {
            tax = tax + 0.05f * (income - 250000);
            System.out.println("Your tax is :"+ tax);
        } else if (income>= 500000.0 && income< 1000000.0) {
            tax = tax + 0.05f * (income - 250000);
            tax = tax + 0.2f * (income - 500000);
            System.out.println("Your tax is :"+ tax);
        } else if (income>= 1000000.0) {
            tax = tax + 0.05f * (income - 250000);
            tax = tax + 0.2f * (income - 500000);
            tax = tax + 0.3f * (income  - 1000000);
            System.out.println("Your tax is :"+ tax);
        }

    }
}
