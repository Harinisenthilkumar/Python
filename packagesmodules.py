# DATE 

import datetime as dt
o1=dt.date.today()
print(o1) # current date

new_date =dt.date(2002,10,29)
print(new_date)
print("year",new_date.year)
print("month",new_date.month)
print("day",new_date.day)

# TIME

new_time = dt.time(11,48,50,10)
print(new_time)
print("hour",new_time.hour)
print("minute",new_time.minute)
print("second",new_time.second)
print("microsecond",new_time.microsecond)


