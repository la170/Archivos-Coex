cant=int(input('Ingrese la cantidad de estudiantes: '))
tEstudiantes=[]
for i in range(cant):
    tEstudiantes={'nom':(input('Ingrese el nombre del estudiante: ', 'gen:'))}
    gen=input('Ingrese el genero del estudiante').lower()
    while gen == 'f' and gen == 'm':
        gen.append(tEstudiantes[gen])
    print(tEstudiantes)
