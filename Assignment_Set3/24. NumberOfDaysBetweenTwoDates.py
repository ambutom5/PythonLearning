# 24. Calculate number of days between two given dates.

from datetime import datetime,date

date1 = date(2026,8,6)
date2 = date(2026,8,2)
datediff = date1 - date2
print(datediff.days)


date1 = "05-10-1990"
date2 = "24-08-2026"
date1 = datetime.strptime(date1,"%d-%m-%Y").date()
date2 = datetime.strptime(date2,"%d-%m-%Y").date()
datediff = date2 - date1
print(datediff.days)


