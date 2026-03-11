package Numbers;
import java.lang.Math;
import java.util.Scanner;
public class ArmstrongNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        double orignum = num, newnum =0, temp;

        while(num>0){
            temp = num%10;
            temp = Math.pow(temp,3);
            newnum += temp;
            num /= 10;
        }
        if(newnum == orignum){
            System.out.println("It is an armstrong number");
        }
        else {
            System.out.println("It isnt");
        }
    }
}
