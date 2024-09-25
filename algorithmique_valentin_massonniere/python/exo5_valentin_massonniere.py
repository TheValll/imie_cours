# -*- coding: utf-8 -*-

# 5.3
# Ecrire un algorithme qui demande deux nombres à l’utilisateur et l’informe ensuite si
# leur produit est négatif ou positif (on laisse de côté le cas où le produit est nul).
# Attention toutefois : on ne doit pas calculer (et du coup tester) le produit des deux
# nombres.


# DEBUT
#     Ecrire le premier nombre (a)
#     Ecrire le deuxième nombre (b)

#     SI a et b sont renseignés
#         Essayer de faire les actions suivantes :
#             Convertir a en un entier
#             Convertir b en un entier

#             SI a est supérieur à 0 ET b est supérieur à 0
#                 Afficher "Le produit des deux nombres est positif"
#             SINON SI a est supérieur à 0 ET b est inférieur à 0
#                 Afficher "Le produit des deux nombres est négatif"
#             SINON SI a est inférieur à 0 ET b est inférieur à 0
#                 Afficher "Le produit des deux nombres est négatif"
#             SINON
#                 Afficher "Le produit des deux nombres est positif"
#         SI une erreur se produit (par exemple, si les entrées ne sont pas des nombres)
#             Afficher un message d'erreur "Le format de vos saisies est incorrect, entrez des nombres"
#             Rappeler la fonction get_product_sign pour redemander les saisies
#     SINON
#         Afficher un message "user input not found" (aucune saisie)
# FIN


print("Resultat algo 5.3")

def get_product_sign():
    a = input("Entrez un nombre 1")
    b = input("Entrez un nombre 2")

    if a and b:
        try:
            a = int(a)
            b = int(b)

            if a > 0 and b > 0:
                print("Le produit des deux nombres est positif")
            elif a > 0 and b < 0:
                print("Le produit des deux nombres est négatif")
            elif a < 0 and b < 0:
                print("Le produit des deux nombres est négatif")
            else:
                print("Le produit des deux nombres est positif")
        except ValueError:
            print("Le format de vos saisies sont incorrect entrez des nombres")
            get_product_sign()
    else:
        print("user input not found")

get_product_sign()


# 5.4
# Ecrire un algorithme qui demande trois noms à l’utilisateur et l’informe ensuite s’ils
# sont rangés ou non dans l’ordre alphabétique.

# DEBUT
#     Ecrire le premier nom (nom1)
#     Ecrire le deuxième nom (nom2)
#     Ecrire le troisième nom (nom3)

#     SI nom1, nom2 et nom3 sont renseignés
#         Essayer de faire les actions suivantes :
#             Créer un tableau (array) contenant nom1, nom2 et nom3
#             Trier le tableau et stocker le résultat dans array_sorted

#             SI array est égal à array_sorted
#                 Afficher "Les noms sont dans l'ordre alphabétique"
#             SINON
#                 Afficher "Les noms ne sont pas dans l'ordre alphabétique"
#         SI une erreur se produit (par exemple, si les entrées ne sont pas des chaînes)
#             Afficher un message d'erreur "Le format de vos saisies est incorrect, entrez des noms"
#             Rappeler la fonction check_alphabetic_order pour redemander les saisies
#     SINON
#         Afficher un message "user input not found" (aucune saisie)
# FIN

print("Resultat algo 5.4")

def check_alphabetic_order():
    nom1 = input("Entrez un nom 1")
    nom2 = input("Entrez un nom 2")
    nom3 = input("Entrez un nom 3")

    if nom1 and nom2 and nom3:
        try:
            array = [nom1, nom2, nom3]
            array_sorted = array.sort()

            if array == array_sorted:
                print("Les noms sont dans l'ordre alphabétique")
            else:
                print("Les noms ne sont pas dans l'ordre alphabétique")
        except ValueError:
            print("Le format de vos saisies sont incorrect entrez des noms")
            check_alphabetic_order()
    else:
        print("user input not found")

check_alphabetic_order()


# 5.5
# Le prix du ticket de cinéma dépend de l’âge, et de la détention d’une carte
# d’abonnement :
# Sans carte : 10€ pour une personne de plus de 25 ans, 7.5€ sinon
# Sur présentation de la carte une réduction de 20 % est faite
# Calculer le prix du billet en fonction de ces paramètres.


# DEBUT
#     Ecrire l'âge de l'utilisateur (age)
#     Ecrire si l'utilisateur a la carte de cinéma (card) : "Y" ou "N"

