real = float(input("Digite um valor em reais: R$"))
dol = 4.99
eur = 5.47
yuan = 0.73
cot1 = real / dol
cot2 = real / eur
cot3 = real / yuan

print("A conversão de R${:.2f} reais para dólares é: ${:.2f}".format(real, cot1))
print("A conversão de R${:.2f} reais para euro é: ${:.2f}".format(real, cot2))
print("A conversão de R${:.2f} reais para yuan é: ${:.2f}".format(real, cot3))
