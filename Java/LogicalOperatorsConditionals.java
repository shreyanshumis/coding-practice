public class LogicalOperatorsConditionals {
    public static void main(String[] args) {
        System.out.println("For Logical AND");
        boolean a = true;
        boolean b = false;
        if (a && b){//both have to be true for yes else no
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }

        System.out.println("For Logical OR");

        if (a || b){//if any one or both are true then true else false
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }

        System.out.println("For Logical NOT");//if something is true then false. vice versa
        System.out.print("Not(a) is ");
        System.out.println(!a);//opposite of a
        System.out.print("Not(b) is ");
        System.out.println(!b);//opposite of b
    }
}

