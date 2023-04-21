m = float(input("Digite um valor em metros: "))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print("A medida de {}m corresponde a {:.3f}km".format(m, km))
print("A medida de {}m corresponde a {:.2f}hm".format(m, hm))
print("A medida de {}m corresponde a {:.1f}dam".format(m, dam))
print("A medida de {}m corresponde a {:.1f}dm".format(m, dm))
print("A medida de {}m corresponde a {}cm".format(m, cm))
print("A medida de {}m corresponde a {}mm".format(m, mm))