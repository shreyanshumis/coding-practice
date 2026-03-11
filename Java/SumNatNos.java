import java.util.Scanner;
public class SumNatNos {
    public static void main(String[] args) {
        System.out.println("Enter the limit of sum of natural numbers:");
        Scanner sc = new Scanner(System.in);
        int lim = sc.nextInt();
        int sum=0;
        for(int i=1; i<=lim; i++){
            sum=sum+i;
        }
        System.out.println(sum);
    }
}
