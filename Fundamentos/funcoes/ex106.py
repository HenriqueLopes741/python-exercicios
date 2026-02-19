c = ('0\033[m', 
    '\033[0;30;41m',
    '')

def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(msg)
    print('~' * tam)
    print(c[0], end='')


comando = ''

while True: 
    titulo('SISTEMA DE AJUDA pyHElp', 1)
    comando = str(input("Função ou Biblioteca: "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÈ LOGO')