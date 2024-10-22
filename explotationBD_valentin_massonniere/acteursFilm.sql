-- phpMyAdmin SQL Dump
-- version 3.4.5
-- http://www.phpmyadmin.net
--
-- Client: localhost
-- Généré le : Lun 16 Janvier 2012 à 16:41
-- Version du serveur: 5.5.16
-- Version de PHP: 5.3.8

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données: `acteurFilm`
--

-- --------------------------------------------------------

--
-- Structure de la table `acteurs`
--
drop table if EXISTS `acteurs` ;
CREATE TABLE IF NOT EXISTS `acteurs` (
   id      Int  Auto_increment  NOT NULL ,
  `NomActeur` char(32) NOT NULL DEFAULT '',
  `PrenomActeur` char(32) NOT NULL DEFAULT '',
  `DateNaissanceActeur` varchar(32) DEFAULT NULL,
  `PaysActeur` varchar(16) DEFAULT NULL,
  CONSTRAINT acteurs_PK PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `acteurs`
--

INSERT INTO `acteurs` (`NomActeur`, `PrenomActeur`, `DateNaissanceActeur`, `PaysActeur`) VALUES
('Bale', 'Christian', '30 janvier 1974', 'Angleterre'),
('Bean', 'Sean', '17 avril 1959', 'Angleterre'),
('Cage', 'Nicolas', '7 janvier 1964', 'USA'),
('Caine', 'Michael', '14 mars 1933', 'Angleterre'),
('Connery', 'Sean', '25 aout 1930', 'Angleterre'),
('Cotillard', 'Marion', '30 septembre 1975', 'France'),
('Depardieu', 'Gerard', '27 decembre 1948', 'France'),
('Diaz', 'Cameron', '30 aout 1972', 'USA'),
('DiCaprio', 'Leonardo', '11 novembre 1974', 'USA'),
('Fox', 'Megan', '16 mai 1986', 'USA'),
('Jackman', 'Hugh', '12 octobre 1968', 'Australie'),
('Johansson', 'Scarlett', '22 novembre 1984', 'USA'),
('LaBeouf', 'Shia', '11 juin 1986', 'USA'),
('MacDowell', 'Andie', '21 avril 1958', 'USA'),
('MacGregor', 'Ewan', '31 mars 1971', 'Angleterre'),
('Marsden', 'James', '18 septembre 1973', 'USA'),
('Murray', 'Bill', '21 septembre 1950', 'USA'),
('Prime', 'Optimus', 'Inconnue', 'Cybertron'),
('Wilson', 'Lambert', '3 aout 1958', 'France'),
('Worthington', 'Sam', '2 aout 1976', 'USA');

-- --------------------------------------------------------

--
-- Structure de la table `film`
--
drop table if EXISTS `film` ;
CREATE TABLE IF NOT EXISTS `film` (
   id      Int  Auto_increment  NOT NULL ,
  `TitreFilm` char(64) NOT NULL,
  `GenreFilm` varchar(32) DEFAULT NULL,
  `Pays` varchar(16) DEFAULT NULL,
  `AnneeSortie` int(11) DEFAULT NULL,
  `NomRealisateur` char(32) DEFAULT NULL,
  `PrenomRealisateur` char(32) DEFAULT NULL,
  `Budget` int(11) DEFAULT NULL,
  CONSTRAINT film_PK PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `film`
--

INSERT INTO `film` (`TitreFilm`, `GenreFilm`, `Pays`, `AnneeSortie`, `NomRealisateur`, `PrenomRealisateur`, `Budget`) VALUES
('Equilibrium', 'Fantastique', 'USA', 2003, 'Wimmer', 'Kurt', 20),
('Freddy - les griffes de la nuit', 'Horreur', 'USA', 2010, 'Bay', 'Michael', 35),
('Ghost rider', 'Fantastique', 'USA', 2007, 'Johnson', 'Mark', 110),
('Il etait une fois', 'Comedie', 'USA', 2007, 'Lima', 'Kevin', 85),
('Inception', 'Fantastique', 'USA', 2010, 'Nolan', 'Christopher', 160),
('Jennifers body', 'Horreur', 'USA', 2009, 'Kusama', 'Karyn', 16),
('Le prestige', 'Fantastique', 'USA', 2006, 'Nolan', 'Christopher', 40),
('Lhomme au masque de fer', 'Action', 'Angleterre', 1998, 'Wallace', 'Randall', 35),
('Matrix reloaded', 'Fantastique', 'USA', 2003, 'Wachowski', 'Freres', 138),
('Rock', 'Action', 'USA', 1996, 'Bay', 'Michael', 75),
('Terminator renaissance', 'Fantastique', 'USA', 2009, 'MacGinty', 'Joseph', 200),
('The Box', 'Fantastique', 'USA', 2009, 'Kelly', 'Richard', 27),
('The island', 'Fantastique', 'USA', 2005, 'Bay', 'Michael', 126),
('Transformers', 'Fantastique', 'USA', 2007, 'Bay', 'Michael', 150),
('Transformers 2 : la revanche', 'Fantastique', 'USA', 2009, 'Bay', 'Michael', 200),
('Un jour sans fin', 'Comedie', 'USA', 1993, 'Ramis', 'Harold', 14),
('Vendredi 13', 'Horreur', 'USA', 2009, 'Bay', 'Michael', 19),
('Xmen origins : Wolverine', 'Fantastique', 'USA', 2009, 'Hood', 'Gavin', 150);

-- --------------------------------------------------------

--
-- Structure de la table `realisateur`
--
drop table if EXISTS `realisateur` ;
CREATE TABLE IF NOT EXISTS `realisateur` (
   id      Int  Auto_increment  NOT NULL ,
  `NomRealisateur` char(32) NOT NULL DEFAULT '',
  `PrenomRealisateur` char(32) NOT NULL DEFAULT '',
  `DateNaissanceRealisateur` varchar(16) DEFAULT NULL,
  `NombreFilm` int(11) DEFAULT NULL,
  CONSTRAINT realisateur_PK PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `realisateur`
--

INSERT INTO `realisateur` (`NomRealisateur`, `PrenomRealisateur`, `DateNaissanceRealisateur`, `NombreFilm`) VALUES
('Bay', 'Michael', '17 fevrier 1965', 6),
('Hood', 'Gavin', '12 mai 1963', 1),
('Johnson', 'Mark', '30 octobre 1964', 1),
('Kelly', 'Richard', '28 mars 1975', 1),
('Kusama', 'Karyn', '21 mars 1968', 1),
('Lima', 'Kevin', '1962', 1),
('MacGinty', 'Joseph', '9 aout 1968', 1),
('Nolan', 'Christopher', '30 juillet 1970', 2),
('Ramis', 'Harold', '21 novembre 1944', 1),
('Wachowski', 'Freres', 'Non communiquee', 1),
('Wallace', 'Randall', '1949', 1),
('Wimmer', 'Kurt', 'Non communiquee', 1);

-- --------------------------------------------------------

--
-- Structure de la table `role`
--
drop table if EXISTS `role` ;
CREATE TABLE IF NOT EXISTS `role` (
   id      Int  Auto_increment  NOT NULL ,
  `TitreFilm` char(64) NOT NULL DEFAULT '',
  `NomActeur` char(32) NOT NULL DEFAULT '',
  `PrenomActeur` char(32) NOT NULL DEFAULT '',
  `RoleFilm` varchar(64) DEFAULT NULL,
  `SalaireFilm` int(11) DEFAULT NULL,
  CONSTRAINT role_PK PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `role`
--

INSERT INTO `role` (`TitreFilm`, `NomActeur`, `PrenomActeur`, `RoleFilm`, `SalaireFilm`) VALUES
('Equilibrium', 'Bale', 'Christian', 'John Preston', 760),
('Equilibrium', 'Bean', 'Sean', 'Partridge', 60),
('Ghost rider', 'Cage', 'Nicolas', 'Johnny Blaze', 15000),
('Il etait une fois', 'Marsden', 'James', 'Le prince Edouard', 500),
('Inception', 'Caine', 'Michael', 'Miles', 75),
('Inception', 'Cottillard', 'Marion', 'Mall', 850),
('Inception', 'DiCaprio', 'Leonardo', 'Dom Cobb', 20000),
('Jennifers body', 'Fox', 'Megan', 'Jennifer Check', 11000),
('Le prestige', 'Bale', 'Christian', 'Alfred Borden', 1700),
('Le prestige', 'Caine', 'Michael', 'Cutter', 350),
('Le prestige', 'Jackman', 'Hugh', 'Robert Angier', 1800),
('Le prestige', 'Johansson', 'Scarlett', 'Olivia', 950),
('Lhomme au masque de fer', 'Depardieu', 'Gerard', 'Porthos', 1),
('Lhomme au masque de fer', 'DiCaprio', 'Leonardo', 'Louis XIV', 3500),
('Matrix reloaded', 'Wilson', 'Lambert', 'Le Merovingien', 10000),
('Rock', 'Cage', 'Nicolas', 'Stanley Goodspeed', 1500),
('Rock', 'Connery', 'Sean', 'John Patrick Mason', 6000),
('Terminator renaissance', 'Bale', 'Christian', 'John Connor', 12000),
('Terminator renaissance', 'Worthington', 'Sam', 'Marcus Wright', 9000),
('The Box', 'Diaz', 'Cameron', 'Norma Lewis', 3000),
('The Box', 'Marsden', 'James', 'Arthur Lewis', 1000),
('The island', 'Bean', 'Sean', 'Merrick', 150),
('The island', 'Johansson', 'Scarlett', 'Jordan 2delta', 900),
('The island', 'MacGregor', 'Ewan', 'Lincoln 6echo', 2000),
('Transformers', 'Fox', 'Megan', 'Mikaela Banes', 7000),
('Transformers', 'LaBeouf', 'Shia', 'Sam Witwicky', 13000),
('Transformers', 'Prime', 'Optimus', 'Lui-meme', 0),
('Transformers 2 : la revanche', 'Fox', 'Megan', 'Mikaela Banes', 12000),
('Transformers 2 : la revanche', 'LaBeouf', 'Shia', 'Sam Witwicky', 14000),
('Transformers 2 : la revanche', 'Prime', 'Optimus', 'Lui-meme', 0),
('Un jour sans fin', 'MacDowell', 'Andie', 'Rita', 250),
('Un jour sans fin', 'Murray', 'Bill', 'Phil Connors', 600),
('Xmen origins : Wolverine', 'Jackman', 'Hugh', 'Logan', 5000);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
