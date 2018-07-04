from Utilities import Cost as c
from CrowdFind import CrowdSourcing as cs
from Items import Item
import logging
import sys
from datetime import datetime

def setItems(maxAnswers,selectivity):
    array = []
    for i in range(0,maxAnswers):
        x = Item.Item(i, selectivity)
        array.append(x)
    return array


def uncOptCost(maxAnswers,K1,select,err,m1,m2,max,unc):
    log = open("logging.log","a")
    sys.stdout = log
    print("start " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.warning("start " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    numFasi = 0
    numDomande = 0
    L = []
    U = []
    items = setItems(maxAnswers,select)

    #Mi calcolo il costo atteso per ogni elemento in assenza di risposte ricevute
    y00 = c.Y00(err, select, 0, max, m1, m2, unc)

    #Copio il dataset in una lista temporanea su cui poi eseguirò le operazioni di remove
    for i in items:
        i.setCost(y00)
        i.setSelectivity(select)
        U.append(i)


    #Per ogni elemento in U, finché la nostra lista di elementi Yes è minore del numero di elementi yes desiderati
    while(len(L)<K1):
        print("-----------------FASE n°" + str(numFasi) + "----------------")
        logging.warning("-----------------FASE n°" + str(numFasi) + "----------------")
        U.sort(key=lambda x: x.expCost)
        newList = U[0:K1-len(L)]
        numFasi = numFasi+1

        for w in newList:
            print("costo atteso: " + str(w.expCost))
            logging.warning("Costo atteso: " + str(w.expCost))
            print(str(w.assumption))

            #Eseguo sempre il minimo numero di domande tra quelle necessarie per raggiungere la soglia yes (m1) e la soglia no (m2)
            for k in range(0,min(m1-w.n1, m2-w.n2)):
                numDomande = numDomande+1
                cs.crowdSourcing(err,w)

            #Se l'item per la strategy è NO allora lo rimuovo dal dataset
            if (w.n2==m2):
                U.remove(w)
            print("n1: " + str(w.n1)+" n2: "+str(w.n2) + " id: " + str(w.id))
            logging.warning("n1: " + str(w.n1)+" n2: "+str(w.n2) + " id: " + str(w.id))
            costoCorrente = c.Y(err,select,w.n1,w.n2,m1,m2,y00)
            if (costoCorrente==0):
                U.remove(w)
                L.append(w)
            else:
                w.setCost(costoCorrente)
    print("Numero fasi: " + str(numFasi))
    logging.warning("Numero fasi: " + str(numFasi))
    print("Numero domande: " + str(numDomande))
    logging.warning("Numero domande: " + str(numDomande))
    print("fine " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.warning("fine " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return L








