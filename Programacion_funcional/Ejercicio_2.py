import math

def seno(x):
    return math.sin(x)

def coseno(x):
    return math.cos(x)

def tangente(x):
    return math.tan(x)

def exponencial(x):
    return math.exp(x)

def logaritmo_nep(x):
    return math.log(x)

def tabla(opcion, lista, value):
    verdad = opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5
    if verdad:
        for i in range(value+1):
            print(f'{i} : {round(lista[i],2)}')


def main():
    mas = 'si'
    texto = """ 
    Escoja una funcion:
        1) Seno
        2) Coseno
        3) Tangente
        4) Exponencial
        5) Logaritmo neperiano
    """
    
    while mas == 'si':
        value = int(input('Introduzca un valor: '))
        opcion = int(input(texto))
        lista = []
        if opcion == 1:        
            for i in range(value+1):
                lista.append(seno(i))            
        elif opcion == 2:        
            for i in range(value+1):
                lista.append(coseno(i)) 
        elif opcion == 3:        
            for i in range(value+1):
                lista.append(tangente(i)) 
        elif opcion == 4:        
            for i in range(value+1):
                lista.append(exponencial(i)) 
        elif opcion == 5:        
            for i in range(value+1):
                lista.append(logaritmo_nep(i))
        else: 
            lista = [0]

        tabla(opcion, lista, value)
        mas = input('¿desea continuar añadir más palabras (si/no)? ')
        


if __name__ == "__main__":
    main()