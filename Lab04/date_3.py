from datetime import datetime

current_datetime = datetime.now()

date_without_microseconds = current_datetime.replace(microsecond=0)

print("Current Date with Microseconds:", current_datetime)
print("Current date without Microseconds:", date_without_microseconds)