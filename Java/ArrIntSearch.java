public class ArrIntSearch {
    public static void main(String[] args) {
        int [] arr = {1,2,3,4,5};
        int givenInt= 2;
        boolean presence = false;
        for(int i=0; i<arr.length;i++){
            if (arr[i]==givenInt){
                presence = true;
                break;
            }
            }
        if (presence==true){
            System.out.println("The element is present");
        }
        else {
            System.out.println("It is not present");
        }
    }
}
