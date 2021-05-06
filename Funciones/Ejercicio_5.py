from math import pi
def Area_circulo(radio):
    """Función que calcula el area de un circulo
    Parámetros:
    radio: El radio del circulo.
    Devuelve el area del circulo"""   
    return round(2*pi*radio**2,2)

def Volumen_cilindro(radio, altura):
    """Función que calcula el volumen de un cilindro
    Parámetros:
    radio: El radio del cilindro
    altura: La altura del cilindro
    Devuelve el volumen del cilindro"""   
    return round(Area_circulo(radio)*altura,2)

if __name__ == "__main__":
    print(Area_circulo(2))
    print(Volumen_cilindro(3,5))
