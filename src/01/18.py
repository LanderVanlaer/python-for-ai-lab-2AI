# Timedelta objects don’t have an easy-to-use strftime method.
# Create a custom function 'mystrfdelta'which extracts the number of days and seconds
# (using timedelta_object.days and timedelta_object.seconds). Using the days and seconds,
# calculate in that function the number of days, hours, minutes and seconds and return them as a tuple.
#
# Example:
#   date1 = datetime.now()
#   date2 = datetime(2021, 9, 20)
#   diff = date2 - date1
#   print(diff)
#   print(mystrfdelta(diff))
#
#   6 days, 8:36:46.337900
#   (6, 8, 36, 46)

from datetime import datetime, timedelta


def mystrfdelta(d: timedelta):
    days = d.days
    hours = d.seconds // 3600
    minutes = (d.seconds - hours * 3600) // 60
    seconds = d.seconds - minutes * 60 - hours * 3600
    return days, hours, minutes, seconds


date1 = datetime.now()
date2 = datetime(2023, 2, 28, 3)
diff = date2 - date1
print(diff)
print(mystrfdelta(diff))
