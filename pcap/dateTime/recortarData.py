import datetime

dt=datetime.datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%Y/%m/%d %H:%M:%S"))
print(dt.strftime("%a, %Y %b  %d"))
print(dt.strftime("%A, %Y %B  %d"))
print(dt.strftime("%A: %w"))
print(dt.strftime("Day of the year: %j"))
print(dt.strftime("Week number of the year: %W"))
