def is_isogram(string):
    string.lower()
    isogram = set()
    for char in string.lower():
        if char in isogram:
            return False    
        else:
            isogram.add(char)
    return True
        
print(is_isogram("DOom"))

# def is_isogram(string):
#  # return len(string) == len(set(string.lower()))

# def is_isogram(string):
#     string = string.lower()
#     for letter in string:
#         if string.count(letter) > 1: return False
#     return True

# def is_isogram(string): 
#     return len(set(string.lower())) == len(string)

# def is_isogram(string):
#     #your code here
#     char_dict = {}
#     string = string.lower()
    
#     for char in string:
#         if char in char_dict:
#             # increment count of this character
#             char_dict[char] = char_dict[char] + 1
#         else:
#             char_dict[char] = 1
    
#     # loop over the characters in dictionary, if any have
#     # more than 1 found, this string is not an isogram, so break
#     # the loop and function and return False.
#     for key in char_dict:
#         if char_dict[key] > 1:
#             return False
            
#     # If no duplicates were found in the loop directly above,
#     # this must be an isogram, so return true!
#     return True

# def is_isogram(string):
#     s = set(string.lower()) 
#     if len(s) == len(string): 
#         return True
#     return False

# is_isogram = lambda s: len(set(s.lower())) == len(s)

# def is_isogram(string):
#     string = string.lower()
#     return len(string) == len(set(string))

# def is_isogram(string):
#     return len(set(list(string.lower()))) == len(string)

# from collections import Counter

# def is_isogram(string):
#     for x in Counter(string.lower()).values():
#         if x > 1:
#             return False
#     return True

