public class ArrayReverse {
    public static void main(String[] args) {
        int [] arr = {1,2,3,4,5,6,7};
        int [] rev = new int[7];
        int mid = Math.floorDiv(arr.length-1,2);
        int temp;
        int l = arr.length;
        for(int i =0;i<mid;i++){
            temp = arr[i];
            arr[i] = arr[l-1-i];
            arr[l-1-i] = temp;

        }
        for(int element: arr){
            System.out.print(element + " ");
        }

    }
}
