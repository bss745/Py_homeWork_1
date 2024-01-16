import random

def generate_random_list(list_len, start_value=1, end_value=100):
	return [random.randint(start_value, end_value) for _ in range(list_len)]

#	# Алгорітм Bubble Sort
def bubble_sort(nums):
	swapped = True
	while swapped:
		swapped = False
		for i in range(len(nums) - 1):
			if nums[i] > nums[i + 1]:
				nums[i], nums[i + 1] = nums[i + 1], nums[i]
				swapped = True


#	# Алгорітм Selection Sort
def selection_sort(nums):
	for i in range(len(nums)):
		lowest_value_index = i
		for j in range(i + 1, len(nums)):
			if nums[j] < nums[lowest_value_index]:
				lowest_value_index = j
		nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
	

#	# Алгорітм Insertion Sort
def insertion_sort(nums):
	for i in range(1, len(nums)):
		item_to_insert = nums[i]
		j = i - 1
		while j >= 0 and nums[j] > item_to_insert:
			nums[j + 1] = nums[j]
			j -= 1
		nums[j + 1] = item_to_insert


#	# Алгорітм Merge Sort
def merge(left_list, right_list):
	sorted_list = []
	left_list_index = right_list_index = 0
	left_list_lenght, right_list_lenght = len(left_list), len(right_list)

	for _ in range(left_list_lenght + right_list_lenght):
		if left_list_index < left_list_lenght and right_list_index < right_list_lenght:
			if left_list[left_list_index] <= right_list[right_list_index]:
				sorted_list.append(left_list[left_list_index])
				left_list_index += 1
			else:
				sorted_list.append(right_list[right_list_index])
				right_list_index += 1
		elif left_list_index == left_list_lenght:
			sorted_list.append(right_list[right_list_index])
			right_list_index += 1
		elif right_list_index == right_list_lenght:
			sorted_list.append(left_list[left_list_index])
			left_list_index += 1

	return sorted_list


def merge_sort(nums):
	if len(nums) <= 1:
		return nums
	
	middle_index = len(nums) // 2

	left_list = merge_sort(nums[:middle_index])
	right_list = merge_sort(nums[middle_index:])

	return merge(left_list, right_list)



numbers = generate_random_list(10)
print(numbers)
# bubble_sort(numbers)
# selection_sort(numbers)
# insertion_sort(numbers)
# numbers = merge_sort(numbers)
# print(numbers)

##################################
# SEARCH
# Алгорітм лінейного пошуку
def linear_search(nums, target) -> int:
	for i in range(len(nums)):
		if nums[i] == target:
			return i
	return -1 # означает, что значение не найдено

print(linear_search(numbers, 3))
print(linear_search(numbers, 74))
print(linear_search(numbers, 55))
print(linear_search(numbers, 76))

##################################
# SEARCH
# Алгорітм бінарного пошуку
# Бінарний пошук ефективний якщо список відсортований та дуже великий
def binary_search(nums, search_item) -> int:
	first_index = 0
	last_index = len(nums) - 1

	while first_index <= last_index:
		middle_index = (first_index + last_index) // 2
		if nums[middle_index] == search_item:
			return middle_index
		else:
			if search_item < nums[middle_index]:
				last_index = middle_index - 1
			else:
				first_index = middle_index + 1

	return -1

numbers.sort()
print(numbers)
print(binary_search(numbers, 74))
print(binary_search(numbers, 3))
print(binary_search(numbers, 55))
print(binary_search(numbers, 76))

################################
def partition (nums, low_index, high_index):
	# вибираємо середній елемент як опорний
	# так само можливий вибір першого, останнього або довільного ел-тов як опорного
	pivot = nums[(low_index + high_index) // 2]
	i = low_index - 1
	j = high_index + 1

	while True:
		i += 1
		while nums[i] < pivot:
			i += 1

		j -= 1
		while nums[j] > pivot:
			j -= 1

		if i >= j:
			return j
		
		# Якщо елемент з індексом i (ліворуч від опорного) більше ніж елемент з індексом j
		# (праворуч від опорного) то міняємо їх місцями
		nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
	# допоміжна функція
	def _quick_sort(items, low_index, high_index):
		if low_index < high_index:
			split_index = partition(items, low_index, high_index)
			_quick_sort(items, low_index, split_index)
			_quick_sort(items, split_index + 1, high_index)

	_quick_sort(nums, 0, len(nums) - 1)

nums = [1, 2, 4, 7, 6, 8, 9, 2, 2, 6, 4, 3]
print(nums)
quick_sort(nums)
print(nums)

##################################################
# Алгорітм бінарного пошуку через рекурсію
def binary_search(array, value, start, end):
	if end >= start:
		mid = (start + end) // 2
		if array[mid] == value:
			return mid
		elif array[mid] > value:
			return binary_search(array, value, start, mid - 1)
		else:
			return binary_search(array, value, mid + 1, end)
		
	else:
		return -1
	
my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(my_array, 3, 0, len(my_array) - 1))
print(my_array)

