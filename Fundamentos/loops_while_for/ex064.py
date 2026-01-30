
n = dig = total = 0
while n != 999:
    n = int(input('digite um valor[digite 999 para parar]: '))
    if n != 999:
        total += n
        dig += 1
print(f'foram digitados \033[31m{dig}\033[m números \n'
      f'e a soma de todos eles é \033[31m{total}\033[m')

