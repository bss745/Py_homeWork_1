# ООП - об'єктно-орієнтоване програмування
# Клас - кастомний тип даних, який описує деякий об'єкт
# Клас - креслення майбутнього екземпляра об'єкта

# Інкапсуляція - приховування внутрішньої реалізації та надання санкціонованого доступу
# до інтерфейсу класу. Як чорна скринька. 
# Абстрагуємося від внутрішньої реалізації

# Спадкування - створення нового класу на основі вже існуючого
# Розширення базового класу - дочірніми/дочірніми класами
# Абстрагуємось від базового класу/класів, використовуючи дочірній клас

# Поліморфізм - один інтерфейс та багато реалізацій.
# Абстрагуємось від конкретної реалізації


# class Demo:
# 	def __init__(self, text):
# 		self.text = text

# 	def show_info(self):
# 		print("Hello world!")


# test1 = Demo("Hello world!")
# test1.show_info()
# test2 = Demo("Test")
# test2.show_info()
# print(test2.text)
# test2.text = "QQQQQQ"
# print(test2.text)
# print(test1.text)

##
# __init__ Конструктор класу - дозволяє створити екземпляр класу. 
# Можливо з параметрами та без параметрів.
# self - посилання на контекст класу, екземпляр класу
# контекст класу - все, що є частиною класу (екземпляра)

# class Person:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age

# 	def show_person(self):
# 		print(f"Name: {self.name} age: {self.age}")

# user1 = Person("Vasya", 33)
# user2 = Person("Petya", 44)
# user1.show_person()
# user2.show_person()
# print(user1.name)
# user1.name = ""
# print(user1.name)
# user1.show_person()
# # Person.show_person(user2)

#####
# Статичний метод (функція), поле (змінна) відносяться для класу, і до екземпляра
# статичний ел-т можна використовувати не створюючи екземпляр класу
# Найчастіше статичні класи використовують для опису конфігів
# та інших службових об'єктів, там де немає сенсу створювати екземпляри
# class Car:
# 	company_name = "BMW"

# 	def __init__(self, color, year):
# 		self.color = color
# 		self.year = year

# 	def show_info(self):
# 		print(f"Company: {self.company_name}\nColor: {self.color}\nYear: {self.year}")

# 	@staticmethod # декоратор, который говорит о том, что этот метод статический
# 	def show_company_name():
# 		print(f"Company: {Car.company_name}")

# car1 = Car("red", 2024)
# car1.show_info()
# car1.show_company_name()
# Car.show_company_name()
# # Car.show_info() # нужен экземпляр
# # print(Car.color) # не будет работать, т.к. color не статичское поле 

# ###############
# class InvoiceTypes:
# 	SimpleInvoice = "Simple"
# 	UrgentInvoice = "Urgent"
# 	CashInvoice = "Cash"

# print(InvoiceTypes.UrgentInvoice)

####################
##
# v2 Реалізація інкапсуляції використовуючи анотації властивостей
# class User:
# 	__name: str = "no name" # private поле доступне тільки всередині цього класу
# 	__age: int = 0
# 	__secret : int = 12345

# 	def __init__(self, name=None, age=None):
# 		# self.__name = name
# 		# self.age = age
# 		# застосовуємо інкапсуляцію
# 		self.name = name
# 		self.age = age

# 	# getter - для отримання значення приватного поля
# 	@property
# 	def name(self):
# 		return self.__name
	
# 	# setter - для санкціонованого доступу до приватної змінної (поля)
# 	@name.setter
# 	def name(self, name):
# 		if 2 < len(name) < 50:
# 			self.__name = name
# 		else:
# 			print("Incorrect name length")

# 	@property
# 	def age(self):
# 		return self.__age
	
# 	@age.setter
# 	def age(self, age):
# 		if 18 < age < 150:
# 			self.__age = age
# 		else:
# 			print("Incorrect age!")

# 	# public method - публічна (доступна ззовні) функція
# 	def show_info(self):
# 		print(f"Name: {self.__name} age: {self.__age}")
# 		# self.__secret_info()

# 	# private method - недоступна ззовні функція
# 	def __secret_info(self):
# 		print(f"Secret code: {self.__secret}")

# anton = User("Anton", -34)
# anton.show_info()
# anton.age = 40
# anton.show_info()
# anton.age = 400
# anton.show_info()
# print(anton.name)

