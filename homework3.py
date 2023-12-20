# 1. Користувач вводить із клавіатури номер дня тижня (1-7). 
# Необхідно вивести на екран назви дня тижня. Наприклад, якщо 1, на екрані напис понеділок,
# 2 — вівторок тощо.

try:
	user_select = int(input("Enter day of the week: "))

	match user_select:
		case 1:
			print("Monday")
		case 2:
			print("Tuesday")
		case 3:
			print("Wednesday")
		case 4:
			print("Thursday")
		case 5:
			print("Friday")
		case 6:
			print("Saturday")
		case 7:
			print("Sunday")
		case _:
			print("Wrong day of the week!")
except Exception as e:
	print(f"Error {e}")

######################################################
	
# 2. Користувач вводить два числа. Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран
# у порядку зростання

try:
	num1 = int(input("Введіть перше число: "))
	num2 = int(input("Введіть друге число: "))

except ValueError as error:
	print("Enter only integer values, please!")
except Exception as error: 
	print(f"Exception occurred: {error}")

	if num1 == num2:
		print("Введені числа рівні")
		
	elif num1 > num2:
		print(num1)
		print(num2)

	else:
		print(num2)
		print(num1)

#############################################
	
# 3. Користувач вводить два числа та матем дію: + - * або /
# Залежно від введеної матем дії вивести результат
	
num3 = int(input("Введіть перше число вправи 3 : "))
num4 = int(input("Введіть друге число вправи 3: "))

try:
	result = num3 / num4
	print(f"Result: {result}")
	
except ZeroDivisionError as error:
	print(f"ZeroDivisionError occurred: {error}")
except ValueError as error:
	print("Enter only integer values, please!")
	print(f"ValueError: {error}")
except Exception as error: 
	print(f"Exception occurred: {error}")
