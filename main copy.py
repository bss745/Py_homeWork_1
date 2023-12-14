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
