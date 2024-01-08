# Кортеж (tuple) - константний (inmutable) список
# можна працювати як із звичайним списком, тільки не можна нічого міняти
# (функції, які змінюють колекцію відсутні в кортежі)
# CRUD -> create, read, update, delete (у кортежі можна робити тільки read)

# info = ("test1", 123)
# print(info)
# print(type(info))

# info = "test2", 123456, 789654
# print(info)
# print(type(info))

# print(info[0])

# # info[0] = 123 #TypeError: 'tuple' object does not support item assignment

# num = int(input("Enter number: "))
# nums = 12, int(input("Enter number: ")), num
# print(nums)

##################

# import copy

# info = ("test1", 123)
# test = copy.deepcopy(info)
# print(test)

# info_copy = info
# print(info_copy)
# print(info)

# info_list = list(info)
# print(info_list)
# info_list.append(123)
# print(info_list)
# print(info)

# info = tuple(info_list)
# print(info)
# print(info_list)
# print(info[1:3])
# print(info)

##############################

# for num in 1, 2, 3, 4, 5, 6, "Hello", 7:
# 	print(num)

# for num in range(5):
# 	print(num)

# for num in range(1, 5):
# 	print(num)

# for num in range(1, 5, 2):
# 	print(num)

# print(range(5))
# print(range(1, 5))
# print(range(1, 5, 2))
# result = range(5)
# print(result)
# print(type(result))

# numbers = list(range(10))
# print(numbers)

# numbers = list(range(3, 10))
# print(numbers)

# numbers = list(range(1, 10, 2))
# print(numbers)

# numbers = list(range(10, 0, -1))
# print(numbers)

# numbers = tuple(range(10, 0, -1))
# print(numbers)

# result = sorted(numbers)
# print(result)
# print(numbers)

################################
## DICTIONARY ##
# dict -> словник, колекція key: value

# # users = {
# # 	1: "John",
# # 	2: "Vasya",
# # 	3: "Petya",
# # 	"key1": "some value",
# # 	2.4: 123,
# # 	True: 111,
# # 	2: "qwerty" # дублювати ключі не можна!
# }

# print(users)
# print(type(users))
# print(users[1]) # [1] -> це не індекс, а key
# print(users["key1"])
# print(users[2.4])
# print(users[True])
# print(users[2])

# users_list = [
# 	("+11112567", "Tom"),
# 	("+49855545", "Bob"),
# 	("+38555402", "Alice")
# ]

# users_dict = dict(users_list)
# print(users_dict)

# users_list = list(users_dict)
# print(users_list)

######################################
##

# users = {
# 	("+11111111", "Tom"),
# 	("+22222222", "Bob"),
# 	("+33333333", "Alice")
# }

# users_dict = {
# 	("+11111111": "Tom"),
# 	("+22222222": "Bob"),
# 	("+33333333": "Alice")
# }

# print(type(users))

# users_dict = dict(users)
# print(users_dict)
# print(users_dict["+33333333"]) # TypeError: 'set' object is not subscriptable
# users_dict["+33333333"] = "Petya" # чогось так не працює
# print(users_dict)

# users_dict["+44444444"] = "Test"
# print(users_dict)
# print()

# for key in users_dict:
# 	print(users_dict[key], end=" ") # TypeError: list indices must be integers or slices, not tuple

# print()

# for key in users_dict.keys():
# 	print(key, end=" ") # AttributeError: 'list' object has no attribute 'keys'

# print()
# print(users_dict.keys())
# print(list(users_dict.keys()))

# for value in users_dict.values():
# 	print(value, end=" ")
# print()
# print(users_dict.values())

# print()

# for key, value in users_dict.items():
# 	print(f"key: {key} value: {value}")
# print()
# print(users_dict.items())

#####
## приклади функцій в словниках

# users = {
# 	"+11111111": "Tom",
# 	"+33333333": "Bob",
# 	"+55555555": "Alice"
# }

# print(users["+33333333"])
# print(users.get("+33333333", "key not exists"))

# # del users["+55555555"]
# # print(users)
# deleted_value = users.pop("+55555550", "key not exist")
# print(deleted_value)
# print(users)

# users.clear()
# print(users)

###
# users_1 = {
# 	"+11111111": "Tom",
# 	"+33333333": "Bob",
# 	"+55555555": "Alice"
# }
# users_copy = users_1.copy()

# print(users_1)
# print(users_copy)
# users_copy[111] = "qqqqqq"
# print(users_1)
# print(users_copy)

# users_2 = {
# 	"+11111111": "eeeeee",
# 	"+44444": "qqqqqq",
# 	"+12341234": "wwwwww"
# }

# users_1.update(users_2)
# print(users_1)
# print(users_2)

#######
# json
# users = {
# 	"Vasya": {
# 		"phone": "123123",
# 		"email": "qwerty1@mail.com",
# 		"hobbies": ["one", "two", "three"]
# 	},
# 	"Petya": {
# 		"phone": "1345556",
# 		"email": "fghjslkb@mail.com",
# 		"hobbies": "hockey",
# 		"add_data": {
# 			1: "test-1",
# 			2: "test-2"
# 		}
# 	}
# }
# print(users["Vasya"]["hobbies"][1])
# print(users["Petya"]["add_data"][2])

##
# v1
# key = input("Enter key: ")
# if key in users:
# 	print(users[key])
# else:
# 	print("Nothing found!")

# v2
# key = input("Enter key: ").strip().lower()
# for current_key in users.keys():
# 	if key == current_key.lower():
# 		print(users[current_key])
# 		break
# else:
# 	print("Nothing found!")

