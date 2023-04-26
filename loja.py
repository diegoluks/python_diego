print("{:=^40}".format(" LOJAS FREITAS "))
preço = float(input("Preço das compras: R$"))
print('''FORMAS DE PAGAMENTO
[1] À vista dinheiro/PIX
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input("Qual é a opção? "))
if opção == 1:
    total = preço - (preço / 100 * 10)
elif opção == 2:
    total = preço - (preço / 100 * 5)
elif opção == 3:
    total = preço 
    parcela = total / 2
    print("Sua compra será parcelada em 2x de R${:.2f} sem juros.".format(parcela))
elif opção == 4:
    total = preço + (preço / 100 * 20)
    totalparc = int(input("Quantas parcelas? "))
    parcela = total / totalparc
    print("Sua compra será parcelada em {}x de R${:.2f} com juros.".format(totalparc, parcela))
else:
    total = preço
    print("\033[31mOPÇÃO INVÁLIDA DE PAGAMENTO.TENTE NOVAMENTE!\033[m")
print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preço, total))
print("{:=^40}".format(" LOJAS FREITAS "))


    