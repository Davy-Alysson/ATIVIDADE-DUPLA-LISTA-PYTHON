import os
os.system('cls')

vetorA = []
vetorB = []
vetorC = []

for i in range(5):

    numeros_a = int(input(f'Digite o {i + 1}° número para A: '))
    vetorA.append(numeros_a)
    numeros_b = int(input(f'Digite o {i + 1}° número para B: '))
    vetorB.append(numeros_b)
    vetorC.append(numeros_a + numeros_b)

print(f'Números do vetor A: {vetorA} ')
print(f'Números do vetor B: {vetorB} ')
print(f'Números do vetor C: {vetorC} ')