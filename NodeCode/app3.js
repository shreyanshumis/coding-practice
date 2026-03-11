const express = require('express');
const fs = require('fs');

const app = express();

app.get('/read', (req, res) => {

    const filename = req.query.file;

    if (!filename) {
        return res.send("Please provide a file name in query string. Example: /read?file=test.txt");
    }

    let count = 0;

    const interval = setInterval(() => {

        fs.readFile(filename, 'utf8', (err, data) => {

            if (err) {
                clearInterval(interval);
                return res.send("File not found!");
            }

            count++;

            let lines = data.split('\n').length;
            let words = data.split(/\s+/).filter(w => w.length > 0).length;

            res.write(`
                <h3>Read Attempt: ${count}</h3>
                <b>Content:</b><br>${data.replace(/\n/g, "<br>")}<br><br>
                <b>Lines:</b> ${lines} <br>
                <b>Words:</b> ${words}
                <hr>
            `);

        });

    }, 200);

    setTimeout(() => {
        clearInterval(interval);
        res.end("<h2>Reading Stopped</h2>");
    }, 2000); // stops after 2 seconds
});

app.listen(3000, () => {
    console.log("Server running at http://localhost:3000");
});