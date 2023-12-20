# print("Hello world")
#
# print("Hello world!")
# print()
# print('test')

# print("Hello world", "Text1", "Text2", sep=", ", end=" ")
# print("Hello world")
# print('test')

# однорядковий коментар

'''
три одинарні лапки
багаторядковий
коментар
тут можна писати будь-який текст і він буде проігнорований інтерпретатором
'''

# Ctrl + / -> comment или uncomment

# print("hello11")
# print("hello22")
#
# aljfjklsdfjkvskjfd
# print("qwerty")

####
# escape послідовності
# \n -> перенесення на новий рядок
# print("Hello\n\nworld")
# # \t -> табуляція -> 4 пробіли. (буває в консолі 2 або 8 пробіли)
# print("Hello\n\tworld")
# print("\\ -> дзеркалювання, екранування – якщо необхідно службовий символ зробити друкованим")
# print("Hello\\n\\t\"world\"")
# print("\\\\\\\\\\")
# # print("\n" * 10)

#####
# int -> ціле число 12
# float -> дробове число 12.5
# bool -> логічний тип даних: True False
# str -> рядок - масив (набір) символів

# Змінна - це іменована область оперативної пам'яті значення можна змінювати
# number: int = 10
# print(number)
# print(type(number))
# number = 20.5
# print(number)
# print(type(number))
# number = "Vasya"
# print(number)
# print(type(number))
# number = True
# print(number)
# print(type(number))

# = оператор присвоєння
# userName1 = "Vasya"
# print(userName1)
# user_name = "Petya"
# print(user_name)
###

# input -> буде очікувати на введення даних з клавіатури в консолі і поверне за замовчуванням значення типу даних str
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# # # v1
# # print("Name: ", name, " Age: ", age)
# # # v2 конкатенація - складання рядків. Рядок + рядок -> один великий рядок
# # print("Name: " + name + " Age: " + str(age))
# # # print("Name: " + name + " Age: " + age, 1234, "qwehbkqwer" + "sdbhdvsfkjhbdsvafbk")
# # # v3 інтерполяція рядка - вбудовування змінних у рядок завдяки функції format (вивчимо докладніше пізніше)
# print(f"Name: {name} age: {age}")
# #
# # print(int(age) + 10)

###########
################################################################
# + - * /
# print(2 + 3)
# print(2 - 3)
# print(2 * 3)
# print(2 / 3)
# print(2 ** 3)  # основа ** показник (зведення в ступінь
# print(2 // 3)  # ціла частина від розподілу
# print(2 % 3)  # залишок від ділення

# num1 = 15
# num2 = 8
# print(num1 // num2)
# print(num1 % num2)
# print(num1 / num2)

############
# ввести з клавіатури тризначне число та вивести суму цифр цього числа
# // %
# int() - так як input поверне str, нам потрібно цей рядок привести до типу int (ціле число)
# щоб можна було застосовувати арифметичні оператори
# number = int(input("Enter 3-digit number: "))
# # 146
# n1 = number // 100
# # v1
# n2 = number // 10 % 10
# # v2
# # n2 = number % 100 // 10
# n3 = number % 10
#
# result = n1 + n2 + n3
# print(f"n1: {n1} n2: {n2} n3 {n3}")
# print(f"Result: {result}")

# number = 10
# print(number)

# у Python є такі базові типи винятків:

# BaseException: базовий тип для всіх вбудованих винятків

# Exception: базовий тип, який зазвичай застосовується для створення своїх типів винятків

# ArithmeticError: базовий тип для винятків, пов'язаних з аріфметичними операціями
# (OverflowError, ZeroDivisionError, FloatingPointError)

# BufferError: Виняток, який виникає при неможливості виконати операцію з буфером

# LookUpError: базовий тип для винятків, які виникають під час звернення до колекцій
# за некоректним ключем або індексом (наприклад, IndexError, KeyError)

# https://docs.python.org/3/library/exceptions.html

# IndexError: виняток виникає, якщо індекс при зверненні до елемента колекції знаходиться 
# поза допустимим діапазоном

# KeyError: виникає, якщо у словнику немає ключа, за яким відбувається звернення до елемента словника

# OverFlowError: виникає, якщо результат арифметичної операції не може бути представлений поточним
# чисельним типом (зазвичай типом float)

# RecursionError: виникає, якщо перевищено допустиму глибину рекурсії

# TypeError: якщо операція або функція застосовується до значення неприпустимого типу

# ValueError: виникає, якщо операція або функція одержують об'єкт коректного типу з некоректним значенням

# ZeroDivisionError: виникає при розподілі на нуль

# NotImplementedError: тип виключення для вказівки, що якісь методи класу не реалізовані

# ModuleNotFoundError: виникає при неможливості знайти модуль при його імпорті директивою import

# OSError: тип винятків, які генеруються при виникненні помилок системи (наприклад, неможливо знайти файл,
# пам'ять диска заповнена і т.д.)

try:
	num1 = int(input("Enter first number: "))
	num2 = int(input("Enter second number: "))

	result = num1 / num2

	print(f"Result: {result}")
except ZeroDivisionError as error:
	print(f"ZeroDivisionError occurred: {error}")
except ValueError as error:
	print("Enter only integer values, please!")
	print(f"ValueError: {error}")
except Exception as error: # Exception -> базовий тип виключення пишемо останнім з except
	print(f"Exception occurred: {error}")
finally: # Відпрацьовує завжди. Писати при потребі
	print("End of calculation")

print("some text")

try:
	name = input("Enter your name: ")

	if 1 < len(name) < 20:
		print(f"Hello, {name}")
	else:
		raise Exception("Please enter a valid name!") # raise -> згенерувати виняток (кинути виняток)
except Exception as e:
	print(f"Error: {e}")

##########################
	
try:
	print("1. Start game\n2. Settings\n3. Saved games\n4. Exit")
	user_select = int(input("Enter menu number: "))

	# v1
	if user_select == 1:
		print("Game started")
	elif user_select == 2:
		print("Settings opened")
	elif user_select == 3:
		print("Saved games opened")
	elif user_select == 4:
		print("Exit...")
	else:
		print("Incorrect menu item!")

	#v2
	match user_select:
		case 1:
			print("Game started")
		case 2:
			print("Settings opened")
		case 3:
			print("Saved games opened")
		case 4:
			print("Exit...")
		case _:
			print("Incorrect menu item!")
except Exception as e:
	print(f"Error {e}")

#################################
	
print(num := 74) # моржовий оператор

################################

_ = "Petya"
print(_)

################################

#### Цикли
# - while
# - for

# v1
# i = 0

# while i < 10:
# 	print(i, end=" ")
# 	i += 1 # i = i + 1

# print("\ntest")

# v2
i = 0

while True:
	
	if i == 5:
		print("continue...")
		i += 1
		continue	# пропустить подальші дії циклу, але цикл не зупиниться

	if i >= 10:
		print("break...")
		break	# цикл зупиниться (повне зупинення циклу)

	print(i)
	i += 1

###############################################
	
sum_nums = 0
count = 0

try:
	while True:
		try:
			number = int(input("Enter any number or 0 for exit: "))
			if number == 0 and count == 0:
				print("Enter another number!")
				continue

			if number == 0:
				print("end...")
				break

			sum_nums += number
			count += 1
		except ValueError as error:
			print("Enter numbers only!")

	average = sum_nums / count
	print(f"Sum: {sum_nums}")
	print(f"Count: {count}")
	print(f"Average {average}")

except Exception as error:
	print(error)

