public class DoWhileDemonstration {
    public static void main(String[] args) {
        int a = 20;
        while(a>25){ //will never execute
            System.out.println("While loop executed");
        }
        //=================================================//

        do {
            System.out.println("Do-while executed");//this will execute ATLEAST once
        } while(a>25);
    }
}
