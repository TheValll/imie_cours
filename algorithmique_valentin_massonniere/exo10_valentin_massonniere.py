# -*- coding: utf-8 -*-


# 10.2
# Ecrire un algorithme puis code python pour la recherche d’un no de téléphone à
# partir d’un nom. Le fichier annuaire.txt est utilisé en lecture.
# Le programme boucle sur la saisie de noms jusqu’à chaîne vide.


print("Resultat algo 9.2")

def annulaire():

    while True:
        name = input("Entrez un nom")

        if name.strip() == '':
            return
        
        phone = input("Entrez un numéro")
            
        if name and phone:
            line = f"Name : {name}, Phone : {phone} \n"
            name = ""
            phone = ""

            try:
                with open("annulaire.txt", "a") as f:
                    f.write(line)
                print("Données mises à jour")
            except:
                print("Une erreur est survenue")
                return
        else:
            print("user input not found")

annulaire()