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

 Date: 14/07/2018 23:52:05
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
  `Energy` int(11) NULL DEFAULT NULL,
  `Gems` int(11) NULL DEFAULT NULL,
  `Level` int(11) NULL DEFAULT NULL,
  `Proficiency` int(11) NULL DEFAULT NULL,
  `Speed` float NULL DEFAULT NULL,
  `Judgment` float NULL DEFAULT NULL,
  `Calculate` float NULL DEFAULT NULL,
  `Accuracy` float NULL DEFAULT NULL,
  `Observation` float NULL DEFAULT NULL,
  `Memory` float NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
