import random

random.seed()

class EmpacotarMacas:
    qtdePacotes = 0
    pesoMacas = 0.0
    def __init__(self, qtdeMacas):
        self.macas = qtdeMacas

    def empacotar(self):
        if self.macas >0:
            self.qtdePacotes+=1
            self.pacoteAtual=0.0
            while self.macas > 0:
                self.macas -= 1
                self.pesoDaMaca = 0.2 + ((random.random()/10)*3)
                self.pacoteAtual += self.pesoDaMaca
                self.pesoMacas += self.pesoDaMaca
                if self.pacoteAtual > 300:
                    self.qtdePacotes += 1
                    self.pacoteAtual = self.pesoDaMaca

    def __str__(self):
        return f'Foram empacotadas {self.qtdePacotes} caixas de maçãs com um total de {self.pesoMacas:.2f} de peso de maçãs'
    
macas=EmpacotarMacas(1000)
macas.empacotar()
print(macas)