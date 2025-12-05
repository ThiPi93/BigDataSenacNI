import numpy as np
import pandas as pd

imdb_rating = np.genfromtxt('/content/oscars_df.csv', delimiter=',', skip_header=1, dtype=None, encoding='utf-8', usecols=10)
print(imdb_rating)
print(type(imdb_rating))
