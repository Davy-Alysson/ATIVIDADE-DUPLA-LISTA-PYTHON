import os
os.system('cls')

numeros = []
numeros_maiores_10 = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número:"))
    numeros.append(numero)

    if numero > 10:
        numeros_maiores_10.append(numero)


print(f"A soma de todos os números é: {sum(numeros)}")
print(f"Tem {len(numeros_maiores_10)} maiores que 10.")

    