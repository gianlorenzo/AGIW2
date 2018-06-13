from Utilities import Cost as c
from CrowdFind import CrowdSourcing as cs
from Items import Item


array = []
for i in range(0,5):
    x = Item.Item(0.8)
    array.append(x)


def uncOptCost(items,K1,select,err,m1,m2,max,unc):
    j = 0
    L = []
    U = []
    y00 = c.Y00(err, select, 0, max, m1, m2, unc)

    for i in items:
        i.setCost(y00)
        i.setSelectivity(select)
        U.append(i)

    for x in U:

        while(len(L)<K1 and j<5):
            print("-----------------ITERAZIONE n°" + str(j) + "----------------")
            U.sort(key=lambda x: x.expCost)
            newList = U[0:K1]
            j = j+1

            for w in newList:
                print("costo atteso: " + str(w.expCost))
                print(w)
                cs.crowdSourcing(err,w)
                print("n1: " + str(w.n1)+" n2: "+str(w.n2))
                costoCorrente = c.Y(err,select,w.n1,w.n2,m1,m2,y00)
                if (costoCorrente==0):
                    U.remove(w)
                    L.append(w)
                else:
                    w.setCost(costoCorrente)
    return L



list = uncOptCost(array,5,0.8,0.3,8,3,900,0.01)
for i in list:
    i.toString()






