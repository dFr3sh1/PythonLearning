# Listes
"""
listes_1 = [1, 2, 3, 4, 4, 6, 7, 35, 84]
villes = ['Paris', 'Berlin', 'Londres', 'Bruxelles']
liste_2 = [listes_1, villes]
Liste_3 = []

# Tuples
tuple_1 = (1, 2, 6, 1, 7)

# String
prenom = 'Nicolas'

# Indexing
print(villes[0])

# Slicing
#liste[début : fin : pas]
print(villes[:3]) # Généralement on omis ne mettre l'index cero lors de le slicing
print(villes[2:]) # On peut également démarrer le slicing à partir d'autre indexe que le cero
print(villes[::2]) # On peut tout solliciter avec décalages de deux pas (ou autre)
print(villes[::-1]) #On sollicite les éléments de la liste dans le sens conttraire, càd du dernier au premier.

# Actions qu'on peut réaliser avec les listes

villes.append('Dublin')
print(villes)

villes.insert(2, 'Madrid')
print(villes)

# On peutt également intégrer une liste à la fin de notre liste appuyé de la fonction .extend
villes_2 = ['Amsterdam', 'Rome']
villes.extend(villes_2)
print(villes)

#len() est la fonctioon pour compter les éléments de la liste

# Pour trier par ordre alphabétique
villes.sort()
print(villes)

villes.sort(reverse=True)
print(villes)

# count() est la fonction qui nous permettre de compter combien de fois un élément apparaît dans une liste.
villes.count('Paris')

if 'Paris' in villes:
    print('Oui')
else:
    print('Non')
# Pour solliciter
for i in villes:
    print(i)

# Pour solliciter les index ett valeurs des éléments de la liste
for index, valeur in enumerate(villes):
    print(index, valeur)

# Pour mélanger les éléments de différents listes on utilise la fonction zip

for a, b in zip(villes, listes_1):
    print(a, b)

Exercicse : reprendre la fonction de fibonacci de l'exercise précédent et au lieu d'imprimer seulement la valeurr d'a il devra nous retourner 
le fibonacci de tous les éléments d'une liste"""


def fibonacci(n):
    a = 0
    b = 1
    fin = [a]
    while b < n:
        a,b = b, a+b
        fin.append(a)
    return fibonacci

print(fibonacci(1000))



