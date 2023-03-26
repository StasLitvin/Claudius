CREATE DATABASE  IF NOT EXISTS `claudius` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `claudius`;
-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: claudius
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `coupons`
--

DROP TABLE IF EXISTS `coupons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coupons` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` text,
  `us` text,
  `cod` text,
  `coin` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coupons`
--

LOCK TABLES `coupons` WRITE;
/*!40000 ALTER TABLE `coupons` DISABLE KEYS */;
INSERT INTO `coupons` VALUES (1,'KFC','Купон на 25%','2132asdaws-qawas21',1503),(3,'BK','30%','asd2112as-12',10000),(4,'BK','30%','asd2112as-12',10000),(5,'KFC','Купон на 25%','2132asdaws-qawas21',1503),(6,'МАК','Купон на 25%','2132asdaws-qawas21',1503),(7,'BK','30%','asd2112as-12',10000),(10,'BK','30%','asd2112as-12',10000);
/*!40000 ALTER TABLE `coupons` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` text,
  `surname` text,
  `fatherland` text,
  `email` text,
  `password` text,
  `pos` text,
  `s` text,
  `coin` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'1','2','3','4','5','Преподаватель','Интроверта',0),(2,'1','2','3','4','5','Преподаватель','Интроверта',0),(3,'1','2','3','4','5','Преподаватель','Интроверта',0),(4,'1','2','3','4','5','Преподаватель','Интроверта',0),(5,'Интроверт','Иванов','Иванович','sdfsd@gmail.ru','dsfsd','Ученик','Интроверт',4646),(7,'Экстровер','Иванов','Иванович','asdasd@asda.asd','asdasda','Ученик','Экстроверт',497),(8,'sadasd','asdasd','sadas','asdas@sad.ru','sada','Ученик','Экстроверта',0),(9,'sadasd','asdasd','sadas','asdas@sad.ru','sada','Ученик','Экстроверта',0),(10,'sadasd','asdasd','sadas','asdas@sad.ru','sada','Ученик','Экстроверта',0),(11,'sadasd','asdasd','sadas','asdas@sad.ru','sada','Ученик','Экстроверта',0),(12,'sadasd','asdasd','sadas','asdas@sad.ru','sada','Ученик','Экстроверта',0),(13,'','','','','Заполните поле!',NULL,'Интроверт',0),(14,'asdadas','фывфыв','asd','фывфы@sda.asd','asdasdas',NULL,'Интроверт',0),(15,'asd','Заполните поле!','sad','asds@sad.we','asdasd',NULL,'Интроверт',0),(16,'asdas','asdasdas','sadasd','claud@sda.ru','parol','Преподаватель','Экстроверт',0),(17,'Амбиверт','Иванов','Иванович','Claud_ambr@mail.ru','parol','Ученик','Амбиверт',0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-18 22:02:47
