from datetime import date
atual = date.today().year
nascimento = int(input("Ano de nascimento: "))
idade = atual - nascimento
m = ("masculino")
f = ("feminino")
sexo = input("Escreva o sexo: ")
print("Quem nasceu em {} tem {} anos em {}.".format(nascimento, idade, atual))
if sexo == m:
    print("O alistamento é obrigatório para o sexo \033[31mMASCULINO!\033[m")
elif sexo == f:
    print("O alistamento não é obrigatório para o sexo \033[32mFEMININO!\033[m")
if idade == 18 and sexo == m:
    print("Você tem que se alistar \033[31mIMEDIATAMENTE!\033[m")
elif idade < 18 and sexo == m:
    saldo = 18 - idade
    print("Ainda faltam {} anos para o seu alistamento.".format(saldo))
    ano = atual + saldo
    print("Seu alistamento será em {}.".format(ano))
elif idade > 18 and sexo == m:
    saldo = idade - 18
    print("Você já deveria ter se alistado há {} anos.".format(saldo))
    ano = atual - saldo
    print("Seu alistamento foi em {}.".format(ano))
    
