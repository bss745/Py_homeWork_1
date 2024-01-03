import random

NUMS_SIZE = 10
NUM_MIN = -100
NUM_MAX = 100
numbers = []
negative_numbers = 0
pared_numbers = 0
unpared_numbers = 0
div_three = 0
div_MinMax = 1
sum = 0

for i in range(NUMS_SIZE):
	numbers.append(random.randint(NUM_MIN, NUM_MAX))
	if numbers[i] < 0:
		negative_numbers += numbers[i]
print("========================================================")
print("===Ex. 1===")
print(numbers)
print(negative_numbers)

for i in range(NUMS_SIZE):
	numbers.append(random.randint(NUM_MIN, NUM_MAX))
	if numbers[i] % 2 == 0:
		pared_numbers += numbers[i]
print("===Ex. 2===")
print(pared_numbers)

for i in range(NUMS_SIZE):
	numbers.append(random.randint(NUM_MIN, NUM_MAX))
	if numbers[i] % 2 != 0:
		unpared_numbers += numbers[i]
print("===Ex. 3===")
print(unpared_numbers)

for i in range(NUMS_SIZE):
	numbers.append(random.randint(NUM_MIN, NUM_MAX))
	if numbers[i] % 3 == 0:
		div_three += numbers[i]
print("===Ex. 4===")
print(div_three)
print()

min_number = min(numbers)
max_number = max(numbers)
for i in range(NUMS_SIZE):
	numbers.append(random.randint(NUM_MIN, NUM_MAX))
	div_MinMax = min_number * max_number
print("===Ex. 5===")
print(min_number)
print(max_number)
print(div_MinMax) 

for i in range(NUMS_SIZE):
	numbers.append(random.randint(NUM_MIN, NUM_MAX))
	if numbers[i] > 0:
		sum += numbers[i]
print("===Ex. 6===")
print(sum)
print()



#### v2
print("========================================================")

new_list = []
list_2 = []
list_3 = []
list_4 = []
list_5 = []

for i in range(NUMS_SIZE):
	new_list.append(random.randint(NUM_MIN, NUM_MAX))
	if new_list[i] % 2 == 0:
		list_2.append(new_list[i])
print(new_list)
print(list_2)
print()

for i in range(NUMS_SIZE):
	new_list.append(random.randint(NUM_MIN, NUM_MAX))
	if new_list[i] % 2 != 0:
		list_3.append(new_list[i])
print(list_3)
print()

for i in range(NUMS_SIZE):
	new_list.append(random.randint(NUM_MIN, NUM_MAX))
	if new_list[i] < 0:
		list_4.append(new_list[i])
print(list_4)
print()

for i in range(NUMS_SIZE):
	new_list.append(random.randint(NUM_MIN, NUM_MAX))
	if new_list[i] > 0:
		list_5.append(new_list[i])
print(list_5)
print()
	



