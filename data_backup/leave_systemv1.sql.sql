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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departments`
--

LOCK TABLES `departments` WRITE;
/*!40000 ALTER TABLE `departments` DISABLE KEYS */;
INSERT INTO `departments` VALUES (1,'Management','All those allowed to approve leave',0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(2,'Operation','Other staff members ',0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17');
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
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `designation`
--

LOCK TABLES `designation` WRITE;
/*!40000 ALTER TABLE `designation` DISABLE KEYS */;
INSERT INTO `designation` VALUES (1,' HR Manager','description',NULL,1,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(2,'Director','description',NULL,1,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(3,'Deputy Director–Clinical','description',NULL,1,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(4,'Deputy Director – SI','description',NULL,1,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(5,'Deputy Director  - SSD','description',NULL,1,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(6,' Coordinators','description',NULL,1,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(7,'SCLARO','description',NULL,1,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(8,'Office Assistants','description',NULL,2,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(9,'County Mentorship Lead','description',NULL,2,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(10,'Clinical Program officer','description',NULL,2,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(11,'Biostatistician','description',NULL,2,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(12,'Data Analyst','description',NULL,2,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(13,'MLE Officer','description',NULL,2,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(14,'Accountant','description',NULL,2,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(15,'Assistant MLE Manager','description',NULL,2,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(16,'ICT Manager','description',NULL,2,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(17,'Facility HTS Lead','description',NULL,2,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(18,'Evaluation/STEP Assistant','description',NULL,2,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(19,'VMMC Incharge','description',NULL,2,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(20,'EIMC LEAD','description',NULL,2,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(21,'VMMC EIMC Lead mobilizer','description',NULL,2,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(22,'VMMC Mobilizers','description',NULL,2,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(23,'Transport Manager','description',NULL,2,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(24,'Drivers','description',NULL,2,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(25,'Motorcycle riders','description',NULL,2,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(26,'SCLARO','description',NULL,2,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(27,'IRA','description',NULL,2,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(28,'SC/ICT /EMR officer','description',NULL,2,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(29,'ICT Assistant','description',NULL,2,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(30,'PROGRAMMER','description',NULL,2,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(31,'Assistant Programmer','description',NULL,2,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(32,' SECURITY GUARD','description',NULL,2,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(33,' SCMLE Officer','description',NULL,2,2,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_registration`
--

LOCK TABLES `employee_registration` WRITE;
/*!40000 ALTER TABLE `employee_registration` DISABLE KEYS */;
INSERT INTO `employee_registration` VALUES (1,10101,'Admin','Leave System','2004-12-01 00:00:00','1','2004-12-01 00:00:00','500000',1,'Faces','Permanent','eagik@kemri-ucsf.org','0780698944','Mbita','Kenyan','27358109','Single','JK','9090909','','','','','','',0,0,1,'001','2019-04-05 07:15:38','2019-04-05 07:15:38','LeaveAdmin@10101','$2b$12$GVJGjdZRoOU8vre3Lzd6tOIFOXgs5RlbMSMC4OuwtzvWlPLhfWtdS',NULL,NULL,NULL,NULL);
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `initial_leave_balance`
--

LOCK TABLES `initial_leave_balance` WRITE;
/*!40000 ALTER TABLE `initial_leave_balance` DISABLE KEYS */;
INSERT INTO `initial_leave_balance` VALUES (1,10101,10,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17');
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leave_applications`
--

LOCK TABLES `leave_applications` WRITE;
/*!40000 ALTER TABLE `leave_applications` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leave_approval`
--

LOCK TABLES `leave_approval` WRITE;
/*!40000 ALTER TABLE `leave_approval` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leave_authorization`
--

LOCK TABLES `leave_authorization` WRITE;
/*!40000 ALTER TABLE `leave_authorization` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leave_reliever`
--

LOCK TABLES `leave_reliever` WRITE;
/*!40000 ALTER TABLE `leave_reliever` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leave_types`
--

LOCK TABLES `leave_types` WRITE;
/*!40000 ALTER TABLE `leave_types` DISABLE KEYS */;
INSERT INTO `leave_types` VALUES (1,'Annual Leave',30,0,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(2,'Maternity Leave -',90,0,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(3,'Paternity Leave',14,0,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(4,'Sick Leave ',10,0,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(5,'Compassionate',10,0,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(6,'Study Leave',10,0,0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_activity`
--

LOCK TABLES `login_activity` WRITE;
/*!40000 ALTER TABLE `login_activity` DISABLE KEYS */;
INSERT INTO `login_activity` VALUES (1,'10101','$2b$12$GVJGjdZRoOU8vre3Lzd6tOIFOXgs5RlbMSMC4OuwtzvWlPLhfWtdS','active',NULL,NULL,'127.0.0.1','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',NULL,0);
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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `public_holidays`
--

LOCK TABLES `public_holidays` WRITE;
/*!40000 ALTER TABLE `public_holidays` DISABLE KEYS */;
INSERT INTO `public_holidays` VALUES (1,'Christmas Day','2019-12-25',0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(2,'Boxing Day 26th','2019-12-26',0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(3,'Labour Day','2019-05-01',0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(4,'Madaraka Day','2019-06-01',0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(5,'Mashujaa Day','2019-10-20',0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(6,'Jamhuri (Independence) Day','2019-12-12',0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(7,'New Year\'s Day','2020-01-01',0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(8,'Good Friday ','2019-04-19',0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17'),(9,'Easter Monday','2019-04-22',0,1,'001','2019-04-05 07:47:17','2019-04-05 07:47:17');
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff_supervisors`
--

LOCK TABLES `staff_supervisors` WRITE;
/*!40000 ALTER TABLE `staff_supervisors` DISABLE KEYS */;
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

-- Dump completed on 2019-04-05  8:53:02
