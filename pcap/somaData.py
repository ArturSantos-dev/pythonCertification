
while True:
    try:
        num = int(input("Digite uma data: "))
        break
    except ValueError:
        print("Valor invalido. Digite novamente.")

num_array = list(str(num))
while num >9:
    num=0
    for numero in num_array:
        num=num+int(numero)
    num_array = list(str(num))
print(num)