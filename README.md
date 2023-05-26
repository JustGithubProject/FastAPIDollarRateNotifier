# Email Exchange Rate Tracker

This project is a simple web application that allows users to input their email address and receive the current exchange rate for the dollar. The application fetches the exchange rate from an external source and sends it to the user's email address.

## Usage

1. Clone the repository: git clone https://github.com/your-username/email-exchange-rate-tracker.git
2. Install the required dependencies: pip install -r requirements.txt
3. Set up the necessary environment variables:
- `SMTP_USER`: Your email address (sender's address)
- `SMTP_PASSWORD`: Your email account password
- `SMTP_SERVER`: Your email provider's SMTP server
- `SMTP_PORT`: SMTP server port (e.g., 587)
4. Run the application: uvicorn main:app --reload

5. Open your web browser and navigate to [http://localhost:8000](http://localhost:8000).

6. Enter your email address and click "Submit".

7. Check your email inbox for the exchange rate notification.

## Technologies Used

- Python
- FastAPI
- HTML
- CSS
