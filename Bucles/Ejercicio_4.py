def main():
    num = int(input('Ingrese un numero entero: '))
    numeros = []
    for i in range(num):
        
        numeros.append(i)
        
    numeros.append(num)

    numeros.sort(reverse=True)

    print(numeros)


if __name__ == "__main__":
    main()