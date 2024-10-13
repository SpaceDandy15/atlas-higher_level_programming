-- This script retrieves all Comedy shows from the hbtn_0d_tvshows database.
-- Each record displays the show title, sorted in ascending order.

SELECT 
    tv_shows.title                         -- Select the title of the TV shows
FROM 
    tv_shows                               -- From the tv_shows table
JOIN 
    tv_show_genres                        -- Join with the tv_show_genres table
    ON tv_shows.id = tv_show_genres.show_id  -- Using show ID to join both tables
JOIN 
    tv_genres                              -- Join with the tv_genres table to filter by genre
    ON tv_show_genres.genre_id = tv_genres.id  -- Using genre ID to join
WHERE 
    tv_genres.name = 'Comedy'             -- Filter to only include shows in the Comedy genre
ORDER BY 
    tv_shows.title ASC;                   -- Sort results in ascending order by show title
