"""
def signe(x):
    if x > 0:
        print(x, 'positif')
    elif x == 0:
        print(x, 'nul')
    else:
        print(x, 'négatif')

signe(1)

for element in range(10):
    print(element)

for element in range(5, 10, 2):
    print(element)

for element in range(10, -10, -1):
    print(element)

for element in range(10, -10, -1):
    signe(element)
x = 0

while x > 10:
    print(x)
    x += 1
"""

def fibonacci(n):
    a = 0
    b = 1
    while a <= n:
        print(a)
        a, b = b, a + b

fibonacci(69)
print(fibonacci)




