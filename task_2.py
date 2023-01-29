import random
import time
random.seed(10)

# Завдання 2. Додати до попереднього завдання код будь-якого алгоритму
# сортування. Додати функцію, яка б обчислювала середній час роботи алгоритму
# сортування. Функція повинна приймати список і кількість ітерацій циклів
# сортування, а повертати середній час роботи алгоритму сортування.

print('\n--- Task 2. BUBBLE SORT ---')

# Список, куди будуть сортуватися числа.
int_list = []

# Кількість елементів для пошуку.
for i in range(0, 300):            # Діпазон пошуку
    int_list.append(random.randint(1, 1000))
print('Unsorted list:', int_list, '\n')


# Функція Бульбашкового алгоритму сортування.
def bubble_sort(int_list, print_step=False):
    n = len(int_list)
    # Буде шукати, поки не перевірить весь список.
    for i in range(n - 1):
        for j in range(n - 1, i, - 1):
            if int_list[j] < int_list[j - 1]:
                int_list[j], int_list[j - 1] = int_list[j - 1], int_list[j]
            # Друкує кожен масив даних, що у діапазоні пошуку.
            elif print_step:
                print(f"array = {i}: ", end='')
                start_time = time.time()
                print(f'{int_list}')
                print('Array execution time:',
                      (time.time() - start_time) / len(int_list))


start_time = time.time()
# Запуск функції.
bubble_sort(int_list, True)
print('\nSorted list:', int_list)
print('Amount of numbers in the list:', len(int_list))
print('The execution time is %s seconds.' % (time.time() - start_time))
