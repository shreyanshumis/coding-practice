import java.util.Scanner;

public class SumNumInMultTables {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int sumTotal=0;
        for(int i=1;i<=10;i++){
            sumTotal += (num*i);
        }
        System.out.println(sumTotal);
    }
}
