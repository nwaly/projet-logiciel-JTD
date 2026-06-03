-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8mb3 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`calendrier`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`calendrier` (
  `Calendrier_ID` INT NOT NULL,
  `Calendrier_jour` DATE NOT NULL,
  PRIMARY KEY (`Calendrier_ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`tracker`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`tracker` (
  `Tracker_ID` INT NOT NULL,
  `Tracker_nom` TINYTEXT NOT NULL,
  `Tracker_description` MEDIUMTEXT NOT NULL,
  `Tracker_couleur` ENUM('rouge', 'orange', 'jaune', 'vert', 'bleu', 'violet', 'rose') NOT NULL,
  `Tracker_icone` ENUM('rond', 'carré', 'triangle', 'goute', 'livre', 'lune', 'sport', 'none') NOT NULL,
  PRIMARY KEY (`Tracker_ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`calendrier_has_tracker`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`calendrier_has_tracker` (
  `Calendrier_Calendrier_ID` INT NOT NULL,
  `Tracker_Tracker_ID` INT NOT NULL,
  `Calendrier_has_Tracker_Statut` TINYINT(1) NULL DEFAULT NULL,
  PRIMARY KEY (`Calendrier_Calendrier_ID`, `Tracker_Tracker_ID`),
  INDEX `fk_Calendrier_has_Tracker_Tracker1_idx` (`Tracker_Tracker_ID` ASC) VISIBLE,
  INDEX `fk_Calendrier_has_Tracker_Calendrier1_idx` (`Calendrier_Calendrier_ID` ASC) VISIBLE,
  CONSTRAINT `fk_Calendrier_has_Tracker_Calendrier1`
    FOREIGN KEY (`Calendrier_Calendrier_ID`)
    REFERENCES `mydb`.`calendrier` (`Calendrier_ID`),
  CONSTRAINT `fk_Calendrier_has_Tracker_Tracker1`
    FOREIGN KEY (`Tracker_Tracker_ID`)
    REFERENCES `mydb`.`tracker` (`Tracker_ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`journal`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`journal` (
  `Journal_ID` INT NOT NULL AUTO_INCREMENT,
  `Journal_titre` TINYTEXT NOT NULL,
  `Journal_date` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Journal_contenu` MEDIUMTEXT NOT NULL,
  `Journal_modification` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Journal_ID`))
ENGINE = InnoDB
AUTO_INCREMENT = 33
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`parametres`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`parametres` (
  `Parametres_ID` INT NOT NULL,
  `Parametres_affichage` VARCHAR(45) NULL DEFAULT NULL,
  `Parametres_couleur` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`Parametres_ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`tache`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`tache` (
  `Tache_ID` INT NOT NULL AUTO_INCREMENT,
  `Tache_date` DATE NOT NULL,
  `Tache_nom` TINYTEXT NOT NULL,
  `Tache_statut` TINYINT(1) NOT NULL,
  `Tache_sous_tache` TINYINT(1) NOT NULL,
  PRIMARY KEY (`Tache_ID`))
ENGINE = InnoDB
AUTO_INCREMENT = 20
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
