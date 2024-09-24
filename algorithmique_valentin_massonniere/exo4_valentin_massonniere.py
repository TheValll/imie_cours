# -*- coding: utf-8 -*-

# 4.2.1
# Entier val, double
# Début
# Val ← 231
# Double ← Val * 2
# Ecrire Val
# Ecrire Double
# Fin

print("Resultat algo 4.2.1")

value1 = 231
double_value1 = value1*2
print(value1)
print(double_value1)

# 4.2.2
# Ecrire un programme qui demande un nombre à l’utilisateur, puis qui calcule et
# affiche le carré de ce nombre.
# Indices :
# Pour convertir la chaîne « 123 » en nombre 123 écrire :
# Val = int(“123”)
# Pour élever A à la puissance B : A ** B

print("Resultat algo 4.2.2")

def square_number():
    user_input1 = input("Entrez un nombre")
    if user_input1:
        try:
            result = pow(int(user_input1),2)
            print(result)
        except:
            print("Ceci n'est pas un nombre")
            square_number()
    else:
        print("user input not found")

square_number()

# 4.2.3
# Ecrire un programme qui lit le prix HT d’un article, le nombre d’articles et le taux de
# TVA, et qui fournit le prix total TTC correspondant.
# Faire en sorte que des libellés apparaissent clairement. Ex
# Prix total 10.30 €

print("Resultat algo 4.2.3")

def calculate_ttc():
    ht_price = input("Entrez un prix HT")
    nb_article = input("Entrez un nombre d'article")
    tva_rate = input("Entrez la TVA")

    if ht_price and nb_article and tva_rate:
        try:
            result = round((int(ht_price) * int(tva_rate) / 100) * int(nb_article), 2)
            print(f"Le prix total est de {result} e")
        except:
            print("Le format de vos saisies sont incorrect entrez des nombres")
            calculate_ttc()
    else:
        print("user input not found")

calculate_ttc()