-- This query retrieves all genres from the hbtn_0d_tvshows database
-- and counts the number of shows linked to each genre.
-- It displays the genre and the corresponding number of shows.

SELECT genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id  -- Join genres with tv_show_genres
GROUP BY genres.name  -- Group by genre name to count the shows for each genre
HAVING COUNT(tv_show_genres.show_id) > 0  -- Only include genres with at least one linked show
ORDER BY number_of_shows DESC;  -- Sort the results by the number of shows in descending order
