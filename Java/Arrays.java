import java.util.Scanner;

public class Arrays {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] marks = new int[10];
        System.out.println("Enter 10 values:");
        for (int i = 0; i < marks.length; i++) {
            marks[i] = sc.nextInt();
        }
        for (int i = 0; i < marks.length; i++) {
            System.out.print(marks[i] + "  ");
        }
    }
}

/*

int [] marks;    -> Declaration
marks = new int[5]-> Memory allocation

int [] marks = new int[5] -> both of the above

int [] marks = {1,2,3,4,5}; -> Declaration + Initialization
Java automatically knows the size

 */
