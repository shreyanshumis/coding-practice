import java.util.Scanner;

public class SumNEvenNums_For {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the no. of even numbers to sum up:");
        int limit = sc.nextInt();
        int sum=0;
        for (int i=0;i<limit;i++){
            sum += (2*i);
        }
        System.out.println(sum);

    }
}
