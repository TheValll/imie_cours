import streamlit as st

from utils import NewPage
from utils import Algo_part_4

NewPage.main("Algo ui", "wide", "auto")

# Section 4

st.write("Algo part 4")
st.write(f"""Enoncé : \n
4.2.2 Ecrire un programme qui demande un nombre à l’utilisateur, puis qui calcule et affiche le carré de ce nombre. 
Indices : Pour convertir la chaîne « 123 » en nombre 123 écrire : 
Val = int(“123”) 
Pour élever A à la puissance B : A ** B""")

input_4_2_2 = st.text_input("Entrez un nombre")
confirm_4_2_2 = st.button("Confirm", key=1)

if confirm_4_2_2:
    Algo_part_4.square_number(input_4_2_2)


st.write(f"""Enoncé : \n
4.2.3
Ecrire un programme qui lit le prix HT d’un article, le nombre d’articles et le taux de
TVA, et qui fournit le prix total TTC correspondant.
Faire en sorte que des libellés apparaissent clairement. Ex
Prix total 10.30 €""")

ht_price = st.text_input("Entrez un HT")
nb_article = st.text_input("Entrez un nombre de produit")
tva_rate = st.text_input("Entrez une TVA")
confirm_4_2_3_2 = st.button("Confirm", key=2)

if confirm_4_2_3_2:
    Algo_part_4.calculate_ttc(ht_price, nb_article, tva_rate)