import os
os.system('cls')

numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número:"))
    numeros.append(numero)
    
print(f'Números em ordem: {numeros}')
print(f'Números inversos: {numeros[4], numeros[3], numeros[2], numeros[1], numeros[0]}')