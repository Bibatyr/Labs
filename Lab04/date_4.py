from datetime import datetime

date1 = datetime(2024, 2, 17, 12, 30, 0)
date2 = datetime(2024, 2, 19, 10, 15, 0)

difference = date2 - date1

difference_in_seconds = difference.total_seconds()

print("Difference between two dates in seconds:", difference_in_seconds)