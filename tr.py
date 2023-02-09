edad=float(input('¿Cual es su edad?'))
prof=int(input('¿Cual es su nivel de educacion? \n 1.Profesional \n 2. Especialista, managier o Doctorado \n 3. Otro fuera de ese rango')) 
match prof:
    case 1:
        if edad>=25 and edad<=35:
            print('es apto para cubrir la vacante')
    case 2:
        if edad>0:
            print('es apt para la vacante')
    case 3:
        print('no es apto para esta vacante')