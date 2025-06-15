//import java.util.Scanner;

public class Letter_CustomName {
    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        String name = sc.next();
//        System.out.printf("Dear %s Thanks a lot!", name);
//        //or
//        System.out.println("Dear " + name + " Thanks a lot!");
        String letter = "Dear <|name|> Thanks a lot!";
        letter = letter.replace("<|name|>", "Shrey");
        System.out.println(letter);
    }
}
