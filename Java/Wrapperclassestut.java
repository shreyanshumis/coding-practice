public class Wrapperclassestut {
    public static void main(String[] args) {
        /*Wrapper classes
        The wrapper class in Java provides the mechanism to convert primitive into object and object into primitive.*/

        //Autoboxing
        int a = 20;
        Integer awrap = Integer.valueOf(a);
        System.out.println(awrap);

        //Unboxing
        Integer awrap2 = new Integer(69);
        int a2 = awrap2.intValue();
        System.out.println(a2);

    }
}
