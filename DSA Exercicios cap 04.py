# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.
'''Primeira solução usando Map'''
lista = list()

for i in range(1,4):
    lista.append(i)

def potencia(x):
    return x**3


listaPotencia = list()

print(list((map(potencia,lista))))

'''segundo opção utiliziando direto no for'''
lista = [2,4,6]
potencia = [num**3 for num in lista]
print(potencia)

# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
palavras = 'A Data Science Academy oferece os melhores cursos de análise de dados do Brasil'.split()
resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
for i in resultado:
    print (i)
    

def Palavras(x):
        return x.upper(),x.lower(),len(x)
  
for i in palavras:
    print(Palavras(i))

resultado = map(lambda x: [x.upper(),x.lower(),len(x)], palavras)
    
for i in resultado:
    print(i)


# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Caso não saiba o que é matriz transposta, visite este link: https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.
matrix = [[1, 2,3],[3,4,5],[5,6,6],[7,8,0]]

transposta = [[linha[i] for linha in matrix] for i in range(len(matrix[1]))]

for i in matrix:
    print(i)

for i in transposta:
    print(i)
    
# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo. 
# Aplique as duas funções aos elementos da lista abaixo. 
# Obs: as duas funções devem ser aplicadas simultaneamente.
lista = [0, 1, 2, 3, 4]

potencia = map(lambda x: [x**2,x**3],lista)

for i in potencia:
    print(i)
    
def potencia(x):
    return x**2,x**3

for i in lista:
    print(potencia(i))
    

# Exercício 5 - Abaixo você encontra duas listas. Faça com que cada elemento da listaA seja elevado 
# ao elemento correspondente na listaB.
listaA = [2, 3, 4]
listaB = [10, 11, 12]

def potencia(x,y):
    return x**y,y**x

resultado = list(map(potencia,listaA,listaB))
                
print(resultado)

resultado = map(lambda x,y: [x**y, y**x],listaA,listaB)

for i in resultado:
    print(i)
    
# Exercício 6 - Considerando o range de valores abaixo, use a função filter() para retornar apenas os valores negativos.
range(-5, 5)

condicao = range(-5, 5)
resultado = list(filter((lambda x: x> 0),condicao))
        
print(resultado)

# Exercício 7 - Usando a função filter(), encontre os valores que são comuns às duas listas abaixo.
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]

resultado = list(filter(lambda x: x in a,b))

print(resultado)

# Exercício 8 - Considere o código abaixo. Obtenha o mesmo resultado usando o pacote time. 
# Não conhece o pacote time? Pesquise!
import datetime
print (datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))

import time
print("Horas: "+ time.strftime("%d/%m/%Y %H:%M:%S"))

# Exercício 9 - Considere os dois dicionários abaixo. 
# Crie um terceiro dicionário com as chaves do dicionário 1 e os valores do dicionário 2.
dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}

def trocaValores(d1, d2):
    dicTemp = dict()
    for d1key, d2val in zip(d1,d2.values()):
        dicTemp[d1key] = d2val
    return dicTemp

dict3 = trocaValores(dict1, dict2)
print(dict3)
dict3 = trocaValores(dict2, dict1)
print(dict3)

# Exercício 10 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5.
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
lista2= list()

def resultado(x=list()):
    for indice,valor in enumerate(x):
        if indice > 5:
            print(valor)
    

resultado(lista)

    




