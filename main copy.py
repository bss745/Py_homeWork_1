
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
