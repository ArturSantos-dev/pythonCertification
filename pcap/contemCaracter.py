def compararCaracteres(texto1, texto2):
    for letra in texto1:
        if letra in texto2:
            continue
        else:
            return False
    return True
primeiro=input("Digite o primeiro texto: ").lower()
segundo=input("Digite o segundo texto: ").lower()
print(compararCaracteres(primeiro, segundo))