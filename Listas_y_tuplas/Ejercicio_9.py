palabra = input('Ingrese una palabra: ')
longitud = len(palabra)
vocales = ['a','e','i','o','u']
for vocal in vocales:
    times = 0
    for letra in palabra:
        if letra == vocal:
            times += 1
    print(f'La vocal {vocal} aparece {times} en la palabra')
    
