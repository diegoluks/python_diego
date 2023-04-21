km = float(input("Qual a quantidade de km percorridos? "))
dias = int(input("Qual a quantidade de dias alugados? "))
pagamento = (dias * 60) + (km * 0.15)
print("O valor a pagar é R${:.2f}".format(pagamento))
