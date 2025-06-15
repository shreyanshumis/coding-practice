public class RecurSumNatNo {
    //Recursive sum of natural numbers
    static int recurNo(int n) {
        if(n==1){
            return 1;
        }
        else {
            return n + recurNo(n-1);
        }
    }

    public static void main(String[] args) {
        System.out.println(recurNo(10));

    }
}

