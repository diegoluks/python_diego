n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
if n1 > n2:
    print("O \033[32mPRIMEIRO\033[m valor é maior! ")
elif n1 < n2:
    print("O \033[32mSEGUNDO\033[m valor é maior" )
elif n1 == n2:
    print("Os dois valores são \033[36mIGUAIS\033[m! ")