#  A task Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi
# letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
# MASALAN countLetter("e", "engineer") 3ni return qiladi.


# // B Masalaning sharti va yechimi
# Shunday function tuzing, u 1ta string parametrga ega bolsin,
# hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
# MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.


# task C Shunday function tuzing, u 2ta string parametr ega bolsin,
# hamda agar har ikkala string bir hil harflardan iborat bolsa true aks holda false qaytarsin
# MASALAN checkContent("mitgroup", "gmtiprou") return qiladi true;
'''
def check_names(name1, name2):
    # Harflarni alifbo tartibida taxlab, keyin solishtiramiz
    return sorted(name1) == sorted(name2)


print(check_names("Alex", "Kevin"))
'''

# D-TASK (NodeJS)
# Shunday function tuzingki unga integerlardan iborat array pass bolsin va
# function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
# MASALAN: getHighestIndex([5, 21, 12, 21, 8]) return qiladi 1 sonini.


'''E-TASK (NodeJS)===================

Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni
teskari qilib return qilsin.
MASALAN: getReverse("hello") return qilsin "olleh"
'''


def get_reverse(name):
    x = ""
    for abc in name:
        x = abc + x
    return x


print(get_reverse("samigjonov"))
