# Solicita ao usuário o número de termos que deseja calcular
n = int(input("Digite o número de termos que deseja calcular: "))

# Inicializa os dois primeiros termos da sequência
a, b = 0, 1

# Exibe os primeiros n termos da sequência
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
