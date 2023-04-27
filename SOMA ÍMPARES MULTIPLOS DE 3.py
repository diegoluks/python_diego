soma = 0
c = 0
for cont in range(1, 501, 2):
    if cont % 3 == 0:
        c = c + 1
        soma = soma + cont
print("A soma de todos os {} valores solicitados é {}".format(c, soma))