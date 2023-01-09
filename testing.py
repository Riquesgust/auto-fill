import random
from random import randrange
import decimal
itens = input()
itens = itens.split('/')
for i in range(1, len(itens)):
    itens[i] = itens[i].replace(",", ".")
aList = []


for i in range(0,len(itens)):
    print(i)
    for j in range(i+1, int(itens[i])+1):
        print(itens[j])
    
    i=1+int(itens[i])
    print(i)

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