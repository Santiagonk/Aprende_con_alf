

def mean(lista):
    suma = 0
    for i in lista:
        suma +=i
    return suma/len(lista)

def std(lista):
    suma = 0
    for i in lista:
        suma += (i-mean(lista))**2
    return (suma/len(lista))**0.5    

def seleccionados(lista, desviacion, media):
    atipicos = []
    for i in lista:
        puntuacion = (i - media) / desviacion
        if puntuacion < -3 or puntuacion > 3:
            atipicos.append(i)
    return atipicos


def main():
    datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000]
    desviacion = std(datos)
    media = mean(datos)
    print(seleccionados(datos, desviacion, media))
    


if __name__ == "__main__":
    main()