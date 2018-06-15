from Utilities import Cost as c
from CrowdFind import CrowdSourcing as cs
from Items import Item


array = []
for i in range(0,1000000):
    x = Item.Item(i, 0.8)
    array.append(x)


def uncOptCost(items,K1,select,err,m1,m2,max,unc):
    numFasi = 0
    numDomande = 0
    L = []
    U = []
    y00 = c.Y00(err, select, 0, max, m1, m2, unc)

    for i in items:
        i.setCost(y00)
        i.setSelectivity(select)
        U.append(i)

    for x in U:

        while(len(L)<K1):
            print("-----------------FASE n°" + str(numFasi) + "----------------")
            U.sort(key=lambda x: x.expCost)
            newList = U[0:K1]
            numFasi = numFasi+1

            for w in newList:
                print("costo atteso: " + str(w.expCost))
                print(str(w.assumption))
                for k in range(0,min(m1-w.n1, m2-w.n2)):
                    numDomande = numDomande+1
                    cs.crowdSourcing(err,w)
                print("n1: " + str(w.n1)+" n2: "+str(w.n2) + " id: " + str(w.id))
                costoCorrente = c.Y(err,select,w.n1,w.n2,m1,m2,y00)
                if (costoCorrente==0):
                    U.remove(w)
                    L.append(w)
                else:
                    w.setCost(costoCorrente)
    print("Numero fasi: " + str(numFasi))
    print("Numero domande: " + str(numDomande))
    return L



list = uncOptCost(array,15,0.05,0.5,8,5,1000,0.01)
for i in list:
    print(str(i.assumption))
    i.toString()






