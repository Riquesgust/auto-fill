

finaList = []
while(True):
    itens = input().split('/')
    for i in range(1, len(itens)):
        itens[i] = itens[i].replace(",", ".")
    aList = []
        
    for i in range(1, len(itens)):
        decimals = int(len(itens[i].split('.')[1]))
        for j in range(3):
            if j == 0:
                
                aList.append((str(round(float(itens[i]), decimals))).replace(".",","))
            else:
                randomFactor = randrange(0,10)
                randomFactor = (randomFactor/(10**(decimals-1)))
                x = random.uniform(-randomFactor, randomFactor)
                y = float(itens[i])
                z = (str(round((x+y), decimals))).replace(".", ",")
                aList.append(z)
    finaList.append(aList)
    if((input("Continue?:").lower()) != ""):
        break


