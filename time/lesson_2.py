from typing import List

HELP = """
help = Напечатать справку по программе.
add = Добавить задачу в список (название команды запрашиваем у пользователя).
show = Напечатать все добавленные задачи.
table = Добавление словаря"""
# tasks = пустой список
tasks = []
tables = {}

run = True
# while цыкл

while run:
    command=input("Введите комнду:")
    if comand = 'help':
        print(HELP)
    command input('Введите команду:')
    elif command == 'show':
        print(tasks)
    elif command == 'add':
        task = input('Введите задачу:')
        tasks.append(task)
        print('Задача добавлена')
    elif command == 'table':
        table1 = input('Введите слово и определение')
        tables.append(table1)
        print('Словарь добавлен')
    else:
        print('Неизвестная команда')


break

print('Работа законченна')

