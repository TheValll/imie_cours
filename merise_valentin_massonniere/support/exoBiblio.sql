#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------


#------------------------------------------------------------
# Table: Adherent
#------------------------------------------------------------

CREATE TABLE Adherent(
        id_adherent  Int  Auto_increment  NOT NULL ,
        nom_adherent Varchar (50) NOT NULL ,
        numero_rue   Int NOT NULL ,
        rue          Varchar (50) NOT NULL ,
        code_postale Int NOT NULL ,
        ville        Varchar (50) NOT NULL
	,CONSTRAINT Adherent_PK PRIMARY KEY (id_adherent)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Editeur
#------------------------------------------------------------

CREATE TABLE Editeur(
        id_editeur  Int  Auto_increment  NOT NULL ,
        nom_editeur Varchar (50) NOT NULL
	,CONSTRAINT Editeur_PK PRIMARY KEY (id_editeur)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Collection
#------------------------------------------------------------

CREATE TABLE Collection(
        id_collection  Int  Auto_increment  NOT NULL ,
        nom_collection Varchar (50) NOT NULL ,
        id_editeur     Int NOT NULL
	,CONSTRAINT Collection_PK PRIMARY KEY (id_collection)

	,CONSTRAINT Collection_Editeur_FK FOREIGN KEY (id_editeur) REFERENCES Editeur(id_editeur)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Auteur
#------------------------------------------------------------

CREATE TABLE Auteur(
        id_auteur  Int  Auto_increment  NOT NULL ,
        nom_auteur Varchar (50) NOT NULL
	,CONSTRAINT Auteur_PK PRIMARY KEY (id_auteur)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Livre
#------------------------------------------------------------

CREATE TABLE Livre(
        id_livre    Int  Auto_increment  NOT NULL ,
        code_livre  Int NOT NULL ,
        titre_livre Varchar (50) NOT NULL
	,CONSTRAINT Livre_PK PRIMARY KEY (id_livre)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Emprunt
#------------------------------------------------------------

CREATE TABLE Emprunt(
        id_emprunt         Int  Auto_increment  NOT NULL ,
        date_emprunt       Date NOT NULL ,
        quantite_emprunter Int NOT NULL ,
        id_adherent        Int NOT NULL ,
        id_collection      Int NOT NULL
	,CONSTRAINT Emprunt_PK PRIMARY KEY (id_emprunt)

	,CONSTRAINT Emprunt_Adherent_FK FOREIGN KEY (id_adherent) REFERENCES Adherent(id_adherent)
	,CONSTRAINT Emprunt_Collection0_FK FOREIGN KEY (id_collection) REFERENCES Collection(id_collection)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Ecrire
#------------------------------------------------------------

CREATE TABLE Ecrire(
        id_livre  Int NOT NULL ,
        id_auteur Int NOT NULL
	,CONSTRAINT Ecrire_PK PRIMARY KEY (id_livre,id_auteur)

	,CONSTRAINT Ecrire_Livre_FK FOREIGN KEY (id_livre) REFERENCES Livre(id_livre)
	,CONSTRAINT Ecrire_Auteur0_FK FOREIGN KEY (id_auteur) REFERENCES Auteur(id_auteur)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Posseder
#------------------------------------------------------------

CREATE TABLE Posseder(
        id_collection           Int NOT NULL ,
        id_livre                Int NOT NULL ,
        nombre_exemplaire_livre Int NOT NULL
	,CONSTRAINT Posseder_PK PRIMARY KEY (id_collection,id_livre)

	,CONSTRAINT Posseder_Collection_FK FOREIGN KEY (id_collection) REFERENCES Collection(id_collection)
	,CONSTRAINT Posseder_Livre0_FK FOREIGN KEY (id_livre) REFERENCES Livre(id_livre)
)ENGINE=InnoDB;

