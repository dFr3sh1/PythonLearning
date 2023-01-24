###
# Premiers pas en POO (Programamtion Orintée Objet)
###
# - Différence programmation impérattive / objet
# - Le plus simple possible
# - Exercices, mises en situation


# Personne
#   Données : name, age
#   Actions : 
#       - Se présenter() "Méthodes"
#       - Demander_son_nom() / inputs "Méthodes"

# --- DÈFINITION ---
# name : str
# age : int
# 1 - Si age == 0
#   => "Bonjour , je m'appelle Toto"
#   => On n'affiche pas mineur
# 2 -  Si nom == ""
#    => Demander no à l'utilisateur
#   => Prompt_name(...)  -> input("") -> name    


class Person:
    def __init__(self, name: str = "", age: int = 0): # Création du constructeur, par défault il existe un qqp dans le code mais c'est mieux de créer le notre car par convention les paramètres sont égaux.
        self.name = name
        self.age  = age
        if name == "":
            self.Prompt_name()
        print(f"Constructeur personne {self.name}")
    
    def Introduce_yourself(self):
        person_info = "Bonjour, Je m'appelle. " + (self.name)
        if self.age != 0:
            person_info += " J'ai " + str(self.age) + " ans."
        print(person_info)
        if self.age != 0:
            print("Je suis majeur.e" if self.Is_older() else "Je suis mineur.e") # De la même façon que on peut accéder à une variable self on peutt le faire avec la méthode

    def Is_older(self):
        return self.age >= 18
    
    def Prompt_name(self):
        self.name = input("Quel est votre nom ? ")
        
    
    # def Other_function(self):
    #     print(f"Nom : {self.name}")

# --- UTILISATTION ---
person1 = Person("Jean", 30)  # Je crée une personne
person2 = Person("Paul", 0)  # Je crée une personne
person3 = Person()
person4 = Person(age=20)

# Person.Introduce_yourself(person1)
person1.Introduce_yourself() # Méthode de classe, utilisation du "self"
person2.Introduce_yourself()
person3.Introduce_yourself()
person4.Introduce_yourself()

print("estMajeur1 : ", person1.Is_older())
print("estMajeur2 : ", person2.Is_older())

#person1.Other_function() # Méthode de classe


# def show_person_information(name, age):
#     print(f"La personne s'appelle {name}, son age est {age} ans")
    

# def ask_person_name():
#     name = input("Quel est votre nom ? ")
#     return name


name1 = "Jean"
age1 = 30

name2 = "Paul"
age2 = 25

# show_person_information(name1, age1)
# show_person_information(name2, age2)

# name3 = ask_person_name()
# age3 = 18 

# show_person_information(name3, age3)

