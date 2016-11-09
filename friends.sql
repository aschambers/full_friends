SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema emaildb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema emaildb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `emaildb` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema friends
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema friends
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `friends` DEFAULT CHARACTER SET utf8 ;
USE `emaildb` ;

-- -----------------------------------------------------
-- Table `emaildb`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `emaildb`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

USE `friends` ;

-- -----------------------------------------------------
-- Table `friends`.`friends`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friends`.`friends` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL DEFAULT NULL,
  `last_name` VARCHAR(45) NULL DEFAULT NULL,
  `occupation` VARCHAR(45) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

