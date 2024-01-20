import datetime

print("************************************")
print(
    "Built-In datetime module" + "\n"
    "========================="
)
print("************************************")

future_date = datetime.date(2222, 9, 20)
print("Future date: ", future_date)

print(future_date.year)
print(future_date.month)
print(future_date.day)

some_time = datetime.time(16,34, 52)
print("Some time: ", some_time)

print(some_time.hour)
print(some_time.minute)
print(some_time.second)

print("************************************")
print(
    "Using the datetime class" + "\n"
    "========================="
)
print("************************************")

from datetime import datetime

future_datetime = datetime(2100, 10, 12, 20, 50, 15)
print("Future date and time: ", future_datetime)

print(dir(datetime))

print(future_datetime.hour)

print("Formatted date: ", future_datetime.strftime("%B %d %Y")) # October 12 2100
print("Formatted date: ", future_datetime.strftime("%I:%M %p")) # 08:50 PM
print("Formatted date and Time: ", future_datetime.strftime("%A, %B %d, %Y %I:%M %p")) # Tuesday, October 12, 2100 08:50 PM
print("Formatted month ", future_datetime.strftime("%B"))
print("Formatted date: ", future_datetime.strftime("%Y"))

print("************************************")
print(
        "Converting Strings to Datetime" + "\n"
        "==============================="
)
print("************************************")

formatted_datetime_str = "3000-11-20 14:25:45"

parsed_datetime = datetime.strptime(formatted_datetime_str, "%Y-%m-%d %H:%M:%S")
print(parsed_datetime)
print(parsed_datetime.year)

parsed_date = datetime.strptime("June 03, 2050", "%B %d, %Y")
print(parsed_date)
parsed_time = datetime.strptime("10:12 AM", "%I:%M %p")
print(parsed_time)
parsed_month = datetime.strptime("June", "%B")
print(parsed_month)
parsed_year = datetime.strptime("2222", "%Y")

print("************************************")
print(
        "Working With the Timedelta Class" + "\n"
        "==============================="
)
print("************************************")

from datetime import datetime, timedelta

future_datetime = datetime(2100, 12, 10, 18, 10, 45)
print("Original date: ", future_datetime)
print(future_datetime + timedelta(days = 100))
print(future_datetime + timedelta(hours = 3))
print(future_datetime + timedelta(days = 3, hours = 5, minutes = 15))
print(future_datetime - timedelta(days = 365, hours=24))


print("************************************")
print(
        "Build-In Time Module" + "\n"
        "==============================="
)
print("************************************")

import time
current_time_in_seconds = time.time()
print(current_time_in_seconds)
print(time.ctime(current_time_in_seconds))
print(time.ctime(23423423423))
start_time = time.time()
print('start : ', start_time)
time.sleep(3)
my_list = list(range(10_000_000))
print(my_list[1000000])
end_time = time.time()
print('continue : ', end_time)
print('Time spend : ', round(end_time-start_time, 2))


