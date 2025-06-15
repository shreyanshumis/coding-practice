import java.util.Scanner;
public class FactorialIterative3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int fac = sc.nextInt();
        int temp=1;
        int i = fac;
        while(i>0){
            temp = temp * i;
            i--;
        }
        System.out.println(temp);
    }
}
