package Tutorial;
import java.util.Scanner;
class Clock{
    int hours, mins, secs;
    Clock(int h, int m, int s){
        hours=h;
        mins=m;
        secs=s;
    }

    void isTimeValid(){
        if(hours>=0 && hours<24 && mins>0 && mins<60 && secs>0 && secs<60){
            System.out.println("Valid time");
        }
        else {
            System.out.println("Invalid time.");
        }
    }

    void ampm(){
        if(hours<12){
            System.out.println("Time ->"+ hours + ":"+ mins + ":"+ secs + " AM");
        }
        else{
            hours = hours-12;
            System.out.println("Time ->"+ hours + ":"+ mins + ":"+ secs + " PM");
        }
    }

}

public class program2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter hours, minutes and seconds:");
        int h1= sc.nextInt();
        int m1= sc.nextInt();
        int s1 = sc.nextInt();
        Clock c1 = new Clock(h1,m1,s1);

        c1.isTimeValid();
        c1.ampm();
    }
}
