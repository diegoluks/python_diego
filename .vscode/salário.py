salário = float(input("Qual é o salário do funcionário? R$"))
aumen = salário + (salário / 100 * 15)
print("Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}".format(salário, aumen))
