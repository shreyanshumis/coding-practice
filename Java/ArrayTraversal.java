public class ArrayTraversal {
    public static void main(String[] args) {
        int [] marks = {31,82,37,90,98};
//        System.out.println(marks.length); //length property

        //Displaying array (Naive way)
        System.out.println(marks[0]);
        System.out.println(marks[1]);
        System.out.println(marks[2]);
        System.out.println(marks[3]);
        System.out.println(marks[4]);

        System.out.println("============");

        //Displaying array (Better way)
        for (int i : marks) {
            System.out.println(i); //enhanced for or for each loop
        }

//        for(int i=0;i<marks.length;i++){
//            System.out.println(marks[i]);
//        }                         //regular for loop

        System.out.println("============");

        //printing in reverse order
        for(int i=marks.length-1;i>=0;i--){
            System.out.println(marks[i]);
        }
    }
}
