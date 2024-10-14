import datetime

print(datetime.datetime.now())

def timeToExecute(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        end = datetime.datetime.now()
        print('tempo para executar a funcao '+func.__name__+':', (end - start))
    return wrapper
@timeToExecute
def soma(a, b):
    print(a + b)
soma(1, 2)

@timeToExecute
def subtracao(a, b):
    print(a - b)

subtracao(1, 2)

@timeToExecute
def multiplicacao(a, b):
    print(a * b)

multiplicacao(34543253432432143214324, 434321431453425342)