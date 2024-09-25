import streamlit as st

from utils import NewPage
from utils import Algo_part_5

NewPage.main("Algo ui", "wide", "auto")

# Section 5

st.write("Algo part 5")
st.write(f"""Enoncé : \n
5.3
Ecrire un algorithme qui demande deux nombres à l’utilisateur et l’informe ensuite si
leur produit est négatif ou positif (on laisse de côté le cas où le produit est nul).
Attention toutefois : on ne doit pas calculer (et du coup tester) le produit des deux
nombres.""")

a = st.text_input("Entrez un nombre a")
b = st.text_input("Entrez un nombre b")
confirm_5_3 = st.button("Confirm", key=1)

if confirm_5_3:
    Algo_part_5.get_product_sign(a, b)


st.write(f"""Enoncé : \n
5.4
Ecrire un algorithme qui demande trois noms à l’utilisateur et l’informe ensuite s’ils
sont rangés ou non dans l’ordre alphabétique.""")

nom1 = st.text_input("Entrez un nom 1")
nom2 = st.text_input("Entrez un nom 2")
nom3 = st.text_input("Entrez un nom 3")
confirm_5_3_2 = st.button("Confirm", key=2)

if confirm_5_3_2:
    Algo_part_5.get_product_sign(a, b)


st.write(f"""Enoncé : \n
5.5
Le prix du ticket de cinéma dépend de l’âge, et de la détention d’une carte
d’abonnement :
Sans carte : 10€ pour une personne de plus de 25 ans, 7.5€ sinon
Sur présentation de la carte une réduction de 20 % est faite
Calculer le prix du billet en fonction de ces paramètres.""")

age = st.text_input("Entrez votre age", key=110)
card = st.text_input("Avez-vous la carte du cinéma ? Y or N")
confirm_5_3_3 = st.button("Confirm", key=3)

if confirm_5_3_3:
    Algo_part_5.get_cinema_ticket_price(age, card)


st.write(f"""Enoncé : \n
5.6
Définition d’une année bissextile sur wikipédia :
Depuis l'ajustement du calendrier grégorien, l'année sera bissextile (elle aura 366
jours)1
:
 si l'année est divisible par 4 et non divisible par 100, ou
 si l'année est divisible par 400.
 Sinon, l'année n'est pas bissextile (elle a 365 jours).
(« divisible » signifie que la division donne un nombre entier, sans reste).
Ainsi, 2019 n'est pas bissextile. L'an 2008 était bissextil suivant la première règle
(divisible par 4 et non divisible par 100). L'an 1900 n'était pas bissextil car divisible
par 4, mais aussi par 100 (première règle non respectée) et non divisible par 400
(seconde règle non respectée). L'an 2000 était bissextil car divisible par 400.
Ecrire un code Python qui demande la valeur d’une année et indique si elle est
bissextile. NE PAS RECOPIER LA SOLUTION disponible sur le web. On attend
votre propre code.""")

year = st.text_input("Entrez une année")
confirm_5_3_4 = st.button("Confirm", key=4)

if confirm_5_3_4:
    Algo_part_5.get_leap_year(year)


st.write(f"""Enoncé : \n
5.7
Cet algorithme est destiné à prédire l'avenir, et il doit être infaillible !
Il lira au clavier l’heure et les minutes, et il affichera l’heure qu’il sera une minute
plus tard. Par exemple, si l'utilisateur tape 21 puis 32, l'algorithme doit répondre :
"Dans une minute, il sera 21 heures 33".
NB : on suppose que l'utilisateur entre une heure valide. Pas besoin donc de la
vérifier.
NB : il n’y aura pas de ‘s’ à heure dans la réponse “il sera 1 heure 33”""")

hours = st.text_input("Entrez une heure: ")
minutes = st.text_input("Entrez une minute: ")
confirm_5_3_5 = st.button("Confirm", key=5)

if confirm_5_3_5:
    Algo_part_5.predict_hours(hours, minutes)


st.write(f"""Enoncé : \n
5.8
Un magasin de reprographie facture 0,10 € les dix premières photocopies, 0,09 €
les vingt suivantes et 0,08 € au-delà. Ecrivez un algorithme qui demande à
l’utilisateur le nombre de photocopies effectuées et qui affiche la facture
correspondante.""")

nb_paper = st.text_input("Entrez un nombre de photocopies: ")
confirm_5_3_6 = st.button("Confirm", key=6)

if confirm_5_3_6:
    Algo_part_5.get_invoice(nb_paper)


st.write(f"""Enoncé : \n
5.10
Une compagnie d'assurance automobile propose à ses clients quatre familles de
tarifs identifiables par une couleur, du moins au plus onéreux : tarifs bleu, vert,
orange et rouge. Le tarif dépend de la situation du conducteur :
• un conducteur de moins de 25 ans et titulaire du permis depuis moins de deux
ans, se voit attribuer le tarif rouge, si toutefois il n'a jamais été responsable
d'accident. Sinon, la compagnie refuse de l'assurer.
• un conducteur de moins de 25 ans et titulaire du permis depuis plus de deux ans,
ou de plus de 25 ans mais titulaire du permis depuis moins de deux ans a le droit au
tarif orange s'il n'a jamais provoqué d'accident, au tarif rouge pour un accident,
sinon il est refusé.
• un conducteur de plus de 25 ans titulaire du permis depuis plus de deux ans
bénéficie du tarif vert s'il n'est à l'origine d'aucun accident et du tarif orange pour un
accident, du tarif rouge pour deux accidents, et refusé au-delà
• De plus, pour encourager la fidélité des clients acceptés, la compagnie propose un
contrat de la couleur immédiatement la plus avantageuse s'il est entré dans la
maison depuis plus d'un an.
Ecrire l'algorithme permettant de saisir les données nécessaires (sans contrôle de
saisie) et de traiter ce problème. Avant de se lancer à corps perdu dans cet
exercice, on pourra réfléchir un peu et s'apercevoir qu'il est plus simple qu'il n'en a
l'air (cela s'appelle faire une analyse !)""")

age = st.text_input("Entrez votre age")
asPermis = st.text_input("Avez-vous le permis Y or N")
since = st.text_input("Depuis combien d'annees ?")
accidents = st.text_input("Combien d'accidents avez-vous eu ?")
confirm_5_3_7 = st.button("Confirm", key=7)

if confirm_5_3_7:
    Algo_part_5.get_assurance_price(age,asPermis,since,accidents)