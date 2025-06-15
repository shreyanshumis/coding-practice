package Tutorial;

import java.util.Scanner;
public class program1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean check = true;
        System.out.println("Enter numbers, press zero to exit");
        int oddNum= 0, evenNum =0;
        int oddCount = 0, evenCount=0;
        int avgOdd=0, avgEve=0;
        while(check){

            int inpNum = sc.nextInt();
            if(inpNum!=0){
            if(inpNum%2==0){
                evenNum+=inpNum;
                evenCount++;
            }

            else {
                oddNum+=inpNum;
                oddCount++;
            }

        }
            else {
                check= false;
            }
        }

        avgEve = evenNum/evenCount;
        avgOdd = oddNum/oddCount;

        System.out.println("Even number sum is = "+ evenNum);
        System.out.println("Odd number sum is = "+ oddNum);

        System.out.println("Even number average = "+ avgEve);
        System.out.println("Odd number average = "+ avgOdd);
    }
}
