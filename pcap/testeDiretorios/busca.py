import os

def find(path, dir_name):
    # Função para buscar recursivamente os diretórios
    for root, dirs, files in os.walk(path):
        if dir_name in dirs:
            print(os.path.join(root, dir_name))

if __name__ == "__main__":
    path = "./tree"  # Caminho inicial da busca
    dir_name = "python"  # Nome do diretório a ser encontrado
    find(path, dir_name)
