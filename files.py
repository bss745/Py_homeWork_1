#### FILES ####
##
# r (Read) - файл відкривається для читання. Якщо файл не знайдено, 
# то генерується виняток FileNotFoundError

# w (Write) - файл відкривається для запису. Якщо файл відсутній, то він створюється.
# Якщо такий файл вже є, то він створюється заново і відповідно старі дані в ньому стираються.

# a (Append) - файл відкривається для запису. Якщо файл вітсутній, то він створюється.
# Якщо подібний файл вже є, дані записуються в його кінець.

# b (Binary) - Використовується для роботи з бінарними файлами. Застосовується разом з
# іншими режимами - w або r.
# 
#	# v1
# try:
# 	my_file = open("hello.txt", "w")
# 	try:
# 		my_file.write("Hello, John")
# 	except Exception as e:
# 		print(e)
# 	finally:
# 		my_file.close()
# except Exception as e:
# 	print(e)

#	# v2
# with open("hello_1.txt", "w") as text_file:
# 	text_file.write("and goodbye")

# with open("hello_1.txt", "a") as text_file:
# 	text_file.write("&\nBarbara\n")

# with open("hello_1.txt", "r") as myfile:
# 	# v1
# 	# result = myfile.read()
# 	# print(result)
# 	# v2
# 	# result = myfile.readline()
# 	# print(result)
# 	# result = myfile.readline(3)
# 	# print(result)
# 	# v3
# 	# result = myfile.readlines()
# 	# print(result)
# 	# v4
# 	# for line in myfile:
# 	# 	print(line, end="")
# 	# v5
# 	line = myfile.readline()
# 	while line:
# 		print(line, end="")
# 		line = myfile.readline()

########
# FILENAME = "notes.txt"
# NOTES_COUNT = 3

# notes = []

# for i in range(NOTES_COUNT):
# 	notes.append(input(f"Enter note: {i + 1}: ").strip())

# with open(FILENAME, "a") as file:
# 	for i in range(NOTES_COUNT):
# 		file.write(f"{i + 1}. {notes[i]}\n")

# with open(FILENAME, "r") as file:
# 	print(file.read())

###
# import pickle
# FILENAME = "notes.dat"

# users = [
# 	["John", "123456789"],
# 	["Peter", "987654321"],
# 	["Vasya", "165498765"]
# ]

# with open(FILENAME, "wb") as file:
# 	pickle.dump(users, file) # серіалізація

# with open(FILENAME, "rb") as file:
# 	users_from_file = pickle.load(file) # десеріалізація
# 	print(users_from_file)
# 	for user in users_from_file:
# 		print(f"Name: {user[0]} Phone: {user[1]}")

#####
# import shelve

# FILENAMES = "notess"

# with shelve.open(FILENAMES) as users:
# 	users["John"] = "123456789"
# 	users["Peter"] = "987654321"
# 	users["Vasya"] = "462138952"

# with shelve.open(FILENAMES) as users:
# 	users["Petya"] = "123123123123"
# 	print(users["Petya"])
# 	print(users["John"])

# 	for key in users:
# 		print(f"{key} - {users[key]}")

# 	print(users)
# 	users.pop("John", "not found")

# 	print("-" * 10)

# 	for key in users:
# 		print(f"{key} - {users[key]}")

#####
import csv

FILENAME = "users.csv"

# v1
# users = [
# 	["John", "123456789"],
# 	["Peter", "987654321"],
# 	["Vasya", "165498765"]
# ]

# with open(FILENAME, "w", newline="") as file:
# 	writer = csv.writer(file)
# 	writer.writerows(users)

# with open(FILENAME, "a", newline="") as file:
# 	user = ["Anton", "888777666"]
# 	writer = csv.writer(file)
# 	writer.writerow(user)

# with open(FILENAME, "r", newline="") as file:
# 	reader = csv.reader(file)
# 	for row in reader:
# 		print(f"{row[0]} - {row[1]}")

# # v2
# users = [
# 	{"name": "John", "phone": "111"},
# 	{"name": "Petya", "phone": "222"},
# 	{"name": "Vasya", "phone": "333"}
# ]

# with open(FILENAME, "w", newline="") as file:
# 	columns = ["name", "phone"]
# 	writer = csv.DictWriter(file, fieldnames=columns)
# 	writer.writeheader()

# 	#all users
# 	writer.writerows(users)

# 	#one user
# 	user: dict = {"name": "Test", "phone": "555"}
# 	writer.writerow(user)

# with open(FILENAME, "r", newline="") as file:
# 	reader = csv.DictReader(file)
# 	for row in reader:
# 		print(row["name"], " - ", row["phone"])

