import json

class Vehicle_To_Json:
    def __init__(self, numeroDeRegistro, anoDeProducao, passageiros, peso):
        self.numeroDeRegistro = numeroDeRegistro
        self.anoDeProducao = anoDeProducao
        self.passageiros = passageiros
        self.peso = peso
    def __str__(self):
        return f"numeroDeRegistro: {self.numeroDeRegistro}, anoDeProducao: {self.anoDeProducao}, passageiros: {self.passageiros}, peso: {self.peso}"

class Json_To_Vehicle:
    def __init__(self, json):
        self.numeroDeRegistro = json["numeroDeRegistro"]
        self.anoDeProducao = json["anoDeProducao"]
        self.passageiros = json["passageiros"]
        self.peso = json["peso"]
    def __str__(self):
        return f"numeroDeRegistro: {self.numeroDeRegistro}, anoDeProducao: {self.anoDeProducao}, passageiros: {self.passageiros}, peso: {self.peso}"

result=input("O que eu posso fazer por você? \n\t1 - produzir um Json descrevendo um carro \n\t2 - decodificar uma Json em um carro\n")

if result == "1":
    numeroDeRegistro = input("Digite o numero de registro do carro: ")
    anoDeProducao = input("Digite o ano de produção do carro: ")
    passageiros = input("Digite o numero de passageiros do carro: ")
    peso = input("Digite o peso do carro: ")
    carro = Vehicle_To_Json(numeroDeRegistro, anoDeProducao, passageiros, peso)
    print("Objeto: ", carro)
    print("Json: ", json.dumps(carro.__dict__))
    print("Json: ", carro.__dict__)
elif result == "2":
    json_str = input("Digite o Json do carro: ")
    json_car = json.loads(json_str)
    carro = Json_To_Vehicle(json_car)
    print("Json: ", json_car)
    print("Objeto: ", carro)
