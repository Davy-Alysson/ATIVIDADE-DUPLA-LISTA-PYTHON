import os
os.system('cls')

nomes = []
salarios = []

acima_de_dois_mil = 0


for i in range(5):
    nome = input(f'Digite o nome do {i+1}° funcionário: ')
    salario = float(input(f'Digite o salário do {nome} funcionário: R$ '))
    
    nomes.append(nome)
    salarios.append(salario)
    
    if salario > 2000.00:
        acima_de_dois_mil += 1
    
    maior_salario = max(salarios)
    indice_maior = salarios.index(maior_salario)
    nome_maior_salario = nomes[indice_maior]

print(f'Funcionário com maior salário: {nome_maior_salario} (R$ {maior_salario:.2f}) ')
print(f'Quantidade de funcionários que ganham acima de R$ 2.000,00: {acima_de_dois_mil} pessoas')