public class EscapeSeq {
    public static void main(String[] args) {
        //format the letter by adding escape sequences -CWH Practice set
        String letter = "Dear CWH, Good job.. Thank you";
        String letter2 = "Dear CWH, \n\tGood job.. \n\tThank you";
        System.out.println("Original:" + letter);
        System.out.println("Modified:" + letter2);
    }
}
