-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 23, 2024 at 11:40 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `social_media`
--

-- --------------------------------------------------------

--
-- Table structure for table `friendships`
--

CREATE TABLE `friendships` (
  `user1` varchar(50) NOT NULL,
  `user2` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `friendships`
--

INSERT INTO `friendships` (`user1`, `user2`) VALUES
('anya', 'kal'),
('anya', 'mallows'),
('anya', 'moonie'),
('kal', 'anya'),
('kal', 'mallows'),
('mallows', 'anya'),
('mallows', 'kal'),
('moonie', 'anya');

-- --------------------------------------------------------

--
-- Table structure for table `friend_requests`
--

CREATE TABLE `friend_requests` (
  `from_user` varchar(50) NOT NULL,
  `to_user` varchar(50) NOT NULL,
  `status` enum('pending','accepted','rejected') DEFAULT 'pending'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `friend_requests`
--

INSERT INTO `friend_requests` (`from_user`, `to_user`, `status`) VALUES
('anya', 'kal', 'accepted'),
('kal', 'mallows', 'accepted'),
('mallows', 'anya', 'accepted'),
('moonie', 'anya', 'accepted');

-- --------------------------------------------------------

--
-- Table structure for table `social_media_link`
--

CREATE TABLE `social_media_link` (
  `link` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `social_media_link`
--

INSERT INTO `social_media_link` (`link`) VALUES
('');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `username` varchar(50) NOT NULL,
  `age` int(11) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `interests` text DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `social_media_link` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`username`, `age`, `location`, `gender`, `interests`, `password`, `social_media_link`) VALUES
('anya', 2, 'cat land', 'F', 'bubong', 'anya', 'https//wagniyokopababainsabubong.com'),
('kal', 19, 'taguig', 'F', 'cats, lloyd', 'kal', 'https//misskonasiya.com'),
('mallows', 2, 'cat land', 'F', 'lloyd', 'mallows', 'https//ineedmorepetting.com'),
('moonie', 3, 'taguig', 'F', '', 'moonie', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `friendships`
--
ALTER TABLE `friendships`
  ADD PRIMARY KEY (`user1`,`user2`),
  ADD KEY `user2` (`user2`);

--
-- Indexes for table `friend_requests`
--
ALTER TABLE `friend_requests`
  ADD PRIMARY KEY (`from_user`,`to_user`),
  ADD KEY `to_user` (`to_user`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`username`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `friendships`
--
ALTER TABLE `friendships`
  ADD CONSTRAINT `friendships_ibfk_1` FOREIGN KEY (`user1`) REFERENCES `users` (`username`) ON DELETE CASCADE,
  ADD CONSTRAINT `friendships_ibfk_2` FOREIGN KEY (`user2`) REFERENCES `users` (`username`) ON DELETE CASCADE;

--
-- Constraints for table `friend_requests`
--
ALTER TABLE `friend_requests`
  ADD CONSTRAINT `friend_requests_ibfk_1` FOREIGN KEY (`from_user`) REFERENCES `users` (`username`) ON DELETE CASCADE,
  ADD CONSTRAINT `friend_requests_ibfk_2` FOREIGN KEY (`to_user`) REFERENCES `users` (`username`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
