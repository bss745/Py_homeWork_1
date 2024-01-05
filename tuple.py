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

users = {
	("+11111111", "Tom"),
	("+22222222", "Bob"),
	("+33333333", "Alice")
}

# users_dict = {
# 	("+11111111", "Tom"),
# 	("+22222222", "Bob"),
# 	("+33333333", "Alice")
# }

print(type(users))

users_dict = dict(users)
print(users_dict)
print(users_dict["+33333333"]) # TypeError: 'set' object is not subscriptable
users_dict["+33333333"] = "Petya" # чогось так не працює
print(users_dict)

# for key in users:
# 	print(users[key], end=" ") # TypeError: list indices must be integers or slices, not tuple

# print()

for key in users.keys():
	print(key, end=" ") # AttributeError: 'list' object has no attribute 'keys'