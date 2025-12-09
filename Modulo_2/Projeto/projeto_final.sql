CREATE DATABASE projeto_final_UC2;

USE projeto_final_UC2; 

CREATE TABLE dados_projeto(
	indice INT PRIMARY KEY,
    film VARCHAR(100),
	oscar_year VARCHAR(10),  -- Nessa coluna existem oscar em que pussuem dois anos, exemplo: "1927/28" - Devo ajeitar 
    film_studio_producer VARCHAR(100),
	award VARCHAR(100),
	year_of_release INT,
	movie_time INT, -- Unidade em minutos
	movie_genre VARCHAR(100),
	imdb_rating DECIMAL(5, 2),
	imdb_votes  VARCHAR(10) -- Os dados dos votos utilizam "," exemplo: "12,221" - Devo ajeitar no documento CSV ou posso devo utilizar outro tipo de dado?
);

-- 5 Queries --
SELECT * FROM dados_projetos;