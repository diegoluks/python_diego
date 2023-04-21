meu_cartão = int(input("Digite o n° do seu cartão de crédito: "))
cartão_lido = 1
achei_meu_cartão_na_lista = False
while cartão_lido != 0 and not achei_meu_cartão_na_lista:
    cartão_lido = int(input("Digite o n° do próximo cartão de crédito: "))
    if cartão_lido == meu_cartão:
        achei_meu_cartão_na_lista = True
if achei_meu_cartão_na_lista:
    print("Meu cartã está lá")
else:
    print("Meu cartão não está lá")