# #######################
# class MyConverter:
# 	__money_sum = 0
# 	__uah_rate = 38.7
# 	__converter_direction = 1

# 	def __init__(self, input_money, converter_dir):
# 		self.money_sum = input_money
# 		self.converter_direction = converter_dir

# 	@property
# 	def converter_direction(self):
# 		return self.__converter_direction
	
# 	@converter_direction.setter
# 	def converter_direction(self, direction):
# 		if direction == 1 or direction == 2:
# 			self.__converter_direction = direction
# 		else:
# 			raise Exception("Provide correct converter direction!")
		
# 	@property
# 	def money_sum(self):
# 		return self.__money_sum
	
# 	@money_sum.setter
# 	def money_sum(self, money):
# 		if 0 < money < 1000000:
# 			self.__money_sum = money
# 		else:
# 			raise Exception("Provide correct sum of money!")
		
# 	# readonly property
# 	@property
# 	def uah_rate(self):
# 		return self.__uah_rate
	
# 	def show_current_uah_rate(self):
# 		print(f"Current UAH rate: {self.__uah_rate}")


# 	def show_result(self):
# 		print(self.__get_money_result())

# 	def __get_money_result(self):
# 		match self.converter_direction:
# 			case 1:
# 				return f"{self.__money_sum:.2f} UAH = {self.__get_usd_sum():.2f} USD"
# 			case 2:
# 				return f"{self.__money_sum:.2f} USD = {self.__get_uah_sum():.2f} UAH"
			

# 	def __get_usd_sum(self):
# 		return self.__money_sum / self.__uah_rate
	
# 	def __get_uah_sum(self):
# 		return self.__money_sum * self.__uah_rate
	
# try:
# 	converter_1 = MyConverter(5000, 1)
# 	converter_1.show_result()

# 	converter_2 = MyConverter(50, 2)
# 	converter_2.show_result()

# 	converter_3 = MyConverter(0, -0)
# 	converter_3.show_result()
# except Exception as error:
# 	print(error)


########################
# class Person:
# 	__name = "no name"
# 	__age = 18

# 	def __init__(self, name, age, hobby):
# 		self.name = name # name setter
# 		self.age = age	# age setter
# 		self.hobby = hobby	# public field
	
# 	@property
# 	def name(self):
# 		return self.__name
	
# 	@name.setter
# 	def name(self, name):
# 		if 2 < len(name) < 30:
# 			self.__name = name

# 	@property
# 	def age(self):
# 		return self.__age
	
# 	@age.setter
# 	def age(self, age):
# 		if 0 < age < 150:
# 			self.__age = age

# 	def show_info(self):
# 		print(f"Name: {self.__name}\nAge: {self.__age}\nHobby: {self.hobby}")


# class Company:
# 	__name = "no company name"

# 	def __init__(self, company_name: str, users: list[Person] = None):
# 		self.__name = company_name # дописать инкапсуляции проверки get и set
# 		self.users = users

# 	def show_users(self):
# 		print(f"Found {len(self.users)} users")
# 		for user in self.users:
# 			user.show_info()
# 			print()

# 	def add_user(self, user: Person):
# 		if isinstance(user, Person):
# 			self.users.append(user)
# 			return
# 		raise Exception(f"Provided value with incorrect type for user: {type(user)}")
	
# try:
# 	users: list[Person] = [Person("John", 33, "soccer"), Person("David", 36, "soccer"), Person("Julia", 25, "camping")]
# 	google = Company("Google", users)
# 	google.show_users()
# 	google.add_user(Person("Craig", 55, "coach"))
# 	google.show_users()
# except Exception as error:
# 	print(error)

#######################
# успадкування 
# class Person:
# 	__name = "no name"
# 	__age = 18

# 	def __init__(self, name, age):
# 		self.name = name # name setter
# 		self.age = age	# age setter
# 		self.__secret = 12345 # (private) -> доступ тільки всередині класу
# 		self._hobby = "no info"	# (protected) -> доступ всередині класу та в класах спадкоємцах
	
# 	@property
# 	def name(self):
# 		return self.__name
	
# 	@name.setter
# 	def name(self, name):
# 		if len(name) > 2:
# 			self.__name = name

