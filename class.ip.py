print("==============INHERITANCE=================")
# Inheritance bu meros olish
# Parent ota class ozini child classiga meros berishi Polymorphism

# () qavisni qoymasak ham Python buni bor deb oylar ekan


class Animal:  # Parent
    # static state = malumot berish uchun
    description = "The class is parent for animals"

    # constructor = special method orqali __init__
    def __init__(self, voice):
        self.voice = voice

    # method
    def make_voice(self):
        # voice qiymati bollean boladi shunga reja qildik
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):  # Child class  javascriptda bu yerda extend bolar edi
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        # bu yerda ota talab etkan qiymatni jonatamiz
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound} - {self.sound}")

    def protect(self):
        print(f"Yes i can protect you")


class Cat(Animal):  # Child class  javascriptda bu yerda extend bolar edi
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        # bu yerda ota talab etkan qiymatni jonatamiz
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound} - {self.sound}")

    def play(self):
        pass


class Fish(Animal):  # Child class  javascriptda bu yerda extend bolar edi
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        # bu yerda ota talab etkan qiymatni jonatamiz
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound} - {self.sound}")

    def swim(self):
        print(f"Yes i can swim!")

# har uchchali classimizda ishlaydigan method talab etilsa shuni biz har biriga bermasdan parent qlasda berib ketsak child classda yozmasdan ishlatishimz mumkun ekan


dog = Dog("Rex", "woof", True)
cat = Cat("Tom", "myow", True)
fish = Dog("Nemo", "zzzz", False)
dog.introduce()
cat.introduce()
fish.introduce()
# introduceni har birida yozib chiqtik kop vaht oladi noqulay
# lekin bizda parent classda (make_voice) degan method bor ekan biz uni har bir child classda ishlatishimiz mumkun ekan shu Inheritance deb aytsak bolar ekan
dog.make_voice()
fish.make_voice()
# make_voiceni biz bitta qlib parent classda berib kettik lekin hammasida ishlayapti child classda
# Inheritance juda qulay umumiy hislat state methodlarni parent classda bitta qlib berib ketib child classda ishlatishimz mumkun ekan

print("-----")
print(Animal.description)
print(Dog.description)
# bu yerda parent classdagi static state yoki methodlarni ham bemalol ozidan uning farzandiga beishimiz mumkun ekan

# !! Muhum hamda parent otasiga public hamda protected propertilarini path qila olar ekan

print("==============POLYMORPHISM=================")
# Bir methodning bir necha shakliga ega bolishi bir narsani kop turiga ega bolishi


class Animal:  # Parent
    description = "The class is parent for animals"

    def __init__(self, voice):
        self.voice = voice

    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound} - {self.sound}")

    def protect(self):
        print(f"Yes i can protect you")

    def make_voice(self):
        print(f"the {self.name} says {self.voice}")


# bu make voice methodi parent classda va buni child classlar qabul qilayapt bu tabiy
dog.make_voice()
fish.make_voice()
# lekin shu make voice child classdaham bolsachi qaysi ishga tushadi
# Animal make voice or child make voice = JAVOB Dogning ichidagi  make voice ishga tushadi

# Demak Polymorphism degani bir hil methodimizni turli hil shakillari bolishi mumkun ekan parent hamda child classlarda
