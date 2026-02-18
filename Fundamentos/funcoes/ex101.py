from datetime import datetime

ano = datetime.now().year

def alistamento(data):
    data = int(input('Em que ano você nasceu? '))
    idade = ano - data

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL' 