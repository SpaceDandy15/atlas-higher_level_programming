-- This script retrieves all shows from the hbtn_0d_tvshows database
-- and lists all genres linked to each show. If a show has no genre,
-- NULL will be displayed in the genre column.

SELECT 
    tv_shows.title,                      -- Select the title of the TV shows
    tv_genres.name AS genre              -- Select the genre name (NULL if no genre)
FROM 
    tv_shows                              -- From the tv_shows table
LEFT JOIN 
    tv_show_genres                       -- Left join with tv_show_genres table
    ON tv_shows.id = tv_show_genres.show_id  -- Using show ID to join both tables
LEFT JOIN 
    tv_genres                             -- Left join with the tv_genres table
    ON tv_show_genres.genre_id = tv_genres.id  -- Using genre ID to join
ORDER BY 
    tv_shows.title ASC,                  -- Sort results by show title in ascending order
    genre ASC;                           -- Sort results by genre name in ascending order
