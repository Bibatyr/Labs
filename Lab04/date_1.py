from datetime import datetime, timedelta

current_date = datetime.now()

new_date = current_date - timedelta(days = 5)

print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("New date(after subtracting five days):", new_date.strftime("%Y-%m-%d"))