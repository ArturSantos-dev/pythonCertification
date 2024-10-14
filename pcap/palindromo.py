def palindromo(texto):
    texto = texto.lower()
    texto=''.join(texto.split())
    return texto == texto[::-1]

textDoUsuario=input("Digite um texto para verificar se é um palíndromo: ")
if palindromo(textDoUsuario):
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")
