# -*- coding: utf-8 -*-

# 1.2 Enoncé
# Dans le fichier exo1.py écrire une fonction permettant de dessiner divers sapins de
# hauteur h donnée.
# Voici quelques exemples pour h= 5.

print("Resultat algo 1.2")

def sapin_plein():
    h = 5
    for i in range(h):
        print(" " * (h - i - 1), end="")
        print("*" * (2 * i + 1))

sapin_plein()