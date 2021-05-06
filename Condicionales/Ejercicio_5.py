

edad = int(input('Ingrese su edad: '))
ingresos = float(input('Ingrese sus ingresos: '))

if edad >= 16 and ingresos >= 1000:
    print('Usted puede tributar.')
else:
    print('Usted no puede tributar.')