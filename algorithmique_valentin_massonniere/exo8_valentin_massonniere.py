# -*- coding: utf-8 -*-

# 8.2
# Ecrire un algorithme qui déclare un tableau de 9 notes, dont on fait ensuite saisir les
# valeurs par l’utilisateur. 

# DEBUT
#     Initialiser une liste vide (list)

#     POUR i allant de 0 à 8 (inclus)
#         Ecrire un nombre (user_input)

#         SI user_input est renseigné
#             Essayer de faire les actions suivantes :
#                 Convertir user_input en un entier

#                 Ajouter user_input à la liste (list)
#             SI une erreur se produit (par exemple, si l'entrée n'est pas un nombre)
#                 Afficher "Entrez un nombre correct"
#                 Appeler la fonction list_user() pour redemander les saisies
#         SINON
#             Afficher "user input no found" (aucune saisie)

#     Afficher la liste (list)
# FIN

print("Resultat algo 8.2")

def list_user():

    list = []

    for i in range(9):
        user_input = input("Entrez un nombre")

        if user_input:
            try:
                user_input = int(user_input)
                list.append(user_input)
            except ValueError:
                print("Entrez un nombre correct")
                list_user()
        else:
            print("user input no found")

    print(list)

# list_user()


# 8.3
# Ecrivez un algorithme constituant un tableau, à partir de deux tableaux de même
# longueur préalablement saisis. Le nouveau tableau sera la somme des éléments
# des deux tableaux de départ. 


# DEBUT
#     Initialiser table1 avec les valeurs [4, 8, 7, 9, 1, 5, 4, 6]
#     Initialiser table2 avec les valeurs [7, 6, 5, 2, 1, 3, 7, 4]
#     Initialiser une table vide (table3)

#     POUR i allant de 0 à la longueur de table1 - 1
#         Ajouter à table3 la somme de table1[i] et table2[i]

#     Afficher table1
#     Afficher table2
#     Afficher table3
# FIN

print("Resultat algo 8.3")

def sum_table():
    table1 = [4, 8, 7, 9, 1, 5, 4, 6]
    table2 = [7, 6, 5, 2, 1, 3, 7, 4]
    table3 = []

    for i in range(len(table1)):
        table3.append(table1[i] + table2[i])

    print(table1)
    print(table2)
    print(table3)

sum_table()


# 8.4
# Ecrivez un algorithme permettant, à l’utilisateur de saisir les noms d’élèves et notes
# d'une classe. Le programme, une fois la saisie terminée (touche ‘q’), affiche la
# moyenne puis les noms et notes des élèves dont la note est supérieure à la
# moyenne de la classe. 


# DEBUT
#     Initialiser une liste vide (classe)

#     Définir la fonction school_notes()
#         Rendre la variable classe accessible globalement

#         Ecrire un nom (student)
#         SI student est égal à "q"
#             Retourner (terminer la fonction)

#         Ecrire une note (note)
#         SI student et note sont renseignés
#             Essayer de faire les actions suivantes :
#                 Convertir note en un nombre flottant

#                 Créer un dictionnaire student_data avec les clés "name" et "note"
#                 Ajouter student_data à la liste classe
#                 Afficher "Enregistré !"
#             SI une erreur se produit (par exemple, si la note n'est pas un nombre valide)
#                 Afficher "Entrez un nombre valide pour les notes."
#         SINON
#             Afficher "Aucune entrée trouvée."

#         Filtrer la liste classe pour obtenir une nouvelle liste (classe_filtered)
#         contenant seulement les étudiants dont la note est supérieure à 10

#         Afficher la liste classe
#         Afficher la liste classe_filtered

#         Appeler la fonction school_notes() pour redemander des saisies
# FIN

print("Resultat algo 8.4")

classe = []

def school_notes():
    global classe

    student = input("Entrez un nom")
    if student == "q":
        return

    note = input("Entrez une note")
    if student and note:
        try:
            note = float(note)
            student_data = {
                "name": student,
                "note": note
            }
            classe.append(student_data)
            print("Enregistré !")
        except ValueError:
            print("Entrez un nombre valide pour les notes.")
    else:
        print("Aucune entrée trouvée.")

    classe_filtered = [s for s in classe if s['note'] > 10]

    print(classe)
    print(classe_filtered)

    school_notes()

school_notes()