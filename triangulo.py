r1= float(input('primeiro lado: '))
r2 = float(input('segundo lado: '))
r3 = float(input('terceiro lado: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Forma triangulo')
else:
   print('não forma')
   