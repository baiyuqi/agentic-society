/*
 Navicat Premium Dump SQL

 Source Server         : agentic_society
 Source Server Type    : SQLite
 Source Server Version : 3045000 (3.45.0)
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3045000 (3.45.0)
 File Encoding         : 65001

 Date: 07/12/2024 07:32:58
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for _quiz_answer_old_20240723
-- ----------------------------
DROP TABLE IF EXISTS "_quiz_answer_old_20240723";
CREATE TABLE "_quiz_answer_old_20240723" (
  "id" INTEGER NOT NULL,
  "index" INTEGER,
  "experiment_name" VARCHAR(30),
  "persona_id" VARCHAR(30),
  "question_group_id" VARCHAR(30),
  "agent_answer" VARCHAR,
  "response" VARCHAR,
  "quiz_sheet" TEXT,
  PRIMARY KEY ("id")
);

-- ----------------------------
-- Table structure for chat
-- ----------------------------
DROP TABLE IF EXISTS "chat";
CREATE TABLE "chat" (
  "id" INTEGER NOT NULL,
  "chatters" VARCHAR NOT NULL,
  "state" VARCHAR NOT NULL,
  "summary" VARCHAR NOT NULL,
  PRIMARY KEY ("id")
);

-- ----------------------------
-- Table structure for experiment
-- ----------------------------
DROP TABLE IF EXISTS "experiment";
CREATE TABLE "experiment" (
  "id" INTEGER NOT NULL,
  "name" VARCHAR(30),
  "type" VARCHAR(30),
  "description" VARCHAR(30),
  "persona_group" VARCHAR,
  "question_group" VARCHAR,
  PRIMARY KEY ("id")
);

-- ----------------------------
-- Table structure for friend_relationship
-- ----------------------------
DROP TABLE IF EXISTS "friend_relationship";
CREATE TABLE "friend_relationship" (
  "from_id" INTEGER NOT NULL,
  "to_id" INTEGER NOT NULL,
  PRIMARY KEY ("from_id", "to_id")
);

-- ----------------------------
-- Table structure for persona
-- ----------------------------
DROP TABLE IF EXISTS "persona";
CREATE TABLE "persona" (
  "id" INTEGER NOT NULL,
  "age" INTEGER NOT NULL,
  "workclass" VARCHAR(30) NOT NULL,
  "education" VARCHAR(30) NOT NULL,
  "education_num" VARCHAR(30) NOT NULL,
  "marital_status" VARCHAR(30) NOT NULL,
  "occupation" VARCHAR(30) NOT NULL,
  "relationship" VARCHAR(30) NOT NULL,
  "race" VARCHAR(30) NOT NULL,
  "sex" VARCHAR(30) NOT NULL,
  "capital_gain" VARCHAR(30) NOT NULL,
  "capital_loss" VARCHAR(30) NOT NULL,
  "hours_per_week" VARCHAR(30) NOT NULL,
  "native_country" VARCHAR(30) NOT NULL,
  "income" VARCHAR(30) NOT NULL,
  "persona_desc" text,
  "elicited" text,
  PRIMARY KEY ("id")
);

-- ----------------------------
-- Table structure for persona_group
-- ----------------------------
DROP TABLE IF EXISTS "persona_group";
CREATE TABLE "persona_group" (
  "id" INTEGER NOT NULL,
  "name" VARCHAR(30),
  "description" VARCHAR(30),
  "personas" VARCHAR,
  "question_set" VARCHAR(30),
  PRIMARY KEY ("id")
);

-- ----------------------------
-- Table structure for personality
-- ----------------------------
DROP TABLE IF EXISTS "personality";
CREATE TABLE "personality" (
  "persona_id" INTEGER NOT NULL,
  "model" VARCHAR(30),
  "theory" VARCHAR(30),
  "question" INTEGER,
  "personality_json" VARCHAR,
  "extraversion" FLOAT,
  "friendliness" FLOAT,
  "gregariousness" FLOAT,
  "assertiveness" FLOAT,
  "activity_level" FLOAT,
  "excitement_seeking" FLOAT,
  "cheerfulness" FLOAT,
  "agreeableness" FLOAT,
  "trust" FLOAT,
  "morality" FLOAT,
  "altruism" FLOAT,
  "cooperation" FLOAT,
  "modesty" FLOAT,
  "sympathy" FLOAT,
  "conscientiousness" FLOAT,
  "self_efficacy" FLOAT,
  "orderliness" FLOAT,
  "dutifulness" FLOAT,
  "achievement_striving" FLOAT,
  "self_discipline" FLOAT,
  "cautiousness" FLOAT,
  "neuroticism" FLOAT,
  "anxiety" FLOAT,
  "anger" FLOAT,
  "depression" FLOAT,
  "self_consciousness" FLOAT,
  "immoderation" FLOAT,
  "vulnerability" FLOAT,
  "openness" FLOAT,
  "imagination" FLOAT,
  "artistic_interests" FLOAT,
  "emotionality" FLOAT,
  "adventurousness" FLOAT,
  "intellect" FLOAT,
  "liberalism" FLOAT,
  "extraversion_score" VARCHAR(30),
  "friendliness_score" VARCHAR(30),
  "gregariousness_score" VARCHAR(30),
  "assertiveness_score" VARCHAR(30),
  "activity_level_score" VARCHAR(30),
  "excitement_seeking_score" VARCHAR(30),
  "cheerfulness_score" VARCHAR(30),
  "agreeableness_score" VARCHAR(30),
  "trust_score" VARCHAR(30),
  "morality_score" VARCHAR(30),
  "altruism_score" VARCHAR(30),
  "cooperation_score" VARCHAR(30),
  "modesty_score" VARCHAR(30),
  "sympathy_score" VARCHAR(30),
  "conscientiousness_score" VARCHAR(30),
  "self_efficacy_score" VARCHAR(30),
  "orderliness_score" VARCHAR(30),
  "dutifulness_score" VARCHAR(30),
  "achievement_striving_score" VARCHAR(30),
  "self_discipline_score" VARCHAR(30),
  "cautiousness_score" VARCHAR(30),
  "neuroticism_score" VARCHAR(30),
  "anxiety_score" VARCHAR(30),
  "anger_score" VARCHAR(30),
  "depression_score" VARCHAR(30),
  "self_consciousness_score" VARCHAR(30),
  "immoderation_score" VARCHAR(30),
  "vulnerability_score" VARCHAR(30),
  "openness_score" VARCHAR(30),
  "imagination_score" VARCHAR(30),
  "artistic_interests_score" VARCHAR(30),
  "emotionality_score" VARCHAR(30),
  "adventurousness_score" VARCHAR(30),
  "intellect_score" VARCHAR(30),
  "liberalism_score" VARCHAR(30),
  PRIMARY KEY ("persona_id")
);

-- ----------------------------
-- Table structure for question
-- ----------------------------
DROP TABLE IF EXISTS "question";
CREATE TABLE "question" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "question_set" TEXT NOT NULL,
  "index" BIGINT,
  "passage" TEXT,
  "question" TEXT,
  "options" TEXT,
  "label" TEXT,
  "answer" TEXT,
  "other.solution" TEXT,
  "other.level" BIGINT,
  "other.type" TEXT,
  "standard_id" INTEGER
);

-- ----------------------------
-- Table structure for question_answer
-- ----------------------------
DROP TABLE IF EXISTS "question_answer";
CREATE TABLE "question_answer" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "experiment_name" TEXT,
  "index" BIGINT,
  "persona_id" BIGINT,
  "question_id" BIGINT,
  "agent_answer" TEXT,
  "agent_solution" TEXT,
  "response" TEXT
);

-- ----------------------------
-- Table structure for question_answer_summary
-- ----------------------------
DROP TABLE IF EXISTS "question_answer_summary";
CREATE TABLE "question_answer_summary" (
  "id" INTEGER NOT NULL,
  "experiment_name" VARCHAR(30),
  "persona_id" VARCHAR(30),
  "score" FLOAT,
  PRIMARY KEY ("id")
);

-- ----------------------------
-- Table structure for question_group
-- ----------------------------
DROP TABLE IF EXISTS "question_group";
CREATE TABLE "question_group" (
  "id" INTEGER NOT NULL,
  "name" VARCHAR(30) NOT NULL,
  "description" VARCHAR(30),
  "questions" text,
  "type" VARCHAR(30),
  "table" VARCHAR(30),
  "quiz_sheet" TEXT,
  "question_set" VARCHAR(30),
  PRIMARY KEY ("id")
);

-- ----------------------------
-- Table structure for question_set
-- ----------------------------
DROP TABLE IF EXISTS "question_set";
CREATE TABLE "question_set" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "name" TEXT,
  "description" TEXT
);

-- ----------------------------
-- Table structure for quiz_answer
-- ----------------------------
DROP TABLE IF EXISTS "quiz_answer";
CREATE TABLE "quiz_answer" (
  "id" INTEGER NOT NULL,
  "index" INTEGER,
  "experiment_name" VARCHAR(30),
  "persona_id" VARCHAR(30),
  "question_group_id" VARCHAR(30),
  "agent_answer" VARCHAR,
  "response" VARCHAR,
  "quiz_sheet" TEXT,
  "sheet_ind" integer,
  PRIMARY KEY ("id")
);

-- ----------------------------
-- Table structure for sqlite_sequence
-- ----------------------------
DROP TABLE IF EXISTS "sqlite_sequence";
CREATE TABLE "sqlite_sequence" (
  "name",
  "seq"
);

-- ----------------------------
-- View structure for persona_personality
-- ----------------------------
DROP VIEW IF EXISTS "persona_personality";
CREATE VIEW "persona_personality" AS select 
 CASE
   WHEN persona.age BETWEEN 16 AND 20 THEN '16_19'
  WHEN persona.age BETWEEN 20 AND 30 THEN '20_29'
  WHEN persona.age BETWEEN 30 AND 40 THEN '30_39'
  WHEN persona.age BETWEEN 40 AND 50 THEN '40_49'
  WHEN persona.age BETWEEN 50 AND 60 THEN '50_59'
  WHEN persona.age BETWEEN 60 AND 70 THEN '60_69'
  WHEN persona.age BETWEEN 70 AND 80 THEN '70_79'
  WHEN persona.age BETWEEN 80 AND 90 THEN '80_89'
  WHEN persona.age BETWEEN 90 AND 100 THEN '90_99'
  WHEN persona.age BETWEEN 100 AND 110 THEN '100_109'
END AS age_range, 
persona.*, personality.* from persona, personality where persona.id = personality.persona_id;

-- ----------------------------
-- View structure for qa_view
-- ----------------------------
DROP VIEW IF EXISTS "qa_view";
CREATE VIEW "qa_view" AS select  question_answer.*,  persona.*,  question.* from  question_answer 
	LEFT JOIN persona ON  question_answer.persona_id = persona.id
	LEFT JOIN question ON  question_answer.question_id = question.id;

-- ----------------------------
-- Auto increment value for question
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 5758 WHERE name = 'question';

-- ----------------------------
-- Indexes structure for table question
-- ----------------------------
CREATE INDEX "ix_questions_index"
ON "question" (
  "index" ASC
);

-- ----------------------------
-- Auto increment value for question_answer
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 945 WHERE name = 'question_answer';

-- ----------------------------
-- Indexes structure for table question_answer
-- ----------------------------
CREATE INDEX "ix_question_answer_index"
ON "question_answer" (
  "index" ASC
);

-- ----------------------------
-- Auto increment value for question_set
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 1 WHERE name = 'question_set';

PRAGMA foreign_keys = true;
