CREATE DATABASE projeto_final_UC2;

USE projeto_final_UC2; 

CREATE TABLE tomato_projeto(
	indice INT PRIMARY KEY,
    film VARCHAR(30),
	oscar_year VARCHAR(10),  -- Nessa coluna existem oscar em que pussuem dois anos, exemplo: "1927/28" - Devo ajeitar 
    film_studio_producer VARCHAR(100),
	award VARCHAR(10),
	year_of_release INT,
	movie_time INT, -- Unidade em minutos
	movie_genre VARCHAR(20),
    tomatometer_status VARCHAR(30),
	tomatometer_rating DECIMAL(5, 2),
	tomatometer_count DECIMAL(5, 2),
    audience_status VARCHAR(10),
    audience_rating DECIMAL(5, 2),
	audience_count DECIMAL(5, 2)
);


ALTER TABLE imdb_projeto
CHANGE `IMDB Rating` imdb_rating DECIMAL(3,1);

ALTER TABLE imdb_projeto
CHANGE `Movie Time` movie_time INT;

ALTER TABLE imdb_projeto
CHANGE `Oscar Year` oscar_year VARCHAR(10);

ALTER TABLE imdb_projeto
ADD COLUMN id_filme INT AUTO_INCREMENT PRIMARY KEY;

ALTER TABLE tomato_rating_comma
ADD COLUMN id_tomato INT AUTO_INCREMENT PRIMARY KEY;

ALTER TABLE tomato_rating_comma
ADD CONSTRAINT fk_filme
FOREIGN KEY (Film)
REFERENCES imdb_projeto(Film);

ALTER TABLE imdb_projeto
ADD UNIQUE (Film);

-- 5 QUERIES --
-- 1º Querie
SELECT * FROM imdb_projeto;

-- 2º Querie
SELECT Film, imdb_rating
FROM imdb_projeto
WHERE imdb_rating >= 8.0
ORDER BY imdb_rating DESC;


-- 3º Querie 
SELECT ROUND(AVG(movie_time), 2) AS media_duracao
FROM imdb_projeto;


-- 4º Querie
SELECT Film, oscar_year, Award
FROM imdb_projeto
WHERE Award = 'Winner'
ORDER BY oscar_year ASC;


-- 5º Querie
SELECT Film, oscar_year, Award, imdb_rating
FROM imdb_projeto
WHERE Award = 'Winner'
ORDER BY imdb_rating DESC;



