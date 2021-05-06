diccionario = {}
mas = 'si'
while mas == 'si':
    palabra = input('Introduzca las palabras de la siguiente manera Español:Ingles ')
    palabra = palabra.split(':')
    diccionario[palabra[0]]=palabra[1]
    mas = input('¿Quieres añadir más palabras (si/no)? ')
mas = 'si'
while mas == 'si':
    traduccion = input('Introduce una palabra que quieras traducir: ')
    print("la traduccion de la palabra es: ",diccionario.get(traduccion,'No tenemos la traduccion'))
    mas = input('¿Quieres añadir más palabras (si/no)? ')





