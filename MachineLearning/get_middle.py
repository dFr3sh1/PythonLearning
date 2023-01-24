def get_middle(s):
    odd_or_even_string = int(len(s) / 2)
    if len(s) % 2 == 0:
        return s[(odd_or_even_string - 1)] + s[odd_or_even_string]  #s[odd_or_even_string and odd_or_even_string + 1]
    else:
        return s[odd_or_even_string: odd_or_even_string + 1]

print(get_middle("Holl"))

# def get_middle(s):
#     index, odd = divmod(len(s), 2)
#     return s[index] if odd else s[index - 1:index + 1]

# import math
# def get_middle(s):
#     #your code here
#     x = len(s)
#     y = int(x/2)
#     if x%2==0:
#         return s[y-1:y+1]
#     else:
#         return s[y:y+1]

# def get_middle(s):
#     i = (len(s) - 1) // 2
#     return s[i:-i] or s

# def get_middle(s):
#     while len(s) > 2:
#         s = s[1:-1]
#     return s

# def get_middle(s):
#     a = len(s)
#     if len(s) == 1:
#         return s
#     elif len(s) % 2 == 0:
#         return s[int(a/2) - 1] + s[int(a/2)]
#     else:
#         return s[int(a/2)]

# def get_middle(s):
#     return s[(len(s)-1)//2:len(s)//2+1]

# def get_middle(s):
#     x = int(len(s)/2)
#     return s[x] if len(s)%2!=0 else s[x-1:x+1]

# def get_middle(s):
#     return s[(len(s) - 1) // 2 : (len(s) + 2) // 2]