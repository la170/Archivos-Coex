# empleado = {}
# empleados = []
# cant = int(input('Ingrese el numero de empleados: '))
# for i in range(cant):
#     empleado['empleado'] = input(f'Ingrese el nombre del empleado numero {i+1}: ')
#     empleado['antiguedad'] = int(input('¿Cuantos años lleva en la empresa? '))
#     empleado['horas'] = int(input('¿Cuantas horas trabajó en el mes? '))
#     empleado['valor'] = float(input('¿Ingrese el valor de la hora? '))
#     empleados.append(empleado)
#     empleado = {}
# for x in range(len(empleados)):
#     print(f'''--------Recibo----------
# Nombre del empleado: {empleados[x]['empleado']}
# Años que lleva en la empresa: {empleados[x]['antiguedad']}
# Horas que trabajó en el mes: {empleados[x]['horas']}
# El valor de la hora: {empleados[x]['valor']}
# Total a cobrar en bruto: {empleados[x]['hora']*empleados[x]['valor']}
# Total del descuento: {(empleados[x]['hora']*empleados[x]['valor'])*0.13}
# Valor neto a cobrar: {((empleados[x]['hora']*empleados[x]['valor'])*0.13)}
# ''')


# alumno = {}
# alumnos, f = [],[]
# cant = int(input('¿Cúantos alumnos son? '))
# print('''----------Menu----------
# 1. Alumnos que aprobaron
# 2. Alumnos que habilitan en diciembre
# 3. Alumnos que habilitan el examen en marzo
# 4. Alumnos con el mejor promedio''')
# opcion = int(input('¿Que opcion desea utilizar?'))
# for i in range(cant):
#     alumno['código'] = input('Ingrese el código del estudiante: ')
#     alumno['nombre'] = input('¿Cúal es el nombre del estudiante? ')
#     alumno['promedio'] = float(input('¿Cual es el promedio del estudiante?'))
#     alumnos.append(alumno)
#     alumno = {}
# match opcion:
#     case 1:
#         for x in range(cant):
#             if alumnos[x]['promedio']>=7:
#                 print(f'''---------Alumnos que aprobaron-------------
#                 Codigo: {alumnos[x]['código']}
#                 Nombre: {alumnos[x]['nombre']}
#                 Promedio: {alumnos[x]['promedio']}
#                 ''')
#             else:
#                 continue
#     case 2:
#         for x in range(cant):
#             if alumnos[x]['promedio']<7 and alumnos[x]['promedio'] >=4:
#                 print(f'''---------Alumnos que aprobaron-------------
#                 Codigo: {alumnos[x]['código']}
#                 Nombre: {alumnos[x]['nombre']}
#                 Promedio: {alumnos[x]['promedio']}
#                 ''')
#             else:
#                 continue
#     case 3:
#         for x in range(cant):
#             if alumnos[x]['promedio'] <4:
#                 print(f'''---------Alumnos que aprobaron-------------
#                 Codigo: {alumnos[x]['código']}
#                 Nombre: {alumnos[x]['nombre']}
#                 Promedio: {alumnos[x]['promedio']}
#                 ''')
#             else:
#                 continue
#     case 4:
#         for x in range(cant):
#             if alumnos[x]['promedio']>=7:
#                 f.append(alumnos[x]['promedio'])
#                 if max([f]):
#                     print(f'''---------Alumnos que aprobaron-------------
#                 Codigo: {alumnos[x]['código']}
#                 Nombre: {alumnos[x]['nombre']}
#                 Promedio: {alumnos[x]['promedio']}
#                 ''')
#             else:
#                 continue


alumno = {}
alumnos, c = [],[]
cant = int(input('¿Cúantos alumnos son? '))
print('''----------Menu----------
1. Definir cantidad de estudiantes
2. Resgistrar datos estudiantes
3. Mostrar listado de estudiantes
4. Registar notas estudiantes
5. Imprimir notas estudiantes
6. Acerca del autor
7. Salir
''')
opcion = int(input('¿Que opcion desea utilizar?'))
for i in range(cant):
    alumno['código'] = input('Ingrese el código del estudiante: ')
    alumno['nombre'] = input('¿Cúal es el nombre del estudiante? ')
    alumno['promedio'] = float(input('¿Cual es el promedio del estudiante?'))
    alumnos.append(alumno)
    alumno = {}
match opcion:
    case 1:
        cant = int(input('¿Cúantos alumnos son? '))
    case 2:
        for i in range(cant-1):
            alumno['nombre'] = input('¿Cúal es el nombre del estudiante? ')
            c=int(input('Ingrese su codigo: '))
            for j in range(c):
                while c != alumno[j]['codigo']:
                    print('codigo repetido vuelva a intentar')
                else:
                    alumno['codigo'] = c
            alumno['nivel'] = input('Ingrese el nivel (Beginner, junior, senior): ')
            alumnos.append(alumno)
            alumno = {}
    case 3:
        print(alumnos)
