import java.util.Scanner;

public class SumNEvenNums_While {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the no. of even numbers to sum up:");
        int limit = sc.nextInt();
        int sum=0;
        int i=0;
        while(i<limit){
            sum +=(2*i);
            i++;
        }
        System.out.println(sum);

    }
}
