import java.security.SecureRandom;
import java.util.Scanner;

public class PasswordGen {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the password length: ");
        int length = scanner.nextInt();

        String password = generatePassword(length);
        System.out.println("Generated Password: " + password);

        scanner.close();
    }

    private static String generatePassword(int length) {
        String uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String lowercaseLetters = "abcdefghijklmnopqrstuvwxyz";
        String numbers = "0123456789";
        String specialChars = "@#$%&*";

        String allChars = uppercaseLetters + lowercaseLetters + numbers + specialChars;

        SecureRandom secureRandom = new SecureRandom();
        StringBuilder passwordBuilder = new StringBuilder(length);

        passwordBuilder.append(uppercaseLetters.charAt(secureRandom.nextInt(uppercaseLetters.length())));
        passwordBuilder.append(lowercaseLetters.charAt(secureRandom.nextInt(lowercaseLetters.length())));
        passwordBuilder.append(numbers.charAt(secureRandom.nextInt(numbers.length())));
        passwordBuilder.append(specialChars.charAt(secureRandom.nextInt(specialChars.length())));

        for (int i = 4; i < length; i++) {
            passwordBuilder.append(allChars.charAt(secureRandom.nextInt(allChars.length())));
        }

        return passwordBuilder.toString();
    }
}
