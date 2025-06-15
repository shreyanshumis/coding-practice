public class FibonacciRecursion {
    public static void main(String[] args) {
        int n = 10;
        for (int i = 0; i<n; i++){
            System.out.print(fibo(i)+ " ");
        }}
    static int fibo(int x){
        if (x == 0){
            return 0;
        }
        else if(x == 1){
            return 1;
        }
        else {
            return fibo(x-1) + fibo(x-2);
        }
    }
}


