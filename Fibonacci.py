# Inicializa os dois primeiros termos da sequência
a, b = 0, 1
# Inicializa a soma dos termos pares
soma = 0

# Loop para calcular a sequência de Fibonacci
while b < 4000000:
    # Verifica se o termo atual é par
    if b % 2 == 0:
        soma += b

    # Calcula o próximo termo da sequência
    a, b = b, a + b

# Exibe a soma dos termos pares
print(soma)
