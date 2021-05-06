persona = {}
mas = 'Sí'
while mas == 'Sí':
    llave = input('¿Qué dato quieres introducir? ')
    valor = input(llave + ': ')
    persona[llave] = valor
    print(persona)
    mas = input('¿Quieres añadir más información (Sí/No)? ')