########################################
def guess_a_number(start, end, attempts=0):
	if end >= start:
		mid = (start + end) // 2
		user_input = input(f"Your number is {mid}? '+' -> yes or '-' -> no: ").strip().lower()
		attempts += 1
		if user_input == '+':
			print(f"Congratulations! We guessed your number! Attempts: {attempts}")
			return
		elif user_input == '-':
			user_input = input(f"Your number is bigger then {mid}? '+' -> yes or '-' -> no: ").strip(). lower()
			if user_input == '+':
				guess_a_number(mid + 1, end, attempts)
			elif user_input == '-':
				guess_a_number(start, mid - 1, attempts)


guess_a_number(1, 15)

#################### LIBRARY #########################

# import random
# import math
# from random import *
# from random import randint, search

# print(random.randint(1, 100)) # від 1 до 100
# print(random.random()) # повертає якесь дробне число від 0 до 1 
# print(random.choice("qwerty")) # вибір символу із строки
# print(random.randrange(10)) # від нуля до 9
# print(random.randrange(2, 10)) # від 2 до 9
# print(random.randrange(2, 10, 2)) # від 2 до 9 через один (кожен другий)
# nums = [1, 2, 3, 4, 5]
# random.shuffle(nums) # перемішуємо значення списку
# print(nums)

##
# print(-math.inf)
# print(math.inf)
# print(math.ceil(10.2))
# print(math.floor(10.999))
# print(math.factorial(5))
# print(math.pow(2, 3))
# print(math.sqrt(9))

##
# from decimal import *

# number = 0.1 + 0.1 + 0.1
# print(number)
# number = Decimal('0.1')
# number = number + number + number
# print(number)

# number = Decimal('0.333')
# number = number.quantize(Decimal("1.00"))
# print(number)

# number = Decimal('0.333')
# number = number.quantize(Decimal("1.0000"))
# print(number)

# number = Decimal('12.123456789')
# number = number.quantize(Decimal("1.0000"))
# print(number)

# number = Decimal('12.5555')
# number = number.quantize(Decimal("1.000"))
# print(number)

# number = Decimal('12.9999')
# number = number.quantize(Decimal("1.000"))
# print(number)

# # округлення відбувається до найближчого парного числа, якщо округлена частина дорівнює 5
# number = Decimal('12.025')
# number = number.quantize(Decimal("1.00"), ROUND_HALF_EVEN)
# print(number)

# number = Decimal('12.035')
# number = number.quantize(Decimal("1.00"), ROUND_HALF_EVEN)
# print(number)

#####
# datetime
import datetime as dt

# print(dt.date.today())
# print(dt.date(2022, 11, 10))
# print(dt.time())
# print(dt.time(10, 13, 15))
# print(dt.time(10, 13))
#
# print(dt.datetime.now())
# dt_now = dt.datetime.now()
# print(f"{dt_now.day}/{dt_now.month}/{dt_now.year} {dt_now.hour}:{dt_now.minute}:{dt_now.second}:{dt_now.microsecond}")
# #
# print(dt.datetime)
#
# my_date = dt.datetime.strptime("12/03/2020", "%d/%m/%Y")
# print(my_date)

# www.programiz.com/python-programming/datetime/strftime

from datetime import datetime, timezone, timedelta

# naive
naive = datetime.now()
print("Naive DateTime:", naive)

# UTC aware
UTC = datetime.now(timezone.utc)
print("UTC DateTime", UTC)

# creating a datetime with JST (Japan) TimeZone
jst_dateTime = datetime.now(timezone(timedelta(hours=+9), 'JST'))
print("In JST::", jst_dateTime)

#####

# Генератори колекцій
# list comprehension

# newlist = [expression for item in iterable (if condition)]

