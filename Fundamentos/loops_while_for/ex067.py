n1 = cont = 0 
soma = 0
while True:
    print('-' * 20 )
    n1 = int(input('Quer ver a tabuada de qual valor?'))
    if n1 < 0: 
        break
    print('-' * 20 )
    for c in range (1, 11):
        print(f'{n1} x {c} = {n1*c}')
print('PROGRAMA TABUADA ENCERRADO VOLTE SEMPRE!')