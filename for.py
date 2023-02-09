y=3
for i in range(1,4):
    x= int(input('ingrese su clave '))
    if x==123456:
        print('Bienvenido')
        break
    elif x!=123456:
        y-=1
        print(f'Va {i} intentos, Le quedan {y}')
        print('ingrese bien su contraseña')
else:
        print('Se acabaron los intentos')