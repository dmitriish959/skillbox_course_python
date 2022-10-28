#import time
#n=31536000
#time_format = time.strftime("День: %A, Время: %H:%M:%S, Месяц: %B", time.gmtime(n))
#print("Нужный формат времени:-",time_format)

a=int(input("Введите количество секуд:"))
h=a//3600
m=(a//60)%60
s=a%60
if m<10:
    m=str('0'+str(m))
else:
    m=str(m)
if s<10:
    s=str('0'+str(s))
else:
    s=str(s)
print(str(h)+':'+str(m)+':'+str(s))
