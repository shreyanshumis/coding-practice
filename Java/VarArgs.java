public class VarArgs {

        static int add(int ...arr){ // int ...arr => int [] arr but it can take any amount of arguments lmao
            int result = 0;
            for (int a : arr){
                result = result + a;
            }
            return result;
        }

        public static void main(String[] args){
            //as u can see with the examples below...any no. of args can be taken
            System.out.println(add(1,2));
            System.out.println(add(2,3,4));
            System.out.println(add(4,5,6));
        }
    }