# 	@property
# 	def age(self):
# 		return self.__age
	
# 	@age.setter
# 	def age(self, age):
# 		if age > 18:
# 			self.__age = age

# 	@property
# 	def hobby(self):
# 		return self._hobby
	
# 	def show_info(self):
# 		print(f"Name: {self.name}, Age: {self.age}")

# # v1
# # class Employee(Person): # успадковуємось від класу Person
# # 	def work(self):
# # 		print(f"{self.name} works!")
# # 		# print(self.__secret) #AttributeError: 'Employee' object has no attribute 'Employee.__secret'
# # 		# print(self.hobby) # є доступ так як у базовому класі це поле protected

# # vasya = Employee("Vasya", 33)
# # vasya.show_info()
# # vasya.work()

# # print(vasya._hobby) # до protected полів не варто звертатись безпосередньо, краще використовувати getter
# # print(vasya.hobby)
# # print(vasya.__dict__)

# # v2
# class Employee(Person):
# 	def __init__(self, name, age, company):
# 		# v1
# 		super().__init__(name, age) # виклик конструктора базового класу Person
# 		# super() -> посилання на базовий клас, отримуємо доступ до елементів базового класу
# 		# v2
# 		# Person.__init__(self, name, age)
# 		self.company = company

# 	# def work(self):
# 	# 	print(f"{self.name} works!")
# 	# 	# print(self.__secret) #AttributeError: 'Employee' object has no attribute 'Employee.__secret'
# 	# 	# print(self.hobby) # є доступ так як у базовому класі це поле protected

# 	# перевизначення методу
# 	def show_info(self):
# 		super().show_info() # виклик з методу базового класу
# 		print(f"Works in {self.company} company")

# vasya = Employee("Vasya", 33, "Google")
# vasya.show_info()
# # vasya.work()

# # print(vasya._hobby) # до protected полів не варто звертатись безпосередньо, краще використовувати getter
# # print(vasya.hobby)
# print(vasya.__dict__)


############################################

# class Employee:
# 	def __init__(self, name):
# 		self.name = name

# 	def work(self):
# 		print(f"{self.name} works!")

# class Student:
# 	def __init__(self, name):
# 		self.name = name

# 	def study(self):
# 		print(f"{self.name} studies!")

# class WorkingStudent(Student, Employee): # множинне спадкування
# 	pass

# vasya = WorkingStudent("Vasya")
# vasya.work()
# vasya.study()
# print(WorkingStudent.mro())

# [<class '__main__.WorkingStudent'>, <class '__main__.Student'>, <class '__main__.Employee'>, <class 'object'>]

# v4 приклад ромбовидного наслідування
# class Person:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age

# 	def show_info(self):
# 		print(f"Name: {self.name}\nAge: {self.age}")

# class Employee(Person):
# 	def __init__(self, name, age, company = None):
# 		super().__init__(name, age)
# 		self.company = company

# 	def show_info(self):
# 		super().show_info()
# 		print(f"Company: {self.company}")

# class Student(Person):
# 	def __init__(self, name, age, university=None):
# 		super().__init__(name, age)
# 		self.university = university	

# 	def show_info(self):
# 		super().show_info()
# 		print(f"University: {self.university}")

# class WorkingStudent(Student, Employee):
# 	def __init__(self, name, age, company, university):
# 		Student.__init__(self, name, age, university)
# 		Employee.__init__(self, name, age, company)

# 	def show_info(self):
# 		super().show_info()
# 		# Student.show_info(self)
# 		# Employee.show_info(self)

# vasya = WorkingStudent("Vasya", 33, "Google", "Tech")
# vasya.show_info()
# # print(vasya.company)
# # print(vasya.university)
# print(WorkingStudent.mro())

# [<class '__main__.WorkingStudent'>, <class '__main__.Student'>, <class '__main__.Employee'>, <class 'object'>]

##########################
# https://makina-corpus.com/python/python-tutorial-understanding-python-mro-class-search-path
# http://www.srikathtechnologies.com/blog/python/mro.aspx

####
# class Transport:
# 	def __init__(self, name, year):
# 		self.name = name
# 		self.year = year

# 	def show_info(self):
# 		print(f"Name: {self.name}\nYear: {self.year}")


