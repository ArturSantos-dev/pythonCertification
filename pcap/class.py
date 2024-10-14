while True:
    try:
        num = int(input("Digite um número inteiro: "))
        break
    except ValueError:
        print("Valor inválido. Digite novamente.")

num_array = list(str(num))

for p in range(5):
    for i in range(len(num_array)):
        if p == 0:
            if num_array[i] == "1":
                print("  # ", end="")
            elif num_array[i] in ["2", "3", "5", "6", "7", "8", "9", "0"]:
                print("### ", end="")
            elif num_array[i] == "4":
                print("# # ", end="")
        elif p == 1:
            if num_array[i] in ["1", "2", "3", "7"]:
                print("  # ", end="")
            elif num_array[i] in ["4", "8", "9", "0"]:
                print("# # ", end="")
            elif num_array[i] in ["5", "6"]:
                print("#   ", end="")
        elif p == 2:
            if num_array[i] in ["1", "7"]:
                print("  # ", end="")
            elif num_array[i] in ["2", "3", "4", "5", "6", "8", "9"]:
                print("### ", end="")
            elif num_array[i] == "0":
                print("# # ", end="")
        elif p == 3:
            if num_array[i] in ["1", "4", "7", "9", "5", "3"]:
                print("  # ", end="")
            elif num_array[i] in ["6", "8", "0"]:
                print("# # ", end="")
            elif num_array[i] == "2":
                print("#   ", end="")
        elif p == 4:
            if num_array[i] in ["1", "4", "7"]:
                print("  # ", end="")
            elif num_array[i] in ["2", "3", "5", "6", "8", "9", "0"]:
                print("### ", end="")
        print(" ", end="")  # Para separar os números
    print()  # Nova linha após cada linha completa de p





