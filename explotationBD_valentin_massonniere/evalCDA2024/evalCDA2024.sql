-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  jeu. 28 jan. 2021 à 15:03
-- Version du serveur :  5.7.26
-- Version de PHP :  7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  evalCDA2024
--
DROP DATABASE IF EXISTS evalCDA2024 ;
CREATE DATABASE IF NOT EXISTS evalCDA2024 DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE evalCDA2024;

-- --------------------------------------------------------

--
-- Structure de la table fabricant
--

DROP TABLE IF EXISTS fabricant;
CREATE TABLE IF NOT EXISTS fabricant (
  id int(11) NOT NULL AUTO_INCREMENT,
  nom varchar(50) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table fabricant
--

INSERT INTO fabricant (id, nom) VALUES
(1, 'Netgear'),
(2, 'Cisco'),
(3, 'Startech'),
(4, 'Anteor'),
(5, 'Systolic'),
(6, 'Plecom'),
(7, 'Siemens');

-- --------------------------------------------------------

--
-- Structure de la table materiel
--

DROP TABLE IF EXISTS materiel;
CREATE TABLE IF NOT EXISTS materiel (
  id int(11) NOT NULL AUTO_INCREMENT,
  nom varchar(50) NOT NULL,
  description text NOT NULL,
  dateInstallation date NOT NULL,
  id_Fabricant int(11) NOT NULL,
  id_Responsable int(11) DEFAULT NULL,
  PRIMARY KEY (id),
  KEY Materiel_Fabricant_FK (id_Fabricant),
  KEY Materiel_Responsable0_FK (id_Responsable)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table materiel
--

INSERT INTO materiel (id, nom, description, dateInstallation, id_Fabricant, id_Responsable) VALUES
(1, 'Switch', 'Switch Gigabit, Cisco, SG110-16, 16 ports', '2021-01-10', 2, 1),
(2, 'Switch', 'Switch Gigabit, Cisco, SG110-24, 24 ports', '2020-12-13', 2, 2),
(3, 'MFax150', 'Serveur de fax MFax150', '2020-08-09', 6, 7),
(4, 'Routeur', 'Routeur 4G de GENEKO', '2020-09-07', 6, 6),
(5, 'Passerelle GSM', 'Passerelle GSM analogique 2GSMGate', '2019-01-26', 6, 7),
(6, 'Serveur', 'Serveur Lame XT 5612', '2012-01-25', 4, 4),
(7, 'Rack serveur', 'Rack pour application réseau - 6 ports Lan - 1U 6Lan LCD Core2Duo', '2011-01-25', 4, 5),
(8, 'Serveur', 'Serveur PRIMERGY Econel 200 S2', '2002-01-25', 7, 2),
(9, 'Station', 'PC SIMATIC WinAC RTX pour automtisme embarqué', '2013-01-25', 7, 7);

-- --------------------------------------------------------

--
-- Structure de la table responsable
--

DROP TABLE IF EXISTS responsable;
CREATE TABLE IF NOT EXISTS responsable (
  id int(11) NOT NULL AUTO_INCREMENT,
  nom varchar(50) NOT NULL,
  service varchar(50) NOT NULL,
  embauche date NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table responsable
--

INSERT INTO responsable (id, nom, service, embauche) VALUES
(1, 'Smith', 'D11', '2000-11-01'),
(2, 'ManuBoy', 'D11', '1990-12-20'),
(3, 'Warwick', 'D21', '1980-11-01'),
(4, 'Mayuko', 'D21', '1995-11-01'),
(5, 'Shahaf', 'D22', '1999-11-01'),
(6, 'Zvonko', 'D23', '2012-01-01'),
(7, 'Gino', 'D24', '2014-11-01');

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table materiel
--
ALTER TABLE materiel
  ADD CONSTRAINT Materiel_Fabricant_FK FOREIGN KEY (id_Fabricant) REFERENCES fabricant (id),
  ADD CONSTRAINT Materiel_Responsable0_FK FOREIGN KEY (id_Responsable) REFERENCES responsable (id);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