#####
# import os

# os.mkdir("test_folder")

# os.rmdir("test_folder")

# file_name = "hello_2.txt"
# if os.path.exists(file_name):
# 	os.remove(file_name)
# 	print("File removed!")
# else:
# 	print("File not found!")

# доп написати скрипт для видалення всіх файлів вказаної директорії
	
# відносний шлях - щодо поточної директорії (папки де знаходиться вихідний файл, який ви запустили)
# with open("f1/f2/test.txt", "w") as myfile:
# 	myfile.write("hello world")
# ##
# with open("../../test1.txt", "w") as myfile:
# 	myfile.write("hello world")
# абсолютний шлях - повний шлях починаючи з диска С://test_folder/...

################################################################
# import json

# # # json string data
# # employee_string = '{"first_name": "Michael", "last_name": "Rodgers", "department": "Marketing"}'

# # # check data type with type() method
# # print(type(employee_string))

# # # convert string to object
# # json_object = json.loads(employee_string)

# # # check new data type
# # print(type(json_object))

# # # output
# # # <class 'dict'>

# # # access first_name in dictionary
# # print(json_object["first_name"])
# # print(json_object["department"])

# ##
# employees_string = '''
# {
# 	"employees" : [
# 		{
# 			"first_name": "Michael",
# 			"last_name": "Rodgers",
# 			"department": "Marketing"
# 		},
# 		{
# 			"first_name": "Michelle",
# 			"last_name": "Williams",
# 			"department": "Engineering"
# 		}
# 	]
# }
# '''

# data = json.loads(employees_string)

# print(type(data))
# # # output
# # # <class 'dict'>

# # access first_name
# for employee in data["employees"]:
# 	print(employee["first_name"])

# json_str = json.dumps(data)
# print(json_str)
# print(type(json_str))

################
import json
import os

# создаём путь к файлу
PATH_TO_DO_LIST = "myTodolist.json"

# функция создания файла
def create_to_do_list_json_file(path_to_storage: str) -> None:
	# если нет пути к файлу
	if not os.path.exists(path_to_storage):
		# открываем на запись с подключением юникода (язык)
		with open(path_to_storage, "w", encoding="UTF-8") as file:
			# создание переменной - словаря (ключ "todos" - значение "список")
			todos_dict: dict = {"todos": []}
			# json.dumps превращает словарь в строчку
			# и записываем строчку в специфическом формате
			file.write(json.dumps(todos_dict))
	# если файл есть - кидаем исключение
	else:
		raise FileExistsError("File already exists!")
	
# функция, которая позволяет считать все задачи
def get_todo_items(path_to_storage: str) -> dict:
	# открываем файл для чтения
	with open(path_to_storage, "r", encoding="utf-8") as file:
		# считает и вернёт словарь, в которм ключ "todos", а значение все задачи
		return json.load(file)
	
# функция добавления задач
def add_todo_item(path_to_storage: str, todo_item: str) -> str:
	# считывание текущих задач
	current_todos = get_todo_items(path_to_storage)
	# добавление, обращаемся по ключу и добавляем строчку с задачей
	current_todos["todos"].append(todo_item)
	# открываем файл и перезаписываем
	with open(path_to_storage, "w", encoding="utf-8") as file:
		# превращаем в строчку и с помощью indent форматируем для удобства чтения
		json.dump(current_todos, file, indent=4)
		return todo_item
	
# функция удаления задачи
def remove_todo_item(path_to_storage: str, todo_item: str) -> str:
	current_todos = get_todo_items(path_to_storage)
	# обращаемся к ключу и удаляем задачу по значению
	current_todos["todos"].remove(todo_item)
	# открываем файл и перезаписываем
	with open(path_to_storage, "w", encoding="utf-8") as file:
		json.dump(current_todos, file, indent=4)
		return todo_item
	
# если файл настроен как основной, то будет выполняться дальнейший код
if __name__ == "__main__":
	# если существует путь
	if os.path.exists(PATH_TO_DO_LIST):
		# получаем все задачи
		print(get_todo_items(PATH_TO_DO_LIST))
		# добавляем задачи
		add_todo_item(PATH_TO_DO_LIST, "first item")
		add_todo_item(PATH_TO_DO_LIST, "second item")
		# если что-то не нужно удаляем
		# remove_todo_item(PATH_TO_DO_LIST, "first item")
		print(get_todo_items(PATH_TO_DO_LIST))
	else:
		create_to_do_list_json_file(PATH_TO_DO_LIST)

# дописать меню
# добавить функцию изменения по порядковому номеру (от 1 до ...)
# протестировать все функции