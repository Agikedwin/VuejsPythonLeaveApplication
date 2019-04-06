-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: leave_system
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.16.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `departments`
--

DROP TABLE IF EXISTS `departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `departments` (
  `department_id` int(11) NOT NULL AUTO_INCREMENT,
  `department_name` varchar(100) NOT NULL,
  `description` varchar(100) DEFAULT NULL,
  `is_deleted` tinyint(1) DEFAULT NULL,
  `userid` int(11) NOT NULL,
  `editor` varchar(20) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL,
  `date_updated` datetime DEFAULT NULL,
  PRIMARY KEY (`department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departments`
--

LOCK TABLES `departments` WRITE;
/*!40000 ALTER TABLE `departments` DISABLE KEYS */;
INSERT INTO `departments` VALUES (5,'Management','At management Level, can approve leave',0,1,'001','2019-03-17 14:44:55','2019-03-17 14:44:55'),(15,'Operational','2',0,1,'001','2019-03-19 09:28:57','2019-03-19 09:28:57'),(16,'Test','9',0,1,'001','2019-04-02 04:40:20','2019-04-02 04:40:20'),(17,'test','6',0,1,'001','2019-04-02 04:40:20','2019-04-02 04:40:20');
/*!40000 ALTER TABLE `departments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `designation`
--

