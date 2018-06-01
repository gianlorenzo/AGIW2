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
        CQ = []
        for c in I1:
            n1 = 5
            n2 = 10
            CQ.append(min(n1,n2))
        for elem in CQ:
            answer = crowdSourcing(elem)
            if answer == 1:
                U.remove(elem)
                L.append(elem)
            else:
                U.remove(elem)
    return L



uncOptCost(items,3)