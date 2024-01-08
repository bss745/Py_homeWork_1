# def say_hello():
# 	print("Hello")

# number = 10
# print(number)
# print(say_hello)
# say_hello() # виклик функції (функція починає працювати)
# say_hello()

# def say_hello():
# 	print("Hello friends")

# say_hello()

# def say_hello(name):
# 	print(f"Hello {name}")
# 	name = "qqqq"
# 	# print(f"Hello {name}")

# say_hello("Test user")
# name = "Anton"
# say_hello(name)
# print(name)

# def say_hello_name(username):
# 	print(f"Hello, {username}")

# say_hello_name("Vasya")
# name = "Petya"
# say_hello_name(name)

# def user_info(name: str, age: int, hobby: str) -> None:
# 	print(f"Welcome, {name}! Your age: {age} and hobby is {hobby}")

# try:
# 	name = input("Enter your name: ")
# 	age = int(input("Enter your age: "))
# 	user_hobby = input("Enter your hobby: ")
# 	user_info(name, age, user_hobby)
# except Exception as e:
# 	print(e)

##############################

#####################
# після того, як відпрацює ключове слово return - функція припиняє свою роботу (тільки функція)
# return - поверне результат роботи функції. Після відпрацювання return - решта дій функції не
# відпрацюють та функція завершить свою роботу. Якщо у функції є цикл - у циклі return працює як
# break, але на відміну від break поверне результат, а не просто зупинить дії. Якщо у функції є цикли,
# і в одному із циклів спрацював return - функція припинить свою роботу. Ключове слово return може
# зустрічатися в тілі функції скільки завгодно разів.
	
# def add(n1, n2):
# 	return n1 + n2


# def sub(n1, n2):
# 	return n1 - n2


# def mult(n1, n2):
# 	return n1 * n2

# def division(n1, n2):
# 	return n1 / n2

# def calculate() -> None:
# 	first_number = int(input("Enter first number: "))
# 	second_number = int(input("Enter second number: "))
# 	math_operation = input("Enter math operation + - * / ")

# 	match math_operation:
# 		case "+":
# 			print(f"{first_number} {math_operation} {second_number} = {add(first_number, second_number)}")
# 		case "-":
# 			print(f"{first_number} {math_operation} {second_number} = {sub(first_number, second_number)}")
# 		case "*":
# 			print(f"{first_number} {math_operation} {second_number} = {mult(first_number, second_number)}")
# 		case "/":
# 			print(f"{first_number} {math_operation} {second_number} = {division(first_number, second_number)}")
# 		case _:
# 			raise Exception("Invalid math operation!")
		
# try:
# 	calculate()
# except ValueError:
# 	print("Enter valid number!")
# except ZeroDivisionError:
# 	print("Do not divide by zero, please!")
# except Exception as error:
# 	print(error)

########
# def user_info(name: str, age: int = 18, hobby: str = "no hobby") -> None:
# 	print(f"Welcome, {name}! Your age: {age} and hobby is {hobby}")

# user_info("Vasya", 33, "test")
# user_info("Vasya", 33)
# user_info("Vasya")

# user_info(hobby="walking", name="Petya", age=33)

#########
# Усі параметри, які розташовуються праворуч від символа * отримують значення
# лише за ім'ям

def print_person(name, *, age, company):
	print(f"Name: {name} Age: {age} Company: {company}")


print_person("Bob", age=41, company="Microsoft")


def print_person(*, name, age, company):
	print(f"Name: {name} Age: {age} Company: {company}")


print_person(name="Mike", age=44, company="Oracle")

#######
# Якщо навпаки треба визначити параметри, яким можна передавати значення лише за позицією
# тобто позиційні параметри, можна використовувати символ / (всі параметри які йдуть до символу /, 
# є позиційними і можуть отримувати значення лише за позицією)
def print_person(name, /, age, company="Microsoft"):
	print(f"Name: {name} Age: {age} Company: {company}")


print_person("Tom", company="JetBrains", age=24)
print_person("Ellen", 44)


def print_person(name, /, age=18, *, company):
	print(f"Name: {name} Age: {age} Company: {company}")


print_person("Sam", company="Google")
print_person("Jack", 37, company="Apple")
print_person("Bryan", company="HP", age=42)