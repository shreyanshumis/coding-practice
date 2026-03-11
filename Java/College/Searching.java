
public class Searching {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7};
        int elementToFind = 4;

        boolean found = false;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == elementToFind) {
                found = true;
                break; // Exit the loop if the element is found
            }
        }

        if (found) {
            System.out.println("Element " + elementToFind + " found in the array.");
        } else {
            System.out.println("Element " + elementToFind + " not found in the array.");
        }
    }
}
