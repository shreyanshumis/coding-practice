import java.util.Scanner;

public class SpaceToUnderscores {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a small sentence:");
        String sentence= sc.nextLine();
        System.out.println("Converting...");
        sentence = sentence.replace(" ", "_");
        System.out.println("New String:"+ sentence);
    }
}
