import pandas as pd

# webpage url

url = 'https://en.wikipedia.org/wiki/History_of_Python'

# extraer tables 

dfs = pd.read_html(url) ##data frames, mátriz con datos que posee sus propios métodos

# obtener la prima tabla

df = dfs[0]

# obtener las columnas

columns = df['Version']

print(columns)