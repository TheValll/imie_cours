#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------


#------------------------------------------------------------
# Table: Article
#------------------------------------------------------------

CREATE TABLE Article(
        id_article   Int  Auto_increment  NOT NULL ,
        nom_article  Varchar (50) NOT NULL ,
        prix_article Float NOT NULL
	,CONSTRAINT Article_PK PRIMARY KEY (id_article)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Facture
#------------------------------------------------------------

CREATE TABLE Facture(
        id_facture   Int  Auto_increment  NOT NULL ,
        date_facture Date NOT NULL
	,CONSTRAINT Facture_PK PRIMARY KEY (id_facture)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Commande
#------------------------------------------------------------

CREATE TABLE Commande(
        id_facture       Int NOT NULL ,
        id_article       Int NOT NULL ,
        quantite_article Int NOT NULL
	,CONSTRAINT Commande_PK PRIMARY KEY (id_facture,id_article)

	,CONSTRAINT Commande_Facture_FK FOREIGN KEY (id_facture) REFERENCES Facture(id_facture)
	,CONSTRAINT Commande_Article0_FK FOREIGN KEY (id_article) REFERENCES Article(id_article)
)ENGINE=InnoDB;