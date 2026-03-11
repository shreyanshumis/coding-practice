const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));

// Employee Data (stored at server)
const employees = [
    { name: "Shreyanshu", department: "HR", salary: 40000 },
    { name: "Someone", department: "IT", salary: 50000 },
    { name: "Anyone", department: "Finance", salary: 60000 },
    { name: "Noone", department: "Marketing", salary: 45000 }
];

// Show Form
app.get('/', (req, res) => {
    let formHTML = `
        <h2>Select Employees</h2>
        <form method="POST" action="/calculate">
    `;

    employees.forEach((emp, index) => {
        formHTML += `
            <input type="checkbox" name="emp" value="${index}">
            ${emp.name} - ${emp.department} - ₹${emp.salary}<br>
        `;
    });

    formHTML += `<br><button type="submit">Calculate Total Salary</button></form>`;
    res.send(formHTML);
});

// Calculate Total Salary
app.post('/calculate', (req, res) => {
    let selected = req.body.emp;
    let total = 0;

    if (!selected) {
        return res.send("No employees selected");
    }

    if (!Array.isArray(selected)) {
        selected = [selected];
    }

    selected.forEach(i => {
        total += employees[i].salary;
    });

    res.send(`<h2>Total Salary = ₹${total}</h2>`);
});

app.listen(3000, () => {
    console.log("Server running at http://localhost:3000");
});