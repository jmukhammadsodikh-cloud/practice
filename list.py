''' List
     (1) Working with lists
     (2) List methods
     (3) Lambda function
     (4) enumarate, map and filter
'''
print("========= Working with lists ============")
# Java/Php/NodeJS array => Python list

# literal
person = {"name": "Justin", "age": 25}  # dictionary
people = ("Andrew", "John", "Michael")  # tuple
groups = ["MIT", "FLEXY", "DEVEX", "MG"]  # list

for team in groups:
    print(f"the team: {team}")
# constructor
letters = list("HELLO WORLD")
print(f"the letters: {letters} and size: {len(letters)}")  # size

print("======")
fruits = ["apple", "orange", "lemon", "kiwi"]

a = fruits[0]
b = fruits[0:2]  # noldan ikkigacha = 2ni ozini olmaydi
c = fruits[::3]  # noldi ol keyin uchti ol
d = fruits[:: - 1]  # teskari


print("a", a)
print("b", b)
print("c", c)
print("d", d)


print("========= List methods ============")
# list methods => append(), insert(), pop(), remove(), clear(), sort(), index()

letters = ["a", "b", "d"]

letters.append("c")      # add value behind
print(f"the append letters: {letters}")

letters.insert(0, "z")   # add value front
print(f"the insert letters: {letters}")

size = len(letters) - 1
result1 = letters.pop(size)   # pop behind with len
print(f"the pop result1: {result1} and letters: {letters}")

result2 = letters.pop(0)    # pop front only with index
print(f"the pop result2: {result2} and letters: {letters}")

print("===========")

animals = ["dog", "cat", "capybara", "fish", "lion"]
print("animals:", animals)

animals.remove("lion")     # remove the value
print("animals remove:", animals)

del animals[2:4]  # delete values
print("animals delete:", animals)

exist = animals.index("cat")  # index qaysidur value bor yoqligini tekshirish
print("cat exist:", exist)

animals.clear()
print("animals clear:", animals)

if "cat" in animals:
    # error handling with => if else
    print("index of cat:", animals.index("cat"))
else:
    print("cat does not exist")

print("---------")
numbers = [123, 12, 3, 4, 77, 23, 23]
numbers.sort()  # sort default
print("sort default:", numbers)
numbers.sort(reverse=True)  # sort reverse
print("sort reverse:", numbers)

# immutable => sorted function, index() method
numbs = [23, 1, 34, 8, 0, 56]
new_numbs = sorted(numbs)
print(f"the sorted numbs {numbs} and new_numbs {new_numbs}")
