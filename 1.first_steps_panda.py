# https://colab.research.google.com/notebooks/mlcc/intro_to_pandas.ipynb?hl=en#scrollTo=T5OlrqtdtCIb

import pandas as pd
import numpy as np


# california_housing_dataframe = pd.read_csv("https://storage.googleapis.com/ml_universities/california_housing_train.csv", sep=",")
# california_housing_dataframe.describe()

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])
cities = pd.DataFrame({ 'City name': city_names, 'Population': population })
cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / cities['Area square miles']

# Exercise 1
cities['Boolean'] = cities['Area square miles'].apply(lambda val: val > 50) & city_names.apply(lambda val: "San" in str(val))

print(cities)

print(cities.index)
print(cities.reindex(np.random.permutation(cities.index)))

#Exercise #2
print(cities.reindex([5,5,5 ]))




