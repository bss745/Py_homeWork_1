# ввести з клавіатури число
# -  програма переводить в милі або ярди або дюйми

n1 = int(input("Введіть кількість метрів: "))
n2 = int(input("Введіть число від 1 до 3: "))

if n2 == 1:
	result = int(n1 *  1.09)
	print(f"{result} ярдів")
elif n2 == 2:
	result = int(n1 *  2.54)
	print(f"{result} дюймів")
elif n2 == 3:
	result = int(n1 *  1.8)
	print(f"{result} міль")
else:
	print("Число повинно бути від 1 до 3!")

