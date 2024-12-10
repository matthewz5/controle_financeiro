-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema schema_projeto_controle_financeiro
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema schema_projeto_controle_financeiro
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `schema_projeto_controle_financeiro` ;
USE `schema_projeto_controle_financeiro` ;

-- -----------------------------------------------------
-- Table `schema_projeto_controle_financeiro`.`DADOS_BANCO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `schema_projeto_controle_financeiro`.`DADOS_BANCO` (
  `id_BAN` INT NOT NULL,
  `BAN_ORIGEM` VARCHAR(50) NULL,
  `BAN_CATEGORIA` VARCHAR(50) NULL,
  `BAN_VALOR` FLOAT NULL,
  `BAN_DATA` DATE NULL,
  PRIMARY KEY (`id_BAN`),
  UNIQUE INDEX `id_BAN_UNIQUE` (`id_BAN` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `schema_projeto_controle_financeiro`.`DADOS_SALARIO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `schema_projeto_controle_financeiro`.`DADOS_SALARIO` (
  `id_SAL` INT NOT NULL,
  `SAL_ORIGEM` VARCHAR(50) NULL,
  `SAL_CATEGORIA` VARCHAR(50) NULL,
  `SAL_DATA_IN` DATE NULL,
  `SAL_DATA_OUT` DATE NULL,
  `SAL_VALOR` FLOAT NULL,
  `SAL_DATA` DATE NULL,
  PRIMARY KEY (`id_SAL`),
  UNIQUE INDEX `id_SAL_UNIQUE` (`id_SAL` ASC) VISIBLE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
