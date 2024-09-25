# Import the required libraries
import os
import sys
main_path = os.path.abspath(__file__ + "../")
sys.path.append(main_path)
import streamlit as st
from datetime import datetime, timedelta, time

class NewPage:

    # Set up a streamlit page
    # Parameters:
    # favicon: The favicon of the page
    # title: The title of the page
    # layout: The layout of the page
    # initial_sidebar_state: The initial sidebar state of the page

    def main(title, layout, initial_sidebar_state):
        st.set_page_config(
            page_title=f"{title}", 
            layout=f"{layout}", 
            initial_sidebar_state=f"{initial_sidebar_state}",
        )

    # Hide streamlit menu (hamburger) and footer
    def hide_streamlit_menu():
        padding_top=0
        hide_streamlit_style = f"""
        <style>
        #MainMenu {{visibility: hidden;}}
        .appview-container .main .block-container{{padding-top: {padding_top}rem;}}
        footer {{visibility: hidden;}}
        </style>
        """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

    # Add a title at the page
    def title_page(title):
        st.markdown(f"<h1 style='color: #12BBEF;'>{title}</h1>", unsafe_allow_html=True)


class Algo_part_4:

    def square_number(input):
        if input:
            try:
                result = pow(int(input),2)
                st.write(f"Le résultat est {result}")
            except:
                st.error("Ceci n'est pas un nombre")
        else:
            st.error("user input not found")


    def calculate_ttc(ht_price, nb_article, tva_rate):

        if ht_price and nb_article and tva_rate:
            try:
                result = round((int(ht_price) * int(tva_rate) / 100) * int(nb_article), 2)
                st.write(f"Le prix total est de {result} e")
            except:
                st.error("Le format de vos saisies sont incorrect entrez des nombres")
        else:
            st.error("user input not found")


class Algo_part_5:
    def get_product_sign(a,b):

        if a and b:
            try:
                a = int(a)
                b = int(b)

                if a > 0 and b > 0:
                    st.write("Le produit des deux nombres est positif")
                elif a > 0 and b < 0:
                    st.write("Le produit des deux nombres est négatif")
                elif a < 0 and b < 0:
                    st.write("Le produit des deux nombres est négatif")
                else:
                    st.write("Le produit des deux nombres est positif")
            except:
                st.error("Le format de vos saisies sont incorrect entrez des nombres")
        else:
            st.error("user input not found")

    
    def get_cinema_ticket_price(age, card):

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

                st.write(f"Le prix est de {price} e")
            except:
                st.error("Le format de vos saisies sont incorrect entrez un nombre ou insérer Y ou N pour indiquer si vous avez la carte du cinéma")
        else:
            st.error("user input not found")

    
    def get_leap_year(year):
        if year:
            try:
                year = int(year)

                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    st.write("L'année est bissextile")
                else:
                    st.write("L'année n'est pas bissextile")

            except:
                st.error("Le format de vos saisies sont incorrect entrez un nombre")
        else:
            st.error("user input not found")
    

    def predict_hours(hours, minutes):
        if hours and minutes:
            try:
                hours = int(hours)
                minutes = int(minutes)

                if hours >= 24 or hours < 0 or minutes >= 60 or minutes < 0:
                    raise Exception
                
                user_time = datetime.combine(datetime.today(), time(hours, minutes))
                preddict_time = user_time + timedelta(minutes=1)

                if preddict_time.hour > 1:
                    st.write(f"Dans une minute, il sera {preddict_time.hour} heures et {preddict_time.minute}")
                else:
                    st.write(f"Dans une minute, il sera {preddict_time.hour} heure et {preddict_time.minute}")

            except Exception:
                st.error("Le format de vos saisies est incorrect entrez des heures et minutes valides")
        else:
            st.error("user input not found")


    def get_invoice(nb_paper):
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

                st.write(f"La facture est de {round(invoice, 2)} e")

            except:
                st.error("Le format de vos saisies est incorrect entrez un nombre")
        else:
            st.error("user input not found")

    
    def get_assurance_price(age, asPermis, since, accidents):

        if asPermis == "N":
            st.write("Vous ne pouvez pas vous inscrire sans permis")
            return
        
        if age and asPermis and since and accidents:
            
            try:
                age = int(age)
                since = int(since)
                accidents = int(accidents)

                if accidents > 2:
                    st.write("Vous ne pouvez pas vous inscrire avec plus de 2 accidents")
                    return

                if age < 25 and since < 2 and accidents > 0:
                    st.write("Vous ne pouvez pas vous inscrire avec un accident")
                    return

                if age < 25 and since < 2:
                    st.write("Vous êtes éligible au tarif rouge")
                elif (age < 25 and since >= 2) or (age >= 25 and since < 2):
                    st.write("Vous êtes éligible au tarif orange" if accidents == 0 else "Vous êtes éligible au tarif rouge")
                elif age >= 25 and since >= 2:
                    st.write("Vous êtes éligible au tarif vert" if accidents == 0 else "Vous êtes éligible au tarif orange")
            except:
                st.error("Le format de vos saisies sont incorrect entrez les valeurs correctement")

        else:
            st.error("user input not found")
