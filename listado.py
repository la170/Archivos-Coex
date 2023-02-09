v=int(input('¿Cuantos números desea ingresar?'))
lista1=[]
lista2=[]
for i in range(v):
    lista1.append(input('Ingrese un valor'))
for i in range(v):
    lista2.append((input('Ingrese otro valor')))
print (lista1)
print (lista2)
for j in range(len(lista1)):
    for n in range(len(lista2)):
        if lista1[j] == lista2[n]:
            continue
        