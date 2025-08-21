-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema MusicHall_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema MusicHall_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `MusicHall_db` DEFAULT CHARACTER SET utf8mb4 ;
USE `MusicHall_db`;

-- -----------------------------------------------------
-- Table `MusicHall_db`.`profile`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `MusicHall_db`.`profile` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB;

SELECT * FROM profile;

-- -----------------------------------------------------
-- Table `MusicHall_db`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `MusicHall_db`.`user` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(50) NOT NULL,
  `cpf` VARCHAR(11) NOT NULL,
  `password` VARCHAR(130) NOT NULL,
  `profile_ID` INT NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  UNIQUE INDEX `cpf_UNIQUE` (`cpf` ASC) VISIBLE,
  INDEX `fk_user_profile_idx` (`profile_ID` ASC) VISIBLE,
  CONSTRAINT `fk_user_profile`
    FOREIGN KEY (`profile_ID`)
    REFERENCES `MusicHall_db`.`profile` (`ID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

ALTER TABLE user
ADD COLUMN name_completed VARCHAR(80);

SELECT * FROM user;

-- -----------------------------------------------------
-- Table `MusicHall_db`.`event`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `MusicHall_db`.`event` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `event_name` VARCHAR(45) NOT NULL,
  `limit_peaple` BIGINT NOT NULL,
  `date_event` DATE NOT NULL,
  `hour_event` TIME NOT NULL,
  `description` TEXT(500) NOT NULL,
  `user_ID` INT NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE INDEX `date_event_UNIQUE` (`date_event` ASC) VISIBLE,
  UNIQUE INDEX `hour_event_UNIQUE` (`hour_event` ASC) VISIBLE,
  INDEX `fk_event_user1_idx` (`user_ID` ASC) VISIBLE,
  CONSTRAINT `fk_event_user1`
    FOREIGN KEY (`user_ID`)
    REFERENCES `MusicHall_db`.`user` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

ALTER TABLE event
ADD COLUMN image_event VARCHAR(150);


-- -----------------------------------------------------
-- Table `MusicHall_db`.`sector`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `MusicHall_db`.`sector` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `limit_ticket` BIGINT NOT NULL,
  `price` DECIMAL(10,2) NOT NULL,
  `event_ID` INT NOT NULL,
  PRIMARY KEY (`ID`),
  INDEX `fk_sector_event1_idx` (`event_ID` ASC) VISIBLE,
  CONSTRAINT `fk_sector_event1`
    FOREIGN KEY (`event_ID`)
    REFERENCES `MusicHall_db`.`event` (`ID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

SELECT * FROM sector;

-- -----------------------------------------------------
-- Table `MusicHall_db`.`client`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `MusicHall_db`.`client` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(80) NOT NULL,
  `cpf` VARCHAR(11) NOT NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `MusicHall_db`.`ticket`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `MusicHall_db`.`ticket` (
  `client` INT NOT NULL,
  `event` INT NOT NULL,
  `sector_ID` INT NOT NULL,
  `id_ticket` VARCHAR(50) NOT NULL,
  `date_issue` DATETIME NOT NULL,
  `status` ENUM("emitido", "validado", "cancelado") NOT NULL DEFAULT 'emitido',
  INDEX `fk_client_has_event_event1_idx` (`event` ASC) VISIBLE,
  INDEX `fk_client_has_event_client1_idx` (`client` ASC) VISIBLE,
  PRIMARY KEY (`id_ticket`),
  UNIQUE INDEX `id_ticket_UNIQUE` (`id_ticket` ASC) VISIBLE,
  INDEX `fk_tickets_sector1_idx` (`sector_ID` ASC) VISIBLE,
  CONSTRAINT `fk_client_has_event_client1`
    FOREIGN KEY (`client`)
    REFERENCES `MusicHall_db`.`client` (`ID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_client_has_event_event1`
    FOREIGN KEY (`event`)
    REFERENCES `MusicHall_db`.`event` (`ID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_tickets_sector1`
    FOREIGN KEY (`sector_ID`)
    REFERENCES `MusicHall_db`.`sector` (`ID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
