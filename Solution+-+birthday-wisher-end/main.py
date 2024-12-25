from datetime import datetime
import pandas as pd
import random
import smtplib

# Update with your email details
MY_EMAIL = "thisismjeyz@gmail.com"
MY_PASSWORD = "nwhk ywod grxh sfcc"

# Get today's date
today = datetime.now()
today_tuple = (today.month, today.day)

# Read birthday data
data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# Check if today matches a birthday
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    try:
        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", birthday_person["name"])

        # Send email
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_person["email"],
                msg=f"Subject:Happy Birthday!\n\n{contents}"
            )
        print(f"Birthday email sent to {birthday_person['name']} ({birthday_person['email']})!")
    except FileNotFoundError:
        print(f"Error: Letter template {file_path} not found.")
    except smtplib.SMTPAuthenticationError:
        print("SMTP Authentication Error: Please check your email credentials.")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("No birthdays today.")
