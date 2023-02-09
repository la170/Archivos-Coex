a=[]
salir=False
case1=True
case2=False
case3=False
case4=False
while salir==False:
    menu=int(input('''1. Ingresa el nombre de los animales
2. Muestra su orden alfabéticamente
3. Ingresa un numero del 1 al 10 para ver cuales animales se encuentran entre el numero dicho y el final del la lista
4. Verifica si el nombre del animal esta en la lista
5. Salir
Ingrese la opcion: '''))
    match menu:
        case 1:
            if case1==True:
                for i in range(1,11):
                    a.append(input(f'Ingrese el nombre del {i} animal '))
        case 2:
            if case1==True and case2==True:
                a.sort(reverse=False)
                print(a)
            print('Tiene que primero realizar el paso 1')
        case 3:
            if case1==True and case2==True:
                num=int(input('Ingrese un numero entre 1 y 10: '))
                if num>=1 and num<=10:
                    print(f'''entre el animal {a[num]} y el final se encuentran los siguientes animales: 
                    {a[num-1:]}''')
            print('Tiene que primero realizar el paso 1 y 2')
        case 4:
            if case1==True and case2==True and case3==True:
                d=input('Digite el nombre de un animal: ')
                if d in a:
                    print(f'El animal {d} esta en la lista')
                else:
                    print('no esta en la lista')
            print('Tiene que primero realizar el paso 1, 2 y 3')
        case 5:
            salir=True