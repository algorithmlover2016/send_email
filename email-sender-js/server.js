const express = require('express');
const bodyParser = require('body-parser');
const nodemailer = require('nodemailer');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.json());
app.use(express.static('public')); // Serve static files from public directory

// Nodemailer transporter setup
let transporter = nodemailer.createTransport({
    service: 'gmail', // Use your email service
    auth: {
        user: process.env.EMAIL_USER, // Load user from .env file
        pass: process.env.EMAIL_PASS  // Load pass from .env file
    }
});

app.post('/submit-email', (req, res) => {
    const { email } = req.body;
    
    if (!email) {
        return res.status(400).send('Email is required');
    }
    
    let mailOptions = {
        from: process.env.EMAIL_USER,
        to: email,
        subject: 'Hello!',
        text: `Hello, ${email}!`
    };
    
    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            console.log(error);
            return res.status(500).send('Error sending email');
        }
        
        console.log('Email sent: ' + info.response);
        res.status(200).send('Email sent');
    });
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
