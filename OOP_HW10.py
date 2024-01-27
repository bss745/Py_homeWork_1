# Завдання 1:

# Створіть клас "Місто". 
# Необхідно зберігати в полях класу: назву міста, назву регіону, назву країни,
# кількість жителів міста, поштовий індекс міста, телефонний код міста.
# Реалізуйте доступ до окремих полів (Інкапсуляція).
print("=====Ex. 1=====")

class City:
	__name = "no name"
	__region = "no info"
	__country = "Ukraine"
	__population = 1000
	__postal_code = 00000
	__phone_code = +380
    
	def __init__(self, name, region, country, population: int, postal_code: int, phone_code):
		self.__name = name  				# Назва міста
		self.__region = region  			# Назва регіону
		self.__country = country  			# Назва країни
		self.__population = population  	# Кількість жителів міста
		self.__postal_code = postal_code	# Поштовий індекс міста
		self.__phone_code = phone_code		# Телефонний код міста


	@property
	def name(self):
		return self.__name
    
	@name.setter
	def name(self, new_name):
		self.__name = new_name

	
	@property
	def region(self):
		return self.__region

	@region.setter
	def region(self, new_region):
		self.__region = new_region


	@property
	def country(self):
		return self.__country

	@country.setter
	def country(self, new_country):
		self.__country = new_country


	@property 
	def population(self):
		return self.__population

	@population.setter
	def population(self, new_population):
		self.__population = new_population


	@property
	def postal_code(self):
		return self.__postal_code

	@postal_code.setter
	def postal_code(self, new_postal_code):
		self.__postal_code = new_postal_code


	@property
	def phone_code(self):
		return self.__phone_code
	
	@phone_code.setter
	def phone_code(self, new_phone_code):
		self.__phone_code = new_phone_code

    
city = City("Київ", "Київський", "Україна", 2800000, "03000", "+380")
    
print("Назва міста:", city.name)
print("Назва регіону:", city.region)
print("Назва країни:", city.country)
print("Кількість жителів міста:", city.population)
print("Поштовий індекс міста:", city.postal_code)
print("Телефонний код міста:", city.phone_code)


city.population = 3000000
city.postal_code = "03100"
    
    # Виведення змінених значень
print("\nПісля змін:")
print("Кількість жителів міста:", city.population)
print("Поштовий індекс міста:", city.postal_code)

# Завдання 2:

# Створіть клас "Країна".
# Необхідно зберігати в полях класу: назву країни, назву континенту,
# кількість жителів країни, телефонний код країни, назву столиці, назву міст країни.
# Реалізуйте доступ до окремих полів (Інкапсуляція).
print("=====Ex. 2=====")

class Country:
	__name = "no name"
	__continent = "no info"
	__population = 1000
	__phone_code = "no info"
	__capital = "no info"
	__cities = "no info"
   
	
	def __init__(self, name, continent, population, phone_code, capital, cities):
		self.__name = name  			# Назва країни
		self.__continent = continent  	# Назва континенту
		self.__population = population  # Кількість жителів країни
		self.__phone_code = phone_code  # Телефонний код країни
		self.__capital = capital  		# Назва столиці
		self.__cities = cities  		# Список назв міст країни

    # Методи доступу до полів (гетери)
	@property
	def name(self):
		return self.__name

	@name.setter
	def set_name(self, new_name):
		self.__name = new_name

	
	@property
	def continent(self):
		return self.__continent

	@continent.setter
	def continent(self, new_continent):
		self.__continent = new_continent

	
	@property
	def population(self):
		return self.__population

	@population.setter
	def population(self, new_population):
		self.__population = new_population

	
	@property
	def phone_code(self):
		return self.__phone_code

	@phone_code.setter
	def phone_code(self, new_phone_code):
		self.__phone_code = new_phone_code

	
	@property
	def capital(self):
		return self.__capital

	@capital.setter
	def capital(self, new_capital):
		self.__capital = new_capital

	
	@property
	def cities(self):
		return self.__cities

	@cities.setter
	def cities(self, new_cities):
		self.__cities = new_cities
# Приклад використання класу
country_cities = ["Київ", "Львів", "Одеса"]  # Приклад списку міст країни
country = Country("Україна", "Європа", 44000000, "+380", "Київ", country_cities)
    
    # Використання гетерів
print("Назва країни:", country.name)
print("Назва континенту:", country.continent)
print("Кількість жителів країни:", country.population)
print("Телефонний код країни:", country.phone_code)
print("Назва столиці:", country.capital)
print("Назви міст країни:", country.cities)

    # Використання сетерів
country.population = 45000000
country.phone_code = "+38044"
    
    # Виведення змінених значень
print("\nПісля змін:")
print("Кількість жителів країни:", country.population)
print("Телефонний код країни:", country.phone_code)