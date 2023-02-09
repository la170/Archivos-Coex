
estudiantes=[]
notas=[]
salir=False
while salir==False:
    menu=int(input('''1. Ingresar 5 estudiantes
2. Ingresar nota de cada estudiante
3. Mostrar mayor nota y de que estudiante es 
4. Mostrar estudiantes y notas
5. Salir '''))
match menu:
    case 1:
        for i in range(5):
            estudiantes.append(input(f'Ingrese el nombre del {i+1} estudiante'))
    case 2:
        for i in range(5):
            notas.append(float(input(f'Ingrese la nota del {i+1} estudiante:')))
    case 3:
        mayor=max(notas)
        for i in range(5):
            if estudiantes[i]==mayor:
                print(f'Estudiante {estudiantes[i]}:{notas[i]}')
    case 4:
        for i in range(5):
            print(f'')