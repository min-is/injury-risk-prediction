-- Create warehouse
CREATE WAREHOUSE IF NOT EXISTS ATHLETE_WH
WITH WAREHOUSE_SIZE = 'XSMALL';

-- Create database/schema
CREATE DATABASE IF NOT EXISTS INJURY_RISK;
CREATE SCHEMA IF NOT EXISTS ATHLETE_DATA;

CREATE TABLE IF NOT EXISTS athlete_bios (
    athlete_id STRING PRIMARY KEY,
    height_cm FLOAT,
    weight_kg FLOAT,
    position STRING,
    team STRING
);

CREATE TABLE IF NOT EXISTS biomechanical_data (
    session_id STRING,
    athlete_id STRING,
    left_force FLOAT,
    right_force FLOAT,
    asymmetry_score FLOAT GENERATED ALWAYS AS (ABS(left_force - right_force)),
    recorded_at TIMESTAMP
);