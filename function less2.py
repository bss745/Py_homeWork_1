# def hello(): print("Hello")

# print(hello)
# message = hello # надав посилання на функцію в іншу змінну
# print(message)

# hello()
# message()

# ###############

# def add(a, b): return a + b

# def sub(a, b): return a - b

# def mult(a, b): return a * b

# def division(a, b): return a / b


# def select_math_operation(user_choice):
# 	match user_choice:
# 		case "+":
# 			return add
# 		case "-":
# 			return sub
# 		case "*":
# 			return mult
# 		case "/":
# 			return division
# 		case "_":
# 			raise Exception("Invalid operation!")
		

# try:
# 	operation = input("Enter math operation: ")
# 	math_operation = select_math_operation(operation)
# 	result = math_operation(4, 9)
# 	print(f"Result: {result}")
# except Exception as error:
# 	print(error)

# ################
	
# message = lambda: print("Hello world!")
# message()

# square = lambda side_1, side_2: side_1 * side_2
# print(square(2, 4))

# ##########
# def calculate(a, b, math_operation) -> None:
# 	print(f"Result: {math_operation(a, b)}")

# calculate(2, 5, lambda n1, n2: n1 + n2)
# calculate(24, 8, lambda n1, n2: n1 / n2)

# ############ (lambda)
# def select_math_operation(user_choice):
# 	match user_choice:
# 		case "+":
# 			return lambda a, b: a + b # повернення посилання на функцію
# 		case "-":
# 			return lambda a, b: a - b
# 		case "*":
# 			return lambda a, b: a * b
# 		case "/":
# 			return lambda a, b: a / b
# 		case "_":
# 			raise Exception("Invalid operation!")
		

# try:
# 	operation = input("Enter math operation: ")
# 	math_operation = select_math_operation(operation)
# 	result = math_operation(4, 9)
# 	print(f"Result: {result}")
# except Exception as error:
# 	print(error)

############## LEGB
	
############# області видимості
	
# number = 10

# def test() -> None:
# 	number: int = 11 # перекриття глобальної змінної

# 	if 1:
# 		number = 12

# 		if 1:
# 			number = 13
# 			print(number)
# 	print(number)

# print(number)
# test()
# print(number)
# number = 35
# print(number)

# ##############
# print("==================================")
# number = 10

# def test() -> None:
# 	global number
# 	number = 11 # змінюємо значення глобальної функції
# 	print(number)


# print(number)
# test()
# print(number)

# print("==================================")

# def outer():
# 	number = 1


# 	def inner():
# 		# nonlocal number
# 		number = 2
# 		print(number)

# 	inner()
# 	print(number)

# outer()

# print("==================================")

# number = 10

# def outer():
# 	global number
# 	number = 1
# 	new_number = number

# 	def inner():
# 		global number
# 		nonlocal new_number
# 		new_number = 2.2
# 		print(new_number)
# 		number = 2

# 		def inner_number_2():
# 			global number
# 			nonlocal new_number
# 			new_number = 3.2
# 			print(new_number)
# 			number = 3

# 		inner_number_2()

# 	inner()
# 	print(new_number)

# outer()
# print(number)

# #####################
# print("===============================================================")
# # Замикання (closure) представляє функцію, яка запам'ятовує своє лексичне оточення 
# # навіть у тому випадку коли вона виконується поза своєю областю видимості.

# # Зовнішня функція, яка визначає деяку область видимості і в якій визначені деякі 
# # змінні та параметри - лексичне оточення

# # змінні та параметри (лексичне оточення), які визначені у зовнішній функції

# # вкладена функція, яка використовує змінні та параметри зовнішньої функції

# def outer():
# 	number = 10
# 	print("outer")
# 	print(number)
# 	test = 10
# 	test_2 = 111

# 	def inner():
# 		nonlocal number
# 		number += 1
# 		# print("test")
# 		print(number)
# 		print("Hello")

# 	return inner

# inner_func = outer()
# inner_func()
# inner_func()
# inner_func()

#######################

# # v1
# def multiply(num1):
# 	def inner(num2): return num1 * num2
# 	return inner

# # v2
# def multiply(num1): return lambda num2: num1 * num2

# # def multiply_v2(num1, num2):
# # 	return num1 * num2

# # for i in range(1, 10):
# # 	print(f"{3} * {i} = {multiply_v2(3, i)}")


# number1 = 3
# mult_func = multiply(number1)
# print(mult_func(4))
# print(mult_func(5))
# print(mult_func(6))

