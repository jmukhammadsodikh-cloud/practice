''' Packages & Debugging
    (1) python packages & core packages
    (2) package maneger & external package
    (3) debugging
'''

import turtle
print("======== python packages & core packages ============")
''' Python packages/modules: core, file and external '''
# core packages => python documentation > https://docs.python.org/3/library
# python bilan birga keladigon package turtle

# ichki core packages python
t = turtle.Turtle()
t.shape("turtle")  # cursor
t.speed(8)  # teslik
t.circle(150)

# turtle.done()
# we can also draw pizza via turtle module

print("---------------")
# import qilmasdan qabul qilish python bilan birga keladi
# opendan => syntax orqali turli tuman malumot oqishimiz mumkun
my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print("content:", content)
finally:
    my_file.close()

# with Contex manager => ishni yengillashtirib beradi
with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your:content:", your_content)

print("Done")
# Avtomatik ravishda close qladi
