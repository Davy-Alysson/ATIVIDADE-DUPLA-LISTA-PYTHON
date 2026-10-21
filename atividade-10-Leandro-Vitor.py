import os
os.system('cls')

idades = []
maiores_de_idade = 0

print("--- Leitura de Idades (0 a 120 anos) ---\n")

for i in range(5):
    while True:
        try:
            idade = int(input(f"Digite a idade da {i + 1}ª pessoa: "))
            if 0 <= idade <= 120:
                break
            else:
                print("Idade inválida! Digite um valor entre 0 e 120.")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

    idades.append(idade)

    # Conta maiores de idade (18 anos ou mais)
    if idade >= 18:
        maiores_de_idade += 1

# Exibe as estatísticas
print("\n--- Resultados ---")
print(f"Maior idade: {max(idades)} anos")
print(f"Menor idade: {min(idades)} anos")
print(f"Quantidade de maiores de idade (>= 18): {maiores_de_idade}")