#     SI age est renseigné ET card est "Y" ou "N"
#         Essayer de faire les actions suivantes :
#             Convertir age en un entier

#             SI card est "Y"
#                 Définir card à True
#             SINON
#                 Définir card à False

#             SI age est supérieur à 25
#                 Définir price à 10
#             SINON
#                 Définir price à 7.5

#             SI card est True
#                 price = price - (price * 20 / 100)

#             Arrondir price à 2 décimales

#             Afficher "Le prix est de {price} e"
#         SI une erreur se produit (par exemple, si les entrées ne sont pas des nombres)
#             Afficher un message d'erreur "Le format de vos saisies est incorrect, entrez un nombre ou insérer Y ou N pour indiquer si vous avez la carte du cinéma"
#             Rappeler la fonction get_cinema_ticket_price pour redemander les saisies
#     SINON
#         Afficher un message "user input not found" (aucune saisie)
# FIN


print("Resultat algo 5.5")

def get_cinema_ticket_price():
    age = input("Entrez votre age")
    card = input("Avez-vous la carte du cinéma ? Y or N")

    if age and card == "Y" or card == "N":
        try:
            age = int(age)
            if card == "Y":
                card = True
            else:
                card = False

            if age > 25:
                price = 10
            else:
                price = 7.5

            if card == True:
                price = price - (price * 20 / 100)

            price = round(price,2)

            print(f"Le prix est de {price} e")
        except ValueError:
            print("Le format de vos saisies sont incorrect entrez un nombre ou insérer Y ou N pour indiquer si vous avez la carte du cinéma")
            get_cinema_ticket_price()
    else:
        print("user input not found")

get_cinema_ticket_price()


# 5.6
# Définition d’une année bissextile sur wikipédia :
# Depuis l'ajustement du calendrier grégorien, l'année sera bissextile (elle aura 366
# jours)1
# :
#  si l'année est divisible par 4 et non divisible par 100, ou
#  si l'année est divisible par 400.
#  Sinon, l'année n'est pas bissextile (elle a 365 jours).
# (« divisible » signifie que la division donne un nombre entier, sans reste).
# Ainsi, 2019 n'est pas bissextile. L'an 2008 était bissextil suivant la première règle
# (divisible par 4 et non divisible par 100). L'an 1900 n'était pas bissextil car divisible
# par 4, mais aussi par 100 (première règle non respectée) et non divisible par 400
# (seconde règle non respectée). L'an 2000 était bissextil car divisible par 400.
# Ecrire un code Python qui demande la valeur d’une année et indique si elle est
# bissextile. NE PAS RECOPIER LA SOLUTION disponible sur le web. On attend
# votre propre code.


# DEBUT
#     Ecrire l'année (year)

#     SI year est renseigné
#         Essayer de faire les actions suivantes :
#             Convertir year en un entier

#             SI (year % 4 est égal à 0 ET year % 100 n'est pas égal à 0) OU (year % 400 est égal à 0)
#                 Afficher "L'année est bissextile"
#             SINON
#                 Afficher "L'année n'est pas bissextile"

#         SI une erreur se produit (par exemple, si l'entrée n'est pas un nombre)
#             Afficher un message d'erreur "Le format de vos saisies est incorrect, entrez un nombre"
#             Rappeler la fonction get_leap_year pour redemander les saisies
#     SINON
#         Afficher un message "user input not found" (aucune saisie)
# FIN


print("Resultat algo 5.6")

def get_leap_year():
    year = input("Entrez une année")

    if year:
        try:
            year = int(year)

            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                print("L'année est bissextile")
            else:
                print("L'année n'est pas bissextile")

        except ValueError:
            print("Le format de vos saisies sont incorrect entrez un nombre")
            get_leap_year()
    else:
        print("user input not found")

get_leap_year()



# 5.7
# Cet algorithme est destiné à prédire l'avenir, et il doit être infaillible !
# Il lira au clavier l’heure et les minutes, et il affichera l’heure qu’il sera une minute
# plus tard. Par exemple, si l'utilisateur tape 21 puis 32, l'algorithme doit répondre :
# "Dans une minute, il sera 21 heures 33".
# NB : on suppose que l'utilisateur entre une heure valide. Pas besoin donc de la
# vérifier.
# NB : il n’y aura pas de ‘s’ à heure dans la réponse “il sera 1 heure 33”


