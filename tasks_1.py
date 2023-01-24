import random
from random_words import RandomWords


# Завдання 1. Створити три списки: int_list, float_list, str_list.
# int_list заповнити випадковими цілочисельними значеннями у кількості
# 5000 елементів в діапазоні від 0 до 1000.
# float_list - випадковими цілочисельними значеннями у кількості
# 5000 елементів в діапазоні від 0,1 до 100,0.
#  str_list - випадковми словами у кількості 5000 елементів.


print('--- Task 1 ---')

#random.seed(10)
int_list = []
float_list = []

str_list = []
words = RandomWords()


# Кількість елементів для пошуку
for i in range(0, 5000):
                                    # Діпазон пошуку
    int_list.append(random.randint(0, 1000))


for i in range(0, 5000):
    float_list.append(random.uniform(0.1, 100.0))

for i in range(0, 5000):
    str_list.append(words.random_word())


print('Integer list:', int_list)
print('In the integer list', len(int_list), 'random numbers.')
print(random.random(), '\n')

print('Float list:', float_list)
print('In the flot list', len(float_list), 'random float numbers.')
print(random.random(), '\n')

print('String list:', str_list)
print('In the string list', len(str_list), 'random words.')
print(random.random())





# Завдання 2. Додати до попереднього завдання код будь-якого алгоритму
# сортування. Додати функцію, яка б обчислювала середній час роботи алгоритму
# сортування. Функція повинна приймати список і кількість ітерацій циклів
# сортування, а повертати середній час роботи алгоритму сортування.