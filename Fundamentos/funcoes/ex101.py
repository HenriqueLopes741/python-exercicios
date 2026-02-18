from datetime import datetime

atual = datetime.now().year

def voto(ano):
    idade = atual - ano

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'

nas = int(input("Em que ano você nasceu? "))
print(voto(nas))
