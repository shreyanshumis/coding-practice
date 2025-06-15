import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class studentreg extends JFrame implements ActionListener {
    private JTextField firstNameField, lastNameField, ageField;
    private JRadioButton maleRadio, femaleRadio;
    private JComboBox<String> courseComboBox;
    private JButton registerButton;

    public studentreg() {
        setTitle("Student Registration Form");

        setLayout(null);

        JLabel firstNameLabel = new JLabel("First Name:");
        JLabel lastNameLabel = new JLabel("Last Name:");
        JLabel ageLabel = new JLabel("Age:");
        JLabel genderLabel = new JLabel("Gender:");
        JLabel courseLabel = new JLabel("Course:");

        firstNameLabel.setBounds(30, 30, 80, 25);
        lastNameLabel.setBounds(30, 70, 80, 25);
        ageLabel.setBounds(30, 110, 80, 25);
        genderLabel.setBounds(30, 150, 80, 25);
        courseLabel.setBounds(30, 190, 80, 25);

        firstNameField = new JTextField();
        lastNameField = new JTextField();
        ageField = new JTextField();

        firstNameField.setBounds(120, 30, 200, 25);
        lastNameField.setBounds(120, 70, 200, 25);
        ageField.setBounds(120, 110, 200, 25);
        maleRadio = new JRadioButton("Male");
        femaleRadio = new JRadioButton("Female");

        maleRadio.setBounds(120, 150, 80, 25);
        femaleRadio.setBounds(200, 150, 80, 25);

        ButtonGroup genderGroup = new ButtonGroup();
        genderGroup.add(maleRadio);
        genderGroup.add(femaleRadio);

        String[] courses = {"Computer Science", "Mathematics", "Physics", "Biology", "Chemistry"};
        courseComboBox = new JComboBox<>(courses);

        courseComboBox.setBounds(120, 190, 200, 25);

        registerButton = new JButton("Register");

        registerButton.setBounds(120, 230, 100, 30);

        registerButton.addActionListener(this);

        add(firstNameLabel);
        add(lastNameLabel);
        add(ageLabel);
        add(genderLabel);
        add(courseLabel);

        add(firstNameField);
        add(lastNameField);
        add(ageField);

        add(maleRadio);
        add(femaleRadio);

        add(courseComboBox);

        add(registerButton);

        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null); // Center the frame
        setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == registerButton) {
            // Retrieve entered data
            String firstName = firstNameField.getText();
            String lastName = lastNameField.getText();
            String age = ageField.getText();
            String gender = maleRadio.isSelected() ? "Male" : "Female";
            String course = (String) courseComboBox.getSelectedItem();

            JOptionPane.showMessageDialog(this,
                    "Registration Successful!\n\n" +
                            "First Name: " + firstName + "\n" +
                            "Last Name: " + lastName + "\n" +
                            "Age: " + age + "\n" +
                            "Gender: " + gender + "\n" +
                            "Course: " + course);
        }
    }

    public static void main(String[] args) {
        new studentreg();
    }
}
