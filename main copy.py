a: int = 10
b: int = 15
c: int = 20

print(a + b + c)
print(a * b * c)

ac: float = 12.5
bd: float = 7.0
s = ac * bd / 2

print(s)

number = int(input("Enter 4-digit number: "))
# # 1324
n1 = number // 1000

n2 = number // 100 % 10

n3 = number // 10 % 10

n4 = number % 10
#
result = n1 * n2 * n3 * n4
print(f"n1: {n1} n2: {n2} n3: {n3} n4: {n4}")
print(f"Result: {result}")

########

# умови
#v1

# n1 = 10
# n2 = 20

# v2
n1, n2 = 10, 20 # множинне привласнення

print(n1 > n2)
print(n1 >= n2)
print(n1 < n2)
print(n1 <= n2)
print(n1 == n2) # поверне True, якщо обидва операнди рівні (однакові)
print(n1 != n2, end="\n" "\n") # поверне True, якщо обидва операнди різні
#
print(1 == 1 and 3 == 3) # поверне True, якщо обидва операнди рівні True, інакше False 
print(1 == 1 or 2 == 3) # поверне True, якщо хоча б один операнд дорівнює True, інакше False
#
is_valid = False
print(is_valid)
print(not is_valid) # not -> інверсіяБ якщо значення False стане True і навпаки

print("hello" in "hello world") # виведе True