# Inicializando o vetor
VET = []

# Lendo 10 números
for i in range(10):
    numero = int(input(f"Digite o número {i + 1}: "))
    VET.append(numero)

# Verificando números repetidos
for i in range(10):
    for j in range(i + 1, 10):
        if VET[i] == VET[j]:
            print(f"O número {VET[i]} se repete nas posições {i} e {j}")