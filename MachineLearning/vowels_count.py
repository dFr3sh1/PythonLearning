def get_count(sentence):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for char in sentence:
        if char in vowels and char != "y":
            count += 1
    return count

get_count("hello")
print(get_count("hello"))

# def getCount(inputStr):
#     return sum(1 for let in inputStr if let in "aeiouAEIOU")

# def getCount(s):
#     return sum(c in 'aeiou' for c in s)

# def getCount(inputStr):
#     num_vowels = 0
#     for char in inputStr:
#         if char in "aeiouAEIOU":
#            num_vowels = num_vowels + 1
#     return num_vowels

# import re
# def getCount(str):
#     return len(re.findall('[aeiou]', str, re.IGNORECASE))

# def getCount(inputStr):
#     return sum(inputStr.count(char) for char in ['a', 'e', 'i', 'o', 'u'])

# def getCount(inputStr):
#     return len([x for x in inputStr if x in 'aeoiu'])

# def getCount(inputStr):
#     num_vowels = 0
#     # your code here
#     for i in inputStr:
#         if i in ['a', 'e', 'i', 'o', 'u']:
#             num_vowels += 1
#         else:
#             pass
#     return num_vowels

# def getCount(string):
#     return sum([i in list('euioa') for i in string])

# def getCount(inputStr):
#     list_vowels = ['a', 'e', 'i', 'o', 'u']
#     return sum([inputStr.count(vowel) for vowel in list_vowels])

# getCount = lambda s: sum(s.count(i) for i in 'aeiou')

