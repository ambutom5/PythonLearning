import datetime

x = datetime.datetime.now()
print("Current Date & Time   :",x)
print("Abbreviated Weekday    :",x.strftime("%a"))
print("Full Weekday           :",x.strftime("%A"))
print("Abbreviated Month      :",x.strftime("%b"))
print("Full month             :",x.strftime("%B"))
print("Abbreviated year       :",x.strftime("%y"))
print("Full year              :",x.strftime("%Y"))

print("Hour(12 Hour Format)   :",x.strftime("%I"))
print("Time - Minute          :",x.strftime("%M"))
print("Hour(24 Hour Format)   :",x.strftime("%H"))
print("Time - Minute          :",x.strftime("%M"))
print("AM/PM                  :",x.strftime("%p"))

print("Local version of date  :",x.strftime("%x"))
print("Local version of time  :",x.strftime("%X"))

print(x.strftime("%Y-%m-%d %H:%M:%S"))
print("Today is",x.strftime("%A, %B %d, %Y"))

# | **Code** | **Meaning** | **Example Output** |
# | --- | --- | --- |
# | ``%Y`` | Year (4 digits) | ``2026`` |
# | ``%y`` | Year (2 digits) | ``26`` |
# | ``%m`` | Month (01–12) | ``08`` |
# | ``%B`` | Full month name | ``August`` |
# | ``%b`` | Abbreviated month name | ``Aug`` |
# | ``%d`` | Day of month (01–31) | ``11`` |
# | ``%A`` | Full weekday name | ``Tuesday`` |
# | ``%a`` | Abbreviated weekday name | ``Tue`` |
# | ``%H`` | Hour (24-hour) | ``14`` |
# | ``%I`` | Hour (12-hour) | ``02`` |
# | ``%M`` | Minute | ``10`` |
# | ``%S`` | Second | ``45`` |
# | ``%p`` | AM/PM | ``PM`` |
