def caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

def main():
    while True:
        try:
            text = input("Digite uma linha de texto para criptografar: ")
            shift = int(input("Digite o valor de mudança (1-25): "))
            if 1 <= shift <= 25:
                break
            else:
                print("Por favor, insira um valor de mudança entre 1 e 25.")
        except ValueError:
            print("Valor inválido. Por favor, insira um número inteiro.")

    encrypted_text = caesar_cipher(text, shift)
    print("Texto criptografado:", encrypted_text)

if __name__ == "__main__":
    main()