# class BaseAuto(Transport):
# 	def __init__(self, name, year, wheels_count=0):
# 		super().__init__(name, year)
# 		self.wheels_count = wheels_count

# 	# перекриття метода базового класу
# 	def show_info(self):
# 		print(f"Wheels count: {self.wheels_count}")

# class WaterTransport(Transport):
# 	def __init__(self, name, year, displacement=0.):
# 		super().__init__(name, year)
# 		self.displacement = displacement

# 	# перекриття метода базового класу
# 	def show_info(self):
# 		print(f"Displacement: {self.displacement}")


# class Car(BaseAuto):
# 	def __init__(self, name, year, wheels_count, doors_count=0):
# 		super().__init__(name, year, wheels_count)
# 		self.doors_count = doors_count

# 	# перекриття метода базового класу
# 	def show_info(self):
# 		print(f"Doors count: {self.doors_count}")


# class Amphibian(WaterTransport, BaseAuto):
# 	def __init__(self, name, year, wheels_count, displacement):
# 		WaterTransport.__init__(self, name, year, displacement)
# 		BaseAuto.__init__(self, name, year, wheels_count)

# 	# перекриття метода базового класу
# 	def show_info(self):
# 		Transport.show_info(self)
# 		WaterTransport.show_info(self)
# 		BaseAuto.show_info(self)


# test_car = Amphibian("BMW", 2024, 4, 123.6)
# test_car.show_info()
# print(Amphibian.mro())

##################################
# # поліморфізм
# # https://maxdrive.kyiv.ua/dokumentacija/pochta/chto-takoe-polimorfizm-v-python

# print(len("hello"))
# print(len([1,2,6,4]))
# print(len({1,5,6,7}))
# print(len({1: "one", 2: "two"}))

# #####
# class Parrot:
# 	__name = "Kesha"

# 	def fly(self):
# 		print(f"Parrot {self.__name} can fly")

# 	def swim(self):
# 		print(f"Parrot {self.__name} can't swim")


# class Penguin:
# 	__name = "Bob"

# 	def fly(self):
# 		print(f"Penguin {self.__name} can't fly")

# 	def swim(self):
# 		print(f"Penguin {self.__name} can swim")


# class Zoo:
# 	def __init__(self, animals: list):
# 		self.animals = animals

# 	def show_zoo_animals(self):
# 		for animal in self.animals:
# 			animal.fly()
# 			animal.swim()
# 			print()

# my_animals = [Parrot(), Penguin()]
# my_zoo = Zoo(my_animals)
# my_zoo.show_zoo_animals()


# ################
# class Triangle(object):
# 	__name = "Triangle"

# 	def show_info(self):
# 		print(f"This is {self.__name}")


# class Circle(object):
# 	__name = "Circle"

# 	def show_info(self):
# 		print(f"This is {self.__name}")


# class Rectangle(object):
# 	__name = "Rectangle"

# 	def show_info(self):
# 		print(f"This is {self.__name}")

# def get_geometry_figures_info(geom_figures):
# 	for geom in geom_figures:
# 		geom.show_info()

# get_geometry_figures_info([Triangle(), Rectangle(), Rectangle(), Circle()])

###############
# Mixin классы - это классы, у которых нет данных, но есть методы
# Mixin используются для добавления одних и тех же методов в разные классы
#
# в Python примеси делаются с помощью классов
# Так как в Python нет отдельного типа для примесей, классам-примесям принято давать
# имена, заканчивающиеся на Mixin

# С одной стороны, то же самое можно делать с помощью наследования обычных классов,
# но не всегда те методы, которые нужны в разных дочерних классах, имеют смысл в родительском

# class Radio:
# 	def play_song(self):
# 		pass

# 	def set_station(self, station):
# 		pass


# class RadioUserMixin(object):
# 	def __init__(self):
# 		self.radio = Radio()

# 	def play_song_on_station(self, station):
# 		self.radio.set_station(station)
# 		self.radio.play_song()

# class Vehicle:
# 	pass


# class Car(Vehicle, RadioUserMixin):
# 	pass


#############################
### MAGIC METHODS ###
# перезавантаження операторів

from typing import Any


class Car:
	def __init__(self, name, price):
		self.name = name
		self.price = price


	def show_info(self):
		print(f"Name: {self.name}")
		print(f"Price: {self.price}")


	def __add__(self, other):
		if isinstance(other, Car):
			return self.price + other.price
		elif other > 0:
			return self.price + other
		else:
			raise ValueError("Incorrect param")
		
