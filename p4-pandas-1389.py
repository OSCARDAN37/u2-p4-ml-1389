import pandas as pd
import numpy as np
# Oscar Flores NC = 1389
n_filas = 5
n_columnas = 5
tag_columna = tuple('ABCDE')#etiquetas para las columnas de una tupla
print(tag_columna)
matriz = np.random.randint(1, 6, size=(n_filas, n_columnas))
print("Genera matriz de 5 filas por 5 columnas")
print("Con numeros aleatorios comprendidos entre 1 y 10")
print(matriz)
# la variable df es DataFrame
df=pd.DataFrame(matriz, columns= tag_columna)
print("---La tabla o DataFrame---NC 1389")
print(df)
print("--- Oscar Flores ---NC 1389")