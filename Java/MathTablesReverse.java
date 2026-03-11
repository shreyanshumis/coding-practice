import java.util.Scanner;

public class MathTablesReverse {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number to see it's table");
        int num = sc.nextInt();
        for(int i = 10; i>0;i--){
            int res = num *i;
            System.out.printf(" %d * %d = " + res + "\n", num, i);
        }
    }
}
