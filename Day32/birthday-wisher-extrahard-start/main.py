##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import smtplib
import random

MY_EMAIL= "youremail@gmail.com"
MY_PASSWORD= "xxxx xxxx xxxx xxxx"
# 1. Update the birthdays.csv
data = pd.read_csv("Day32/birthday-wisher-extrahard-start/birthdays.csv")
# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
today_tuple = (today.month, today.day)

birthday_dict = {(row['month'], row['day']): row for (index,row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    file_path = f"Day32/birthday-wisher-extrahard-start/letter_templates/letter_{random.choice([1,2,3])}.txt"
    with open(file_path, 'r') as letter:
        content = letter.read()
        content = content.replace('[NAME]', birthday_person['name'])
# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person['email'], msg=f"Subject:This is my birthday\n\n{content}")


