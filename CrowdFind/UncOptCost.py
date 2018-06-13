from Utilities import Cost as c



def uncOptCost(items,K1,err,select,m1,m2,max,unc):
    L = []
    U = []
    y00 = c.Y00(err, select, 0, max, m1, m2, unc)
    for i in items:
        U.append(i)
    for x in U:
        while(len(L)<K1):
            sorted(U for x.expCost in U)
            newList = U[0:K1]
            for w in newList:
                costoCorrente = c.Y(0.33,0.8,0,0,7,2,y00)
                if (costoCorrente==0):
                    K1 = K1-1
                    U.remove(w)






