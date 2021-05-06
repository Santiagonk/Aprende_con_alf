cesta = {}
mas = 'si'
coste = 0
while mas == 'si':
    producto = input('¿Qué producto quieres introducir? ')
    valor = float(input(producto + ': '))
    cesta[producto] = valor
    coste += valor
    mas = input('¿Quieres añadir más productos (si/no)? ')
for item in cesta:
    print(item," cuesta :",cesta[item])

print('El coste total es de:', coste)