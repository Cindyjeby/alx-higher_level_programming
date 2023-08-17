-- Script that lists all the shows from hbtn_od_tvshows_rate by their rateing

SELECT tv_shows.title, tv_show_genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
