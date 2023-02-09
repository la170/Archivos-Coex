opcion=0
flag1,flag2,flag4=False,False,False
acumulador=0
while opcion!=6:
    opcion=int(input('''
    Digita una opcion: 
    1. Ingrese el nombre del estudiante
    2. Ingrese las noptas del estudiante
    3. Mostrar la nota definitiva del estudiante
    4. Mostrar si el estidiante aprueba o no la materia
    5.Mostrar el nombre del estudiante, la nota definitiva y si aprobó o no la materia
    6. salir
    '''))
    match opcion:
        case 1:
            nombre=input('Digita el nombre del estudiante: ')
            flag1=True
        case 2:
            if flag1==True:
                for i in range(5):
                    nota=-1
                    while nota<0 or nota>5:
                        nota=float(input(f'Digita la nota: {i+1}'))
                    acumulador+=nota
                definitiva=acumulador/5
                flag2=True
            else: 
                print('primero debes hacer el paso 1')
        case 3:
            if flag1== True and flag2==True:
                print(f'su nota definitiva es: {definitiva}')
            else:
                print('primero debes hacer el paso 1 y 2') 
        case 4:
            if flag1== True and flag2==True:
                if definitiva>=3.5:
                    print('Aprobó')
                    estado= 'Aprobó'
                else:
                    print('Reprobó')
                    estado= 'Reprobó'
                flag4=True
            else:
                print('primero debes hacer el paso 1, 2, 3') 
        case 5:
            if flag1== True and flag2==True and flag4==True:
                print(f'Nombre {nombre} \nDefinitiva: {definitiva} \n{estado} la materia') 
        case 6:
            break
        case otro:
            print('Opcion invalida')

