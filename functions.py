""" FUNCTIONS
   (1) Define vs Call
   (2) Parametr vs Argument
   (3) Keyword vs default arguments
   (4) Scope 
"""
print("=======Define(parametr) vs Call(argument)=========")
# build in function > print() type()
# function - reusable block of code !
# Instead of block {} in Java, Python uses indentation :,

# Define - build qlish Parametr ham shu yerda


def greet(a):
    print(f"How do you do, {a}")  # Void qiymat qaytarmidi orniga NONE


def greeting(b):
    print("greeting is executed")  # Return qiymat qaytaradi
    return f"Hi {b}"


# Call - execute chaqirish Argument ham shu yerda
result1 = greet("MARCO")
print("result1:", result1)

result2 = greeting("MARTIN")
print("result2:", result2)

print("=======Keyword vs default arguments=========")
# Define


def give_greet(name, age):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!"


# Call
# Keyword argument shu kodimizni tiniqroq qlish uchun
result3 = give_greet(name="Justin", age=28)
print("result3:", result3)


def give_greet2(name, age=29):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!"


# Default argumentin parametrda berib ketamiz default holatida
result3 = give_greet2(name="Justin")
print("result3:", result3)


print("======= Scope=========")

b = 40  # 3
# Define


def calculate(a):  # 2
    c = a + b  # 1
    print(f"c value:", {c})


# Call
calculate(90)
