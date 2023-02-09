user=['pablo','pepito','stif']
key=['12345','qwerty123','password']
for i in reversed(range(3)):
    user1=input('Ingrese su usuario: ').lower()
    key1=input('Ingrese su contraseña: ')
    if user1 in user and key1 in key:
        print('Bienvenido', user1)
        break
    else:
        print('Usuario o contraseña son incorrectos, le queda',(i), 'oportunidades')
