-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : lun. 21 nov. 2022 à 19:49
-- Version du serveur : 8.0.31
-- Version de PHP : 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `medical`
--
create database if not exists medical;
use medical;
-- --------------------------------------------------------

--
-- Structure de la table `consultation_fin`
--

DROP TABLE IF EXISTS `consultation_fin`;
CREATE TABLE IF NOT EXISTS `consultation_fin` (
  `id_consultation` int NOT NULL AUTO_INCREMENT,
  `id_patient` int DEFAULT NULL,
  `consultation_final` text COLLATE utf8mb4_general_ci,
  `ordonnance` text COLLATE utf8mb4_general_ci,
  `situation_dossier` char(15) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id_consultation`),
  KEY `fk_info_patient` (`id_patient`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `consultation_initial`
--

DROP TABLE IF EXISTS `consultation_initial`;
CREATE TABLE IF NOT EXISTS `consultation_initial` (
  `id_consiltation_inial` int NOT NULL AUTO_INCREMENT,
  `poids` float NOT NULL,
  `taille` float NOT NULL,
  `temperature` int NOT NULL,
  `Glycemie` float NOT NULL,
  `pression` float NOT NULL,
  `allergie` char(3) COLLATE utf8mb4_general_ci NOT NULL,
  `imc` char(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `douleur` char(3) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `maladies_chroniques` char(3) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `interpretation_imc` char(30) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id_consiltation_inial`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `consultation_initial`
--

INSERT INTO `consultation_initial` (`id_consiltation_inial`, `poids`, `taille`, `temperature`, `Glycemie`, `pression`, `allergie`, `imc`, `douleur`, `maladies_chroniques`, `interpretation_imc`) VALUES
(1, 11, 11, 11, 11, 1111, '11', 'oui', 'oui', 'oui', NULL),
(2, 63, 1, 37, 1, 11, '13', 'non', 'oui', 'oui', NULL),
(3, 60, 1, 37, 1, 14, '11', 'oui', 'oui', 'oui', NULL),
(4, 63, 1, 35, 2, 13, 'oui', '11', 'oui', 'oui', NULL),
(5, 60, 1, 36, 2, 14, 'oui', '60.0', 'oui', 'oui', NULL),
(6, 60, 1, 36, 2, 12, 'oui', '60.0', 'non', 'oui', 'Obésité morbide ou massive'),
(7, 50, 1, 36, 1, 2, 'oui', '50.0', 'oui', 'non', 'Obésité morbide ou massive'),
(8, 50, 1, 36, 2, 12, 'oui', '50.0', 'oui', 'oui', 'Obésité morbide ou massive'),
(9, 50, 1, 36, 1.3, 15, 'oui', '50.0', 'non', 'oui', 'Obésité morbide ou massive'),
(10, 50, 1, 36, 2, 15, 'oui', '50.0', 'oui', 'oui', 'Obésité morbide ou massive'),
(11, 40, 1, 36, 2, 13, 'oui', '40.0', 'oui', 'oui', 'Obésité morbide ou massive'),
(12, 65, 1.78, 36, 13, 12.5, 'non', '65.0', 'oui', 'oui', 'Obésité morbide ou massive'),
(13, 64, 1.78, 36, 1.3, 14.2, 'oui', '64.0', 'oui', 'non', 'Obésité morbide ou massive'),
(14, 64, 1.78, 35, 1.4, 14.2, 'non', '20.199469763918696', 'oui', 'non', 'Corpulence normale');

-- --------------------------------------------------------

--
-- Structure de la table `info_patient`
--

DROP TABLE IF EXISTS `info_patient`;
CREATE TABLE IF NOT EXISTS `info_patient` (
  `id_patient` int NOT NULL AUTO_INCREMENT,
  `datenaiss` date DEFAULT NULL,
  `age` int DEFAULT NULL,
  `grps` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `situation_fam` char(15) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `email` char(35) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `numero_tel` char(14) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `add_patient` char(25) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `note` char(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `sexe` char(9) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `nom_prenom` char(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id_patient`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `info_patient`
--

INSERT INTO `info_patient` (`id_patient`, `datenaiss`, `age`, `grps`, `situation_fam`, `email`, `numero_tel`, `add_patient`, `note`, `sexe`, `nom_prenom`) VALUES
(1, '2015-05-20', 19, 'A', 'cele', 'taha@taha', '060606060', 'casa', 'aucune', 'Male', 'xxxxx'),
(2, '2015-05-20', 40, 'A', 'Marie', 'mohammed@mohammed', '0606060606', 'casa', 'none', 'Male', 'Mohammed ouad'),
(3, '1999-11-09', 23, 'A+', 'Cele', 'achraf@achraf', '0607070809', 'bouznika', '', 'Male', 'Achraf allaoui');

-- --------------------------------------------------------

--
-- Structure de la table `utilisateurs`
--

DROP TABLE IF EXISTS `utilisateurs`;
CREATE TABLE IF NOT EXISTS `utilisateurs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(25) NOT NULL,
  `email` varchar(50) NOT NULL,
  `numero` varchar(10) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `utilisateurs`
--

INSERT INTO `utilisateurs` (`id`, `nom`, `email`, `numero`, `password`) VALUES
(1, 'admin', 'admin@admin.com', '0655448821', '1234'),
(2, 'reception', 'Khadija@khadija', '0603040506', '5678'),
(3, 'Docteur', 'taha@taha.com', '0687784420', '1508');

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `consultation_fin`
--
CREATE TABLE IF NOT EXISTS consultation_fin (id_consultation INT PRIMARY KEY AUTO_INCREMENT, id_patient INT, consultation_final TEXT, ordonnance TEXT, situation_dossier CHAR(15) NOT NULL, constraint fk_info_patient FOREIGN KEY(id_patient) REFERENCES info_patient(id_patient) on delete cascade);


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
