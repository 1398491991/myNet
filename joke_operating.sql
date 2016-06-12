/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50710
Source Host           : localhost:3306
Source Database       : games_pool

Target Server Type    : MYSQL
Target Server Version : 50710
File Encoding         : 65001

Date: 2016-06-12 16:41:47
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for joke_operating
-- ----------------------------
DROP TABLE IF EXISTS `joke_operating`;
CREATE TABLE `joke_operating` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `state` int(11) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `operating_type` smallint(6) NOT NULL,
  `operating_type_china` varchar(10) NOT NULL,
  `operating_text` varchar(250) NOT NULL,
  `joke_id_id` int(11) NOT NULL,
  `operating_joke_user_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `joke_operating_joke_id_id_252b716b_fk_joke_id` (`joke_id_id`),
  KEY `joke_operatin_operating_joke_user_id_id_5ce62dac_fk_user_info_id` (`operating_joke_user_id_id`),
  CONSTRAINT `joke_operatin_operating_joke_user_id_id_5ce62dac_fk_user_info_id` FOREIGN KEY (`operating_joke_user_id_id`) REFERENCES `user_info` (`id`),
  CONSTRAINT `joke_operating_joke_id_id_252b716b_fk_joke_id` FOREIGN KEY (`joke_id_id`) REFERENCES `joke` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of joke_operating
-- ----------------------------
INSERT INTO `joke_operating` VALUES ('2', '0', '2016-06-12 14:28:08.279000', '2016-06-12 14:28:08.279000', '2', '赞', '', '1291', '2');
INSERT INTO `joke_operating` VALUES ('3', '0', '2016-06-12 14:29:40.558000', '2016-06-12 14:29:40.558000', '3', '踩', '', '1297', '2');
INSERT INTO `joke_operating` VALUES ('4', '0', '2016-06-12 14:34:05.057000', '2016-06-12 14:34:05.058000', '3', '踩', '', '1296', '2');
INSERT INTO `joke_operating` VALUES ('5', '0', '2016-06-12 14:36:13.924000', '2016-06-12 14:36:13.924000', '3', '踩', '', '1297', '2');
INSERT INTO `joke_operating` VALUES ('6', '0', '2016-06-12 14:40:37.073000', '2016-06-12 14:40:37.073000', '3', '踩', '', '1281', '2');
INSERT INTO `joke_operating` VALUES ('7', '0', '2016-06-12 14:48:35.032000', '2016-06-12 14:48:35.032000', '1', '评论', '真好啊真好啊！！！', '1282', '2');
INSERT INTO `joke_operating` VALUES ('8', '0', '2016-06-12 15:05:20.636000', '2016-06-12 15:05:20.636000', '3', '踩', '', '2', '2');
