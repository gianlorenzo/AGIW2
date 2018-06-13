from Utilities import Probability as p

#Costo in domande per determinare se un nuovo item soddisfa la proprietà p
def Y00(err,select,current_min,current_max,m1,m2,uncertainty):
    alfa = current_min + (current_max - current_min) / 2
    k = p.p1(err,select,0,0)*Y(err,select,1,0,m1,m2,alfa) + p.p0(err,select,0,0)*Y(err,select,0,1,m1,m2,alfa) + 1
    if (alfa >= k-uncertainty and alfa <= k+uncertainty):
        return alfa
    if (alfa < k):
        print('valore di alfa: ' + str(alfa) + ' valore > di alfa: ' + str(k))
        return Y00(err,select,alfa,current_max,m1,m2,uncertainty)
    if (alfa > k):
        print('valore di alfa: ' + str(alfa) + ' valore < di alfa: ' + str(k))
        return Y00(err,select,current_min,alfa,m1,m2,uncertainty)

#Costo in domande per determinare se un nuovo item soddisfa la proprietà p a partire da un insieme (n1,n2) di risposte
def Y(err, select, n1, n2, m1, m2, y00):
    if (n1==m1):
        return 0
    if (n2==m2):
        return y00
    return min(y00, p.p1(err,select,n1,n2)*Y(err,select,n1+1,n2,m1,m2,y00) + p.p0(err,select,n1,n2)*Y(err,select,n1,n2+1,m1,m2,y00) + 1)

print('Valore di Y00: ' + str(Y00(0.1,0.05,0,100,6,3,0.01)))