# DEBUT
#     Ecrire l'heure (hours)
#     Ecrire la minute (minutes)

#     SI hours et minutes sont renseignés
#         Essayer de faire les actions suivantes :
#             Convertir hours en un entier
#             Convertir minutes en un entier

#             SI hours est supérieur ou égal à 24 OU hours est inférieur à 0 OU minutes est supérieur ou égal à 60 OU minutes est inférieur à 0
#                 Lever une exception (erreur)

#             Créer une variable user_time qui combine la date actuelle avec l'heure et les minutes fournies
#             Créer une variable preddict_time en ajoutant 1 minute à user_time

#             SI preddict_time.hour est supérieur à 1
#                 Afficher "Dans une minute, il sera {preddict_time.hour} heures et {preddict_time.minute}"
#             SINON
#                 Afficher "Dans une minute, il sera {preddict_time.hour} heure et {preddict_time.minute}"

#         SI une erreur se produit (par exemple, si les entrées ne sont pas valides)
#             Afficher un message d'erreur "Le format de vos saisies est incorrect, entrez des heures et minutes valides"
#             Rappeler la fonction predict_hours pour redemander les saisies
#     SINON
#         Afficher un message "user input not found" (aucune saisie)
# FIN


print("Resultat algo 5.7")

from datetime import datetime, timedelta, time

def predict_hours():
    hours = input("Entrez une heure: ")
    minutes = input("Entrez une minute: ")

    if hours and minutes:
        try:
            hours = int(hours)
            minutes = int(minutes)

            if hours >= 24 or hours < 0 or minutes >= 60 or minutes < 0:
                raise Exception
            
            user_time = datetime.combine(datetime.today(), time(hours, minutes))
            preddict_time = user_time + timedelta(minutes=1)

            if preddict_time.hour > 1:
                print(f"Dans une minute, il sera {preddict_time.hour} heures et {preddict_time.minute}")
            else:
                print(f"Dans une minute, il sera {preddict_time.hour} heure et {preddict_time.minute}")

        except Exception:
            print("Le format de vos saisies est incorrect entrez des heures et minutes valides")
            predict_hours()
    else:
        print("user input not found")

predict_hours()


# 5.8
# Un magasin de reprographie facture 0,10 € les dix premières photocopies, 0,09 €
# les vingt suivantes et 0,08 € au-delà. Ecrivez un algorithme qui demande à
# l’utilisateur le nombre de photocopies effectuées et qui affiche la facture
# correspondante.


# DEBUT
#     Ecrire le nombre de photocopies (nb_paper)

#     SI nb_paper est renseigné
#         Essayer de faire les actions suivantes :
#             Convertir nb_paper en un entier
#             Définir invoice à 0

#             POUR i de 0 à nb_paper - 1 FAIRE
#                 SI i < 10
#                     Définir price à 0.10
#                     invoice = invoice + price
#                 SINON
#                     Définir price à 0.10 - (arrondir(i/10, 0)/100)
#                     invoice = invoice + price

#             Arrondir invoice à 2 décimales

#             Afficher le montant total de invoice
#         SI une erreur se produit (par exemple, si l'entrée n'est pas un nombre)
#             Afficher un message d'erreur "Le format de vos saisies est incorrect, entrez un nombre"
#             Rappeler la fonction get_invoice pour redemander les saisies
#     SINON
#         Afficher un message "user input not found" (aucune saisie)
# FIN

print("Resultat algo 5.8")

def get_invoice():
    nb_paper = input("Entrez un nombre de photocopies: ")

    if nb_paper:
        try:
            nb_paper = int(nb_paper)
            invoice = 0

            for i in range(nb_paper):
                if i < 10:
                    price = 0.10
                    invoice += price
                    invoice = round(invoice, 2)
                else:
                    price = 0.10 - (round(i/10,0)/100)
                    invoice += price
                    invoice = round(invoice, 2)

            print(round(invoice, 2))

        except ValueError:
            print("Le format de vos saisies est incorrect entrez un nombre")
            get_invoice()
    else:
        print("user input not found")

get_invoice()


# 5.9
# Les habitants de la principauté de Conamo paient l’impôt selon les règles
# suivantes :
# • les hommes de plus de 20 ans paient l’impôt . Dans ce cas la valeur de l’impôt est
# de 10 % du revenu imposable entre 20 et 40 ans compris, 15 % au-delà.
# • les femmes paient l’impôt si elles ont entre 18 et 35 ans . Dans ce cas la valeur de
# l’impôt est de 10 % du revenu imposable.
# • les autres ne paient pas d’impôt
# Le programme demandera donc l’âge et le sexe du Conamolien, et se prononcera
# donc ensuite sur le fait que l’habitant est imposable.
# Il demandera le revenu imposable et affichera la valeur de l’impôt.


