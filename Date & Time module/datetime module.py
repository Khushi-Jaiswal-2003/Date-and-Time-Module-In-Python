from datetime import datetime

b = datetime(month=9, year=2021, day= 3)
print(b)

c = datetime(day= 3, year=2021, hour=10, month=9, minute=41, second=20, microsecond=45)
print(c)

c1 = datetime(2019, 10, 28)
print(c1)

c2 = datetime(2019, 3, 21, 10, 59, 41, 10000)
print(c2)
print(c2.year)

d = time(hour=12, minute=10, second =11)
print(d)

e = timedelta(days=12, seconds =30, hours=4, minutes=56)
print(e)