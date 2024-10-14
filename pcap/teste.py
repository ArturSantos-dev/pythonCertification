v=[1,2,3]

def g(primeiraEntrada,segundaEntrada,minhaLambda):
    return minhaLambda(primeiraEntrada,segundaEntrada)

print(g(1,1, lambda x,y: v[x:y+1]))
