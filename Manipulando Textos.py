import os

arquivo = open(os.path.join("C:/Users/Samsung Max/Desktop/Data Science Academy/Python/Arquivos/ManipulandoTexto.txt"),"w")

texto = "Manipulando arquivo de texto no python"


for palavra in texto.split():
    arquivo.write(f"{palavra} ")


arquivo.close()


arquivo = open("C:/Users/Samsung Max/Desktop/Data Science Academy/Python/Arquivos/ManipulandoTexto.txt","r")


print(arquivo.read())

arquivo.close()

with open("C:/Users/Samsung Max/Desktop/Data Science Academy/Python/Arquivos/ManipulandoTexto.txt","r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
    print(len(conteudo))


with open(os.path.join("C:/Users/Samsung Max/Desktop/Data Science Academy/Python/Arquivos/ManipulandoTexto2.txt"),"w") as arquivo:
    arquivo.write(texto[:5])
    arquivo.write("\n")
    arquivo.write(texto[:10])


arquivo = open("C:/Users/Samsung Max/Desktop/Data Science Academy/Python/Arquivos/ManipulandoTexto2.txt","r")
conteudo = arquivo.read()
print(conteudo)


arquivo.close



    


