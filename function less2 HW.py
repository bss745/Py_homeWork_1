
###############################

# Завдання 1.

# Написати рекурсивну функцію знаходження ступеня числа.
print("===== Ex. 1=====")
def my_pow(base, exponent):
	if exponent <= 1:
		return base 
	
	return base * my_pow(base, exponent - 1)

result = my_pow(2, 3)
print(result)

# Завдання 2.

# Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.
# Проілюструйте роботу функції прикладом. (Протестувати)
print("===== Ex. 2=====")

def print_stars(N):
    if N <= 0:
        return
    print('*', end='')
    
    print_stars(N - 1)

N = int(input("Введіть кількість зірок (ціле число): "))

print_stars(N)
print()

# Завдання 3.

# Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.
# Користувач вводить a та b. Проілюструйте роботу функції прикладом.
print("===== Ex. 3=====")

def sum_range(num_1, num_2):
    if num_1 > num_2:
        return 0
    return num_1 + sum_range(num_1 + 1, num_2)

num_1 = int(input("Введіть перше значення: "))
num_2 = int(input("Введіть друге значення: "))

result = sum_range(num_1, num_2)
print(f"Сума чисел у діапазоні від {num_1} до {num_2}: {result}")

# Завдання 4.

# Напишіть рекурсивну функцію, яка приймає одновимірний масив із 100 цілих чисел 
# заповнених випадковим чином і знаходить позицію, з якої починається послідовність із 10 чисел,
# сума яких мінімальна. вивести на екран весь масив, вивести на екран послідовність
print("===== Ex. 4=====")

import random

def find_min_sum_position(arr, current_position=0, min_sum_position=0, current_min_sum=float('inf')):
    if current_position + 10 > len(arr):
        return min_sum_position
    
    current_sum = sum(arr[current_position:current_position+10])
    
    if current_sum < current_min_sum:
        current_min_sum = current_sum
        min_sum_position = current_position
    
    return find_min_sum_position(arr, current_position + 1, min_sum_position, current_min_sum)

random_numbers = [random.randint(1, 100) for _ in range(100)]

print("Весь масив:")
print(random_numbers)

result_position = find_min_sum_position(random_numbers)

min_sequence = random_numbers[result_position:result_position+10]
print(f"\nПослідовність з 10 чисел з мінімальною сумою:")
print(min_sequence)