import java.util.Scanner;

public class Grades_SwitchCase {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter grade from A-F");
        char grade = sc.next().charAt(0);
        grade = Character.toLowerCase(grade);

//NORMAL SWITCH
        switch(grade){
            case 'a':
                System.out.println("You are doing excellent!");
                break;
            case 'b':
                System.out.println("You're doing a fabulous job!");
                break;
            case 'c':
                System.out.println("You're doing a good job!");
                break;
            case 'd':
                System.out.println("You can do much better!");
                break;
            case 'e':
                System.out.println("You need to improve..");
                break;
            case 'f':
                System.out.println("You really do need to improve");
                break;
            default:
                System.out.println("Invalid input");}

//ENHANCED SWITCH
        switch (grade) {
            case 'a' -> System.out.println("You are doing excellent!");
            case 'b' -> System.out.println("You're doing a fabulous job!");
            case 'c' -> System.out.println("You're doing a good job!");
            case 'd' -> System.out.println("You can do much better!");
            case 'e' -> System.out.println("You need to improve..");
            case 'f' -> System.out.println("You really do need to improve");
            default -> System.out.println("Invalid input");}
    }
}
