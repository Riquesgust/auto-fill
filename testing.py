import random
from random import randrange
import decimal
itens = input()
itens = itens.split('/')
for i in range(1, len(itens)):
    itens[i] = itens[i].replace(",", ".")
print(itens)
aList = []

for i in range(1, len(itens)):
    decimals = int(len(itens[i].split('.')[1]))
    for j in range(3):
        if j == 0:
            aList.append(round(float(itens[i]), decimals))
        else:
            randomFactor = randrange(0,10)
            randomFactor = (randomFactor/(10**(decimals-1)))
            x = random.uniform(-randomFactor, randomFactor)
            y = float(itens[i])
            aList.append(round((x+y), decimals))
    #print(aList)