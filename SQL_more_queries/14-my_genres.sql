-- This script retrieves all genres associated with the TV show 'Dexter'.
-- Each record displays the genre name, sorted in ascending order.

SELECT 
    tv_genres.name                       -- Select the genre name
FROM 
    tv_genres                            -- From the tv_genres table
JOIN 
    tv_show_genres                       -- Join with the tv_show_genres table
    ON tv_genres.id = tv_show_genres.genre_id  -- Using genre ID to join both tables
JOIN 
    tv_shows                              -- Join with the tv_shows table to find the show
    ON tv_show_genres.show_id = tv_shows.id     -- Using show ID to join
WHERE 
    tv_shows.title = 'Dexter'            -- Filter to only include the show 'Dexter'
ORDER BY 
    tv_genres.name ASC;                  -- Sort results in ascending order by genre name
