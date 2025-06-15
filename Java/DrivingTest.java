import java.util.Scanner;

public class DrivingTest {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your age:");
        int age = sc.nextInt();
        if(age>18){
            System.out.println("You are eligible for driving!");
        }
        else if (age==18) {
            System.out.println("You are partially eligible, you should take a driving test");
        }
        else {
            System.out.println("You are not eligible.");
        }
    }
}
