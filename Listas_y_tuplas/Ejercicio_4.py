loteria=[]

num = int(input(f'¿Cuantos numeros tiene la loteria? '))

for i in range(num):
    lote = int(input(f'Ingresa el {i+1} de la loteria: '))
    loteria.append(lote)
loteria.sort()
print(f'Los numeros de la loteria: {loteria}')