# DEBUT de get_conamo_sexe_age
#     Ecrire l'âge de l'utilisateur (age)
#     Ecrire le sexe de l'utilisateur (sexe) : "M" ou "F"

#     SI age est renseigné ET sexe est "M" ou "F"
#         Essayer de faire les actions suivantes :
#             Convertir age en un entier

#             SI sexe est "M"
#                 SI age > 20
#                     Définir taxable à True
#                     Définir rate à 10
#                 SINON SI age > 40
#                     Définir taxable à True
#                     Définir rate à 15
#                 SINON
#                     Définir taxable à False
#                     Définir rate à 0

#             SI sexe est "F"
#                 SI age > 18 ET age < 35
#                     Définir taxable à True
#                     Définir rate à 10
#                 SINON
#                     Définir taxable à False
#                     Définir rate à 0

#             Retourner taxable, rate

#         SI une erreur se produit (par exemple, si l'entrée n'est pas un nombre)
#             Afficher un message d'erreur "Le format de vos saisies est incorrect, entrez un nombre et indiquez M ou F pour votre sexe"
#             Rappeler la fonction get_conamo_sexe_age pour redemander les saisies
#     SINON
#         Afficher un message "user input not found" (aucune saisie)
# FIN de get_conamo_sexe_age

# DEBUT de get_taxe_value
#     Ecrire le salaire (salary)
#     Ecrire le taux (rate)

#     Retourner round(salary * rate / 100, 2)
# FIN de get_taxe_value

# DEBUT de get_taxable
#     Appeler la fonction get_conamo_sexe_age et récupérer taxable, rate

#     SI taxable est True
#         Afficher "Vous êtes imposable avec un taux de {rate} %"
#         Ecrire le salaire (salary)

#         SI salary est renseigné
#             Essayer de faire les actions suivantes :
#                 Convertir salary en un entier
#                 Définir taxe_value en appelant get_taxe_value(salary, rate)
#                 Afficher "La valeur de votre impôt est de {taxe_value} e"
#             SI une erreur se produit (par exemple, si l'entrée n'est pas un nombre)
#                 Afficher un message d'erreur "Le format de vos saisies est incorrect, entrez un nombre"
#                 Rappeler la fonction get_taxable pour redemander les saisies
#         SINON
#             Afficher un message "user input not found" (aucune saisie)
#     SINON
#         Afficher "Vous n'êtes pas imposable"
# FIN de get_taxable


print("Resultat algo 5.9")

def get_conamo_sexe_age():
    age = input("Entrez votre age")
    sexe = input("Entrez votre sexe M or F")

    if age and sexe == "M" or sexe == "F":
        try:
            age = int(age)

            if sexe == "M":
                if age > 20:
                    taxable = True
                    rate = 10
                elif age > 40:
                    taxable = True
                    rate = 15
                else:
                    taxable = False
                    rate = 0

            if sexe == "F":
                if age > 18 and age < 35:
                    taxable = True
                    rate = 10
                else:
                    taxable = False
                    rate = 0

            return taxable, rate

        except ValueError:
            print("Le format de vos saisies sont incorrect entrez un nombre et indiquer M ou F pour votre sexe")
            get_conamo_sexe_age()
    else:
        print("user input not found")

def get_taxe_value(salary, rate):
    return round(salary * rate / 100, 2)

def get_taxable():
    taxable, rate = get_conamo_sexe_age()

    if taxable:
        print(f"Vous êtes impossable avec un taux de {rate} %")
        salary = input("Entrez votre salaire")

        if salary:
            try:
                salary = int(salary)
                taxe_value = get_taxe_value(salary, rate)
                print(f"La valeur de votre impôt est de {taxe_value} e")
            except ValueError:
                print("Le format de vos saisies sont incorrect entrez un nombre")
                get_taxable()
        else: 
            print("user input not found")
    else:
        print("Vous n'êtes pas impossable")

get_taxable()


