r1= int(input('primeiro numero: '))
r2 = int(input('segundo numero: '))
r3 = int(input('terceiro numero: '))

menor = r1
if (r2 < menor):
    menor = r2
if (r3 < menor):
    r3 = menor
    
print('O menor numero é: ', menor)  