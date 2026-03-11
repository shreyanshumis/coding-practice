
import java.io.BufferedReader;
import java.io.InputStreamReader;
class Emp {
    Emp() {
        System.out.println("Employee Details");
    }

    Emp(String name) {
        System.out.println("Employee name - " + name);
    }

    Emp(String dept, int id) {
        System.out.println("Employee Department - " + dept);
        System.out.println("Employee ID - " + id);
    }
}
public class Parameterized_cons {

    public static void main(String[] args) {
        String n, d;
        int id;
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader bf = new BufferedReader(isr);
        //BufferedReader bf =new BufferedReader(new InputStreamReader(System.in));
        try{
            System.out.println("Enter Employee name - ");
            n=bf.readLine();
            System.out.println("Enter Employee department - ");
            d=bf.readLine();
            System.out.println("Enter Employee id - ");
            id=Integer.parseInt(bf.readLine());


            Emp e1=new Emp();
            Emp e2=new Emp(n);
            Emp e3=new Emp(d,id);
        }
        catch (Exception e) {
            // TODO Auto-generated catch block
            System.out.println();
        }

    }
}
