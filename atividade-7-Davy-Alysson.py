import os
os.system('cls')

lista_A_geral = []
lista_B_positivos = []
numeros_copiados = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número:"))
    lista_A_geral.append(numero)
    
    if numero > 0 and numero in lista_A_geral:
        numeros_copiados.append(numero)
        lista_B_positivos.append(numero)
        
print(f"Números positivos: {lista_B_positivos}")
print(f"Foram copiados {len(numeros_copiados)} números")