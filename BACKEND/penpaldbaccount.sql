-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 08, 2025 at 05:51 PM
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
-- Database: `penpaldb`
--

-- --------------------------------------------------------

--
-- Table structure for table `friendships`
--

CREATE TABLE `friendships` (
  `id` int(100) NOT NULL,
  `user1` varchar(50) NOT NULL,
  `user2` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `friend_requests`
--

CREATE TABLE `friend_requests` (
  `id` int(100) NOT NULL,
  `from_user` varchar(50) NOT NULL,
  `to_user` varchar(50) NOT NULL,
  `status` enum('pending','accepted','rejected') DEFAULT 'pending'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(100) NOT NULL,
  `username` varchar(50) NOT NULL,
  `age` int(11) NOT NULL,
  `location` varchar(100) DEFAULT NULL,
  `gender` enum('Male','Female','Other') DEFAULT NULL,
  `password` varchar(255) NOT NULL,
  `social_media_link` varchar(255) DEFAULT NULL,
  `gmail` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `age`, `location`, `gender`, `password`, `social_media_link`, `gmail`) VALUES
(4, 'MALLOWS_20', 25, 'Taguig CIty, Philippines', 'Female', '$argon2id$v=19$m=65536,t=3,p=4$wlhLaW3tfS8F4HxvjZGyVg$0Lz4A8PdoMJBAer3+SxCyB7zTkaTVKybUWBdDjfoVgU', 'https://www.instagram.com/mallows_cutie', 'mallows@gmail.com'),
(5, 'traveler_jay24', 26, 'Cebu City, Philippines', 'Male', '$argon2id$v=19$m=65536,t=3,p=4$BsCYE0LovXeOcS6llDImJA$GrXYH+JrN2mjuzxlyGHXUx6UwolAZfhhLtEhW3n/beE', 'https://www.facebook.com/travelerjay24', 'traveler.jay24@gmail.com'),
(6, 'foodie_mika89', 35, 'Quezon City, Philippines', 'Female', '$argon2id$v=19$m=65536,t=3,p=4$1Zqzds75fy8lBKAU4pzT2g$fcdyDCmSe0rFlQU1N/zDIzl/9rmdRVH0H5IRW3vtv7c', 'https://www.instagram.com/foodie.mika89', 'foodie.mika89@yahoo.com'),
(7, 'booklover_karen', 23, 'Davao City, Philippines', 'Female', '$argon2id$v=19$m=65536,t=3,p=4$NyaEsHZubU3JGSOk9N57Lw$YY8vMcmSKN2qU8VptQMTjGxt+r4ltZhjWNxFN1Co2Pk', 'https://twitter.com/bookloverkaren', 'karen.books01@gmail.com'),
(8, 'techy_mark22', 28, 'Manila, Philippines', 'Male', '$argon2id$v=19$m=65536,t=3,p=4$8p4TorT2nvP+n7PWuhfCOA$W51j8KSFAAkc0xOWkWkMgJdKq4A8bkH10DBSfErEUlk', 'https://www.linkedin.com/in/techymark22', 'mark.techy22@hotmail.com'),
(9, 'artistica_ella', 24, 'Tagaytay, Philippines', 'Female', '$argon2id$v=19$m=65536,t=3,p=4$bc1ZC8H4HyPkvDdGKAVAKA$v/M4HWbBRG1CVw6foaPm4eEDkH9NDiieo5ce5oAd5Kk', 'https://www.behance.net/artisticaella', 'ella.art@gmail.com'),
(10, 'gamer_lance', 25, 'Bacolod City, Philippines', 'Male', '$argon2id$v=19$m=65536,t=3,p=4$kTKmFEKIkRICIMTYew9BqA$oqjv9wLQZGIaQeFpMHee8NTfv0wgmsRBdxsQ2QEBdQQ', 'https://www.twitch.tv/gamerlance', 'gamer.lance99@outlook.com'),
(11, 'fashionista_bea', 25, 'Makati, Philippines', 'Female', '$argon2id$v=19$m=65536,t=3,p=4$s7a2NiakdK51zrnXGiMkxA$LNjgbKdtLJrfV/zpPqf4l5q41RMI0qGHIStzFwFf1cs', 'https://www.instagram.com/fashionistabea', 'bea.style@gmail.com'),
(12, 'moviebuff_jake', 29, 'Pasig City, Philippines', 'Male', '$argon2id$v=19$m=65536,t=3,p=4$m5Pyfi+F0Ppf613LGWPMmQ$jpgDRJCqSBM+DQKKv/XPwgRp4JpI1ayaRETgod19Ats', 'https://www.facebook.com/moviebuffjake', 'jake.movies@hotmail.com'),
(13, 'cookmaster_lynn', 36, 'Zamboanga City, Philippines', 'Female', '$argon2id$v=19$m=65536,t=3,p=4$2dtbq/XeO4fwvjcGwHgP4Q$jXziQPF7i1bvaa6h+JA0v48d34xCsrZZ8wTvMv6sQag', 'https://www.pinterest.com/cookmasterlynn', 'lynn.cooks@gmail.com'),
(14, 'edu_mateo', 31, 'Baguio City, Philippines', 'Male', '$argon2id$v=19$m=65536,t=3,p=4$fe/9H6M0xljL2dvb+x9j7A$C6XQXXDsUs+ZDlsnOgxVdhVH6ySi+oM80wWESS8YN0U', 'https://www.linkedin.com/in/edumateo', 'mateo.edu@gmail.com'),
(15, 'wanderlust_nina', 32, 'Palawan, Philippines', 'Female', '$argon2id$v=19$m=65536,t=3,p=4$jjEmRMg5R2gtZYwxhjBGqA$ohiGsaZ255AUO0fh6nibnm9M/iioKm8lH2rNFzSE7E0', 'https://www.instagram.com/wanderlustnina', 'nina.wanderlust@yahoo.com'),
(16, 'sciencegeek_john', 25, 'Legazpi City, Philippines', 'Male', '$argon2id$v=19$m=65536,t=3,p=4$JyQEgPDe25sz5ry3lnIuhQ$AtBOa2kwNokoWiRpSUxH2lNgsOVz8h5EzFYzH0G6Xyo', 'https://twitter.com/sciencegeekjohn', 'john.science@gmail.com'),
(17, 'musiclover_anne', 25, 'General Santos City, Philippines', 'Male', '$argon2id$v=19$m=65536,t=3,p=4$l9J6z/k/Z4xRirH2vhdCKA$xmmaoH8dz348Ndu//tSSLn/oIuMuwSmjU/XHSqHjLt0', 'https://www.spotify.com/musicloveranne', 'anne.music@gmail.com'),
(18, 'photog_mark', 34, 'Dumaguete City, Philippines', 'Male', '$argon2id$v=19$m=65536,t=3,p=4$h5AyplRqbQ3BWMsZQwjhXA$seDivupPM+b4dHDylP+AhbJPvaTmotpbo9iveARXWE8', 'https://www.behance.net/photogmark', 'mark.photo@hotmail.com'),
(19, 'business_mia', 29, 'Cagayan de Oro, Philippines', 'Male', '$argon2id$v=19$m=65536,t=3,p=4$TIlRSknJ2dtbKwWA8D6HsA$480AyFb6ghhdGonDtP+ZEHs1OOz6sivVGg4/V01MWWc', 'https://www.linkedin.com/in/businessmia', 'mia.business@gmail.com'),
(20, 'lifestyle_joey', 21, 'Cavite, Philippines', 'Male', '$argon2id$v=19$m=65536,t=3,p=4$gHCOce69VwphLIXw3ltLaQ$k1Vozssa2RLzUMAUMdGCBp5sCqGP4ypheyS4wOpTogo', 'https://www.facebook.com/lifestylejoey', 'joey.lifestyle@gmail.com'),
(21, 'artsy_sam', 33, 'Taguig, Philippines', 'Female', '$argon2id$v=19$m=65536,t=3,p=4$FiIEYOxda21tDQHAWKu1Vg$MgLroTLjC1knw9mn95FDyDrDIgl9rsPCkVJQSw3zGs8', 'https://www.instagram.com/artsysam', 'sam.artsy@gmail.com'),
(22, 'techwizard_andrei', 27, 'Pampanga, Philippines', 'Male', '$argon2id$v=19$m=65536,t=3,p=4$B2Cs9T5HSKlVCkHIWYuxdg$zfkfk/8CqYuWctocYbaSxOamYPIIAT08YvtYunx5k8k', 'https://github.com/techwizardandrei', 'andrei.tech@gmail.com'),
(23, 'bookworm_claire', 20, 'Batangas, Philippines', 'Female', '$argon2id$v=19$m=65536,t=3,p=4$TUkpZSylVArBGGNs7V1r7Q$IMY1TIYRVCeA6bTBtOV8+m2rUhMp05cvbH9s9RZDpHs', 'https://twitter.com/bookwormclaire', 'claire.books@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `user_interests`
--

CREATE TABLE `user_interests` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `interest` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_interests`
--

INSERT INTO `user_interests` (`id`, `username`, `interest`) VALUES
(1, 'GroupPenpal', 'PHOTOGRAPHY'),
(2, 'GroupPenpal', 'EDUCATION'),
(3, 'GroupPenpal', 'MOVIES'),
(4, 'GroupPenpal', 'BOOKS'),
(5, 'GroupPenpal', 'BUSINESS'),
(6, 'PenpalGroup', 'PHOTOGRAPHY'),
(7, 'PenpalGroup', 'MUSIC'),
(8, 'PenpalGroup', 'EDUCATION'),
(9, 'PenpalGroup', 'MOVIES'),
(10, 'PenpalGroup', 'BUSINESS'),
(11, 'sigmass', 'PHOTOGRAPHY'),
(12, 'sigmass', 'EDUCATION'),
(13, 'sigmass', 'MOVIES'),
(14, 'sigmass', 'BOOKS'),
(15, 'sigmass', 'BUSINESS'),
(16, 'MALLOWS_20', 'PHOTOGRAPHY'),
(17, 'MALLOWS_20', 'EDUCATION'),
(18, 'MALLOWS_20', 'MOVIES'),
(19, 'MALLOWS_20', 'BOOKS'),
(20, 'MALLOWS_20', 'LIFESTYLE'),
(21, 'traveler_jay24', 'TECHNOLOGY'),
(22, 'traveler_jay24', 'PHOTOGRAPHY'),
(23, 'traveler_jay24', 'MUSIC'),
(24, 'traveler_jay24', 'TRAVEL'),
(25, 'traveler_jay24', 'SCIENCE'),
(26, 'foodie_mika89', 'ARTS'),
(27, 'foodie_mika89', 'TRAVEL'),
(28, 'foodie_mika89', 'COOKING'),
(29, 'foodie_mika89', 'LIFESTYLE'),
(30, 'foodie_mika89', 'BUSINESS'),
(31, 'booklover_karen', 'ARTS'),
(32, 'booklover_karen', 'EDUCATION'),
(33, 'booklover_karen', 'MOVIES'),
(34, 'booklover_karen', 'BOOKS'),
(35, 'booklover_karen', 'SCIENCE'),
(36, 'techy_mark22', 'TECHNOLOGY'),
(37, 'techy_mark22', 'GAMING'),
(38, 'techy_mark22', 'PHOTOGRAPHY'),
(39, 'techy_mark22', 'MOVIES'),
(40, 'techy_mark22', 'SCIENCE'),
(41, 'artistica_ella', 'ARTS'),
(42, 'artistica_ella', 'PHOTOGRAPHY'),
(43, 'artistica_ella', 'FASHION'),
(44, 'artistica_ella', 'MOVIES'),
(45, 'artistica_ella', 'LIFESTYLE'),
(46, 'gamer_lance', 'TECHNOLOGY'),
(47, 'gamer_lance', 'GAMING'),
(48, 'gamer_lance', 'MUSIC'),
(49, 'gamer_lance', 'MOVIES'),
(50, 'gamer_lance', 'SCIENCE'),
(51, 'fashionista_bea', 'TECHNOLOGY'),
(52, 'fashionista_bea', 'TRAVEL'),
(53, 'fashionista_bea', 'FASHION'),
(54, 'fashionista_bea', 'LIFESTYLE'),
(55, 'fashionista_bea', 'BUSINESS'),
(56, 'moviebuff_jake', 'TECHNOLOGY'),
(57, 'moviebuff_jake', 'MUSIC'),
(58, 'moviebuff_jake', 'MOVIES'),
(59, 'moviebuff_jake', 'BOOKS'),
(60, 'moviebuff_jake', 'LIFESTYLE'),
(61, 'cookmaster_lynn', 'COOKING'),
(62, 'cookmaster_lynn', 'FASHION'),
(63, 'cookmaster_lynn', 'BOOKS'),
(64, 'cookmaster_lynn', 'LIFESTYLE'),
(65, 'cookmaster_lynn', 'BUSINESS'),
(66, 'edu_mateo', 'TECHNOLOGY'),
(67, 'edu_mateo', 'ARTS'),
(68, 'edu_mateo', 'EDUCATION'),
(69, 'edu_mateo', 'BOOKS'),
(70, 'edu_mateo', 'SCIENCE'),
(71, 'wanderlust_nina', 'PHOTOGRAPHY'),
(72, 'wanderlust_nina', 'TRAVEL'),
(73, 'wanderlust_nina', 'COOKING'),
(74, 'wanderlust_nina', 'FASHION'),
(75, 'wanderlust_nina', 'LIFESTYLE'),
(76, 'sciencegeek_john', 'TECHNOLOGY'),
(77, 'sciencegeek_john', 'GAMING'),
(78, 'sciencegeek_john', 'EDUCATION'),
(79, 'sciencegeek_john', 'BOOKS'),
(80, 'sciencegeek_john', 'SCIENCE'),
(81, 'musiclover_anne', 'ARTS'),
(82, 'musiclover_anne', 'PHOTOGRAPHY'),
(83, 'musiclover_anne', 'MUSIC'),
(84, 'musiclover_anne', 'TRAVEL'),
(85, 'musiclover_anne', 'MOVIES'),
(86, 'photog_mark', 'TECHNOLOGY'),
(87, 'photog_mark', 'ARTS'),
(88, 'photog_mark', 'PHOTOGRAPHY'),
(89, 'photog_mark', 'LIFESTYLE'),
(90, 'photog_mark', 'SCIENCE'),
(91, 'business_mia', 'TECHNOLOGY'),
(92, 'business_mia', 'ARTS'),
(93, 'business_mia', 'FASHION'),
(94, 'business_mia', 'EDUCATION'),
(95, 'business_mia', 'BUSINESS'),
(96, 'lifestyle_joey', 'ARTS'),
(97, 'lifestyle_joey', 'PHOTOGRAPHY'),
(98, 'lifestyle_joey', 'MUSIC'),
(99, 'lifestyle_joey', 'FASHION'),
(100, 'lifestyle_joey', 'LIFESTYLE'),
(101, 'artsy_sam', 'ARTS'),
(102, 'artsy_sam', 'PHOTOGRAPHY'),
(103, 'artsy_sam', 'MUSIC'),
(104, 'artsy_sam', 'TRAVEL'),
(105, 'artsy_sam', 'FASHION'),
(106, 'techwizard_andrei', 'TECHNOLOGY'),
(107, 'techwizard_andrei', 'GAMING'),
(108, 'techwizard_andrei', 'EDUCATION'),
(109, 'techwizard_andrei', 'MOVIES'),
(110, 'techwizard_andrei', 'SCIENCE'),
(111, 'bookworm_claire', 'ARTS'),
(112, 'bookworm_claire', 'EDUCATION'),
(113, 'bookworm_claire', 'BOOKS'),
(114, 'bookworm_claire', 'LIFESTYLE'),
(115, 'bookworm_claire', 'SCIENCE');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `friendships`
--
ALTER TABLE `friendships`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user1` (`user1`,`user2`),
  ADD KEY `user2` (`user2`);

--
-- Indexes for table `friend_requests`
--
ALTER TABLE `friend_requests`
  ADD PRIMARY KEY (`id`),
  ADD KEY `from_user` (`from_user`),
  ADD KEY `to_user` (`to_user`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `user_interests`
--
ALTER TABLE `user_interests`
  ADD PRIMARY KEY (`id`),
  ADD KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `friendships`
--
ALTER TABLE `friendships`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `friend_requests`
--
ALTER TABLE `friend_requests`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `user_interests`
--
ALTER TABLE `user_interests`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=116;

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

--
-- Constraints for table `user_interests`
--
ALTER TABLE `user_interests`
  ADD CONSTRAINT `user_interests_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
