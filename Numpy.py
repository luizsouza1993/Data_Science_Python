import numpy as np

print(np.__version__)

vetor1 = np.array([1,2,3,4,5,6])

print(vetor1.shape)

vetor2 = np.arange(0,11,1)

print(vetor2)

teste = np.eye(4)

print(teste)


teste2 = np.diag(np.array([10,20,30]))

print(teste2)


vetor1 = np.append(0,5)

print(vetor1)

lista2 = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]

matriz = np.matrix(lista2)

print(matriz)

print(type(matriz))

print(matriz.dtype)

print(matriz.shape)

print(np.shape(matriz))