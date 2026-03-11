import java.util.Scanner;

public class Marks {
    public static void main(String[] args) {
        System.out.println("Enter your marks(out of 100) in these five subjects:\n1. Maths \n2. Comp Apps \n3. Science \n4. Economics \n5. EVS \n");
        Scanner sc = new Scanner(System.in);
        int maths= sc.nextInt();
        int computerApps= sc.nextInt();
        int science= sc.nextInt();
        int economics= sc.nextInt();
        int environmentalStudies= sc.nextInt();

        double percentage = ((double) (maths + computerApps + science + economics + environmentalStudies) /500)*100;
        System.out.println("The percentage of the student is" + percentage);
    }
}
