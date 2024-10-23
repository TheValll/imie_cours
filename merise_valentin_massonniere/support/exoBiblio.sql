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
        id_emprunt   Int  Auto_increment  NOT NULL ,
        date_emprunt Date NOT NULL
	,CONSTRAINT Emprunt_PK PRIMARY KEY (id_emprunt)
)ENGINE=InnoDB;

#------------------------------------------------------------
# Table: Emprunter
#------------------------------------------------------------

CREATE TABLE DemandeEmprunt(
        id_emprunt              Int NOT NULL ,
        id_adherent             Int NOT NULL ,
        nombre_exemplaire_livre Int NOT NULL
	,CONSTRAINT Emprunter_PK PRIMARY KEY (id_emprunt,id_adherent)

	,CONSTRAINT Emprunter_Emprunt_FK FOREIGN KEY (id_emprunt) REFERENCES Emprunt(id_emprunt)
	,CONSTRAINT Emprunter_Adherent0_FK FOREIGN KEY (id_adherent) REFERENCES Adherent(id_adherent)
)ENGINE=InnoDB;

