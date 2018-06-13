from random import random

#A seconda della selettività e dell'errore del worker, dà una risposta positiva o negativa
def giveAnAnswer(err,item):
    if (random()<=err):
        return not item.assumption
    else:
        return item.assumption

def crowdSourcing(err, item):
    if (giveAnAnswer(err,item) == 1):
        item.n1 = item.n1 + 1
    else:
        item.n2 = item.n2 + 1


