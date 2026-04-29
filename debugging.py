''' Packages & Debugging
    (1) python packages & core packages
    (2) package maneger & external package
    (3) debugging
'''

from PIL import Image
import turtle
print("======== python packages & core packages ============")
''' Python packages/modules: core, file and external '''
# core packages => python documentation > https://docs.python.org/3/library
# python bilan birga keladigon core package => turtle

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

print("======== package maneger & external package ============")
# python bilan birga kelmaydigan packagelar royhati => External packages > https://pypi.org/
# image bilan ishlashga pillow package
# package manager pip => bu python bilan keladigon manager bu orqali external package ornatamiz
# package manager => pip pipenv npm yarn composer brew

# working with images => pillow
with Image.open("material/logo.png") as img_obj:
    resized_img = img_obj.resize((200, 200))
    resized_img.show()
    resized_img.save("material/sample.png")
