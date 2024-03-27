# importing date and time in a variable
import datetime as dt
# storing today's date
today = dt.date.today()
print(today.month)
print(today.day)
print(today.year)
#store a date new year
new_year = dt.date(2024,1,1)
print(new_year.month)
print(new_year.day)
print(new_year.year)