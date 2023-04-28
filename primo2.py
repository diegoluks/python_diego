num = int(input("Digite um n°: "))
total = 0
for cont in range(1, num + 1):
    if num % cont == 0:
        print("\033[32m", end=' ')
        total += 1
    else:
        print("\033[31m", end=' ')
    print("{}".format(cont), end=' ')
print("\n\033[33mO n° {} foi dividido {} vezes\033[m".format(num, total))
if total == 2:
    print("\033[32m")
    print("O n° {} é PRIMO por ser divisível por 1 e por ele mesmo.".format(num))
else:
    print("\033[31m")
    print("O n° {} NÃO É PRIMO!".format(num))



