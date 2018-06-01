from random import choice

def crowdSourcing(elem):
    answer = choice([1, 0])
    return answer


items = [1,2,3,4,5,6,7,8,7,7,6,55]


def uncOptCost(I,K1):
    L = []
    U = []
    for i in I:
        U.append(i)
    while (len(L) < K1):
        I1 = []
        for x in U[0:K1]:
            I1.append(x)
        CQ = {}
        for c in I1:
            n1 = 5 # è il numero minore di YES necessari per far diventare Y(R(I)=0
            n2 = 10 # il numero minore di NO necessari per far diventare Y(R(I))= Y(0,0)
            CQ[c] = min(n1,n2)
        for elem in CQ.keys():
            answer = crowdSourcing(elem)
            print (str(elem)+" "+str(answer))
            if answer == 1:
                U.remove(elem)
                L.append(elem)
                print("Lista U " + str(U))
                print("Lista L "+ str(L))
            else:
                U.remove(elem)
                print("Lista U "+str(U))
    return L

uncOptCost(items,3)
