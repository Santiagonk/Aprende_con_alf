def main():
    n = int(input('Escoje un numero del uno al 10: '))
    name_file = 'tabla-'+str(n)+'.txt'
    
    lista = 'La tabla del ' + str(n) 
    for i in range(1,11):
        lista = lista + ' \n ' + str(n) + 'X' + str(i) + '=' + str(n*i)

    f = open(name_file, 'w')
    f.write(lista) 
    f.close()

if __name__ == "__main__":
    main()