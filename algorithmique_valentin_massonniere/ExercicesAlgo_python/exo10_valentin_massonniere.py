# -*- coding: utf-8 -*-


# 10.2
# Ecrire un algorithme puis code python pour la recherche d’un no de téléphone à
# partir d’un nom. Le fichier annuaire.txt est utilisé en lecture.
# Le programme boucle sur la saisie de noms jusqu’à chaîne vide.


print("Resultat algo 9.2")

def annulaire():
    stop = False

    while stop:
        name = input("Entrez un nom")

        if name.strip() == '':
            stop = True
        
        phone = input("Entrez un numéro")
            
        if name and phone:
            line = f"Name : {name}; Phone : {phone} \n"
            name = ""
            phone = ""

            try:
                with open("annulaire.txt", "a") as f:
                    f.write(line)
                print("Données mises à jour")
            except ValueError:
                print("Une erreur est survenue")
                stop = True
        else:
            print("user input not found")

annulaire()