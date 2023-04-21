altura = float(input("Altura da parede: "))
largura = float(input("Largura da parede: "))
área = largura * altura
print("Sua parede tem a dimensão de {}x{} e sua área é de {}m².".format(altura, largura, área))
tinta = área / 2
print("Para pintar essa parede, será necessário {}L de tinta.".format(tinta))
