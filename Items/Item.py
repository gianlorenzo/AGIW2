from random import random
from Utilities import Cost as c

class Item:

    def __init__(self, id, selectivity):
        self.n1 = 0
        self.n2 = 0
        self.selectivity = selectivity
        self.id = id
        self.expCost = 0
        if (random()<=self.selectivity):
            self.assumption = True
        else:
            self.assumption = False

    def setSelectivity(self,s):
        self.selectivity = s

    def setCost(self,c):
        self.expCost = c

    def setN1(self,yes):
        self.n1 = yes

    def setN2(self,no):
        self.n2 = no

    def toString(self):
        print("Risposte N1: " + str(self.n1) + "; Risposte N2: " + str(self.n2) + "; ID: " + str(self.id))