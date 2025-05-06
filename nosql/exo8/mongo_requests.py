from bdd_connect import MongoDB
from pymongo.errors import PyMongoError

def get_adresse_paris():
    try:
        col = MongoDB.get_col("adresse_paris", "adresse")
        if col is None:
            print("Impossible de récupérer la collection 'adresse' de 'adresse_paris'")
            return []
        return list(col.find())
    except PyMongoError as e:
        print(f"Erreur lors de la récupération des adresses de Paris : {e}")
        return []

def get_adresse_paris_tour():
    try:
        col = MongoDB.get_col("adresse_paris_tour", "adresse_tour")
        if col is None:
            print("Impossible de récupérer la collection 'adresse' de 'adresse_paris_tour'")
            return []
        return list(col.find())
    except PyMongoError as e:
        print(f"Erreur lors de la récupération des adresses de Paris (tour) : {e}")
        return []
