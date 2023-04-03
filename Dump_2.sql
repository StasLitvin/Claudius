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
-- Table structure for table `answer_user`
--

DROP TABLE IF EXISTS `answer_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `answer_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_user` int NOT NULL,
  `id_answer` int NOT NULL,
  `id_task` int NOT NULL,
  `coin` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_idx` (`id_user`),
  KEY `answer_idx` (`id_answer`),
  KEY `task_idx` (`id_task`),
  CONSTRAINT `answer_us` FOREIGN KEY (`id_answer`) REFERENCES `answers` (`id`),
  CONSTRAINT `task_us` FOREIGN KEY (`id_task`) REFERENCES `tasks` (`id`),
  CONSTRAINT `user_an` FOREIGN KEY (`id_user`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answer_user`
--

LOCK TABLES `answer_user` WRITE;
/*!40000 ALTER TABLE `answer_user` DISABLE KEYS */;
INSERT INTO `answer_user` VALUES (20,12,2,1,0),(21,12,3,3,10),(22,12,1,1,NULL),(23,12,4,3,NULL),(24,12,1,1,NULL),(25,12,3,3,10),(26,12,1,1,NULL),(27,12,3,3,10),(28,12,2,1,0),(29,12,4,3,NULL),(30,12,2,1,0),(31,12,4,3,NULL),(32,12,2,1,0),(33,12,4,3,NULL),(34,12,1,1,NULL),(35,12,3,3,10),(36,12,2,1,0),(37,12,4,3,NULL);
/*!40000 ALTER TABLE `answer_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `answers`
--

DROP TABLE IF EXISTS `answers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `answers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_task` int NOT NULL,
  `answer` text NOT NULL,
  `true_task` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `task_answ_idx` (`id_task`),
  CONSTRAINT `task_answ` FOREIGN KEY (`id_task`) REFERENCES `tasks` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answers`
--

LOCK TABLES `answers` WRITE;
/*!40000 ALTER TABLE `answers` DISABLE KEYS */;
INSERT INTO `answers` VALUES (1,1,'asd',1),(2,1,'sad',0),(3,3,'sdss',1),(4,3,'sssss',0);
/*!40000 ALTER TABLE `answers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classes`
--

DROP TABLE IF EXISTS `classes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `classes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `description` text NOT NULL,
  `lecture_count` int NOT NULL,
  `users_count` int NOT NULL,
  `img` text NOT NULL,
  `subject` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classes`
--

LOCK TABLES `classes` WRITE;
/*!40000 ALTER TABLE `classes` DISABLE KEYS */;
INSERT INTO `classes` VALUES (1,'Язык программирования Python','что-то',11,4,'coins.png','IT'),(2,'Язык программирования Python','что-то',11,4,'coins.png','IT'),(3,'rnj','sd',231,212,'coins.png','IT');
/*!40000 ALTER TABLE `classes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classes_user`
--

DROP TABLE IF EXISTS `classes_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `classes_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_classes` int NOT NULL,
  `id_user` int NOT NULL,
  `passed` int DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `user_idx` (`id_user`),
  KEY `class_idx` (`id_classes`),
  CONSTRAINT `class` FOREIGN KEY (`id_classes`) REFERENCES `classes` (`id`),
  CONSTRAINT `user` FOREIGN KEY (`id_user`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classes_user`
--

LOCK TABLES `classes_user` WRITE;
/*!40000 ALTER TABLE `classes_user` DISABLE KEYS */;
INSERT INTO `classes_user` VALUES (2,1,14,0),(3,1,12,0);
/*!40000 ALTER TABLE `classes_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `complexity`
--

DROP TABLE IF EXISTS `complexity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `complexity` (
  `id` int NOT NULL AUTO_INCREMENT,
  `point` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `complexity`
--

LOCK TABLES `complexity` WRITE;
/*!40000 ALTER TABLE `complexity` DISABLE KEYS */;
INSERT INTO `complexity` VALUES (1,10),(2,22),(3,40);
/*!40000 ALTER TABLE `complexity` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Table structure for table `lecture_user`
--

DROP TABLE IF EXISTS `lecture_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lecture_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_lectore` int NOT NULL,
  `id_user` int NOT NULL,
  `passed` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `lacture_idx` (`id_lectore`),
  KEY `user_idx` (`id_user`),
  KEY `user_lec_idx` (`id_user`),
  CONSTRAINT `lacture` FOREIGN KEY (`id_lectore`) REFERENCES `lectures` (`id`),
  CONSTRAINT `user_lec` FOREIGN KEY (`id_user`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lecture_user`
--

LOCK TABLES `lecture_user` WRITE;
/*!40000 ALTER TABLE `lecture_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `lecture_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lectures`
--

DROP TABLE IF EXISTS `lectures`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lectures` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_class` int NOT NULL,
  `name` text NOT NULL,
  `lecture` text NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_idx` (`id_class`),
  CONSTRAINT `id` FOREIGN KEY (`id_class`) REFERENCES `classes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lectures`
--

LOCK TABLES `lectures` WRITE;
/*!40000 ALTER TABLE `lectures` DISABLE KEYS */;
INSERT INTO `lectures` VALUES (1,1,'Лекция1','asd'),(2,1,'Лекция2','saf');
/*!40000 ALTER TABLE `lectures` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tasks`
--

DROP TABLE IF EXISTS `tasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tasks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_lecture` int NOT NULL,
  `id_complexity` int NOT NULL,
  `task` text NOT NULL,
  PRIMARY KEY (`id`),
  KEY `point_idx` (`id_complexity`),
  KEY `lecture_idx` (`id_lecture`),
  CONSTRAINT `lecture` FOREIGN KEY (`id_lecture`) REFERENCES `lectures` (`id`),
  CONSTRAINT `point` FOREIGN KEY (`id_complexity`) REFERENCES `complexity` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tasks`
--

LOCK TABLES `tasks` WRITE;
/*!40000 ALTER TABLE `tasks` DISABLE KEYS */;
INSERT INTO `tasks` VALUES (1,1,2,'sad'),(2,2,3,'asss'),(3,1,1,'asd'),(4,2,3,'qqq'),(5,2,3,'sd');
/*!40000 ALTER TABLE `tasks` ENABLE KEYS */;
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
  `salt` text,
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
INSERT INTO `users` VALUES (1,'1','2','3','4','5',NULL,'Преподаватель','Интроверта',0),(2,'1','2','3','4','5',NULL,'Преподаватель','Интроверта',0),(3,'1','2','3','4','5',NULL,'Преподаватель','Интроверта',0),(4,'1','2','3','4','5',NULL,'Преподаватель','Интроверта',0),(5,'Интроверт','Иванов','Иванович','sdfsd@gmail.ru','dsfsd',NULL,'Ученик','Интроверт',4646),(7,'Экстровер','Иванов','Иванович','asdasd@asda.asd','asdasda',NULL,'Ученик','Экстроверт',497),(8,'sadasd','asdasd','sadas','asdas@sad.ru','sada',NULL,'Ученик','Экстроверта',0),(9,'sadasd','asdasd','sadas','asdas@sad.ru','sada',NULL,'Ученик','Экстроверта',0),(10,'sadasd','asdasd','sadas','asdas@sad.ru','sada',NULL,'Ученик','Экстроверта',0),(11,'sadasd','asdasd','sadas','asdas@sad.ru','sada',NULL,'Ученик','Экстроверта',0),(12,'sadasd','asdasd','sadas','asdas@sad.ru','sada',NULL,'Ученик','Экстроверта',0),(13,'','','','','Заполните поле!',NULL,NULL,'Интроверт',0),(14,'asdadas','фывфыв','asd','фывфы@sda.asd','asdasdas',NULL,NULL,'Интроверт',0),(15,'asd','Заполните поле!','sad','asds@sad.we','asdasd',NULL,NULL,'Интроверт',0),(16,'asdas','asdasdas','sadasd','claud@sda.ru','parol',NULL,'Преподаватель','Экстроверт',0),(17,'Амбиверт','Иванов','Иванович','Claud_ambr@mail.ru','parol',NULL,'Ученик','Амбиверт',0);
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

-- Dump completed on 2023-04-03 23:54:49
