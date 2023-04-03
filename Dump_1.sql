CREATE DATABASE IF NOT EXISTS `claudius`
/*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */
/*!80016 DEFAULT ENCRYPTION='N' */
;

USE `claudius`;

-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: claudius
-- ------------------------------------------------------
-- Server version	8.0.32
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */
;

/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */
;

/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */
;

/*!50503 SET NAMES utf8 */
;

/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */
;

/*!40103 SET TIME_ZONE='+00:00' */
;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */
;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */
;

/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */
;

/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */
;

--
-- Table structure for table `coupons`
--
DROP TABLE IF EXISTS `coupons`;

/*!40101 SET @saved_cs_client     = @@character_set_client */
;

/*!50503 SET character_set_client = utf8mb4 */
;

CREATE TABLE `coupons` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` text,
  `us` text,
  `cod` text,
  `coin` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 11 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

/*!40101 SET character_set_client = @saved_cs_client */
;

--
-- Dumping data for table `coupons`
--
LOCK TABLES `coupons` WRITE;

/*!40000 ALTER TABLE `coupons` DISABLE KEYS */
;

INSERT INTO
  `coupons`
VALUES
  (1, 'KFC', 'Купон на 25%', '2132asdaws-qawas21', 1503),
(3, 'BK', '30%', 'asd2112as-12', 10000),
(4, 'BK', '30%', 'asd2112as-12', 10000),
(5, 'KFC', 'Купон на 25%', '2132asdaws-qawas21', 1503),
(6, 'МАК', 'Купон на 25%', '2132asdaws-qawas21', 1503),
(7, 'BK', '30%', 'asd2112as-12', 10000),
(10, 'BK', '30%', 'asd2112as-12', 10000);

/*!40000 ALTER TABLE `coupons` ENABLE KEYS */
;

UNLOCK TABLES;

--
-- Table structure for table `users`
--
DROP TABLE IF EXISTS `users`;

/*!40101 SET @saved_cs_client     = @@character_set_client */
;

/*!50503 SET character_set_client = utf8mb4 */
;

CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` text,
  `surname` text,
  `fatherland` text,
  `email` text,
  `password` text,
  `salt` text,
  `pos` text,
  `s` text,
  `coin` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 18 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

/*!40101 SET character_set_client = @saved_cs_client */
;

--
-- Dumping data for table `users`
--
LOCK TABLES `users` WRITE;

/*!40000 ALTER TABLE `users` DISABLE KEYS */
;

INSERT INTO
  `users`
VALUES
  (
    1,
    '1',
    '2',
    '3',
    '4',
    '3f93661f80004cb66a9f7893f0e1ca8e3b5f9f6ff36210fc3a3da2044ea06141',
    '1',
    'Преподаватель',
    'Интроверта',
    0
  ),
(
    2,
    '1',
    '2',
    '3',
    '4',
    '3f93661f80004cb66a9f7893f0e1ca8e3b5f9f6ff36210fc3a3da2044ea06141',
    '1',
    'Преподаватель',
    'Интроверта',
    0
  ),
(
    3,
    '1',
    '2',
    '3',
    '4',
    '3f93661f80004cb66a9f7893f0e1ca8e3b5f9f6ff36210fc3a3da2044ea06141',
    '1',
    'Преподаватель',
    'Интроверта',
    0
  ),
(
    4,
    '1',
    '2',
    '3',
    '4',
    '3f93661f80004cb66a9f7893f0e1ca8e3b5f9f6ff36210fc3a3da2044ea06141',
    '1',
    'Преподаватель',
    'Интроверта',
    0
  ),
(
    5,
    'Интроверт',
    'Иванов',
    'Иванович',
    'sdfsd@gmail.ru',
    '7488fbacdd6c64a8fab4d1145a53c15f2afa89ef680a77f86c4cd49a9a51d6df',
    '1',
    'Ученик',
    'Интроверт',
    4646
  ),
(
    7,
    'Экстровер',
    'Иванов',
    'Иванович',
    'asdasd@asda.asd',
    'ee044a085fd1ea2f7894cc08a102ff5a2b9eec7f8d4d6e8cf66f166974a65983',
    '1',
    'Ученик',
    'Экстроверт',
    497
  ),
(
    8,
    'sadasd',
    'asdasd',
    'sadas',
    'asdas@sad.ru',
    '26ba55ecc8e9a8e8f4abfcf2b2b5f92a32f88fd68b57a223d6f115bb0525d892',
    '1',
    'Ученик',
    'Экстроверта',
    0
  ),
(
    9,
    'sadasd',
    'asdasd',
    'sadas',
    'asdas@sad.ru',
    '26ba55ecc8e9a8e8f4abfcf2b2b5f92a32f88fd68b57a223d6f115bb0525d892',
    '1',
    'Ученик',
    'Экстроверта',
    0
  ),
(
    10,
    'sadasd',
    'asdasd',
    'sadas',
    'asdas@sad.ru',
    '26ba55ecc8e9a8e8f4abfcf2b2b5f92a32f88fd68b57a223d6f115bb0525d892',
    '1',
    'Ученик',
    'Экстроверта',
    0
  ),
(
    11,
    'sadasd',
    'asdasd',
    'sadas',
    'asdas@sad.ru',
    '26ba55ecc8e9a8e8f4abfcf2b2b5f92a32f88fd68b57a223d6f115bb0525d892',
    '1',
    'Ученик',
    'Экстроверта',
    0
  ),
(
    12,
    'sadasd',
    'asdasd',
    'sadas',
    'asdas@sad.ru',
    '26ba55ecc8e9a8e8f4abfcf2b2b5f92a32f88fd68b57a223d6f115bb0525d892',
    '1',
    'Ученик',
    'Экстроверта',
    0
  ),
(
    13,
    '',
    '',
    '',
    '',
    '67b176705b46206614219f47a05aee7ae6a3edbe850bbbe214c536b989aea4d2',
    '1',
    NULL,
    'Интроверт',
    0
  ),
(
    14,
    'asdadas',
    'фывфыв',
    'asd',
    'фывфы@sda.asd',
    'c335c1474a456eb26aa4ca06906846baf82ebfb4e73a6789afecdb9a61cb7184',
    '1',
    NULL,
    'Интроверт',
    0
  ),
(
    15,
    'asd',
    'Заполните поле!',
    'sad',
    'asds@sad.we',
    '65d6cf1b688f1bbee8e806d5567923883cecb860f368854fd5ea9ac61dfd0b64',
    '1',
    NULL,
    'Интроверт',
    0
  ),
(
    16,
    'asdas',
    'asdasdas',
    'sadasd',
    'claud@sda.ru',
    'b13044b9d9a77aa1eecbf8faeea73ac4b8d9d697fbca5a0a3ddaf06b38efbb35',
    '1',
    'Преподаватель',
    'Экстроверт',
    0
  ),
(
    17,
    'Амбиверт',
    'Иванов',
    'Иванович',
    'Claud_ambr@mail.ru',
    'b13044b9d9a77aa1eecbf8faeea73ac4b8d9d697fbca5a0a3ddaf06b38efbb35',
    '1',
    'Ученик',
    'Амбиверт',
    0
  );

/*!40000 ALTER TABLE `users` ENABLE KEYS */
;

UNLOCK TABLES;

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */
;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */
;

/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */
;

/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */
;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */
;

/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */
;

/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */
;

/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */
;

-- Dump completed on 2023-03-18 22:02:47