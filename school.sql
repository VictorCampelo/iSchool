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

-- -----------------------------------------------------
-- Schema school
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `school` DEFAULT CHARACTER SET utf8 ;
USE `school` ;

-- -----------------------------------------------------
-- Table `school`.`student`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `school`.`student` (
  `username` VARCHAR(16) NOT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `password` VARCHAR(32) NOT NULL,
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP(),
  `student_id` INT(10) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`student_id`),
  UNIQUE INDEX `student_id_UNIQUE` (`student_id` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `school`.`class`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `school`.`class` (
  `class_id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `student_id` INT(10) NOT NULL,
  PRIMARY KEY (`class_id`, `student_id`),
  INDEX `fk_class_student1_idx` (`student_id` ASC),
  CONSTRAINT `fk_class_student1`
    FOREIGN KEY (`student_id`)
    REFERENCES `school`.`student` (`student_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `school`.`subject`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `school`.`subject` (
  `subject_id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`subject_id`),
  UNIQUE INDEX `subject_id_UNIQUE` (`subject_id` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `school`.`class_has_subject`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `school`.`class_has_subject` (
  `class_class_id` INT(11) NOT NULL,
  `subject_subject_id` INT(11) NOT NULL,
  PRIMARY KEY (`class_class_id`, `subject_subject_id`),
  INDEX `fk_class_has_subject_subject1_idx` (`subject_subject_id` ASC),
  INDEX `fk_class_has_subject_class1_idx` (`class_class_id` ASC),
  CONSTRAINT `fk_class_has_subject_class1`
    FOREIGN KEY (`class_class_id`)
    REFERENCES `school`.`class` (`class_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_class_has_subject_subject1`
    FOREIGN KEY (`subject_subject_id`)
    REFERENCES `school`.`subject` (`subject_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `school`.`teacher`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `school`.`teacher` (
  `username` VARCHAR(16) NOT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `password` VARCHAR(32) NOT NULL,
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP(),
  `teacher_id` INT(10) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`teacher_id`),
  UNIQUE INDEX `teacher_id_UNIQUE` (`teacher_id` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `school`.`class_has_teacher`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `school`.`class_has_teacher` (
  `class_class_id` INT(11) NOT NULL,
  `teacher_teacher_id` INT(10) NOT NULL,
  PRIMARY KEY (`class_class_id`, `teacher_teacher_id`),
  INDEX `fk_class_has_teacher_teacher1_idx` (`teacher_teacher_id` ASC),
  INDEX `fk_class_has_teacher_class_idx` (`class_class_id` ASC),
  CONSTRAINT `fk_class_has_teacher_class`
    FOREIGN KEY (`class_class_id`)
    REFERENCES `school`.`class` (`class_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_class_has_teacher_teacher1`
    FOREIGN KEY (`teacher_teacher_id`)
    REFERENCES `school`.`teacher` (`teacher_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `school`.`director`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `school`.`director` (
  `username` VARCHAR(16) NOT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `password` VARCHAR(32) NOT NULL,
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP(),
  `director_id` INT(10) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`director_id`),
  UNIQUE INDEX `director_id_UNIQUE` (`director_id` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `school`.`root`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `school`.`root` (
  `username` VARCHAR(16) NOT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `password` VARCHAR(32) NOT NULL,
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP(),
  `root_id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`root_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
