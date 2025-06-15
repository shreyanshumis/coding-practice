class Employeeeeee {
    int id;
    String name;
    public void printDetails(){
        System.out.println("My id is "+ id);
        System.out.println("My name is "+ name);
    }
}

public class CustomClassesInJava {
    public static void main(String[] args) {
        System.out.println("This is our custom class");
        //object tiari hauchi
        Employeeeeee shrey = new Employeeeeee(); //instantiating a new employee object

        //setting attributes/properties
        shrey.id = 01;
        shrey.name = "Shrey";

        //calling the method itself
        shrey.printDetails();

        //printing
        //System.out.println( shrey.id);
        //System.out.println( shrey.name);
    }
}

/*
Any real world object = Properties + Behaviour
Objects in OOPs       = Attributes + Methods(Functions)
 */