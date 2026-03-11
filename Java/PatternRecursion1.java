public class PatternRecursion1 {
    static void pat1(int n){
        if(n>0){
            pat1(n -1 );
        }
        for(int i=0;i <n;i++){
            System.out.print("*");
        }
        System.out.println("");
    }


    public static void main(String[] args) {
        pat1(3);
    }
}

//pat1(3) - ->
//pat1(2) - 3 times star and new line
//pat1(1) - 2 times star and new line + 3 times star and new line
//pat1(0) - 1 times star and new line + 2 times star and new line + 3 times star and new line
//prints them altogether and terminates