-- Script that lists all the shows cntained in the hbtn_0d_tvshows that have at least one genre linked
-- Each record should display: tv_show.title - tv_showgenres.genre_id
-- Results must be dorted inascending order by tv_shows.title and tv_show_genre.genre_id
-- Only one SELECT statement should be used

SELECT tv_show.title, tv_show_genres.genre_id
FROM tv_show_genres
INNER JOIN tv_shows ON tv_show.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show-genres.genre_id ASC;
