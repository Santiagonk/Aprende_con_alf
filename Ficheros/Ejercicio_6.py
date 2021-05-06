def consultar_telefono(f):
  f = open(f, 'r')
  lineas = f.readlines()
  lineas = [i.replace('\n','') for i in lineas]
  lineas = [i.split(',') for i in lineas]
  lineas = [list(map(str.strip, i)) for i in lineas]
# renombramos el espacio de la primera columna y primera fila con 'año'
#lineas[0][1] = 'telefono'
  lineas = {i[0]:i[1] for i in lineas}
  
  f.close
  return lineas


def anadir_telefono(f, dato):
  f = open(f, 'a')
  f.write(dato)
  f.close()

def eliminar_telefono(f, nombre, telefono):
  lineas = consultar_telefono(f)  
  lineas[nombre] = telefono 

  for word in lineas:
    if word == 'nombre':
        dato = 'nombre,telefono' 
        g = open(f, 'w')
        g.write(dato)
        g.close()
    else:
        dato = '\n'+word + ',' + str(lineas[word])
        anadir_telefono(f, dato)

def main():
  f = 'listin.txt'
  pedido = 'Que opcion desea: \n1: Para Añadir un dato\n2: Para cambiar un dato\n3: Para consultar un dato\nPor favor digite la opcion (1, 2, 3): '
  pedido = int(input(pedido))
  if pedido == 1:
      nombre = input('Ingresa el nombre de tu cliente: ')
      telefono = input('Ingresa el telefono de tu cliente: ')
      dato = '\n'+nombre+','+telefono
      anadir_telefono(f, dato)
  elif pedido == 2:
      nombre = input('Ingresa el nombre de tu cliente: ')
      telefono = input('Ingresa el nuevo telefono de tu cliente: ')
      eliminar_telefono(f, nombre, telefono)
  elif pedido == 3:
      nombre = input('Ingresa el nombre de tu cliente: ')
      lineas = consultar_telefono(f)
      print('El telefono de ',nombre,' es: ',lineas[nombre])
  else:
      print('Opcion no existente')

def run():
    mas = 1
    while mas == 1:
        import os
        f = 'listin.txt'
        if os.path.isfile(f):
            
                main()
                

        else:
            print('¡el fichero', f,'no existe!')
            print('Se crea nuevo fichero con el nombre ',f)
            dato = 'nombre,telefono' 
            g =open(f, 'w')
            g.write(dato)
            g.close()
            nombre = input('Ingresa el nombre de tu cliente: ')
            telefono = input('Ingresa el telefono de tu cliente: ')
            dato = '\n'+nombre+','+telefono
            anadir_telefono(f, dato)
        mas = int(input('¿Desea Continuar Si=1,  No =0 ? Ingrese opción:'))
if __name__ == "__main__":
    run()