-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema school
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `school` ;

-- -----------------------------------------------------
-- Schema school
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `school` DEFAULT CHARACTER SET utf8 ;
USE `school` ;

-- -----------------------------------------------------
-- Table `school`.`director`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `school`.`director` ;

CREATE TABLE IF NOT EXISTS `school`.`director` (
  `username` VARCHAR(16) NOT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `password` VARCHAR(32) NOT NULL,
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP(),
  `id` INT(10) NOT NULL AUTO_INCREMENT,
  `update_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP(),
  PRIMARY KEY (`id`),
  UNIQUE INDEX `director_id_UNIQUE` (`id` ASC) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `school`.`class`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `school`.`class` ;

CREATE TABLE IF NOT EXISTS `school`.`class` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `update_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP(),
  `director_id` INT(10) NOT NULL,
  PRIMARY KEY (`id`, `director_id`),
  INDEX `fk_class_director_idx` (`director_id` ASC) ,
  CONSTRAINT `fk_class_director`
    FOREIGN KEY (`director_id`)
    REFERENCES `school`.`director` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `school`.`root`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `school`.`root` ;

CREATE TABLE IF NOT EXISTS `school`.`root` (
  `username` VARCHAR(16) NOT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `password` VARCHAR(32) NOT NULL,
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP(),
  `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `update_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `school`.`student`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `school`.`student` ;

CREATE TABLE IF NOT EXISTS `school`.`student` (
  `username` VARCHAR(16) NOT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `password` VARCHAR(32) NOT NULL,
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP(),
  `id` INT(10) NOT NULL AUTO_INCREMENT,
  `update_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP(),
  PRIMARY KEY (`id`),
  UNIQUE INDEX `student_id_UNIQUE` (`id` ASC) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `school`.`teacher`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `school`.`teacher` ;

CREATE TABLE IF NOT EXISTS `school`.`teacher` (
  `username` VARCHAR(16) NOT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `password` VARCHAR(32) NOT NULL,
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP(),
  `id` INT(10) NOT NULL AUTO_INCREMENT,
  `update_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP(),
  PRIMARY KEY (`id`),
  UNIQUE INDEX `teacher_id_UNIQUE` (`id` ASC) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `school`.`subject`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `school`.`subject` ;

CREATE TABLE IF NOT EXISTS `school`.`subject` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `update_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP(),
  `class_id` INT(11) NOT NULL,
  `teacher_id` INT(10) NOT NULL,
  PRIMARY KEY (`id`, `class_id`, `teacher_id`),
  UNIQUE INDEX `subject_id_UNIQUE` (`id` ASC) ,
  INDEX `fk_subject_class1_idx` (`class_id` ASC) ,
  INDEX `fk_subject_teacher1_idx` (`teacher_id` ASC) ,
  CONSTRAINT `fk_subject_class1`
    FOREIGN KEY (`class_id`)
    REFERENCES `school`.`class` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_subject_teacher1`
    FOREIGN KEY (`teacher_id`)
    REFERENCES `school`.`teacher` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `school`.`subject_has_student`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `school`.`subject_has_student` ;

CREATE TABLE IF NOT EXISTS `school`.`subject_has_student` (
  `subject_id` INT(11) NOT NULL,
  `student_id` INT(10) NOT NULL,
  PRIMARY KEY (`subject_id`, `student_id`),
  INDEX `fk_subject_has_student_student1_idx` (`student_id` ASC) ,
  INDEX `fk_subject_has_student_subject1_idx` (`subject_id` ASC) ,
  CONSTRAINT `fk_subject_has_student_subject1`
    FOREIGN KEY (`subject_id`)
    REFERENCES `school`.`subject` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_subject_has_student_student1`
    FOREIGN KEY (`student_id`)
    REFERENCES `school`.`student` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
