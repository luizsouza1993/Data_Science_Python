#Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista
#para armazenar os números.

numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela

objetos = ["faca","bola","dado","colher","computador"]
print(objetos)

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string

string1 = "Meu pau é "
string2 = "grande"
string3 = string1 + string2

print(string3)

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3,
#4, 4, 4, 5 e depois utilize a função count do # objeto tupla para
#verificar quantas vezes o número 4 aparece na tupla

tupla = (1,2,2,3,4,4,4,5)
print(tupla.count(4))

# Exercício 5 - Crie um dicionário vazio e imprima na tela

dicionario = {}

print(dicionario)

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela

dicionario2 = {"Carro 1": "Fusca","Carro 2": "Gol","Carro 3": "Camaro"}

for k,v in dicionario2.items():
    print(f"{k}: {v}")

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela


dicionario2["Carro 4"]= ("Formula 1")

print(dicionario2)


# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.

dicionario3 = {"Carros ":["Fusca","Chevete"],"Carro 2": "Gol","Carro 3": "Camaro"}

for k,v in dicionario3.items():
    print(f"{k}: {v}")


# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.

lista_elementos = ["Carro", ("coco","vaca"), {"Carro 1": "Fusca","Carro 2": "Gol"},5.0]

print(lista_elementos)

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'

print(frase[0:18])


















                










               