toyota = Car("camry", 12345)
toyota.show_info()

bmw = Car("x5", 55000)
bmw.show_info()

# v1
result = toyota + bmw
# v2
# result = toyota.__add__(bmw)
print(result)

result = toyota + 123
print(result)

# дописать другие арифметические операторы 

# #####
# class Rational:
# 	def __init__(self, a=0, b=1):
# 		a = int(a)
# 		b = int(b)
# 		if b == 0:
# 			raise ValueError("Illegal value of the denominator!")
# 		self.__numerator = a
# 		self.__denominator = b
# 		self.__reduce()

# 	# сокращение дроби
# 	def __reduce(self):
# 		# функция для нахождения наибольшего общего делителя
# 		def gcd(a, b):
# 			if a == 0:
# 				return b
# 			elif b == 0:
# 				return a
# 			elif a >= b:
# 				return gcd(a % b, b)
# 			else:
# 				return gcd(a, b % a)
# 		sign = 1
# 		if (self.__numerator > 0 > self.__denominator) or \
# 				(self.__numerator < 0 < self.__denominator):
# 			sign = -1
# 		a, b = abs(self.__numerator), abs(self.__denominator) # abs - вернёт положительное число
# 		c = gcd(a, b)
# 		self.__numerator = sign * (a // c)
# 		self.__denominator = b // c

# 	# клонировать дробь
# 	def __clone(self):
# 		return Rational(self.__numerator, self.__denominator)
	
# 	@property
# 	def numerator(self):
# 		return self.__numerator
	
# 	@numerator.setter
# 	def numerator(self, value):
# 		self.__numerator = int(value)
# 		self.__reduce()

# 	@property
# 	def denominator(self):
# 		return self.__denominator
	
# 	@denominator.setter
# 	def denominator(self, value):
# 		value = int(value)
# 		if value == 0:
# 			raise ValueError("Illegal value of the denominator!")
# 		self.__denominator = value
# 		self.__reduce()

# 	# привести дробь к строке
# 	def __str__(self) -> str:
# 		return f"{self.__numerator} / {self.__denominator}"
	
# 	def __repr__(self) -> str:
# 		return self.__str__()
	
# 	# привести дробь к вещественному значению
# 	def __float__(self):
# 		if self.__denominator == 0:
# 			raise ZeroDivisionError()
# 		return self.__numerator / self.__denominator
	
# 	# привести дробь к логическому значению
# 	def __bool__(self):
# 		return self.__numerator != 0


# 	# сложение обыкновенных дробей
# 	def __iadd__(self, rhs): # +=
# 		if isinstance(rhs, Rational):
# 			a = self.numerator * rhs.denominator + \
# 				self.denominator * rhs.numerator
# 			b = self.denominator * rhs.denominator
# 			self.__numerator, self.__denominator = a, b
# 			self.__reduce()
# 			return self
# 		else:
# 			raise ValueError("Illegal type of the argument")
	
# 	# drob1 + drob2 ====> drob1 += drob2
		
# 	def __add__(self, rhs):
# 		return self.__clone().__iadd__(rhs)
	
# 	# вычитание обыкновенных дробей
# 	def __isub__(self, rhs): # -=
# 		if isinstance(rhs, Rational):
# 			a = self.numerator * rhs.denominator - \
# 				self.denominator * rhs.numerator
# 			b = self.denominator * rhs.denominator
# 			self.__numerator, self.__denominator = a, b
# 			self.__reduce()
# 			return self
# 		else:
# 			raise ValueError("Illegal type of the argument")
	
# 	def __sub__(self, rhs):
# 		return self.__clone().__isub__(rhs)
	
# 	# умножение обыкновенных дробей
# 	def __imul__(self, rhs): # *=
# 		if isinstance(rhs, Rational):
# 			a = self.numerator * rhs.denominator 
# 			b = self.denominator * rhs.denominator
# 			self.__numerator, self.__denominator = a, b
# 			self.__reduce()
# 			return self
# 		else:
# 			raise ValueError("Illegal type of the argument")
	
# 	def __mul__(self, rhs):
# 		return self.__clone().__imul__(rhs)
	
