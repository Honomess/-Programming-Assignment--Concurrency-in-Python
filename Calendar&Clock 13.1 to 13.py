# 13.1 to 13.3

from datetime import date, datetime

# 13.1 Write the current date as a string to today.txt
today = date.today()
with open("today.txt", "w") as file:
    file.write(today.isoformat())

print("Current date written to today.txt")

# 13.2 Read the text file today.txt into the string today_string
with open("today.txt", "r") as file:
    today_string = file.read()

print("Date read from file:", today_string)

# 13.3 Parse the date from today_string
parsed_date = datetime.strptime(today_string, "%Y-%m-%d")

print("Parsed date:", parsed_date)