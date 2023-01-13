def square_digits(num):
    new_digits_pow = ""
    for dig in str(num):
        new_digits_pow += str(int(dig) ** 2)
    return int(new_digits_pow)

print(square_digits(89))

# def square_digits(num):
#     ret = ""
#     for x in str(num):
#         ret += str(int(x)**2)
#     return int(ret)

# def square_digits(num):
#     return int(''.join(str(int(d)**2) for d in str(num)))

# def square_digits(num):
#     num = str(num)
#     ans = ''
#     for i in num:
#         ans += str(int(i)**2)
#     return int(ans)

# def square_digits(num):
#     return int(''.join(str(int(c)**2) for c in str(num)))

# def square_digits(num):
#     squares = ''
#     for x in str(num):
#         squares += str(int(x) ** 2)
#     return int(squares)

# def square_digits(num):
#     # s converts num to a str so we can index through it
#     # when then loop through the len of the str 
#     # while we're looping the string we convert it back to a int and square it
#     # after we add it to a str to keep it from adding and then convert it to a int
#     s = str(num)
#     t = len(s)
#     y=0
#     g= 0
#     b=""
#     while y < t:
#         g = int(s[y])**2 
#         b= b+ str(g) 
#         final = int(b)
#         y=y+1
#     return(final)   
#     pass

# def square_digits(num):
#     result = 0
#     multiplier = 1
#     while num:
#         digit = num % 10
#         result += digit ** 2 * multiplier
#         multiplier *= (10, 100)[digit > 3]
#         num //= 10
                                        
#     return result