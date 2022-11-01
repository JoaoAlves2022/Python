def VerificaPrimo(x):
    i = 0
    for count in range(2, x):
        if (x % count == 0):
            i += 1
    if (i == 0):
        return True
    else:
        return False

j = int(input("insira um numero de 1 a 100 para verificação: "))
if 0 < j <= 100:
    IsPrimo = VerificaPrimo
    if IsPrimo:
        print("É primo")
    else:
        print("Não é primo")
