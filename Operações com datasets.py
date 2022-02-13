#Operações com datasets


nomeArquivo= str(input("Digite o nome do arquivo:\n"))

arquivoNome = nomeArquivo + "txt"

arquivo= open(arquivoNome,"w")

arquivo.write("Operações com data set: Testando")

arquivo.close()

arquivo = open(arquivoNome,"r")

print(arquivo.read())

arquivo.close()


f = open("C:/Users/Samsung Max/Desktop/Data Science Academy/Python/Arquivos/salarios.csv","r")

dados= f.read()

linhas = dados.split("\n")

print(linhas)

dadosCompletos=[]

for row in linhas:
    dado = row.split(",")
    dadosCompletos.append(dado)

contador = 0

for row in linhas:
    contador+=1
    

print(dadosCompletos)
print(f"linhas {contador}")


colunas = dadosCompletos[0]

contador = 0

for column in colunas:
    contador+=1


print(f"colunas {contador}")
    
    


