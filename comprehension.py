""" Comprehension
    (1) What is comprehension & list comprehension.
    (2) Set and dictionary comprehension
"""
print("===== What is comprehension & list comprehension ===========")
# Comprehension acts like spread operator !
# Python’da comprehension — bu qisqa va ixcham usulda yangi list
# (yoki boshqa kolleksiya) yaratish uchun ishlatiladi.
# Oddiy for loopni bitta qatorda yozish imkonini beradi.

# Umumiy qolip
""" Comprehension general syntax:
    a) *iterable
    b) <expression> for item in iterable
    c)  <expression> for item in iterable <condition> if
"""
# list (comp)
# a version => *iterable
numbers = [10, 2, 3, 4, 22, 8, 3, 23, 4]
list_numbers = [*numbers]

print("list_numbers:", list_numbers)
# yangi reference bilan yangi list qaytarayapti
print(numbers is list_numbers)
# ularni id malumot manzili har hil
print(id(numbers), id(list_numbers))

# b version => <expression> for item in iterable
print("---------")
people = [("Justin", 27), ("Marco", 21), ("Sam", 30)]
first_people = [person[0] for person in people]
print("first_people", first_people)

# c version =>  <expression> for item in iterable <condition> if
print("---------")
cars = [
    ("Ferrari", 78),
    ("Toyota", 87),
    ("Audi", 116),
    ("Bmw", 109),
    ("Pagani", 33)
]
first_cars = [moshina[1] for moshina in cars if moshina[1] > 80]
print("first_cars:", first_cars)
