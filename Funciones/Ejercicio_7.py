def cuadrados(X):
    """Función que calcula la media de una lista
    Parámetros:
    X: lista a la que se requiere sacar la media
    Devuelve la media""" 
    Y = []
    y = 0
    for i in X:
        y = i**2
        Y.append(y) 
    return Y

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    print(cuadrados(x))
    x = [2.3, 5.7, 6.8, 9.7, 12.1, 15.6]
    print(cuadrados(x))