'''CLASS
(1) What is class
(2) Ordinary vs static properties
(3) Special methods / magic methods
'''
print("=======WHAT IS CLASS=============")
# class = blueprint for object creation!
# structure = state constructor method


class Person():
    # state
    message = "class state property"
    # constuctor = magic methods orqali hosil qilamiz

    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    # method
    def introduce(self):
        print(f"This man {self.name} says Hey how do you do!")

    def say_age(self):
        print(f"{self.name} says I am {self.age} !")

    def say_occupation(self):
        print(f"I am a {self.occupation}")

    @classmethod
    def explain(cls):
        print(f"static method property executed")


person1 = Person("MARCO", 22, "Web developer")
person2 = Person("SAM", 29, "Policeman")
person3 = Person("MBAPPE", 30, "Football player")

# ordinary state =  oddiy object bilan yashaydi
print("person1.name:", person1.name)

# ordinary method = oddiy object bilan yashaydi
person1.introduce()
person2.say_age()
person3.say_occupation()

print("=======Ordinary vs Static properties=============")
# Ordinary = oddiy object bilan yashaydi
# Static properties = Class bilan yashaydi

# static state = class bilan chaqiriladi
new_message = Person.message
print(f"new_message:", new_message)

# CLASS DECORATOR orqali static method hosil qilishimiz mumkun
# @classmethod
#  def explain(cls):
# print(f"static method property executed")
Person.explain()

print("=======Special methods / magic methods=============")
# Python's special most common special magic methods are below:
# __init__ __new__ __str__ __call__ __getitem__ __eq__ __item__ ....


class Car():
    # state
    descripion = 'This class makes cars'
    # constructor

    def __new__(cls, *args):
        print("*__new__*")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # method

    def start_engine(self):
        print(f"the {self.name} started engine!!")

    def stop_engine(self):
        print(f"the {self.name} stopped engine!!")

    def __str__(self):
        return f"{self.name} was produced in {self.year} year!"

    def __call__(self):
        print("Object called as function!")
        return True


my_car = Car("Ferrari", 2025)
my_car.start_engine()
my_car.stop_engine()
print("------")
your_car = Car("Toyota", 2023)
print(your_car)
response = your_car()  # Call as a function
print("response:", response)
