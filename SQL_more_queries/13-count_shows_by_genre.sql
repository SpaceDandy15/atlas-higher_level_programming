-- This script retrieves all genres from the hbtn_0d_tvshows database
-- and counts the number of shows linked to each genre.
-- Each record displays the genre and the number of shows linked to that genre.

SELECT 
    genres.name AS genre,                -- Select the genre name
    COUNT(tv_show_genres.show_id) AS number_of_shows  -- Count the number of shows linked to the genre
FROM 
    genres                               -- From the genres table
JOIN 
    tv_show_genres                       -- Join with the tv_show_genres table
    ON genres.id = tv_show_genres.genre_id  -- Using genre ID to join both tables
GROUP BY 
    genres.name                          -- Group results by genre name
HAVING 
    COUNT(tv_show_genres.show_id) > 0   -- Only include genres that have at least one show linked
ORDER BY 
    number_of_shows DESC;                -- Sort results in descending order by the number of shows linked
