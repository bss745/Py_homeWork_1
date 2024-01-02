# a: int = 10
# b: int = 15
# c: int = 20

# print(a + b + c)
# print(a * b * c)

# ac: float = 12.5
# bd: float = 7.0
# s = ac * bd / 2

# print(s)

# number = int(input("Enter 4-digit number: "))
# # # 1324
# n1 = number // 1000

# n2 = number // 100 % 10

# n3 = number // 10 % 10

# n4 = number % 10
# #
# result = n1 * n2 * n3 * n4
# print(f"n1: {n1} n2: {n2} n3: {n3} n4: {n4}")
# print(f"Result: {result}")

# ########

# # умови
# #v1

# # n1 = 10
# # n2 = 20

# # v2
# n1, n2 = 10, 20 # множинне привласнення

# print(n1 > n2)
# print(n1 >= n2)
# print(n1 < n2)
# print(n1 <= n2)
# print(n1 == n2) # поверне True, якщо обидва операнди рівні (однакові)
# print(n1 != n2, end="\n" "\n") # поверне True, якщо обидва операнди різні
# #
# print(1 == 1 and 3 == 3) # поверне True, якщо обидва операнди рівні True, інакше False 
# print(1 == 1 or 2 == 3) # поверне True, якщо хоча б один операнд дорівнює True, інакше False
# #
# is_valid = False
# print(is_valid)
# print(not is_valid) # not -> інверсіяБ якщо значення False стане True і навпаки

# print("hello" in "hello world") # виведе True

################

# hours = int(input("Enter hours: "))

# if 12 <= hours < 24:
# 	print("PM")
# elif 0 <= hours < 12:
# 	print("AM")
# # if hours >= 12 and hours < 24:
# # 	print("PM")
# else:
# 	print("Incorrect hours!")

# # ввести рейтинг фільму: якщо рейтинг дорівнює 5 або 4 - ок, інакше - погано
# # 
# # 
# film_rating = int(input("Enter film rating: "))

# if film_rating > 0 and film_rating <= 5:
# 	if film_rating == 4 or film_rating == 5:
# 		print("Ok!")
# 	else:
# 		print("Not OK!")
# else:
# 	print("Incorrect rating!")

# print("Hello World")

# ввести з клавіатури 3 числа
# - вивести найменше з трьох чисел

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

if n1 < n2 < n3:
	print(n1)
elif n2 < n3 < n1:
	print(n2)
elif n3 < n2 < n1:
	print(n3)
else:
	print("All numbers equal!")


# ввести з клавіатури 3 числа
# - вивести кількість однакових чисел

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

if n1 == n2 == n3:
	print(3)
elif n1 == n2 or n2 == n3 or n1 == n3:
	print(2)
else:
	print(0)

###########################################
	
for i in range(5):
	print(i, end=" ") # 0 1 2 3 4

print()

for i in range(2, 5):
	print(i, end=" ") # 2 3 4

print()

for i in range(1, 5, 2):
	print(i, end=" ") # 1 3

print()

for i in range(1, 9, 2):
	print(i, end=" ") # 1 3 5 7

print()

start, end = 1, 10
for i in range(start, end + 1):
	print(i, end=" ") # 1 2 3 4 5 6 7 8 9 10

print()

start, end = 1, 10
for i in range(end, start - 1, -2):
	print(i, end=" ") # 10 8 6 4 2

print()

start, end = 1, 10
for i in range(end, start - 1, -1):
	print(i, end=" ") # 10 9 8 7 6 5 4 3 2 1

print()

for i in range(1, 10):
	for j in range(1, 10):
		print(i * j, end=" ")
	print()

print()
## v2

i = 1
while i < 10:
	j = 1
	while j < 10:
		print(i * j, end=" ")
		j += 1
	print()
	i += 1

###
# Показати на екран усі прості числа в діапазоні вказаному користувачем
#
# Число називається простим, якщо воно ділиться без залишку тільки на себе і на одиницю
#
# Наприклад, 3 - просте число, а 4 - ні

try:

	start = int(input("Enter start value: "))
	end = int(input("Enter end value: "))

	# v1
	if start > end:
		start, end = end, start

	# v2
	# if start > end: 
	# 	temp = start
	# 	start = end
	# 	end = temp
		
	for number in range(start, end + 1):
		if number < 2:
			continue

		is_simple = True

		for i in range(2, number):
			if number % i == 0:
				is_simple = False
				break
		
		if is_simple:
			print(number, end=" ")
	
except Exception as error:
	print(error)

print()
## rows
	
dogs, cats = 12, 15

result = f"Dogs {dogs} and Cats {cats}"
print(result)

result = "Dogs {} and Cats {}".format(dogs, cats)
print(result)

result = "Dogs {1} and Cats {0}".format(dogs, cats)
print(result)

