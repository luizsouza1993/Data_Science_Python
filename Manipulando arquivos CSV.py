import csv


with open("C:/Users/Samsung Max/Desktop/Data Science Academy/Python/Arquivos/salarios.csv","w") as Arquivo:
    escrita = csv.writer(Arquivo)
    escrita.writerow(("Primeira","Segunda","Terceira"))
    escrita.writerow((30,40,50))


with open("C:/Users/Samsung Max/Desktop/Data Science Academy/Python/Arquivos/salarios.csv","r") as Arquivo:
    leitura = csv.reader(Arquivo)
    for x in leitura:
        print(f"numero de colunas {len(x)}")
        print(x)

    
