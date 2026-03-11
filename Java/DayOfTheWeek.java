import java.util.Scanner;
public class DayOfTheWeek {
    public static void main(String[] args) {
//        1 for monday and so on...
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number and this will give the day of the week");
        byte day = sc.nextByte();

        switch (day) {
            case 1 -> System.out.println("Monday");
            case 2 -> System.out.println("Tuesday");
            case 3 -> System.out.println("Wednesday");
            case 4 -> System.out.println("Thursday");
            case 5 -> System.out.println("Friday");
            case 6 -> System.out.println("Saturday");
            case 7 -> System.out.println("Sunday!");
        }
    }
}
