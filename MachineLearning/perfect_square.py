import math

def is_square(n):
    if n < 0:
        return False
    elif n == 0 and n == 1:
        return True
    else:
        perfect_square = math.isqrt(n)
        return perfect_square ** 2 == n
    
print(is_square(25))
    
    
# def is_square(n):
#     return n > -1 and math.sqrt(n) % 1 == 0;

# def is_square(n):    
#     return n >= 0 and (n**0.5) % 1 == 0


# def is_square(n):    

#     if n < 0:
#         return False

#     sqrt = math.sqrt(n)
    
#     return sqrt.is_integer()

# def is_square(n):    
#     try:
#         return math.sqrt(n).is_integer()
#     except ValueError:
#         return False

# def is_square(n):    
#     if n>=0:
#         if int(n**.5)**2 == n:
#             return True
#     return False

# def is_square(n):    
#     return n>=0 and sqrt(n).is_integer()

# def is_square(n):
#   return n >= 0 and int(math.sqrt(n)) ** 2 == n