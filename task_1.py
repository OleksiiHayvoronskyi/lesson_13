import random
from random_words import RandomWords
import time

# Завдання 1. Створити три списки: int_list, float_list, str_list.
# int_list заповнити випадковими цілочисельними значеннями у кількості
# 5000 елементів в діапазоні від 0 до 1000.
# float_list - випадковими цілочисельними значеннями у кількості
# 5000 елементів в діапазоні від 0,1 до 100,0.
#  str_list - випадковми словами у кількості 5000 елементів.

print('\n--- Task 1 ---')

int_list = []
float_list = []
str_list = []

words = RandomWords()

start_time = time.time()


def get_sorting():
    # Кількість елементів для пошуку.
    for i in range(0, 5000):           # Діпазон пошуку
        int_list.append(random.randint(0, 1000))
    print('Integer list:', int_list)
    print('In the integer list', len(int_list), 'random integer numbers.')
    print('The execution time is %s seconds.' % (time.time() - start_time))

    for i in range(0, 5000):
        float_list.append(random.uniform(0.1, 100.0))
    print('\nFloat list:', float_list)
    print('In the flot list', len(float_list), 'random float numbers.')
    print('The execution time is %s seconds.' % (time.time() - start_time))

    for i in range(0, 5000):
        str_list.append(words.random_word())
    print('\nString list:', str_list)
    print('In the string list', len(str_list), 'random words.')
    print('The execution time is %s seconds.' % (time.time() - start_time))


get_sorting()
print('\nTotal execution time is %s seconds.' % (time.time() - start_time))
