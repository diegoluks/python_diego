num = int(input("Digite um número para ver sua tabuada: "))
print("-" * 12)
for cont in range(1, 11):
    print("{} x {:1} = {}".format(num, cont, num * cont))
print("-" * 12)
    