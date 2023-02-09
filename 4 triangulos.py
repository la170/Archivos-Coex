v, r, e= 0,0,0
for i in range(1,5):
    print(f'Triangulo numero {i}')
    a = float(input('Ingrese el lado a de su triandulo: '))
    if a != 0:
            print('vuelva y ingrese el numero')
            b= float(input('Ingrese el lado b de su triandulo: '))
            if b!= 0:
                c= float(input('Ingrese el lado c de su triandulo: '))
                if c!= 0:
                    if a == b == c:
                        print('Triangulo equilatero')
                        v+=1
                    if a == b != c:
                        print('Triangulo isosceles')
                        e += 1
                    if a != b != c:
                        print('Triangulo escaleno')
                        r += 1
                    print(f'Cantidad de triangulos equilateros: {v}')
                    print(f'Cantidad de triangulos isosceles: {e}')
                    print(f'Cantidad de triangulos escaleno: {r}')
                    if v<e and e>r:
                        print(f'hay en menor cantidad el triangulo equilatero, con una repiticion de {v} veces')
                    if e<v and v>r:
                        print(f'hay en menor cantidad el triangulo  isosceles, con una repiticion de {e} veces')
                    if r<v and v>e:
                        print(f'hay en menor cantidad el triangulo escaleno, con una repiticion de {r} veces')
