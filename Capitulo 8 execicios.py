# Crie um array NumPy com 1000000 e uma lista com 1000000.
# Multiplique cada elemento do array e da lista por 2 e calcule o tempo de execução com cada um dos objetos (use %time).
# Qual objeto oferece melhor performance, array NumPy ou lista?

import numpy as np
import time
import sqlite3
from numpy.random import f
import pandas as pd

teste = np.arange(1000000)

lista = [x for x in range(1000000+1)]

inicio = time.time()
teste2 = teste *2
fim =time.time()
print(f"{fim-inicio:.3f}")

inicio = time.time()
lista2 = [x*2 for x in lista]
fim =time.time()
print(f"{fim-inicio:.3f}")

# Exercício 2
# Crie um array de 10 elementos
# Altere o valores de todos os elementos dos índices 5 a 8 para 0

teste3 = np.arange(10)

teste3[5:8] = 0

print(teste3)

# Crie um array de 3 dimensões e imprima a dimensão 1 

teste4 = np.array([[[1,1,1],[2,2,2]],[[1,1,1],[2,2,2]]])

print(teste4[0])

# Crie um array de duas dimensões (matriz).
# Imprima os elementos da terceira linha da matriz
# Imprima todos os elementos da primeira e segunda linhas e segunda e terceira colunas

teste5 = np.array([[4,4,4],[2,2,2],[3,3,3]])

print(teste5[2])

# Imprima todos os elementos da primeira e segunda linhas e segunda e terceira colunas

print(teste5[:2,1:])

# Calcule a transposta da matriz abaixo
arr = np.arange(15).reshape((3, 5))
arr

teste7= arr.T

print(arr)
print(teste7)

# Considere os 3 arrays abaixo
# Retorne o valor do array xarr se o valor for True no array cond. Caso contrário, retorne o valor do array yarr.
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

resultado = [(a if c else b) for a,b,c in zip(xarr,yarr,cond)]
print(resultado)

# Crie um array A com 10 elementos e salve o array em disco com a extensão npy
# Depois carregue o array do disco no array B

A = np.arange(10)

np.save("C:/Users/Samsung Max/OneDrive/Área de Trabalho/Data Science Academy/Python/arrayA.npy",A)

B = np.load("C:/Users/Samsung Max/OneDrive/Área de Trabalho/Data Science Academy/Python/arrayA.npy")

print(B)

# Considerando a série abaixo, imprima os valores únicos na série
import pandas as pd
obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c', 'a', 'b'])

print(obj.unique())

# Considerando o trecho de código que conecta em uma url na internet, imprima o dataframe conforme abaixo.
import requests
url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)

data= resp.json()

data[0]['title']

tabela = pd.DataFrame(data, columns= ['number','title','labels','state'])

print(tabela)

import sqlite3

# Crie um banco de dados no SQLite, crie uma tabela, insira registros, 
# consulte a tabela e retorne os dados em dataframe do Pandas

nomes_idade = {'Nome': ['Luiz','Jennifer'],'idade': [28,23]}

tabela = dict(nomes_idade)

con = sqlite3.connect('teste')

query = '''
create table teste 
(id int primary key, nome varchar(30), idade int, sexo char(1))
'''

con.execute(query)
con.commit()

dados = [(1,'luiz',30,'m'),(2,'Romeu',23,'m')]
insert =  'insert into teste values (?,?,?,?)'
con.executemany(insert, dados)
con.commit()

cursor = con.execute('select * from teste')
linhas = cursor.fetchall()

cursor.description
df = pd.DataFrame(linhas, columns=[x[0] for x in cursor.description])

print(df)



