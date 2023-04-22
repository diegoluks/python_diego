casa = float(input("Qual o valor da casa? R$"))
salário = float(input("Qual o salário do comprador? R$"))
anos = int(input("Em quantos anos irá pagar? "))
prestação = casa / (anos * 12)
mínimo = (salário / 100) * 30
print("para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}".format(casa, anos, prestação))
if prestação <= mínimo:
    print("\033[32mEmpréstimo pode ser CONCEDIDO!\033[m")
else:
    print("\033[31mEmprestimo não pode ser CONCEDIDO!\033[m")