# iterable: джерело даних, що перебирається, в якості якого може виступати список, безліч,
# послідовність або навіть функція, яка повертає набір даних, наприклад, range()

# item: елемент, що витягується з джерела даних

# expression: вираз, який повертає повне значення. Це значення потім повертається в список,
# що генерується

# condition: умова, якій повинні відповідати елементи, що витягуються з джерела даних.
# якщо елемент НЕ задовольняє умову, він не вибирається. Необов'язковий параметр

# # v1
# numbers = [-1, 2, -3, 4, -5, 6, -7, 8, -9]
# numbers_positive = []
# for num in numbers:
# 	if num > 0:
# 		numbers_positive.append(num)

# print(numbers_positive)

# # v2
# numbers_positive_2 = [num for num in numbers if num > 0]
# print(numbers_positive_2)

# #
# nums = [n for n in range(10)]
# print(nums)

# nums = [n for n in range(10) if n % 2 == 0]
# print(nums)

# users = {1: "John", 2: "Peter", 3: "Max"}
# print(users)
# names = [name for name in users.values()]
# print(names)
# users_data = [f"{key}: {users[key]}" for key in users.keys() if key > 2]
# print(users_data)

# numbers = [-1, 2, -3, 4, -5, 6, -7, 8, -9]
# numbers_positive_2 = tuple([num * 2 for num in numbers if num > 0])
# print(numbers_positive_2)
# new_numbers = [num * 2 if num > 5 else num for num in numbers if num > 0]
# print(new_numbers)

# ##
# my_dict = {i: i ** 2 for i in range(10)}
# print(my_dict)

# ##
# my_set = {i for i in range(10)}
# print(my_set)

# #######################################
# ## Генераторні функції
# # Генератор - це об'єкт, який відразу при створенні не обчислює всіх своїх елементів
# generator = (i for i in range(3))
# # print(generator)
# # print(next(generator))
# # print(next(generator))
# # print(next(generator))
# # print(next(generator)) # StopIteration
# # close() -> зупинка генератора
# # throw() -> генератор кине виняток

# for i in generator:
# 	print(i)

# def create_generator():
# 	number = 1
# 	while True:
# 		yield number
# 		number += 1


# my_gen = create_generator()
# print(my_gen)
# try:
# 	for i in my_gen:
# 		print(i)
# 		if i > 10:
# 			# my_gen.close()
# 			my_gen.throw(Exception("End!"))
# except Exception as e:
# 	print(e)

############### REG EX (регулярні вирази) #########################
# \d - відповідає будь-якій одній цифрі і замінює собою вираз [0-9];
# \D - виключає всі цифри та замінює [^0-9];
# \w - замінює будь-яку цифру, букву, а також знак нижнього підкреслення;
# \W - будь-який символ крім латиниці, цифр або нижнього підкреслення;
# \s - відповідає будь-якому пробельному символу;
# \S - описує будь-який не пробільний символ.

# . - один символ, крім нового рядка \n;
# ? - 0 або 1 входження шаблону зліва;
# * - 1 і більше входжень шаблону зліва;
# * - 0 і більше входжень шаблону зліва;
# \b - кордон слова;
# [..] - Один із символів у дужках ([^..] - будь-який символ, крім тих, що у дужках);
# \ - екранування спеціальних символів (\. - означає "точку", \+ - знак "плюс");
# ^ і $ - початок і кінець рядка відповідно;
# {n, m} - від n до m входжень ({, m} - від 0 до m);
# a|b - відповідає a або b;
# () - групує вираз і повертає звичайний текст;
# \t, \n, \r - символ табуляції, нового рядка та повернення каретки відповідно;

# для чого використовуються регулярні вирази
# для визначення потрібного формату, наприклад телефонного номеру або email-адреси;
# для розбивки рядків на підрядки;
# для пошуку, заміни та вилучення символів;
# для швидкого виконання нетривіальних операцій.

# а ось найбільш популярні методи, які надає модуль:

# re.match() - цей метод шукає за заданим шаблоном на початку рядка
# re.search() - метод схожий на match(), але шукає не тільки на початку рядка
# re.findall() - повертає список усіх знайдених збігів
# У методу findall() немає обмежень на пошук на початку або в кінці рядка
# re.split() - цей метод поділяє рядок за заданим шаблоном
# re.sub() - шукає шаблон у рядку і замінює його на вказаний підрядок
# Якщо шаблон не знайдено, рядок залишається незмінним
# re.compile() - ми можемо зібрати регулярний вираз в окремий об'єкт, який можна використовувати для пошуку

