import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class AddressBook extends JFrame {
    private DefaultTableModel tableModel;
    private JTable contactTable;

    public AddressBook() {
        super("Address Book");

        tableModel = new DefaultTableModel();
        tableModel.addColumn("Name");
        tableModel.addColumn("Phone Number");
        tableModel.addColumn("Email");

        contactTable = new JTable(tableModel);

        JButton addButton = new JButton("Add");
        JButton editButton = new JButton("Edit");
        JButton deleteButton = new JButton("Delete");

        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                addContact();
            }
        });

        editButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                editContact();
            }
        });

        deleteButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                deleteContact();
            }
        });

        JPanel buttonPanel = new JPanel();
        buttonPanel.add(addButton);
        buttonPanel.add(editButton);
        buttonPanel.add(deleteButton);

        getContentPane().setLayout(new BorderLayout());
        getContentPane().add(new JScrollPane(contactTable), BorderLayout.CENTER);
        getContentPane().add(buttonPanel, BorderLayout.SOUTH);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(500, 300);
        setLocationRelativeTo(null);
        setVisible(true);
    }

    private void addContact() {
        String name = JOptionPane.showInputDialog(this, "Enter Name:");
        String phoneNumber = JOptionPane.showInputDialog(this, "Enter Phone Number:");
        String email = JOptionPane.showInputDialog(this, "Enter Email:");
        tableModel.addRow(new Object[]{name, phoneNumber, email});
    }

    private void editContact() {
        int selectedRow = contactTable.getSelectedRow();
        if (selectedRow == -1) {
            JOptionPane.showMessageDialog(this, "Please select a contact to edit.");
            return;
        }

        String name = (String) tableModel.getValueAt(selectedRow, 0);
        String phoneNumber = (String) tableModel.getValueAt(selectedRow, 1);
        String email = (String) tableModel.getValueAt(selectedRow, 2);

        String editedName = JOptionPane.showInputDialog(this, "Edit Name:", name);
        String editedPhoneNumber = JOptionPane.showInputDialog(this, "Edit Phone Number:", phoneNumber);
        String editedEmail = JOptionPane.showInputDialog(this, "Edit Email:", email);

        tableModel.setValueAt(editedName, selectedRow, 0);
        tableModel.setValueAt(editedPhoneNumber, selectedRow, 1);
        tableModel.setValueAt(editedEmail, selectedRow, 2);
    }

    private void deleteContact() {
        int selectedRow = contactTable.getSelectedRow();
        if (selectedRow == -1) {
            JOptionPane.showMessageDialog(this, "Please select a contact to delete.");
            return;
        }
        tableModel.removeRow(selectedRow);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new AddressBook();
            }
        });
    }
}
