-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 30, 2022 at 10:49 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.0.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tollbooth_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `id` int(11) NOT NULL,
  `nameofcarowner` varchar(50) NOT NULL,
  `numberplate` varchar(10) NOT NULL,
  `phonenumber` varchar(20) NOT NULL,
  `distancefrom` varchar(20) NOT NULL,
  `destinationto` varchar(20) NOT NULL,
  `amount` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`id`, `nameofcarowner`, `numberplate`, `phonenumber`, `distancefrom`, `destinationto`, `amount`) VALUES
(1, 'Angela', 'KDE 835R', '+254707690637', 'Syokimau', 'Arthi river', 300);

-- --------------------------------------------------------

--
-- Table structure for table `vehicle`
--

CREATE TABLE `vehicle` (
  `id` int(11) NOT NULL,
  `nameofowner` varchar(50) NOT NULL,
  `idnumber` int(10) NOT NULL,
  `phonenumber` varchar(20) NOT NULL,
  `residence` varchar(20) NOT NULL,
  `cartype` varchar(20) NOT NULL,
  `numberplate` varchar(20) NOT NULL,
  `modelname` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Vehicles Registration';

--
-- Dumping data for table `vehicle`
--

INSERT INTO `vehicle` (`id`, `nameofowner`, `idnumber`, `phonenumber`, `residence`, `cartype`, `numberplate`, `modelname`) VALUES
(1, 'angela', 5678906, '254707690637', 'Nairobi', 'Demio', 'KCA 456N', 'Mazda'),
(2, 'Eric Dan', 2147483647, '254707690637', 'Thika', 'Toyota', 'KBA 345H', 'Premio'),
(3, 'Alice Zane', 26789645, '+254707690637', 'Nairobi', 'Nissan', 'KEB 423B', 'Note'),
(4, 'Maina Jan', 23456789, '254707690637', 'Nairobi', 'Nissan', 'KCE 269H', 'March'),
(5, 'Angela', 34563456, '254707690637', 'Nairobi', 'Totota', 'KDU 234Y', 'Premio'),
(6, 'Neo Lee', 78963849, '254707690637', 'Kileleshwa', 'Audi', 'KCF 324Y', 'A3'),
(7, 'Dan Joseph', 2147483647, '+254707690637', 'Nairobi', 'Nissan', 'KRA 283U', 'Jeep');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `vehicle`
--
ALTER TABLE `vehicle`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `vehicle`
--
ALTER TABLE `vehicle`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
