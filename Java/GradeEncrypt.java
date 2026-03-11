import java.util.Scanner;
public class GradeEncrypt {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your grade!");
        char grade = sc.next().charAt(0);
        //Encrypt
        grade = (char)(grade + 8);
        System.out.println("Encrypted:" + grade);
        //Decrypt
        grade = (char)(grade - 8);
        System.out.println("Decrypted:" + grade);
    }
}
