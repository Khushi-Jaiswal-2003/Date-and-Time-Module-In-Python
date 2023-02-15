from datetime import datetime
a = datetime.today()
print(a)
print(type(a))

b =a.strftime("%B %d, %Y")
print(b)
print(type(b))

c = a.strftime("%d/%b/%Y")
print(c)

d = a.strftime("%d-%m-%Y")
print(d)

e = a.strftime("%H:%M:%S")
print(e)

f = a.strftime("%I:%M:%S")
print(f)