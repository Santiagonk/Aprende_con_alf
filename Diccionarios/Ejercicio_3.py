Frutas = {'Plátano':1.35,'Manzana':0.80,'Pera':0.85,'Naranja':0.70}

Fruta = input('Introduce una fruta: ')
Peso = float(input('Introduce la cantidad de fruta en kilos qué deseas: '))
proof = Frutas.get(Fruta,'Fruta no existe')

if type(proof)==str:
    print('No tenemos esta fruta')
else:
    print(f'El total es {proof*Peso}')
