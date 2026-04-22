'''CLASS deep diving
   (1) Encapsulation
   (2) Inheritance
   (3) Polymorphism
'''

# kapsulaga orab qoyish malumotlarni himoya qlish
print("========Encapsulation============")
# Encapsulation > public __private  _protected


class Accaunt():

    description = "Thi class makes different bank accaunts"

    def __init__(self, owner, amount):
        self.__owner = owner  # private qildik suniy ozgartirib bomaydi tashqaridan
        self.__amount = amount

    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("deposit:", amount)      # deposit amountga kopaytirsin
        self.__amount += amount

    def withdraw(self, amount):        # withdraw qlib pul ayrisin
        print("withdraw:", amount)
        self.__amount -= amount

    @property
    def holder(self):            # getter orqali private malumot tashqaridan qabul qilish
        return self.__owner

    @holder.setter
    def holder(self, new_owner):
        print("holder.setter:", new_owner)
        self.__owner = new_owner

    def change_ownership(self, new_owner):
        # shu holatta ishlatib kelayotkan edik lekin bizni getterimizni setteri bor
        print("change ownership:", new_owner)
        self.__owner = new_owner


my_account = Accaunt("MARCO", 2000)  # object hosil qlib test qlamiz
my_account.get_balance()
print("----------")
my_account.deposit(1000)
my_account.withdraw(500)
my_account.get_balance()

print("------")  # tashqaridan suniy ravishda ozgartirdik marco millioner bank bankrot
my_account.owner = "JECk"
# my_account.amount = 150000
my_account.get_balance()

# private qilgandan keyin hatto isminiham kora olmaymiz
# print(my_account.__owner)

# endi hatolikni ushaymiz
print("------")
try:
    result = my_account.__amount      # tashqi olamga himoya private bilan
    print("result:", result)
except Exception as err:
    print("No amount state found", err)

# owner qiymatni qabul qlishni hohlasak DECORATOR property foydalanamiz
# method emas state boladi shu singari ishlatamiz

account_owner = my_account.holder
# endi ownerni getter orqali qabul qilayapmiz
print(f"account_owner:", account_owner)

print("owner before:", my_account.holder)  # state
# my_account.change_ownership("MARTIN")
print("owner after:", my_account.holder)

# setter orqali juda qulay
my_account.holder = "JOHN"  # bu state method emas () yoq
print("owner after:", my_account.holder)
