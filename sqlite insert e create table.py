import sqlite3
import os
import random
import datetime
import time
import matplotlib.pyplot as plt

#abrindo conexão com o banco de dados
conn = sqlite3.connect('dsa.db')

#criando cursor
c= conn.cursor()

#função para criar tabela
def create_table():
    c.execute('create table if not exists produtos(id integer primary key autoincrement not null, date text, '\
              'prod_name text, valor real)')
    
#função para inserir linha
def data_insert():
    c.execute("insert into produtos values(10,'2020-01-01 14:32:00','teclado', 90)")
    conn.commit()
    c.close()
    conn.close()
    
    
#função para inserir valores
def data_insert_var():
    produtos = ['monitor','carro''ferro de passar','cama','TV','livro','moto','bike','patinete','patins']
    for i in range(0,9):
        time.sleep(2.0)
        new_data = datetime.datetime.now()
        new_prod_name = produtos[i]
        new_valor = random.randrange(50,150)
        c.execute('insert into produtos (date,prod_name,valor) values (?,?,?)',(new_data,new_prod_name,new_valor))
        conn.commit()
    


#função para select geral
def select_geral():
    c.execute('select * from produtos')
    for linha in c.fetchall():
        print(linha)
        
def select_filtro(x):
    c.execute(f'select * from produtos where valor > {x}')
    for linha in c.fetchall():
        print(linha)

def select_coluna(x):
    c.execute(f'select * from produtos where valor')
    for linha in c.fetchall():
        print(linha[x])

def delete_valor_abaixo(valor):
    c.execute(f'delete from produtos where valor <{valor}')
    conn.commit()
    
def update_valor(valor):
    c.execute(f'update produtos set valor = 100 where valor <{valor}')
    conn.commit()
    
def dados_grafico():
    c.execute(f'select prod_name, valor from produtos')
    dados = c.fetchall()
    produto = [produto[0] for produto in dados]
    valores = [valor[1] for valor in dados]
    plt.bar(produto,valores)
    plt.show()
        

dados_grafico()

c.close()
conn.close()


