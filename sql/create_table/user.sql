/*
 Navicat MySQL Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 80011
 Source Host           : localhost:3306
 Source Schema         : openbrain

 Target Server Type    : MySQL
 Target Server Version : 80011
 File Encoding         : 65001

 Date: 27/07/2018 18:50:06
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `PID` int(11) NOT NULL AUTO_INCREMENT,
  `ID` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '',
  `UserIcon` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '',
  `Energy` int(11) NULL DEFAULT 0,
  `Gems` int(11) NULL DEFAULT 0,
  `Level` int(11) NULL DEFAULT 0,
  `Proficiency` int(11) NULL DEFAULT 0,
  `Speed` float NULL DEFAULT 0,
  `Judgment` float NULL DEFAULT 0,
  `Calculate` float NULL DEFAULT 0,
  `Accuracy` float NULL DEFAULT 0,
  `Observation` float NULL DEFAULT 0,
  `Memory` float NULL DEFAULT 0,
  `Ranking` int(11) NOT NULL,
  `Grade` int(11) NULL DEFAULT 0,
  PRIMARY KEY (`PID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
