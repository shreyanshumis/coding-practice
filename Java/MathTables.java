import java.util.Scanner;

public class MathTables {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number to see it's table");
        int num = sc.nextInt();
        for(int i = 1; i<=10;i++){
            int res = num *i;
            System.out.printf(" %d * %d = " + res + "\n", num, i);
        }
    }
}
