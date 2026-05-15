def get_length(name):
    result = len(name)
    return result


print(get_length("marco"))


def get_first(name):
    result = name[0]
    return result


print(get_first("jeck"))


def get_last(name):
    result = name[-1]
    return result


print(get_last("dany"))


def reverse_word(word):
    a = word[::-1]
    return a


print(reverse_word("hello"))


def is_palindrome(word):
    a = word
    b = word[::-1]
    return a == b


print(is_palindrome("dad"))

print("============= har kuni 5ta task ==========")


def count_letter(word, letter):
    count = 0
    for x in word:
        if x == letter:
            count += 1

    return count


print(count_letter("banana", "a"))


def count_vowels(expression):
    count = 0
    a = "aeiou"
    for x in expression:
        if x in a:
            count += 1
    return count


print(count_vowels("hello"))


def find_longest(sentance):
    longest = ""
    for x in sentance.split():
        if len(x) > len(longest):
            longest = x
    return longest


print(find_longest("I love Uzbekistan"))
