# -*- coding: utf-8 -*-

# 6.2
# Ecrire un algorithme qui demande à l’utilisateur un nombre compris entre 1 et 3
# jusqu’à ce que la réponse convienne.

# DEBUT
#     Initialiser value à -1

#     TANT QUE value <= 0 OU value >= 3
#         Ecrire "Entrez un nombre entre 1 et 3" (user_input)

#         SI user_input est renseigné
#             Essayer de faire les actions suivantes :
#                 Convertir user_input en un entier (value)
#             SI une erreur se produit (par exemple, si l'entrée n'est pas un nombre)
#                 Afficher "Entrez un nombre correct"
#         SINON
#             Afficher "user input not found"

#     Afficher "Vous avez gagné"
# FIN


print("Resultat algo 6.2")

def loop_user():

    value = -1

    while value <= 0 or value >= 3:
        user_input = input("Entrez un nombre entre 1 et 3")
        
        if user_input:
            
            try:
                value = int(user_input)
            except:
                print("Entrez un nombre correct")
        else:
            print("user input no found")

    print("Vous avez gagné")

loop_user()

# 6.3
# Ecrire un algorithme qui demande un nombre compris entre 10 et 20, jusqu’à ce que
# la réponse convienne. En cas de réponse supérieure à 20, on fera apparaître un
# message : « Plus petit ! », et inversement, « Plus grand ! » si le nombre est inférieur
# à 10.

# DEBUT
#     Initialiser value à -1

#     TANT QUE value < 10 OU value > 20
#         Ecrire "Entrez un nombre entre 10 et 20" (user_input)

#         SI user_input est renseigné
#             Essayer de faire les actions suivantes :
#                 Convertir user_input en un entier (value)

#                 SI value < 10
#                     Afficher "Plus grand!"
#                 SINON SI value > 20
#                     Afficher "Plus petit!"
#             SI une erreur se produit (par exemple, si l'entrée n'est pas un nombre)
#                 Afficher "Entrez un nombre correct"
#         SINON
#             Afficher "user input not found"

#     Afficher "Vous avez gagné"
# FIN


print("Resultat algo 6.3")

def just_price():
    value = -1

    while value < 10 or value > 20:
        user_input = input("Entrez un nombre entre 10 et 20: ")
        
        if user_input:
            try:
                value = int(user_input)

                if value < 10:
                    print("Plus grand!")

                elif value > 20:
                    print("Plus petit!")
                    
            except ValueError:
                print("Entrez un nombre correct")
        else:
            print("user input no found")

    print("Vous avez gagné")

just_price()


# 6.4
# Reprendre l’exercice de calcul d’année bissextile. Faire en sorte que l’on demande
# des dates jusqu'à la saisie de la lettre ‘q’ , pour sortir. Pour chaque date saisie,
# afficher si la date est bissextile ou non.

# DEBUT
#     Ecrire une année (year)

#     SI year est égal à "q"
#         Retourner (fin de la fonction)

#     SI year est renseigné
#         Essayer de faire les actions suivantes :
#             Convertir year en un entier

#             SI (year % 4 == 0 ET year % 100 != 0) OU (year % 400 == 0)
#                 Afficher "L'année est bissextile"
#             SINON
#                 Afficher "L'année n'est pas bissextile"

#             Appeler la fonction get_leap_year()

#         SI une erreur se produit (par exemple, si l'entrée n'est pas un nombre)
#             Afficher un message d'erreur "Le format de vos saisies est incorrect, entrez un nombre"
#             Appeler la fonction get_leap_year() pour redemander les saisies
#     SINON
#         Afficher un message "user input not found" (aucune saisie)
# FIN


print("Resultat algo 6.4")

def get_leap_year():
    year = input("Entrez une année")

    if year == "q":
        return

    if year:
        try:
            year = int(year)

            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                print("L'année est bissextile")
            else:
                print("L'année n'est pas bissextile")

            get_leap_year()

        except:
            print("Le format de vos saisies sont incorrect entrez un nombre")
            get_leap_year()
    else:
        print("user input not found")

get_leap_year()


# 6.5
# Ecrire un algorithme qui demande un nombre de départ, et qui calcule la somme des
# entiers jusqu’à ce nombre. Par exemple, si l’on entre 5, le programme doit calculer :
# 1 + 2 + 3 + 4 + 5 = 15

# DEBUT
#     Ecrire un nombre (number)

#     SI number est renseigné
#         Essayer de faire les actions suivantes :
#             Convertir number en un entier

#             Initialiser result à 0

#             POUR i allant de 0 à number (inclus)
#                 Ajouter i à result
#                 Afficher i et result

#             Afficher "Le nombre final est" et result
#         SI une erreur se produit (par exemple, si l'entrée n'est pas un nombre)
#             Afficher un message d'erreur "Le format de vos saisies est incorrect, entrez un nombre"
#             Appeler la fonction loop_number() pour redemander les saisies
#     SINON
#         Afficher un message "user input not found" (aucune saisie)
# FIN


print("Resultat algo 6.5")

def loop_number():
        number = input("Entrez un nombre")

        if number:
            try:
                number = int(number)
                result = 0

                for i in range(number + 1):
                    result += i
                    print(i, result)

                print(f"Le nombre final est {result}")
            except:
                print("Le format de vos saisies sont incorrect entrez un nombre")
                loop_number()
        else:
            print("user input not found")

loop_number()


# 6.6
# Lire la suite des prix (en euros entiers et terminée par zéro) des achats d’un client.
# Calculer la somme qu’il doit, lire la somme qu’il paye, et simuler la remise de la
# monnaie en affichant les textes "10 Euros", "5 Euros" et "1 Euro" autant de fois qu’il
# y a de coupures de chaque sorte à rendre.

print("Resultat algo 6.6")


# 6.7
# Ecrire un algorithme qui demande successivement des nombres à l’utilisateur, et qui
# lui dise ensuite quel était le plus grand parmi ces nombres. La saisie d’un 0 arrête la
# demande .
# L’algo affiche le plus grand nombre et sa position. Exemple :
# Entrez le nombre numéro 1 : 12
# Entrez le nombre numéro 2 : 14
# etc.
# Entrez le nombre numéro 20 : 0
# Le plus grand de ces nombres est : 14 en position 2

# DEBUT
#     Initialiser une liste vide (list)

#     TANT QUE vrai
#         Ecrire un nombre (user_input)

#         SI user_input est renseigné
#             Essayer de faire les actions suivantes :
#                 Convertir user_input en un entier

#                 Ajouter user_input à la liste (list)

#                 SI user_input est égal à 0
#                     Sortir de la boucle
#             SI une erreur se produit (par exemple, si l'entrée n'est pas un nombre)
#                 Afficher "Entrez un nombre correct"
#         SINON
#             Afficher "user input not found" (aucune saisie)

#     Initialiser high_number avec la valeur maximale de list
#     Initialiser index avec l'index de high_number dans list

#     Afficher "Le nombre le plus grand est" high_number et "à la position" index + 1
# FIN


print("Resultat algo 6.7")

def get_high_number():

    list = []

    while True:
        user_input = input("Entrz un nombre")

        if user_input:
            try:
                user_input = int(user_input)
                list.append(user_input)

                if user_input == 0:
                    break
            except:
                print("Entrez un nombre correct")
        else:
            print("user input not found")

    high_number = max(list)
    index = list.index(high_number)

    print(f"Le nombre le plus grand est {high_number} à la position {index + 1}")

get_high_number()