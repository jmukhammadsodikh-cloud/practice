''' OPERATORS & CONDITIONS
    (1) OPERATORS
    (2) CONDITION
    (3) LOGICAL OPERATORS
'''
print("=========OPERATORS=========")
# + - > >= < <=  == * /   // % += -=  **

# sodda amallar
a = 20
b = 5
print("a > b", a > b)
print("a * b", a * b)
print("a / b", a / b)

print("======")  # toliq boluv va qoldiq // %
c = 20
d = 5
result = c // d
left = c % d
print(f"the result{result} and left: {left}")

print("======")  # shortcut  +=

# c = c + 100
c += 100
print("c:", c)

print("b*b2", b**2)  # b kvadrati
print("b*b*b3", b**3)  # b kubi ozini uch martda kopaytiramiz

# Python bizga bergan erkinligii...
print("======")  # hatto stringniham oziga kopaytirsa boladi pythonda
print("=" * 5)

print("======")  # ikkita variable solishtiruv ==
h = dict(name="Jack", age=20)
v = dict(name="John", age=20)  # faqat qiymat solishtiradi only value
print("c==d", h == v)

print(id(v), id(h))  # hotiradagi joylashuvi

print("======")  # ikkita variable  reference solishtiruv is
data = c is d
m = c

print("c is d", data)  # reference solishtiradi malumot manzilini
print("c is m", c is m)


print("=========CONDITION=========")
x = 45  # truthy hamda falsy qaytaradi
if x > 50:
    print("case A:")
elif x > 100:
    print("case B")
else:
    print("case C")


print("=========LOGICAL OPERATORS=========")
# Mantiqiy operatorlar hosil qilsak ham bolar ekan
print("-----")
age = 16
person = None
if age > 18:
    print("adult")
else:
    print("child")
# bu mantiqni yanada soddaroq varianti bor Logical operator orqali (ternary operator)
# Ternary = qisqa satir bilan kop ishlatiladi
age1 = 20
person_1 = "adult" if age > 18 else "minor"
print("person1:", person_1)

print("------")
is_student = True
is_admin = True
is_parent = True
is_guest = False

if not is_student:
    print("welcome here, do you want to be student")
elif is_admin:
    print("Please go to this office")
elif is_guest and is_parent:
    print("waiting room is over there")
else:
    print("Other cases")
