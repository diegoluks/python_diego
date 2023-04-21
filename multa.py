velocidade = int(input("Qual a velocidade atua do carro? "))
if velocidade > 80:
    print("MULTADO! Você excedeu o limite permitido da via que é de 80Km/h")
    multa = (velocidade - 80) * 7
    print("Você deve pagar uma multa de R${:.2f}! ".format(multa))
else:
    print("Tenha um bom dia! Dirija com segurança! ")