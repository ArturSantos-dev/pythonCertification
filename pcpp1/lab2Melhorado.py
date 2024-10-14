import json

class Vehicle:
    def __init__(self, numeroDeRegistro, anoDeProducao, passageiros, peso):
        self.numeroDeRegistro = numeroDeRegistro
        self.anoDeProducao = anoDeProducao
        self.passageiros = passageiros
        self.peso = peso

    def __str__(self):
        return (f"numeroDeRegistro: {self.numeroDeRegistro}, "
                f"anoDeProducao: {self.anoDeProducao}, "
                f"passageiros: {self.passageiros}, "
                f"peso: {self.peso}")

    def to_json(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        return Vehicle(data['numeroDeRegistro'], 
                       data['anoDeProducao'], 
                       data['passageiros'], 
                       data['peso'])

# Escolha do usuário
result = input("O que eu posso fazer por você? \n\t1 - produzir um JSON descrevendo um carro \n\t2 - decodificar um JSON em um carro\n")

if result == "1":
    numeroDeRegistro = input("Digite o número de registro do carro: ")
    anoDeProducao = input("Digite o ano de produção do carro: ")
    
    # Convertendo entrada para booleano para 'passageiros'
    passageiros_input = input("Passageiros [s/n]: ").strip().lower()
    if passageiros_input == 's':
        passageiros = True
    elif passageiros_input == 'n':
        passageiros = False
    else:
        print("Entrada inválida para passageiros. Use 's' ou 'n'.")
        exit(1)

    try:
        peso = float(input("Digite o peso do carro: "))
    except ValueError:
        print("Peso inválido! Por favor, insira um número.")
        exit(1)

    carro = Vehicle(numeroDeRegistro, anoDeProducao, passageiros, peso)
    print("Objeto: ", carro)
    print("JSON: ", carro.to_json())

elif result == "2":
    json_str = input("Digite o JSON do carro: ")
    try:
        carro = Vehicle.from_json(json_str)
        print("Objeto: ", carro)
    except json.JSONDecodeError:
        print("JSON inválido! Por favor, insira um JSON válido.")
else:
    print("Opção inválida!")