# 	# деление обыкновенных дробей
# 	def __itruediv__(self, rhs): # /=
# 		if isinstance(rhs, Rational):
# 			a = self.numerator * rhs.denominator 
# 			b = self.denominator * rhs.denominator
# 			self.__numerator, self.__denominator = a, b
# 			self.__reduce()
# 			return self
# 		else:
# 			raise ValueError("Illegal type of the argument")
	
# 	def __truediv__(self, rhs):
# 		return self.__clone().__itruediv__(rhs)
	
# 	# отношение обыкновенных дробей
# 	def __eq__(self, rhs): # ==
# 		if isinstance(rhs, Rational):
# 			return (self.numerator == rhs.numerator) and \
# 					(self.denominator == rhs.denominator)
# 		else:
# 			return False
		
# 	def __ne__(self, rhs): # !=
# 		if isinstance(rhs, Rational):
# 			return not self.__eq__(rhs)
# 		else:
# 			return False

# 	def __gt__ (self, rhs): # >
# 		if isinstance(rhs, Rational):
# 			return self.__float__() > rhs.__float__()
# 		else:
# 			return False

# 	def __lt__ (self, rhs): # <
# 		if isinstance(rhs, Rational):
# 			return self.__float__() < rhs.__float__()
# 		else:
# 			return False	
	
# 	def __ge__ (self, rhs): # >=
# 		if isinstance(rhs, Rational):
# 			return not self.__lt__(rhs)
# 		else:
# 			return False	
	
# 	def __le__ (self, rhs): # <=
# 		if isinstance(rhs, Rational):
# 			return not self.__gt__(rhs)
# 		else:
# 			return False	

# if __name__ == '__main__':
# 	r1 = Rational(3, 4)
# 	print(float(r1))
# 	print(r1)
# 	print(f"r1 = {r1}")
# 	r2 = Rational(5, 6)
# 	# r1 += r2
# 	print(r1)
# 	print(f"r2 = {r2}")
# 	print(f"{r1} + {r2} = {r1 + r2}")
# 	print(f"{r1} - {r2} = {r1 - r2}")
# 	print(f"{r1} * {r2} = {r1 * r2}")
# 	print(f"{r1} / {r2} = {r1 / r2}")
# 	print(f"{r1} == {r2} {r1 == r2}")
# 	print(f"{r1} != {r2} {r1 != r2}")
# 	print(f"{r1} > {r2} {r1 > r2}")
# 	print(f"{r1} < {r2} {r1 < r2}")
# 	print(f"{r1} >= {r2} {r1 >= r2}")
# 	print(f"{r1} <= {r2} {r1 <= r2}")

	##################################
	# Абстрактні методи

	# from abc import ABC, abstractmethod

	# абстрактний клас містить у собі абстрактні методи, тобто методи без реалізації помічені
	# декоратором @abstractmethod з модуля abc, а також методи з реалізацією(звичайні методи)
	# Оскільки абстрактний клас містить у собі абстрактні методи - всі дочірні класи мають
	# надати реалізації цих методів. Так само не можна створить екземпляр класу, у якого
	# хоча б один абстрактний метод.

	# Інтерфейс - це клас, у якого тільки абстрактні методи. Такий клас необхідний, якщо вам
	# потрібно створити якийсь контракт, зобов'язання надати реалізацію цих методів для 
	# інших класів спадкоємців.
# class Polygon(ABC):
# 	@abstractmethod # цей метод без реалізації і всі дочірні класи повинні надати
# 					#	  реалізацію цього методу
# 	def noofsides(self):
# 		pass

# 	def show_info(self):
# 		print(f"I`m from Polygon")

# class Triangle(Polygon):
# 	# overriding abstract method

# 	def noofsides(self):
# 		print(f"I have 3 sides")

# class Pentagon(Polygon):
# 	# overriding abstract method

# 	def noofsides(self):
# 		print(f"I have 5 sides")

# class Hexagon(Polygon):
# 	# overriding abstract method

# 	def noofsides(self):
# 		print(f"I have 6 sides")

# class Quadrilateral(Polygon):
# 	# overriding abstract method

# 	def noofsides(self):
# 		print(f"I have 4 sides")

