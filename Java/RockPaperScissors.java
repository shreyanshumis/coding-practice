import java.util.Scanner;
import java.util.Random;

public class RockPaperScissors {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Random rand = new Random();

        String userInp = sc.next();
        userInp= userInp.toLowerCase();
        int random = rand.nextInt(3);
        String compImp = " ";

        if (random == 0){
            compImp = "rock";
        } else if (random == 1) {
            compImp = "paper";
        } else if (random == 2) {
            compImp = "scissors";
        }

        System.out.println("User : "+ userInp);
        System.out.println("Computer : "+ compImp);
        if (userInp.equals(compImp)){
            System.out.println("Tie");
        } else if (userInp.equals("rock") && compImp.equals("paper")) {
            System.out.println("Computer wins!");
        } else if (userInp.equals("paper") && compImp.equals("scissors")) {
            System.out.println("Computer wins!");
        } else if (userInp.equals("scissors") && compImp.equals("rock")){
            System.out.println("Computer wins!");
        } else {
            System.out.println("You won!");
        }
    }
}
