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

 Date: 22/07/2018 01:55:25
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
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
  `Rank` int(11) NOT NULL,
  `Grade` int(11) NULL DEFAULT 0,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
