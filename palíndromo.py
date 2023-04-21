# Define a função que verifica se um número é um palíndromo
def is_palindrome(n):
    return str(n) == str(n)[::-1]

# Define a função que converte um número de Lychrel para palíndromo
def lychrel_to_palindrome(n, max_iterations=500):
    for i in range(max_iterations):
        n += int(str(n)[::-1])
        if is_palindrome(n):
            return n
    return None

# Solicita ao usuário o número de entrada
n = int(input("Digite um número de Lychrel: "))

# Converte o número para palíndromo (se possível)
palindrome = lychrel_to_palindrome(n)

# Exibe o resultado
if palindrome:
    print(f"O número {n} foi convertido para o palíndromo {palindrome}.")
else:
    print(f"Não foi possível converter o número {n} para um palíndromo em até 500 iterações.")
