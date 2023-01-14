/*
 Navicat Premium Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 80031
 Source Host           : localhost:3306
 Source Schema         : nokia_take_home_challenge

 Target Server Type    : MySQL
 Target Server Version : 80031
 File Encoding         : 65001

 Date: 14/01/2023 22:57:42
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for data
-- ----------------------------
DROP TABLE IF EXISTS `data`;
CREATE TABLE `data`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `data` json NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of data
-- ----------------------------
INSERT INTO `data` VALUES (1, '{\"data\": \"{\\\"data\\\":[{\\\"row\\\":0,\\\"col\\\":0,\\\"question\\\":\\\"\\\",\\\"answer\\\":\\\"\\\",\\\"editable\\\":true,\\\"children\\\":[]}]}\"}');

SET FOREIGN_KEY_CHECKS = 1;
