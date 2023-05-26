<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Email Exchange Rate Tracker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
        }

        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }

        h1 {
            color: #333;
            text-align: center;
        }

        p {
            margin-bottom: 10px;
        }

        code {
            background-color: #f1f1f1;
            padding: 2px 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Email Exchange Rate Tracker</h1>

        <p>This project is a simple web application that allows users to input their email address and receive the current exchange rate for the dollar. The application fetches the exchange rate from an external source and sends it to the user's email address.</p>

        <h2>Usage</h2>

        <ol>
            <li>Clone the repository:<br><code>git clone https://github.com/your-username/email-exchange-rate-tracker.git</code></li>
            <li>Install the required dependencies:<br><code>pip install -r requirements.txt</code></li>
            <li>Set up the necessary environment variables:<br>
                <ul>
                    <li><code>SMTP_USER</code>: Your email address (sender's address)</li>
                    <li><code>SMTP_PASSWORD</code>: Your email account password</li>
                    <li><code>SMTP_SERVER</code>: Your email provider's SMTP server</li>
                    <li><code>SMTP_PORT</code>: SMTP server port (e.g., 587)</li>
                </ul>
            </li>
            <li>Run the application:<br><code>uvicorn main:app --reload</code></li>
            <li>Open your web browser and navigate to <a href="http://localhost:8000">http://localhost:8000</a>.</li>
            <li>Enter your email address and click "Submit".</li>
            <li>Check your email inbox for the exchange rate notification.</li>
        </ol>

        <h2>Technologies Used</h2>

        <ul>
            <li>Python</li>
            <li>FastAPI</li>
            <li>HTML</li>
            <li>CSS</li>
        </ul>

        <h2>License</h2>

        <p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>
    </div>
</body>
</html>