# 5.10
# Une compagnie d'assurance automobile propose à ses clients quatre familles de
# tarifs identifiables par une couleur, du moins au plus onéreux : tarifs bleu, vert,
# orange et rouge. Le tarif dépend de la situation du conducteur :
# • un conducteur de moins de 25 ans et titulaire du permis depuis moins de deux
# ans, se voit attribuer le tarif rouge, si toutefois il n'a jamais été responsable
# d'accident. Sinon, la compagnie refuse de l'assurer.
# • un conducteur de moins de 25 ans et titulaire du permis depuis plus de deux ans,
# ou de plus de 25 ans mais titulaire du permis depuis moins de deux ans a le droit au
# tarif orange s'il n'a jamais provoqué d'accident, au tarif rouge pour un accident,
# sinon il est refusé.
# • un conducteur de plus de 25 ans titulaire du permis depuis plus de deux ans
# bénéficie du tarif vert s'il n'est à l'origine d'aucun accident et du tarif orange pour un
# accident, du tarif rouge pour deux accidents, et refusé au-delà
# • De plus, pour encourager la fidélité des clients acceptés, la compagnie propose un
# contrat de la couleur immédiatement la plus avantageuse s'il est entré dans la
# maison depuis plus d'un an.
# Ecrire l'algorithme permettant de saisir les données nécessaires (sans contrôle de
# saisie) et de traiter ce problème. Avant de se lancer à corps perdu dans cet
# exercice, on pourra réfléchir un peu et s'apercevoir qu'il est plus simple qu'il n'en a
# l'air (cela s'appelle faire une analyse !)


# DEBUT
#     Ecrire l'âge du conducteur (age)
#     Ecrire si le conducteur a le permis (asPermis) : "Y" ou "N"

#     SI asPermis est "N"
#         Afficher "Vous ne pouvez pas vous inscrire sans permis"
#         Retourner

#     Ecrire depuis combien d'années le conducteur a le permis (since)
#     Ecrire combien d'accidents le conducteur a eu (accidents)

#     SI age, asPermis, since, et accidents sont renseignés
#         Essayer de faire les actions suivantes :
#             Convertir age en un entier
#             Convertir since en un entier
#             Convertir accidents en un entier

#             SI accidents > 2
#                 Afficher "Vous ne pouvez pas vous inscrire avec plus de 2 accidents"
#                 Retourner

#             SI age < 25 ET since < 2 ET accidents > 0
#                 Afficher "Vous ne pouvez pas vous inscrire avec un accident"
#                 Retourner

#             SI age < 25 ET since < 2
#                 Afficher "Vous êtes éligible au tarif rouge"
#             SINON SI (age < 25 ET since >= 2) OU (age >= 25 ET since < 2)
#                 Afficher "Vous êtes éligible au tarif orange" SI accidents == 0 SINON "Vous êtes éligible au tarif rouge"
#             SINON
#                 Afficher "Vous êtes éligible au tarif vert" SI accidents == 0 SINON "Vous êtes éligible au tarif orange"
#         SI une erreur se produit (par exemple, si l'entrée n'est pas un nombre)
#             Afficher un message d'erreur "Le format de vos saisies est incorrect, entrez les valeurs correctement"
#             Rappeler la fonction get_assurance_price pour redemander les saisies
#     SINON
#         Afficher un message "user input not found" (aucune saisie)
# FIN

print("Resultat algo 5.10")

def get_assurance_price():
    age = input("Entrez votre age")
    asPermis = input("Avez-vous le permis Y or N")

    if asPermis == "N":
        print("Vous ne pouvez pas vous inscrire sans permis")
        return

    since = input("Depuis combien d'annees ?")
    accidents = input("Combien d'accidents avez-vous eu ?")
    
    if age and asPermis and since and accidents:
        
        try:
            age = int(age)
            since = int(since)
            accidents = int(accidents)

            if accidents > 2:
                print("Vous ne pouvez pas vous inscrire avec plus de 2 accidents")
                return

            if age < 25 and since < 2 and accidents > 0:
                print("Vous ne pouvez pas vous inscrire avec un accident")
                return

            if age < 25 and since < 2:
                print("Vous êtes éligible au tarif rouge")
            elif (age < 25 and since >= 2) or (age >= 25 and since < 2):
                print("Vous êtes éligible au tarif orange" if accidents == 0 else "Vous êtes éligible au tarif rouge")
            elif age >= 25 and since >= 2:
                print("Vous êtes éligible au tarif vert" if accidents == 0 else "Vous êtes éligible au tarif orange")
        except ValueError:
            print("Le format de vos saisies sont incorrect entrez les valeurs correctement")
            get_assurance_price()

    else:
        print("user input not found")

get_assurance_price()