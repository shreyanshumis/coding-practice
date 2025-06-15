public class StringsInJava {
    public static void main(String[] args) {
        String name = new String("Shrey");
        String name2 = "Shrey";

        //String is a class
        //Strings are immutable
        System.out.println(name);
        System.out.println(name2);

        //Different ways to print in Java
        System.out.print("print"); //same line
        System.out.println("println"); //next line
        int a = 6;
        float b = 3.323f;
        System.out.printf("The value of a is %d and b is %f", a, b); //f is format specifier
        // %d for int, %f for float, %c for char, %S for strings
        System.out.format("The value of a is %d and b is %f", a, b); //same thing - same behaviour
    }
}
