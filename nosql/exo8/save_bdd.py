from pymongo.errors import PyMongoError, ConnectionFailure
from bdd_connect import MongoDB

def save_bdd(adresses_proches):
    try:
        db = MongoDB.get_db("adresse_finale")
        col_name = "adresses_clean"
        col = MongoDB.get_col("adresse_finale", col_name)

        if col_name in db.list_collection_names():
            db.drop_collection(col_name)
            collection = db[col_name]

            if adresses_proches:
                collection.insert_many(adresses_proches)
                print(f"{len(adresses_proches)} documents insérés dans 'adresse_paris_resultat {col_name}'.")
            else:
                print("Aucun document à insérer ")
    except ConnectionFailure as e:
        print(f"Échec de la connexion à MongoDB : {e}")
    except PyMongoError as e:
        print(f"Erreur lors de l'insertion dans la base de données : {e}")
