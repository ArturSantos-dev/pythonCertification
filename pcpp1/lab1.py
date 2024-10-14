import sys
import requests

# Configuração inicial
servidor = 'localhost'
porta = 3000

# Verificar a quantidade de argumentos
if len(sys.argv) == 2:
    servidor = sys.argv[1]
elif len(sys.argv) == 3:
    servidor = sys.argv[1]
    try:
        porta = int(sys.argv[2])
        if porta < 1 or porta > 65535:
            print("Porta ínvalida - adeus")
            sys.exit(2)
    except ValueError:
        print("Porta ínvalida - adeus")
        sys.exit(2)
else:
    print("Faltando argumentos - adeus")
    sys.exit(1)

def getHeader():
    try:
        reply = requests.head(f'http://{servidor}:{porta}/cars')
        print(reply.status_code)
    except requests.RequestException:
        print('Communication error')
        sys.exit(4)
    else:
        if reply.status_code == requests.codes.ok:
            return reply.headers
        elif reply.status_code == requests.codes.not_found:
            print("Resource not found")
            sys.exit(4)
        else:
            print('Server error')
            sys.exit(3)
    return None

# Executa a função e imprime o cabeçalho
headers = getHeader()
if headers:
    print(headers)

