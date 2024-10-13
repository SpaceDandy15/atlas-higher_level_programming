-- This query retrieves all TV shows from the hbtn_0d_tvshows database that do not have any genres linked.
-- Each record displays the show's title and NULL for the genre_id.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id  -- Use LEFT JOIN to include all shows
WHERE tv_show_genres.genre_id IS NULL  -- Filter to only include shows without linked genres

-- The ORDER BY clause sorts the results by tv_shows.title and genre_id in ascending order.
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
