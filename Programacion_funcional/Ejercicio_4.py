import random

def funcion_taker(funcion, lista):
    '''Función que filtra los elementos de una lista que devuelven true al aplicarle una función booleana.

    Parámetros:
        - funcion: Es una función booleana (devuleve true o false)
        - lista: Es una lista con valores que se pasarán como argumentos a funcion.
    Devuelve:
        Una lista con los elementos de la lista que devuelven true al aplicarles la función booleana.
    '''
    new = []
    for i in lista:
        if funcion(i):
            new.append(i)

    return new

def booleana_2(numero):
    if numero < 4:
        return True
    else:
        return False

def booleana_1(numero):
    if numero > 4:
        return True
    else:
        return False

def par(n):
    return n % 2 == 0

def main():
  lista = [ random.randint(0,10) for i in range(100)]
  
  a = funcion_taker(booleana_1, lista)
  b = funcion_taker(booleana_2, lista)
  c = funcion_taker(par, lista)

  print (a, b, c)




if __name__ == "__main__":
    main()