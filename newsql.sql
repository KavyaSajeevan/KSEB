/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - python_kseb_fisat
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`python_kseb_fisat` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `python_kseb_fisat`;

/*Table structure for table `bill` */

DROP TABLE IF EXISTS `bill`;

CREATE TABLE `bill` (
  `bill_id` int(50) NOT NULL AUTO_INCREMENT,
  `cons_id` int(50) DEFAULT NULL,
  `usage` varchar(200) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `reading_id` int(50) DEFAULT NULL,
  `bill_date` date DEFAULT NULL,
  `pay_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`bill_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `bill` */

insert  into `bill`(`bill_id`,`cons_id`,`usage`,`amount`,`reading_id`,`bill_date`,`pay_status`) values 
(4,11,'50','160.0',7,'2020-03-11','Payed'),
(5,14,'1350','10125.0',9,'2025-03-04','Payed'),
(6,14,'50','160.0',10,'2025-03-08','Payed'),
(7,14,'50','160.0',11,'2025-03-09','Payed'),
(8,15,'200','640.0',12,'2025-03-09','Payed'),
(9,15,'1','3.2',13,'2025-03-09','Payed');

/*Table structure for table `bill_prediction` */

DROP TABLE IF EXISTS `bill_prediction`;

CREATE TABLE `bill_prediction` (
  `prediction_id` int(11) NOT NULL AUTO_INCREMENT,
  `cons_id` int(11) DEFAULT NULL,
  `fanUsage` varchar(100) DEFAULT NULL,
  `refrigeratorUsage` varchar(100) DEFAULT NULL,
  `acUsage` varchar(100) DEFAULT NULL,
  `tvUsage` varchar(100) DEFAULT NULL,
  `monitorUsage` varchar(100) DEFAULT NULL,
  `motorPumpUsage` varchar(100) DEFAULT NULL,
  `temp` varchar(100) DEFAULT NULL,
  `humidity` varchar(100) DEFAULT NULL,
  `monthlyHours` varchar(100) DEFAULT NULL,
  `tariffRate` varchar(100) DEFAULT NULL,
  `bill_amount` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`prediction_id`)
) ENGINE=MyISAM AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;

/*Data for the table `bill_prediction` */

