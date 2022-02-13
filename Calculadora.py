def soma(x,y):
    return x+y

def sub(x,y):
    return x-y

def div(x,y):
    return x/y

def mult(x,y):
    return x*y


print('''Calculadora Python: 
       [1] - SOMA
       [2] - SUBTRAÇÃO
       [3] - DIVISÃO
       [4] - MULTIPLICAÇÃO
      ''')
print("\nDigite uma das opçoes acima:\n")

escolha = int(input())
print(f"\nOpção escolhida: {escolha}")
x = float(input("Numero 1: "))
y = float(input("Numero 2: "))

if escolha == 1:
    print(soma(x,y))
elif escolha ==2:
    print(sub(x,y))
elif escolha ==3:
    print(div(x,y))
elif escolha ==4:
    print(mult(x,y))
else:
    print ("Opção Incorreta")



    


