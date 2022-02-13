#Missão: Implemente um algoritmo para determinar se uma string possui todos os caracteres exclusivos.

class caracteres_exclusivos(object):
    
    def caracter_unique(self,string):
        if string == None:
            return False
        letras = set()
        for letra in string:
            if letra.lower() in letras:
                print("Incorreto")
                return False
            else:
                letras.add(letra)
        print("Correto")
        return True
        
teste = caracteres_exclusivos()
palavra = "Luiz"
teste.caracter_unique(palavra)