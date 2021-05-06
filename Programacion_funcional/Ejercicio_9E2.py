def module(v):
    '''
    Función que calcula el módulo de un vector.
    Parámetros:
        v: Una tupla de números reales.
    Devuelve:
        El módulo del vector v.
    '''
    return sum([x ** 2 for x in v]) ** 0.5

print(module((3, 4)))
print(module((1, 2, 3)))