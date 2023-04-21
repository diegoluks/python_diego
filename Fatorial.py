n = int(input("Digite um número natural: "))
fat = 1

for i in range(1, n+1):
    fat *= i

print(f"{n}! = {fat}")
