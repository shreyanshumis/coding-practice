import java.util.Scanner;
public class TypeOfWebsite {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the url:");
        String urlInput = sc.nextLine();
        if(urlInput.endsWith(".org")){
            System.out.println("Organization.");
        } else if (urlInput.endsWith(".com")) {
            System.out.println("Commercial.");
        } else if (urlInput.endsWith(".in")) {
            System.out.println("Indian.");
        }
    }
}