DROP TABLE IF EXISTS `designation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `designation` (
  `designation_id` int(11) NOT NULL AUTO_INCREMENT,
  `designation_name` varchar(100) NOT NULL,
  `description` varchar(300) DEFAULT NULL,
  `code` varchar(50) DEFAULT NULL,
  `department_id` int(11) NOT NULL,
  `level` int(11) NOT NULL,
  `is_deleted` tinyint(1) DEFAULT NULL,
  `userid` int(11) NOT NULL,
  `editor` varchar(20) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL,
  `date_updated` datetime DEFAULT NULL,
  PRIMARY KEY (`designation_id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `designation_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `designation`
--

LOCK TABLES `designation` WRITE;
/*!40000 ALTER TABLE `designation` DISABLE KEYS */;
INSERT INTO `designation` VALUES (1,'HR','description',NULL,5,2,0,1,'001','2019-03-30 06:33:48','2019-03-30 06:33:48'),(2,'Programmer','description',NULL,5,2,1,1,'001','2019-03-30 06:33:48','2019-03-30 06:33:48'),(3,'programmer','description',NULL,5,2,0,1,'001','2019-03-30 06:33:48','2019-03-30 06:33:48'),(4,'Drivers','description',NULL,15,2,0,1,'001','2019-03-30 06:33:48','2019-03-30 06:33:48'),(5,'procurement','description',NULL,15,2,0,1,'001','2019-03-30 06:33:48','2019-03-30 06:33:48'),(6,'county Lead','description',NULL,5,2,0,1,'001','2019-04-03 07:08:53','2019-04-03 07:08:53'),(7,'county Lead','description',NULL,5,2,0,1,'001','2019-04-03 07:08:53','2019-04-03 07:08:53');
/*!40000 ALTER TABLE `designation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_registration`
--

DROP TABLE IF EXISTS `employee_registration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee_registration` (
  `employee_id` int(11) NOT NULL AUTO_INCREMENT,
  `payroll_no` int(11) NOT NULL,
  `surname` varchar(50) NOT NULL,
  `other_names` varchar(100) DEFAULT NULL,
  `appointment_date` datetime DEFAULT NULL,
  `designation` varchar(100) DEFAULT NULL,
  `dob` datetime DEFAULT NULL,
  `entry_salary` varchar(100) DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  `program` varchar(100) DEFAULT NULL,
  `terms_of_service` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone_no` varchar(100) DEFAULT NULL,
  `birth_place` varchar(100) DEFAULT NULL,
  `nationalty` varchar(100) DEFAULT NULL,
  `passport_idno` varchar(100) DEFAULT NULL,
  `marital_status` varchar(100) DEFAULT NULL,
  `spause_name` varchar(100) DEFAULT NULL,
  `spause_idno` varchar(100) DEFAULT NULL,
  `kra_no` varchar(100) DEFAULT NULL,
  `nssf_no` varchar(100) DEFAULT NULL,
  `nhif_no` varchar(100) DEFAULT NULL,
  `bank_name` varchar(100) DEFAULT NULL,
  `branch` varchar(100) DEFAULT NULL,
  `account_no` varchar(100) DEFAULT NULL,
  `supervisor_status` tinyint(1) DEFAULT NULL,
  `is_deleted` tinyint(1) DEFAULT NULL,
  `userid` int(11) NOT NULL,
  `editor` varchar(20) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL,
  `date_updated` datetime DEFAULT NULL,
  `username` varchar(150) NOT NULL,
  `password` text NOT NULL,
  `resev1` varchar(100) DEFAULT NULL,
  `presev12` varchar(100) DEFAULT NULL,
  `resev13` varchar(100) DEFAULT NULL,
  `presev14` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`employee_id`,`payroll_no`),
  UNIQUE KEY `payroll_no` (`payroll_no`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_registration`
--

LOCK TABLES `employee_registration` WRITE;
/*!40000 ALTER TABLE `employee_registration` DISABLE KEYS */;
INSERT INTO `employee_registration` VALUES (1,10510,'Lucy ','Adhiambo  Ochola','2018-08-01 00:00:00','5','2004-12-01 00:00:00','40000',0,'purchases','Contract','joerironald@gmail.com','0725129000','kisumu','kenyan','248900','Married','jared John','24567','23000','0097887','09877','equity','kisumu','0987765',0,0,1,'001','2019-03-30 06:33:48','2019-03-30 06:33:48','Leave@10510','$2b$12$wU1Pwtkn7NQF1aCZmprrsOR0lXkyTTTH2VU5mLHaWTAW9sJz8QX02',NULL,NULL,NULL,NULL),(4,34526,'Denis','Ochola','2017-12-03 00:00:00','1','2009-08-02 00:00:00','70000',0,'hr','Contract','joerironald@gmail.com','07834455','kisumu','kenyan','87994','Married','janet ','3456666','7866543','','','','','',1,0,1,'001','2019-03-30 06:33:48','2019-03-30 06:33:48','Leave@34526','$2b$12$k9DamWyhzxVK.ml5BCcLNevqIfep2FI4SWEeqrvhDGeg09jRCOlkW',NULL,NULL,NULL,NULL),(22,10512,'Tonny','wendo seme','2018-02-12 00:00:00','4','2000-11-01 00:00:00','38000',0,'faces','Contract','joerironald@gmail.com','0967767','siaya','kenyan','34523','Single','dinah','201999','09452eree','','','','','',1,0,1,'001','2019-03-30 06:33:48','2019-03-30 06:33:48','whizedvinAG@@73','$2b$12$tq8kv8VEIMf4qJldQPV6YOBbWeRnXxlWcLkxYxZ/NyuUc4R0x1Mmm',NULL,NULL,NULL,NULL),(23,50142,'Melisa ','Ivy','2019-02-04 00:00:00','6','2018-11-04 00:00:00','200000',0,'Faces','Contract','eagik@kemri-ucsf.org','2090191','Mp-Shaa','kenyan','23890','Single','none','234890','234897829','897889','088088','corp','uhuru','7890202',1,0,1,'001','2019-04-03 07:08:53','2019-04-03 07:08:53','Leave@50142','$2b$12$d1uupYZHPzvti7Gi3m7Kp.zJ0YZCj6ABGQFKwVTSRQJ9x2Es600QC',NULL,NULL,NULL,NULL),(25,50143,'Snanza ','A Marionya','2019-02-04 00:00:00','4','2018-11-04 00:00:00','200000',0,'Faces','Contract','eagik@kemri-ucsf.org','2090191','Mp-Shaa','kenyan','23890','Single','none','234890','234897829','897889','088088','corp','uhuru','7890202',0,0,1,'001','2019-04-03 07:41:40','2019-04-03 07:41:40','Leave@50143','$2b$12$a1WxqhZxi6lsfJRecxNMyep6mj7h.jx/HZmANQyKegNcOSQywNaZ.',NULL,NULL,NULL,NULL),(26,34234,'Jane','gasheni','2019-04-05 00:00:00','3','2019-04-11 00:00:00','30000',0,'power','Permanent','eagik@kemri-ucsf.org','23457','naivasha','kenya','3450','Widowed','erokkk','789','2343453','4rere','3456','4r4r','corp','23466',1,0,1,'001','2019-04-03 07:41:40','2019-04-03 07:41:40','Leave@34234','$2b$12$H6/pwRdXKQxRzrk29wkAzuv28y4B0ndX7VFGrHSzsSAjtcBzPvuba',NULL,NULL,NULL,NULL),(28,200200,'Serah','Maogani','2019-04-05 00:00:00','5','2019-04-11 00:00:00','30000',0,'power','Permanent','eagik@kemri-ucsf.org','23457','naivasha','kenya','3450','Widowed','erokkk','789','2343453','4rere','3456','4r4r','corp','23466',0,0,1,'001','2019-04-03 07:41:40','2019-04-03 07:41:40','Leave@200200','$2b$12$gYNit0D1.3e9NLBhhS1Aj.kFNimraZHatNsNLpwn89yR8BOl5HBne',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `employee_registration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `initial_leave_balance`
--

DROP TABLE IF EXISTS `initial_leave_balance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `initial_leave_balance` (
  `balance_id` int(11) NOT NULL AUTO_INCREMENT,
  `payroll_no` int(11) NOT NULL,
  `initial_balance` int(11) NOT NULL,
  `is_deleted` tinyint(1) DEFAULT NULL,
  `userid` int(11) NOT NULL,
  `editor` varchar(20) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL,
  `date_updated` datetime DEFAULT NULL,
  PRIMARY KEY (`balance_id`),
  KEY `payroll_no` (`payroll_no`),
  CONSTRAINT `initial_leave_balance_ibfk_1` FOREIGN KEY (`payroll_no`) REFERENCES `employee_registration` (`payroll_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `initial_leave_balance`
--

LOCK TABLES `initial_leave_balance` WRITE;
/*!40000 ALTER TABLE `initial_leave_balance` DISABLE KEYS */;
/*!40000 ALTER TABLE `initial_leave_balance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `leave_applications`
--

DROP TABLE IF EXISTS `leave_applications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `leave_applications` (
  `application_id` int(11) NOT NULL AUTO_INCREMENT,
  `leave_id` int(11) NOT NULL,
  `payroll_no` int(11) NOT NULL,
  `date_from` date DEFAULT NULL,
  `date_to` date DEFAULT NULL,
  `approved` int(11) DEFAULT NULL,
  `leave_status` int(11) NOT NULL,
  `application_note` varchar(300) DEFAULT NULL,
  `is_deleted` tinyint(1) DEFAULT NULL,
  `userid` int(11) NOT NULL,
  `editor` varchar(20) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL,
  `date_updated` datetime DEFAULT NULL,
  PRIMARY KEY (`application_id`),
  KEY `leave_id` (`leave_id`),
  KEY `payroll_no` (`payroll_no`),
  CONSTRAINT `leave_applications_ibfk_1` FOREIGN KEY (`leave_id`) REFERENCES `leave_types` (`leave_id`),
  CONSTRAINT `leave_applications_ibfk_2` FOREIGN KEY (`payroll_no`) REFERENCES `employee_registration` (`payroll_no`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leave_applications`
--

LOCK TABLES `leave_applications` WRITE;
/*!40000 ALTER TABLE `leave_applications` DISABLE KEYS */;
INSERT INTO `leave_applications` VALUES (1,1,10510,'2019-03-19','2019-03-26',0,0,'test application',0,1,'001','2019-03-30 09:50:00','2019-03-30 09:50:00'),(2,1,34526,'2019-03-13','2019-03-20',0,0,'test application ',0,1,'001','2019-03-30 10:02:10','2019-03-30 10:02:10'),(3,1,10510,'2019-03-01','2019-03-06',0,0,'test',0,1,'001','2019-03-30 10:11:09','2019-03-30 10:11:09'),(4,1,10512,'2019-03-05','2019-03-16',0,0,'tesr',0,1,'001','2019-03-31 16:10:50','2019-03-31 16:10:50'),(5,1,10512,'2019-03-06','2019-03-06',0,0,'test',0,1,'001','2019-03-31 16:14:54','2019-03-31 16:14:54'),(6,1,10512,'2019-03-13','2019-03-15',0,0,'test',0,1,'001','2019-03-31 16:16:11','2019-03-31 16:16:11'),(7,1,10512,'2019-03-06','2019-03-15',0,0,'test',0,1,'001','2019-03-31 16:21:18','2019-03-31 16:21:18'),(8,1,10512,'2019-03-06','2019-03-08',0,0,'test',0,1,'001','2019-03-31 16:22:32','2019-03-31 16:22:32'),(9,1,10512,'2019-03-19','2019-03-20',0,0,'test',0,1,'001','2019-03-31 16:24:31','2019-03-31 16:24:31'),(10,1,50142,'2019-04-04','2019-04-08',1,0,'take break from work',0,1,'001','2019-04-03 07:41:40','2019-04-03 07:41:40'),(11,3,50142,'2019-04-04','2019-04-11',0,0,'Visit a doctor',0,1,'001','2019-04-03 07:41:40','2019-04-03 07:41:40'),(12,3,34234,'2019-04-05','2019-04-10',1,0,'routine medical checkup',0,1,'001','2019-04-04 03:55:32','2019-04-04 03:55:32');
/*!40000 ALTER TABLE `leave_applications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `leave_approval`
--

DROP TABLE IF EXISTS `leave_approval`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `leave_approval` (
  `approval_id` int(11) NOT NULL AUTO_INCREMENT,
  `application_id` int(11) NOT NULL,
  `payroll_no` int(11) NOT NULL,
  `next_person_to_approve` int(11) NOT NULL,
  `aproval_status` int(11) NOT NULL,
  `note` varchar(350) NOT NULL,
  `is_deleted` tinyint(1) DEFAULT NULL,
  `userid` int(11) NOT NULL,
  `editor` varchar(20) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL,
  `date_updated` datetime DEFAULT NULL,
  PRIMARY KEY (`approval_id`),
  KEY `application_id` (`application_id`),
  KEY `payroll_no` (`payroll_no`),
  CONSTRAINT `leave_approval_ibfk_1` FOREIGN KEY (`application_id`) REFERENCES `leave_applications` (`application_id`),
  CONSTRAINT `leave_approval_ibfk_2` FOREIGN KEY (`payroll_no`) REFERENCES `employee_registration` (`payroll_no`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leave_approval`
--

LOCK TABLES `leave_approval` WRITE;
/*!40000 ALTER TABLE `leave_approval` DISABLE KEYS */;
INSERT INTO `leave_approval` VALUES (1,10,34234,0,1,'Proceed and enjoy your leave',0,1,'001','2019-04-03 09:41:29','2019-04-03 09:41:29'),(2,11,34234,34526,1,'Escalated to higher level',0,1,'001','2019-04-03 09:41:29','2019-04-03 09:41:29'),(3,11,34234,34526,0,'test approval',0,1,'001','2019-04-04 04:53:06','2019-04-04 04:53:06'),(4,11,34234,34526,0,'escalate to next level',0,1,'001','2019-04-04 04:53:06','2019-04-04 04:53:06'),(5,12,34526,34234,0,'Test escalate',0,1,'001','2019-04-04 06:31:01','2019-04-04 06:31:01'),(6,12,34234,0,1,'Proceed to leave',0,1,'001','2019-04-04 06:31:01','2019-04-04 06:31:01');
/*!40000 ALTER TABLE `leave_approval` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `leave_authorization`
--

DROP TABLE IF EXISTS `leave_authorization`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `leave_authorization` (
  `auth_id` int(11) NOT NULL AUTO_INCREMENT,
  `supervisor_payroll_no` int(11) NOT NULL,
  `emp_payroll_no` int(11) NOT NULL,
  `leave_application_id` int(11) NOT NULL,
  `leave_id` int(11) NOT NULL,
  `auth_stage` int(11) NOT NULL,
  `note` varchar(350) DEFAULT NULL,
  `is_deleted` tinyint(1) DEFAULT NULL,
  `userid` int(11) NOT NULL,
  `editor` varchar(20) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL,
  `date_updated` datetime DEFAULT NULL,
  PRIMARY KEY (`auth_id`),
  KEY `supervisor_payroll_no` (`supervisor_payroll_no`),
  CONSTRAINT `leave_authorization_ibfk_1` FOREIGN KEY (`supervisor_payroll_no`) REFERENCES `employee_registration` (`payroll_no`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leave_authorization`
--

LOCK TABLES `leave_authorization` WRITE;
/*!40000 ALTER TABLE `leave_authorization` DISABLE KEYS */;
INSERT INTO `leave_authorization` VALUES (1,34234,50142,10,1,0,'AUTH NOTE',0,1,'001','2019-04-03 07:41:40','2019-04-03 07:41:40'),(2,34234,50142,11,3,0,'AUTH NOTE',0,1,'001','2019-04-03 07:41:40','2019-04-03 07:41:40'),(3,34526,34234,12,3,0,'AUTH NOTE',0,1,'001','2019-04-04 03:55:32','2019-04-04 03:55:32');
/*!40000 ALTER TABLE `leave_authorization` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `leave_reliever`
--

DROP TABLE IF EXISTS `leave_reliever`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `leave_reliever` (
  `reliever_id` int(11) NOT NULL AUTO_INCREMENT,
  `leave_id` int(11) NOT NULL,
  `payroll_no` int(11) NOT NULL,
  `reliever_payroll_no` int(11) NOT NULL,
  `date_from` date DEFAULT NULL,
  `date_to` date DEFAULT NULL,
  `relieve_status` int(11) NOT NULL,
  `application_note` varchar(300) DEFAULT NULL,
  `is_deleted` tinyint(1) DEFAULT NULL,
  `userid` int(11) NOT NULL,
  `editor` varchar(20) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL,
  `date_updated` datetime DEFAULT NULL,
  PRIMARY KEY (`reliever_id`),
  KEY `leave_id` (`leave_id`),
  KEY `payroll_no` (`payroll_no`),
  KEY `reliever_payroll_no` (`reliever_payroll_no`),
  CONSTRAINT `leave_reliever_ibfk_1` FOREIGN KEY (`leave_id`) REFERENCES `leave_types` (`leave_id`),
  CONSTRAINT `leave_reliever_ibfk_2` FOREIGN KEY (`payroll_no`) REFERENCES `employee_registration` (`payroll_no`),
  CONSTRAINT `leave_reliever_ibfk_3` FOREIGN KEY (`reliever_payroll_no`) REFERENCES `employee_registration` (`payroll_no`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leave_reliever`
--

LOCK TABLES `leave_reliever` WRITE;
/*!40000 ALTER TABLE `leave_reliever` DISABLE KEYS */;
INSERT INTO `leave_reliever` VALUES (1,1,10510,34526,'2019-03-01','2019-03-06',0,'test',0,1,'001','2019-03-30 10:11:09','2019-03-30 10:11:09'),(2,1,10512,34526,'2019-03-05','2019-03-16',0,'tesr',0,1,'001','2019-03-31 16:10:50','2019-03-31 16:10:50'),(3,1,10512,34526,'2019-03-06','2019-03-06',0,'test',0,1,'001','2019-03-31 16:14:54','2019-03-31 16:14:54'),(4,1,10512,34526,'2019-03-13','2019-03-15',0,'test',0,1,'001','2019-03-31 16:16:11','2019-03-31 16:16:11'),(5,1,10512,34526,'2019-03-06','2019-03-15',0,'test',0,1,'001','2019-03-31 16:21:18','2019-03-31 16:21:18'),(6,1,10512,34526,'2019-03-06','2019-03-08',0,'test',0,1,'001','2019-03-31 16:22:32','2019-03-31 16:22:32'),(7,1,10512,34526,'2019-03-19','2019-03-20',0,'test',0,1,'001','2019-03-31 16:24:31','2019-03-31 16:24:31'),(8,1,50142,34234,'2019-04-04','2019-04-08',0,'take break from work',0,1,'001','2019-04-03 07:41:40','2019-04-03 07:41:40'),(9,3,50142,34234,'2019-04-04','2019-04-11',0,'Visit a doctor',0,1,'001','2019-04-03 07:41:40','2019-04-03 07:41:40'),(10,3,34234,34526,'2019-04-05','2019-04-10',0,'routine medical checkup',0,1,'001','2019-04-04 03:55:32','2019-04-04 03:55:32');
/*!40000 ALTER TABLE `leave_reliever` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `leave_types`
--

DROP TABLE IF EXISTS `leave_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `leave_types` (
  `leave_id` int(11) NOT NULL AUTO_INCREMENT,
  `leave_name` varchar(50) NOT NULL,
  `no_days` int(11) NOT NULL,
  `countinous` tinyint(1) DEFAULT NULL,
  `is_deleted` tinyint(1) DEFAULT NULL,
  `userid` int(11) NOT NULL,
  `editor` varchar(20) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL,
  `date_updated` datetime DEFAULT NULL,
  PRIMARY KEY (`leave_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leave_types`
--

LOCK TABLES `leave_types` WRITE;
/*!40000 ALTER TABLE `leave_types` DISABLE KEYS */;
INSERT INTO `leave_types` VALUES (1,'Annual Leave',30,0,0,1,'001','2019-03-30 06:33:48','2019-03-30 06:33:48'),(2,'Study Leave',10,0,0,1,'001','2019-04-03 07:41:40','2019-04-03 07:41:40'),(3,'Sick Leave',20,0,0,1,'001','2019-04-03 07:41:40','2019-04-03 07:41:40'),(4,'Compassionate',15,0,0,1,'001','2019-04-03 07:41:40','2019-04-03 07:41:40');
/*!40000 ALTER TABLE `leave_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login_activity`
--

DROP TABLE IF EXISTS `login_activity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `login_activity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `payroll_no` varchar(80) NOT NULL,
  `token` text,
  `account_status` varchar(80) NOT NULL,
  `login_timestamp` datetime DEFAULT NULL,
  `logout_timestamp` datetime DEFAULT NULL,
  `ip_address` varchar(80) NOT NULL,
  `user_agent` varchar(300) NOT NULL,
  `uuid` varchar(80) DEFAULT NULL,
  `is_deleted` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=88 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_activity`
--

LOCK TABLES `login_activity` WRITE;
/*!40000 ALTER TABLE `login_activity` DISABLE KEYS */;
INSERT INTO `login_activity` VALUES (1,'10510','$2b$12$wU1Pwtkn7NQF1aCZmprrsOR0lXkyTTTH2VU5mLHaWTAW9sJz8QX02','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(2,'10510','$2b$12$wU1Pwtkn7NQF1aCZmprrsOR0lXkyTTTH2VU5mLHaWTAW9sJz8QX02','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(3,'10510','$2b$12$wU1Pwtkn7NQF1aCZmprrsOR0lXkyTTTH2VU5mLHaWTAW9sJz8QX02','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(4,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(5,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(6,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(7,'10510','$2b$12$wU1Pwtkn7NQF1aCZmprrsOR0lXkyTTTH2VU5mLHaWTAW9sJz8QX02','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(8,'10510','$2b$12$wU1Pwtkn7NQF1aCZmprrsOR0lXkyTTTH2VU5mLHaWTAW9sJz8QX02','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(9,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(10,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(11,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(12,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(13,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(14,'34526','$2b$12$k9DamWyhzxVK.ml5BCcLNevqIfep2FI4SWEeqrvhDGeg09jRCOlkW','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(15,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(16,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(17,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(18,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(19,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(20,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(21,'10510','$2b$12$wU1Pwtkn7NQF1aCZmprrsOR0lXkyTTTH2VU5mLHaWTAW9sJz8QX02','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(22,'10510','$2b$12$wU1Pwtkn7NQF1aCZmprrsOR0lXkyTTTH2VU5mLHaWTAW9sJz8QX02','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(23,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(24,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(25,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(26,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(27,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(28,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(29,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(30,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(31,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(32,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(33,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(34,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(35,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(36,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(37,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(38,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(39,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(40,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(41,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(42,'34526','$2b$12$k9DamWyhzxVK.ml5BCcLNevqIfep2FI4SWEeqrvhDGeg09jRCOlkW','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(43,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(44,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(45,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(46,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(47,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(48,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(49,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(50,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(51,'10512','$2b$12$NeRmlk2tvxd0/8OPXmvRP.xAX.IdgRC/SmED5utU11dEjYdwwQIIi','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(52,'10512','$2b$12$tq8kv8VEIMf4qJldQPV6YOBbWeRnXxlWcLkxYxZ/NyuUc4R0x1Mmm','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(53,'34526','$2b$12$k9DamWyhzxVK.ml5BCcLNevqIfep2FI4SWEeqrvhDGeg09jRCOlkW','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(54,'10512','$2b$12$tq8kv8VEIMf4qJldQPV6YOBbWeRnXxlWcLkxYxZ/NyuUc4R0x1Mmm','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(55,'10512','$2b$12$tq8kv8VEIMf4qJldQPV6YOBbWeRnXxlWcLkxYxZ/NyuUc4R0x1Mmm','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(56,'10512','$2b$12$tq8kv8VEIMf4qJldQPV6YOBbWeRnXxlWcLkxYxZ/NyuUc4R0x1Mmm','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(57,'10512','$2b$12$tq8kv8VEIMf4qJldQPV6YOBbWeRnXxlWcLkxYxZ/NyuUc4R0x1Mmm','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(58,'10512','$2b$12$tq8kv8VEIMf4qJldQPV6YOBbWeRnXxlWcLkxYxZ/NyuUc4R0x1Mmm','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(59,'10512','$2b$12$tq8kv8VEIMf4qJldQPV6YOBbWeRnXxlWcLkxYxZ/NyuUc4R0x1Mmm','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(60,'10512','$2b$12$tq8kv8VEIMf4qJldQPV6YOBbWeRnXxlWcLkxYxZ/NyuUc4R0x1Mmm','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(61,'10512','$2b$12$tq8kv8VEIMf4qJldQPV6YOBbWeRnXxlWcLkxYxZ/NyuUc4R0x1Mmm','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(62,'34526','$2b$12$k9DamWyhzxVK.ml5BCcLNevqIfep2FI4SWEeqrvhDGeg09jRCOlkW','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(63,'34526','$2b$12$k9DamWyhzxVK.ml5BCcLNevqIfep2FI4SWEeqrvhDGeg09jRCOlkW','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(64,'50142','$2b$12$d1uupYZHPzvti7Gi3m7Kp.zJ0YZCj6ABGQFKwVTSRQJ9x2Es600QC','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(65,'34526','$2b$12$k9DamWyhzxVK.ml5BCcLNevqIfep2FI4SWEeqrvhDGeg09jRCOlkW','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(66,'50142','$2b$12$d1uupYZHPzvti7Gi3m7Kp.zJ0YZCj6ABGQFKwVTSRQJ9x2Es600QC','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(67,'34234','$2b$12$H6/pwRdXKQxRzrk29wkAzuv28y4B0ndX7VFGrHSzsSAjtcBzPvuba','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(68,'50142','$2b$12$d1uupYZHPzvti7Gi3m7Kp.zJ0YZCj6ABGQFKwVTSRQJ9x2Es600QC','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(69,'34234','$2b$12$H6/pwRdXKQxRzrk29wkAzuv28y4B0ndX7VFGrHSzsSAjtcBzPvuba','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(70,'34234','$2b$12$H6/pwRdXKQxRzrk29wkAzuv28y4B0ndX7VFGrHSzsSAjtcBzPvuba','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(71,'34234','$2b$12$H6/pwRdXKQxRzrk29wkAzuv28y4B0ndX7VFGrHSzsSAjtcBzPvuba','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(72,'34526','$2b$12$k9DamWyhzxVK.ml5BCcLNevqIfep2FI4SWEeqrvhDGeg09jRCOlkW','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(73,'34234','$2b$12$H6/pwRdXKQxRzrk29wkAzuv28y4B0ndX7VFGrHSzsSAjtcBzPvuba','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(74,'50142','$2b$12$d1uupYZHPzvti7Gi3m7Kp.zJ0YZCj6ABGQFKwVTSRQJ9x2Es600QC','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',NULL,0),(75,'50142','$2b$12$d1uupYZHPzvti7Gi3m7Kp.zJ0YZCj6ABGQFKwVTSRQJ9x2Es600QC','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(76,'50142','$2b$12$d1uupYZHPzvti7Gi3m7Kp.zJ0YZCj6ABGQFKwVTSRQJ9x2Es600QC','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(77,'34526','$2b$12$k9DamWyhzxVK.ml5BCcLNevqIfep2FI4SWEeqrvhDGeg09jRCOlkW','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(78,'34234','$2b$12$H6/pwRdXKQxRzrk29wkAzuv28y4B0ndX7VFGrHSzsSAjtcBzPvuba','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(79,'34234','$2b$12$H6/pwRdXKQxRzrk29wkAzuv28y4B0ndX7VFGrHSzsSAjtcBzPvuba','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(80,'34526','$2b$12$k9DamWyhzxVK.ml5BCcLNevqIfep2FI4SWEeqrvhDGeg09jRCOlkW','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(81,'34234','$2b$12$H6/pwRdXKQxRzrk29wkAzuv28y4B0ndX7VFGrHSzsSAjtcBzPvuba','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(82,'34526','$2b$12$k9DamWyhzxVK.ml5BCcLNevqIfep2FI4SWEeqrvhDGeg09jRCOlkW','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(83,'34526','$2b$12$k9DamWyhzxVK.ml5BCcLNevqIfep2FI4SWEeqrvhDGeg09jRCOlkW','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(84,'34234','$2b$12$H6/pwRdXKQxRzrk29wkAzuv28y4B0ndX7VFGrHSzsSAjtcBzPvuba','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(85,'34526','$2b$12$k9DamWyhzxVK.ml5BCcLNevqIfep2FI4SWEeqrvhDGeg09jRCOlkW','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(86,'34234','$2b$12$H6/pwRdXKQxRzrk29wkAzuv28y4B0ndX7VFGrHSzsSAjtcBzPvuba','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0),(87,'34526','$2b$12$k9DamWyhzxVK.ml5BCcLNevqIfep2FI4SWEeqrvhDGeg09jRCOlkW','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0);
/*!40000 ALTER TABLE `login_activity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `public_holidays`
--

DROP TABLE IF EXISTS `public_holidays`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `public_holidays` (
  `holiday_id` int(11) NOT NULL AUTO_INCREMENT,
  `holiday_name` varchar(100) NOT NULL,
  `holiday_date` date DEFAULT NULL,
  `is_deleted` tinyint(1) DEFAULT NULL,
  `userid` int(11) NOT NULL,
  `editor` varchar(20) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL,
  `date_updated` datetime DEFAULT NULL,
  PRIMARY KEY (`holiday_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `public_holidays`
--

LOCK TABLES `public_holidays` WRITE;
/*!40000 ALTER TABLE `public_holidays` DISABLE KEYS */;
/*!40000 ALTER TABLE `public_holidays` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff_supervisors`
--

DROP TABLE IF EXISTS `staff_supervisors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `staff_supervisors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `supervisor_payroll_no` int(11) NOT NULL,
  `payroll_no` int(11) NOT NULL,
  `note` varchar(350) DEFAULT NULL,
  `is_deleted` tinyint(1) DEFAULT NULL,
  `userid` int(11) NOT NULL,
  `editor` varchar(20) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL,
  `date_updated` datetime DEFAULT NULL,
  PRIMARY KEY (`id`,`payroll_no`),
  KEY `payroll_no` (`payroll_no`),
  CONSTRAINT `staff_supervisors_ibfk_1` FOREIGN KEY (`payroll_no`) REFERENCES `employee_registration` (`payroll_no`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff_supervisors`
--

LOCK TABLES `staff_supervisors` WRITE;
/*!40000 ALTER TABLE `staff_supervisors` DISABLE KEYS */;
INSERT INTO `staff_supervisors` VALUES (1,34526,10512,NULL,1,1,'001','2019-04-02 04:57:01','2019-04-02 04:57:01'),(2,34526,10512,NULL,0,1,'001','2019-04-02 06:56:59','2019-04-02 06:56:59'),(3,34526,34526,NULL,0,1,'001','2019-04-02 07:10:07','2019-04-02 07:10:07'),(4,34234,50142,NULL,0,1,'001','2019-04-03 07:41:40','2019-04-03 07:41:40'),(5,34526,34234,NULL,0,1,'001','2019-04-03 07:41:40','2019-04-03 07:41:40');
/*!40000 ALTER TABLE `staff_supervisors` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-04  7:15:25
