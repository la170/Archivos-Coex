nota1= float(int(input('Ingrese el valor de la primer nota: ')))
if nota1>=0 and nota1<=5:
    nota2= float((input('Ingrese el valor de la segunda nota: ')))
    if nota2>=0 and nota2<=5:
        nota3= float((input('Ingrese el valor de la tercera nota: ')))
        if nota3>=0 and nota3<=5:
            tra1= float((input('Ingrese el valor del primer trabajo: ')))
            if tra1>=0 and tra1<=5:
                tra2= float((input('Ingrese el valor del segundo trabajo: ')))
                if tra2>=0 and tra2<=5:
                    exf= float((input('Ingrese el valor del examen final: ')))
                    if exf>=0 and exf<=5:
                        auto= float((input('Ingrese el valor de la autoevaluación: ')))
                        if auto>=0 and auto<=5:
                            hetero= float((input('Ingrese el valor de la heteroevaluación: ')))
                            if hetero>=0 and auto<=5:
                                print('Su nota es:')
                            else:
                                    print('Recuerde ingresar su nota dentro del rango 0 a 5')
                        else:
                                    print('Recuerde ingresar su nota dentro del rango 0 a 5')
                    else:
                                    print('Recuerde ingresar su nota dentro del rango 0 a 5')    
                else:
                                    print('Recuerde ingresar su nota dentro del rango 0 a 5')
            else:
                                    print('Recuerde ingresar su nota dentro del rango 0 a 5')
        else:
                                    print('Recuerde ingresar su nota dentro del rango 0 a 5')   
    else:
            print('Recuerde ingresar su nota dentro del rango 0 a 5')
else:
    print('Recuerde ingresar su nota dentro del rango 0 a 5')
x  = ((nota1+nota2+nota3)/3)*0.55
y= ((tra1+tra2)/2)*0.15
w= (exf*0.2)
a= ((auto+hetero)/2)*0.1
l= (x+y+w+a)
print(f'{l}')
if l>=0 and l<=1.9:
    print('Se encuentra en el nivel: Muy bajo')
elif l>=2 and l<=2.9:
    print('Se encuentra en el nivel: Bajo')
elif l>=3 and l<=3.9:
    print('Se encuentra en el nivel: Básico')
elif l>=4 and l<=4.6:
    print('Se encuentra en el nivel: Alto')
elif l>=4.7 and l<=5:
    print('Se encuentra en el nivel: Superior')