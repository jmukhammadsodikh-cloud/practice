print("=========Iterable objects & Range==============")
# TAKRORLANISH xususiyatiga ega objectlar
# Iterable objects > string, dic, tuple, list, range, map, filter.

text_message = "Good morning"  # eng soddasi string
for letter in text_message:
    print(f"the letter: {text_message}")

name = "MARCO"
for letter in name:
    print(f"the name letter: {letter}")
 # range
range_obj = range(5)
print(f"range_obj:{range_obj}")

for ele in range_obj:
    print("the element:", {ele})


print("=========DICTIONARY==============")
# DICTIONARY is JSON object deb ataladi chunki json formatda hosil qlamiz
# maxsus objectlar yasamoqchi bolsak DICTIONARY foydalanamz

# Simple method or with Dict() function
person = {"name": "MARCO", "age": "21", "single": True}
person_obj = dict(name="MARCO", age=21, single=True)
print(f"person {person}")
print(f"person_obj {person_obj}")

name = person_obj["name"]  # obj ichidagi key olish
print("name:", name)

# name2 = person_obj["occupation"] # yoq keyni olish ERROR berad
# print("name2:", name2)

# ERROR oldini olish NONE boladi =  method get() bilan
name2 = person_obj.get("name")
name3 = person_obj.get("occupation")
balance = person_obj.get("balance", 0)  # NONE orniga default 0 qiymat
print(f"the name:{name2} the occupation {name3} and the balance {balance}")

# DIC iterable object
del person_obj["single"]  # delete
for key in person_obj:  # iterate
    print(f"the key {key}")
