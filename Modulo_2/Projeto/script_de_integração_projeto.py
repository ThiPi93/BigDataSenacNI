import pandas as pd
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="projeto_final_UC2"
)

query_1 = "SELECT * FROM imdb_projeto"

df_1 = pd.read_sql(query_1, conexao)

df_1.head(11)

query_2 = """
SELECT Film, imdb_rating
FROM imdb_projeto
WHERE imdb_rating >= 8.0
ORDER BY imdb_rating DESC
"""

df_2 = pd.read_sql(query_2, conexao)

df_2

query_3 = """
SELECT ROUND(AVG(movie_time), 2) AS media_duracao
FROM imdb_projeto
"""

df_3 = pd.read_sql(query_3, conexao)

df_3

query_4 = """
SELECT Film, oscar_year, Award
FROM imdb_projeto
WHERE Award = 'Winner'
ORDER BY oscar_year ASC
"""

df_4 = pd.read_sql(query_4, conexao)

df_4

query_5 = """
SELECT Film, oscar_year, Award, imdb_rating
FROM imdb_projeto
WHERE Award = 'Winner'
ORDER BY imdb_rating DESC
"""

df_5 = pd.read_sql(query_5, conexao)

df_5

############################

import pandas as pd
import mysql.connector

# -----------------------------
# CONEXÃO
# -----------------------------
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="projeto_final_UC2"
)

print("Conexão estabelecida!")

# -----------------------------
# QUERY JOIN ENTRE AS TABELAS
# -----------------------------
query_join = """
SELECT 
    i.id_filme,
    i.Film,
    i.imdb_rating,
    i.movie_time,
    t.tomatometer_rating,
    t.audience_rating
FROM imdb_projeto AS i
JOIN tomato_rating_comma AS t
    ON i.Film = t.Film
ORDER BY i.imdb_rating DESC;
"""

pd.read_sql("SHOW COLUMNS FROM tomato_rating_comma", conexao)

df_join = pd.read_sql(query_join, conexao)
# -----------------------------
# CARREGAR RESULTADO NO PANDAS
# -----------------------------


# Mostrar resultado completo
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

df_join



