lista=[]
cont=1
lista1=[]
lista2=[]
m=0
z=0
for i in range(4):
    lista.append([])
    for j in range(6):
        lista[i].append(cont)
        cont+=1
print(lista)
for x in range(len(lista)):
    for y in range(len(lista[x])):
        m = m + lista[x][y]
    lista1.append(m)
    m=0
print(lista1)
for w in range(len(lista[0])):
    for q in range(len(lista)):
        z= z + lista[q][w]
    lista2.append(z)
    z=0
print(lista2)
