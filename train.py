#  A task Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi
# letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
# MASALAN countLetter("e", "engineer") 3ni return qiladi.

def count_letter(letter, word):
    count = 0
    for x in word:
        if x == letter:
            count += 1
    return count


print(count_letter("a", "assalomu aleykum aka"))


# // B Masalaning sharti va yechimi
# Shunday function tuzing, u 1ta string parametrga ega bolsin,
# hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
# MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.

def count_digits(number):
    count = 0
    for i in number:
        if i >= "0" and i <= "9":
            count += 1
    return count


print(count_digits("I was born in 2005 and 10th october"))


# task C Shunday function tuzing, u 2ta string parametr ega bolsin,
# hamda agar har ikkala string bir hil harflardan iborat bolsa true aks holda false qaytarsin
# MASALAN checkContent("mitgroup", "gmtiprou") return qiladi true;
print("----")


def checkContent(word, defenation):
    if len(word) == len(defenation):
        return True
    else:
        return False


print(checkContent("mashaqqat", "mit"))


# D-TASK (NodeJS)

# Shunday function tuzingki unga integerlardan iborat array pass bolsin va
# function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
# MASALAN: getHighestIndex([5, 21, 12, 21, 8]) return qiladi 1 sonini.
