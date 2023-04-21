numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é maior que 1
if numero > 1:
    # Loop para verificar se o número é divisível por algum número menor que ele
    for i in range(2, numero):
        if (numero % i) == 0:
            print("não primo")
            break
    else:
        print("primo")
else:
    print("não primo")
