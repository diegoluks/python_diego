nota1 = float(input("Digite a 1° nota: "))
nota2 = float(input("Digite a 2° nota: "))
nota3 = float(input("Digite a 3° nota: "))
nota4 = float(input("Digite a 4° nota: "))
nota5 = float(input("Digite a 5° nota: "))
total = nota1 + nota2 + nota3 + nota4 + nota5
media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print("A soma total das notas é: {}".format(total))
print("A média aritmética é {:.2f}".format(media))
if total >= 60:
    print("O aluno foi \033[32mAPROVADO!\033[m")
elif total < 60 and total >= 45:
    print("O aluno está de \033[33mRECUPERAÇÃO!\033[m")
else:
    print("O aluno foi \033[31mREPROVADO!\033[m")

