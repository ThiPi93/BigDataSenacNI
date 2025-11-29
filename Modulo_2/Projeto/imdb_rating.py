import numpy as np
import pandas as pd

lista_numeros = [10, 20, 30, 40, 50]
meu_array = np.array(lista_numeros)

print(meu_array)
# Saída: [10 20 30 40 50]
print(type(meu_array))
# Saída: <class 'numpy.ndarray'>

# Comparando com uma série do Pandas
minha_serie = pd.Series(lista_numeros)
print(minha_serie)
print(type(minha_serie))

####################################################

# Extraindo a coluna 'preco' do arquivo vendas_produtos.csv com Numpy
imdb_rating = np.genfromtxt('C:\Users\felix.thiago\Documents\BigDataSenacNI\Modulo_2\Projeto\oscars_df.csv', delimiter=',', skip_header=1, dtype=None, encoding='utf-8', usecols=8)
print(imdb_rating)
print(type(imdb_rating))

media = np.mean(imdb_rating)
print(f"Média dos preços: R$ {media:.2f}")


# Obtenha a mediana:
mediana = np.median(imdb_rating)
print(f"Mediana dos preços: R$ {mediana:.2f}")


# Calcule a distância entre a média e a mediana:
distancia = (media - mediana) / mediana
print(f"Distância entre a média e a mediana: {distancia * 100:.2f}%")