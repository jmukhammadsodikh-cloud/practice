print("===number===")
# in JAVA: variable is name of storage location
# in PYTHON: variable is named reference

count = 500
count_type = type(count)
print("count:", count, count_type)

# qulayroq print qilishni hohlasak format print
print(f"the count: {count} and type: {count_type}")

# qoida: pythonda primitive variable ham object
result1 = count.bit_count()  # method
result2 = count.numerator    # state
print(result1, result2)


print("===string===")
# methods: upper() lower() title() find() replace()
course = "MIT Ai Python Foundation"
result = type(course)
print(f"the type of course (1): {result}")
result = course.title()
print(f"the course title (2): {result}")

result = course.upper()
print(f"the course name with uppercase (3): {result}")

# Bu yerda result ozgaruvchisiga yangi qiymat yuklanyapti
result = course.replace("Foundation", "Master class by Martin")
print(f"the replaced name: (4) {result}")

print(course)  # avvalgi qiymatiga bu methodlar tasir korsatmaydi

# Agar avvalgi qiymatini ozgartirmoqchi bolsak:
course = course.replace("Foundation", "Master class by Martin")
# Bu yerda endi 'result' emas, yangilangan 'course' ni chiqarish mantiqan togri boladi
print(f"the updated course: (5) {course}")


print("===boolean===")
# functions > type() input() bool() int() str()
y = input("Give your value for y:")
print("y:", y)

result = y.isnumeric()
print(f"the input value is numeric: {result}")

# TRUTHY vs FALSY values
# TRUTHY > true 100 -100 "MIT"
# FAlSY > false 0 "" None
test_falsy = "" or False or 0 or None or 100
print("The test_falsy:", bool(test_falsy))
# falsy qiymatlar ichida bitta true bolsa falsy = truega aylanadi

test_truthy = "MIT"
print("The test_truthy:", bool(test_truthy))
