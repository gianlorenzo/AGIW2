
def yes1(err):
    return (1-err)

def yes0(err):
    return (err)

def no0(err):
    return (1-err)

def no1(err):
    return (err)

def pN1N21(n1,n2,err):
    return (((1-err)**n1)*((err)**n2))

def pN1N20(n1,n2,err):
    return (((err)**n1)*((1-err)**n2))

def p1N1N2(n1,n2,err,selectivity):
    return (pN1N21(n1,n2,err)*selectivity/pN1N2(n1,n2,err,selectivity))

def p0N1N2(n1,n2,err,selectivity):
    return (pN1N20(n1,n2,err)*(1-selectivity)/pN1N2(n1,n2,err,selectivity))

def pN1N2(n1,n2,err,selectivity):
    return (selectivity*pN1N21(n1,n2,err)+(1-selectivity)*pN1N20(n1,n2,err))

def p1(errorRate,selectivity,n1,n2):
    return p1N1N2(n1,n2,errorRate,selectivity)*yes1(errorRate)+p0N1N2(n1,n2,errorRate,selectivity)*yes0(errorRate)

def p0(errorRate,selectivity,n1,n2):
    return p1N1N2(n1,n2,errorRate,selectivity)*no1(errorRate)+p0N1N2(n1,n2,errorRate,selectivity)*no0(errorRate)


## Funziona tutto