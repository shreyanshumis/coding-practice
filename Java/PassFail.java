import java.sql.SQLOutput;
import java.util.Scanner;
public class PassFail {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter marks of 3 subjects.");
        double mark1 = sc.nextDouble();
        double mark2 = sc.nextDouble();
        double mark3 = sc.nextDouble();
        System.out.println("Enter the total marks for all");
        double total = sc.nextDouble();
        double perc1 = (mark1/total)*100;
        double perc2 = (mark2/total)*100;
        double perc3 = (mark3/total)*100;
        double totalPerc = ((perc1+perc2+perc3)/(total*3))*100;


        if (perc1>=33 && perc2>=33 && perc3>=33 && totalPerc> 40){
            System.out.println("You have Passed! Congratulations!");
        } else {
            System.out.println("You have failed!!!! congrats");
        }
    }
}

//public class PassFail (Code by CWH) {
//    public static void main(String[] args) {
//        byte m1, m2, m3;
//        Scanner sc = new Scanner(System.in);
//        System.out.println("Enter your marks in 3 Subjects");
//        m1 = sc.nextByte();
//        m2= sc.nextByte();
//        m3 = sc.nextByte();
//        float avg = (m1+m2+m3)/3.0f;
//        System.out.println("Your Overall percentage is: " + avg);
//        if(avg>=40 && m1>=33 && m2>=33 && m3>=33){
//            System.out.println("Congratulations, You have been promoted");
//        }
//        else{
//            System.out.println("Sorry, You have not been promoted! Please try again.");
//        }
//
//    }
//}
