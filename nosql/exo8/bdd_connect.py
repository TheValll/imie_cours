import pymongo
from pymongo.errors import ConnectionFailure, ConfigurationError, PyMongoError

class MongoDB:

    @staticmethod
    def get_client():
        try:
            myclient = pymongo.MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=5000)
            myclient.admin.command('ping')
            return myclient
        except (ConnectionFailure, ConfigurationError) as e:
            print(f"Erreur de connexion à MongoDB : {e}")
            return None

    @staticmethod
    def get_db(db_name):
        try:
            myclient = MongoDB.get_client()
            if myclient is None:
                return None
            mydb = myclient[db_name]
            return mydb
        except PyMongoError as e:
            print(f"Erreur lors de la récupération de la base de données '{db_name}' : {e}")
            return None

    @staticmethod
    def get_col(db_name, col_name):
        try:
            mydb = MongoDB.get_db(db_name)
            if mydb is None:
                return None
            mycol = mydb[col_name]
            return mycol
        except PyMongoError as e:
            print(f"Erreur lors de la récupération de la collection '{col_name}' dans la base '{db_name}' : {e}")
            return None