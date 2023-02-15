from datetime import date
a = date(2003, 10, 19)
b = date.today()
# todo 18-1 = 17 (TRUE = 1)
age = b.year - a.year -((b.month, b.day) < (a.month, a.day))
print(age)