import re

result = re.match(r'he', 'hello world hello')
print(result)
print(result.group(0))

result = re.search(r'world', 'hello world hello')
print(result.start())
print(result.end())

result = re.findall(r'he', 'hello world hello')
print(result)

result = re.split(r'l', 'hello world hello', maxsplit=1)
print(result)

result = re.split(r'l', 'hello world hello')
print(result)

pattern = re.compile('hello')
result = pattern.findall('hello world hello')
print(result)

result = re.findall(r'.', 'It is a long established fact that a reader')
print(result)

result = re.findall(r'\w', 'It is a long established fact that a reader')
print(result)

result = re.findall(r'\w*', 'It is a long established fact that a reader')
print(result)

result = re.findall(r'\w+', 'It is a long established fact that a reader')
print(result)

result = re.findall(r'\w+$', 'It is a long established fact that a reader')
print(result)

result = re.findall(r'^\w+', 'It is a long established fact that a reader')
print(result)

result = re.findall(r'\w\w', 'It is a long established fact that a reader')
print(result)

result = re.findall(r'\b\w', 'It is a long established fact that a reader')
print(result)

result = re.findall(r'@\w+.\w+', 'test1@gmail.com, test2@qqq.com, test3@www.com')
print(result)

result = re.findall(r'@\w+.(\w+)', 'test1@gmail.com, test2@qqq.ua, test3@www.com')
print(result)

result = re.findall(r'\d{2}-\d{2}-\d{4}', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-017-2004')
print(result)

li = ['9999999999', '999999-999', '99999x9999']

for val in li:
	if re.match(r'[0-9]{1}[0-9]{9}', val) and len(val) == 10:
		print('yes')
	else:
		print('no')


################HOME WORK#################

# Написати валідації за допомогою регулярних виразів та протестувати на рiзних кейсах:
import re

# №1 ﻿- домашній номер телефону (тільки цифри та довжина номера)
print("===== Ex. 1 =====")

def validate_home_phone_number(phone_number):
    # Регулярний вираз для перевірки, чи номер містить тільки цифри та має довжину від 5 до 7 символів.
    pattern = re.compile(r'^\d{5,7}$')

    # Перевірка чи номер відповідає регулярному виразу.
    if pattern.match(phone_number):
        return True
    else:
        return False

# Приклад використання та тестування:
phone_number = input("Введіть домашній номер телефону: ")

if validate_home_phone_number(phone_number):
    print("Номер телефону валідний.")
else:
    print("Номер телефону не валідний.")

# 2 - Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
print("===== Ex. 2 =====")

def validate_mobile_phone_number(phone_number):
    # Регулярний вираз для перевірки, чи номер містить тільки цифри та можливий плюс на початку.
    pattern = re.compile(r'^\+?\d{10,15}$')

    # Перевірка чи номер відповідає регулярному виразу.
    if pattern.match(phone_number):
        return True
    else:
        return False

# Приклад використання та тестування:
phone_number = input("Введіть мобільний номер телефону: ")

if validate_mobile_phone_number(phone_number):
    print("Мобільний номер телефону валідний.")
else:
    print("Мобільний номер телефону не валідний.")

# 3- email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)
print("===== Ex. 3 =====")

def validate_email(email):
    # Регулярний вираз для перевірки формату email.
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    # Перевірка чи email відповідає регулярному виразу.
    if pattern.match(email):
        return True
    else:
        return False

# Приклад використання та тестування:
user_email = input("Введіть свій email: ")

if validate_email(user_email):
    print("Email валідний.")
else:
    print("Email не валідний.")
    
# 4 - ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)
print("===== Ex. 4 =====")

def validate_full_name(full_name):
    # Регулярний вираз для перевірки формату ПІБ.
    pattern = re.compile(r'^[a-zA-Zа]{2,20}\s[a-zA-Zа]{2,20}\s[a-zA-Zа]{2,20}$')

    # Перевірка чи ПІБ відповідає регулярному виразу.
    if pattern.match(full_name):
        return True
    else:
        return False

# Приклад використання та тестування:
user_full_name = input("Введіть ПІБ клієнта: ")

if validate_full_name(user_full_name):
    print("ПІБ валідний.")
else:
    print("ПІБ не валідний.")
