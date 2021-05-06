

opcion = input('¡Bienvenido a Bella Napoli! \nComentanos quieres una pizza vegetariana (Si: S o No: N) ')

if opcion.lower() == 's':
    print('Los ingredientes disponibles son: \nPimiento \nTofu')
else: 
     print('Los ingredientes disponibles son: \nPeperoni \nJamon \nSalmon')

ingrediente = input('¿Que ingrediente deseas? ')

if ingrediente.lower() == 'pimiento' or ingrediente.lower() == 'tofu':
    print(f'Tu pizza es vegetariana!!! \nLos ingredientes son: \nMozzarella \nTomate \n{ingrediente}')
elif ingrediente.lower() == 'peperoni' or ingrediente.lower() == 'jamon' or ingrediente.lower() == 'salmon': 
     print(f'Tu pizza no es vegetariana \nLos ingredientes son: \nMozzarella \nTomate \n{ingrediente}')
else:
    print(f'No tenemos este ingrediente')