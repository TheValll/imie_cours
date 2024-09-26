# 1.2
#  Si une année n'est pas multiple de 4, elle n'est pas bissextile.
#  Si elle est multiple de 4, on regarde si elle est multiple de 100.
#  Si c'est le cas, on regarde si elle est multiple de 400.
#  Si c'est le cas, l'année est bissextile.
#  Sinon, elle n'est pas bissextile.
#  Sinon, elle est bissextile.


print("Resultat algo 1.2")

def get_leap_year():
    year = input("Entrez une année : ")

    if year:
        try:
            year = int(year)

            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                bissextile = True
                print(f"Is {year} a leap year ? : {bissextile}")
            else:
                bissextile = False
                print(f"Is {year} a leap year ? : {bissextile}")

        except ValueError:
            print("Le format de vos saisies sont incorrect entrez un nombre")
            get_leap_year()
    else:
        print("user input not found")

get_leap_year()