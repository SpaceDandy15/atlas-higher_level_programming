# SQL Tasks for Higher Level Programming

This repository contains a series of SQL scripts designed for database management and manipulation tasks using MySQL. Each task is aimed at building foundational SQL skills, including table creation, data insertion, data retrieval, and data aggregation.

## Table of Contents

1. [Introduction](#introduction)
2. [Tasks Overview](#tasks-overview)
3. [Database Setup](#database-setup)
4. [How to Run the Scripts](#how-to-run-the-scripts)
5. [License](#license)

## Introduction

The tasks in this repository focus on various SQL operations within the `hbtn_0c_0` database. The main objectives include creating tables, inserting data, querying data, and performing calculations to better understand SQL syntax and operations.

## Tasks Overview

Below is a list of tasks included in this repository:

1. **List Tables**: Script to list all tables in a specified database.
   - **File**: `3-list_tables.sql`
   
2. **Create First Table**: Script to create a table called `first_table` with `id` and `name` columns.
   - **File**: `4-first_table.sql`
   
3. **Describe First Table**: Script to display the description of `first_table` without using `DESCRIBE`.
   - **File**: `5-full_table.sql`
   
4. **List Values**: Script to list all rows from the `first_table`.
   - **File**: `6-list_values.sql`
   
5. **Insert Value**: Script to insert a new row in `first_table` with specified values.
   - **File**: `7-insert_value.sql`
   
6. **Count Records**: Script to count the number of records with `id = 89` in `first_table`.
   - **File**: `8-count_89.sql`
   
7. **Create Second Table**: Script to create `second_table` with columns `id`, `name`, and `score`, and insert multiple rows.
   - **File**: `9-full_creation.sql`
   
8. **List Top Scores**: Script to list all records from `second_table`, displaying `score` and `name` ordered by score.
   - **File**: `10-top_score.sql`
   
9. **List Best Scores**: Script to list records with `score >= 10`.
   - **File**: `11-best_score.sql`
   
10. **Update Score**: Script to update Bob's score to 10 without using his ID.
    - **File**: `12-no_cheating.sql`
    
11. **Remove Low Scores**: Script to remove records with `score <= 5`.
    - **File**: `13-change_class.sql`
    
12. **Compute Average**: Script to compute the average score of all records in `second_table`.
    - **File**: `14-average.sql`
    
13. **Count Grouped Scores**: Script to count records with the same score and display the results sorted by count.
    - **File**: `15-groups.sql`
    
14. **List Non-Empty Records**: Script to list records from `second_table` where `name` is not null, ordered by descending score.
    - **File**: `16-no_link.sql`

## Database Setup

To use these scripts, you need to have MySQL installed and a database named `hbtn_0c_0`. Ensure that you have the necessary privileges to create tables and insert data.

## How to Run the Scripts

To execute any script, use the following command in your terminal:

```bash
cat <script_name.sql> | mysql -hlocalhost -uroot -p hbtn_0c_0
