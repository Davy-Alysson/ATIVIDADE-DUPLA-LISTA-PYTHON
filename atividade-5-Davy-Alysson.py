import os
os.system('cls')

notas = []
quantidade_passados = []

for i in range(5):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

    if nota >= 6:
        quantidade_passados.append(1)
media = sum(notas) / len(notas)
    
    

print(f"Notas: {notas}")
print(f"Média: {media}")
print(f"Ficaram {len(quantidade_passados)} alunos acima da média")