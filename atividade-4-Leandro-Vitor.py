import os
os.system('cls')

numeros = []

for  i in range(8):
    
    numero = int(input(f'Digite o {i + 1}° número: '))
    numeros.append(numero)
os.system('cls')
busca = int(input('Digite um número para pesquisar: '))
    
if busca in numeros:
    posicao = numeros.index(busca)
    print(f'O número existe e está na posição: {posicao + 1}')
else:
    print('O número não foi encontrado. ')