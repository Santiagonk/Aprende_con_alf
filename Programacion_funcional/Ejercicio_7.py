def Notas_por_clase(diccionario):
    Grade = {}
    score = 0
    for clave in diccionario.keys():
        clavemin = clave
        clave = clave.upper()
        Grade[clave] = grade(diccionario[clavemin]) 
    return Grade

def grade(score):
    '''
    Función que devuelve la calificación correspondiente a una nota.
    Parámetros:
        score: Es un valor real entre 0 y 10.
    Devuelve:
        La calificación correspondiente a la nota score.
    '''
    if score < 5:
        return 'SS'
    elif score < 7:
        return 'AP'
    elif score < 9:
        return 'NT'
    elif score < 10:
        return 'SB'
    else:
        return 'MH'


def main():
    a = {'Matemáticas':6.5, 'Física':5, 'Química':3.4, 'Economía':8.2, 'Historia':9.7, 'Programación':10}
    print(f'diccionario 1: {a}')
    b = Notas_por_clase(a)
    print(f'diccionario 2: {b}')

if __name__ == "__main__":
    main()