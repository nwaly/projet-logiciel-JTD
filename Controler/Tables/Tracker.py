"""table tracker
-- -----------------------------------------------------
-- Table `mydb`.`Tracker`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Tracker` (
  `Tracker_ID` INT NOT NULL,
  `Tracker_nom` TINYTEXT NOT NULL,
  `Tracker_description` MEDIUMTEXT NOT NULL,
  `Tracker_couleur` ENUM("rouge", "orange", "jaune", "vert", "bleu", "violet", "rose") NOT NULL,
  `Tracker_icone` ENUM("rond", "carré", "triangle", "goute", "livre", "lune", "sport", "none") NOT NULL DEFAULT '\"none\"',
  PRIMARY KEY (`Tracker_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Calendrier`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Calendrier` (
  `Calendrier_ID` INT NOT NULL,
  `Calendrier_jour` DATE NOT NULL,
  PRIMARY KEY (`Calendrier_ID`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`Calendrier_has_Tracker`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Calendrier_has_Tracker` (
  `Calendrier_Calendrier_ID` INT NOT NULL,
  `Tracker_Tracker_ID` INT NOT NULL,
  `Calendrier_has_Tracker_Statut` TINYINT(1) NULL,
  PRIMARY KEY (`Calendrier_Calendrier_ID`, `Tracker_Tracker_ID`),
  INDEX `fk_Calendrier_has_Tracker_Tracker1_idx` (`Tracker_Tracker_ID` ASC) VISIBLE,
  INDEX `fk_Calendrier_has_Tracker_Calendrier1_idx` (`Calendrier_Calendrier_ID` ASC) VISIBLE,
  CONSTRAINT `fk_Calendrier_has_Tracker_Calendrier1`
    FOREIGN KEY (`Calendrier_Calendrier_ID`)
    REFERENCES `mydb`.`Calendrier` (`Calendrier_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Calendrier_has_Tracker_Tracker1`
    FOREIGN KEY (`Tracker_Tracker_ID`)
    REFERENCES `mydb`.`Tracker` (`Tracker_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;"""

class Tracker ():
    """classe tracker"""
    def __init__(self, base):
        self.base = base

