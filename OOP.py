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
class Person:
	__name = "no name"
	__age = 18

	def __init__(self, name, age):
		self.name = name # name setter
		self.age = age	# age setter
		self.__secret = 12345 # (private) -> доступ тільки всередині класу
		self._hobby = "no info"	# (protected) -> доступ всередині класу та в класах спадкоємцах
	
	@property
	def name(self):
		return self.__name
	
	@name.setter
	def name(self, name):
		if len(name) > 2:
			self.__name = name

	@property
	def age(self):
		return self.__age
	
	@age.setter
	def age(self, age):
		if age > 18:
			self.__age = age

	@property
	def hobby(self):
		return self._hobby
	
	def show_info(self):
		print(f"Name: {self.name}, Age: {self.age}")

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
class Transport:
	def __init__(self, name, year):
		self.name = name
		self.year = year

	def show_info(self):
		print(f"Name: {self.name}\nYear: {self.year}")


class BaseAuto(Transport):
	def __init__(self, name, year, wheels_count=0):
		super().__init__(name, year)
		self.wheels_count = wheels_count

	# перекриття метода базового класу
	def show_info(self):
		print(f"Wheels count: {self.wheels_count}")

class WaterTransport(Transport):
	def __init__(self, name, year, displacement=0.):
		super().__init__(name, year)
		self.displacement = displacement

	# перекриття метода базового класу
	def show_info(self):
		print(f"Displacement: {self.displacement}")


class Car(BaseAuto):
	def __init__(self, name, year, wheels_count, doors_count=0):
		super().__init__(name, year, wheels_count)
		self.doors_count = doors_count

	# перекриття метода базового класу
	def show_info(self):
		print(f"Doors count: {self.doors_count}")


class Amphibian(WaterTransport, BaseAuto):
	def __init__(self, name, year, wheels_count, displacement):
		WaterTransport.__init__(self, name, year, displacement)
		BaseAuto.__init__(self, name, year, wheels_count)

	# перекриття метода базового класу
	def show_info(self):
		Transport.show_info(self)
		WaterTransport.show_info(self)
		BaseAuto.show_info(self)


test_car = Amphibian("BMW", 2024, 4, 123.6)
test_car.show_info()
print(Amphibian.mro())
