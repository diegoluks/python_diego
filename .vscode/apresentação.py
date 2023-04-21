import random
n1 = input("Primeiro aluno: ")
n2 = input("Segundo aluno: ")
n3 = input("Terceiro aluno: ")
n4 = input("Quarto aluno: ")
ordem = [n1,n2,n3,n4]
random.shuffle(ordem)
print("A ordem de apresentação será: ")
print(ordem)
