# Завдання 1:

# Створити ієрархію класів для опису академії.
# Зразковий список класів: Person, Teacher, Student, Subject, Academy і т.д.
# Продумати архітектуру: реалізувати принципи ООП
print("=====Ex. 1=====")

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")


class Teacher(Person):
    def __init__(self, name, age, gender, subject):
        super().__init__(name, age, gender)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}")


class Student(Person):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        if age <= 16:
            raise ValueError("Invalid age for a student.")
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying with ID: {self.student_id}")


class Subject:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Subject: {self.name}")


class Academy:
    __name = "My Academy"
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
        self.subjects = []
        

	
	# @property
	# def name(self):
	# 	return self.__name
        
	# @name.setter
	# def name(self, name):
	# 	if len(name) > 2:
	# 		self.__name = name

    def add_teacher(self, teacher):
        if isinstance(teacher, Teacher):
            self.teachers.append(teacher)
        else:
            print("Invalid teacher object.")

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            print("Invalid student object.")

    def add_subject(self, subject):
        if isinstance(subject, Subject):
            self.subjects.append(subject)
        else:
            print("Invalid subject object.")

    def display_info(self):
        print(f"Academy: {self.name}")
        print("Teachers:")
        for teacher in self.teachers:
            teacher.display_info()
        print("Students:")
        for student in self.students:
            student.display_info()
        print("Subjects:")
        for subject in self.subjects:
            subject.display_info()


math_teacher = Teacher("John Doe", 35, "Male", "Mathematics")
physics_teacher = Teacher("Jane Smith", 40, "Female", "Physics")

student1 = Student("Alice Johnson", 20, "Female", "S001")
student2 = Student("Bob Davis", 22, "Male", "S002")

math_subject = Subject("Mathematics")
physics_subject = Subject("Physics")

academy = Academy("Awesome Academy")
academy.add_teacher(math_teacher)
academy.add_teacher(physics_teacher)
academy.add_student(student1)
academy.add_student(student2)
academy.add_subject(math_subject)
academy.add_subject(physics_subject)

academy.display_info()