public class VowelCheckExample {

    public static void main(String[] args) {
        try {
            String inputString = "xyz"; // Change this to any string you want to check
            checkForVowels(inputString);
            System.out.println("The string contains vowels.");
        } catch (NoVowelsException e) {
            System.out.println(e.getMessage());
        }
    }

    static void checkForVowels(String str) throws NoVowelsException {
        if (!containsVowels(str)) {
            throw new NoVowelsException("Exception: The string does not contain any vowels.");
        }
    }

    static boolean containsVowels(String str) {
        String lowercaseStr = str.toLowerCase();
        return lowercaseStr.matches(".*[aeiou].*");
    }
}

class NoVowelsException extends Exception {
    public NoVowelsException(String message) {
        super(message);
    }
}
