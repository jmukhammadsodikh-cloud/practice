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


print("=========Error handling sysytem==============")
# Hatolikning oldini olish

car_obj = dict(name="FERRARI", year=2024, sport_car=True)
try:
    print(f"passed here")
    result = car_obj["sport_car"]
    print(f"result:", result)
    a = car_obj.speed()
except KeyError as err:
    print(f"No origin state property found", err)
except AttributeError as err:
    print(f"No spped method found", err)
else:
    print(f"Executed successfully without errors")

finally:
    print(f"Final closing logic")
