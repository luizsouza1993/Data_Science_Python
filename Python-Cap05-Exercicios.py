from platform import python_version

print(python_version())


# Exercício 1 - Crie um objeto a partir da classe abaixo, chamado roc1, passando 2 parâmetros e depois faça uma chamada
# aos atributos e métodos
from math import sqrt

class Rocket():
     
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        
    def print_rocket(self):
        print(self.x, self.y)
        
        
        
roc1 = Rocket(5,4)
roc1.print_rocket()
roc1.move_rocket(10,55)
roc1.print_rocket()


class calculo:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def soma(self):
        self = self.x+ self.y
        print(self)
        
    def potencia(self):
        self = self.x**self.y
        print(self)
        
        
numeros = calculo(2,8)
numeros.soma()
numeros.potencia()

# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.


class Pessoa():
    
    def __init__(self,nome,cidade,telefone,email):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
        
    def __str__(self):
        return "A pessoa se chama " + self.nome + ", mora na cidade " + self.cidade + ", o numero de telefone é " + self.telefone + \
                 " e o email " + self.email
    
    def primeiro(self):
        self= self.nome.split()
        return self[0]
            
usuario = Pessoa("Luiz Claudio de Souza", "Joinville","47999132454","luiz.santosfc10@hotmail.com")

print(str(usuario))
print(usuario.primeiro())

# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os 
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.

class Smartphone(object):
    def __init__(self,tamanho,interface):
        self.tamanho = tamanho
        self.interface = interface
        
class MP3Player(Smartphone):
    def __init__(self, capacidade, interface = "LED",tamanho = "Grande"):
        self.capacidade = capacidade
        Smartphone.__init__(self, tamanho, interface)
        
    def print_MP3Player(self):
        print(f"Valores para o objeto criado: {self.tamanho} ,{self.interface} , {self.capacidade}")

teste = Smartphone("Grande","Led")
device = MP3Player("128gb")
device.print_MP3Player()