public class ArrMinimumElem {
    public static void main(String[] args) {
        int [] arr = {3,5,47,69,8,2};
        int min = arr[0];
        for(int i=1;i<arr.length;i++){
            if(arr[i]<min){
                min = arr[i];
            }
            else {
                continue;
            }
        }
        System.out.println("The biggest element is ="+min);
    }
}
