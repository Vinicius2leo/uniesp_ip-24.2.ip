import numpy as np

# Definindo o tamanho da matriz
n = 10

# Criando a matriz A com valores inteiros aleatórios entre 0 e 100
A = np.random.randint(0, 100, size=(n, n))

# Imprimindo a matriz A
print("Matriz A:")
print(A)

# Calculando a soma de todos os valores da matriz A
soma_A = np.sum(A)
print("\nSoma de todos os valores da matriz A:", soma_A)

# Criando a matriz B, onde cada item é o valor da matriz A * 3
B = A * 3

# Imprimindo a matriz B
print("\nMatriz B (A * 3):")
print(B)