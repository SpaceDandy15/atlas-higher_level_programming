-- This query retrieves all TV shows along with their associated genre IDs
-- from the hbtn_0d_tvshows database, displaying NULL for shows without genres.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id  -- Using LEFT JOIN to include all shows, even those without genres

-- The ORDER BY clause sorts the results first by the title of the TV shows
-- in ascending order and then by genre_id in ascending order.
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
