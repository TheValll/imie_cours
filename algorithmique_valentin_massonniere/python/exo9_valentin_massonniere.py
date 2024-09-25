# -*- coding: utf-8 -*-

# 9.2
# Écrire un algorithme qui permette de connaître ses chances de gagner au tiercé,
# quarté, quinté et autres impôts volontaires.
# On demande à l’utilisateur le nombre de chevaux partants, et le nombre de chevaux
# joués. Les deux messages affichés devront être :
# Dans l’ordre : une chance sur X de gagner
# Dans le désordre : une chance sur Y de gagner
# X et Y nous sont donnés par la formule suivante, si n est le nombre de chevaux
# partants et p le nombre de chevaux joués (on rappelle que le signe ! signifie
# "factorielle ") :
# X = n ! / (n - p) !
# Y = n ! / (p ! * (n – p) !)


print("Resultat algo 9.2")

def factorielle(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def lotery():

    n = input("Entrez le nombre de chevaux partants")
    p = input("Entrez le nombre de chevaux joués")

    if n and p :
        try:
            n = int(n)
            p = int(p)

            if n < 0 or p < 0 or p > n:
                print("Les valeurs doivent être positives et p ne peut pas dépasser n.")
                return

            X = factorielle(n) / factorielle(n - p)
            Y = factorielle(n) / (factorielle(p) * factorielle(n - p))

            print(f"Dans l’ordre : une chance sur {round(X,0)} de gagner")
            print(f"Dans le désordre : une chance sur {round(Y,0)} de gagner")
        except ValueError:
            print("Entrez des nombres correct")
            lotery()
    else:
        print("user input not found")

lotery()


# 9.3
# Écrivez une fonction qui renvoie le nombre de voyelles contenues dans une chaîne
# de caractères passée en argument. Au passage, notez qu'une fonction a tout à fait
# le droit d'appeler une autre fonction.
# Essayer la fonction avec la chaîne “je m’amuse beaucoup en algorithmique”


print("Resultat algo 9.2")

import operator as op 

vowels="aeiouAEIOU"
char = "je m’amuse beaucoup en algorithmique"
  
def count_vowel(char): 
    count = 0

    for i in range(len(char)):
        if op.countOf(vowels, char[i])>0: 
            count += 1

    print(count)

count_vowel(char)