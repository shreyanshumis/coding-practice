package Tutorial;

//abstract class Employee {
//    private String name;
//    private int employeeId;
//    protected double basicSalary;
//
//    public Employee(String name, int employeeId, double basicSalary) {
//        this.name = name;
//        this.employeeId = employeeId;
//        this.basicSalary = basicSalary;
//    }
//
//    // Abstract method to calculate net salary
//    public abstract double calculateNetSalary();
//
//    // Abstract method to display employee information
//    public abstract void displayInfo();
//}
//
//class Manager extends Employee {
//    private double allowance;
//
//    public Manager(String name, int employeeId, double basicSalary, double allowance) {
//        super(name, employeeId, basicSalary);
//        this.allowance = allowance;
//    }
//
//    // Override calculateNetSalary for Manager
//    @Override
//    public double calculateNetSalary() {
//        return basicSalary + allowance;
//    }
//
//    // Override displayInfo for Manager
//    @Override
//    public void displayInfo() {
//        System.out.println("Manager Information:");
//        System.out.println("Name: " + name);
//        System.out.println("Employee ID: " + employeeId);
//        System.out.println("Basic Salary: $" + basicSalary);
//        System.out.println("Allowance: $" + allowance);
//        System.out.println("Net Salary: $" + calculateNetSalary());
//    }
//}
//
//class Clerk extends Employee {
//    private double overtimePay;
//
//    public Clerk(String name, int employeeId, double basicSalary, double overtimePay) {
//        super(name, employeeId, basicSalary);
//        this.overtimePay = overtimePay;
//    }
//
//    // Override calculateNetSalary for Clerk
//    @Override
//    public double calculateNetSalary() {
//        return basicSalary + overtimePay;
//    }
//
//    // Override displayInfo for Clerk
//    @Override
//    public void displayInfo() {
//        System.out.println("Clerk Information:");
//        System.out.println("Name: " + name);
//        System.out.println("Employee ID: " + employeeId);
//        System.out.println("Basic Salary: $" + basicSalary);
//        System.out.println("Overtime Pay: $" + overtimePay);
//        System.out.println("Net Salary: $" + calculateNetSalary());
//    }
//}
//
public class program3 {
//    public static void main(String[] args) {
//        Manager manager = new Manager("John Smith", 101, 5000.0, 1000.0);
//        Clerk clerk = new Clerk("Alice Johnson", 102, 3000.0, 500.0);
//
//        manager.displayInfo();
//        System.out.println();
//        clerk.displayInfo();
//    }
}
