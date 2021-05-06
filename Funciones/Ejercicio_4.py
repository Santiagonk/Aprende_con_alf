def factura(Sin_IVA,IVA=25):
    """Función que calcula el total de una factura tras el IVA
    Parámetros:
    Sin_IVA: EL valor antes del IVA.
    IVA: El valor del IVA en porcentaje si no se ingresa nada es 25%
    Devuelve el valor de la factura"""    
    return Sin_IVA*(1 + IVA/100)
    
if __name__ == "__main__":
    print(factura(1000,10))
    print(factura(1000))
