# -*- coding: utf-8 -*-

# 7.2
# Ecrire un algorithme qui demande un nombre de départ, et qui ensuite écrit la table
# de multiplication de ce nombre, présentée comme suit (cas où l'utilisateur entre le
# nombre 7) :
# Table de 7 :
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# …
# 7 x 10 = 70


# DEBUT
#     Ecrire un nombre (a)

#     SI a est renseigné
#         Essayer de faire les actions suivantes :
#             Convertir a en un entier

#             POUR i allant de 0 à 10 (inclus)
#                 Afficher "a x i =" et le résultat de a multiplié par i
#         SI une erreur se produit (par exemple, si l'entrée n'est pas un nombre)
#             Afficher un message d'erreur "Le format de vos saisies sont incorrect, entrez des nombres"
#             Appeler la fonction multiplication() pour redemander les saisies
#     SINON
#         Afficher un message "user input not found" (aucune saisie)
# FIN


print("Resultat algo 7.2")

def multiplication():
    a = input("Entrez un nombre")

    if a:
        try:
            a = int(a)

            for i in range(11):
                print(f"{a} x {i} = {a*i}")
        except:
            print("Le format de vos saisies sont incorrect entrez des nombres")
            multiplication()
    else:
        print("user input not found")

# multiplication()