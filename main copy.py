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
