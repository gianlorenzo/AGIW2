from Utilities import Cost as c

class Item:

    n1 = 0
    n2 = 0
    isValuate = False
    selectivity = 0.8
    y = c.Y00(0.33,selectivity,0,200,15,50,0.05)


    def setSelectivity(self,s):
        self.selectivity = s

    def setCost(self,c):
        self.y = c

    def setN1(self,yes):
        self.n1 = yes

    def setN2(self,no):
        self.n2 = no

    def setValuate(self):
        self.selectivity = True



x = Item()

x.y