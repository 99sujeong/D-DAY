import datetime

now = datetime.datetime.now()

print(now)

#now = datetime.datetime.now()
print(now, type(now))

today = datetime.date.today()
td = datetime.timedelta(days=5)
for i in range(5,0,-1):
    td = datetime.timedelta(days=i)
    print(today-td)
