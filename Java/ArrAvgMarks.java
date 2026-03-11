public class ArrAvgMarks {
    public static void main(String[] args) {
        int [] marks = {99,97,69,32,78};
        int avg, sum=0;
        for (int i : marks) {
            sum += i;
        }
        avg = sum/marks.length;
        System.out.println(avg);
    }
}
