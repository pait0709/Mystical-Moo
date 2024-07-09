CREATE DATABASE  IF NOT EXISTS `mystical_moo` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `mystical_moo`;
-- MySQL dump 10.13  Distrib 8.0.32, for macos13 (x86_64)
--
-- Host: localhost    Database: mystical_moo
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `coupon`
--

DROP TABLE IF EXISTS `coupon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coupon` (
  `coupon_id` int NOT NULL AUTO_INCREMENT,
  `discount` int NOT NULL,
  `valid_till` date NOT NULL,
  PRIMARY KEY (`coupon_id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Passwd` varchar(50) NOT NULL,
  `GST_id` varchar(40) NOT NULL,
  `house` varchar(50) NOT NULL,
  `street` varchar(50) NOT NULL,
  `pincode` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `holds`
--

DROP TABLE IF EXISTS `holds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `holds` (
  `h_cust_id` int NOT NULL,
  `h_coupon_id` int NOT NULL,
  PRIMARY KEY (`h_cust_id`,`h_coupon_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory` (
  `product_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` text,
  `rating` float DEFAULT NULL,
  `price` int NOT NULL,
  `discount` int DEFAULT NULL,
  `type` enum('Camel','Buffalo','Goat','Cow','Yak','Horse','Donkey') DEFAULT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=99 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Invoice`
--

DROP TABLE IF EXISTS `Invoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Invoice` (
  `gst_id` int NOT NULL,
  `inv_date` date NOT NULL,
  `inv_price` decimal(10,2) NOT NULL,
  `inv_payment_type` enum('Cash','Pre-Paid','Post-payment') NOT NULL,
  `inv_cust_id` int NOT NULL,
  `inv_order_id` int NOT NULL,
  PRIMARY KEY (`inv_cust_id`,`inv_order_id`),
  KEY `inv_order_id` (`inv_order_id`),
  CONSTRAINT `invoice_ibfk_1` FOREIGN KEY (`inv_cust_id`) REFERENCES `customer` (`id`),
  CONSTRAINT `invoice_ibfk_2` FOREIGN KEY (`inv_order_id`) REFERENCES `orders` (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `OrderProduct`
--

DROP TABLE IF EXISTS `OrderProduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `OrderProduct` (
  `order_product_quantity` int NOT NULL,
  `order_id` int NOT NULL,
  `order_product_id` int NOT NULL,
  PRIMARY KEY (`order_id`,`order_product_id`),
  KEY `order_product_id` (`order_product_id`),
  CONSTRAINT `orderproduct_ibfk_1` FOREIGN KEY (`order_product_id`) REFERENCES `inventory` (`product_id`),
  CONSTRAINT `orderproduct_ibfk_2` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `order_cust_id` int NOT NULL,
  `order_coupon_id` int DEFAULT NULL,
  `order_price` decimal(10,2) NOT NULL,
  `order_payment` enum('Cash','Pre-Paid','Post-payment') DEFAULT NULL,
  `order_status` enum('Fulfilled','Placed') DEFAULT NULL,
  PRIMARY KEY (`order_id`),
  KEY `order_cust_id` (`order_cust_id`),
  KEY `order_coupon_id` (`order_coupon_id`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`order_cust_id`) REFERENCES `customer` (`id`),
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`order_coupon_id`) REFERENCES `coupon` (`coupon_id`)
) ENGINE=InnoDB AUTO_INCREMENT=305 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Shipping_Details`
--

DROP TABLE IF EXISTS `Shipping_Details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Shipping_Details` (
  `date_order` date NOT NULL,
  `date_fullfill` date NOT NULL,
  `shi_payment_type` enum('Cash','Pre-Paid','Post-payment') NOT NULL,
  `shi_cust_id` int NOT NULL,
  `shi_order_id` int NOT NULL,
  PRIMARY KEY (`shi_cust_id`,`shi_order_id`),
  KEY `shi_order_id` (`shi_order_id`),
  CONSTRAINT `shipping_details_ibfk_1` FOREIGN KEY (`shi_cust_id`) REFERENCES `customer` (`id`),
  CONSTRAINT `shipping_details_ibfk_2` FOREIGN KEY (`shi_order_id`) REFERENCES `orders` (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping events for database 'mystical_moo'
--

--
-- Dumping routines for database 'mystical_moo'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-11  0:00:43
