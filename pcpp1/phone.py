class Phone:
    def __init__(self, number):
        self.number = number
    def turn_on(self):
        print("Phone is on")
    def turn_off(self):
        print("Phone is off")
    def call(self, number):
        print(f"Calling {number}")

meuTelefone = Phone(input("Digite o número do telefone: "))
meuTelefone.turn_on()
meuTelefone.call(input("Digite o número para ligar: "))
meuTelefone.turn_off()