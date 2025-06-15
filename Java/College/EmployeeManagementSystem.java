import java.sql.*;
import java.util.Scanner;

public class EmployeeManagementSystem {

    private static final String JDBC_URL = "jdbc:mysql://localhost:3306/your_database_name";
    private static final String JDBC_USER = "your_username";
    private static final String JDBC_PASSWORD = "your_password";

    public static void main(String[] args) {
        try (Connection connection = DriverManager.getConnection(JDBC_URL, JDBC_USER, JDBC_PASSWORD)) {
            initializeDatabase(connection);
            showMenu(connection);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private static void initializeDatabase(Connection connection) throws SQLException {
        try (Statement statement = connection.createStatement()) {
            String createTableSQL = "CREATE TABLE IF NOT EXISTS Employee (" +
                    "employee_id INT PRIMARY KEY AUTO_INCREMENT," +
                    "name VARCHAR(255) NOT NULL," +
                    "designation VARCHAR(255) NOT NULL," +
                    "salary DOUBLE NOT NULL)";
            statement.executeUpdate(createTableSQL);
        }
    }

    private static void showMenu(Connection connection) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Employee Management System");
            System.out.println("1. Add Employee");
            System.out.println("2. View Employee Details");
            System.out.println("3. Update Employee Details");
            System.out.println("4. Delete Employee");
            System.out.println("5. Exit");

            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    addEmployee(connection);
                    break;
                case 2:
                    viewEmployeeDetails(connection);
                    break;
                case 3:
                    updateEmployeeDetails(connection);
                    break;
                case 4:
                    deleteEmployee(connection);
                    break;
                case 5:
                    System.out.println("Exiting...");
                    scanner.close();
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid choice. Please enter a valid option.");
            }
        }
    }

    private static void addEmployee(Connection connection) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Adding Employee...");

        System.out.print("Enter employee name: ");
        String name = scanner.nextLine();

        System.out.print("Enter employee designation: ");
        String designation = scanner.nextLine();

        System.out.print("Enter employee salary: ");
        double salary = scanner.nextDouble();

        try (PreparedStatement preparedStatement = connection.prepareStatement(
                "INSERT INTO Employee (name, designation, salary) VALUES (?, ?, ?)")) {

            preparedStatement.setString(1, name);
            preparedStatement.setString(2, designation);
            preparedStatement.setDouble(3, salary);

            int rowsAffected = preparedStatement.executeUpdate();

            if (rowsAffected > 0) {
                System.out.println("Employee added successfully!");
            } else {
                System.out.println("Failed to add employee.");
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private static void viewEmployeeDetails(Connection connection) {
        System.out.println("Viewing Employee Details...");

        try (Statement statement = connection.createStatement()) {
            ResultSet resultSet = statement.executeQuery("SELECT * FROM Employee");

            while (resultSet.next()) {
                int employeeId = resultSet.getInt("employee_id");
                String name = resultSet.getString("name");
                String designation = resultSet.getString("designation");
                double salary = resultSet.getDouble("salary");

                System.out.println("Employee ID: " + employeeId);
                System.out.println("Name: " + name);
                System.out.println("Designation: " + designation);
                System.out.println("Salary: " + salary);
                System.out.println("---------------------");
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private static void updateEmployeeDetails(Connection connection) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Updating Employee Details...");

        System.out.print("Enter employee ID to update: ");
        int employeeId = scanner.nextInt();

        try (PreparedStatement preparedStatement = connection.prepareStatement(
                "SELECT * FROM Employee WHERE employee_id = ?")) {

            preparedStatement.setInt(1, employeeId);

            ResultSet resultSet = preparedStatement.executeQuery();

            if (resultSet.next()) {
                // Employee found, proceed with update
                System.out.print("Enter new name: ");
                String newName = scanner.next();

                System.out.print("Enter new designation: ");
                String newDesignation = scanner.next();

                System.out.print("Enter new salary: ");
                double newSalary = scanner.nextDouble();

                try (PreparedStatement updateStatement = connection.prepareStatement(
                        "UPDATE Employee SET name=?, designation=?, salary=? WHERE employee_id=?")) {

                    updateStatement.setString(1, newName);
                    updateStatement.setString(2, newDesignation);
                    updateStatement.setDouble(3, newSalary);
                    updateStatement.setInt(4, employeeId);

                    int rowsAffected = updateStatement.executeUpdate();

                    if (rowsAffected > 0) {
                        System.out.println("Employee details updated successfully!");
                    } else {
                        System.out.println("Failed to update employee details.");
                    }

                }

            } else {
                System.out.println("Employee not found with ID: " + employeeId);
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private static void deleteEmployee(Connection connection) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Deleting Employee...");

        System.out.print("Enter employee ID to delete: ");
        int employeeId = scanner.nextInt();

        try (PreparedStatement preparedStatement = connection.prepareStatement(
                "DELETE FROM Employee WHERE employee_id = ?")) {

            preparedStatement.setInt(1, employeeId);

            int rowsAffected = preparedStatement.executeUpdate();

            if (rowsAffected > 0) {
                System.out.println("Employee deleted successfully!");
            } else {
                System.out.println("Failed to delete employee.");
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
