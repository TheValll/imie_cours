insert into `Adherent` (`id_adherent`, `nom_adherent`, `numero_rue`, `rue`, `code_postale`, `ville`) values (002, 'John', '3', 'rue XX', '75001', 'Paris')

insert into `Auteur` (`id_auteur`, `nom_auteur`) values (001, 'Moliere');

insert into `Auteur` (`id_auteur`, `nom_auteur`) values (120, 'Hugo');

insert into `Editeur` (`id_editeur`, `nom_editeur`) values (1, 'Gallimard');

insert into `Editeur` (`id_editeur`, `nom_editeur`) values (2, 'Laffont');

insert into `Collection` (`id_collection`, `nom_collection`, `id_editeur`) values (001, 'Pleiade', 01)

insert into `Collection` (`id_collection`, `nom_collection`, `id_editeur`) values (002, 'Folio', 01)

insert into `Collection` (`id_collection`, `nom_collection`, `id_editeur`) values (003, 'Ailleurs', 02)

insert into `Emprunt` (`id_emprunt`, `date_emprunt`) values (001, '15/01/2020')

insert into `Emprunt` (`id_emprunt`, `date_emprunt`) values (002, '19/01/2020')

insert into `Emprunt` (`id_emprunt`, `date_emprunt`) values (007, '22/01/2020')