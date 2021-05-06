
nombre = input('Ingrese su nombre: ')
sexo = input('Ingrese M si es hombre y F si es mujer: ')

if sexo == 'M':
    if nombre.lower() > 'n':
        print('Usted esta en el grupo A')
    else:
        print('Usted esta en el grupo B')
elif sexo == 'F':
    if nombre.lower() < 'm':
        print('Usted esta en el grupo A')
    else:
        print('Usted esta en el grupo B')
else:
    print('Error, no ingresaste ni hombre ni mujer')
        