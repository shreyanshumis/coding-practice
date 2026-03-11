public class ArrFloatSum {
    public static void main(String[] args) {
        float [] arr={4.5f,5.5f,6.9f,3.1f,9.9f};
        float sum=0.0f;
        for(int i=0;i<arr.length;i++){
            sum += arr[i];
        }
        System.out.println(sum);
    }
}
