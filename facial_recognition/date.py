from datetime import datetime

dateTimeObj = datetime.now()
dateObj = dateTimeObj.date()
timeObj = dateTimeObj.time()

print(dateTimeObj)
print(dateObj)
print(timeObj)