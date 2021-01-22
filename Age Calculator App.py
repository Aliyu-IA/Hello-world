# import datetime module
import datetime

# call the current calender with .now method
now = datetime.datetime.now()

# create an input func asking for your current age
what_is_your_age = int(input("Age? "))

# Substract current year with age to get the year you were born
year_you_were_born = now.year - what_is_your_age
print(f'You were born in : {year_you_were_born}')
