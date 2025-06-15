package Tutorial;
import java.util.Scanner;
public class program4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String inputString = sc.nextLine();
        inputString = inputString.toLowerCase(); // Convert to lowercase for case-insensitive counting

        // Create an array to store the frequency of each character
        int[] frequency = new int[26]; // Assuming only lowercase letters; adjust for uppercase and additional characters

        // Iterate through the string and update the frequency array
        for (int i = 0; i < inputString.length(); i++) {
            char ch = inputString.charAt(i);
            if (ch >= 'a' && ch <= 'z') {
                int index = ch - 'a'; // Calculate the index for the character 'a' to 'z'
                frequency[index]++;
            }
        }

        // Print the character frequencies
        for (char ch = 'a'; ch <= 'z'; ch++) {
            int index = ch - 'a';
            if (frequency[index] > 0) {
                System.out.println(ch + ": " + frequency[index]);
            }
        }
    }
}

