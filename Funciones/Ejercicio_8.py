def media(X):
    """Función que calcula la media de una lista
    Parámetros:
    X: lista a la que se requiere sacar la media
    Devuelve la media"""  
    return round(sum(X) / len(X),2)
def varianza(X):
    suma = 0
    mu = media(X)
    for i in X:
        suma += (i-mu)**2
    return suma / len(X)
def desviacion_estandar(X):
    return (varianza(X))**0.5

def main(X):
    print(f'De la lista {X}')
    print(f'la media es: {media(X)}')
    print(f'la varianza es: {varianza(X)}')
    print(f'la desviacion estandar es: {desviacion_estandar(X)}')
    return

if __name__ == "__main__":
    X = [1, 2, 3, 4, 5]
    main(X)
    X = [2.3, 5.7, 6.8, 9.7, 12.1, 15.6]
    main(X)
