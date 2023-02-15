from time import time, ctime, localtime
epoch = time()
print(epoch)

et = ctime(epoch)
print(et)

print(ctime())

stobj = localtime()
print(stobj.tm_mday, end ="/")
print(stobj.tm_mon, end= "/")
print(stobj.tm_year)

print(stobj.tm_hour, end =":")
print(stobj.tm_min, end =":")
print(stobj.tm_sec)

print("Week:",stobj.tm_wday)
print("Total days count:",stobj.tm_yday)
print(stobj.tm_isdst)