# for number2 in range(1, 10):
# 	print(f"{number1} * {number2} = {mult_func(number2)}")
	

################################
# args and kwargs
# упаковка в кортеж	
# def example_1(*args, text="hello world"):
# 	print(args)
# 	print(text)


# example_1(text="some text")
# example_1(1, 2, 3, 4, 5, 6, 7, 8, 9)

# # распаковка из кортежа
# def sum_numbers(n1, n2, n3, n4):
# 	print(n1 + n2 + n3 + n4)

# numbers = [2, 4, 1, 5]
# sum_numbers(numbers[0], numbers[1], numbers[2], numbers[3])
# sum_numbers(*numbers)


# # упаковка в словарь
# def example_2(**kwargs):
# 	print(kwargs)
	

# example_2()
# example_2(name="Vasya", age=33)


# # распаковка из словаря
# def example_3(name, age):
# 	print(name, age)

# user = {
# 	"name": "Petya",
# 	"age": 44
# }

# example_3(**user)

# #################
# def show_info(name, age, *args, **kwargs):
# 	print(f"Hello: {name}, your age is: {age}")
# 	print(args)
# 	print(kwargs)

# show_info("John", 44, 1, 2, 3, 4, text1="text1", text2="text2")

########## рекурсия

# Рекурсія - коли функція викликає сама себе
# 1. Продумати, яке або які параметри функції будуть змінені при рекурсивному виклику
# 2. Визначити умову або умови виходу з рекурсії
# 3. Запустити рекурсію (виклик цієї ж функції)

def factorial(number):
	if number <= 1:
		return 1
	
	return number * factorial(number - 1)

print(factorial(5))


# #	factorial(5) -> 5 * factorial(4) => 120
# #	factorial(4) -> 4 * factorial(3) => 24
# #	factorial(3) -> 3 * factorial(2) => 6
# #	factorial(2) -> 2 * factorial(1) => 2
# #	factorial(5) => 1

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
    # Базовий випадок: якщо N <= 0, завершити рекурсію
    if N <= 0:
        return
    # Вивести зірку
    print('*', end='')
    # Викликати функцію зменшуючи N на 1
    print_stars(N - 1)

# Запитати користувача про кількість зірок
N = int(input("Введіть кількість зірок (ціле число): "))

# Викликати функцію з введеним значенням N
print_stars(N)
print()
# Завдання 3.

# Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.
# Користувач вводить a та b. Проілюструйте роботу функції прикладом.
print("===== Ex. 3=====")

def sum_range(a, b):
    # Базовий випадок: якщо a > b, сума - 0
    if a > b:
        return 0
    # Рекурсивний випадок: додати поточне число та суму для наступного числа
    return a + sum_range(a + 1, b)

# Запитати користувача про a та b
a = int(input("Введіть значення a: "))
b = int(input("Введіть значення b: "))

# Викликати функцію та вивести результат
result = sum_range(a, b)
print(f"Сума чисел у діапазоні від {a} до {b}: {result}")

# Завдання 4.

# Напишіть рекурсивну функцію, яка приймає одновимірний масив із 100 цілих чисел 
# заповнених випадковим чином і знаходить позицію, з якої починається послідовність із 10 чисел,
# сума яких мінімальна. вивести на екран весь масив, вивести на екран послідовність
print("===== Ex. 4=====")

import random

def find_min_sum_position(arr, current_position=0, min_sum_position=0, current_min_sum=float('inf')):
    # Базовий випадок: якщо досягнуто кінець масиву
    if current_position + 10 > len(arr):
        return min_sum_position
    
    # Рекурсивний випадок: обчислити суму для поточної позиції
    current_sum = sum(arr[current_position:current_position+10])
    
    # Порівняти з поточним мінімумом та оновити значення, якщо потрібно
    if current_sum < current_min_sum:
        current_min_sum = current_sum
        min_sum_position = current_position
    
    # Рекурсивно викликати для наступної позиції
    return find_min_sum_position(arr, current_position + 1, min_sum_position, current_min_sum)

# Згенерувати масив з 100 випадкових цілих чисел
random_numbers = [random.randint(1, 100) for _ in range(100)]

# Вивести весь масив
print("Весь масив:")
print(random_numbers)

# Викликати функцію та отримати позицію
result_position = find_min_sum_position(random_numbers)

# Вивести послідовність з мінімальною сумою
min_sequence = random_numbers[result_position:result_position+10]
print(f"\nПослідовність з 10 чисел з мінімальною сумою:")
print(min_sequence)