import os

def get_file(folder_path=None):
    if folder_path is None:
        print("Ajouter un chemin en paramètre pour afficher tous les fichiers sous ce chemin")
        return

    try:
        if not os.path.isdir(folder_path):
            print(f"Le chemin '{folder_path}' n'est pas un répertoire valide.")
            return
        
        for path, dirs, files in os.walk(folder_path): 
            for filename in files:
                print(f"Path : {path}, File : {filename}")
                
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

get_file("C:/Users/Valentin/Documents/imie_cours")
get_file()