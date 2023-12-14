=======
# print(s)

# number = int(input("Enter 4-digit number: "))
# # # 1324
# n1 = number // 1000

# n2 = number // 100 % 10

# n3 = number // 10 % 10

# n4 = number % 10
# #
# result = n1 * n2 * n3 * n4
# print(f"n1: {n1} n2: {n2} n3: {n3} n4: {n4}")
# print(f"Result: {result}")

# ########

# # умови
# #v1

# # n1 = 10
# # n2 = 20

# # v2
# n1, n2 = 10, 20 # множинне привласнення

# print(n1 > n2)
# print(n1 >= n2)
# print(n1 < n2)
# print(n1 <= n2)
# print(n1 == n2) # поверне True, якщо обидва операнди рівні (однакові)
# print(n1 != n2, end="\n" "\n") # поверне True, якщо обидва операнди різні
# #
# print(1 == 1 and 3 == 3) # поверне True, якщо обидва операнди рівні True, інакше False 
# print(1 == 1 or 2 == 3) # поверне True, якщо хоча б один операнд дорівнює True, інакше False
# #
# is_valid = False
# print(is_valid)
# print(not is_valid) # not -> інверсіяБ якщо значення False стане True і навпаки

# print("hello" in "hello world") # виведе True

################

# hours = int(input("Enter hours: "))

# if 12 <= hours < 24:
# 	print("PM")
# elif 0 <= hours < 12:
# 	print("AM")
# # if hours >= 12 and hours < 24:
# # 	print("PM")
# else:
# 	print("Incorrect hours!")

# # ввести рейтинг фільму: якщо рейтинг дорівнює 5 або 4 - ок, інакше - погано
# # 
# # 
# film_rating = int(input("Enter film rating: "))

# if film_rating > 0 and film_rating <= 5:
# 	if film_rating == 4 or film_rating == 5:
# 		print("Ok!")
# 	else:
# 		print("Not OK!")
# else:
# 	print("Incorrect rating!")

# print("Hello World")

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

