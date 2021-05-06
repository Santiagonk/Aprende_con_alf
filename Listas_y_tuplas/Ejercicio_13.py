num = int(input('Ingrese el numero de elementos de la muestra: '))
muestra = []
varianzas = 0
suma = 0
for i in range(num):
    numero = float(input('Ingrese un numero: '))
    suma += numero
    muestra.append(numero)

media = suma / num

for i in range(num):
    varianzas += (muestra[i]-media)**2

varianza = varianzas / num
desviacion_estandar = varianza**0.5

print(f'la media es: {media} \nla desviacion estandar es: {desviacion_estandar}')