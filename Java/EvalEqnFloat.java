public class EvalEqnFloat {
    public static void main(String[] args) {
        float a = 7/4 * 9/2; //The individual numbers here are still integers...
        float b = 7/4.0f * 9/2.0f; //These are floating point numbers so they will return the correct value.
        System.out.println("Int wala:" + a);
        System.out.println("Float wala:" + b);
    }
}
