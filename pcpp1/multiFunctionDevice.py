class Scanner:
    def __init__(self, name):
        self.name = name

    def scan(self):
        print(f'{self.name} está escaneando um documento')

class Printer:
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f'{self.name} está imprimindo um documento')

class Fax():
    def __init__(self, name):
        self.name = name
    def print(self):
        print(f'{self.name} está enviando um documento por fax')
    def scan(self):
        print(f'{self.name} está recebendo um documento por fax')

class SPF(Scanner, Printer, Fax):
    def __init__(self, name):
        Scanner.__init__(self, name)
        Printer.__init__(self, name)
        Fax.__init__(self, name)

class SFP(Scanner, Fax, Printer):
    def __init__(self, name):
        Scanner.__init__(self, name)
        Fax.__init__(self, name)
        Printer.__init__(self, name)

spf=SPF('SPF')
sfp=SFP('SFP')
spf.scan()
spf.print()
sfp.scan()
sfp.print()