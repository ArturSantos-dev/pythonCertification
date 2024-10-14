def coletaSudoku():
    num = []
    for i in range(9):
        while True:
            try:
                entrada = input(f"Digite nove dígitos para o grupo {i+1}: ")
                if len(entrada) != 9 or not entrada.isdigit():
                    print("Digite exatamente nove dígitos.")
                    continue
                num.append([int(digito) for digito in entrada])  # Converte cada dígito em um inteiro e adiciona à lista num
                break
            except ValueError:
                print("Valor inválido. Digite novamente.")
    return num

def formaSudoku(jogo):
    # Verifica horizontal e vertical
    for i in range(9):
        linha = set()
        coluna = set()
        for j in range(9):
            if jogo[i][j] == 0 or jogo[j][i] == 0:
                return False
            if jogo[i][j] in linha or jogo[j][i] in coluna:
                return False
            linha.add(jogo[i][j])
            coluna.add(jogo[j][i])
    
    # Verifica quadrados 3x3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not verificaQuadrado3x3(jogo, i, j):
                return False

    return True

def verificaQuadrado3x3(jogo, linha, coluna):
    numeros = set()
    for i in range(3):
        for j in range(3):
            num = jogo[linha + i][coluna + j]
            if num in numeros:
                return False
            numeros.add(num)
    return True

# Coleta e imprime o Sudoku
sudoku = coletaSudoku()
for linha in sudoku:
    print(linha)

# Verifica se o Sudoku está correto
print(formaSudoku(sudoku))