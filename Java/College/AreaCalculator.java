
public class AreaCalculator {

    static void calc(int a){
        System.out.println(a*a);
    }

    static void calc(int a, int b){ //square
        System.out.println(a*b);
    }

    static void calc(double a){
        System.out.println(3.14*a*a);
    }

    public static void main(String[] args) {
        calc(4);
        calc(4,6);
        calc(1.2);
    }
}
