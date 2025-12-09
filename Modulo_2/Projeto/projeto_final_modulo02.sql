CREATE DATABASE projeto_final_modulo02;

USE projeto_final_modulo02; 

CREATE TABLE dados_projeto(
indice INT PRIMARY KEY,
film VARCHAR(100),
oscar_year INT, -- Nessa coluna existem oscar em que pussuem dois anos, exemplo: "1927/28" - Devo ajeitar no documento CSV ou posso devo utilizar outro tipo de dado?
film_studio_producer VARCHAR(100),
award VARCHAR(100),
year_of_release INT,
movie_time INT,
movie_genre VARCHAR(100),
imdb_rating DECIMAL(5, 2),
imdb_votes  INT, -- Os dados dos votos utilizam "," exemplo: "12,221" - Devo ajeitar no documento CSV ou posso devo utilizar outro tipo de dado?
genre VARCHAR(100),
content_rating VARCHAR(100),
directors VARCHAR(100),
actors VARCHAR(100),

);

SET GLOBAL local_infile = 1;
LOAD DATA LOCAL INFILE 'C:/Users/felix.thiago/Documents/BigDataSenacNI/Modulo_2/Projeto/imdb_projeto'
INTO TABLE dados_projeto
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS 
SET imdb_votes = REPLACE(@imdb_votes, ',', '');