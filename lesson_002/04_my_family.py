#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Катя', 'Саша', 'Лариса', 'Настя']


# список списков приблизителного роста членов вашей семьи
my_family_height = [['Саша', 173], ['Катя', 162], ['Лариса', 164], ['Настя', 161]]
    # ['имя', рост],


# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
h = (my_family_height[0][1])
print('Рост отца -', h, 'см')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
height_families = (
        my_family_height[0][1]
        + my_family_height[1][1]
        + my_family_height[2][1]
        + my_family_height[3][1]
)

print('Общий рост моей семьи -', height_families, 'см')