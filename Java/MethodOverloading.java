public class MethodOverloading {

    static void calc(int a, int b){
        System.out.println(a+b);//add
    }

    static void calc(int a){ //square
        System.out.println(a*a);
    }

    static void calc(double a, double b){
        System.out.println(a/b);
    }

    public static void main(String[] args) {
        calc(1,2);
        calc(4);
        calc(1.2,0.5);
    }
}
