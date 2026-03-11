import java.util.Scanner;
public class LowerCaseConvert {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a String");
        String str = sc.nextLine();
        System.out.println("Original:"+str);
        str = str.toLowerCase();
        System.out.println("Lower case:" + str);
    }
}
