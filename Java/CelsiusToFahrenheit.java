import java.util.Scanner;
public class CelsiusToFahrenheit {

    static double convertTemp(double temp){
        double fahrenheit = (temp * 9/5) + 32;
        return fahrenheit;
    }

    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.println("Enter the temperature");
        double celc = sc.nextDouble();
        System.out.println("The temperature in fahrenheit is: "+ convertTemp(celc));
    }
}
