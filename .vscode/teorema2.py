import math
an = float(input("Digite um ângulo: "))
sen = math.sin(math.radians(an))
print("O ângulo de {} tem o SENO de {:.2f}".format(an, sen))
coss = math.cos(math.radians(an))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(an, coss))
tang = math.tan(math.radians(an))
print("O ângulo de {} tem a tangente de {:.2f}".format(an, tang))

