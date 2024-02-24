import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print(yesterday, yesterday.strftime("%x"))
print(today, today.strftime("%x"))
print(tomorrow, tomorrow.strftime("%x"))