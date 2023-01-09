traduction = {
    "chien": "dog",
    "chat": "cat",
    "souris": "mouse",
    "oiseau": "bird"
    }
"""
    Créer une fonction trier qui prend comme argument un dictionnaire classeur avec deux associations, 
    une liste "positif" et une "negatif", censé de ranger un nombre soit positif ou négatif en fonction de son signe 
 """

classeur = {
    "positif": [0, 1, 2, 3, 4, 5 , 6],
    "negatif": [7, 8, 9, 10, 11],
}

def trier(classeur, nombre):
    if nombre > 0:
        classeur['positif'].append(nombre)
    else:
        classeur['negatif'].append(nombre)
        
    return classeur

trier(classeur, -2)