insert  into `bill_prediction`(`prediction_id`,`cons_id`,`fanUsage`,`refrigeratorUsage`,`acUsage`,`tvUsage`,`monitorUsage`,`motorPumpUsage`,`temp`,`humidity`,`monthlyHours`,`tariffRate`,`bill_amount`) values 
(1,14,'85','855','55','55','85','88','88','88','88','88','4278.8643'),
(2,14,'22','23','0','21','1','0','5.496','78.2','492','8.5','4278.8643'),
(3,14,'8','20','2','8','1','0','5.678','78.1','546','8.5','4278.8643'),
(4,14,'33','66','66','66','9','4','7','9','33','99','55868.58'),
(5,14,'2','22','66','9933','6669','9','2','3','36','66','241905.02'),
(6,14,'66','9','36','85','63','69','25','36','85','25','None'),
(7,14,'66','9','36','85','63','69','25','36','85','25','21390.389'),
(8,14,'36','25','9','36','96','36','25','36','36','66','34860.27'),
(9,14,'36','25','9','36','96','36','25','36','36','66','34860.27'),
(10,14,'5','96','36','25','36','96','36','9','33','69','None'),
(11,14,'36','25','96','39','36','23','36','9','9','3','None'),
(12,14,'25','66','25','366','99','96','25','66','36','25','27751.549'),
(13,14,'7','22','3','21','1','0','6.121','75','475','9.2','None'),
(14,14,'2','36','25','63','399','39','23','36','36','2.9','None'),
(15,14,'22','36','25','63','399','39','23','36','36','2.9','None'),
(16,14,'8','20','2','8','1','0','5.678','78.1','546','8.5','None'),
(17,14,'8','20','2','8','1','0','5.678','78.1','546','8.5','4633.149'),
(18,14,'8','20','2','8','1','0','5.678','78.1','546','8.5','None'),
(19,14,'8','20','2','8','1','0','5.678','78.1','546','8.5','4633.149'),
(20,14,'5','19','2','20','1','0','5.471','76.7','493','9.2','None'),
(21,14,'15','22','0','20','1','0','4.769','75.6','494','8.2','None'),
(22,14,'15','22','0','20','1','0','4.769','75.6','494','8.2','None'),
(23,14,'15','22','0','20','1','0','4.769','75.6','494','8.2','3988.549'),
(24,14,'33','6','3','33','66','66','3.99','6.6','996','99','None'),
(25,14,'33','6','3','33','66','66','3.99','6.6','996','99','61414.727'),
(26,14,'52','55','52','55','22','55','3.9','6.9','66','66','0.0'),
(27,14,'55','55','55','5555','33','55','22.99','33.9','555','55','95497.28'),
(28,14,'55','55','55','5555','33','55','22.99','33.9','555','55','95497.28'),
(29,14,'66','66','96','96','66','96','3.99','999','96','99','None'),
(30,14,'66','66','96','96','66','96','3.99','999','96','99','None'),
(31,14,'66','66','96','96','66','96','3.99','999','96','99','60625.555'),
(32,14,'6666','66','66','66','66','66','66','6696','33','666','None'),
(33,14,'6666','66','66','66','66','66','66','6696','33','666','406714.78'),
(34,14,'6666','66','66','66','66','66','66','6696','33','666','406714.78'),
(35,14,'33','6363','33','63','33','33','66','33','36','33','None'),
(36,14,'66','33','33','63','33','33','33','33','33','63','None'),
(37,14,'66','33','33','63','33','33','33','33','33','63','33077.78'),
(38,14,'33','33','33','66','33','3','3.9','3.9','33','66','35467.277'),
(39,14,'3399','99','99','99','99','66','99','699','99','66','70432.805'),
(40,14,'33','63','36','366','66','66','3.9','6.9','33','33','25164.547'),
(41,14,'33','3333','33','36','669','39','3.9','36.9','666','66','151947.12'),
(42,14,'66','66','666','33','66','36','6.99','6.9','33','33','57097.992'),
(43,14,'5','21','3','17','1','0','4.382','76.9','447','9.1','4161.2817'),
(44,14,'14','22','3','17','1','0','4.382','76.9','447','9.1','4146.624'),
(45,14,'7','20','0','18','1','0','4.735','74.3','307','8.2','2532.1099'),
(46,14,'22','22','3','17','1','0','4.92','73.7','699','9.1','6316.9937'),
(47,14,'22','33','66','36','33','33','3.9','6.9','399','33','20541.514'),
(48,15,'7','20','0','18','1','0','4.735','74.3','307','8.2','2532.1099');

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `comp_id` int(50) NOT NULL AUTO_INCREMENT,
  `cons_id` int(50) DEFAULT NULL,
  `complaints` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`comp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

insert  into `complaints`(`comp_id`,`cons_id`,`complaints`,`date`,`status`) values 
(5,11,'fgxc','2020-03-11','.km.kjn'),
(6,11,'bshs','2020-03-11','NA'),
(7,11,'bzb','2020-03-11','NA'),
(8,14,'hhd','2025-03-09','NA'),
(9,15,'jdjd','2025-03-09','NA');

/*Table structure for table `consumers` */

DROP TABLE IF EXISTS `consumers`;

CREATE TABLE `consumers` (
  `cons_id` int(50) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `f_name` varchar(100) DEFAULT NULL,
  `l_name` varchar(100) DEFAULT NULL,
  `h_name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `pincode` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `connectiontype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`cons_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `consumers` */

insert  into `consumers`(`cons_id`,`login_id`,`f_name`,`l_name`,`h_name`,`place`,`pincode`,`phone`,`email`,`connectiontype`) values 
(9,NULL,'vipinnnnn','kaimal','sreenilay','malakkara','689532','9744423271','vipinmkaimal@gmail.com',NULL),
(11,19,'kkk','kli','kli','kli','987778','9877899876','guyv@fd.gd','Home'),
(14,22,'ann maryanna','anna','ann maryanna house','kochi','691333','6255545484','shemi96ven@gmail.com','Industrial'),
(15,23,'kavya','kr','kavya house','kochi','691333','9874561230','kavya@gmail.com','Home');

/*Table structure for table `employee` */

DROP TABLE IF EXISTS `employee`;

CREATE TABLE `employee` (
  `emp_id` int(50) NOT NULL AUTO_INCREMENT,
  `login_id` int(50) DEFAULT NULL,
  `f_name` varchar(100) DEFAULT NULL,
  `l_name` varchar(100) DEFAULT NULL,
  `h_name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `qualification` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `employee` */

insert  into `employee`(`emp_id`,`login_id`,`f_name`,`l_name`,`h_name`,`place`,`email`,`phone`,`qualification`) values 
(4,11,'vipin','kaimal','sreenilay','malakkara','vipinmkaimal@gmail.com','9744423271','mca'),
(5,14,'vipin','kaimal','sreenilay','malakkara','vipinmkaimal@gmail.com','9744423271','mca');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(50) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `login_type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`login_type`) values 
(1,'admin@','admin@','admin'),
(2,'asd','asd','employee'),
(3,'asd','asd','employee'),
(4,'asd','asd','employee'),
(5,'vipin','vipin','employee'),
(6,'vipin','vipin','employee'),
(7,'vipin','vipin','employee'),
(8,'aaa','aaaa','consumers'),
(9,'qwerty','asd','consumers'),
(10,'vipin','vipin','employee'),
(11,'vipin','vipin','employee'),
(12,'vipin','vipin','consumers'),
(13,'aaa','ppp','employee'),
(14,'vipin','vipin','employee'),
(15,'kkj','kkj','consumers'),
(16,'kkj','kkj','consumers'),
(17,'kli','kli','consumers'),
(18,'kil','kil','consumers'),
(19,'oi','oi','consumers'),
(22,'u','u','consumers'),
(23,'kavya@gmail.com','kavya@gmail.com','consumers');