# #####
# for i in range(5):
# 	print(i)
# 	if i >= 3:
# 		break
# else:
# 	print("end")

######################
# # Множини (set) представляють ще один вид набору, який зберігає тільки унікальні елементи.
# Дублікати будуть видалені

# users = {"Tom", "Bob", "Alice", "Tom"}
# print(users)
# print(type(users))

# people = ["Mike", "Phil", "John"]
# users = set(people)
# print(users)
# # # # #
# print(len(users))
# # # # #
# users.add("Sam")
# print(users)
# # #
# users = {"Tom", "Bob", "Alice"}
# #
# user = "Tom"
# if user in users:
# 	users.remove(user)	# якщо немає генерується виняток
# print(users)
# # #
# users = {"Tom", "Bob", "Alice"}
# #
# users.discard("Dolly") # елемент "Dolly" відсутній і метод нічого не робить
# print(users)
# # # #
# users.clear()
# print(users)
# # #
# users = {"Tom", "Bob", "Alice"}
# #
# for user in users:
# 	print(user)

# # copy() працює так само як в list, dict і т.д.
# #
users = {"Tom", "Bob", "Alice"}
users_2 = {"Sam", "Robby", "Bob"}

users_3 = users.union(users_2)
print(users_3)
# #
users = {"Tom", "Bob", "Alice"}
users_2 = {"Sam", "Robby", "Bob", "Tom", "Joe"}
#
# # v 1
users_3 = users.intersection(users_2) # перетин множин(що загальне у першої та другої множини)
# # v 2
print(users & users_2)
print(users_3)
# #
users = {"Tom", "Bob", "Alice"}
users_2 = {"Sam", "Robby", "Bob", "Tom", "Joe"}
users.intersection_update(users_2) # те саме тільки результат буде записаний в users
print(users)

users = {"Tom", "Bob", "Alice"}
users_2 = {"Sam", "Kate", "Bob"}
#
# # v1
users_3 = users.difference(users_2) # що є тільки в першій і немає у другій множині
print(users_3)
# # v2
print(users - users_2)
# #
users.difference_update(users_2)
print(users)
print(users_2)
# #
users = {"Tom", "Bob", "Alice"}
users_2 = {"Sam", "Robby", "Bob", "Tom", "Joe"}
# # v1
users_3 = users.symmetric_difference(users_2) # унікальні значення першої і другої множин
print(users_3)
# 
# # v2
print(users ^ users_2)

# #
users = {"Tom", "Bob", "Alice"}
superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}

print(users.issubset(superusers)) # True
print(superusers.issubset(users)) # False

# #
users = {"Tom", "Bob", "Alice"}
superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}

print(users.issuperset(superusers)) # False
print(superusers.issuperset(users)) # True

# # Тип Frozen set є видом множин, які не можуть бути змінені (за типом typle у list)
users = frozenset({"Tom", "Bob", "Alice"})
print(users)
users = set(users)
print(users)
# # можна використовувати всі функції звичайного set крым тих, що модифыкують значення 


######################## HOME WORK ###############################

# 1. Створить список чисел. Заберіть дублікати значень. Вивести унікальні значення
import random

def create_list_with_rundom_numbers(list_length=10, start_number=1, end_number=10) -> list:
	# v1
	# new_list = list()
	# for _ in range(list_length):
	# 	new_list.append(random.randint(start_number, end_number))
	# return new_list
	
	# v2 (через генератори)
	return [random.randint(start_number, end_number) for _ in range(list_length)]


def remove_duplicates(list_to_remove) -> list:
	return list(set(list_to_remove))


def get_unique_values(list_numbers) -> list:
	unique_values = []
	for number in list_numbers:
		if list_numbers.count(number) == 1:
			unique_values.append(number)

	return unique_values

numbers = create_list_with_rundom_numbers()
print(numbers)

numbers_without_duplicates = remove_duplicates(numbers)
print(numbers_without_duplicates)

unique_numbers = get_unique_values(numbers)
print(unique_numbers)


###############
# 2. Дано 2 списка
# Порахуйте скільки чисел міститься як у першому списку, так і у другому

numbers_1 = create_list_with_rundom_numbers(start_number=1, end_number=20)
numbers_2 = create_list_with_rundom_numbers(start_number=1, end_number=20)

print(numbers_1)
print(numbers_2)


def calc_number_of_equal_numbers_v1(nums_1: list[int], nums_2: list[int]) -> int:
	print(set(nums_1).intersection(set(nums_2)))
	return len(set(nums_1).intersection(set(nums_2)))


def calc_number_of_equal_numbers_v2(nums_1: list[int], nums_2: list[int]) -> int:
	counter = 0
	equal_numbers = []
	for num in nums_1:
		if num in nums_2 and num not in equal_numbers:
			equal_numbers.append(num)
			# print(num, end=" ")
			counter +=1

	print(equal_numbers)
	return counter

print(f"Result: {calc_number_of_equal_numbers_v1(numbers_1, numbers_2)}")
print(f"Result: {calc_number_of_equal_numbers_v2(numbers_1, numbers_2)}")


######
# 3. 

def generate_text(seed="Hello", multiplier=5):
	return (seed + " ") * multiplier


def calc_diff_strings(text: str) -> int:
	print(text)
	print(text.split())
	return len(set(text.split()))


print(calc_diff_strings(generate_text("Hello world", 10)))
print(calc_diff_strings(generate_text("Hello how are you thank you", 1)))