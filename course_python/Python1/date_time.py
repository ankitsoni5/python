from datetime import date, datetime
from datetime import timedelta

today = date.today()

print(today)
print(today.year)
print(today.month)
print(today.day)
print(type(today))

# print specific date

birthday= date(year=1994,month=3,day=17)
print(birthday)

# replace: pass only parameter which need to be replaced on current obj

upcomming_bday = birthday.replace(year=today.year)
print(upcomming_bday)

# Date format

formate_date = upcomming_bday.strftime('%d/%m/%Y')
print(formate_date)
print(upcomming_bday.strftime('%d-%B-%Y'))

#Create a date obj which is 1 week from now.
# we have to create a delta which can be added to today to manipulate the date
one_week_add = timedelta(weeks=1) # give the week to jump. here 1 is given to add 1 week in today
one_week_ahead = today + one_week_add
print(one_week_ahead) 

# a date obj which is 2 weeks and 15 days from now
add = timedelta(weeks=2, days=15)
new1 = today + add
print(new1)

# create a date obj which is 2 weeks 15 day in the past from now
print(today-add)

# datetime
dtime = datetime.now()
print(dtime)
print(type(dtime))
print(dtime.day,dtime.minute,dtime.year,dtime.hour)
print(dtime.date())
print(dtime.time())

# comparing date and time using relational operation
print(today > upcomming_bday)
print(today == dtime.date())