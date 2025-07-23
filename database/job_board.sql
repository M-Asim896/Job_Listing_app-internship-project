-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 10, 2025 at 04:00 PM
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
-- Database: `job_board`
--

-- --------------------------------------------------------

--
-- Table structure for table `job`
--

CREATE TABLE `job` (
  `id` int(11) NOT NULL,
  `title` varchar(120) NOT NULL,
  `company` varchar(120) NOT NULL,
  `location` varchar(120) NOT NULL,
  `posting_date` varchar(50) NOT NULL,
  `job_type` varchar(50) NOT NULL,
  `tags` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `job`
--

INSERT INTO `job` (`id`, `title`, `company`, `location`, `posting_date`, `job_type`, `tags`) VALUES
(8, 'junior', 'ACOR', 'AMERICA', '9-7-2025', 'Full-time', 'web developer'),
(9, 'Senior TS React Developer', 'Prezly', 'Remote', '2025-07-10', 'Remote', 'Scraped, Python'),
(10, 'Software Engineer', 'Loancrate', 'Remote', '2025-07-10', 'Remote', 'Scraped, Python'),
(11, 'Security Researcher', 'Spearbit', 'Remote', '2025-07-10', 'Remote', 'Scraped, Python'),
(12, 'Senior Flutter Developer', 'ExpertGrain', 'Remote', '2025-07-10', 'Remote', 'Scraped, Python'),
(13, 'Customer Onboarding & Support Specialist', 'Gymflow', 'Remote', '2025-07-10', 'Remote', 'Scraped, Python');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `job`
--
ALTER TABLE `job`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `job`
--
ALTER TABLE `job`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
