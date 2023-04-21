salário = float(input("Qual é o salário do funcionário? R$"))
if salário > 1250:
    aumento = salário + (salário / 100 * 10) 
    print("Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora".format(salário, aumento))
    print("PARABÉNS pelo o aumento!! ")
else:
    salário <= 1250
    aumento = salário + (salário / 100 * 15)
    print("Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.".format(salário, aumento))
    print("PARABÉNS pelo o aumento!! ")

