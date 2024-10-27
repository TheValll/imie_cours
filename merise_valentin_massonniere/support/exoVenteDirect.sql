#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------


#------------------------------------------------------------
# Table: Aimal
#------------------------------------------------------------

CREATE TABLE Aimal(
        id_animal   Int  Auto_increment  NOT NULL ,
        nom_animal  Varchar (50) NOT NULL ,
        prix_animal Int NOT NULL
	,CONSTRAINT Aimal_PK PRIMARY KEY (id_animal)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Legume
#------------------------------------------------------------

CREATE TABLE Legume(
        id_legume   Int  Auto_increment  NOT NULL ,
        nom_legume  Varchar (50) NOT NULL ,
        prix_legume Int NOT NULL
	,CONSTRAINT Legume_PK PRIMARY KEY (id_legume)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Fruit
#------------------------------------------------------------

CREATE TABLE Fruit(
        id_fruit   Int  Auto_increment  NOT NULL ,
        nom_fruit  Varchar (50) NOT NULL ,
        prix_fruit Int NOT NULL
	,CONSTRAINT Fruit_PK PRIMARY KEY (id_fruit)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Commande
#------------------------------------------------------------

CREATE TABLE Commande(
        id_commande Int  Auto_increment  NOT NULL ,
        date_vente  Date NOT NULL
	,CONSTRAINT Commande_PK PRIMARY KEY (id_commande)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Vendre
#------------------------------------------------------------

CREATE TABLE Vendre(
        id_commande     Int NOT NULL ,
        id_fruit        Int NOT NULL ,
        id_animal       Int NOT NULL ,
        id_legume       Int NOT NULL ,
        quantite_animal Float NOT NULL ,
        quantite_legume Float NOT NULL ,
        quantite_fruit  Float NOT NULL
	,CONSTRAINT Vendre_PK PRIMARY KEY (id_commande,id_fruit,id_animal,id_legume)

	,CONSTRAINT Vendre_Commande_FK FOREIGN KEY (id_commande) REFERENCES Commande(id_commande)
	,CONSTRAINT Vendre_Fruit0_FK FOREIGN KEY (id_fruit) REFERENCES Fruit(id_fruit)
	,CONSTRAINT Vendre_Aimal1_FK FOREIGN KEY (id_animal) REFERENCES Aimal(id_animal)
	,CONSTRAINT Vendre_Legume2_FK FOREIGN KEY (id_legume) REFERENCES Legume(id_legume)
)ENGINE=InnoDB;

