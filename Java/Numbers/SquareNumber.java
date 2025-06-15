package Numbers;
import java.lang.Math;
import java.util.Scanner;
public class SquareNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter a number");
        int num = sc.nextInt();
        double sq = Math.sqrt(num);

        if (sq*sq == num){
            System.out.println("The number is a square number");
        }
        else if(sq*sq != num){
            System.out.println("The number isn't a square number");
        }
        else {
            System.out.println("Invalid input");
        }
    }
}
