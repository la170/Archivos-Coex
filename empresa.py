tiempo= float(input('¿cuanto es el tiempo de servicio?'))
sueldo= float(input('¿cual es su sueldo?'))
civil= int(input('¿cual es su estado civil?\n marque sengun corresponda:\n 1. soltero 2.casado'))
if tiempo>=5 and civil=1:
    porcentaje=2
    elif tiempo>=6 and tiempo<=10 and civil=1:
        porcentaje=
    elif tiempo>=10 and civil=1:
    porcentaje= 10
    elif tiempo<=5 and civil=2:
        porcentaje=5
    elif tiempo>=6 and tiempo<=10 and civil=2:
        porcentaje=10
    elif tiempo>=10 and civil=2:
        porcentaje=15
print(f'el salario tiene valor de {(sueldo*porcentaje)+sueldo}')