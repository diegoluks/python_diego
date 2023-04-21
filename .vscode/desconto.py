preço = float(input("Qual o preço do produto? R$"))
descon1 = preço / 100 * 5
descon2 = preço - descon1
print("O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}".format(preço, descon2))
