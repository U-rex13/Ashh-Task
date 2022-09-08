import datetime
current = datetime.datetime.now()
print("Todays date and time is:\n(dateformat Days-Month-Year & timeformat Hours:Minutes:Seconds)")
print(current.strftime("%d/%m/%y %H:%M:%S"))
