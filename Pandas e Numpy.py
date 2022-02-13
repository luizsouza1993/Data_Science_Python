from pandas import read_excel, DataFrame
from matplotlib import pyplot as plt
teste = dict()

teste = {'Nome': ['Luiz', 'Jennifer','Roberto','Junior'], 'idade': [28,23,10,15]}

frame = DataFrame(teste)

plt.plot(frame['Nome'],frame['idade'])
plt.xlabel('Nome')
plt.ylabel('Idade')
plt.title('Idade das pessoas')
plt.show()

plt.plot(frame['Nome'],frame['idade'],label='Idade')
plt.legend()
plt.title('Idade das pessoas')
plt.show()

plt.bar(frame['Nome'],frame['idade'],label='Idade',color = 'darkblue')
plt.legend()
plt.title('Idade das pessoas')
plt.show()

teste = []
teste = [x for x in range(1,100,10)]

for i in range(100):
    if i%2==0:
        teste.append(i)
        teste.append(i)
        teste.append(i)
        teste.append(i)
        teste.append(i)
        teste.append(i)
        teste.append(i)
    

range_idade = [x for x in range (100)]

plt.hist(teste, range_idade, histtype='stepfilled', rwidth=2.0)
plt.show()





