#removendo banco de dados se existir

import os

os.remove(r'escola.db') if os.path.exists(r'escola.db') else None

import sqlite3

con = sqlite3.connect(r'escola.db')

cur = con.cursor()

query = '''
create table cursos (
    id int primary key,
    titulo varchar(100),
    categoria varchar (100)
)
'''
cur.execute(query)

insert_sql = 'insert into cursos values (?,?,?)'

dados = [(1000, 'ciencia de dados','data science'),
(1001, 'big data fundamentos','big data'),
(1002,'python fundamentos','analise de dados')
]

for dado in dados:
    cur.execute(insert_sql,dado)
    
con.commit()

select = 'select * from cursos'

cur.execute(select)


dados = cur.fetchall()

print(type(dados))

for linha in dados:
    print(linha[2])
    
con.close()

