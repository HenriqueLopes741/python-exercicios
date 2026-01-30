num = input("Informe um número: ")

print(f"Unidade: {num[-1]}")
print(f"Dezena: {num[-2] if len(num) > 1 else 0}")
print(f"Centena: {num[-3] if len(num) > 2 else 0}")
print(f"Milhar: {num[-4] if len(num) > 3 else 0}")
