# выводит текст из фаила txt
# for i in open('01_jorney_begin.txt'):
    #print(i.strip())
# закрывает фаил, не забывать
# f.close()
#x = file = open('01_jorney_begin.txt','r')
#x = print(file.read())
#f = open('skazka.txt','a')
#f.write('s')
skaska = open('01_jorney_begin.txt', 'r', encoding='utf-8')
skaska = open('02_unexpected_meet.txt', 'r', encoding='utf-8')
skaska = open('03_murder.txt', 'r', encoding='utf-8')
skaska = open('04_second_victim.txt', 'r', encoding='utf-8')
skaska = open('05_retribution.txt', 'r', encoding='utf-8')
privet = open('skazka.txt', 'a', encoding='utf-8')
for i in skaska.readlines():
    privet.write(i)
skaska.close()


#x.readlines()
#print('x')
# Функция записи в фаил txt
#f = open('skazka.txt', 'a')
#f.write('x')
#f.close()









