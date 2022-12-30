# x = 1
# print(x)
# y = 2.5

# #A rithmetic
# print(x + y)
# print( x - y)
# print(x * y)
# print(x / y)
# print(x ** y) #Dans cette expression nous sommes en train de dire x puissance de y
# # Comparaison
# print(x > y)
# print(x >= y)
# print(x < y)
# print(x <= y)
# print(x == y)
# print(x != y)
# # Logique
# print(False & True) # AND
# print(False | True) # OR
# print(False ^ True) # XOR
# # String
# prenom = 'Guillaume 0'

# Functions
# f = lambda x: x ** 2 # function d'x est égale à x puissance de deux
# print(f(3))

def e_potentielle(masse, hauteur, g = 9.81):
    E = masse * hauteur * g
    print(E, 'Joules')
    return E

e_potentielle(masse = 65, hauteur = 1.68)
print(e_potentielle)

def e_potentielle_limite(masse, hauteur, limite, g=9.81):
    E = masse * hauteur * g
    return E < limite

e_potentielle_limite(65, 1.68, 1000)



