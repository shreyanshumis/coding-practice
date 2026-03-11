import java.util.Scanner;
public class KmToMiles {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter value in kms:");
        double km = sc.nextDouble();
        double mile = km/1.609;
        System.out.println("Kms : " + km + "\nMiles : " + mile);
    }
}
