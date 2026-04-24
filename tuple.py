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

# LIST = ozgartirish mumkun qiymatin
fruits = ["apple", "banana", "kiwi", "apricot"]
print("before list", fruits)
fruits[2] = "lemon"
print("after list", fruits)

# Malumotlar ozgarishin oldini olish uchun TUPLE ishlatamiz
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

# args > tuple = qachonki argumentlarimiz soni noaniq bolsa bitta qlib ovolamiz


def calculate(*args):
    print("args >", args)
    total = 1
    for x in args:
        total += x
    print(f"the total value: {total}")
    return total


calculate(10, 20)
