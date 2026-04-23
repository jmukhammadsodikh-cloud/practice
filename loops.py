'''Loop Operators
   (1) For
   (2) break / else
   (3) while
'''

print("=========for operator===========")
#  for = takrorlanish miqdori aniq bolganda ishlatamiz
# Iterable objects > string, dic, tuple, list, range, map, filter.
text = "MERCY"
numbs = [28, 2, 4, 90, 12]
car_obj = dict(name="TESLA", year=2024, model="S class")
range_obj = range(8)

print("------")
for letter in text:
    print(f"the letter: {letter}")

print("------")
for number in numbs:
    print(f"the number: {number}")

print("------")
for key in car_obj:
    print(f"the key: {key} => the value: {car_obj.get(key)}")

print("------")
for x in range_obj:
    print(f"the element: {x}")

print("------")  # range steps

print("========= brake / else ===========")
for x in range(1, 20, 5):
    print(f"the x: {x}")   # for operator ichida break else =
    if x > 100:
        print(f"Reached the break")
        break
else:
    print("Loopes successfully")


print("========= while ===========")
# while takrorlanish miqdorini bilmaymiz balki 5 10 qadam
numb = 50
while numb > 0:
    numb -= 10
    print(f"the number equals {numb}")

print("------")
count = 0
while True:
    count += 1
    x = int(input("Find number"))

    if x == 41:
        print(f"You found number in {count} steps")
        break
    else:
        print("Wrong please find again")
