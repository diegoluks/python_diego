peso = float(input("Qual o seu peso? (Kg) "))
altura = float(input("Qual a sua altura? (m) "))
IMC = (peso / altura ** 2)
print("O IMC dessa pessoa é de {:.2f}".format(IMC))
if IMC < 18.5:
    print("Você está abaixo do peso IDEAL!")
elif 18.5 <= IMC < 25:
    print("PARABÉNS! Você está com o peso IDEAL!")
elif 25 <= IMC < 30:
    print("CUIDADO! Você está com sobrepeso.")
elif 30 <= IMC < 40:
    print("Você está com obesidade!")
elif IMC >= 40:
    print("CUIDADO! Você está com obesidade morbida.")

