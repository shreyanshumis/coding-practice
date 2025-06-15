public class StaticNonStaticMethod {

    static int One(int x, int y){ //Static method
        return x+y;
    }

    int Two(int x, int y){ //non Static method
        return x+y;
    }

    public static void main(String[] args) {//program3 method
        //STATIC
        int c = One(1,2); //Static method

        //NON STATIC
        StaticNonStaticMethod obj = new StaticNonStaticMethod(); //Object creation
        int c1 = obj.Two(1,2); //non static method
    }
}
