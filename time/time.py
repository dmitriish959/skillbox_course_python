import time
n=31536000
time_format = time.strftime("День: %A, Время: %H:%M:%S, Месяц: %B", time.gmtime(n))
print("Нужный формат времени:-",time_format)
