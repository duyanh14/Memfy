-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 29, 2021 at 10:55 PM
-- Server version: 10.1.45-MariaDB
-- PHP Version: 5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `zjrfpnjq_memfy`
--

-- --------------------------------------------------------

--
-- Table structure for table `banner`
--

CREATE TABLE `banner` (
  `id` int(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `image` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `disable` int(1) NOT NULL,
  `date` bigint(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `banner`
--

INSERT INTO `banner` (`id`, `title`, `image`, `url`, `disable`, `date`) VALUES
(1, ':o', 'https://scontent.fhan5-8.fna.fbcdn.net/v/t1.15752-9/s2048x2048/245597136_409472547398218_7816266873269883972_n.jpg?_nc_cat=110&ccb=1-5&_nc_sid=ae9488&_nc_ohc=PVbyyDh1-D0AX8Cbld8&_nc_ht=scontent.fhan5-8.fna&oh=8fc91632d6fedb7ee5e18367633dc241&oe=619EC2D9', 'https://kickey.net', 1, 1635314989),
(2, 'hu wa', 'https://scontent.xx.fbcdn.net/v/t1.15752-9/245342722_3076854555892860_5989290048710825241_n.jpg?_nc_cat=107&ccb=1-5&_nc_sid=ae9488&_nc_ohc=nx6yflcan4oAX90er5D&tn=c8ClBzeSOvXiBn2P&_nc_ht=scontent.xx&oh=705c0a9611c8cd9e79e09691df1f301d&oe=619CA77F', 'https://kickey.net', 1, 1635314999);

-- --------------------------------------------------------

--
-- Table structure for table `hardware`
--

CREATE TABLE `hardware` (
  `id` varchar(255) NOT NULL,
  `date` bigint(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hardware`
--

INSERT INTO `hardware` (`id`, `date`) VALUES
('21b78967fdd2f016c0c97b4453bafb25', 1635286171),
('4e1bcb5f8c7ae239773df22999811609', 1635512134),
('538ad8889d0cb4fc2a8d1782bf11eb2a', 1635510276),
('5bea395a288703d39c769b5af2bfe5e2', 1635512698),
('651690af64d6afce0be8a5dc52d393f8', 1635514426),
('654a5ca7523a8c9896e66fcf7c89bfc3', 1635508877),
('7e52102fffc16bd4baa45c97355d996a', 1635511177),
('9033a3755d885bdc33181220bd324c68', 1635510654),
('98524e867ab985df68fafcc09ee63ed6', 1635511423),
('9e20b1d5184a144a2b44ac524e5c1f84', 1635513066),
('a21b8344b844e845386d60e11aabeae4', 1635526821),
('b430a63ce19b7535b9984432ed69e6fe', 1635325875),
('d21b2da122250aa4c67fa88a94f53c3e', 1635518641),
('d55c2d865375d8ce3893791f59d8c750', 1635524240),
('e3269bbe2efc3319a2c9d514255ee1df', 1635511406),
('fee5b6e001a4e5dcc31ebb73fd0ca3bb', 1635511105);

-- --------------------------------------------------------

--
-- Table structure for table `hardware_active`
--

CREATE TABLE `hardware_active` (
  `id` int(255) NOT NULL,
  `hardware` varchar(255) NOT NULL,
  `date` bigint(255) NOT NULL,
  `ip` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hardware_active`
--

INSERT INTO `hardware_active` (`id`, `hardware`, `date`, `ip`) VALUES
(1171, '654a5ca7523a8c9896e66fcf7c89bfc3', 1635508877, '27.72.31.30'),
(1173, '538ad8889d0cb4fc2a8d1782bf11eb2a', 1635510276, '14.232.133.20'),
(1174, '9033a3755d885bdc33181220bd324c68', 1635510654, '42.119.72.206'),
(1175, 'fee5b6e001a4e5dcc31ebb73fd0ca3bb', 1635511105, '42.113.158.153'),
(1176, '7e52102fffc16bd4baa45c97355d996a', 1635511177, '27.66.71.150'),
(1177, 'e3269bbe2efc3319a2c9d514255ee1df', 1635511406, '116.107.56.124'),
(1178, '98524e867ab985df68fafcc09ee63ed6', 1635511423, '58.186.53.131'),
(1179, '98524e867ab985df68fafcc09ee63ed6', 1635511425, '58.186.53.131'),
(1180, '4e1bcb5f8c7ae239773df22999811609', 1635512134, '14.248.150.174'),
(1181, '5bea395a288703d39c769b5af2bfe5e2', 1635512698, '27.79.228.12'),
(1182, '9e20b1d5184a144a2b44ac524e5c1f84', 1635513066, '125.212.172.101'),
(1183, '651690af64d6afce0be8a5dc52d393f8', 1635514426, '14.182.147.252'),
(1184, '654a5ca7523a8c9896e66fcf7c89bfc3', 1635515517, '27.72.31.30'),
(1185, 'd21b2da122250aa4c67fa88a94f53c3e', 1635518641, '1.53.89.142'),
(1186, 'd21b2da122250aa4c67fa88a94f53c3e', 1635520272, '1.53.89.142'),
(1187, 'd55c2d865375d8ce3893791f59d8c750', 1635524240, '1.53.227.110'),
(1188, '651690af64d6afce0be8a5dc52d393f8', 1635526682, '14.182.147.252'),
(1189, 'a21b8344b844e845386d60e11aabeae4', 1635526821, '74.125.212.78'),
(1190, '21b78967fdd2f016c0c97b4453bafb25', 1635543903, '27.72.31.30');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `banner`
--
ALTER TABLE `banner`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hardware`
--
ALTER TABLE `hardware`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hardware_active`
--
ALTER TABLE `hardware_active`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `banner`
--
ALTER TABLE `banner`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `hardware_active`
--
ALTER TABLE `hardware_active`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1191;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
