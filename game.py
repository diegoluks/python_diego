from random import randint
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input("Qual a sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!!!")
print("-=" * 12)
print("O computador jogou {}".format(itens[computador]))
print("O jogador jogou {}".format(itens[jogador]))
print("-=" * 12)
if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print("\033[33mEMPATE\033[m")
        print("-=" * 12)
    elif jogador == 1:
        print("\033[32mJOGADOR VENCE\033[m")
        print("-=" * 12)
    elif jogador == 2:
        print("\033[31mCOMPUTADOR VENCE\033[m")
        print("-=" * 12)
    else:
        print("\033[36mJOGADA INVÁLIDA!\033[m")
        print("-=" * 12)
elif computador == 1: # Computador jogou PAPEL
    if jogador == 0:
        print("\033[31mCOMPUTADOR VENCE\033[m")
        print("-=" * 12)
    elif jogador == 1:
        print("\033[33mEMPATE\033[m")
        print("-=" * 12)
    elif jogador == 2:
        print("\033[32mJOGADOR VENCE\033[m")
        print("-=" * 12)
    else:
        print("\033[36mJOGADA INVÁLIDA!\033[m")
        print("-=" * 12)
elif computador == 2: # Computador jogou TESOURA
    if jogador == 0:
        print("\033[32mJOGADOR VENCE\033[m")
        print("-=" * 12)
    elif jogador == 1:
        print("\033[31mCOMPUTADOR VENCE\033[m")
        print("-=" * 12)
    elif jogador == 2:
        print("\033[33mEMPATE\033[m")
        print("-=" * 12)
    else:
        print("\033[36mJOGADA INVÁLIDA!\033[m")
        print("-=" * 12)

