public class BreakAndContinue {
    public static void main(String[] args) {
        for(int i=0;i<=10;i++){
            if(i==7){
                break;//terminates the entire loop
            } else if (i==3) {
                continue;//skips the current iteration
            }
            System.out.println(i);
        }
    }
}

