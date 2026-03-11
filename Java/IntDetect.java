import java.util.Scanner;
public class IntDetect {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a integer number and we will check if it is an integer or not");
        System.out.println(sc.hasNextInt());
    }
}
