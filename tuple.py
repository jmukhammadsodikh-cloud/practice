""" Tuple
    (1) What is tuple
    (2) Unpacking arguments
    (3) Zip
"""
print("=========================================== What is tuple ================================================")
# Java/PHP/NodeJS array => Pythonda esa array = list

# literal
numbs = [13, 23, 13, 4, 6]
car_dic = {"brand": "Ferrari", "year": 1995}


# constructor
letters = list("Hello world")
person_dic = dict(name="Martin", age=32)

# LIST = ozgartirish mumkun qiymatin============
fruits = ["apple", "banana", "kiwi", "apricot"]
print("before list", fruits)
fruits[2] = "lemon"
print("after list", fruits)

# Malumotlar ozgarishin oldini olish uchun TUPLE ishlatamiz======================
# Tuple ichida joylashgan qiymatlarni umuman ozgartirib bolmaydi
animals = ("monkey", "cat", "dog", "elephant")
# tuple = string bollean null number hosil qilaoladi
tuple_obj = ("MARCO", 23, True, None)

print(animals[1])
# animals[1] = "pig"   # we cannot mutate tuple

print("=========================================== Unpacking arguments ================================================")
# argumentlarni yoyish = Tuple bilan
groups = ("MIT", "DEVEX", "FLEXY", "MG")
(a, b, *c) = groups
print(f"the:a {a} and the d: {c}")
# Qoida = () qavis qoyish kerak

# argument yoyish==================


# *args > tuple = qachonki argumentlarimiz soni noaniq bolsa bitta qlib ovolamiz argsga wrap qib qoyamiz


def calculate(*args):
    print("args >", args)
    total = 1
    for x in args:
        total += x
    print(f"the total value: {total}")
    return total


calculate(10, 20)

# **kwargs > dictionary==============


def introduce(**kwargs):
    print(
        f"Hi I am {kwargs["name"]} and I am {kwargs["age"]} and come from {kwargs["nation"]}")


introduce(name="Henry", age=32, nation="Korea")
introduce(name="Marco", age=22, nation="Uzbek")

# *args / **kwargs bir vahtda ==========


def greet(*args, **kwargs):
    print("*args>", args)
    print("**kwargs>", kwargs)


greet("hi", True, 23, name="John", age=22,)


print("=========================================== Zip ================================================")
# zip maxsus object 2ta tuple birlashtirib beradi
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ("a", "b", "c", "d")

zipped = zip(tuple1, tuple2)
print(zipped)
result = list(zipped)
print(result)
