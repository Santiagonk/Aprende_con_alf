def main():
    n = int(input('Escoje un numero del 1 al 10: '))
    m = int(input('Escoje un numero del 1 al 10: '))
    name_file = 'tabla-'+str(n)+'.txt'
    try: 
        f = open(name_file, 'r')
    except FileNotFoundError:
        print('No existe el fichero con la tabla del', n)
    else:
        f = open(name_file, "r")
        i=0
        for x in f:
            if i == m:
                print(x)
            i +=1


if __name__ == "__main__":
    main()