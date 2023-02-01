import random
import time
random.seed(10)

# Завдання 2. Додати до попереднього завдання код будь-якого алгоритму
# сортування. Додати функцію, яка б обчислювала середній час роботи алгоритму
# сортування. Функція повинна приймати список і кількість ітерацій циклів
# сортування, а повертати середній час роботи алгоритму сортування.

print('\n--- Task 2. BUBBLE SORT ---')

# Списки, куди будуть сортуватися числа.
int_list_1 = []
int_list_2 = []
int_list_3 = []

# Кількість елементів для пошуку.
for i in range(0, 1000):  # Діпазон пошуку
    int_list_1.append(random.randint(1, 1000))
    int_list_2.append(random.randint(1, 1000))
    int_list_3.append(random.randint(1, 1000))


# Функція Бульбашкового алгоритму сортування.
def bubble_sort(int_list_1, int_list_2, int_list_3, print_step=False):
    n_1 = len(int_list_1)
    n_2 = len(int_list_2)
    n_3 = len(int_list_3)

    # Масив 1.
    print('Array 1:')
    start_time = time.time()
    print('Unsorted array 1:', int_list_1)
    for i in range(n_1):
        sorted = False
        for j in range(0, n_1 - i - 1):
            if int_list_1[j] > int_list_1[j + 1]:
                int_list_1[j], int_list_1[j + 1] = int_list_1[j + 1], \
                    int_list_1[j]
                sorted = True
        if not sorted:
            break
        # Крок сортування.
        # elif print_step:
        #     start_time = time.time()
        #     print(f"sorting = {i}: ", end='')
        #     print(f'{int_list_1}', end='')
        #     print(': time is %s seconds.' % (time.time() - start_time))

    print('Sorted array 1:', int_list_1)
    print('Amount of numbers in the array 1:', len(int_list_1))
    print('Time is %s seconds.' % (time.time() - start_time),
          '\n')

    # Масив 2.
    print('Array 2:')
    start_time = time.time()
    print('Unsorted array 2:', int_list_2)
    for i in range(n_2):
        sorted = False
        for g in range(0, n_2 - i - 1):
            if int_list_2[g] > int_list_2[g + 1]:
                int_list_2[g], int_list_2[g + 1] = int_list_2[g + 1], \
                    int_list_2[g]
                sorted = True
        if not sorted:
            break
        # Крок сортування.
        # elif print_step:
        #     start_time = time.time()
        #     print(f"sorting = {i}: ", end='')
        #     print(f'{int_list_2}', end='')
        #     print(': time is %s seconds.' % (time.time() - start_time))

    print('Sorted array 2:', int_list_2)
    print('Amount of numbers in the list 2:', len(int_list_2))
    print('Time is %s seconds.' % (time.time() - start_time),
          '\n')

    # Масив 3.
    print('Array 3:')
    start_time = time.time()
    print('Unsorted array 3:', int_list_3)
    for i in range(n_3):
        sorted = False
        for d in range(0, n_3 - i - 1):
            if int_list_3[d] > int_list_3[d + 1]:
                int_list_3[d], int_list_3[d + 1] = int_list_3[d + 1], \
                    int_list_3[d]
                sorted = True
        if not sorted:
            break
        # Крок сортування.
        # elif print_step:
        #     start_time = time.time()
        #     print(f"sorting = {i}: ", end='')
        #     print(f'{int_list_3}', end='')
        #     print(': time is %s seconds.' % (time.time() - start_time))

    print('Sorted array 3:', int_list_3)
    print('Amount of numbers in the list 3:', len(int_list_3))
    print('Time is %s seconds.' % (time.time() - start_time),
          '\n')


start_time = time.time()
# Запуск функції.
bubble_sort(int_list_1, int_list_2, int_list_3, True)
print('The total execution time is %s seconds.' % (time.time() - start_time))