# # TypeError: Can`t instantiate abstract class Polygon without an implementation for
# # 			abstract method 'noofsides'
# # test = Polygon()
# # test.noofsides()

# # Driver code
# R = Triangle()
# R.noofsides()

# K = Quadrilateral()
# K.noofsides()

# R = Pentagon()
# R.noofsides()

# K = Hexagon()
# K.noofsides()
# K.show_info()

# # Поліморфізм функцій
# print(len("Программист"))
# print(len(["Яблоко", "Банан", "Груша"]))
# print(len({"Имя": "Максим", "Address": "Киев"}))

# Поліморфізм класів
class Cat:
	def __init__(self, klichka, vozrast):
		self.klichka = klichka
		self.vozrast = vozrast

	def status(self):
		print(f"Я кішка. Мене звуть {self.klichka}. Мій вік {self.vozrast} років")

	def say(self):
		print("Мяу")

class Dog:
	def __init__(self, klichka, vozrast):
		self.klichka = klichka
		self.vozrast = vozrast

	def status(self):
		print(f"Я пес. Мене звуть {self.klichka}. Мій вік {self.vozrast} років")

	def say(self):
		print("Гав")

	def hello(self):
		print(f"Hello {self.klichka}")

class PetDog(Dog):
	def __init__(self, klichka, vozrast, owner):
		super().__init__(klichka, vozrast)
		self.owner = owner

	# перевизначення методу
	def hello(self):
		super().hello()
		print(f"Owner: {self.owner}")

test = PetDog("test", 1, "Vasya")
test.hello()

cat_obj = Cat("Муська", 18)
dog_obj = Dog("Барон", 12)

for pet in (cat_obj, dog_obj):
	pet.say()
	pet.status()
	pet.say()

#	# Поліморфізм та успадкування
from math import pi
from abc import ABC, abstractmethod

# інтерфейс
class BaseShape(ABC):
	@abstractmethod
	def area(self):
		pass

class Shape(BaseShape):
	def __init__(self, name):
		self.name = name

	# def area(self):
	# 	pass

	def info(self):
		return "Я двухмерная форма"
	
	def __str__(self):
		return "строковое представление объекта Shape"
	

class Square(Shape):
	def __init__(self, length):
		super().__init__("Квадрат")
		self.length = length

	def area(self):
		return self.length ** 2
	
class Circle(Shape):
	def __init__(self, radius):
		super().__init__("Круг")
		self.radius = radius

	def area(self):
		return pi * self.radius ** 2
	
class AreaCalculator:
	def __init__(self, geom_object) -> None:
		self.geom_object = geom_object

	def get_area(self):
		print(self.geom_object.area())

# my_shape = Shape("my_shape")
# print(my_shape)

kvadrat = Square(8)
krug = Circle(14)
# print(kvadrat)
# print(kvadrat.info())
# print(krug.info())
# print(kvadrat.area())

areaCalculator = AreaCalculator(kvadrat)
areaCalculator.get_area()
areaCalculator = AreaCalculator(krug)
areaCalculator.get_area()
print(Square.mro())
print(AreaCalculator.mro())

##########################################
# нужно загрузить библиотеку accessify
# from accessify import private, protected, implements

# class ICar:
# 	def show(self):
# 		pass

# 	def test(self):
# 		pass


# @implements(ICar)
# class Car:
# 	@private # доступ будет только внутри этого класса
# 	def show_secret(self):
# 		print("Secret token")

# 	@protected # доступ будет внутри этого класса и в дочерних
# 	def show_data_for_child_classes(self):
# 		print("Data for child classes")

# 	# доступ будет везде
# 	def show(self):
# 		print("Into from secret method")
# 		self.show_secret()
# 		print("Info from protected method")
# 		self.show_data_for_child_classes()

# 	def test(self):
# 		print("Test method")


# class SuperCar(Car):
# 	def show_parents_method(self):
# 		print("Info from secret method")
# 		self.show_secret()
# 		print("Info from protected method")
# 		self.show_data_for_child_classes()

# super_car = SuperCar()
# super_car.show_parents_method()
# super_car.show_data_for_child_classes()

# car1 = Car()
# car1.show()
# car1.test()
# car1.show_data_for_child_classes()
# car1.show_secret()

####
from controller import controller

def main():
	controller = Controller()
	controller.menu()

if __name__ == '__main__':
	main() 