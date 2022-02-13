import re


genero = 'acao,drama,comedia'

generoCorreto = re.findall(r'[a-z]+',genero)

print(generoCorreto)
