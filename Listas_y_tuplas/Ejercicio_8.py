word = input('Ingrese una palabra: ')
longitud = len(word)
letras = []
letrasint = []
for i in range(longitud):
    letra = word[i]
    letras.append(letra)
for i in range(longitud, 0, -1):
    letra = word[i-1]
    letrasint.append(letra)
if letrasint == letras:
    print(f'Es un palindromo')
else:
    print(f'No es un palindromo')