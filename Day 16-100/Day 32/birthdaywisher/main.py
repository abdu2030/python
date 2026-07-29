import smtplib
import pandas
import datetime as dt
import random


MY_EMAIL = "abduade324@gmail.com"
MY_PASSWORD = "exwx tfic fvww icte"


# Get today's date.
today = dt.datetime.now()

# Store today's month and day as a tuple.
# Example: July 29 becomes (7, 29).
today_tuple = (today.month, today.day)


# Read birthdays.csv using pandas.
birthday_data = pandas.read_csv("birthdays.csv")


# Convert the CSV data into a dictionary.
# The key is (month, day).
# The value is the person's complete CSV row.
birthday_dictionary = {
    (row["month"], row["day"]): row
    for index, row in birthday_data.iterrows()
}


# Check whether today's month and day exist in the dictionary.
if today_tuple in birthday_dictionary:
    birthday_person = birthday_dictionary[today_tuple]

    # Randomly choose letter_1.txt, letter_2.txt, or letter_3.txt.
    random_letter_number = random.randint(1, 3)

    # Open and read the randomly selected letter.
    with open(
        f"letter_templates/letter_{random_letter_number}.txt",
        "r",
        encoding="utf-8",
    ) as letter_file:
        letter_content = letter_file.read()

    # Replace [NAME] with the birthday person's real name.
    personalised_letter = letter_content.replace(
        "[NAME]",
        birthday_person["name"],
    )

    # Connect to Gmail's SMTP server.
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # Secure the connection.
        connection.starttls()

        # Log in to the sender's Gmail account.
        connection.login(
            user=MY_EMAIL,
            password=MY_PASSWORD,
        )

        # Send the birthday email.
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=(
                f"Subject:Happy Birthday!\n\n"
                f"{personalised_letter}"
            ),
        )

    print(f"Birthday email sent to {birthday_person['name']}.")

else:
    print("No birthday today.")