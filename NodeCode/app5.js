const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));

// -------- PRODUCT DATA (SERVER SIDE) --------
const products = [
    { name: "Dinner Set", color: "White", price: 2500 },
    { name: "Fashion Set", color: "Red", price: 1800 },
    { name: "Table Set", color: "Brown", price: 3000 },
    { name: "Fabric Set", color: "Blue", price: 1500 }
];


// -------- 1. FORM PAGE --------
app.get('/', (req, res) => {

    let form = `
        <h2>Product Selection</h2>
        <form method="POST" action="/bill">
    `;

    products.forEach((p, i) => {
        form += `
            <input type="checkbox" name="prod" value="${i}">
            ${p.name} (${p.color}) - ₹${p.price}<br>
        `;
    });

    form += `
        <br>
        <button type="submit">GENERATE BILL</button>
        </form>
    `;

    res.send(form);
});


// -------- 2. BILL GENERATION --------
app.post('/bill', (req, res) => {

    let selected = req.body.prod;
    let total = 0;

    if (!selected) {
        return res.send(`
            <h3>No product selected</h3>
            <a href="/">Go Back</a>
        `);
    }

    if (!Array.isArray(selected)) {
        selected = [selected];
    }

    selected.forEach(i => {
        total += products[i].price;
    });

    res.send(`
        <h2>Total Price = ₹${total}</h2>
        <a href="/">CLICK HERE TO ORDER AGAIN</a>
    `);
});


// -------- START SERVER --------
app.listen(3000, () => {
    console.log("Server running at http://localhost:3000");
});