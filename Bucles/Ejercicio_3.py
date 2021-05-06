def main():
    num = int(input('Ingrese un numero entero: '))
    numeros = []
    for i in range(num):
        if i % 2 != 0:
            numeros.append(i)
        else:
            pass
    if num % 2 != 0:
        numeros.append(num)
    else:
        pass
    
    print(numeros)


if __name__ == "__main__":
    main()