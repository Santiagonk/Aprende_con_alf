import os

def main():
    n = int(input('Escoje un numero del uno al 10: '))
    name_file = 'tabla-'+str(n)+'.txt'
    if os.path.isfile(name_file):
        f=open(name_file)
        print(f.read())
        f.close()
    else:
        print('¡el fichero', name_file,'no existe!')


if __name__ == "__main__":
    main()