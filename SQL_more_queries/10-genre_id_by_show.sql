-- Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_tvshows;

-- Use the database
USE hbtn_0d_tvshows;

-- Lists all shows contained in the database that have at least one genre linked
SELECT tv_shows.title, tv_shows_genres.genre_id 
FROM tv_shows
JOIN tv_shows_genres ON tv_shows.id = tv_shows_genres.show_id
ORDER BY tv_shows.title ASC, tv_shows_genres.genre_id ASC;