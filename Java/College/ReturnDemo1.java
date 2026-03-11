
import java.util.Scanner;
class Box1 {
    double width;
    double height;
    double depth;
    double volume()
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter width");
        double width = sc.nextDouble();
        System.out.println("Enter height");
        double height = sc.nextDouble();
        System.out.println("Enter depth");
        double depth = sc.nextDouble();
        return width * height * depth;
    }
}

public class ReturnDemo1
{
    public static void main(String[] args) {
        Box1 cuboid = new Box1();
        double vol;
        vol = cuboid.volume();
        System.out.println("Volume:"+ vol);
    }
}
