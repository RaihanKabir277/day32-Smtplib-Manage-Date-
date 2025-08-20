
import datetime as dt

now = dt.datetime.now()

# print(now)
year = now.year
month = now.month
hour = now.hour
minitue = now.minute
microsecond = now.microsecond

# print(microsecond)

day_of_week = now.weekday()
# print(day_of_week)

date_of_birth = dt.datetime(year=2024, month=12, day=15)
print(date_of_birth)

