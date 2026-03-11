const express = require('express');
const bodyParser = require('body-parser');
const session = require('express-session');

const app = express();

app.use(bodyParser.urlencoded({ extended: true }));

app.use(session({
    secret: "loginSecret",
    resave: false,
    saveUninitialized: true
}));


// -------- JSON USER DATA --------
let users = [
    { UserID: "101", Password: "pass1", Username: "Shreyanshu", Failure_Attempt: 0 },
    { UserID: "102", Password: "pass2", Username: "hjdwhhd", Failure_Attempt: 0 }
];


// -------- LOGIN PAGE --------
app.get('/', (req, res) => {

    res.send(`
        <h2>Login</h2>

        <form method="POST" action="/login">
            UserID: <input type="text" name="userid"><br><br>
            Password: <input type="password" name="password"><br><br>
            <button type="submit">Login</button>
        </form>
    `);
});


// -------- LOGIN LOGIC --------
app.post('/login', (req, res) => {

    const { userid, password } = req.body;

    let user = users.find(u => u.UserID === userid);

    if (!user) {
        return res.send("Invalid UserID");
    }

    // If already locked
    if (user.Failure_Attempt >= 3) {
        return res.send("<h2>WARNING: Account Locked due to 3 Failed Attempts</h2>");
    }

    if (user.Password === password) {

        user.Failure_Attempt = 0;
        req.session.user = user.Username;

        res.send(`
            <h2>Welcome ${user.Username}</h2>
        `);

    } else {

        user.Failure_Attempt += 1;

        if (user.Failure_Attempt >= 3) {
            return res.send("<h2>WARNING: Account Locked due to 3 Failed Attempts</h2>");
        }

        res.send(`
            <h3>Login Failed! Attempt: ${user.Failure_Attempt}</h3>
            <a href="/">Try Again</a>
        `);
    }

});


// -------- START SERVER --------
app.listen(3000, () => {
    console.log("Server running at http://localhost:3000");
});