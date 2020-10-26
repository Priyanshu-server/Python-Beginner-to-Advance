import time
print(time.time())

a  = time.localtime(time.time())
a_modify = time.asctime(time.localtime()) #Local time

b = time.ctime() #Local Time (shortcut)
print(b)

c = time.asctime(time.gmtime()) #Global time (UTC Time)
print(c)


d = time.gmtime() #Inverse of gmtime or localtime
print(d)
print(d.tm_hour)
print(time.mktime(d))


# time.sleep(2)
# print("After 2 seconds")

named_tuple = time.localtime()

for_time = time.strftime("%m/%d/%Y, %H:%M:%S",named_tuple)
print(for_time)

time_string = "10 July, 2020"
result = time.strptime(time_string,"%d %B, %Y")
print(result)



