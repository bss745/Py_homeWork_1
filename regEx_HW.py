# Написати валідації за допомогою регулярних виразів та протестувати на рiзних кейсах:
import re

# №1 ﻿- домашній номер телефону (тільки цифри та довжина номера)
print("===== Ex. 1 =====")

def validate_home_phone_number(phone_number):
    pattern = re.compile(r'^\d{5,7}$')

    if pattern.match(phone_number):
        return True
    else:
        return False

phone_number = input("Введіть домашній номер телефону: ")

if validate_home_phone_number(phone_number):
    print("Номер телефону валідний.")
else:
    print("Номер телефону не валідний.")

# 2 - Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
print("===== Ex. 2 =====")

def validate_mobile_phone_number(phone_number):
    pattern = re.compile(r'^\+?\d{10,15}$')

    if pattern.match(phone_number):
        return True
    else:
        return False

phone_number = input("Введіть мобільний номер телефону: ")

if validate_mobile_phone_number(phone_number):
    print("Мобільний номер телефону валідний.")
else:
    print("Мобільний номер телефону не валідний.")

# 3- email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)
print("===== Ex. 3 =====")

def validate_email(email):
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    if pattern.match(email):
        return True
    else:
        return False

user_email = input("Введіть свій email: ")

if validate_email(user_email):
    print("Email валідний.")
else:
    print("Email не валідний.")
    
# 4 - ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)
print("===== Ex. 4 =====")

def validate_full_name(full_name):
    pattern = re.compile(r'^[a-zA-Zа]{2,20}\s[a-zA-Zа]{2,20}\s[a-zA-Zа]{2,20}$')

    if pattern.match(full_name):
        return True
    else:
        return False

user_full_name = input("Введіть ПІБ клієнта: ")

if validate_full_name(user_full_name):
    print("ПІБ валідний.")
else:
    print("ПІБ не валідний.")