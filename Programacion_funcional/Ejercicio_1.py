

def desc(precio, descuento):
    return precio*(1-descuento/100)

def iva(precio):
    return precio*1.19

def precio_total(precio, descuento, cantidad):
    total = desc(precio, descuento)
    return total*cantidad

def main():
    mas = 'si'
    diccionario = {}
    lista = []
    while mas == 'si':
        producto = input('Introduzca el nombre del producto ')
        precio = float(input('Precio del producto: '))
        descuento = int(input('Descuento del producto: '))
        cantidad = int(input('Numero de elementos: '))        
        total=precio_total(precio, descuento, cantidad)
        lista.append(total)
        diccionario[producto] = {'Precio':precio, 'Cantidad':cantidad, 'Descuento': descuento, 'total':round(total,2)}
        mas = input('¿Quieres añadir más palabras (si/no)? ')
  
    cuenta = 0
    for value in lista:
        cuenta += value
    
    print(diccionario)
    print(f'La cuenta total es: {round(iva(cuenta),2)}')


if __name__ == "__main__":
    main()