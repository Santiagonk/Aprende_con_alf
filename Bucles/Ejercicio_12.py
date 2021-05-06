word = input('Introduce una palabra: ')
letra = input('Introduce una letra: ')
conteo = 0
for i in range(len(word)-1, -1, -1):
    if word[i].lower() == letra:
        conteo += 1
    else:
        pass
print(f'{word} tiene {conteo} veces la letra {letra}')