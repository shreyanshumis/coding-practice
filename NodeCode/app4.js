const express = require('express');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');

const app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(cookieParser());


// -------- 1. FORM PAGE --------
app.get('/captureData', (req, res) => {
    res.send(`
        <h2>Course Form</h2>

        <form method="POST" action="/setCookies">
            Course Code: <input type="text" name="coursecode"><br><br>
            Course Name: <input type="text" name="coursename"><br><br>
            School: <input type="text" name="schoolname"><br><br>
            Credits: <input type="number" name="credit"><br><br>

            <button type="submit">Submit Data</button>
        </form>

        <br>
        <a href="/getAllCookies">List All Cookies</a>
    `);
});


// -------- 2. SET COOKIES + REDIRECT --------
app.post('/setCookies', (req, res) => {

    const course = {
        coursecode: req.body.coursecode,
        coursename: req.body.coursename,
        schoolname: req.body.schoolname,
        credit: req.body.credit
    };

    const myinfo = {
        title: "SERVER METADATA",
        name: "APACHE",
        version: "12.5",
        region: "ATLANTA"
    };

    res.cookie('course', JSON.stringify(course));
    res.cookie('myinfo', JSON.stringify(myinfo));

    res.redirect('/getCookies/course');
});


// -------- 3. SHOW COURSE COOKIE --------
app.get('/getCookies/course', (req, res) => {

    if (!req.cookies.course) {
        return res.send("No course cookie found");
    }

    res.send(JSON.parse(req.cookies.course));
});


// -------- 4. SHOW ALL COOKIES --------
app.get('/getAllCookies', (req, res) => {

    if (!req.cookies.course || !req.cookies.myinfo) {
        return res.send("No cookies found");
    }

    res.send({
        course: JSON.parse(req.cookies.course),
        myinfo: JSON.parse(req.cookies.myinfo)
    });
});


// -------- START SERVER --------
app.listen(8000, () => {
    console.log("Server running at http://localhost:8000/captureData");
});