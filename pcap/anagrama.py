def anagrama(texto1, texto2):
    anagram=True
    texto1 = texto1.lower()
    texto2 = texto2.lower()
    for letra in texto1:
        if letra in texto2:
            continue
        else:
            anagram=False
            break
    for letra in texto2:
        if letra in texto1:
            continue
        else:
            anagram=False
            break
    return anagram

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")
if len(palavra1) != len(palavra2):
    print("As palavras não são anagramas.")
elif palavra1 == palavra2:
    print("As palavras são anagramas.")
elif palavra1 == '' or palavra2 == '':
    print("As palavras não são anagramas.")
else:
    print("As palavras são anagramas." if anagrama(palavra1, palavra2) else "As palavras não são anagramas.")

