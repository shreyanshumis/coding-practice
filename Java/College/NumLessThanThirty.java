
import java.util.Scanner;
public class NumLessThanThirty {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int num = sc.nextInt();
        if (num>=30){
            System.out.println("It is greater than 30");
        }
        else{
            System.out.println("It is less than 30");
        }
    }
}
