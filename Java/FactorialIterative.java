import java.util.Scanner;
public class FactorialIterative {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.println("Enter a number to find it's factorial: ");
        int num = sc.nextInt();
        int fac = 1;
        for(int i = 1; i!=(num+1);i++){
            fac *= i;
        }
        System.out.println(fac);
    }
}
