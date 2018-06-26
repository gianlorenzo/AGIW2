from CrowdFind import UncOptCost


list = UncOptCost.uncOptCost(10000,15,0.9,0.2,10,5,1000,0.01)
for i in list:
    print(str(i.assumption))
    i.toString()



