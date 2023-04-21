distância = float(input("Qual a distância da sua viagem? "))
print("Você irá fazer uma viagem de {:.1f}Km.".format(distância))
if distância <= 200:
    preço = distância * 0.50
    print("O preço da viagem será de R${:.2f}".format(preço))
    print("Faça uma boa viagem! ")
else:
    distância > 200
    preço = distância * 0.45
    print("O preço da viagem será de R${:.2f}.".format(preço))
    print("Faça uma boa viagem! ")