/*Table structure for table `meter_reading` */

DROP TABLE IF EXISTS `meter_reading`;

CREATE TABLE `meter_reading` (
  `reading_id` int(50) NOT NULL AUTO_INCREMENT,
  `cons_id` int(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` int(50) DEFAULT NULL,
  `cur_reading` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`reading_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `meter_reading` */

insert  into `meter_reading`(`reading_id`,`cons_id`,`date`,`time`,`cur_reading`) values 
(7,11,'2020-03-11',63356,'50'),
(8,14,'2025-02-21',150730,'150'),
(9,14,'2025-03-04',225018,'1500'),
(10,14,'2025-03-08',235909,'200'),
(11,14,'2025-03-09',10411,'200'),
(12,15,'2025-03-09',121205,'200'),
(13,15,'2025-03-09',121307,'201');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `noti_id` int(50) NOT NULL AUTO_INCREMENT,
  `notificationtype` varchar(100) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`noti_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`noti_id`,`notificationtype`,`description`,`date`) values 
(1,'Home','djfghieged','2020-03-10'),
(3,'Industrial','rdtfghjk','2020-03-10');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `pay_id` int(50) NOT NULL AUTO_INCREMENT,
  `bill_id` varchar(100) DEFAULT NULL,
  `cons_id` int(50) DEFAULT NULL,
  `amount` int(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`pay_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`pay_id`,`bill_id`,`cons_id`,`amount`,`date`) values 
(2,'4',11,160,'2020-03-11'),
(3,'5',14,10125,'2025-03-04'),
(4,'6',14,160,'2025-03-09'),
(5,'7',14,160,'2025-03-09'),
(6,'7',14,160,'2025-03-09'),
(7,'7',14,160,'2025-03-09'),
(8,'8',15,640,'2025-03-09'),
(9,'9',15,3,'2025-03-09');

/*Table structure for table `prediction` */

DROP TABLE IF EXISTS `prediction`;

CREATE TABLE `prediction` (
  `pred_id` int(50) NOT NULL AUTO_INCREMENT,
  `area_id` int(50) DEFAULT NULL,
  `no_of_consumers` int(100) DEFAULT NULL,
  `avg_temp` varchar(100) DEFAULT NULL,
  `avg_rainfall` varchar(100) DEFAULT NULL,
  `no_of_holidays` varchar(100) DEFAULT NULL,
  `humidity` varchar(100) DEFAULT NULL,
  `predicted_usage` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pred_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `prediction` */

/*Table structure for table `tariff` */

DROP TABLE IF EXISTS `tariff`;

CREATE TABLE `tariff` (
  `tariff_if` int(11) NOT NULL AUTO_INCREMENT,
  `connection_type` varchar(100) DEFAULT NULL,
  `minimum_usage` varchar(100) DEFAULT NULL,
  `maximum_usage` varchar(100) DEFAULT NULL,
  `amount_per_unit` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`tariff_if`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `tariff` */

insert  into `tariff`(`tariff_if`,`connection_type`,`minimum_usage`,`maximum_usage`,`amount_per_unit`) values 
(1,'hj','30','60','1000');

/*Table structure for table `wallet` */

DROP TABLE IF EXISTS `wallet`;

CREATE TABLE `wallet` (
  `wallet_id` int(11) NOT NULL AUTO_INCREMENT,
  `cons_id` int(11) DEFAULT NULL,
  `transaction_amount` decimal(10,0) DEFAULT NULL,
  `transaction_type` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`wallet_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `wallet` */

insert  into `wallet`(`wallet_id`,`cons_id`,`transaction_amount`,`transaction_type`,`date`) values 
(1,11,1000,'credit','2020-03-11'),
(2,11,1000,'credit','2020-03-11'),
(3,11,100,'credit','2020-03-11'),
(4,11,100,'credit','2020-03-11'),
(6,11,160,'debit','2020-03-11'),
(7,14,2000,'credit','2025-03-04'),
(8,14,200,'credit','2025-03-09'),
(9,15,200,'credit','2025-03-09'),
(10,15,300,'credit','2025-03-09'),
(11,15,3,'debit','2025-03-09');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
