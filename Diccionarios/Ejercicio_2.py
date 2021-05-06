nombre = input('¿Cuál es tu nombre? ')
edad = input('¿Cuál es tu edad? ')
direccion = input('Cuál es tu dirección? ')
telefono = input('¿Cuál es tu número de teléfono? ')
persona = {'nombre':nombre, 'edad':edad,'direccion': direccion,'telefono': telefono}
print(persona['nombre'],' tiene ',persona['edad'],' años, vive en ',persona['direccion'],' y su número de teléfono es ',persona['telefono'])