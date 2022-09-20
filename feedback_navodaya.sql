-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 20, 2022 at 10:16 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `feedback navodaya`
--

-- --------------------------------------------------------

--
-- Table structure for table `adminpost`
--

CREATE TABLE `adminpost` (
  `sno` int(70) NOT NULL,
  `Title` text NOT NULL,
  `content` text NOT NULL,
  `slug` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `adminpost`
--

INSERT INTO `adminpost` (`sno`, `Title`, `content`, `slug`) VALUES
(1, 'Captain badges will be distributed to cabinet mambers soon', 'I want to notify you all that the captain badges will be distributed to vidyalaya cabinet members on the occasion of teachers day.', 'Captain-badges-will'),
(2, '\"swachhta pakhwada\"', 'I am going to announce that the \"swachhta pakhwada\" will be organised in our vidyalaya from 1-09-2022\r\nto 15-09-2022. So, all students should participate in all activitied related to \"swachh bharat abhiyaan\"\r\nThank you', '\"swachhta-pakhwada\"-short'),
(3, '\"Sahi Posan Desh Rosan\"', 'Posan maah (september, 2022) is going on. so we all should comfirm our participation in all the activities. And should aware our friends about right nutrition diets. speech compitition and essay writing comptition will be organised in this month.\r\nthank you', '\"Sahi-Posan-Desh'),
(4, 'MP hall in our vidyalaya', 'Our Vidyalaya administration is thinking about the construction of MP hall in our vidyalaya. and we want that you all should share your views and suggestion on this idea.\r\nWe hope the reply from all navodaya family members.\r\nThank you.\r\n', 'MP-hall-in');

-- --------------------------------------------------------

--
-- Table structure for table `comment`
--

CREATE TABLE `comment` (
  `username` text NOT NULL,
  `usercomment` text NOT NULL,
  `type` text NOT NULL,
  `sno` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `comment`
--

INSERT INTO `comment` (`username`, `usercomment`, `type`, `sno`) VALUES
('myteacher', 'I think There is a suitable space for MP hall near the basketball ground', 'teacher', 4),
('myparent', 'Yes this is right step towards the positive growth of the vidyalaya', 'parent', 4);

-- --------------------------------------------------------

--
-- Table structure for table `parentpost`
--

CREATE TABLE `parentpost` (
  `username` text NOT NULL,
  `sno` int(70) NOT NULL,
  `title` text NOT NULL,
  `content` text NOT NULL,
  `slug` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `parentpost`
--

INSERT INTO `parentpost` (`username`, `sno`, `title`, `content`, `slug`) VALUES
('myparent', 1, 'Vidyalaya should provide a better diet for students', 'Dear sir \r\n       as you know students in our vidyalaya play different games and some of them also do serious practice for sports. so the normal diet which is provided to student is insufficient for students. Vidyalaya should provide sprouts and some other protein rich diets. ', 'Vidyalaya-should-provide');

-- --------------------------------------------------------

--
-- Table structure for table `reply`
--

CREATE TABLE `reply` (
  `type` text NOT NULL,
  `adminreply` text NOT NULL,
  `slug` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `reply`
--

INSERT INTO `reply` (`type`, `adminreply`, `slug`) VALUES
('parent', 'We will definitely pay attention to your suggestion.', 'Vidyalaya-should-provide'),
('teacher', 'ok i will think about it', 'xyz-short-short'),
('student', 'thats good', 'Study-Material-In');

-- --------------------------------------------------------

--
-- Table structure for table `studentpost`
--

CREATE TABLE `studentpost` (
  `username` text NOT NULL,
  `sno` int(50) NOT NULL,
  `title` text NOT NULL,
  `content` text NOT NULL,
  `slug` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `studentpost`
--

INSERT INTO `studentpost` (`username`, `sno`, `title`, `content`, `slug`) VALUES
('shivam ', 1, 'Study Material In Our Library', 'Respected Sir\r\n                      Actually we need some  reference / guide Books and some sample papers. so that we can prepare for upcoming exams. Sir please order some study material for board classes in our vidyalaya.\r\nThanks you', 'Study-Material-In');

-- --------------------------------------------------------

--
-- Table structure for table `teacherpost`
--

CREATE TABLE `teacherpost` (
  `username` text NOT NULL,
  `sno` int(70) NOT NULL,
  `title` text NOT NULL,
  `content` text NOT NULL,
  `slug` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `teacherpost`
--

INSERT INTO `teacherpost` (`username`, `sno`, `title`, `content`, `slug`) VALUES
('myteacher', 1, 'xyz', 'abcd', 'xyz-short-short');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `username` text NOT NULL,
  `password` text NOT NULL,
  `type` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`username`, `password`, `type`) VALUES
('shivam', 'password', 'student'),
('myteacher', 'studyonly', 'teacher'),
('myparent', 'childcare', 'parent'),
('admin', 'projectf', 'admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adminpost`
--
ALTER TABLE `adminpost`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `comment`
--
ALTER TABLE `comment`
  ADD UNIQUE KEY `usercomment` (`usercomment`) USING HASH;

--
-- Indexes for table `parentpost`
--
ALTER TABLE `parentpost`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `reply`
--
ALTER TABLE `reply`
  ADD UNIQUE KEY `adminreply` (`adminreply`) USING HASH;

--
-- Indexes for table `studentpost`
--
ALTER TABLE `studentpost`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `teacherpost`
--
ALTER TABLE `teacherpost`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD UNIQUE KEY `username` (`username`) USING HASH,
  ADD UNIQUE KEY `username_2` (`username`) USING HASH;

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `adminpost`
--
ALTER TABLE `adminpost`
  MODIFY `sno` int(70) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `parentpost`
--
ALTER TABLE `parentpost`
  MODIFY `sno` int(70) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `studentpost`
--
ALTER TABLE `studentpost`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `teacherpost`
--
ALTER TABLE `teacherpost`
  MODIFY `sno` int(70) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
