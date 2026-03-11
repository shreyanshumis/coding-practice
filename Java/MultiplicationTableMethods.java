import java.util.Scanner;
public class MultiplicationTableMethods {
    static void multTable(int n){
        for(int i=1;i<=10;i++){
            System.out.println(n*i);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number to find it's table");
        int input = sc.nextInt();
        multTable(input);
    }
}
