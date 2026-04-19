''' OBJECTS
(1) What is object
(2) Iterable objects & Range
(3) DICTIONARY
(4) Error handling sysytem
'''

from math import ceil
import math  # package/module = bu objectlarni biz import qlib olishimz kerak..
import array  # package/module = chunki bular python bilan paralell keladi

print("=========What is object==============")
# An Object has state and method properties
# Everything is object in Python

print(type("Hello Marco"))
print(type(24))
print(type(True))  # bular
print(type(array))
print(type(math))

# Paradigm > Functional Programming & OOP
# OOP 4 CONCEPTS > Abstraction | Encapsulation | Polymorphism | Inheritance
result = math.ceil(32.9)  # CALL
print("result:", result)

# from package import ceil = aniq bir method chaqirmoqchi bolsak
result2 = ceil(33.9)
print("result2:", result2)
