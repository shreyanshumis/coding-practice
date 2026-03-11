public class ArrMaximumElem {
    public static void main(String[] args) {
        int [] arr = {3,5,47,69,8,2};
        int max = arr[0];
        for(int i=1;i<arr.length;i++){
            if(arr[i]>max){
                max = arr[i];
            }
            else {
                continue;
            }
        }
        System.out.println("The biggest element is ="+max);
    }
}
