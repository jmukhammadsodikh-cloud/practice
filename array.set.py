""" Array & Set
    (1) Array
    (2) Set
    (3) Specific operators with set
"""
# Array juda katta sonlar bilan ishlasak oddiy hollarda list tavsiya qilinar ekan
from array import array
numbers = array("i", [1, 4, 5, 7, 8, 41])
print("numbers(1):", numbers)

numbers.append(100)  # behind
numbers.insert(0, 14)  # front
print("numbers(2):", numbers)

numbers.remove(5)
numbers.pop()
print("numbers(3):", numbers)

del numbers[0:2]
print("numbers(4):", numbers)

print("========== Set ==========")
# {set} of unique collection without keeping order !
# qaytarilmaydigan unique toplam
new_numbers = array("i", [1, 4, 7, 5, 4, 7, 8, 9, 9])
numbs_set = set(new_numbers)

print("numbs_set:", numbs_set)

numbs_set.add(200)
print("numbs_set(1)", numbs_set)

numbs_set.add(7)
print("numbs_set(2)", numbs_set)


print("========== Specific operators with set ==========")
# | & - ^
a = {10, 20, 50}
b = {20, 40}

result1 = a | b     # union => bu ikkala toplamni bitta set qlib beradi
result2 = a & b    # intersection => ikkita setda bir hil bolgan toplamni beradi
result3 = a - b   # difference => ikkita setni ayrib beradi
result4 = a ^ b  # symetric difference => ikkita setda bir hil bolmagan toplamni beradigi

print("result1:", result1)
print("result2:", result2)
print("result3:", result3)
print("result4:", result4)