result = "Dogs {1} and Cats {1}".format(dogs, cats)
print(result)

print()

###
message = "Hello world"

# [] - індексатори
# Індекс - це порядковий номер елемента в колекції (масиві). Note: не всі колекції підтримують індекси
# Індекси рахуються з нуля

print(message[0])
print(len(message)) # кількість символів у рядку
# print(message[len(message)]) # IndexError: string index out of range
print(message[len(message) - 1])
print(message[-1])
print(message[10])

###
####
# string - immutable тип даних, рядок змінити не можна
# name = "Petya"
# print(name)
# # name[1] = "r"	# TypeError: 'str' object does not support item assignment
# user_name = "Vasya"
# name = user_name
# print(name)

####
# v1
sentence = "Hello, world"
for letter in sentence:
	print(letter, end=" ")

print()

# v2
for i in range(len(sentence)):
	print(sentence[i], end=" ")

# slices (срезы)
sentence = "Hello, world"
print(sentence[:])
print(sentence[0:])
print(sentence[2:])
print(sentence[2:8])
print(sentence[1:10:2])
print(sentence[::-1])
print(sentence[::-2])

#
name = "Vasya"
surname = "Petrov"
age = 33

fullname = name + " " + surname + " " + str(age) # конкатенація (додавання рядків)
print(fullname)

#
text = "Hello, world" * 3
print(text)

print("---" * 10)

#
a1 = "abc"
a2 = "abs"

if a1 > a2:
	print(a1)

else:
	print(a2)

print(ord("A"))
print(chr(98))

#

text = "hello woRLD"

# isalpha(): повертає True, якщо рядок складається лише з алфавітних символів

print(text.isalpha())

# islower(): повертає True, якщо рядок складається лише із символів у нижньому регістрі

print(text.islower())

# isupper(): повертає True, якщо всі символи рядка у верхньому регістрі

print(text.isupper())

# isdigit(): повертає True, якщо всі символи рядка - цифри

print(text.isdigit())

# isnumeric(): повертає True, якщо рядок є числом

print(text.isnumeric())

# startswith(str): повертає True, якщо рядок починається з підрядка str

print(text.startswith("hello"))

# endswith(str): повертає True, якщо рядок закінчується на підрядок str

print(text.endswith("d"))

# lower(): перекладає рядок у нижній регістр

print(text.lower())

# upper(): перекладає рядок у верхній регістр

print(text.upper())

# title(): початкові символи всіх слів у рядку перекладаються у верхній регістр

print(text.title())

# capitalize(): перекладає у верхній регістр першу літеру тільки першого слова рядка 

print(text.capitalize())

fio = input("Enter FIO: ").title()
print(fio)

# lstrip(): видаляє початкові пробіли з рядка

print(text)
print(text.lstrip())

# rstrip(): видаляє кінцеві пробіли з рядка

print(text)
print(text.rstrip())

# strip(): видаляє початкові та кінцеві пробіли з рядка

print(text)
print(text.strip())

# ljust(width): якщо довжина рядка менша за параметр width, то праворуч від рядка додаються пробіли
# щоб доповнити значення width, а сам рядок вирівнюється по лівому краю

print(text)
print(text.ljust(20))

# rjust(width): якщо довжина рядка менша за параметр width, то зліва від рядка додаються пробіли
# щоб доповнити значення width, а сам рядок вирівнюється по правому краю

print(text)
print(text.rjust(20))

# center(width): якщо довжина рядка менша за параметр width, то ліворуч і праворуч від рядка 
# равномірно додаються пробіли щоб доповнити значення width, а сам рядок вирівнюється по центру

print(text)
print(text.center(20))

# find(str[, start [, end]): повертає індекс підрядка у рядку. Якщо підрядок не знайдено, 
# повертається число -1 
text = "hello world"
print(text.find("hello")) # 0
print(text.find("l")) # 2
print(text.rfind("l")) # 9

first_found_index = text.find("l")
print(text.find("l", first_found_index + 1)) 

print(text.find("p")) # -1

# v1
for i in range(len(text)):
	if text[i] == "l":
		print(i)

# v2
index = 0

for letter in text:
	if letter == "l":
		print(index)
	index += 1

# replace(old, new[, num]): замінює в рядку один підрядок на інший
# text = "hello world hello"
# print(text)
	
# text = text.replace("hello", "goodbye", 1)
# print(text)
	
###############
import string
import random

data_for_password = string.digits + string.ascii_letters + string.punctuation
# print(data_for_password)

new_password = ""

for i in range(8):
	new_password += random.choice(data_for_password)

print(new_password)

# добавить возможность выбора длины пароля от 8 до 16 символов
# если юзер ввел неправильную длину - попросить ввести ещё раз

# если юзер ввёл 'q' или 'Q' - выйти из программы