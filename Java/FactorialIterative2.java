import java.util.Scanner;
public class FactorialIterative2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number");
        int num = sc.nextInt();
        int temp = 1;
        for(int i=num; i>0; i--){
            temp *= i;
        }
        System.out.println(temp);
    }
}
