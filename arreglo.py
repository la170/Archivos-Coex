l=[1,0,4,8,5,7,6,8,7,5,6,4,3,1,9,2]
salir=False
while salir==False:
    menu=int(input('''----------Menu-----------
    1. Ingrese que numero desea buscar
    2. Mostrar posicion'''))
    match menu:
        case 1:
            numero=int(input('Ingrese el numero que desea buscar: '))
        case 2:
            if numero in l:
                x=l.count(numero)
                if x==1:
                    print(f'esta en esta posicion: {l.index((numero))+1}')
                elif x>1:
                    for i in :
                        print(f'esta en esta posicion: {l.index((numero))+1}')
