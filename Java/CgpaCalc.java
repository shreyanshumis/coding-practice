import java.util.Scanner;
public class CgpaCalc {
    public static void main(String[] args) {
        System.out.println("Enter your marks in 3 subjects: ");
        Scanner sc = new Scanner(System.in);
        float sub1 = sc.nextFloat();
        float sub2 = sc.nextFloat();
        float sub3 = sc.nextFloat();

        float cgpa = (sub1+sub2+sub3)/30;
        System.out.println("The CGPA is :- " + cgpa);

    }
}
