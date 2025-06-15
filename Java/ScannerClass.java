import java.util.Scanner; //imports the code for scanner(input)

public class ScannerClass {
    public static void main(String[] args) {
        System.out.println("Taking input from the user");
        Scanner sc = new Scanner(System.in); //reads from the keyboard
        System.out.println("Enter.....");
        //for all the data types....
        int a = sc.nextInt();//reads integer
        float b = sc.nextFloat();//reads float
        String str = sc.next();//ignores after whitespace
        String str1 = sc.nextLine();//reads the entire line
        //print statements...
        System.out.println(a);
        System.out.println(b);
        System.out.println(str);
        System.out.println(str1);

    }
}