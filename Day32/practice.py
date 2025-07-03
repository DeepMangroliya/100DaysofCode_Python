import smtplib
import datetime as dt
import random
from email.message import EmailMessage

MY_EMAIL= "youremail@gmail.com"
MY_PASSWORD= "yyyy yyyy yyyy yyyy"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt", "r") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes).strip()

    msg = EmailMessage()
    msg["Subject"] = "This is my first email"
    msg["From"] = MY_EMAIL
    msg["To"] = MY_EMAIL
    msg.set_content(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.send_message(msg)
        