const express = require('express');
const multer = require('multer');
const path = require('path');

const app = express();

// -------- STORAGE SETUP --------
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, 'uploads/');
    },
    filename: (req, file, cb) => {
        cb(null, file.originalname);
    }
});

const upload = multer({ storage });


// -------- FORM PAGE --------
app.get('/', (req, res) => {
    res.send(`
        <h2>Upload PDF File</h2>

        <form method="POST" action="/upload" enctype="multipart/form-data">
            <input type="file" name="myfile" required><br><br>
            <button type="submit">UPLOAD</button>
        </form>
    `);
});


// -------- UPLOAD + VALIDATION --------
app.post('/upload', upload.single('myfile'), (req, res) => {

    const file = req.file;

    if (!file) {
        return res.send("No file selected");
    }

    const ext = path.extname(file.originalname).toLowerCase();

    if (ext !== '.pdf') {

        return res.send(`
            <h3>Invalid File! Only PDF allowed</h3>
            <a href="/">Try Again</a>
        `);
    }

    res.send(`
        <h3>Valid PDF Uploaded Successfully!</h3>
        File Name: ${file.originalname}
    `);
});


// -------- START SERVER --------
app.listen(3000, () => {
    console.log("Server running at http://localhost:3000");
});