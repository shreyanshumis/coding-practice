public class DoubleTripleSpaces {
    public static void main(String[] args) {
        String line = "This is a  bigggg string";
        System.out.println(line.indexOf("  "));
        System.out.println(line.indexOf("   ")); //if it returns -1 then it has none..
    }
}
