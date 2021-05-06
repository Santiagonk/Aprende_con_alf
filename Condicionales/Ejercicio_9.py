

edad = int(input('¿Cuál es tu edad? '))

if edad < 4:
    print('Puedes entrar gratis')
elif edad >= 4 and edad < 18:
    print('Tu entrada cuesta 5 euros')
else:
    print('Tu entrada cuesta 10 euros')