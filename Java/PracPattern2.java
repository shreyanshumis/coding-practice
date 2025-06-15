public class PracPattern2 {
    public static void main(String[] args) {

        for (int i = 4; i >=0; i--) {
            int j=0;
            while(j<=i){
                System.out.print("*");
                j++;
            }
            System.out.print("\n");
        }
    }
}
