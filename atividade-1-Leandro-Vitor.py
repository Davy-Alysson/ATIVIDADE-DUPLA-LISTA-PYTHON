import os
os.system('cls')


vetor_numero = []

for i in range(5):

    numero = int(input(f'Digite o {i+1}º número: '))
    vetor_numero.append(numero)

print(f'Números em ordem: {vetor_numero} ')
print(f'Números em ordem inversa: {vetor_numero[4], vetor_numero[3],vetor_numero[2],vetor_numero[1],vetor_numero[0], }')