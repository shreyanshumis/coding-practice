public class PatternMethod2 {
    static void pat(){
        for (int i = 0;i<5;i++){
            for (int j=5; j>i;j--){
                System.out.print("*");
            }
            System.out.println(" ");
        }
    }

    public static void main(String[] args) {
        pat();
    }
}
