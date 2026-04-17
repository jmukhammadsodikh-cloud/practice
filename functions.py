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
