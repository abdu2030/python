import smtplib
import datetime as dt
import random

my_email = "abduade324@gmail.com"
password = "exwx tfic fvww icte"

now = dt.datetime.now()
year = now.year
day_of_the_week = now.weekday()

if day_of_the_week == 2:
    with open("quotes.txt", "r", encoding="utf-8") as file:
        content = file.readlines()
        random_line = random.choice(content)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="abdulkerimadem453@gmail.com",
            msg=f"Subject: Motivation\n\n{random_line}"
        )







