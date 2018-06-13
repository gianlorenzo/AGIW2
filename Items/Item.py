from Utilities import Cost as c



class Item:

    n1 = 0
    n2 = 0
    isValuate = False
    selectivity = 0.8
    expCost = c.Y00(0.1,selectivity,0,500,15,10,0.01)


    def setSelectivity(self,s):
        self.selectivity = s

    def setCost(self,c):
        self.expCost = c

    def setN1(self,yes):
        self.n1 = yes

    def setN2(self,no):
        self.n2 = no

    def setValuate(self):
        self.selectivity = True



x = Item()

print(x.y)