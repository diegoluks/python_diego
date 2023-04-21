numero = input("Digite um número inteiro: ")

# Loop para verificar se existe um dígito adjacente igual
for i in range(len(numero)-1):
    if numero[i] == numero[i+1]:
        print("sim")
        break
else:
    print("não")
