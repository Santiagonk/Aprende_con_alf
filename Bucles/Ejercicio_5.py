
cantidad = float(input('Ingrese la cantidad a invertir: '))
años = int(input('Ingrese el numero de años: '))
interes = float(input('Ingrese el interes: '))

for i in range(años):
    cantidad += cantidad*(interes/100)
    print(f'La cantidad en el año {i+1} es {round(cantidad, 2)}')
