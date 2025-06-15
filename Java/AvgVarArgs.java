public class AvgVarArgs {
    static int avg(int ...arr) {
        int tot = 0;
        int count = 1;
        for (int a : arr) {
            tot += a;
            count++;
        }
        return (tot/count);
    }


    public static void main(String[] args) {
        System.out.println(avg(1,6,7));
        }
    }

