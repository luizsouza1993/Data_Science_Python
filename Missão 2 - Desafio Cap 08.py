#Missão: Gerar uma lista de números primos.

import math

class numerosPrimos(object):
    
    def gerandoPrimos(self, max_num):
        if max_num is None:
            raise TypeError('max_num não pode ser None')
        array = [True] * max_num
        array[0] = False
        array[1] = False
        prime = 2
        while prime <= math.sqrt(max_num):
            self.verificar_primos(array, prime)
            prime = self.proximoPrimo(array, prime)
        return array

    def verificar_primos(self, array,primo):
        for i in range(primo*primo, len(array), primo):
            array[i] = False
            
    def proximoPrimo(self, array, prime):
        proximo = prime + 1
        while proximo < len(array) and not array[proximo]:
            proximo += 1
        return proximo


    
teste = numerosPrimos()
