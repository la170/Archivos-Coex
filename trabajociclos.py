# print('1. Sumar una cantidad N números MAYORES a 0 utilizando MIENTRAS.')
# num=1
# sum=0
# print('Si desea detener el programa ingrese 0')
# while num!=0:
#     num=float(input("Ingresa un numero: "))
#     if num>0:
#         sum+=num
#         print(f'El resultado de la suma es: {sum}\n')
#     else:
#         print('ingrese un numero mayor que 0\n') 
# #
# print('2. Imprimir números aleatorios en el rango de 0 a 10 mientras el número no sea igual a cero.')
# import random
# nume=1
# while nume!=0:
#     nume=random.randint(0,10)
#     print(nume)
# #
# print('3. Imprimir 20 números aleatorios en el rango de 1 a 1000.')
# import random
# for x in range(20): 
#     print (random.randint(1,1001))
    
# print('4. Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número.')
# ent=1
# while ent>0:
#     ent= int(input("Ingresa un número entero positivo: "))
#     if ent>0:
#         print(f'los numero impares entre 1 y {ent} son: ')
#         for j in range(1,ent+1):
#                     if j%2==1:
#                         print(j,'- ',end='')
#         break
# print('5. Una persona debe realizar un muestreo con 20 personas para determinar el promedio de peso de los niños, jóvenes, adultos y viejos que existen en su zona habitacional.')
# n,j,a,v,c,c1,c2,c3=0,0,0,0,0,0,0,0
# for i in range(1,20+1):
#     e=int(input('Ingrese su edad'))
#     p=float(input('Ingrese su peso'))
#     if e>=0 and e<=12:
#         c+=1
#         n+=p
#     elif e>=13 and e<=29:
#         c1+=1
#         j+=p
#     elif e>=30 and e<=59:
#         c2+=1
#         a+=p
#     elif e>=60:
#         c3+=1
#         v+=p
# if c>0:
#     print(f'el promedio de los niños es {n/c}')
# if c1>0:
#     print(f'el promedio de los jóvenes es {j/c1}')
# if c2>0:
#     print(f'el promedio de los adultos es {a/c2}')
# if c3>0:
#     print(f'el promedio de los viejos es {v/c3}')

# print('6. Diseñen un algoritmo que imprima la siguiente secuencia:')
# # for i in range(1,6):
# #     for j in range(1,5):
# #         print(f'1.{i}.{j} - ',end='')
# #     print(' ')
# print('7. Un Zoólogo pretende determinar el porcentaje de animales que hay en las siguientes tres categorías de edades: de 0 a 1 año, de más de 1 año y menos de 3 y de 3 o más años. El zoológico todavía no está seguro del animal que va a estudiar. Si se decide por elefantes solo tomara una muestra de 20 de ellos; si se decide por las jirafas, tomara 15 muestras, y si son chimpancés tomara 40.')
# h,ec,e,e1,j1,jc,hj,ch,ch1,ch2,ch3=0,0,0,0,0,0,0,0,0,0,0
# e=int(input('¿Cuantos elefantes hay? '))
# while ec<e:
#     e1=int(input('¿Que edad tiene?'))
#     m=str(input('Si su cantidad esta en dias ingrese 1,'))
#     ec+=1
#     h+=e1
# j=int(input('¿Cuantos jirafas hay? '))
# while jc<j:
#     j1=int(input('¿Que edad tiene?'))
#     jc+=1
#     hj+=j1
# ch=int(input('¿Cuantos chimpancés hay? '))
# while ch2<ch:
#     ch1=int(input('¿Que edad tiene?'))
#     ch2+=1
#     ch3+=ch1
e=input('Ingrese el nombre del estudiante')
print(e)