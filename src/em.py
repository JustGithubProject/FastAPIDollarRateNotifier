import smtplib
from email.message import EmailMessage
from src.config import SMTP_USER, SMTP_PASSWORD
from bs4 import BeautifulSoup as bs4
import requests


SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465


def get_email_template_dashboard(email_of_user: str):
    email = EmailMessage()
    email['Subject'] = 'USDtoUAH'
    email['From'] = SMTP_USER
    email['To'] = email_of_user

    url = "https://wise.com/ru/currency-converter/usd-to-uah-rate"
    req = requests.get(url)
    soup = bs4(req.text, "html.parser")
    span = soup.find("span", class_="text-success")
    if span is not None:
        rate = str(span.text)[0:5]
    else:
        rate = "36.00"

    html_content = f'''
    <html>
      <head>
        <style>
          body {{
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
          }}

          .container {{
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
          }}

          .header {{
            background-color: #007bff;
            padding: 20px;
            color: #fff;
            text-align: center;
          }}

          .content {{
            background-color: #fff;
            padding: 20px;
            margin-top: 20px;
          }}

          .rate {{
            font-size: 24px;
            color: #007bff;
            margin-top: 0;
          }}

          .footer {{
            background-color: #f5f5f5;
            padding: 20px;
            text-align: center;
            font-size: 12px;
            color: #777;
          }}
        </style>
      </head>
      <body>
        <div class="container">
          <div class="header">
            <h1>Здравствуйте, {email_of_user}!</h1>
          </div>
          <div class="content">
            <h2>Вот и ваш отчет:</h2>
            <p class="rate">1 USD = {rate} UAH</p>
          </div>
          <div class="footer">
            <p>С уважением,</p>
            <p>Ваша команда</p>
          </div>
        </div>
      </body>
    </html>
    '''

    email.add_alternative(html_content, subtype='html')
    return email


def send_email_report_dashboard(email: str):
    email = get_email_template_dashboard(email)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)


