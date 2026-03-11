public class ArrSortedUnsorted {
    public static void main(String[] args) {
        int [] arr = {1,2,3,4,5,6};
        boolean isSorted = true;
        for(int i=1;i<arr.length-1;i++){
            if (arr[i]>arr[i+1]){
                isSorted = false;
                break;
            }
        }
        if (isSorted==false){
            System.out.println("This array is not sorted");
        }
        else {
            System.out.println("This array is sorted");
        }
    }
}
