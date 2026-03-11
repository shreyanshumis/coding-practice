

public class LargestElement {
    public static void main(String[] args) {
        int[] arr = {10, 45, 30, 99, 5, 73, 22};
        int largest = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > largest) {
                largest = arr[i];
            }
        }
        System.out.println("The largest element in the array is: " + largest);
    }
}