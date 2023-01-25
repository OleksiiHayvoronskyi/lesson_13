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
for i in range(0, 5000):            # Діпазон пошуку
    int_list.append(random.randint(1, 1000))
print('Unsorted list:', int_list)


# Функція Бульбашкового алгоритму сортування.
def bubble_sort(nums):
    # Закінчиться, коли відсортує список.
    swapped = True
    while swapped:
        # Буде шукати, поки не перевірить весь список.
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        if not swapped:
            break
    print('Sorted list:', int_list)


start_time = time.time()

# Запуск функції.
bubble_sort(int_list)
print('Amount of numbers in the list:', len(int_list))
print('The execution time is %s seconds.' % (time.time() - start_time))
print('The average execution time of each number:',
      (time.time() - start_time) / len(int_list))
