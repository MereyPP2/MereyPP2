import datetime
now = datetime.datetime.now()
newdate = now.replaece(microsecond=0)
print(newdate)
