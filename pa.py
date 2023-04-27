primeiro = int(input("1° termo: "))
razão = int(input("Razão: "))
décimo = primeiro + (10 -1) * razão
for cont in range(primeiro, décimo + razão, razão):
    print("{}".format(cont, end='→'))

