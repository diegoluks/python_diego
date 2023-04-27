soma = 0
c = 0
for cont in range(1, 7):
    n = int(input("Digite o {}°: ".format(cont)))
    if n % 2 == 0:
        soma = soma + n
        c = c + 1
print("Você informou {} n° pares e a soma foi {}.".format(c, soma))




        