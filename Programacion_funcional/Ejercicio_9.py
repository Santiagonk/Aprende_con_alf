
def norma(lista):
    suma = 0
    for i in lista:
        suma += i**2
    return suma**0.5

def main():
    a = [3, 4]
    print(norma(a))
    b = [1, 2, 3]
    print(norma(b))


if __name__ == "__main__":
    main()