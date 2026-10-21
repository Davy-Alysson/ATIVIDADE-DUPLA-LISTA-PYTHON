import os
os.system('cls')


temperaturas = []

for i in range(7):
    temperatura = float(input(f'Digite a temperatuda do {i+1}º dia da semana: '))
    temperaturas.append(temperatura)

for i in range(7):
    print(f'{i + 1}ª Temperatura: {temperaturas[i]:.1f}°C')

print(f'A média da temperatura semanal: {sum(temperaturas) / len(temperaturas):.1f}°')
print(f'Maior temperatura registrada: {max(temperaturas)}°')
print(f'Menor temperatura registrada: {min(temperaturas)}°')