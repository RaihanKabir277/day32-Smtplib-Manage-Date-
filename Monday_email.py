import smtplib
import datetime as dt
import random

my_email = "ra............"


now = dt.datetime.now()
weekday = now.weekday()

if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    # 
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password="**************")
        connection.sendmail(from_addr=my_email,to_addrs="----@yahoo.com", msg=f"Subject: Well wishers\n\n{quote}")

