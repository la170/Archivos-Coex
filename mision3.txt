salir = False
estudiante = {}
estudiantes = []
f = []
nota,nota1,nota2,nota3 = [],[],[],[]
x = False
while salir == False:
    opcion = int(input('''-------------Menú-------------
    1. Cantidad de estudiantes
    2. Registra datos de los talentos
    3. Registrar nota de Misión 1
    4. Registrar nota de Misión 2
    5. Registra nota de Misión 3
    6. Registra prueba de nivel final
    7. Mostrar nombre y nota del talento con la mejor nota en la Misión 1
    8. Mostrar nombre y nota del talento con la mejor nota en la Misión 2
    9. Mostrar nombre y nota del talento con la mejor nota en la Misión 3
    10. Mostrar nombre y el promedio de cada talento 
    11. Mostrar código, nombre, nota misión 1, nota misión 2, nota misión 3, y prueba final
    12. nombre de los talentos que desarrollaron el ejercicio
    13. Salir
    '''))
    match opcion:
        case 1:
            x = True
            cant = int(input('Ingrese cantidad de estudiantes'))
        case 2: 
            while x == True:
                for i in range(cant):
                    estudiante['nombre'] = input('Ingrese el nombre del estudiante: ')
                    estudiante['codigo'] = input('Ingrese el codigo del estudiante: ')
                    estudiantes.append(estudiante)
                    estudiante = {}
                break
            else: 
                print('Primero tiene que realizar el punto 1')
        case 3: 
            for i in range(cant):
                nota.append(float(input(f'Ingrese nota de la Misión 1 para {estudiantes[i]["nombre"]}: ')))
        case 4: 
            for i in range(cant):
                nota1.append(float(input(f'Ingrese nota de la Misión 2 para {estudiantes[i]["nombre"]}: ')))
        case 5:
            for i in range(cant):
                nota2.append(float(input(f'Ingrese nota de la Misión 3 para {estudiantes[i]["nombre"]}: ')))
        case 6: 
            for i in range(cant):
                nota3.append(float(input(f'Ingrese nota de prueba de nivel final para {estudiantes[i]["nombre"]}: ')))
        case 7:
            print(f'Nombre del estudiante {i}: {estudiantes[i]["nombre"]}\nNota más alta del la misión 1: {max(nota)}')
        case 8:
                print(f'Nombre del estudiante {i}: {estudiantes[i]["nombre"]}\nNota más alta de la misión 2: {max(nota1)}')
        case 9:
                print(f'Nombre del estudiante {i}: {estudiantes[i]["nombre"]}\nNota más alta de la misión 3: {max(nota1)}')
        case 10:
            for w in range(len(nota)):
                print(f'Nombre del estudiante {w+1}: {estudiantes[i-1]["nombre"]}\nSu promedio es: {nota[w]+nota1[w]+nota2[w]+nota3[w]/4}')
        case 11:
            print(f'Codigo: {estudiantes[i]["codigo"]}\nNombre: {estudiantes[i-1]["nombre"]}\nNota misión 1: {nota[i]}\nNota misión 2: {nota1[i]}\nNota misión 3: {nota2[i]}\nNota prueba final: {nota[i]}')
        
        case 12:
            print('Lady Katherine Quintero López')

        case 13:
            salir = True
