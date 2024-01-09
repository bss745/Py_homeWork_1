# Завдання 1

# Напишіть функцію, яка обчислює добуток елементів списку цілих. 
# Список передається як параметр. Отриманий результат повертається із функції.
print("=====Ex. 1=====")

import random

def create_list_with_rundom_numbers(list_length=10, start_number=1, end_number=10) -> list:
	return [random.randint(start_number, end_number) for _ in range(list_length)]

# list_lenght = 5
# start_number = 1
# end_number = 10
new_list = list()

# for i in range(list_lenght):
# 	new_list.append(random.randint(start_number, end_number))
	

def mult(new_list):
	dobutok = 1
	for number in new_list:
		dobutok *= number
		# return dobutok
		print(dobutok)
	return mult		
print(new_list)
print(mult(new_list))

# Завдання 2

# Напишіть функцію для знаходження мінімуму у списку цілих. 
# Список передається як параметр. Отриманий результат повертається із функції.

print("=====Ex. 2=====")


def find_min_number(new_list) -> int:
	return (min(new_list))

print(min(new_list))
# print(f"Min: {find_min_number}")

# Завдання 3

# Напишіть функцію, яка визначає кількість простих чисел у списку цілих. 
# Список передається як параметр. Отриманий результат повертається із функції.

print("=====Ex. 3=====")


def find_amount_simple_numbers(new_list) -> int:
	
	for number in new_list:
		
		if number % i == 0:
			simple_number = list()
			simple_number.append(number)
			# simple_number += number
			# print(simple_number)
			print(len(simple_number))
			return simple_number 

print(new_list)
# print(simple_number)
# print(len(simple_number))

# Завдання 4

# Напишіть функцію, яка видаляє зі списку ціле задане число. 
# З функції потрібно повернути кількість видаленних елементів.

print("=====Ex. 4=====")

def remove_number(list_to_remove) -> int:
	return len(set(list_to_remove))

# Завдання 5

# Напишіть функцію, яка отримує два списки як параметр і повертає список, 
# що містить елементи обох списків.

print("=====Ex. 5=====")

def create_list_with_rundom_numbers(list_length=10, start_number=1, end_number=10) -> list:
	return [random.randint(start_number, end_number) for _ in range(list_length)]

numbers_1 = create_list_with_rundom_numbers(start_number=1, end_number=20)
numbers_2 = create_list_with_rundom_numbers(start_number=1, end_number=20)

print(numbers_1)
print(numbers_2)
print(type(numbers_1))


def calc_number_of_equal_numbers_v1(nums_1: list[int], nums_2: list[int]) -> list:
	number = list()
	print(nums_1.append(nums_2))
	number = nums_1.append(nums_2)
	# return number
	print(type(number))

print(f"Result: {calc_number_of_equal_numbers_v1(numbers_1, numbers_2)}")

# Завдання 6

# Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих. 
# Значення для ступеня передається як параметр, список також передається як параметр. 
# Функція повертає новий список, який містить отримані результати.

print("=====Ex. 6=====")
