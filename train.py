'''I-TASK (PYTHON)
Shunday function tuzing, unga string argument pass bolsin. Function ushbu agrumentdagi
digitlarni yangi stringda return qilsin
MASALAN: get_digits("m14i1t") return qiladi "141"
'''


def get_digits(word):
    d = ""
    for x in word:
        if x.isdigit():
            d = d + x
    return d


print(get_digits("m1asha3qqa7t"))

'''G-TASK (PYTHON)
Shunday function tuzingki unga integerlardan iborat array pass bolsin va function
bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini.



def get_highest_index(numbers):
    max_number = numbers[0]
    max_index = 0

    for a, b in enumerate(numbers):
        if b > max_number:
            max_number = b  # endi eng katta son 22 bo‘ldi
            max_index = a    # bu sonning indexini saqladik

    return max_index


print(get_highest_index([10, 3, 9, 22, 12, 51, 2, 44]))
'''
