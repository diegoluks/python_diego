from datetime import date
atual = date.today().year
nascimento = int(input("Ano de nascimento: "))
idade = atual - nascimento
print("O atleta tem {} anos.".format(idade))
if idade <= 9:
    print("CLASSIFICAÇÃO: Mirim")
elif idade <= 14:
    print("CLASSIFICAÇÃO: Infantil")
elif idade <= 19:
    print("CLASSIFICAÇÃO: Junior")
elif idade <= 25:
    print("CLASSIFICAÇÃO: Sênior")
else: 
    print("CLASSIFICAÇÃO: Master")