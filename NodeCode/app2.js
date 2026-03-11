const express = require('express');
const session = require('express-session');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.urlencoded({ extended: true }));

app.use(session({
    secret: "secretKey",
    resave: false,
    saveUninitialized: true
}));

// -------- FORM PAGE --------
app.get('/', (req, res) => {
    res.send(`
        <h2>Session Manager</h2>

        <form method="POST" action="/save">
            Key: <input type="text" name="key" required><br><br>
            Value: <input type="text" name="value" required><br><br>
            <button type="submit">Create / Update</button>
        </form>

        <br>

        <form action="/view" method="GET">
            <button type="submit">View All Sessions</button>
        </form>
    `);
});

// -------- CREATE / UPDATE --------
app.post('/save', (req, res) => {

    const { key, value } = req.body;

    if (!req.session.data) {
        req.session.data = {};
    }

    let msg = req.session.data[key]
        ? "Session Updated"
        : "Session Created";

    req.session.data[key] = value;

    res.send(`
        <h3>${msg}</h3>
        ${key} : ${value}
        <br><br>
        <a href="/">Back</a>
    `);
});

// -------- VIEW ALL --------
app.get('/view', (req, res) => {

    if (!req.session.data) {
        return res.send(`
            <h3>No session variables found</h3>
            <a href="/">Back</a>
        `);
    }

    let output = "<h2>Active Sessions</h2>";

    for (let key in req.session.data) {
        output += `${key} : ${req.session.data[key]} <br>`;
    }

    res.send(output + `<br><a href="/">Back</a>`);
});

app.listen(3000, () => {
    console.log("Server running on http://localhost:3000");
});