##################### Normal Starting Project ######################
import random
import smtplib
import pandas
import datetime as dt


# Read birthdays from the CSV file
birthdays = pandas.read_csv("birthdays.csv")

# Get today's month and day
now = dt.datetime.now()
today = (now.month, now.day)

# Iterate through each row in the DataFrame
for index, birthday in birthdays.iterrows():
    # Extract month and day from the current row
    month = birthday['month']
    day = birthday['day']

    # Check if today matches the birthday
    if today == (month, day):
        # Randomly select a letter template
        template_num = random.randint(1, 3)  # Assuming there are 3 letter templates
        template_path = f"letter_templates/letter_{template_num}.txt"

        # Read the content of the selected letter template
        with open(template_path, "r") as template_file:
            letter_content = template_file.read()

        # Replace [NAME] with the person's actual name
        customized_letter = letter_content.replace("[NAME]", birthday['name'])

        # Print or save the customized letter
        print(customized_letter)


my_email = "mytest@gmail.com"
password = "fs23s21s23s212s31"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs="test71@gmail.com",msg=f"Subject:Birthday Wishes\n\n {customized_letter}")

