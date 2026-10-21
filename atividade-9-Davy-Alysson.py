import os
os.system('cls')

numeros = []
numeros_pares_e_impares = []


for i in range(6):
    numero = int(input('Digite o {i+1}º número: '))
    

for numero in numeros:
    if numero % 2 == 0:
        numeros_pares_e_impares.append(0)
    else:
        numeros_pares_e_impares.append(1)
        
        
print(f"Numeros originais: {numeros}")
print(f"Numeros transformados: {numeros_pares_e_impares}")
    
