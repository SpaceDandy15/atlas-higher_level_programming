# SQL Questions for hbtn_0d_tvshows Database

This repository contains SQL scripts designed to query the `hbtn_0d_tvshows` database. Each script addresses specific questions about the data structure and relationships within the database. The database is designed to manage information about TV shows and their genres.

## Table of Contents

1. [Database Structure](#database-structure)
2. [SQL Scripts](#sql-scripts)
3. [Usage](#usage)
4. [License](#license)

## Database Structure

The `hbtn_0d_tvshows` database includes the following tables:

- **tv_shows**: Contains records of TV shows.
- **genres**: Contains records of genres.
- **tv_show_genres**: A junction table linking TV shows to genres.

## SQL Scripts

Below is a list of SQL scripts included in this repository:

0. **0-select_states.sql**: Create the states table in the database and populate it with initial data.
1. **1-list_states.sql**: List all states from the database.
2. **2-filter_states.sql**: List all states that start with the letter 'N'.
3. **3-fetch_states.sql**: Fetch a state by its ID, passed as an argument.
4. **4-insert_states.sql**: Insert a new state into the database.
5. **5-update_states.sql**: Update a state in the database.
6. **6-delete_states.sql**: Delete a state from the database by ID.
7. **7-count_states.sql**: Count the number of states in the database.
8. **8-list_cities.sql**: List all cities from the database.
9. **9-filter_cities.sql**: List cities linked to a specific state.
10. **10-fetch_cities.sql**: Fetch a city by its ID, passed as an argument.
11. **11-insert_cities.sql**: Insert a new city into the database.

12. **12-no_genre.sql**: List all genres from the database and display the number of shows linked to each genre.
13. **13-count_shows_by_genre.sql**: Count the number of shows linked to each genre and display in descending order.
14. **14-my_genres.sql**: List all genres of the show "Dexter".
15. **15-comedy_only.sql**: List all Comedy shows in the database.
16. **16-shows_by_genre.sql**: List all shows and their linked genres, displaying NULL for shows without a genre.

## Usage

To execute the SQL scripts, you can use the following command in your terminal:

```bash
mysql -hlocalhost -uroot -p hbtn_0d_tvshows < <script_name>.sql
